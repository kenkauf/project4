import pygame

BLACK = (0, 0, 0)
WHITE = (225, 225, 225)

snake_body_w = 15
snake_body_h = 15
snake_body_space = 3

x_change = snake_body_w + snake_body_space
y_change = 0

class Snake(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([snake_body_w, snake_body_h])
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Snake')
allspriteslist = pygame.sprite.Group()

snake_body = []
for i in range(15):
	x = 250-(snake_body_w+snake_body_space)*i
	y = 30
	body = Snake(x, y)
	snake_body.append(body)
	allspriteslist.add(body)  #REFERENCE: http://stackoverflow.com/questions/13851051/how-to-use-sprite-groups-in-pygame

