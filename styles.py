import pysubs2

# “Default” style matching your Aegisub screenshot
DefaultStyle = pysubs2.SSAStyle(
    Name="Default",
    Fontname="HelveticaRounded LT Std BdCn",
    Fontsize=78,
    PrimaryColour="&H00FFFFFF",    # white
    SecondaryColour="&H000000FF",  # red
    OutlineColour="&H00000000",    # black
    BackColour="&H00000000",       # black (shadow)
    Bold=False,
    Italic=False,
    Underline=False,
    StrikeOut=False,
    Outline=3.0,
    Shadow=4.5,
    ScaleX=100,
    ScaleY=100,
    Spacing=0.0,
    Angle=0.0,
    BorderStyle=1,                 # outline+shadow
    Alignment=2,                   # bottom-center
    MarginL=60,
    MarginR=60,
    MarginV=65,
    Encoding=1
)
