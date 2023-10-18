"""
CP1404/CP5632 Practical 05
Look up hexadecimal codes
"""

NAME_TO_CODE = {"absolutezero": "0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "amaranth": "#e52b50",
                "amber": "#ffbf00", "amethyst": '#9966cc', "apricot": "#fbceb1", "aqua": "#00ffff", "beige": "#f5f5dc",
                "bistre": "#3d2b1f"}

color_name = input("Color name: ").lower()

while color_name != "":
    try:
        print(color_name, "is", NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Color name: ").lower()
