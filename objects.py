import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, game, text: str, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: int = 50, color: tuple[int, int, int] = (0, 0, 0)):
        super().__init__()
        self.game = game

        #Implement it inGame
        game.sprites.add(self)
        game.update_functions.append(self.update)

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


class Body(pygame.sprite.Sprite):
    def __init__(self, game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0)):
        super().__init__()
        self.game = game

        #Implement it inGame
        game.sprites.add(self)
        game.update_functions.append(self.update)

        #Atributes
        self.pos = pos
        self.color = color
        self.size = size

        #Body Creation
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.image.fill(self.color)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
