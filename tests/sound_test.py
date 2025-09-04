from CodeQuest import *

# Create a Game Instance
game = Game()

sound = audio.Sound("./tests/test_assets/pipe.mp3")

# Updates every frame
@game.on_update
def update():
    #Play sound when enter key down
    if pygame.K_RETURN in game.keys_down:
        sound.play()
        
    #Stop sound when esc key down
    if pygame.K_ESCAPE in game.keys_down:
        sound.stop()
    

# Run Game
game.run()
