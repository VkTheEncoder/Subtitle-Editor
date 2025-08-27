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
DefaultStyle.marginv     = 95

# ─── Encoding ─────────────────────────────────────────
DefaultStyle.encoding    = 1    # ANSI


# ─── Pika720 ─────────────────────────────────────────────────
Pika720 = pysubs2.SSAStyle()

# ─── Font & Size ───────────────────────────────────────
Pika720.name           = "Default"
Pika720.fontname       = "HelveticaRounded LT Std BdCn"
Pika720.fontsize       = 52

# ─── Colours (ASS uses &HAABBGGRR; AA = alpha) ────────
Pika720.primarycolour   = "&H00FFFFFF"  # white fill (AA=00 → opaque)
Pika720.secondarycolour = "&H000000FF"  # red outline (AA=00 → opaque)
Pika720.outlinecolour   = "&H00000000"  # black border (AA=00 → opaque)
Pika720.backcolour      = "&H96000000"  # semi-transparent black shadow

# ─── Style Flags ───────────────────────────────────────
Pika720.bold        = False
Pika720.italic      = False
Pika720.underline   = False
Pika720.strikeout   = False

# ─── Outline & Shadow Thickness ───────────────────────
Pika720.outline     = 1.9
Pika720.shadow      = 3.1

# ─── Scaling, Spacing, Rotation ───────────────────────
Pika720.scalex      = 100
Pika720.scaley      = 100
Pika720.spacing     = 0.0
Pika720.angle       = 0.0

# ─── Border Style & Alignment ─────────────────────────
Pika720.border_style = 1    # outline + drop-shadow
Pika720.alignment    = 2    # bottom-center

# ─── Margins (Left, Right, Vertical) ──────────────────
Pika720.marginl     = 60
Pika720.marginr     = 60
Pika720.marginv     = 65

# ─── Encoding ─────────────────────────────────────────
Pika720.encoding    = 1    # ANSI



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

SiteStyle.marginl    = 9
SiteStyle.marginr    = 15
SiteStyle.marginv    = 5

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

# ─── Pika 480p ────────────────────────────────────────────────────
Pika480p = pysubs2.SSAStyle()
Pika480p.name           = "Pika 480p"
Pika480p.fontname       = "HelveticaRounded LT Std BdCn"
Pika480p.fontsize       = 36

Pika480p.primarycolour   = "&H00FFFFFF"  # white fill
Pika480p.secondarycolour = "&H000000FF"  # red outline
Pika480p.outlinecolour   = "&H00000000"  # black border
Pika480p.backcolour      = "&H00000000"  # no opaque box

Pika480p.bold        = False
Pika480p.italic      = False
Pika480p.underline   = False
Pika480p.strikeout   = False

Pika480p.outline     = 1.1
Pika480p.shadow      = 2.1

Pika480p.scalex      = 100
Pika480p.scaley      = 100
Pika480p.spacing     = 0.0
Pika480p.angle       = 0.0

Pika480p.border_style = 1   # outline + shadow
Pika480p.alignment    = 2   # bottom-center

Pika480p.marginl     = 60
Pika480p.marginr     = 60
Pika480p.marginv     = 45

Pika480p.encoding    = 1    # ANSI


# ─── Tales Of Herding Gods ─────────────────────────────────────────
TalesOfHerdingGods = pysubs2.SSAStyle()
TalesOfHerdingGods.name            = "Tales Of Herding Gods"

# Font & Size (from your screenshot)
TalesOfHerdingGods.fontname        = "Arial Rounded MT Bold"
TalesOfHerdingGods.fontsize        = 62
TalesOfHerdingGods.bold            = True
TalesOfHerdingGods.italic          = False
TalesOfHerdingGods.underline       = False
TalesOfHerdingGods.strikeout       = False

# Colours
TalesOfHerdingGods.primarycolour   = "&H00FFFFFF"  # white
TalesOfHerdingGods.secondarycolour = "&H000000FF"  # red
TalesOfHerdingGods.outlinecolour   = "&H00000000"  # black
TalesOfHerdingGods.backcolour      = "&H00000000"  # black shadow

# Outline & Shadow (same feel as shrouding)
TalesOfHerdingGods.outline         = 3.1
TalesOfHerdingGods.shadow          = 3.8

# Scaling / spacing / rotation (from screenshot)
TalesOfHerdingGods.scalex          = 87
TalesOfHerdingGods.scaley          = 108
TalesOfHerdingGods.spacing         = 0.0
TalesOfHerdingGods.angle           = 0.0

# Border & placement
TalesOfHerdingGods.border_style    = 1     # outline + drop-shadow
TalesOfHerdingGods.alignment       = 2     # bottom-center

# Margins (from screenshot)
TalesOfHerdingGods.marginl         = 10
TalesOfHerdingGods.marginr         = 10
TalesOfHerdingGods.marginv         = 137

# Encoding
TalesOfHerdingGods.encoding        = 1     # ANSI


STYLES = {
    "Pika 1080p":            [DefaultStyle, SiteStyle],
    "Pika 720p":             [Pika720, SiteStyle],
    "Shrouding The Heavens": [ShroudingTheHeavens],
    "Tales Of Herding Gods": [TalesOfHerdingGods],  
    "Pika 480p":             [Pika480p, SiteStyle],
}
