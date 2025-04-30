# Animation()

```py
Animation(game, name: str, animation: Union[list, str], time_between_frames: float = 1, looping: bool = True)
```

  * **game:** Game instance
  * **name:** Animation name
  * **animation:** If given
    * List of strings: Makes an animation from the sprites in the paths given in the list
    * String: Makes an animation from the sprites in the path given
  * **time_between_frames:** Time between each frame
  * **looping:** Loops animation if true

## Properties

  * **name:** Animation name
  * **time_between_frames:** Time between each frame
  * **looping:** Loops animation if true
  * **frame:** Current frame
  * **on_anim_finnished:** Stores the functions that run when the animation finishes

## Callable Functions

  * **play(time_between_frames: float = None, looping: bool = None):** Plays animation
  * **add_to_game():** Adds animation to the game
  * **remove_from_game():** Removes animation from the game

## Decorators

  * **on_finish(func):** makes the function get called when the animation finishes

```py
@anim.on_finish
def func():
    # code
```