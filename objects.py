import pygame
import sprites
import tools
import math
import random

from typing import Union


class Body(pygame.sprite.Sprite):
    def __init__(self, game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, str, None] = None):
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
        if self.update in self.game.update_functions:
            return self.rect.collidepoint(pos)
    
    #Check if Rect is touching Rect
    def is_colliding_with_rect(self, rect: pygame.Rect):
        if self.update in self.game.update_functions:
            return self.rect.colliderect(rect)

    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.sprites.add(self)
        self.game.update_functions.append(self.update)

    #Remove object
    def remove_from_game(self):
        self.ingame = False
        if self in self.game.sprites:
            self.game.sprites.remove(self)
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)


class RigidBody(Body):
    def __init__(self, game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, None] = None, gravity: pygame.Vector2 = pygame.Vector2(0, 980), mass: float = 1, drag: float = 0, deacceleration: float = 0):
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
    
    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.sprites.add(self)
        self.game.update_functions.append(self.update)
        self.game.update_functions.append(self.physics_update)

    #Remove object
    def remove_from_game(self):
        self.ingame = False
        if self in self.game.sprites:
            self.game.sprites.remove(self)
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)
        if self.physics_update in self.game.update_functions:
            self.game.update_functions.remove(self.physics_update)


class ParticleSystem:
    def __init__(self, game,  num_of_particles: int = 10, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: int = 50, color: tuple[int, int, int] = (0, 0, 0), duration: float = 1, looping: bool = False, direction: tuple[int, int] = (0, 360), velocity: float = 5, drag: float = 1):
        self.game = game
        
        #Attributes
        self.num_of_particles = num_of_particles
        self.pos = pos
        self.size = size
        self.color = color
        self.direction = direction
        self.velocity = velocity
        self.looping = looping
        self.drag = drag
        
        #Particles
        self.particles = []
        
        #Timer
        self.timer = tools.Timer(game, time=duration, looping=looping, play_on_start=False, functions=[self.play, self.is_loop_over])
    
    def play(self):
        self.timer.looping = self.looping
        #Restart and Instantiate Particles
        self.stop()
        for i in range(self.num_of_particles):
            instance = RigidBody(game = self.game, pos = self.pos, size = (self.size, self.size), color = self.color, gravity = (0, 0), drag = self.drag)
            particle_dir = math.radians(random.randint(self.direction[0], self.direction[1]))
            instance.velocity = pygame.Vector2(math.cos(particle_dir), math.sin(particle_dir)) * self.velocity
            self.particles.append(instance)
        if self.looping:
            self.timer.start()
            
    def stop(self):
        for i in self.particles:
            i.remove_from_game()
        self.particles = []
            
    def is_loop_over(self):
        if not self.looping:
            self.stop()