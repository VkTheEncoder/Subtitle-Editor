# Define your ASS style parameters here:
from pysubs2 import SSAStyle

# Play resolution (matching your video)
RESOLUTION = (1920, 1080)

# Single style definition (you can duplicate or extend this dict)
STYLE = {
    "Name": "TwCEN",
    "Fontname": "Tw Cen MT Condensed Extra Bold",
    "Fontsize": 36,
    # ASS uses &HAABBGGRR format (AA=alpha)
    "PrimaryColour": "&H00FFFFFF",   # white
    "SecondaryColour": "&H000000FF", # red (blue/red reversed order)
    "OutlineColour": "&H00000000",   # black
    "BackColour": "&H00000000",      # black (shadow/back)
    "Bold": False,
    "Italic": False,
    "Underline": False,
    "StrikeOut": False,
    "ScaleX": 112,
    "ScaleY": 75,
    "Spacing": 0.0,
    "Angle": 0.0,
    "BorderStyle": 1,    # 1 = Outline+Fill
    "Outline": 0.0,
    "Shadow": 0.0,
    # Alignment codes: 5 = center bottom
    "Alignment": 5,
    "MarginL": 1500,     # ASS margins are in pixels/10
    "MarginR": 1500,
    "MarginV": 1100,
    "Encoding": 1
}

# Helper to build an SSAStyle
ASS_STYLE = SSAStyle(**STYLE)
