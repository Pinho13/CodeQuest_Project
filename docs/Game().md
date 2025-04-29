# Game()

```py
Game(name: str = "Window", width: int = 500, height: int = 500, background_color: tuple[int, int, int] = (255, 255, 255), fps: int = 60, show_fps: bool = True)
```

  * **name:** Name of the window
  * **width:** Width of the window
  * **height:** Height of the window
  * **background_color:** Background color
  * **fps:** Max fps
  * **show_fps:** If true shows fps on top of the window

## Properties

  * **width:** Screen width
  * **height:** Screen height
  * **background_color:** Screen background color
  * **name:** Screen title
  * **fps:** Current FPS
  * **show_fps:** Shows FPS if true
  * **update_functions:** Stores the functions that run every frame
  * **delta_time:** Time between every frame

## Callable Functions

  * **run():** Runs the game (should be called at the end of the file)

## Decorators

  * **on_update(func):** makes function get called every frame

```py
@game.on_update
def func():
    #code
```