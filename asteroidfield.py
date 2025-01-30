import pygame as p
import random as r
from asteroid import Asteroid
from constants import *


class AsteroidField(p.sprite.Sprite):
    edges = [
        [
            p.Vector2(1, 0),
            lambda y: p.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            p.Vector2(-1, 0),
            lambda y: p.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            p.Vector2(0, 1),
            lambda x: p.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            p.Vector2(0, -1),
            lambda x: p.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        p.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = r.choice(self.edges)
            speed = r.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(r.randint(-30, 30))
            position = edge[1](r.uniform(0, 1))
            kind = r.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)