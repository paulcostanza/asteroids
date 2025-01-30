import pygame as p

# Base class for game objects: asteroids and player
class CircleShape(p.sprite.Sprite):
    def __init__(self, x, y, radius):

        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = p.Vector2(x, y)
        self.velocity = p.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_detection(self, another_circle):
        distance = p.math.Vector2.distance_to(self.position, another_circle.position)
        
        if distance <= self.radius:
            return True

        return False