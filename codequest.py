print("CodeQuest Repository Here: https://github.com/Pinho13/CodeQuest_Project")
import pygame
import sys
import objects
import tools
import sprites
import ui

from pygame import Vector2

class Game:
    def __init__(
        self,
        name: str ="Window",
        width: int =500,
        height: int =500,
        background_color: tuple[int, int, int] =(255, 255, 255),
        fps: int =60,
        show_fps: bool = True,
    ):
        pygame.init()
        # Screen
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = background_color
        self.name = name
        pygame.display.set_caption(name)

        # Settings
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.fps = fps
        self.show_fps = show_fps

        #Inputs
        self.keys_down = []
        self.keys_up = []
        self.keys_pressed = []

        #Stores functions that run every frame
        self.update_functions = []

        #Stores sprites
        self.sprites = pygame.sprite.Group()

        #Usefull Variables
        self.delta_time = self.clock.tick(self.fps)

    def check_events(self):
        self.delta_time = self.clock.tick(self.fps)/1000
        self.events = pygame.event.get()

        #Restart Inputs
        self.keys_down = []
        self.keys_up = []
    
        for event in self.events:
            #QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #KEYDOWN event
            if event.type == pygame.KEYDOWN:
                self.keys_down.append(event.key)
                self.keys_pressed.append(event.key)
            
            #KEYUP event
            if event.type == pygame.KEYUP:
                self.keys_up.append(event.key)
                self.keys_pressed.remove(event.key)
            # print(event.dict)

    def on_update(self, func):
        self.update_functions.append(func)
        return func

    def update(self):
        self.screen.fill(self.background_color)
        self.sprites.draw(self.screen)
        for func in self.update_functions:
            func()
        
        if self.show_fps:
            pygame.display.set_caption(self.name + " - " + str(int(self.clock.get_fps())))
        pygame.display.update()

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()