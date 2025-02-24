from helperPage.helperPage import helperPage

import sqlite3

class AddPatient(helperPage):

    def save_changes(self, name):
        """
        Insert a new user (patient) into the `patientInfo` table.
        """
        conn = sqlite3.connect('data/testDB.db')
        c = conn.cursor()

        # Insert the new record
        c.execute(
            "INSERT INTO patientInfo (name) VALUES (?)", 
            (name,)
        )

        # Commit the transaction so changes are saved
        conn.commit()

        # Clean up
        c.close()
        conn.close()
        
        self.manager.current = 'listPatients'

