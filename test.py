from codequest import *
import random

game = Game()

particle_system = objects.ParticleSystem(game, num_of_particles=(1, 5), pos = Vector2(100, 100), looping=True, velocity=(100, 1000), drag = (75, 1000), size=20)

particle_system.play()

    
@game.on_update
def update():
    pass


game.run()