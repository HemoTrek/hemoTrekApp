from screens.helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class TestScreen(helperPage):
    
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        
        if hasattr(app, "current_patient") and app.current_patient:
            self.ids.patientName_label.text = f"Results for {app.current_patient.name}"
            print(f"Displaying Results for {app.current_patient.name}")
        else:
            self.ids.patientName_label.text = "No Patient Selected"
            print("No patient selected.")
            
    def update_wholeblood_result(self, viscosity):
        self.ids.wholeblood_progress.color = (0,1,0,0)
        self.ids.wholeblood_viscosity.text = format(viscosity, ".2f") + " cP"
        self.ids.wholeblood_viscosity.color = (1,0,0,1)

    def update_serum_result(self, viscosity):
        self.ids.serum_progress.color = (0,1,0,0)
        self.ids.serum_viscosity.text = format(viscosity, ".2f") + " cP"
        self.ids.serum_viscosity.color = (1,0,0,1)

    def update_HVS_result(self, diagnosis):
        self.ids.HVS_progress.color = (0,1,0,0)
        self.ids.HVS_evaluation.text = diagnosis
        self.ids.HVS_evaluation.color = (1,0,0,1)

    def update_results(self, results):
        print(f"results: {results}")

        if(results.get('wb_Result')):
            self.update_wholeblood_result(results.get('wb_Result', 'N/A'))

        elif(results.get('sr_result')):
            self.update_serum_result(results.get('sr_result', 'N/A'))

        elif(results.get('diagnosis')):
            self.update_HVS_result(results.get('diagnosis', 'N/A'))
        
        # # Optionally adjust colors based on the values
        # whole = results.get('wholeViscosity')
        # if whole is not None:
        #     self.ids.wholeblood_viscosity.color = (1, 0, 0, 1) if whole > 5.0 else (0, 1, 0, 1)

    def on_results_received(self, results):
        """
        This method should be called when new results arrive.
        It schedules a UI update on the main thread.
        """
        Clock.schedule_once(lambda dt: self.update_results(results))

    def enable_cleaning_button(self):
        """Enable the 'Proceed to Cleaning' button when 'Results Recorded' is clicked."""
        self.ids.proceed_to_cleaning_button.disabled = False
    
    def on_pre_leave(self, *args):
        """Reset the 'Proceed to Cleaning' button to disabled when leaving the screen."""
        self.ids.proceed_to_cleaning_button.disabled = True