import pygame
import sys

class Game:
    def __init__(
        self,
        name="window",
        width=500,
        height=500,
        background_color=(255, 255, 255),
        fps=60,
    ):
        pygame.init()
        # Screen
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = background_color
        pygame.display.set_caption(name)

        # Settings
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.fps = fps
        
        #Inputs
        self.keys_down = []
        self.keys_up = []
        self.keys_pressed = []


        self.update_functions = []

    def check_events(self):
        self.clock.tick()
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

    def add_update_function(self, func):
        self.update_functions.append(func)

    def on_update(self, func):
        self.add_update_function(func)
        return func

    def update(self):
        self.screen.fill(self.background_color)
        for func in self.update_functions:
            func(self)
        pygame.display.update()

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()
