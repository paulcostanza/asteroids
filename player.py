import pygame as p
from  circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # player is a triangle
    # but there hitbox is a circle
    def triangle(self):
        forward = p.Vector2(0, 1).rotate(self.rotation)
        right = p.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        p.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = p.key.get_pressed()

        # left
        if keys[p.K_a]:
            self.rotate(dt * -1)

        if keys[p.K_LEFT]:
            self.rotate(dt * -1)

        # right
        if keys[p.K_d]:
            self.rotate(dt)
        
        if keys[p.K_RIGHT]:
            self.rotate(dt)
