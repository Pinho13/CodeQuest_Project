from scodequest import *

# Create a Game Instance
game = Game()
body = objects.Body(game, pos=Vector2(200, 200), color=(255, 0, 0))
col = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
i = 0

@game.on_update
def update():
    global i
    body.color = col[i]
    if 1 in game.mouse_down:
        if i == 2:
            i = 0
        else:
            i += 1

game.run()