from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.modules import inspector

# Import your screen classes
from homeScreen.homeScreen import HomeScreen
from testScreen.testScreen import TestScreen
from settingsScreen.settingsScreen import SettingsScreen
from listPatientsScreen.listPatientsScreen import listPatientsScreen
from addPatient.addPatient import AddPatient
from selectTestType.selectTestType import SelectTestType
from emergencyPatients.emergencyPatients import EmergencyPatients
from oncologyPatients.oncologyPatients import OncologyPatients
from cleaningScreen.cleaningScreen import CleaningScreen
from setupScreen.setupScreen import SetupScreen

import sqlite3

def init_db():
    # Read the entire SQL script into a string
    with open("schema.sql", "r") as f:
        sql_script = f.read()

    # Connect to your local database file (or memory DB if you want)
    conn = sqlite3.connect("data/patients.db")
    cursor = conn.cursor()

    # Execute the script. This runs each statement in schema.sql
    cursor.executescript(sql_script)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized from schema.sql")


class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = "username"  # Instance attribute instead of class attribute

    def build(self):
        inspector.create_inspector(Window, self)
        self.title = 'HemoTrek'
        self.icon = 'icons/Rhys.png'
        # Explicitly load the .kv files for each screen
        Builder.load_file("homeScreen/homeScreen.kv")
        Builder.load_file("testScreen/testScreen.kv")
        Builder.load_file("settingsScreen/settingsScreen.kv")
        Builder.load_file("listPatientsScreen/listPatientsScreen.kv")
        Builder.load_file("addPatient/addPatient.kv")
        Builder.load_file("selectTestType/selectTestType.kv")
        Builder.load_file("emergencyPatients/emergencyPatients.kv")
        Builder.load_file("oncologyPatients/oncologyPatients.kv")
        Builder.load_file("cleaningScreen/cleaningScreen.kv")
        Builder.load_file("setupScreen/setupScreen.kv")

        
        self.theme_cls.theme_style = "Dark"  # or "Light"
        self.theme_cls.primary_palette = "Lavenderblush"

        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(listPatientsScreen(name='listPatients'))
        sm.add_widget(AddPatient(name='addPatient'))
        sm.add_widget(SelectTestType(name='selectTestType'))
        sm.add_widget(EmergencyPatients(name='emergencyPatients'))
        sm.add_widget(OncologyPatients(name='oncologyPatients'))
        sm.add_widget(CleaningScreen(name='cleaningScreen'))
        sm.add_widget(SetupScreen(name='setupScreen'))

        return sm

if __name__ == "__main__":
    init_db()
    MyApp().run()
