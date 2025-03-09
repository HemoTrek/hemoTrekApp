from kivy.properties import StringProperty
from screens.helperPage.helperPage import helperPage

import sqlite3

class AddPatient(helperPage):

    return_page = StringProperty("")


class AddPatient(helperPage):
    return_page = StringProperty("")
    department = StringProperty("")  # This should be set before navigating to this screen


    def save_changes(self, name, DOB, notes):
        """
        Insert a new patient into the `SeanTest` table.
        """
        try:
            conn = sqlite3.connect('data/appData.db')
            c = conn.cursor()
            c.execute(
                """
                INSERT INTO SeanTest (name, department, dateOfBirth, notes) 
                VALUES (?, ?, ?, ?)
                """,
                (name, self.department, DOB, notes)
            )
            conn.commit()
            c.close()
            conn.close()
            print("Patient added successfully!")
        except Exception as e:
            print("Error adding patient:", e)

        self.manager.current = self.return_page