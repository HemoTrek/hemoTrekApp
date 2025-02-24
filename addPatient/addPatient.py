from helperPage.helperPage import helperPage

import sqlite3

class AddPatient(helperPage):

    def save_changes(self, name):
        """
        Insert a new user (patient) into the `patientInfo` table.
        """
        conn = sqlite3.connect('data/patients.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO patientInfo (name) VALUES (?)", 
            (name,)
        )
        conn.commit()
        c.close()
        conn.close()
        
        self.manager.current = 'listPatients'

