import pysubs2

# Build your style by overriding attributes on a default SSAStyle()
DefaultStyle = pysubs2.SSAStyle()

# Don't pass "Name" or other ASS-field caps to the ctor—just override attrs:
DefaultStyle.fontname       = "HelveticaRounded LT Std BdCn"
DefaultStyle.fontsize       = 78
DefaultStyle.primarycolour  = "&H00FFFFFF"  # white
DefaultStyle.secondarycolour= "&H000000FF"  # red
DefaultStyle.outlinecolour  = "&H00000000"  # black
DefaultStyle.backcolour     = "&H00000000"  # black (shadow)
DefaultStyle.bold           = False
DefaultStyle.italic         = False
DefaultStyle.underline      = False
DefaultStyle.strikeout      = False
DefaultStyle.outline        = 3.0
DefaultStyle.shadow         = 4.5
DefaultStyle.scalex         = 100
DefaultStyle.scaley         = 100
DefaultStyle.spacing        = 0.0
DefaultStyle.angle          = 0.0
DefaultStyle.border_style   = 1    # outline+shadow
DefaultStyle.alignment      = 2    # bottom-center
DefaultStyle.marginl        = 60
DefaultStyle.marginr        = 60
DefaultStyle.marginv        = 65
DefaultStyle.encoding       = 1
