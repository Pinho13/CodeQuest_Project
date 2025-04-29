# ParticleSystem()

```py
ParticleSystem(game, num_of_particles: Union[int, tuple] = 10, pos: pygame.Vector2 = pygame.Vector2(0, 0), size: Union[int, tuple] = 50, color: Union[list, tuple[int, int, int]] = (0, 0, 0), duration: Union[float, tuple] = 1, looping: bool = False, direction: tuple[int, int] = (0, 360), velocity: Union[float, tuple] = 5, drag: Union[float, tuple] = 1)
```

  * **game:** Game instance
  * **num_of_particles:** If given
    * Int: Creates a fix number of particles
    * Tuple: Creates a random number of particles between those two values
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **duration:** If given
    * Float: Particles live for that fixed duration
    * Tuple: Particles live for a random period between those two values
  * **looping:** If true the effect keeps looping
  * **direction:** Direction range where the particles will go
  * **velocity:** If given
    * Float: Particles have fixed velocity
    * Tuple: Particles have a random velocity between those two values
  * **drag:** If given
    * Float: Particles have fixed drag
    * Tuple: Particles have a random drag between those two values

## Properties

  * **num_of_particles:** If given
    * Int: Creates a fix number of particles
    * Tuple: Creates a random number of particles between those two values
  * **pos:** Position of the body
  * **size:** Size of the body
  * **color:** Color of the body
  * **duration:** If given
    * Float: Particles live for that fixed duration
    * Tuple: Particles live for a random period between those two values
  * **looping:** If true the effect keeps looping
  * **direction:** Direction range where the particles will go
  * **velocity:** If given
    * Float: Particles have fixed velocity
    * Tuple: Particles have a random velocity between those two values
  * **drag:** If given
    * Float: Particles have fixed drag
    * Tuple: Particles have a random drag between those two values
  * **particles:** List of body particles on game
  * **timer:** Timer instance that times the event

## Callable Functions

  * **play():** Activates particle system
  * **stop():** Deactivates particle system
  * **destroy_particle(particles: list):** Destroys some particles from the particle system
