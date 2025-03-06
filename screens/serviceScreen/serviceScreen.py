from screens.helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout

class ServiceScreen(Screen):

    def on_pre_enter(self, *args):
        """Populate the service instructions dynamically."""
        service_steps = [
            "Step 1: Watch out for the freaky ahh turtles",
            "Step 2: Homophobia",
            "Step 3: Profit",
            "Remove both microcentrifuge tubes",
            "Dispose of all products in their appropriate waste receptacles",
        ]

        #self.ids.service_steps.clear_widgets()

        for index, step in enumerate(service_steps, start=1):
            # Create a horizontal box for step description and checkbox
            step_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="50dp", md_bg_color = (1,1,1,1))

            # Step description (75% of width)
            step_text = MDLabel(text=step, size_hint_x=0.75, halign="left", theme_text_color="Custom", text_color=(0,0,0,1))
            step_layout.add_widget(step_text)

            # Checkbox (25% of width)
            checkbox = MDCheckbox(size_hint_x=0.25, pos_hint={"center_y": 0.5}, color_active=(0, 0, 0, 1))
            step_layout.add_widget(checkbox)

            # Add the step layout to the list
            self.ids.service_steps.add_widget(step_layout)

            # Add the corresponding image below
            image = Image(source=f"icons/serviceImage{index}.png", size_hint_y=None, height="150dp")
            self.ids.service_steps.add_widget(image)
   
    def return_home(self):
        """
        Navigates back to the home screen.
        """
        self.manager.current = 'home'

    def open_cleaning_screen(self):
        """
        Navigates to the cleaning instructions screen.
        """
        self.manager.current = 'cleaningScreen'