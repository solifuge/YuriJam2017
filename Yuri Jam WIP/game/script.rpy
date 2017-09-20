# The script of the game goes in this file.

# This is a quick dissolve....
define qdis = Dissolve(0.25)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(None, kind=nvl, what_color="#ea7aa0", what_prefix="\"", what_suffix="\"")
define narrator = nvl_narrator
define menu = nvl_menu


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene corkboard

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # These display lines of dialogue.

    "Somebody once told me the world was gonna roll me, I ain't the sharpest tool in the shed. She was lookin' kinda dumb with her finger and her thumb in the shape of an L on her forehead."
    
    show m neut with moveinright
    
    e "You've created a new Ren'Py game."
    
    show r neut wave with moveinright

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show m armlift smile with qdis

    "Sorry, I have no idea what I'm doing."
    
    show r shock with qdis
    
    "Shenanigans!"
    
    # This ends the game.

    return
