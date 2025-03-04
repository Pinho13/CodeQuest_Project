from codequest import *

game = Game()

particle_system = objects.ParticleSystem(game, pos = Vector2(100, 100), velocity=20, size=20)

particle_system.play()


@game.on_update
def update():
    pass


game.run()