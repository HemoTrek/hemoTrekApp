from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDButton, MDIconButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

import sqlite3

class MyCard(MDCard):
    '''Implements a material card.'''

class listPatientsScreen(MDScreen):

    def start_test(self, *args):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("listPatientsScreen - Test Started")
        print(*args)

        self.manager.current = 'test'

    def open_settings(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("listPatientsScreen - Open Settings")
        self.manager.current = 'settings'

    def return_home(self):
        """Navigates back to the home screen."""
        self.manager.current = 'home'

    def add_patient(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("Add Patient")
        self.manager.current = 'addPatient'



    def on_enter(self):
        users = self.get_all_users()
        # Clear any existing widgets from prior loads
        self.ids.user_box.clear_widgets()
        
        for row in users:
            # Create a GridLayout with three columns that fills the card horizontally.
            content = GridLayout(
                cols=3,
                size_hint_y=None,
                height="60dp",    # adjust height as needed
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
                    text=f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}",
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
                    on_press=self.start_test,
                )
            )
            
            # Now add the card with our evenly spaced content.
            self.ids.user_box.add_widget(
                MyCard(
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
        import sqlite3
        conn = sqlite3.connect('data/testDB.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users;")
        rows = c.fetchall()
        c.close()
        conn.close()
        return rows

    
    def clear_all_users(self):
        conn = sqlite3.connect('data/testDB.db')
        c = conn.cursor()
        c.execute("DELETE FROM users;")
        conn.commit()
        c.close()
        conn.close()
        self.on_enter()
