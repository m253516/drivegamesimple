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


# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load('images/car_player.png')
car_loc = car.get_rect()
car_loc.center = width/2 + road_w/4, height*0.8

# load enemy vehicle
car2 = pygame.image.load('images/car_player.png')
car2_loc = car.get_rect()
car2_loc.center = width/2 - road_w/4, height*0.2


# game loop
while running:
    # animate enemy vehicles
    car2_loc[1] += 1 
    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([+int(road_w/2), 0])

    # draw graphics
    grey = (50, 50, 50)
    pygame.draw.rect(
        screen, grey, (width / 2 - road_w / 2, 0, road_w, height))

    # center line
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))

    # left line
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))

    # right line
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 2, 0, roadmark_w, height))

    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)

    pygame.display.update()

pygame.quit()