import json
import os

from kivy.app import App
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout

from screens.helperPage.helperPage import helperPage
from screens.helperPage.instructionCard import InstructionsCard

class SetupScreen(helperPage):

    def on_pre_enter(self, *args):

        json_path = os.path.join(os.path.dirname(__file__), "setupInstuctions.json")
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            instructions = data.get("setup_instructions", [])
        except Exception as e:
            # Fallback to an empty list if the file cannot be read
            print(f"Error loading setup instructions: {e}")
            instructions = []

        self.ids.setup_steps.clear_widgets()

        for step in instructions:
            card = InstructionsCard(
                instruction_text=step.get("instruction", "No instruction provided"),
                image_source=step.get("image", "")
            )
            self.ids.setup_steps.add_widget(card)
