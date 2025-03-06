from codequest import *

#Create a Game Instance
game = Game()

turn = "X"
start_pos = Vector2(100, 100)
buttons = []
count = 0
button_size = Vector2(90, 90)

def play(but: ui.Button):
    global turn, count
    if but.label.text == "":
        but.label.text = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    count += 1

for i in range(3):
    l = []
    y_pos = 150 + 100 * i
    for j in range(3):
        x_pos = 150 + 100 * j
        b = ui.Button(game, pos = Vector2(x_pos, y_pos), size=button_size, normal_color=(210, 210, 210), hover_color=(125, 125, 125), clicked_color=(50, 50, 50), text_color=(0, 0, 0), center=True)
        b.on_click(play)
        l.append(b)
    buttons.append(l)

def reset():
    global buttons, count
    for i in buttons:
        for j in i:
            j.label.text = ""
    count = 0
    
@game.on_update
def update():
    global buttons
    for i in buttons:
        count_x = 0
        count_o = 0
        for j in i:
            if j.label.text == "X":
                count_x += 1
            if j.label.text == "O":
                count_o += 1 
        if count_o == 3 or count_x == 3:
            reset()
    
    for i in range(3):
        if buttons[0][i].label.text == buttons[1][i].label.text and buttons[1][i].label.text == buttons[2][i].label.text and (buttons[0][i].label.text == "X" or buttons[0][i].label.text == "O"):
            reset()
    if buttons[0][0].label.text == buttons[1][1].label.text and buttons[0][0].label.text == buttons[2][2].label.text and (buttons[0][0].label.text == "X" or buttons[0][0].label.text == "O"):
        reset()
    if buttons[0][2].label.text == buttons[1][1].label.text and buttons[0][2].label.text == buttons[2][0].label.text and (buttons[2][0].label.text == "X" or buttons[2][0].label.text == "O"):
        reset()
    if count == 9:
        reset()


game.run()