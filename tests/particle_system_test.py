from CodeQuest import *

# Create a Game Instance
game = Game()

particle_system = objects.ParticleSystem(game, (50, 500), Vector2(250, 250), (10, 25), [(255,0 ,0), (0, 255, 0), (0, 0, 255)], 2, True, velocity=(100, 1000), drag=(75, 1000))
particle_system.play()

# Updates every frame
@game.on_update
def update():
    pass

# Run Game
game.run()
