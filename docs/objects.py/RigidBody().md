### RigidBody()

```py
RigidBody(game, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: pygame.Vector2 = pygame.Vector2(50, 50), color: tuple[int, int, int] = (0, 0, 0), image: Union[sprites.Animator, sprites.Animation, None] = None, gravity: pygame.Vector2 = pygame.Vector2(0, 980), mass: float = 1, drag: float = 0, deacceleration: float = 0, center: bool = False)
```

  * **game:** Game instance
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **image:** If given
    * None: renders as a rectangle
    * String: renders the image in the path given
    * Animation: renders the animation given
    * Animator: renders the current animation on the animator
  * **gravity:** Gravity of the body
  * **mass:** Mass of the body
  * **drag:** Opposite force to velocity
  * **deacceleration:** Opposite force to acceleration
  * **center:** If true the body is centered in the position given

## Properties

  * **pos:** Position of the body
  * **color:** Color of the body
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **image:** Image of the body
  * **center:** If true the body is centered in the position given
  * **gravity:** Gravity of the body
  * **mass:** Mass of the body
  * **drag:** Opposite force to velocity
  * **deacceleration:** Opposite force to acceleration

## Callable Functions

  * **set_rotation(angle: float):** Rotates body (to rotate around the center, center should be true)
  * **is_colliding_with_point(pos: pygame.Vector2):** Checks if body is colliding with point given
  * **is_colliding_with_rect(rect: pygame.Rect):** Checks if body is colliding with point given
  * **add_to_game():** Adds body to the game
  * **remove_from_game():** Removes body from the game
  * **add_force(force: pygame.Vector2):** Adds a force to the body

