import pygame
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
    
    #Check if Point is inside Rect
    def is_colliding_with_point(self, pos: pygame.Vector2):
        return self.rect.collidepoint(pos)
    
    #Check if Rect is touching Rect
    def is_colliding_with_rect(self, rect: pygame.Rect):
        return self.rect.colliderect(rect)


class RigidBody(Body):
    def __init__(self, game, pos = pygame.Vector2(0, 0), size = pygame.Vector2(50, 50), color = (0, 0, 0), gravity: pygame.Vector2 = pygame.Vector2(0, 980), mass: float = 1, drag: float = 0, deacceleration: float = 0):
        super().__init__(game, pos, size, color)
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


class Animation:
    def __init__(self,name: str, animation: Union[list, str], time_between_frames: float = 10, looping: bool = True):
        #Atributes
        self.name = name
        self.animation = []
        self.time_between_frames = time_between_frames
        self.looping = looping
        self.current_frame_index = 0
        self.frame = self.animation[0]
        self.animation_finnished = False

        #Load Animation Images
        if isinstance(animation, str):
            animation = tools.get_files_from_dir(animation)
        self.animation.append(tools.convert_images(animation))

        #Time of Previous Frame
        self.previous_frame_time = pygame.time.get_ticks()
    
    def play(self):
        if pygame.time.get_ticks() - self.previous_frame_time >= self.time_between_frames:
            self.current_frame_index += 1
            if self.current_frame_index == len(self.animation):
                self.current_frame_index = 0
                if not self.looping:
                    self.animation_finnished = True
            self.frame = self.animation[self.current_frame_index]


class Animator:
    def __init__(self, game, idle_anim: Animation, animations: list[Animation]):
        self.game = game

        #Implement it inGame
        game.update_functions.append(self.update)

        #Animations
        self.animations = idle_anim + animations
        self.current_anim = idle_anim
        self.current_frame = idle_anim.frame

    def update(self):
        if self.current_anim.animation_finnished:
            self.current_anim.animation_finnished = False
            self.play(0)

    def play(self, anim: Union[str, int]):
        if isinstance(anim, str):
            for i in self.animations:
                    if i == anim:
                        self.current_anim = i
                        self.current_frame = i.frame
                        i.previous_frame_time = pygame.time.get_ticks()
                        i.play()
        else:
            self.current_anim = self.animations[anim]
            self.current_frame = self.animations[anim].frame
            self.animations[anim].previous_frame_time = pygame.time.get_ticks()
            self.animations[anim].play()