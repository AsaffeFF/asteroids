from logger import log_event
import random
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        x1 = self.velocity.rotate(random_angle)
        x2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = x1 * 1.2
        asteroid2.velocity = x2 * 1.2
        self.kill()