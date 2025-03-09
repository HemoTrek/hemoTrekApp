from kivy.properties import StringProperty, BooleanProperty

from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDButton, MDIconButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

from screens.helperPage.helperPage import helperPage
from screens.helperPage.patientInfoCard import PatientInfoCard

import sqlite3

HOST = '127.0.0.1'  # Server address on the same machine.
PORT = 65432        # Must match the server's port.
class PatientCard(MDCard):
    '''Implements a material card.'''

class EmergencyPatients(helperPage):

    def on_enter(self):
        patientInfo = self.get_all_users()

        for patient in patientInfo:
            print(patient[0])

        # Prepare data for the RecycleView.
        self.ids.recycle_view.data = [
            {
                "name": str(patient[0]),
                "department": str(patient[1])
            }
            for patient in patientInfo 
        ]

    def get_all_users(self):
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("SELECT name, department FROM patientInfo where department = 'Emergency';")
        rows = c.fetchall()
        c.close()
        conn.close()
        return rows
    
    def clear_all_users(self):
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("DELETE FROM patientInfo;")
        conn.commit()
        c.close()
        conn.close()
        self.on_enter()
