print("\nKennedy Kaufman\n61371023")

#import modles
import pygame
import random
import pygame.mixer

#define colors
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
L_GREEN = (127, 191, 63)
YELLOW = (255, 255, 0)
ROTTEN_BROWN = (191, 127, 63)
colorlist=(RED, GREEN, YELLOW, L_GREEN, ROTTEN_BROWN)

#define sizes of sprites
pieceSize = 10
sizeOfSnake = 10
obstacleSize = 10

class Snake:
#create Snake
    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_width() / 2
        # http://www.pygame.org/docs/ref/surface.html
        self.length = pieceSize
        self.grow_to = pieceSize*2
        self.xVel = 0
        self.yVel = -pieceSize
        self.body = []
        self.head = None
        self.crashed = False
        self.color = WHITE

    def event(self, event):
    	#for events that move the snake
    	# key = pygame.key.get_pressed()
    	# dist = 1
    	# if key[pygame.K_DOWN]:
    	# 	self.y += dist
    	# elif key[pygame.K_UP]:
    	# 	self.y -= dist
    	# if key[pygame.K_RIGHT]:
    	# 	self.x += dist
    	# elif key[pygame.K_LEFT]:
    	# 	self.x -+ dist
        if event.key == pygame.K_UP:
            if self.yVel == pieceSize: return
        # http://stackoverflow.com/questions/18669836/is-it-possible-to-write-single-line-return-statement-with-if-statement
            self.xVel = 0
            self.yVel = -pieceSize
        elif event.key == pygame.K_DOWN:
            if self.yVel == -pieceSize: return
            self.xVel = 0
            self.yVel = pieceSize
        elif event.key == pygame.K_LEFT:
            if self.xVel == pieceSize: return
            self.xVel = -pieceSize
            self.yVel = 0
        elif event.key == pygame.K_RIGHT:
            if self.xVel == -pieceSize: return
            self.xVel = pieceSize
            self.yVel = 0
        # http://stackoverflow.com/questions/16183265/how-to-move-sprite-in-pygame


    def move(self):
    	#Snake movement
        self.x += self.xVel
        self.y += self.yVel
        #what happens if snake touches self
        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))
        self.head = pygame.Rect(self.x, self.y, sizeOfSnake, sizeOfSnake)
        #how big snake will grow
        if (self.grow_to > self.length):
            self.length += pieceSize
        #growth control, stop from growing too long
        if (len(self.body) > self.grow_to):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (pop[0], pop[1], sizeOfSnake, sizeOfSnake), 0)

        if (len(self.body) > self.length):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (pop[0], pop[1], sizeOfSnake, sizeOfSnake), 0)

    def draw(self):
    	#create a piece of snake
        pygame.draw.rect(self.surface, self.color, (self.head))
        x, y = self.body[-1]
        pygame.draw.rect(self.surface, BLACK, (x, y, sizeOfSnake, sizeOfSnake), 0)


    def position(self):
    	#where snake is at on screen
        return self.x, self.y

    def eat(self):
    	#it snake eats food, it grows
        self.grow_to += pieceSize

class Apple:
	#create food on screen
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(10, surface.get_width()-10)
        self.y = random.randint(10, surface.get_height()-10)
        #places food randomly
        self.rect = pygame.Rect(self.x, self.y, obstacleSize, obstacleSize)
        self.color = random.choice(colorlist)

    def draw(self):
    	#draw the apple food
        pygame.draw.rect(self.surface, self.color, (self.rect))

    def position(self):
    	#find where food is at
        return self.x, self.y

    def check(self, snakesHead):
    	#see if snake collided with food
        if snakesHead.colliderect(self):
            return True
        else:
            return False

    def erase(self):
    	#erase food that was ate
        pygame.draw.rect(self.surface, BLACK, (self.x, self.y, obstacleSize, obstacleSize), 0)

screen = pygame.display.set_mode((800, 600))
#make screen
clock = pygame.time.Clock()

score = 0
pygame.mixer.init()
impact = pygame.mixer.Sound("sounds/impact.wav")
#initalize sound for eating
snake = Snake(screen)
food1 = Apple(screen)
#create sprites
running = True
#Game is running


while running:
    snake.move()
    snake.draw()
    food1.draw()
    pygame.init()
    #draw sprites and update

    if snake.crashed:
        running = False
        #end game is snake hits self
    elif snake.x <= 0 or snake.x >= 799:
        running = False
        #if snake leaves screen boundaries
    elif snake.y <= 0 or snake.y >= 599:
        running = False
    elif food1.check(snake.head):
    	#when snake eats apple, update score and play sound and erase old apple
        score += 1
        snake.eat()
        impact.play()
        pygame.draw.rect(screen, BLACK, (5, 10, 200, 50)) # so score wont overwrite
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render(("Score: "+str(score)), 1, WHITE)
        screen.blit(label, (10, 10))
        #pygame.display.flip()
        # http://www.pygame.org/docs/tut/tom/games2.html
        food1.erase()
        food1 = Apple(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #endgame
        elif event.type == pygame.KEYDOWN:
            snake.event(event)
            #while running, move snake during key presses

    pygame.display.flip()
    clock.tick(30)