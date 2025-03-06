from kivy.properties import StringProperty, BooleanProperty

from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDButton, MDIconButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

from screens.helperPage.helperPage import helperPage

import sqlite3

HOST = '127.0.0.1'  # Server address on the same machine.
PORT = 65432        # Must match the server's port.
class PatientCard(MDCard):
    '''Implements a material card.'''

class EmergencyPatients(helperPage):

    def on_enter(self):
        patientInfo = self.get_all_users()
        # Clear any existing widgets from prior loads
        self.ids.user_box.clear_widgets()
        
        for row in patientInfo:
            # Create a GridLayout with three columns that fills the card horizontally.
            content = GridLayout(
                cols=3,
                size_hint_y=None,
                height="80dp",    # adjust height as needed
                padding="4dp",
            )
            # Left column: the icon button
            content.add_widget(
                MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=("48dp", "48dp"),
                )
            )
            # Middle column: the label
            content.add_widget(
                MDLabel(
                    #text=f"Checkin Time: {row[0]}, Username: {row[1]}",
                    text=f"{row[1]}", #Displays patient name
                    halign="center",
                    valign="middle",
                )
            )
            # Right column: the Start Test button
            content.add_widget(
                MDButton(
                    MDButtonText(
                        text="Start Test",
                    ),
                    size_hint=(None, None),
                    size=("100dp", "48dp"),
                    pos_hint={"center_y": 0.5},  # Center the button vertically
                    on_press=lambda instance, patientName=row[1]: self.store_patient_and_open_setup_screen(instance, patientName),  # Pass the row (patient data)
                )
            )
            
            # Now add the card with our evenly spaced content.
            self.ids.user_box.add_widget(
                PatientCard(
                    content,
                    style="filled",
                    ripple_behavior=True,
                    # Make sure the card fills horizontally but only as tall as needed:
                    size_hint_x=1,
                    size_hint_y=None,
                    height=content.height,
                )
            )

    def get_all_users(self):
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("SELECT * FROM patientInfo;")
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
