import pygame
from random import randint

print("\nKennedy Kaufman\n\n61371023")

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
RED = (255,0,0)

snake_body_w = 15
snake_body_h = 15
snake_body_space = 3

x_change = snake_body_w + snake_body_space
y_change = 0

score = 0

class Snake(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.pos = [200, 220]

		self.image = pygame.Surface([snake_body_w, snake_body_h])
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def out_of_bounds(self):

		if self.rect.x > 600 or self.rect.y > 800 or self.rect.x < 0 or self.rect.y < 0:
			game_over = True
			print("Knows OOB")

	def update(self):

		self.pos[0] = self.rect.x
		self.pos[1] = self.rect.y 

		if self.out_of_bounds():
			game_over=True

FoodX = 10*randint(0,800/10-1)
FoodY = 10*randint(0,600/10-1)
Food = pygame.Surface((10,10))
Food.fill(RED)

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Snake')
allspriteslist = pygame.sprite.Group()

snake_body = []
for i in range(3):
	x = 250-(snake_body_w+snake_body_space)*i
	y = 30
	body = Snake(x, y)
	snake_body.append(body)
	allspriteslist.add(body)  #REFERENCE: http://stackoverflow.com/questions/13851051/how-to-use-sprite-groups-in-pygame

clock = pygame.time.Clock()
game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = (snake_body_w + snake_body_space) * -1
				y_change = 0
			if event.key == pygame.K_RIGHT:
				x_change = (snake_body_w + snake_body_space)
				y_change = 0
			if event.key == pygame.K_UP:
				x_change = 0
				y_change = (snake_body_h + snake_body_space) * -1
			if event.key == pygame.K_DOWN:
				x_change = 0
				y_change = (snake_body_h + snake_body_space)

	old_body = snake_body.pop()
	allspriteslist.remove(old_body)

	x = snake_body[0].rect.x + x_change
	y = snake_body[0].rect.y + y_change
	body = Snake(x, y)

	snake_body.insert(0, body)
	allspriteslist.add(body)

	screen.fill(BLACK)
	allspriteslist.draw(screen)
	clock.tick(5)
	screen.blit(Food, (FoodX, FoodY))
	pygame.display.flip()          # Reference: http://www.pygame.org/docs/ref/display.html


pygame.quit()