from screens.helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen

class SelectTestType(helperPage):
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.ids.welcome_label.text = f"Welcome {app.username}!\nSelect Test Department"
        print(f"Welcome {app.username}!\nSelect Test Department")

    pass