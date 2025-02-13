from kivy.uix.screenmanager import Screen

class TestScreen(Screen):
    def return_home(self):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("Back to Home")
        self.manager.current = 'home'
