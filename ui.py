import pygame
import sprites
import tools

from typing import Union
from objects import Body

class Text(pygame.sprite.Sprite):
    def __init__(self, game, text: str, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: int = 50, color: tuple[int, int, int] = (0, 0, 0), center: bool = False):
        super().__init__()
        self.game = game

        #Implement it inGame
        game.sprites.add(self)
        game.update_functions.append(self.update)
        self.ingame = True

        #Atributes
        self.pos = pygame.Vector2(pos)
        self.color = color
        self.size = size
        self.text = text
        self.center = center

        #Others
        self.current_size = size

        #Text Creation
        self.text_font = pygame.font.SysFont(None, size)
        self.image = self.text_font.render(text, True, color)
        if center:
            self.rect = self.image.get_rect(center=pos)
        else:
            self.rect = self.image.get_rect(topleft=pos)
    
    def update(self):
        self.check_if_size_changed()
        if self.center:
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.rect = self.image.get_rect(topleft=self.pos)
        self.image = self.text_font.render(self.text, True, self.color)

    def check_if_size_changed(self):
        if self.size != self.current_size:
            self.text_font = pygame.font.SysFont(None, int(self.size))
            self.image = self.text_font.render(self.text, True, self.color)
            self.rect = self.image.get_rect(topleft=self.pos)
            self.current_size = self.size
    
    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.sprites.add(self)
        self.game.update_functions.append(self.update)

    #Remove from rendering and updating
    def remove_from_game(self):
        self.ingame = False
        if self in self.game.sprites:
            self.game.sprites.remove(self)
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)


class Button(Body):
    def __init__(self, game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), normal_image: str = None, hover_image: str = None, clicked_img: str = None, normal_color: tuple[int, int, int] = (0, 0, 0), hover_color: tuple[int, int, int] = None, clicked_color: tuple[int, int, int] = None, text: str = "", text_color: tuple[int, int, int] = (255, 255, 255), center: bool = False):
        super().__init__(game, pos, size, normal_color, normal_image, center)
        self.game = game

        #Implement it inGame
        game.sprites.add(self)
        game.update_functions.append(self.ui_update)

        #Stores Functions for Triggers
        self.__on_click_functions = []
        self.__on_hover_functions = []
        self.__on_unhover_functions = []

        #Image Attributes
        self.normal_image = pygame.image.load(normal_image).convert_alpha() if normal_image != None else normal_image
        self.hover_image = pygame.image.load(hover_image).convert_alpha() if hover_image != None else hover_image
        self.clicked_image = pygame.image.load(clicked_img).convert_alpha() if clicked_img != None else clicked_img

        #Color Attributes
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.label = Text(game,pos=pos+size/2, size=int(self.vec_to_font(text, self.size)), text=text, color=text_color, center=True)

        #Info var
        self.hovering = False
        self.clicked = False

        #Tools
        self.click_cooldown = tools.Timer(game, time=0.1, functions=self.__clicked_var_to_false, play_on_start=False)

    def ui_update(self):
        #Change Text Size
        self.label.size = int(self.vec_to_font(self.label.text, self.size))
        if self.center:
            self.label.pos = self.pos
        else:
            self.label.pos = self.pos + self.size/2

        #Check when mouse hovers
        if not self.hovering and self.is_colliding_with_point(pygame.mouse.get_pos()):
            self.hover()
            if self.hover_image != None:
                self.image = self.hover_image
                self.image = pygame.transform.scale(self.image, self.size)
            elif self.normal_image == None and self.hover_color != None:
                self.color = self.hover_color
        #Check when mouse unhovers
        elif self.hovering and not self.is_colliding_with_point(pygame.mouse.get_pos()):
            self.unhover()
            if self.normal_image != None:
                self.image = self.normal_image
                self.image = pygame.transform.scale(self.image, self.size)
            else:
                self.color = self.normal_color
        
        #Check if mouse is hovering
        self.hovering = self.is_colliding_with_point(pygame.mouse.get_pos())

        #Check if mouse clicked
        if self.hovering and 1 in self.game.mouse_down and not self.clicked:
            if self.clicked_image != None:
                self.image = self.clicked_image
                self.image = pygame.transform.scale(self.image, self.size)
            elif self.normal_image == None and self.clicked_color != None:
                self.color = self.clicked_color
            self.click()
            self.clicked = True
            self.click_cooldown.start()
    
    def click(self):
        for i in self.__on_click_functions:
            if i.__code__.co_argcount == 1:
                i(self)
            else:
                i()
    
    def hover(self):
        for i in self.__on_hover_functions:
            if i.__code__.co_argcount == 1:
                i(self)
            else:
                i()
    
    def unhover(self):
        for i in self.__on_unhover_functions:
            if i.__code__.co_argcount == 1:
                i(self)
            else:
                i()

    def on_click(self, func):
        self.__on_click_functions.append(func)
        return func
    
    def on_hover(self, func):
        self.__on_hover_functions.append(func)
        return func

    def on_unhover(self, func):
        self.__on_unhover_functions.append(func)
        return func
    
    def __clicked_var_to_false(self):
        self.clicked = False
    
    #Add object
    def add_to_game(self):
        self.ingame = True
        self.game.sprites.add(self)
        self.game.update_functions.append(self.update)
        self.game.update_functions.append(self.ui_update)

    #Remove object
    def remove_from_game(self):
        self.ingame = False
        if self in self.game.sprites:
            self.game.sprites.remove(self)
        if self.update in self.game.update_functions:
            self.game.update_functions.remove(self.update)
        if self.ui_update in self.game.update_functions:
            self.game.update_functions.remove(self.ui_update)
    
    #Changes Vector2 Size to FontSize
    def vec_to_font(self, text, vec: pygame.Vector2):
        text_length = len(text)
        if len(text) == 0:
            text_length = 2
        width1 = ((vec.x * 100)/38)/text_length
        height1 = width1 * 1.8
        height2 = ((vec.y * 100)/68)
        if height1 < self.size.y:
            return width1
        else:
            return height2