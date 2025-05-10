# Button()

```py
Button(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), normal_image: str = None, hover_image: str = None, clicked_image: str = None, normal_color: tuple[int, int, int] = (0, 0, 0), hover_color: tuple[int, int, int] = None, clicked_color: tuple[int, int, int] = None, text: str = "", text_color: tuple[int, int, int] = (255, 255, 255), center: bool = False)
```

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **normal_image:** Default button image
  * **hover_image:** Image when mouse hovering button
  * **clicked_image:** Image when button clicked
  * **normal_color:** Default button color
  * **hover_color:** Color when mouse hovering button
  * **clicked_color:** Color when button clicked
  * **text:** Button text
  * **center:** If true the body is centered in the position given

##  Properties

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **normal_image:** Default button image
  * **hover_image:** Image when mouse hovering button
  * **clicked_image:** Image when button clicked
  * **normal_color:** Default button color
  * **hover_color:** Color when mouse hovering button
  * **clicked_color:** Color when button clicked
  * **text:** Button text
  * **center:** If true the body is centered in the position given
  * **label:** Text object
  * **hovering:** If true button is being hovered
  * **clicked:** If true button just got clicked
  * **click_cooldown:** Timer with click cooldown

## Callable Functions

  * **add_to_game():** Adds animation to the game
  * **remove_from_game():** Removes animation from the game

## Decorators

  * **on_click(func):** Makes the function get called when button is clicked
  * **on_hover(func):** Makes the function get called when button is hovered
  * **on_unhover(func):** Makes the function get called when button is unhovered

```py
@button.on_click
def func():
    # run when button clicked

@button.on_hover
def func():
    # run when button hovered

@button.on_unhover
def func():
    # run when button unhovered
```