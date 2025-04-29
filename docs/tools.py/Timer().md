# Timer()

```py
Timer(game, time: float = 1, looping: bool = False, functions: Union[list, function] = [], play_on_start: bool = True)
```

  * **game:** Game instance
  * **time:** Cooldown time
  * **looping:** If true loops the timer
  * **functions:** If given
    * List of functions: The functions will trigger once the timer finishes 
    * Function: THe function will trigger once the timer finishes
  * **play_on_start:** If true timer will start when instantiated

## Properties

  * **time:** Cooldown time
  * **looping:** If true loops the timer
  * **playing:** If true, it is playing
  * **current_cooldown:** Time passed since start of iteration
  * **functions:** List of functions that will run when cooldown is up

## Callable Functions

  * **start():** Starts the timer
  * **stop():** Stops the timer
  * **pause():** Pauses the timer
  * **unpause():** Unpauses the timer
  * **add_to_game():** Adds timer to the game
  * **remove_from_game():** Removes timer from the game
