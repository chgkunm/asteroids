# asteroids

Asteroids is my second [Boot.dev](https://www.boot.dev) project!
It is a small game to understand and implement OOPs.

Game Logic:

- player ship: triangle spaceship with a circle hitbox;

  - player can move and rotate the ship;
  - if player ship and any asteroid collide, it is a immediate game over;
  - player can shoot round bullets which damage/destroy the asteroids.

- asteroids: large, medium and small asteroids;

  - the asteroids are spawned beyond the screen, of random size;
  - after being hit by a bullet large splits into two medium, medium splits into two small, and small are destroyed;
  - after being split, the asteroids move in random direction.

- The collision mechanic is simple.

  - If the distance between the center of the two circle objects is greater the sum of the radii, then there is no collision.
  - If the distance is smaller than the sum, then there is a collision between the two objects.
