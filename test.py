from codequest import *
game = Game()
rect = objects.RigidBody(game=game, pos=Vector2(250, 250), size=Vector2(100, 100), color = (50, 100, 100))


@game.on_update
def update():
    pass

game.run()
