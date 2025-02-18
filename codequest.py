import pygame
import sys

class Game:
    def __init__(self, name="window", width=500, height=500, background_color = (255, 255, 255), fps = 60):
        pygame.init()
        #Screen
        self.screen = pygame.display.set_mode((width, height))
        self.background_color = background_color
        pygame.display.set_caption(name)
        
        #Settings
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.fps = fps
        
        #Inputs
        keys_down = []

        #Make it run
        self.run()

    def check_events(self):
        global keys_down
        self.clock.tick()
        self.events = pygame.event.get()

        #Restart Inputs
        keys_down = []

        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys_down.append(event.key)

    def update(self):
        self.screen.fill(self.background_color)
        pygame.display.update()

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()