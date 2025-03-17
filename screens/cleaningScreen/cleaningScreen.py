import json
import os
import sqlite3
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
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

        self.ids.cleaning_steps.clear_widgets()
        self.current_step = 0  # Initialize current step to 0

        if not instructions:
            error_label = MDLabel(
                text="No cleaning instructions available.",
                halign="center",
                theme_text_color="Error",
            )
            self.ids.cleaning_steps.add_widget(error_label)
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

            # Adjust the image box size to be larger
            image_box = AnchorLayout(
                anchor_x="center",
                anchor_y="center",
                size_hint=(1, 0.8)  # Image box will take 80% of the vertical space
            )

            if step.get("image"):
                image_path = os.path.join(base_dir, step["image"])
                print(f"Loading image: {image_path}")
                
                if os.path.exists(image_path):
                    # Increase the size of the image within the layout
                    image = Image(
                        source=image_path,
                        size_hint=(None, None),  # Make the size explicit
                        size=("360dp", "360dp"),  # Explicit size for the image
                        allow_stretch=True
                    )
                    image_box.add_widget(image)
                else:
                    print(f"Warning: Image not found at {image_path}")

            step_layout.add_widget(image_box)

            instruction_box = MDBoxLayout(
                orientation="vertical",
                size_hint=(1, 0.2),  # Instructions box will take 20% of the vertical space
                padding="5dp",
                spacing="10dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},  # Center the instruction box
            )

            label = MDLabel(
                text=f"[size=48sp]{step.get('instruction')}[/size]",
                theme_text_color="Primary",
                halign="center",  # Horizontally center the label
                valign="middle",  # Vertically center the label
                size_hint_y=None,
                markup=True
            )
            instruction_box.add_widget(label)

            step_layout.add_widget(instruction_box)
            self.ids.cleaning_steps.add_widget(step_layout)

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
        # This function is no longer used since the checkbox was removed
        pass
