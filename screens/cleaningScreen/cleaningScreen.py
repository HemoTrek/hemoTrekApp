import json
import os
import sqlite3
from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from screens.helperPage.helperPage import helperPage

class CleaningScreen(helperPage):

    def on_pre_enter(self, *args):
        """Load cleaning instructions from JSON and add them to the carousel."""
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleaningInstructions.json")  # Corrected the typo
        
        # Load JSON data
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            instructions = data.get("cleaning_instructions", [])
            print(f"Loaded {len(instructions)} cleaning steps.")  # Debugging
        except Exception as e:
            print(f"Error loading cleaning instructions: {e}")
            instructions = []

        self.ids.setup_steps.clear_widgets()  # Clear previous widgets
        self.carousel = Carousel(direction="right", loop=True, size_hint_y=1)  # Ensure the carousel takes up full available height

        if not instructions:
            error_label = MDLabel(
                text="No cleaning instructions available.",
                halign="center",
                theme_text_color="Error",
            )
            self.ids.setup_steps.add_widget(error_label)
            return  # Stop execution

        # Get the absolute path to the "hemoTrekApp" directory
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # Move up to parent directory

        for idx, step in enumerate(instructions):
            print(f"Adding step {idx + 1}: {step.get('instruction')}")  # Debugging

            # Create a layout for each step
            step_layout = MDBoxLayout(
                orientation="vertical",  # Stack elements vertically
                padding="10dp",
                spacing="10dp",
                size_hint_y=None,
                height="300dp"  # Fixed height for consistent layout
            )

            # Image container: Center the image
            image_box = MDBoxLayout(
                orientation="vertical",
                size_hint_y=0.7,  # Image takes 70% of the vertical space
                padding="10dp",
                spacing="5dp",
                pos_hint={"center_x": 0.5}  # Center the image horizontally
            )

            # Instruction image
            if step.get("image"):
                image_path = os.path.join(base_dir, step["image"])  # Ensure correct path
                print(f"Loading image: {image_path}")  # Debugging
                
                if os.path.exists(image_path):  # Check if file exists before adding
                    image = Image(
                        source=image_path,
                        size_hint=(None, None),
                        size=("200dp", "200dp"),
                        allow_stretch=True
                    )
                    image_box.add_widget(image)
                else:
                    print(f"Warning: Image not found at {image_path}")

            # Add image box to the step layout
            step_layout.add_widget(image_box)

            # Instruction and checkbox container: Horizontal layout below the image
            instruction_checkbox_box = MDBoxLayout(
                orientation="horizontal",  # Horizontal arrangement
                size_hint_y=0.3,  # Takes up 30% of the vertical space
                padding="10dp",
                spacing="10dp"
            )

            # Instruction text (left side, 3/4 of the width)
            instruction_box = MDBoxLayout(
                orientation="vertical",
                size_hint_x=0.75,  # Instruction takes 3/4 of the width
                padding="5dp",
                spacing="5dp"
            )

            # Instruction text label
            label = MDLabel(
                text=f"Step {idx + 1}: {step.get('instruction')}",
                theme_text_color="Primary",
                halign="left",
                size_hint_y=None,
                height="40dp"
            )
            instruction_box.add_widget(label)

            # Checkbox box (right side, 1/4 of the width)
            checkbox_box = MDBoxLayout(
                orientation="vertical",
                size_hint_x=0.25,  # Takes up 1/4 of the width
                padding="5dp",
                spacing="5dp",
            )

            # Checkbox for step completion (scale the checkbox to fill the space)
            checkbox = MDCheckbox(size_hint=(1, 1))  # Let the checkbox fill the container's space
            checkbox.bind(active=lambda chk, val, i=idx: self.on_checkbox_active(chk, val, i))
            checkbox_box.add_widget(checkbox)

            # Add instruction box and checkbox box to the horizontal container
            instruction_checkbox_box.add_widget(instruction_box)
            instruction_checkbox_box.add_widget(checkbox_box)

            # Add instruction and checkbox container to the step layout
            step_layout.add_widget(instruction_checkbox_box)

            # Add to carousel
            self.carousel.add_widget(step_layout)

        # Add carousel to UI
        self.ids.setup_steps.add_widget(self.carousel)
        print(f"Total steps added to carousel: {len(self.carousel.slides)}")  # Debugging

        # Fetch latest runsSinceLastService value from the database
        conn = sqlite3.connect('data/appData.db')
        c = conn.cursor()
        c.execute("SELECT usagesSinceLastService FROM deviceService LIMIT 1")
        row = c.fetchone()
        conn.close()

        usages_since_service = row[0] if row else 0  # Default to 0 if no data
        self.ids.runs_since_last_service.text = f"[size=22sp]Perform Servicing[/size][size=14sp]\nRuns Since Last Service: {usages_since_service}[/size]"
        self.ids.complete_button.disabled = usages_since_service >= 5  # Disable button if necessary

    def on_checkbox_active(self, checkbox, value, slide_index):
        """Move to the next slide in the carousel when the checkbox is checked."""
        if value:  # Checkbox was clicked
            next_index = slide_index + 1
            if next_index < len(self.carousel.slides):  # Ensure it doesn't go out of bounds
                self.carousel.index = next_index  # Move to the next slide
                print(f"Moved to step {next_index + 1}")  # Debugging
            else:
                print("Last step reached!")  # Debugging
