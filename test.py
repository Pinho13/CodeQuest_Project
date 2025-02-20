from codequest import *
game = Game()
rect = objects.RigidBody(game=game, pos=Vector2(250, 250), size=Vector2(20, 20), color = (50, 100, 100), drag=200, deacceleration= 2500, gravity= Vector2(0, 980))

rect.add_force(Vector2(-100, -2000))
@game.on_update
def update():
    pass

game.run()
