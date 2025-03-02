import pygame

class Sound:
    def __init__(self, sound: str, volume: float = 1):
        self.sound = pygame.mixer.Sound(sound)
        self.sound.set_volume(volume)
    
    def set_volume(self, volume: float):
        self.sound.set_volume(volume)
    
    def play(self):
        self.sound.play()
    
    def stop(self):
        self.sound.stop()