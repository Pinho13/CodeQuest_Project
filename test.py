from codequest import *
import random

game = Game()

points = ui.Text(game, "0")
score = 0
bodies = []

button = ui.Button(game, normal_color=(100, 100, 100), hover_color=(50, 50, 50), clicked_color=(0, 0, 0))

def create_body():
    global bodies
    bodies.append(objects.Body(game, pos= Vector2(random.randint(0, game.width-100), random.randint(0, game.height-100))))

#timer = tools.Timer(game, 2, True, create_body)


@game.on_update
def update():
    global score
    points.text = str(score)
    for i in bodies:
        if i.is_colliding_with_point(pygame.mouse.get_pos()):
            i.remove_from_game()
            score += 1
            #timer.time -= 0.1

game.run()