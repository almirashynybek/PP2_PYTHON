import pygame
pygame.init()

size = width, height = 800, 600
speed = 20
white = (255, 255, 255)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

flLeft = flRight = False
flUp = flDown = False
clock = pygame.time.Clock()
FPS = 60

x = width // 2
y = height // 2



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                flLeft = False
            elif event.key == pygame.K_RIGHT:
                flRight = False
            elif event.key == pygame.K_UP:
                flUp = False
            elif event.key == pygame.K_DOWN:
                flDown = False
                
    if flLeft:
        x -= speed
    elif flRight:
        x += speed
    elif flUp:
        y -= speed
    elif flDown:
        y += speed
    
    if x < 0:
        x = 0
    elif x > width:
        x = width
    elif y < 0:
        y = 0
    elif y > height:
        y = height
    
    
    screen.fill(white)
    cr = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()

    clock.tick(FPS)
