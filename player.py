import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, SHOT_SPEED
from shot import Shot


class Player(CircleShape):
    containers = None

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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        # align shot direction with player
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= SHOT_SPEED

    def draw(self, screen):
        PLAYER_COLOR = (255, 255, 255)
        LINE_WIDTH = 2
        # DEBUG_COLOR = (255, 0, 0)
        # collision bounding box
        # pygame.draw.circle(screen, DEBUG_COLOR, self.position, self.radius, LINE_WIDTH)
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), LINE_WIDTH)

    def update(self, dt):
        # unfortunately this is only working on the lap top keyboard,
        # but not on custom keyboard connected by usb to thunderbolt dock
        # TODO: figure out issue with external keyboard
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
