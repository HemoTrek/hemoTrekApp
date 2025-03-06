from screens.helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout

class CleaningScreen(Screen):

    def on_pre_enter(self, *args):
        """Populate the cleaning instructions dynamically."""
        setup_steps = [
            "Open the door",
            "Remove Capillary tubes",
            "Remove the pipette tip",
            "Remove both microcentrifuge tubes",
            "Dispose of all products in their appropriate waste receptacles",
        ]

        self.ids.setup_steps.clear_widgets()

        for index, step in enumerate(setup_steps, start=1):
            # Create a horizontal box for step description and checkbox
            step_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="50dp", md_bg_color = (1,1,1,1))

            # Step description (75% of width)
            step_text = MDLabel(text=step, size_hint_x=0.75, halign="left", theme_text_color="Custom", text_color=(0,0,0,1))
            step_layout.add_widget(step_text)

            # Checkbox (25% of width)
            checkbox = MDCheckbox(size_hint_x=0.25, pos_hint={"center_y": 0.5}, color_active=(0, 0, 0, 1))
            step_layout.add_widget(checkbox)

            # Add the step layout to the list
            self.ids.setup_steps.add_widget(step_layout)

            # Add the corresponding image below
            image = Image(source=f"icons/cleaningImage{index}.png", size_hint_y=None, height="150dp")
            self.ids.setup_steps.add_widget(image)
                # Display runsSinceLastService at the bottom
        
        app = App.get_running_app()  # Correctly retrieve the running app instance

        if hasattr(app, "runsSinceLastService"):  # Ensure the attribute exists
            self.ids.runs_since_last_service.text = f"Runs Since Last Service: {app.runsSinceLastService}"
        else:
            self.ids.runs_since_last_service.text = "Runs Since Last Service: 0"  # Fallback if attribute isn't set

    
    def return_home(self):
        """
        Navigates back to the home screen.
        """
        self.manager.current = 'home'

    def start_test(self, *args):
        """
        This method is called when the 'Start Test' button is pressed.
        """
        print("listPatientsScreen - Test Started")
        print(*args)

        self.manager.current = 'test'     

    def open_service_screen(self):
        """
        Navigates to the service instructions screen.
        """
        self.manager.current = 'serviceScreen'