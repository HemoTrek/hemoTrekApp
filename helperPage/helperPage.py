from kivymd.uix.screen import MDScreen

import socket

HOST = '127.0.0.1'  # Server address on the same machine.
PORT = 65432        # Must match the server's port.

class helperPage(MDScreen):

    def open_settings(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        self.manager.current = 'settings'
    
    def open_listPatients(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        self.manager.current = 'listPatients'

    def return_home(self):
        """
        Navigates back to the home screen.
        """
        self.manager.current = 'home'

    def add_patient(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        self.manager.current = 'addPatient'
    
    def return_to_patients(self):
        """
        Navigates back to the listPatients screen.
        """
        self.manager.current = 'listPatients'

    def start_test(self, *args):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("listPatientsScreen - Test Started")
        print(*args)

        self.manager.current = 'test'

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            command = "start test"
            client.sendall(command.encode())
            response = client.recv(1024)
            print("Response from firmware:", response.decode())
