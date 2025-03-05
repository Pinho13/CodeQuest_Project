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
        self.pos = pygame.Vector2(pos)
        self.color = color
        self.size = pygame.Vector2(size)

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
        self.gravity = pygame.Vector2(gravity)
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
    def __init__(self, game,  num_of_particles: Union[int, tuple] = 10, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: Union[int, tuple] = 50, color: Union[list, tuple[int, int, int]] = (0, 0, 0), duration: Union[float, tuple] = 1, looping: bool = False, direction: tuple[int, int] = (0, 360), velocity: float = 5, drag: float = 1):
        self.game = game
        
        #Attributes
        self.num_of_particles = num_of_particles
        self.pos = pygame.Vector2(pos) if type(pos) == pygame.Vector2 else pos
        self.size = size
        self.color = color
        self.direction = direction
        self.velocity = velocity
        self.looping = looping
        self.drag = drag
        
        #Particles
        self.particles = []
        
        #Timer
        self.timer = tools.Timer(game, time=duration, looping=looping, play_on_start=False, functions=[self.play])
    
    def play(self):
        self.timer.looping = self.looping
        particles = []
        for i in range(self.param_in_interval(self.num_of_particles)):
            #Get the particle Size
            size = self.param_in_interval(self.size)
            #Instantiate Particle
            instance = RigidBody(game = self.game, pos = self.param_in_interval(self.pos), size = (size, size), color = self.param_in_interval(self.color), gravity = (0, 0), drag = self.param_in_interval(self.drag))
            #Find Direction and add Force
            particle_dir = math.radians(random.randint(self.direction[0], self.direction[1]))
            instance.velocity = pygame.Vector2(math.cos(particle_dir), math.sin(particle_dir)) * self.param_in_interval(self.velocity)
            #Add to List
            particles.append(instance)
        self.particles += particles
        #Add Destroy Timer
        destroy_timer = tools.Timer(self.game, time = self.timer.time, functions=(lambda: self.destroy_particle(particles)))
        destroy_timer.functions.append(destroy_timer.remove_from_game)
        if self.looping:
            self.timer.start()
            
    def stop(self):
        for i in self.particles:
            i.remove_from_game()
        self.particles = []
        self.timer.stop()
    
    #This receives a parameter and if it is a tuple it outputs a random number between the range given
    def param_in_interval(self, param: Union[int, tuple, list]):
        if type(param) == int or type(param) == pygame.Vector2:
            return param
        elif type(param) == tuple and len(param) == 2:
            i, j = param
            if type(i) == pygame.Vector2:
                return pygame.Vector2(random.randint(int(i.x), int(j.x)), random.randint(int(i.y), int(j.y)))
            elif type(j) == float:
                return random.randrange(i, j)
            elif type(j) == int:
                return random.randint(i, j)
        else:
            return param[random.randint(0, len(param)-1)]

    def destroy_particle(self, particles: list):
        for particle in particles:
            particle.remove_from_game()
            if particle in self.particles:
                self.particles.remove(particle)