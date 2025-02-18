import codequest
import pygame

game = codequest.Game()


@game.on_update
def update(game):
    pygame.draw.rect(game.screen, (255, 0, 0), (50, 50, 100, 100))


game.run()
