from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.app import App
from .patientInfo import Patient
import sqlite3

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
    
    def store_patient_and_open_setup_screen(self, instance, patient):
        """
        Stores patient data and navigates to the setup instructions screen.
        """
        app = App.get_running_app()  # Get the current app instance
        app.patient = patient  # Store selected patient's name
        print(f"Patient Selected: {app.patient}")
        self.open_setup_screen(instance)

    def select_patient(self, patient_data):
        """Create a Patient object and trigger the setup instruction screen."""
        app = App.get_running_app()
        app.current_patient = Patient(name=patient_data)  # Store Patient object
        print(f"Patient selected: {app.current_patient.name}")

        # Instead of starting the test directly, open the setup instruction screen
        self.open_setup_screen()

    def open_cleaning_screen(self):
        """
        Navigates to the cleaning instructions screen.
        """
        self.manager.current = 'cleaningScreen'
    
    def open_service_screen(self):
        """
        Navigates to the service instructions screen.
        """
        self.manager.current = 'serviceScreen'

    def return_home(self):
        """
        Navigates back to the home screen.
        """
        self.manager.current = 'home'
    
    def add_patient(self):
        # Get the addPatient screen instance
        add_patient_screen = self.manager.get_screen("addPatient")
        # Store the current screen name as the return destination.
        add_patient_screen.return_page = self.manager.current
        # Switch to the addPatient screen.
        self.manager.current = "addPatient"

    
    def return_to_patients(self):
        """
        Navigates back to the listPatients screen.
        """
        self.manager.current = 'listPatients'

    def start_test(self, *args):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print(*args)

        # Get the running app instance
        app = App.get_running_app()
        print(f"Patient selected: {app.current_patient}")

        try:
            # Connect to the database
            conn = sqlite3.connect('data/appData.db')
            c = conn.cursor()
            
            # Check if a row exists
            c.execute("SELECT COUNT(*) FROM deviceService")
            row_count = c.fetchone()[0]

            if row_count > 0:
                # Increment usagesSinceLastService for the most recent row
                c.execute("""
                    UPDATE deviceService
                    SET usagesSinceLastService = usagesSinceLastService + 1
                    WHERE rowid = (SELECT MAX(rowid) FROM deviceService)
                """)
                conn.commit()

                # Fetch the updated value
                c.execute("SELECT usagesSinceLastService FROM deviceService ORDER BY rowid DESC LIMIT 1")
                updated_value = c.fetchone()[0]  # Get the incremented value

                print(f"Updated Runs Since Last Service: {updated_value}")
            else:
                updated_value = 0
                print("No existing records in deviceService.")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            updated_value = 0  # Default fallback

        finally:
            conn.close()

        # Update the UI with the new value
        if hasattr(self.ids, "setup_steps"):
            self.ids.setup_steps.clear_widgets()  # Refresh UI
            self.ids.setup_steps.add_widget(MDLabel(
                text=f"Runs Since Last Service: {updated_value}",
                halign="center",
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),
                size_hint_y=None,
                height="50dp"
            ))

        self.manager.current = 'test'


    def reset_service_counter(self):
        """Resets usagesSinceLastService to 0 in the deviceService table."""
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        
        # Update the value in the deviceService table
        c.execute("UPDATE deviceService SET usagesSinceLastService = 0")

        # Commit and close connection
        conn.commit()
        conn.close()

        print("Service usage reset to 0 successfully.")
            
        self.manager.current = 'home'


    def get_usages_since_last_service():
        """Fetches usagesSinceLastService from the deviceService table."""
        try:
            conn = sqlite3.connect('data/appData.db')
            c = conn.cursor()
            
            # Fetch the latest usagesSinceLastService value
            c.execute("SELECT usagesSinceLastService FROM deviceService LIMIT 1")
            result = c.fetchone()

            conn.close()

            # Return the fetched value, defaulting to 0 if no record exists
            return result[0] if result else 0

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return 0  # Default fallback in case of an error

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
