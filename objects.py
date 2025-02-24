import pygame
import sprites
import tools

from typing import Union

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
    def __init__(self, game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, str, None] = None):
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
        self.animator = None
        if image == None:
            self.image = pygame.Surface(size)
            self.image.fill(self.color)
        elif type(image) == str:
            self.animator = image
            self.image = tools.convert_images([image])[0]
            self.image = pygame.transform.scale(self.image, self.size)
        else:
            self.animator = image
            self.image = image.frame
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        if self.animator == None:
            self.image.fill(self.color)
        elif type(self.animator) != str:
            self.image = self.animator.frame
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)
    
    #Check if Point is inside Rect
    def is_colliding_with_point(self, pos: pygame.Vector2):
        return self.rect.collidepoint(pos)
    
    #Check if Rect is touching Rect
    def is_colliding_with_rect(self, rect: pygame.Rect):
        return self.rect.colliderect(rect)


class RigidBody(Body):
    def __init__(self, game, pos = pygame.Vector2(0, 0), size = pygame.Vector2(50, 50), color = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, None] = None, gravity: pygame.Vector2 = pygame.Vector2(0, 980), mass: float = 1, drag: float = 0, deacceleration: float = 0):
        super().__init__(game, pos, size, color, image)
        self.game = game

        #Implement it inGame
        game.update_functions.append(self.physics_update)

        #Atributes
        self.gravity = gravity
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.deacceleration = deacceleration
        self.drag = drag
        self.mass = mass
    
    def physics_update(self):
        #Move
        self.velocity += (self.gravity + self.acceleration) * self.game.delta_time
        self.pos += self.velocity * self.game.delta_time

        #Slow Down
        self.acceleration = self.acceleration.move_towards(pygame.Vector2(), self.deacceleration * self.game.delta_time)
        self.velocity = self.velocity.move_towards(pygame.Vector2(), self.drag * self.game.delta_time)
    
    def add_force(self, force: pygame.Vector2):
        self.acceleration += force/self.mass
