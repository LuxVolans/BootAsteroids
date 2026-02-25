import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt