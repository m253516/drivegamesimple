import pygame
from pygame.locals import *

size = width, height = (400,800)
road_w = int(width/1.6)
roadmark_w = int(width/80)


pygame.init()
running = True

# creating the window
screen = pygame.display.set_mode(size)
bg_color = green = (60, 220, 0)
screen.fill(bg_color)

#draw graphics
grey = (50, 50, 50)
pygame.draw.rect(
    screen, grey, (width/2-road_w/2, 0, road_w, height))

pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))

pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))

pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))
# apply changes
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()