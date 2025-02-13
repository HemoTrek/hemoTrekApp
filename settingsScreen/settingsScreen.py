from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):
    def return_home(self):
        """Navigates back to the home screen."""
        self.manager.current = 'home'

    def save_changes(self, username, dark_mode, notifications, volume):
        """
        Pretend method to 'save' settings.
        In a real app, you'd update user preferences in a file or database.
        """
        print("Saving changes...")
        print(f"Username: {username}")
        print(f"Dark Mode: {dark_mode}")
        print(f"Notifications: {notifications}")
        print(f"Volume: {volume}")
        print("Settings saved!")
