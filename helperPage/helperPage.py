from kivymd.uix.screen import MDScreen
from kivy.app import App

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

    def open_test_type_screen(self):
        """
        Navigates to the emergency patient list screen.
        """
        self.manager.current = 'selectTestType'  

    def open_emergency_patients_screen(self):
        """
        Navigates to the emergency patient list screen.
        """
        self.manager.current = 'emergencyPatients'  
    
    def open_oncology_patients_screen(self):
        """
        Navigates to the emergency patient list screen.
        """
        self.manager.current = 'oncologyPatients'

    def open_setup_screen(self, *args):
        """
        Navigates to the setup instructions screen.
        """
        print("opening setup screen")
        print(*args)
        self.manager.current = 'setupScreen'
    
    def store_patient_and_open_setup_screen(self, instance, row):
        """
        Stores patient data and navigates to the setup instructions screen.
        """
        app = App.get_running_app()  # Get the current app instance
        app.patient = row  # Store selected patient's name
        print(f"Patient Selected: {app.patient}")
        self.open_setup_screen(instance)

    def open_cleaning_screen(self):
        """
        Navigates to the cleaning instructions screen.
        """
        self.manager.current = 'cleaningScreen'

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

   
#Dont touch this - it's joeys stuff
    def select_emergency(self):
        """
        Navigates to the emergency patient list screen.
        """
        self.manager.current = 'test'            
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        #     client.connect((HOST, PORT))
        #     command = "start test"
        #     client.sendall(command.encode())
        #     response = client.recv(1024)
        #     print("Response from firmware:", response.decode())
