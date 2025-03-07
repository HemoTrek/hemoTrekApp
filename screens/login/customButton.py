from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty

class CustomButton(Button):
    # Default colors and font size to mimic a material design style.
    custom_bg_color = ListProperty([0.2, 0.6, 0.86, 1])  # A blue shade
    custom_text_color = ListProperty([1, 1, 1, 1])         # White text
    custom_font_size = NumericProperty(16)               # Default font size

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        # Remove the default background image so we can use our color.
        self.background_normal = ''
        # Apply our custom styles.
        self.background_color = self.custom_bg_color
        self.color = self.custom_text_color
        self.font_size = self.custom_font_size

        # Bind property changes if you want to update them dynamically.
        self.bind(custom_bg_color=lambda instance, value: setattr(self, 'background_color', value))
        self.bind(custom_text_color=lambda instance, value: setattr(self, 'color', value))
        self.bind(custom_font_size=lambda instance, value: setattr(self, 'font_size', value))
