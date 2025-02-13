from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Import your screen classes
from homeScreen.homeScreen import HomeScreen
from testScreen.testScreen import TestScreen
from settingsScreen.settingsScreen import SettingsScreen
from listPatientsScreen.listPatientsScreen import listPatientsScreen
from addPatient.addPatient import AddPatient


class MyApp(MDApp):
    def build(self):
        # Explicitly load the .kv files for each screen
        Builder.load_file("homeScreen/homeScreen.kv")
        Builder.load_file("testScreen/testScreen.kv")
        Builder.load_file("settingsScreen/settingsScreen.kv")
        Builder.load_file("listPatientsScreen/listPatientsScreen.kv")
        Builder.load_file("addPatient/addPatient.kv")
        
        self.theme_cls.theme_style = "Dark"  # or "Light"
        self.theme_cls.primary_palette = "Lavenderblush"

        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(listPatientsScreen(name='listPatients'))
        sm.add_widget(AddPatient(name='addPatient'))
        return sm


if __name__ == "__main__":
    MyApp().run()
