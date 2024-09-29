import pygame
from circleshape import CircleShape
from constants import SHOT_COLOR, SHOT_LINE_WIDTH


# Bullet Specs:
#  - Are small circles
#  - Move at a constant speed in a straight line
#  - Split up asteroids when they collide with them
#  - Are spawned by player input and move in the direction the player is facing
class Shot(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, SHOT_COLOR, self.position, self.radius, SHOT_LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
