import pygame
import tools

from typing import Union

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