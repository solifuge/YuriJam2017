# The script of the game goes in this file.

# Custom "with" Transitions are defined here:
define quickdissolve = Dissolve(0.25)
define starwipeout = ImageDissolve("StarWipe.png", 0.5)
define starwipein = ImageDissolve("StarWipe.png", 0.5, reverse=True)

# Custom "at" Positions are defined here:

transform photo_top:
    xcenter 0.74
    ycenter 0.245

transform sprite_left:
    xcenter 0.6125
    ycenter 0.71

transform sprite_center:
    xcenter 0.74
    ycenter 0.71

transform sprite_right:
    xcenter 0.8667
    ycenter 0.71

# These transforms move the portrait frames or sprites between left, center, and right positions.
transform sprite_to_center:
    easein 0.25 xpos 0.74

transform sprite_to_left:
    easein 0.25 xpos 0.6125

transform sprite_to_right:
    easein 0.25 xpos 0.8667

# These transforms scoot
transform scoot_far_left:
    easein 0.5 xanchor 0.75

transform scoot_left:
    easein 0.5 xanchor 0.625

transform scoot_center:
    easein 0.5 xanchor 0.5

transform scoot_right:
    easein 0.5 xanchor 0.375

transform scoot_far_right:
    easein 0.5 xanchor 0.25

# These transforms instantly set the sprite in the frame.
transform offset_far_left:
    xanchor 0.75

transform offset_left:
    xanchor 0.625

transform offset_center:
    xanchor 0.5

transform offset_right:
    xanchor 0.375

transform offset_far_right:
    xanchor 0.25

# These animations 
transform animate_shake:
    linear 0.125 xanchor 0.51
    linear 0.125 xanchor 0.49
    repeat

transform animate_shake_left:
    linear 0.125 xanchor 0.635
    linear 0.125 xanchor 0.615
    repeat

transform animate_shake_right:
    linear 0.125 xanchor 0.385
    linear 0.125 xanchor 0.365
    repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(None, kind=nvl,
    who_color="#fff", who_outlines=[ (2, "#ffc1d8") ],
    what_color="#ff9fc5", what_outlines=[ (2, "#B24C7F") ],
    what_prefix="\"", what_suffix="\"")

define r = Character(None, kind=nvl,
    who_color="#fff", who_outlines=[ (2, "#b6e0f4") ],
    what_color="#8ed0ee", what_outlines=[ (2, "#336699") ],
    what_prefix="\"", what_suffix="\"")

define menu = nvl_menu
define narrator = Character(None, kind=nvl,
    what_color="#000", what_outlines=[ (0, "#fff") ])

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.R

    scene corkboard with starwipeout

    show photo test at photo_top with easeintop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # These display lines of dialogue.

    "Somebody once told me the world was gonna roll me, I ain't the sharpest tool in the shed. She was lookin' kinda dumb with her finger and her thumb in the shape of an L on her forehead."
    
    show pink dot at sprite_center
    show maple shy smile at sprite_center
    with easeinbottom
    
    m "Hey look, it's me! A Protagonist!"

    show pink dot at sprite_to_left
    show maple neutral at sprite_to_left

    show blue dot at sprite_right
    show rae smile at sprite_right
    with easeinbottom

    r "Make room! You're not the only one in this story, y'know."

    show rae neutral
    show maple reading

    m "Two main characters? Let's see... I think that makes one of us a Deuteragonist, but who..."
    
    show rae shock at scoot_right

    r "I-is that even a word?!"

    # This ends the game.

    return
