from helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout

class SetupScreen(Screen):

    def on_pre_enter(self, *args):
        """Populate the setup instructions dynamically."""
        setup_steps = [
            "Ensure both tubes are inserted into each buckle such that the two red lines are visible from both the top and the bottom.",
            "Ensure that both buckles are securely clasped to each support.",
            "Double check that the clasps on the cylinders are secure.",
            "Ensure the sterilization container fluid is above the minimum level marking.",
            "Ensure the maximum fill line in the waste reservoir is still visible. If you cannot see the maximum line, then empty the reservoir.",
            "Place one blood sample in the wholeblood holder. Ensure the lid of the microcentrifuge tube is closed properly.",
            "Place the other sample in the designated slot within the centrifuge. Ensure the lid of the microcentrifuge tube is closed properly. Close the lid of the centrifuge.",
            "Insert a new pipette tip.",
            "Close the door securely.",
            "Double check that there are no alerts on the screen.",
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
            image = Image(source=f"icons/setupImage{index}.png", size_hint_y=None, height="150dp")
            self.ids.setup_steps.add_widget(image)
   
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