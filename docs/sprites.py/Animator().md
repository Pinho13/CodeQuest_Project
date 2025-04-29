# Animator()

```py
Animator(game, animations: Union[list[Animation], Animation], idle_anim: Animation = None)
```

  * **game:** Game instance
  * **animations:** If given
    * List of animations: Animations in the animator
    * Animation: Makes it the only animation in the animator
  * **idle_anim:** If given
    * Animation: Makes it the idle animation
    * None: makes the idle animation the first animation given in animations

## Propriedades

  * **idle_anim:** The default animation
  * **current_anim:** The current animation
  * **frame:** The current frame
  * **on_anim_finnished:** Stores the functions that run when the animation finishes

## Callable Functions

  * **play(anim: Union[str, int, Animation]):** Plays the animation
  * **remove(anim: Union[str, int, Animation]):** Removes an animation
  * **add_to_game():** Adds animation to the game
  * **remove_from_game():** Removes animation from the game

## Decorators

  * **on_finish(func):** makes the function get called when the animation finishes

```py
@anim.on_finish
def func():
    #code
```