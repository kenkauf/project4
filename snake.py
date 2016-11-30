print("\nKennedy Kaufman\n\n61371023")

#import modles
import pygame
import random

#define colors
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#define sizes of sprites
pieceSize = 10
sizeOfWorm = 10
obstacleSize = 10

class Worm:

    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_width() / 2
        # http://www.pygame.org/docs/ref/surface.html
        self.length = pieceSize
        self.grow_to = pieceSize*2
        self.vx = 0
        self.vy = -pieceSize
        self.body = []
        self.head = None
        self.crashed = False
        self.color = WHITE

    def event(self, event):
        if event.key == pygame.K_UP:
            if self.vy == pieceSize: return
            self.vx = 0
            self.vy = -pieceSize
        elif event.key == pygame.K_DOWN:
            if self.vy == -pieceSize: return
            self.vx = 0
            self.vy = pieceSize
        elif event.key == pygame.K_LEFT:
            if self.vx == pieceSize: return
            self.vx = -pieceSize
            self.vy = 0
        elif event.key == pygame.K_RIGHT:
            if self.vx == -pieceSize: return
            self.vx = pieceSize
            self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))
        self.head = pygame.Rect(self.x, self.y, sizeOfWorm, sizeOfWorm)

        if (self.grow_to > self.length):
            self.length += pieceSize

        if (len(self.body) > self.grow_to):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (pop[0], pop[1], sizeOfWorm, sizeOfWorm), 0)

        if (len(self.body) > self.length):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (pop[0], pop[1], sizeOfWorm, sizeOfWorm), 0)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.head))
        x, y = self.body[-1]
        pygame.draw.rect(self.surface, BLACK, (x, y, sizeOfWorm, sizeOfWorm), 0)

    def position(self):
        return self.x, self.y

    def eat(self):
        self.grow_to += pieceSize



    pygame.display.flip()
    clock.tick(30)