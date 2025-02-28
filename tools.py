import pygame
import os

from typing import Union

#Returns a list of all the files from a directory
def get_files_from_dir(dir: str):
    return [dir + "/" + x for x in os.listdir(dir)]

#Return a list of images loaded from a list of files
def convert_images(anim: list):
        buffer = []
        for i in anim:
            buffer.append(pygame.image.load(i).convert_alpha())
        
        return buffer


class Timer:
    def __init__(self, game, time: float = 1, looping: bool = False, functions: Union[list] = [], play_on_start: bool = True):
        self.game = game

        #Implement it InGame
        self.game.update_functions.append(self.update)

        #Atributes
        if type(functions) != list:
            self.functions = [functions]
        else:
            self.functions = functions
        self.time = time
        self.looping = looping
        
        #Info Variables
        self.playing = play_on_start

        #Auxiliary
        self.current_cooldown = 0
    
    def update(self):
        #Add time to cooldown
        if self.playing:
            self.current_cooldown += self.game.delta_time
        
        #Calling the functions after cooldown
        if self.current_cooldown >= self.time:
            self.current_cooldown = 0
            for i in self.functions:
                  i()
            if not self.looping:
                self.playing = False
    
    #Start timer
    def start(self, time: int = None):
        if time == None:
            time = self.time
        self.current_cooldown = 0
        self.playing = True

    #Stop timer
    def stop(self):
        self.current_cooldown = 0
        self.playing = False

    #Pause timer
    def pause(self):
        self.playing = False

    #Unpause timer
    def unpause(self):
        self.playing = True
    
    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.update_functions.append(self.update)

    #Remove object
    def remove_from_game(self):
        self.ingame = False
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)
