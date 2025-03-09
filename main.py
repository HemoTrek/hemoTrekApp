from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.modules import inspector

# Import your screen classes
from screens.login.login import Login
from screens.testScreen.testScreen import TestScreen
from screens.settingsScreen.settingsScreen import SettingsScreen
from screens.selectTestType.selectTestType import SelectTestType
from screens.emergencyPatients.emergencyPatients import EmergencyPatients
from screens.oncologyPatients.oncologyPatients import OncologyPatients
from screens.cleaningScreen.cleaningScreen import CleaningScreen
from screens.setupScreen.setupScreen import SetupScreen
from screens.serviceScreen.serviceScreen import ServiceScreen

from persistentServer import PersistentServer

import sqlite3

HOST = '127.0.0.1'
PORT = 65432

def init_db():
    # Read the entire SQL script into a string
    with open("schema/schema.sql", "r") as f:
        schema_sql_script = f.read()
    
    with open("schema/createTestPatients.sql", "r") as f:
        data_sql_script = f.read()

    # Connect to your local database file (or memory DB if you want)
    conn = sqlite3.connect("data/appData.db")
    cursor = conn.cursor()

    # Execute the script. This runs each statement in schema.sql
    cursor.executescript(schema_sql_script)
    cursor.executescript(data_sql_script)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized from schema.sql")


class MyApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = "[Username Not Entered]"  
        self.password = "[Password Not Entered]"  
        self.patient = "[No Patient Data Entered]"
        self.runsSinceLastService = 0

    def build(self):
        inspector.create_inspector(Window, self)
        self.title = 'HemoTrek'
        self.icon = 'icons/hemoTrekSmallLogo.png'

        self.theme_cls.theme_style = "Dark"  # or "Light"
        self.theme_cls.primary_palette = "Lavenderblush"
        
        # Explicitly load the .kv files for each screen
        Builder.load_file("screens/login/login.kv")
        Builder.load_file("screens/testScreen/testScreen.kv")
        Builder.load_file("screens/settingsScreen/settingsScreen.kv")
        Builder.load_file("screens/selectTestType/selectTestType.kv")
        Builder.load_file("screens/emergencyPatients/emergencyPatients.kv")
        Builder.load_file("screens/oncologyPatients/oncologyPatients.kv")
        Builder.load_file("screens/cleaningScreen/cleaningScreen.kv")
        Builder.load_file("screens/setupScreen/setupScreen.kv")
        Builder.load_file("screens/serviceScreen/serviceScreen.kv")
        

        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(Login(name='home'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SelectTestType(name='selectTestType'))
        sm.add_widget(EmergencyPatients(name='emergencyPatients'))
        sm.add_widget(OncologyPatients(name='oncologyPatients'))
        sm.add_widget(CleaningScreen(name='cleaningScreen'))
        sm.add_widget(SetupScreen(name='setupScreen'))
        sm.add_widget(ServiceScreen(name='serviceScreen'))

        return sm

if __name__ == "__main__":
    # server = PersistentServer(HOST, PORT)
    # server.start()
    
    # # Keep the server running
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     print("Shutting down server...")
    #     server.stop()

    init_db()
    MyApp().run()

