import json
import os

from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

from screens.helperPage.helperPage import helperPage

class ServiceScreen(helperPage):

    def on_pre_enter(self, *args):
        json_path = os.path.join(os.path.dirname(__file__), "serviceInstructions.json")
        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            instructions = data.get("service_instructions", [])
        except Exception as e:
            print(f"Error loading service instructions: {e}")
            instructions = []

        #self.ids.service_steps.clear_widgets()
        self.current_step = 0  # Initialize current step

        if not instructions:
            error_label = MDLabel(
                text="No service instructions available.",
                halign="center",
                theme_text_color="Error",
            )
            self.ids.service_steps.add_widget(error_label)
            return

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        # Add Carousel
        carousel = Carousel(direction='right', loop=False)
        self.ids.service_steps.add_widget(carousel)

        for idx, step in enumerate(instructions):
            print(f"Adding step {idx + 1}: {step.get('instruction')}")

            step_layout = MDBoxLayout(
                orientation="vertical",
                padding="10dp",
                spacing="10dp",
                size_hint=(1, 1)
            )

            # Enlarged image box (80% height)
            image_box = AnchorLayout(
                anchor_x="center",
                anchor_y="center",
                size_hint=(1, 0.8)
            )

            if step.get("image"):
                image_path = os.path.join(base_dir, step["image"])
                print(f"Loading image: {image_path}")

                if os.path.exists(image_path):
                    image = Image(
                        source=image_path,
                        size_hint=(None, None),
                        size=("360dp", "360dp"),
                        allow_stretch=True
                    )
                    image_box.add_widget(image)
                else:
                    print(f"Warning: Image not found at {image_path}")

            step_layout.add_widget(image_box)

            # Instruction box (20% height), centered
            instruction_box = MDBoxLayout(
                orientation="vertical",
                size_hint=(1, 0.2),
                padding="5dp",
                spacing="10dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )

            label = MDLabel(
                text=f"[size=48sp]{step.get('instruction')}[/size]",
                theme_text_color="Primary",
                halign="center",
                valign="middle",
                size_hint_y=None,
                markup=True
            )
            instruction_box.add_widget(label)

            step_layout.add_widget(instruction_box)
            carousel.add_widget(step_layout)

        print(f"Total service steps added: {len(instructions)}")
