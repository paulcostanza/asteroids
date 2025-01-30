import pygame as p
import random as r
from  circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        p.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):

        # destroyes current size of asteroid
        self.kill()

        # spawn smaller versions here
        if self.radius > ASTEROID_MIN_RADIUS: 
            random_angle = r.uniform(20, 50)

            angle_a = self.velocity.rotate(random_angle)
            angle_b = self.velocity.rotate(random_angle * -1)

            # calculate smaller size
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # new smaller asteroid
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = angle_a * 1.2

            # another new smaller asteroid
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = angle_b * 1.2

        return 