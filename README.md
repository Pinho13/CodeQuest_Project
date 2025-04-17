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

Game(name: str = "Window", width: int = 500, height: int = 500, background_color: tuple[int, int, int] = (255, 255, 255), fps: int = 60, show_fps: bool = True)

  * **name:** Name of the window
  * **width:** Width of the window
  * **height:** Height of the window
  * **background_color:** Background color
  * **fps:** Max fps
  * **show_fps:** If true shows fps on top of the window

## audio.py

### Sound()

Sound(sound: str, volume: float = 1)

  * **sound:** String with the path of the sound
  * **volume:** Volume of the sound

## objects.py

### Body()

Body(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, str, None] = None, center: bool = False)

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **image:** If given
    * None: renders as a rectangle
    * String: renders the image in the path given
    * Animation: renders the animation given
    * Animator: renders the current animation on the animator
  * **center:** If true the body is centered in the position given
