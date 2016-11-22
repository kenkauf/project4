import pygame
import pygame.mixer

FPS = 30
dimensions = [700, 500]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

class Paddle:
    def __init__(self, screen):
        self.screen = screen

        self.x = 300
        self.y = 470
        self.width = 100
        self.height = 15

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.within_right_bound():
            self.x += 10
        elif self.moving_left and self.within_left_bound():
            self.x -= 10

    def within_right_bound(self):
        return self.x <= 600

    def within_left_bound(self):
        return self.x >= 0

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, [self.x, self.y, self.width, self.height])

pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("My Breakout Game")

												#Call sprite objects here
paddle = Paddle(screen)

													#Events to do during game
done = False
game_over = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = True
        elif event.type == pygame.KEYUP:                     #Needed to stop auto movement
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = False
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = False

    if not game_over:
        paddle.update()
        #update ball and blocks here

    screen.fill(BLACK)

    if not game_over:
        #look for blocks
            #draw blocks here
        paddle.draw()
        # draw ball here

    pygame.display.flip()            # Reference: http://www.pygame.org/docs/ref/display.html
    clock.tick(FPS) 

pygame.quit()