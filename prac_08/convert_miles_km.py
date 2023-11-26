"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.609344


class ConverterApp(App):
    """ ConverterApp is a Kivy App for converting miles to kilometers """
    km_output = StringProperty()

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.km_output = ""
        return self.root

    def update_distance(self, miles):
        """ Update the distance in the Kivy App"""
        result = self.calculate_kilometers(miles)
        self.root.ids.output_label.text = f"{result}"

    def calculate_kilometers(self, miles):
        """ Calculate kilometers from miles"""
        try:
            result = float(miles) * CONVERSION_FACTOR
        except ValueError:
            result = 0.0

        return result

    def handle_increment(self, miles, amount):
        """ Add amount to the miles input """
        try:
            miles = float(miles)
            miles += amount
        except ValueError:
            miles = 0
            miles += amount
        self.root.ids.miles_input.text = f"{miles}"


ConverterApp().run()
