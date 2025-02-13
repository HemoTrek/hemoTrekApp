from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):

    def start_test(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("Test Started")
        self.manager.current = 'test'

    def open_settings(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("Open Settings")
        self.manager.current = 'settings'

    def open_listPatients(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("List Patients")
        self.manager.current = 'listPatients'