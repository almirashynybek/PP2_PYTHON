import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
w = 1000
h = 800

screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("Paint")

def draw_menu():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100])
    pygame.draw.line(screen, 'black', (0, 100), (w, 100), 3)
    pygame.draw.rect(screen, 'blue', [20,20, 60, 60])
    pygame.draw.circle(screen, 'red', (140, 50), 35)
    pygame.draw.polygon(screen, 'purple', ((200,80),(250,20),(300,80)))

    blue = pygame.draw.rect(screen, (0,0,255), [w - 50, 15, 35, 35])
    red = pygame.draw.rect(screen, (255,0,0), [w - 50, 55, 35, 35])
    green = pygame.draw.rect(screen, (0,255,0), [w - 90, 15, 35, 35])
    yellow = pygame.draw.rect(screen, 'yellow', [w - 90, 55, 35, 35])
    orange = pygame.draw.rect(screen, 'orange', [w - 130, 15, 35, 35])
    purple = pygame.draw.rect(screen, 'purple', [w - 130, 55, 35, 35])
    white = pygame.draw.rect(screen, 'white', [w - 170, 15, 35, 35])
    brown = pygame.draw.rect(screen, 'brown', [w - 170, 55, 35, 35])
    color_rect = [blue, red, green, yellow, orange, purple, white, brown]
    
run = True
while run:
    timer.tick(fps)
    screen.fill('white')

    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()