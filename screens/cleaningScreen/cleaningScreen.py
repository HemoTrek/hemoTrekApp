import json
import os

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
import sqlite3

from screens.helperPage.helperPage import helperPage
from screens.helperPage.instructionCard import InstructionsCard

class CleaningScreen(helperPage):

    def on_pre_enter(self, *args):
        json_path = os.path.join(os.path.dirname(__file__), "cleaningInstuctions.json")
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            instructions = data.get("cleaning_instructions", [])
        except Exception as e:
            print(f"Error loading cleaning instructions: {e}")
            instructions = []

        self.ids.setup_steps.clear_widgets()

        for step in instructions:
            card = InstructionsCard(
                instruction_text=step.get("instruction", "No instruction provided"),
                image_source=step.get("image", "")
            )
            self.ids.setup_steps.add_widget(card)

        # Connect to the database
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        
        # Fetch the latest usagesSinceLastService value
        c.execute("SELECT usagesSinceLastService FROM deviceService ORDER BY serviceID DESC LIMIT 1")
        usages_since_service = c.fetchone()
        conn.close()

        # Ensure a value was retrieved
        if usages_since_service:
            usages_since_service = usages_since_service[0]  # Extract integer value
        else:
            usages_since_service = 0  # Default value if no entry exists

        self.ids.runs_since_last_service.text = f"Runs Since Last Service: {usages_since_service}"

        # Check if "COMPLETE" button exists
        complete_button = self.ids.get("complete_button")
        if complete_button:
            if usages_since_service >= 5:
                # Remove button if count is 5 or more
                parent_layout = complete_button.parent
                if parent_layout:
                    parent_layout.remove_widget(complete_button)
            else:
                # Ensure the button is visible if usagesSinceLastService < 5
                complete_button.opacity = 1
                complete_button.disabled = False