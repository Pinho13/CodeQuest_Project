# CodeQuest

  CodeQuest is a wrapper for pygame that simplifies the game making process, letting users create games with minimal or no knowledge of pygame. Great for beginners Learning Python.

## How to Start

  * Clone the repo
  * Install Python
  * Install Pygame
  * Create a New Python File in the same Directory
  * Write the Code below

```py
from codequest import *

#Create a Game Instance
game = Game()

#Updates every frame
@game.on_update
def update():
    pass

#Run Game
game.run()
```

## Architecture Overview

  * CodeQuest
    * Game()
    * audio.py
      * Sound()
    * objects.py
      * Body()
      * RigidBody() $${\color{lightblue}From \space Body}$$
      * ParticleSystem()
    * sprites.py
      * Animation()
      * Animator()
    * tools.py
      * Timer()
    * ui.py
      * Text()
      * Button() $${\color{lightblue}From \space Body}$$
    * audio.py
      * Sound()


# Documentation

  ## Game()

Game(name="Window", width=500, height=500, background_color=(255, 255, 255), fps=60, show_fps=True)

  * **name:** Name of the window
  * **width:** Width of the window
  * **height:** Height of the window
  * **background_color:** Background color
  * **fps:** Max fps
  * **show_fps:** Shows fps on top of the window

## audio.py

### Sound()
