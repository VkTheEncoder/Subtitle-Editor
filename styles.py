import pysubs2

# ─── DefaultStyle ─────────────────────────────────────────────────
DefaultStyle = pysubs2.SSAStyle()

# ─── Font & Size ───────────────────────────────────────
DefaultStyle.name           = "Default"
DefaultStyle.fontname       = "HelveticaRounded LT Std BdCn"
DefaultStyle.fontsize       = 78

# ─── Colours (ASS uses &HAABBGGRR; AA = alpha) ────────
DefaultStyle.primarycolour   = "&H00FFFFFF"  # white fill (AA=00 → opaque)
DefaultStyle.secondarycolour = "&H000000FF"  # red outline (AA=00 → opaque)
DefaultStyle.outlinecolour   = "&H00000000"  # black border (AA=00 → opaque)
DefaultStyle.backcolour      = "&H96000000"  # semi-transparent black shadow

# ─── Style Flags ───────────────────────────────────────
DefaultStyle.bold        = False
DefaultStyle.italic      = False
DefaultStyle.underline   = False
DefaultStyle.strikeout   = False

# ─── Outline & Shadow Thickness ───────────────────────
DefaultStyle.outline     = 3.0
DefaultStyle.shadow      = 4.5

# ─── Scaling, Spacing, Rotation ───────────────────────
DefaultStyle.scalex      = 100
DefaultStyle.scaley      = 100
DefaultStyle.spacing     = 0.0
DefaultStyle.angle       = 0.0

# ─── Border Style & Alignment ─────────────────────────
DefaultStyle.border_style = 1    # outline + drop-shadow
DefaultStyle.alignment    = 2    # bottom-center

# ─── Margins (Left, Right, Vertical) ──────────────────
DefaultStyle.marginl     = 60
DefaultStyle.marginr     = 60
DefaultStyle.marginv     = 65

# ─── Encoding ─────────────────────────────────────────
DefaultStyle.encoding    = 1    # ANSI


# ─── SiteStyle ───────────────────────────────────────────────────
SiteStyle = pysubs2.SSAStyle()

SiteStyle.name            = "site"
SiteStyle.fontname        = "Tw Cen MT Condensed Extra Bold"
SiteStyle.fontsize        = 36
SiteStyle.primarycolour   = "&H00FFFFFF"   # white fill
SiteStyle.secondarycolour = "&H000000FF"   # red outline
SiteStyle.outlinecolour   = "&H00000000"   # black border
SiteStyle.backcolour      = "&H00000000"   # black shadow

SiteStyle.bold       = False
SiteStyle.italic     = False
SiteStyle.underline  = False
SiteStyle.strikeout  = False

SiteStyle.outline    = 0.0
SiteStyle.shadow     = 0.0

SiteStyle.scalex     = 112
SiteStyle.scaley     = 75
SiteStyle.spacing    = 0.0
SiteStyle.angle      = 0.0

SiteStyle.border_style = 1       # outline + drop-shadow
SiteStyle.alignment    = 5       # bottom-center

SiteStyle.marginl    = 15
SiteStyle.marginr    = 15
SiteStyle.marginv    = 11

SiteStyle.encoding   = 1        # ANSI


# ─── Shrouding The heavens ─────────────────────────────────────────
ShroudingTheHeavens = pysubs2.SSAStyle()
ShroudingTheHeavens.name            = "Shrouding The heavens"

# Font & Size
ShroudingTheHeavens.fontname        = "Arial Rounded MT Bold"
ShroudingTheHeavens.fontsize        = 67
ShroudingTheHeavens.bold            = True
ShroudingTheHeavens.italic          = False
ShroudingTheHeavens.underline       = False
ShroudingTheHeavens.strikeout       = False

# Colours
ShroudingTheHeavens.primarycolour   = "&H00FFFFFF"  # white
ShroudingTheHeavens.secondarycolour = "&H000000FF"  # red
ShroudingTheHeavens.outlinecolour   = "&H00000000"  # black
ShroudingTheHeavens.shadowcolour    = "&H00FF0000"  # blue

# Outline & Shadow
ShroudingTheHeavens.outline         = 3.0
ShroudingTheHeavens.shadow          = 3.7

# Scaling, Spacing, Rotation
ShroudingTheHeavens.scalex          = 87
ShroudingTheHeavens.scaley          = 108
ShroudingTheHeavens.spacing         = 0.0
ShroudingTheHeavens.angle           = 0.0

# Border Style & Alignment
ShroudingTheHeavens.border_style    = 1     # outline + drop-shadow
ShroudingTheHeavens.alignment       = 2     # bottom-center

# Margins
ShroudingTheHeavens.marginl         = 10
ShroudingTheHeavens.marginr         = 10
ShroudingTheHeavens.marginv         = 125

# Encoding
ShroudingTheHeavens.encoding        = 1     # ANSI

FackyStyle = pysubs2.SSAStyle()

FackyStyle.name            = "facky"
FackyStyle.fontname        = "Tw Cen MT Condensed Extra Bold"
FackyStyle.fontsize        = 36
FackyStyle.primarycolour   = "&H00FFFFFF"   # white fill
FackyStyle.secondarycolour = "&H000000FF"   # red outline
FackyStyle.outlinecolour   = "&H00000000"   # black border
FackyStyle.backcolour      = "&H00000000"   # black shadow

FackyStyle.bold       = False
FackyStyle.italic     = False
FackyStyle.underline  = False
FackyStyle.strikeout  = False

FackyStyle.outline    = 0.0
FackyStyle.shadow     = 0.0

FackyStyle.scalex     = 112
FackyStyle.scaley     = 75
FackyStyle.spacing    = 0.0
FackyStyle.angle      = 0.0

FackyStyle.border_style = 1       # outline + drop-shadow
FackyStyle.alignment    = 5       # bottom-center

FackyStyle.marginl    = 15
FackyStyle.marginr    = 15
FackyStyle.marginv    = 11

FackyStyle.encoding   = 1        # ANSI

STYLES = {
    "Pikasub":               [DefaultStyle, SiteStyle],
    "Shrouding The Heavens": [ShroudingTheHeavens, FackyStyle],
}
