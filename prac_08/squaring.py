"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015

Modified by Sachh Ariel Moka
Started 7/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward' # Modified by Sachh Moka


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (400, 200)  # I changed this from the original file to fit better on my computer
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ Handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
