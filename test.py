from codequest import *
game = Game()
text = objects.Text(game, "Test", color=pygame.Color("black"))

@game.on_update
def update():
    pass


game.run()
