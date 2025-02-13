from kivy.uix.screenmanager import Screen

import sqlite3


class AddPatient(Screen):
    
    def return_to_patients(self):
        """Navigates back to the listPatients screen."""
        self.manager.current = 'listPatients'

    def save_changes(self, name, email):
        """
        Insert a new user (patient) into the `users` table.
        """
        conn = sqlite3.connect('data/testDB.db')
        c = conn.cursor()

        # Insert the new record
        c.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)", 
            (name, email)
        )

        # Commit the transaction so changes are saved
        conn.commit()

        # Clean up
        c.close()
        conn.close()

        print("Saving changes...")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print("Settings (user info) saved!")
        
        self.manager.current = 'listPatients'

