import pygame

from typing import Union

class Text(pygame.sprite.Sprite):
    def __init__(self, game, text: str, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: int = 50, color: tuple[int, int, int] = (0, 0, 0)):
        super().__init__()
        self.game = game

        #Implement it inGame
        game.sprites.add(self)
        game.update_functions.append(self.update)
        self.ingame = True

        #Atributes
        self.pos = pos
        self.color = color
        self.size = size
        self.text = text
        
        #Others
        self.current_size = size

        #Text Creation
        self.text_font = pygame.font.SysFont(None, size)
        self.image = self.text_font.render(text, True, color)
        self.rect = self.image.get_rect(topleft=pos)
    
    def update(self):
        self.check_if_size_changed()

        self.rect = self.image.get_rect(topleft=self.pos)
        self.image = self.text_font.render(self.text, True, self.color)

    def check_if_size_changed(self):
        if self.size != self.current_size:
            self.text_font = pygame.font.SysFont(None, int(self.size))
            self.image = self.text_font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.current_size = self.size
    
    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.sprites.add(self)
        self.game.update_functions.append(self.update)

    #Remove from rendering and updating
    def remove_from_game(self):
        self.ingame = False
        self.game.sprites.remove(self)
        self.game.update_functions.remove(self.update)