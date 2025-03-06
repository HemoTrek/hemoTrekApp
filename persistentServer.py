import socket
import json
import threading

DELIMITER = "\n"

class PersistentServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.running = False

    def start(self):
        """Start the server and wait for a client to connect."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")
        self.accept_client()

    def accept_client(self):
        """Accept a single client connection."""
        self.client_socket, addr = self.server_socket.accept()
        print(f"Accepted connection from {addr}")
        self.running = True
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def listen_for_messages(self):
        """Continuously listen for messages from the connected client."""
        buffer = ""
        while self.running:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    print("Client disconnected.")
                    self.running = False
                    break
                buffer += data.decode()
                while DELIMITER in buffer:
                    message, buffer = buffer.split(DELIMITER, 1)
                    if message:
                        self.handle_message(json.loads(message))
            except Exception as e:
                print("Error receiving data:", e)
                self.running = False

    def handle_message(self, message):
        """Process an incoming message from the client."""
        print("Received message:", message)
        # Optionally, send a response back
        response = {"status": "received", "echo": message}
        self.send_message(response)

    def send_message(self, message):
        """Send a JSON-formatted message to the client."""
        try:
            message = json.dumps(message) + DELIMITER
            self.client_socket.sendall(message.encode())
        except Exception as e:
            print("Error sending message:", e)

    def stop(self):
        """Stop the server and close connections."""
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
