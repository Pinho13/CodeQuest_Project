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
