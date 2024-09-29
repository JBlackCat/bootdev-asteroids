import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_CHILD_SPLITS, ASTEROID_SPLIT_SCALAR


class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        ASTEROID_COLOR = (0, 255, 0)
        LINE_WIDTH = 2
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # smallest asteroid, nothing to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        next_radius = self.radius - ASTEROID_MIN_RADIUS
        children = ASTEROID_CHILD_SPLITS

        for i in range(children):
            angle = split_angle if i % children == 0 else (split_angle * -1)
            child = Asteroid(self.position.x, self.position.y, next_radius)
            child.velocity = self.velocity.rotate(angle) * ASTEROID_SPLIT_SCALAR
