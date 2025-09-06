from CodeQuest import *

game = Game()

text = ui.Text(game, "Test Text", (250, 150), 50, (0,0,0), True)
button = ui.Button(game, Vector2(250, 250), Vector2(100,50), normal_color=(240, 240, 240), hover_color=(200, 200, 200), clicked_color=(150, 150, 150), text="Test Button", text_color=(0,0,0), center=True)

# Updates every frame
@game.on_update
def update():
    pass

# Run Game
game.run()
