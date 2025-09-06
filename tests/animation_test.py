from CodeQuest import *

# Create a Game Instance
game = Game()

anim1 = sprites.Animation(game, "anim", ["./tests/test_assets/image1.png", "./tests/test_assets/image2.png"], 1, True)
anim2 = sprites.Animation(game, "anim", ["./tests/test_assets/image1.png"], 1, True)
animator = sprites.Animator(game, [anim1, anim2])

body = objects.Body(game, size=(200, 100), pos=(250, 250), image=animator, center=True)




@animator.on_finish
def func():
    animator.play(anim2)
    
# Run Game
game.run()
