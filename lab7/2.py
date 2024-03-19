import os
import pygame 

pygame.init()

size = w, h = 400, 400
white = 255, 255, 255

screen = pygame.display.set_mode(size)
image = pygame.image.load("images.png")
clock = pygame.time.Clock()
FPS = 60

music = ["m_1.mp3", "m_2.mp3", "m_3.mp3", "m_4.mp3"]
index = 0

pygame.mixer.music.load(music[index])

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global index
    index = (index + 1) % len(music)
    pygame.mixer.music.load(music[index])
    play_song()

def prev_song():
    global index
    index = (index - 1) % len(music)
    pygame.mixer.music.load(music[index])
    play_song()

    if index < 0:
        index = len(music) - 1
        pygame.mixer.music.load(music[index])
        play_song()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:    #press this keys on keybord 
            if event.key == pygame.K_p:   
                play_song()
            elif event.key == pygame.K_SPACE:  
                stop_song()
            elif event.key == pygame.K_RIGHT:  
                next_song()
            elif event.key == pygame.K_LEFT:  
                prev_song()

    screen.blit(image, (100, 100))
    pygame.display.update()
        
