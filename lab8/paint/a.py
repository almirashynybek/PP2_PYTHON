import pygame, random, math
pygame.init()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
POWDERBLUE = (176, 224, 230, 255)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)


def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

    
def main(): 
    screen = pygame.display.set_mode((1000, 700)) 
    pygame.display.set_caption('paint') 
    icon = pygame.image.load('icon.png') 
    pygame.display.set_icon(icon) 
 
    pygame.draw.rect(screen, SHADOW, (900, 0, 900, 700)) 
    pygame.draw.line(screen, GREY, (904, 0), (904, 700), 3) 
    pygame.draw.line(screen, GREY, (1, 0), (1, 700), 3) 
    pygame.draw.line(screen, GREY, (0, 698), (1000, 698), 3) 
    pygame.draw.line(screen, GREY, (0, 1), (1000, 1), 3) 
    pygame.draw.line(screen, GREY, (998, 0), (998, 700), 3) 
 
    font = pygame.font.SysFont("Verdana", 20) 
    tools_txt = font.render('Tools:', True, BLACK) 
 
    screen.blit(tools_txt, (910, 119)) 
    pygame.draw.rect(screen, GREY, (910, 145, 80, 120), 2) 
    pygame.draw.line(screen, GREY, (950, 145), (950, 225), 2) 
    pygame.draw.line(screen, GREY, (910, 185), (990, 185), 2) 
    pygame.draw.line(screen, GREY, (910, 225), (990, 225), 2) 
    pygame.draw.line(screen, GREY, (0, 697), (900, 697), 2) 
 
    brush_png = pygame.transform.scale(pygame.image.load("brush.png"), (20, 20)) 
    eraser_png = pygame.transform.scale(pygame.image.load("eraser.png"), (20, 20)) 
    clear_png = pygame.transform.scale(pygame.image.load("clear.png"), (30, 30)) 
 
    pygame.draw.rect(screen, BLACK, (918, 197, 25, 15), 2) 
    pygame.draw.circle(screen, BLACK, (970, 205), 9, 2) 
 
    screen.blit(clear_png, (936, 230)) 
    screen.blit(brush_png, (920, 156)) 
    screen.blit(eraser_png, (960, 158)) 
    colors_txt = font.render('Colors:', True, BLACK) 
    screen.blit(colors_txt, (910, 450)) 
    pygame.draw.rect(screen, GREY, (925, 485, 50, 175), 2) 
    clr_list = [RED, ORANGE, YELLOW, GREEN, POWDERBLUE, BLUE, PURPLE, BLACK] 
    clr_rect_list = [] 
    for cl, i in enumerate(range(485, 685, 25), 0): 
        pygame.draw.rect(screen, clr_list[cl], (925, i, 50, 25)) 
        clr_rect_list.append(pygame.Rect((925, i, 50, 25))) 
 
    rect_button = pygame.Rect(912, 187, 38, 38) 
    circle_button = pygame.Rect(952, 187, 38, 38) 
    brush = pygame.Rect((912, 147, 38, 38)) 
    eraser = pygame.Rect((952, 147, 38, 38)) 
    clear = pygame.Rect((912, 227, 78, 38)) 
 
    draw_surf = pygame.Surface((900, 694)) 
    draw_surf.fill(WHITE) 
    screen.blit(draw_surf, (3, 3)) 
 
    mode = 'none' 
    draw_on = False 
    last_pos = (0, 0) 
    color = (255, 128, 0) 
    radius = 5 
    thickness = 2 
 
    def mode_check(mode, color): 
        if mode == 'none': 
            return WHITE 
 
        if mode == 'brush': 
            return color 
        elif mode == 'rect' or mode == 'circle': 
            return color 
        elif mode == 'eraser': 
            return WHITE 
 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                return 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                x, y = event.pos 
 
                if brush.collidepoint(x, y):
                    radius = 10
                    if mode != 'brush':
                        color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        mode = 'brush'

 
                if eraser.collidepoint(x, y): 
                    radius = 10 
                    if mode != 'eraser': 
                        mode = 'eraser' 
                        color = WHITE 
 
                if rect_button.collidepoint(x, y): 
                    if mode != 'rect': 
                        color = (random.randrange(256), random.randrange(256), random.randrange(256)) 
                        mode = 'rect' 
 
                if circle_button.collidepoint(x, y): 
                    if mode != 'circle': 
                        color = (random.randrange(256), random.randrange(256), random.randrange(256)) 
                        mode = 'circle' 
 
                if clear.collidepoint(x, y): 
                    draw_surf.fill(WHITE) 
                    screen.blit(draw_surf, (3, 3)) 
 
                if mode == 'brush' or mode == 'rect' or mode == 'circle': 
                    for i, col in enumerate(clr_rect_list, 0): 
                        if col.collidepoint(x, y): 
                            color = clr_list[i] 
 
                draw_on = True 
 
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
                draw_on = False 
                x2, y2 = event.pos 
                if x > x2: 
                    x, x2 = x2, x 
                if y > y2: 
                    y, y2 = y2, y 
 
                if mode == 'rect': 
                    pygame.draw.rect(draw_surf, color, (x, y, x2 - x, y2 - y), thickness) 
                    screen.blit(draw_surf, (3, 3)) 
                elif mode == 'circle': 
                    radius = int(math.sqrt((x2 - x)**2 + (y2 - y)**2)) // 2 
                    pygame.draw.circle(draw_surf, color, ((x + x2) // 2, (y + y2) // 2), radius, thickness) 
                    screen.blit(draw_surf, (3, 3)) 
 
            if event.type == pygame.MOUSEMOTION: 
                if draw_on: 
                    if mode == 'brush' or mode == 'eraser': 
                        draw_line(draw_surf, last_pos, event.pos, radius, color) 
                        screen.blit(draw_surf, (3, 3)) 
 
                    last_pos = event.pos 
 
        mode_color = mode_check(mode, color) 
 
        if mode == 'brush' or mode == 'eraser': 
            x, y = pygame.mouse.get_pos() 
            if x < 900 - radius and x > radius + 3: 
                if y > radius and y < 695 - radius: 
                    pygame.mouse.set_visible(False) 
                    screen.blit(draw_surf, (3, 3)) 
                    if x + (radius * 2) < 900 - radius and x - (radius * 2) > radius + 3: 
                        if y + (radius * 2) < 695 - radius and y - (radius * 2) > radius: 
                            if mode == 'brush': 
                                pygame.draw.circle(screen, mode_color, (x + 3, y + 3), radius) 
                            else: 
                                pygame.draw.circle(screen, GREY, (x + 3, y + 3), radius, 3) 
            elif x > 900 - radius: 
                pygame.mouse.set_visible(True) 
 
        pygame.display.flip() 
 
    pygame.quit() 
 
 
if __name__ == "__main__":
    main()
