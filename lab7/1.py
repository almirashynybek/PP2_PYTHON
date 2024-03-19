import pygame
from datetime import datetime

pygame.init() 
SCREEN_WIDTH = 830
SCREEN_HEIGHT = 835
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load('main-clock.png')
BG_WIDTH = 500
BG_HEIGHT = 500
BG_X_POS = (SCREEN_WIDTH / 2 - BG_WIDTH / 2)
BG_Y_POS = (SCREEN_HEIGHT / 2 - BG_HEIGHT / 2)

big_arrow1 = pygame.image.load('left-hand.png')
big_arrow2 = pygame.image.load('right-hand.png')
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.13
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pygame.transform.scale(big_arrow1, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))
big_arrow = pygame.transform.scale(big_arrow2, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER


running = True
while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  angle1 = datetime.now().second * -6
  angle2 = datetime.now().minute * -6

  screen.fill(WHITE)
  screen.blit(bg, (0, 0))

  rotated_big_arrow1 = pygame.transform.rotate(big_arrow1, angle1)
  rotated_big_arrow2 = pygame.transform.rotate(big_arrow2, angle2)

  rotated_big_arrow_rect1 = rotated_big_arrow1.get_rect()
  rotated_big_arrow_rect2 = rotated_big_arrow2.get_rect()

  rotated_big_arrow_rect1.center = big_arrow_rect.center
  rotated_big_arrow_rect2.center = big_arrow_rect.center

  screen.blit(rotated_big_arrow1, rotated_big_arrow_rect1)
  screen.blit(rotated_big_arrow2, rotated_big_arrow_rect2)
  
  # Screen updating
  pygame.display.flip()
  clock.tick(FPS)