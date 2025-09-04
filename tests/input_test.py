from CodeQuest import *

# Create a Game Instance
game = Game()

# Updates every frame
@game.on_update
def update():
    if pygame.K_a in game.keys_down:
        print("A key is down")
    
    if pygame.K_a in game.keys_up:
        print("A key is up")
    
    if pygame.K_a in game.keys_pressed:
        print("A key is pressed")
    
    if 1 in game.mouse_down:
        print("MouseButton 1 down")
    
    if 1 in game.mouse_up:
        print("MouseButton 1 up")
    
    if 1 in game.mouse_pressed:
        print("MouseButton 1 pressed")

# Run Game
game.run()