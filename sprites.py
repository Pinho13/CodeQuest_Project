import pygame
import tools

from typing import Union

class Animation:
    def __init__(
        self,
        game,
        name: str,
        animation: Union[list, str],
        time_between_frames: float = 1,
        looping: bool = True,
    ):
        self.game = game

        # Implement it InGame
        self.game.update_functions.append(self.update)
        self.ingame = True

        # Events
        self.on_anim_finnished = []

        # Atributes
        self.name = name
        self.animation = []
        self.time_between_frames = time_between_frames
        self.looping = looping
        self.current_frame_index = 0
        self.animation_finnished = True

        # Load Animation Images
        if isinstance(animation, str):
            animation = tools.get_files_from_dir(animation)
        self.animation = tools.convert_images(animation)
    
        # Current Frame
        self.frame = self.animation[0]

        # Time of Previous Frame
        self.previous_frame_time = pygame.time.get_ticks()
    
    def update(self):
        if not self.animation_finnished:
            self.playing()
        self.frame = self.animation[self.current_frame_index]

    # Method that plays the animation
    def play(self, time_between_frames: float = None, looping: bool = None):
        if looping != None:
            self.looping = looping
        if time_between_frames != None:
            self.time_between_frames = time_between_frames

        self.previous_frame_time = pygame.time.get_ticks()
        self.animation_finnished = False
    
    # Method that cycles through the frame index
    def playing(self):
        if (pygame.time.get_ticks() - self.previous_frame_time)/1000 >= self.time_between_frames and not self.animation_finnished:
            self.current_frame_index += 1
            self.previous_frame_time = pygame.time.get_ticks()
            if self.current_frame_index == len(self.animation)-1:
                if not self.looping:
                    self.animation_finnished = True
            elif self.current_frame_index == len(self.animation):
                # Play all functions from self.on_anim_finnished when animation ends
                for i in self.on_anim_finnished:
                    i()
                self.current_frame_index = 0
    
    # Adds functions to a list that gets called when an animation is finnished
    def on_finish(self, func):
        self.on_anim_finnished.append(func)
        return func
    
    # Add object
    def add_to_game(self):
        self.ingame = True
        self.game.update_functions.append(self.update)

    # Remove from rendering and updating
    def remove_from_game(self):
        self.ingame = False
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)


class Animator:
    def __init__(
        self,
        game,
        animations: Union[list[Animation], Animation],
        idle_anim: Animation = None,
    ):
        self.game = game

        # Implement it InGame
        self.game.update_functions.append(self.update)
        self.ingame = True

        # Events
        self.on_anim_finnished = []

        # Animations
        if type(animations) == Animation:
            animations = [animations]
        idle_anim = animations[0] if idle_anim == None else idle_anim
        self.animations = [idle_anim, ] + animations if idle_anim not in animations else animations
        self.current_anim = idle_anim
        self.frame = idle_anim.frame

        # Play all functions from self.on_anim_finnished when animation ends
        for i in animations:
            i.on_anim_finnished.append(lambda: [i() for i in self.on_anim_finnished])

        self.current_anim.play()

    def update(self):
        self.frame = self.current_anim.frame

    # Plays an animation
    def play(self, anim: Union[str, int, Animation]):
        self.current_anim.animation_finnished = True
        if type(anim) != int:
            for i in self.animations:
                    if i.name == anim or i == anim:
                        self.current_anim = i
                        self.frame = i.frame
                        i.play()
        else:
            self.current_anim = self.animations[anim]
            self.frame = self.animations[anim].frame
            self.animations[anim].play()
    
    # Adds functions to a list that gets called when an animation is finnished
    def on_finnish(self, func):
        self.on_anim_finnished.append(func)
        return func
    
    # Remove Animation
    def remove(self, anim: Union[str, int, Animation]):
        if type(anim) == Animation:
            self.animations.remove(anim)
        elif type(anim) == str:
            buffer = None
            for i in self.animations:
                if i.name == anim:
                    buffer = i
            if buffer != None:
                self.animations.remove(buffer)
        else:
            del self.animations[anim]

    # Add object
    def add_to_game(self):
        self.ingame = True
        self.game.update_functions.append(self.update)

    # Remove from rendering and updating
    def remove_from_game(self):
        self.ingame = False
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)
    