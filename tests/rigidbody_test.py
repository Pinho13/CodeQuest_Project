from CodeQuest import *

# Create a Game Instance
game = Game()

body1 = objects.RigidBody(game, Vector2(100, 100), Vector2(100, 75), deacceleration=500)
body2 = objects.RigidBody(game, Vector2(200, 100), (25, 25), (255, 0, 0), gravity=(0, -80))
body3 = objects.RigidBody(game, Vector2(300, 100), (100, 100), (0, 255, 0))

body1.add_force((0, -1350))

# Updates every frame
@game.on_update
def update():
    pass

# Run Game
game.run()
