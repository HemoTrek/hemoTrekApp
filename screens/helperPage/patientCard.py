from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.fitimage import FitImage
from kivy.metrics import dp

class InstructionsCard(MDCard):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        
        # Fill 90% of the parent's width, remain centered
        self.size_hint_x = 0.9
        self.pos_hint = {'center_x': 0.5}
        
        # If you want a fixed height, set size_hint_y=None and height=...
        # Or if you want it to stretch vertically, use size_hint_y=1 (or another fraction).
        self.size_hint_y = None
        self.height = dp(300)

        self.orientation = "vertical"
        self.radius = [12]  # Rounded corners
        self.padding = dp(8)
        self.spacing = dp(8)

        # Top row: instruction text + switch
        top_row = MDBoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=dp(48),
            spacing=dp(8),
        )

        # Instruction label
        self.instruction_label = MDLabel(
            text=name,
            halign="center",
            valign="middle",
        )

        # Add them to the top row
        top_row.add_widget(self.instruction_label)

        # Add widgets to the card
        self.add_widget(top_row)
