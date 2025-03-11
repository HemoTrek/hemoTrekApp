from screens.helperPage.helperPage import helperPage
from kivy.app import App
from kivy.uix.screenmanager import Screen

class TestScreen(helperPage):
    
    def on_pre_enter(self, *args):
        app = App.get_running_app()
        
        if hasattr(app, "current_patient") and app.current_patient:
            self.ids.patientName_label.text = f"Results for {app.current_patient.name}"
            print(f"Displaying Results for {app.current_patient.name}")
        else:
            self.ids.patientName_label.text = "No Patient Selected"
            print("No patient selected.")
            
    def update_wholeblood_result(self):
        self.ids.wholeblood_progress.color = (0,1,0,0)
        self.ids.wholeblood_viscosity.text = "#.## cP"
        self.ids.wholeblood_viscosity.color = (0,1,0,1)

    def update_serum_result(self):
        self.ids.serum_progress.color = (0,1,0,0)
        self.ids.serum_viscosity.text = "#.## cP"
        self.ids.serum_viscosity.color = (1,0,0,1)

    def update_HVS_result(self):
        self.ids.HVS_progress.color = (0,1,0,0)
        self.ids.HVS_evaluation.text = "Abnormal"
        self.ids.HVS_evaluation.color = (1,0,0,1)


    pass
