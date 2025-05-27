import pysubs2

# Build a clean SSAStyle and then override its fields:
DefaultStyle = pysubs2.SSAStyle()

# ─── Font & Size ───────────────────────────────────────
DefaultStyle.fontname       = "HelveticaRounded LT Std BdCn"
DefaultStyle.fontsize       = 78

# ─── Colours (ASS uses &HAABBGGRR; AA = alpha) ────────
DefaultStyle.primarycolour   = "&H00FFFFFF"  # white fill (AA=00 → opaque)
DefaultStyle.secondarycolour = "&H000000FF"  # red outline (AA=00 → opaque)
DefaultStyle.outlinecolour   = "&H00000000"  # black border (AA=00 → opaque)

# Here’s your semi-transparent shadow/backcolour:
#   Alpha=150 dec → 0x96 hex,
#   so &H96000000 means 150/255 transparency
DefaultStyle.backcolour      = "&H96000000"

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
DefaultStyle.border_style = 1    # 1 = outline + drop-shadow
DefaultStyle.alignment    = 2    # 2 = bottom-center

# ─── Margins (Left, Right, Vertical) ──────────────────
DefaultStyle.marginl     = 60
DefaultStyle.marginr     = 60
DefaultStyle.marginv     = 65

# ─── Encoding ─────────────────────────────────────────
DefaultStyle.encoding    = 1    # 1 = ANSI

# (Everything else inherits pysubs2’s defaults.)
