from codequest import *
import random

game = Game()

particle_system = objects.ParticleSystem(game, num_of_particles=1000, pos = Vector2(250, 250), looping=True, velocity=(100, 1000), drag = (75, 1000), size=(5,20), color=[(255, 0, 0), (0, 255, 0), (0, 0, 255)])

particle_system.play()

    
@game.on_update
def update():
    pass


game.run()