from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.label import MDLabel, MDIcon

class PatientInfoCard(MDCard):
    name = StringProperty("")
    department = StringProperty("")
    date_of_birth = StringProperty("")
    notes = StringProperty("")
    icon = 'account'
    # on_press = ObjectProperty(lambda x: None)  # Default empty function


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Card styling.
        self.size_hint = (None, None)
        self.size = (dp(200), dp(150))
        self.elevation = 4
        self.padding = dp(10)
        self.radius = [10]
        self.orientation = "vertical"
        self.bind(on_touch_down=self.card_clicked)


        # Main vertical layout.
        self.layout = MDBoxLayout(
            orientation="vertical",
            spacing=dp(5),
            padding=(0, 0, 0, 0),
        )

        # Icon area: Wrap MDIcon in an MDAnchorLayout.
        self.icon_layout = MDAnchorLayout(
            size_hint_y=None,
            height=dp(70),  # This controls the available space for the icon.
            anchor_x="center",
            anchor_y="center"
        )
        self.icon_widget = MDIcon(
            icon=self.icon,
            size_hint=(None, None),
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1)
        )
        self.icon_layout.add_widget(self.icon_widget)
        # Bind the entire size so that changes trigger our update.
        self.icon_layout.bind(size=self._update_icon_font_size)

        # Labels for patient info.
        self.name_label = MDLabel(
            text=self.name,
            font_style="Title",
            halign="center",
            size_hint_y=None,
            height=dp(30)
        )
        self.dept_label = MDLabel(
            text=self.department,
            halign="center",
            size_hint_y=None,
            height=dp(24)
        )

        # Assemble the card.
        self.layout.add_widget(self.icon_layout)
        self.layout.add_widget(self.name_label)
        self.layout.add_widget(self.dept_label)
        self.add_widget(self.layout)

        # Bind property changes so that labels update when data changes.
        self.bind(name=lambda instance, value: setattr(self.name_label, 'text', value))
        self.bind(department=lambda instance, value: setattr(self.dept_label, 'text', value))

    def _update_icon_font_size(self, instance, size):
        # Update the icon's font_size to be 80% of the icon_layout's height.
        self.icon_widget.font_size = instance.height * 0.8

    def card_clicked(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.on_press(self.name)  # Call the assigned function