from CodeQuest import *

# Create a Game Instance
game = Game()

def change_background_color():
    if game.background_color == (0,0,0):
        game.background_color = (255,255,255)
    else:
        game.background_color = (0,0,0)

timer1 = tools.Timer(game, 1, True, [change_background_color], True)

# Run Game
game.run()
