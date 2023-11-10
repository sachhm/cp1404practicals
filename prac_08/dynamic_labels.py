"""
CP1404/CP5632 Practical
Dynamically create labels based on content of dictionary
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """ Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Lindsay", "Jason", "Osmond", "Bob", "Larry", "Steve"]

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()

    def create_labels(self):
        """ Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            print(name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
