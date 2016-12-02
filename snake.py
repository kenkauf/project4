print("\nKennedy Kaufman\n61371023\n")

#  TURN ON SOUND, super cool background music will help increase scores, its science

#  Snake Game for SI 206 Project 4
#  Use arrow keys to move snake around
#  Eat the red apples and increase your score
#  Don't eat yourself or go outside the boundries
#  final score will be output

#  import modles
import pygame
import random
import pygame.mixer

#  define colors, not all used but there just in case
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
L_GREEN = (127, 191, 63, .3)
YELLOW = (255, 255, 0)
BROWN = (191, 127, 63)
colorlist=(RED, (178, 34, 42), (255, 69, 0))

#  define sizes of objects
sizeOfSnake = 10
obstacleSize = 10

class Snake:
#  create Snake
    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_width() / 2
        #  http://www.pygame.org/docs/ref/surface.html
        self.length = 10
        self.grow_to = 20
        self.xVel = 0
        self.yVel = -10
        self.body = []
        self.head = None
        self.crashed = False
        self.color = BROWN

    def event(self, event):
    #  handle key movement events of a snake instance
        if event.key == pygame.K_UP:
            if self.yVel == 10: 
            	return
            self.xVel = 0
            self.yVel = -10
        elif event.key == pygame.K_DOWN:
            if self.yVel == -10: 
            	return
            self.xVel = 0
            self.yVel = 10
        elif event.key == pygame.K_LEFT:
            if self.xVel == 10: 
            	return
            self.xVel = -10
            self.yVel = 0
        elif event.key == pygame.K_RIGHT:
            if self.xVel == -10: 
            	return
            self.xVel = 10
            self.yVel = 0
        #  http://stackoverflow.com/questions/16183265/how-to-move-sprite-in-pygame


    def move(self):
    	#  Snake movement
        self.x += self.xVel
        self.y += self.yVel
        # if snake touches self, end game
        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))
        self.head = pygame.Rect(self.x, self.y, sizeOfSnake, sizeOfSnake)
        if (self.grow_to > self.length):
            self.length += 10
        #  snake growth

        if (len(self.body) > self.grow_to):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, L_GREEN, (pop[0], pop[1], sizeOfSnake, sizeOfSnake), 0)

        if (len(self.body) > self.length):
            pop = self.body.pop(-1)
            pygame.draw.rect(self.surface, L_GREEN, (pop[0], pop[1], sizeOfSnake, sizeOfSnake), 0)
        #  growth control, stop from growing too long

    def draw(self):
    	#  create a piece of snake
        pygame.draw.rect(self.surface, self.color, (self.head))
        x, y = self.body[-1]
        pygame.draw.rect(self.surface, L_GREEN, (x, y, sizeOfSnake, sizeOfSnake), 0)


    def position(self):
    	#  where snake is at on screen
        return self.x, self.y

    def eat(self):
    	#  if snake eats food, it grows
        self.grow_to += sizeOfSnake

class Apple:
	#  create food on screen
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(10, surface.get_width()-10)
        self.y = random.randint(10, surface.get_height()-10)
        self.rect = pygame.Rect(self.x, self.y, obstacleSize, obstacleSize)
        self.color = random.choice(colorlist)
        #Reference: http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python

    def draw(self):
    	#  draw the apple food
        pygame.draw.rect(self.surface, self.color, (self.rect))

    def position(self):
    	#  find where food is at
        return self.x, self.y

    def check(self, snakesHead):
    	#  see if snake collided with food
        if snakesHead.colliderect(self):
            return True
        else:
            return False

    def erase(self):
    	#  erase food that was ate
        pygame.draw.rect(self.surface, L_GREEN, (self.x, self.y, obstacleSize, obstacleSize), 0)

score = 0
scoreBoard = []
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SI 206, Project 4, Snake, Kennedy Kaufman")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(L_GREEN)
screen.blit(background, (0, 0))
#  make screen
pygame.display.flip()

clock = pygame.time.Clock()
bite = pygame.mixer.Sound("bite.wav")
pygame.mixer.music.load("EDM.mp3")
# while pygame.mixer.music.get_busy(): 
#     pygame.time.Clock().tick(10)
pygame.mixer.music.play(-1)
#  initalize sound for eating
snake = Snake(screen)
food1 = Apple(screen)
#  create sprites
running = True


while running:
    snake.move()
    snake.draw()
    food1.draw()
    #  draw sprites and update

    if snake.crashed:
        running = False
        print("Thanks for playing. Your final score is", score)
        #  end game is snake hits self
    elif snake.x <= 0 or snake.x >= 799:
        running = False
        print("Thanks for playing. Your final score is", score)
        #  end game if snake leaves screen boundaries
    elif snake.y <= 0 or snake.y >= 599:
        running = False
        print("Thanks for playing. Your final score is", score)
    elif food1.check(snake.head):
    	#  when snake eats apple, update score and play sound and erase old apple
        score += 1
        snake.eat()
        bite.play()
        pygame.draw.rect(screen, L_GREEN, (5, 10, 200, 50)) # so score wont overwrite, REF: http://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render(("Score: "+str(score)), 1, BLACK)
        screen.blit(label, (10, 10))
        #  http://www.pygame.org/docs/tut/tom/games2.html
        food1.erase()
        food1 = Apple(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #  endgame
        elif event.type == pygame.KEYDOWN:
            snake.event(event)
            #  while running, move snake during key presses

    pygame.display.flip()
    clock.tick(30)