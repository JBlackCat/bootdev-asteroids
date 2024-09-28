import pygame
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        print(f"PLAYER_INIT")
        print(f"PLAYER_X: {self.position[0]}")
        print(f"PLAYER_Y: {self.position[1]}")

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        PLAYER_COLOR = (255, 255, 255)
        LINE_WIDTH = 2
        # DEBUG_COLOR = (255, 0, 0)
        # collision bounding box
        # pygame.draw.circle(screen, DEBUG_COLOR, self.position, self.radius, LINE_WIDTH)
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), LINE_WIDTH)
