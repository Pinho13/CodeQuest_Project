from codequest import *

game = Game()



colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
current_color = 0

def change_color():
    global current_color
    current_color += 1
    if current_color == len(colors):
        current_color = 0
    game.background_color = colors[current_color]


timer = tools.Timer(game, 0.01, looping=True, functions=change_color)

@game.on_update
def update():
    pass

game.run()