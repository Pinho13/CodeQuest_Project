from codequest import *
game = Game()

idle = sprites.Animation(game, "idle", "images")
walk = sprites.Animation(game, "walk", ["images/image2.png", "images/image1.png"])

animator = sprites.Animator(game, [idle, walk])

rect = objects.RigidBody(game=game, pos=Vector2(250, 250), size=Vector2(200, 50), color = (50, 100, 100), drag=200, deacceleration= 2500, gravity= Vector2(0, 0),image=animator)

@game.on_update
def update():
    pass

@idle.on_finnish
def when_idle_finnishes():
    print("Changed")
    rect.animator.play(walk)

game.run()
