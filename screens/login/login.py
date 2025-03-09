from kivy.uix.button import Button

from screens.helperPage.helperPage import helperPage
from screens.login.customButton import CustomButton

class Login(helperPage):
    def on_pre_enter(self, *args):
        pass

        # self.ids.button_area.clear_widgets()

        # my_button = CustomButton(
        #                 text="Click Me",
        #                 custom_bg_color=[0.3, 0.7, 0.4, 1],  # Optional: override default background color
        #                 custom_text_color=[1, 1, 1, 1],
        #                 custom_font_size=18,
        #                 on_press=lambda instance: print("Button pressed!")
        #                         )
        # self.ids.button_area.add_widget(my_button)
