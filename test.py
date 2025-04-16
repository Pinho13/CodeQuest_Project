from codequest import *

#Create a Game Instance
game = Game()
obj = objects.Body(game, (100, 100), center = True)

center = Vector2(obj.pos.x + obj.size.x/2, obj.pos.y + obj.size.y/2)
mouse_pos = pygame.mouse.get_pos()

@game.on_update
def update():
    mouse_pos = Vector2(pygame.mouse.get_pos())
    center = Vector2(obj.pos.x + obj.size.x/2, obj.pos.y + obj.size.y/2)
    vec = Vector2(mouse_pos.x-center.x, mouse_pos.y-center.y)
    obj.set_rotation(tools.get_vector_angle(vec))

game.run()