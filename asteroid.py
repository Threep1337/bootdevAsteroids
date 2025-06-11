from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
       pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        asteroid1_velocity = self.velocity.rotate(rand_angle) * NEW_ASTEROID_VELOCITY_INCREASE
        asteroid2_velocity = self.velocity.rotate(rand_angle * -1) * NEW_ASTEROID_VELOCITY_INCREASE
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid1.velocity = asteroid1_velocity
        new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid2.velocity = asteroid2_velocity