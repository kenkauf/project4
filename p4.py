import pygame
import pygame.mixer

print("Kennedy Kaufman\n6137103\n\n")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

class Paddle:
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

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
        pygame.draw.rect(self.gameDisplay, GREEN, [self.x, self.y, self.width, self.height])

class Block:
    def __init__(self, gameDisplay, x, y):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y

def clamp(val, minimum, maximum):
    if val < minimum:
        val = minimum
    elif val > maximum:
        val = maximum
    return val
    
class Ball:
    def __init__(self, screen, paddle, impact, laser):
        self.screen = screen
        self.pos = [200, 220]
        self.x_velo = 8
        self.y_velo = 8
        self.radius = 10
        self.paddle = paddle

        self.impact = impact
        self.laser = laser

    def draw(self):
        pygame.draw.circle(self.screen, YELLOW, self.pos, self.radius)

pygame.init()
gameDisplay = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Project 4: Breakout")

#Call sprite objects here
paddle = Paddle(gameDisplay)

#Events to do during game
gameExit = False                 
game_over = False
clock = pygame.time.Clock()
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
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

    gameDisplay.fill(BLACK)

    if not game_over:
        paddle.draw()


    pygame.display.flip()            # Reference: http://www.pygame.org/docs/ref/display.html
    clock.tick(30) 

pygame.quit()