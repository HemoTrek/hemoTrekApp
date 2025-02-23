import socket
import json
import threading
import time

HOST = '127.0.0.1'
PORT = 65432
DELIMITER = "\n"

class PersistentClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.listener_thread = None
        self.running = False

    def connect(self):
        """Establish a persistent connection to the firmware server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.running = True
        self.listener_thread = threading.Thread(target=self.listen_for_messages, daemon=True)
        self.listener_thread.start()
        print("UI: Connected to firmware.")

    def listen_for_messages(self):
        """Continuously listen for messages from the firmware server."""
        buffer = ""
        while self.running:
            try:
                data = self.socket.recv(1024)
                if not data:
                    print("UI: Connection closed by firmware.")
                    self.running = False
                    break
                buffer += data.decode()
                while DELIMITER in buffer:
                    message, buffer = buffer.split(DELIMITER, 1)
                    if message:
                        self.handle_message(json.loads(message))
            except Exception as e:
                print(f"UI: Error receiving data: {e}")
                self.running = False

    def handle_message(self, message):
        """Process an incoming message from firmware."""
        print("UI: Received message:", message)

    def send_command(self, command_data):
        """Send a JSON-formatted command to the firmware."""
        try:
            message = json.dumps(command_data) + DELIMITER
            self.socket.sendall(message.encode())
        except Exception as e:
            print(f"UI: Error sending command: {e}")

    def disconnect(self):
        self.running = False
        if self.socket:
            self.socket.close()

if __name__ == "__main__":
    client = PersistentClient(HOST, PORT)
    client.connect()

    # Example: Change firmware state to 'active'
    command = {"command": "set_state", "state": "active"}
    client.send_command(command)
    
    # Wait and then request current state
    time.sleep(1)
    command = {"command": "get_state"}
    client.send_command(command)

    # Keep the client running for demonstration (e.g., in a UI loop)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("UI: Disconnecting...")
        client.disconnect()
