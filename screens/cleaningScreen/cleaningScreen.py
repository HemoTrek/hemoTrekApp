import json
import os
import sqlite3
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from screens.helperPage.helperPage import helperPage

# Set fullscreen
Window.fullscreen = 'auto'

class CleaningScreen(helperPage):

    def on_pre_enter(self, *args):
        """Load cleaning instructions from JSON and add them to the carousel."""
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaningInstructions.json")
        
        # Load JSON data
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            instructions = data.get("cleaning_instructions", [])
            print(f"Loaded {len(instructions)} cleaning steps.")  # Debugging
        except Exception as e:
            print(f"Error loading cleaning instructions: {e}")
            instructions = []

        self.ids.setup_steps.clear_widgets()

        if not instructions:
            error_label = MDLabel(
                text="No cleaning instructions available.",
                halign="center",
                theme_text_color="Error",
            )
            self.ids.setup_steps.add_widget(error_label)
            return

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        for idx, step in enumerate(instructions):
            print(f"Adding step {idx + 1}: {step.get('instruction')}")

            step_layout = MDBoxLayout(
                orientation="vertical",
                padding="10dp",
                spacing="10dp",
                size_hint=(1, 1)
            )

            # --------- IMAGE at the top ----------
            image_box = AnchorLayout(
                anchor_x="center",
                anchor_y="top",
                size_hint=(1, 0.6)
            )

            if step.get("image"):
                image_path = os.path.join(base_dir, step["image"])
                print(f"Loading image: {image_path}")
                
                if os.path.exists(image_path):
                    image = Image(
                        source=image_path,
                        size_hint=(None, None),
                        size=("200dp", "200dp"),
                        allow_stretch=True
                    )
                    image_box.add_widget(image)
                else:
                    print(f"Warning: Image not found at {image_path}")

            step_layout.add_widget(image_box)

            # --------- INSTRUCTION + CHECKBOX just below image ----------
            instruction_checkbox_box = MDBoxLayout(
                orientation="horizontal",
                size_hint=(1, None),
                spacing="60dp",
                padding=("10dp", "0dp")  # Removed top padding to keep it close to image
            )

            #Instruction Text
            instruction_label = MDLabel(
                text=f"Step {idx + 1}: {step.get('instruction')}",
                theme_text_color="Primary",
                halign="left",
                size_hint_x=0.75,
                valign="middle"
            )
            instruction_label.bind(size=instruction_label.setter('text_size'))  # Wrap text

            checkbox_box = MDBoxLayout(
                orientation="vertical",
                size_hint_x=0.25,
                padding="0dp",
            )

            checkbox = MDCheckbox(size_hint=(None, None), size=("40dp", "40dp"), pos_hint={"center_x": 0.5, "center_y": 0.5})
            checkbox.bind(active=lambda chk, val, i=idx: self.on_checkbox_active(chk, val, i))
            checkbox_box.add_widget(checkbox)

            instruction_checkbox_box.add_widget(instruction_label)
            instruction_checkbox_box.add_widget(checkbox_box)

            step_layout.add_widget(instruction_checkbox_box)

            # Add step layout to Carousel
            self.ids.setup_steps.add_widget(step_layout)

        print(f"Total steps added: {len(instructions)}")

        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("SELECT usagesSinceLastService FROM deviceService LIMIT 1")
        row = c.fetchone()
        conn.close()

        usages_since_service = row[0] if row else 0
        self.ids.runs_since_last_service.text = f"[size=22sp]Perform Servicing[/size]\n[size=14sp]Runs Since Last Service: {usages_since_service}[/size]"
        self.ids.complete_button.disabled = usages_since_service >= 5

    def on_checkbox_active(self, checkbox, value, slide_index):
        """Move to the next slide when checkbox is checked."""
        if value:
            next_index = slide_index + 1
            if next_index < len(self.ids.setup_steps.children):
                self.ids.setup_steps.index = next_index
                print(f"Moved to step {next_index + 1}")
            else:
                print("Last step reached!")
