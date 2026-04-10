import pygame
from pygame.locals import *
import sys
import random
import time

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Part 2

class Raindrop:
    __slots__ = ("x", "y", "radius")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, window):
        pygame.draw.circle(window, BLUE, (self.x, self.y), self.radius, 2)

# Part 1, 3, 4

class RaindropsManager:
    RAIN_RATE = 0.2
    MAX_RADIUS = 20

    def __init__(self):
        self.raindrops = []
        self.last_rain_time = time.time()

    def maybe_add_raindrop(self):
        now = time.time()
        if now - self.last_rain_time >= RaindropsManager.RAIN_RATE:
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            self.raindrops.append(Raindrop(x, y))
            self.last_rain_time = now

    def update_all(self):
        for drop in self.raindrops:
            drop.update()

        self.raindrops = [
            drop for drop in self.raindrops
            if drop.radius <= RaindropsManager.MAX_RADIUS
        ]

    def draw_all(self, window):
        for drop in self.raindrops:
            drop.draw(window)


# Part 1
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

manager = RaindropsManager()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    manager.maybe_add_raindrop()
    manager.update_all()

    window.fill(BLACK)

    manager.draw_all(window)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
