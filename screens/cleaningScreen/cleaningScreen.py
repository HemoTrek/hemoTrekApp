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
from screens.helperPage.helperPage import helperPage

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
        self.carousel = Carousel(direction="right", loop=True, size_hint_y=1)

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
                size_hint_y=None,
                height="300dp"
            )

            # Image container: Center the image properly
            image_box = AnchorLayout(
                anchor_x="center",
                anchor_y="center",
                size_hint=(1, None),
                height="250dp"
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

            instruction_checkbox_box = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=0.3,
                padding="10dp",
                spacing="10dp"
            )

            instruction_box = MDBoxLayout(
                orientation="vertical",
                size_hint_x=0.75,
                padding="5dp",
                spacing="5dp"
            )

            label = MDLabel(
                text=f"Step {idx + 1}: {step.get('instruction')}",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height="40dp"
            )
            instruction_box.add_widget(label)

            checkbox_box = MDBoxLayout(
                orientation="vertical",
                size_hint_x=0.25,
                padding="5dp",
                spacing="5dp",
            )

            checkbox = MDCheckbox(size_hint=(1, 1))
            checkbox.bind(active=lambda chk, val, i=idx: self.on_checkbox_active(chk, val, i))
            checkbox_box.add_widget(checkbox)

            instruction_checkbox_box.add_widget(instruction_box)
            instruction_checkbox_box.add_widget(checkbox_box)
            step_layout.add_widget(instruction_checkbox_box)
            self.carousel.add_widget(step_layout)

        self.ids.setup_steps.add_widget(self.carousel)
        print(f"Total steps added to carousel: {len(self.carousel.slides)}")

        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("SELECT usagesSinceLastService FROM deviceService LIMIT 1")
        row = c.fetchone()
        conn.close()

        usages_since_service = row[0] if row else 0
        self.ids.runs_since_last_service.text = f"[size=22sp]Perform Servicing[/size][size=14sp]\nRuns Since Last Service: {usages_since_service}[/size]"
        self.ids.complete_button.disabled = usages_since_service >= 5

    def on_checkbox_active(self, checkbox, value, slide_index):
        """Move to the next slide in the carousel when the checkbox is checked."""
        if value:
            next_index = slide_index + 1
            if next_index < len(self.carousel.slides):
                self.carousel.index = next_index
                print(f"Moved to step {next_index + 1}")
            else:
                print("Last step reached!")
