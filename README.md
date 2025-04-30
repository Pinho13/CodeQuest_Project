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
    * [Game()](docs/Game().md)
    * <font color="red"><a href=https://github.com/Pinho13/CodeQuest_Project/blob/main/docs/Game().md>A</a></font>
    * audio.py
      * [Sound()](docs/audio.py/Sound().md)
    * objects.py
      * [Body()](docs/objects.py/Body().md)
      * [RigidBody()](docs/objects.py/RigidBody().md) $${\color{lightblue}From \space Body}$$
      * [ParticleSystem()](docs/objects.py/ParticleSystem().md)
    * sprites.py
      * [Animation()](docs/sprites.py/Animation().md)
      * [Animator()](docs/sprites.py/Animator().md)
    * [tools.py](docs/tools.py/tools.py.md)
      * [Timer()](docs/tools.py/Timer().md)
    * ui.py
      * Text()
      * Button() $${\color{lightblue}From \space Body}$$


# Documentation

## Game()

```py
Game(name: str = "Window", width: int = 500, height: int = 500, background_color: tuple[int, int, int] = (255, 255, 255), fps: int = 60, show_fps: bool = True)
```

  * **name:** Name of the window
  * **width:** Width of the window
  * **height:** Height of the window
  * **background_color:** Background color
  * **fps:** Max fps
  * **show_fps:** If true shows fps on top of the window

## audio.py

### Sound()

```py
Sound(sound: str, volume: float = 1)
```

  * **sound:** String with the path of the sound
  * **volume:** Volume of the sound

## objects.py

### Body()

```py
Body(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, str, None] = None, center: bool = False)
```

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

### RigidBody()

```py
RigidBody(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, None] = None, gravity: pygame.Vector2 = pygame.Vector2(0, 980), mass: float = 1, drag: float = 0, deacceleration: float = 0, center: bool = False)
```

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **image:** If given
    * None: renders as a rectangle
    * String: renders the image in the path given
    * Animation: renders the animation given
    * Animator: renders the current animation on the animator
  * **gravity:** Gravity of the body
  * **mass:** Mass of the body
  * **drag:** Opposite force to velocity
  * **deacceleration:** Opposite force to acceleration
  * **center:** If true the body is centered in the position given

### ParticleSystem()

```py
ParticleSystem(game, num_of_particles: Union[int, tuple] = 10, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: Union[int, tuple] = 50, color: Union[list, tuple[int, int, int]] = (0, 0, 0), duration: Union[float, tuple] = 1, looping: bool = False, direction: tuple[int, int] = (0, 360), velocity: Union[float, tuple] = 5, drag: Union[float, tuple] = 1)
```

  * **game:** Game instance
  * **num_of_particles:** If given
    * Int: Creates a fix number of particles
    * Tuple: Creates a random number of particles between those two values
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **duration:** If given
    * Float: Particles live for that fixed duration
    * Tuple: Particles live for a random period between those two values
  * **looping:** If true the effect keeps looping
  * **direction:** Direction range where the particles will go
  * **velocity:** If given
    * Float: Particles have fixed velocity
    * Tuple: Particles have a random velocity between those two values
  * **drag:** If given
    * Float: Particles have fixed drag
    * Tuple: Particles have a random drag between those two values

## sprites.py

### Animation()

```py
Animation(game, name: str, animation: Union[list, str], time_between_frames: float = 1, looping: bool = True)
```

  * **game:** Game instance
  * **name:** Animation name
  * **animation:** If given
    * List of strings: Makes an animation from the sprites in the paths given in the list
    * String: Makes an animation from the sprites in the path given
  * **time_between_frames:** Time between each frame
  * **looping:** Loops animation if true

### Animator()

```py
Animator(game, animations: Union[list[Animation], Animation], idle_anim: Animation = None)
```

  * **game:** Game instance
  * **animations:** If given
    * List of animations: Animations in the animator
    * Animation: Makes it the only animation in the animator
  * **idle_anim:** If given
    * Animation: Makes it the idle animation
    * None: makes the idle animation the first animation given in animations


## tools.py

### Timer()

```py
Timer(game, time: float = 1, looping: bool = False, functions: Union[list, function] = [], play_on_start: bool = True)
```

  * **game:** Game instance
  * **time:** Cooldown time
  * **looping:** If true loops the timer
  * **functions:** If given
    * List of functions: The functions will trigger once the timer finishes 
    * Function: THe function will trigger once the timer finishes
  * **play_on_start:** If true timer will start when instantiated


## ui.py

### Text()

```py
Text(game, text: str, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: int = 50, color: tuple[int, int, int] = (0, 0, 0), center: bool = False)
```

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **center:** If true the body is centered in the position given

### Button()

```py
Button(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), normal_image: str = None, hover_image: str = None, clicked_image: str = None, normal_color: tuple[int, int, int] = (0, 0, 0), hover_color: tuple[int, int, int] = None, clicked_color: tuple[int, int, int] = None, text: str = "", text_color: tuple[int, int, int] = (255, 255, 255), center: bool = False)
```

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **normal_image:** Default button image
  * **hover_image:** Image when mouse hovering button
  * **clicked_image:** Image when button clicked
  * **normal_color:** Default button color
  * **hover_color:** Color when mouse hovering button
  * **clicked_color:** Color when button clicked
  * **text:** Button text
  * **center:** If true the body is centered in the position given