import pygame
import os

#Returns a list of all the files from a directory
def get_files_from_dir(dir: str):
    return [dir + "/" + x for x in os.listdir(dir)]

#Return a list of images loaded from a list of files
def convert_images(self, anim: list):
        buffer = []
        for i in anim:
            buffer.append(pygame.image.load(i).convert_alpha())
        
        return buffer