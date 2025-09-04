from CodeQuest import *

# Create a Game Instance
game = Game()

body1 = objects.Body(game, Vector2(100, 100), Vector2(100, 75),center=True, image="./tests/test_assets/image1.png")
body2 = objects.Body(game, Vector2(200, 100), (25, 25), (255, 0, 0))
body3 = objects.Body(game, Vector2(300, 100), (100, 100), (0, 255, 0))

body1.set_rotation(45)

# Updates every frame
@game.on_update
def update():
    #Tests Point Collision
    if body2.is_colliding_with_point(pygame.mouse.get_pos()):
        body2.color = (0, 0, 255)
    else:
        body2.color = (255, 0, 0)
    
    if body3.is_colliding_with_point(pygame.mouse.get_pos()):
        body3.color = (0, 0, 255)
    else:
        body3.color = (0, 255, 0)

# Run Game
game.run()
