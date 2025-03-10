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
            # Fallback to an empty list if the file cannot be read
            print(f"Error loading cleaning instructions: {e}")
            instructions = []

        self.ids.setup_steps.clear_widgets()

        for step in instructions:
            card = InstructionsCard(
                instruction_text=step.get("instruction", "No instruction provided"),
                image_source=step.get("image", "")
            )
            self.ids.setup_steps.add_widget(card)
    
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        
        # Fetch the latest usagesSinceLastService value
        c.execute("SELECT usagesSinceLastService FROM deviceService LIMIT 1")
        usages_since_service = c.fetchone()
        conn.close()

        self.ids.runs_since_last_service.text = f"Runs Since Last Service: {usages_since_service[0]}"
