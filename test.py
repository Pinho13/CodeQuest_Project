from codequest import *
import random

game = Game()
button = ui.Button(game, text="ababa")
#text = ui.Text(game, "a", size=100)

@game.on_update
def update():
    pass


game.run()