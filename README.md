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

# Create a Game Instance
game = Game()

# Updates every frame
@game.on_update
def update():
    pass

# Run Game
game.run()
```

## Architecture Overview

  * CodeQuest
    * [Game()](docs/Game().md)
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
      * [Text()](docs/ui.py/Text().md)
      * [Button()](docs/ui.py/Button().md) $${\color{lightblue}From \space Body}$$
