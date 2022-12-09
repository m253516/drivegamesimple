import pygame
from pygame.locals import *
import random
import button

pygame.init()
clock = pygame.time.Clock()

# creating the window
size = width, height = (400,800)
screen = pygame.display.set_mode(size)

# Music
music = pygame.mixer.music.load('music/Killing my Love.mp3')
pygame.mixer.music.play(-1)

# variables for menu screen
main_menu = True

# variables for road
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1
level = 0

# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load('images/car_p1.png')
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.9

car3 = pygame.image.load('images/car_p2.png')
car3_loc = car.get_rect()
car3_loc.center = left_lane, height*0.8

# load enemy vehicle
car2 = pygame.image.load('images/barrel_red_down.png')
car2_loc = car.get_rect()
car2_loc.center = left_lane, height*0.2

# load button images
start_img = pygame.image.load("images/start_btn.png")
exit_img = pygame.image.load("images/exit_btn.png")

# create button instances
start_button = button.Button(width/8, height/2, start_img, 0.5)
exit_button = button.Button(9*width/16, height/2, exit_img, 0.5)

# define fonts
font1 = pygame.font.SysFont('arialblack', 40)

counter = 0
# game loop
running = True
while running:
    clock.tick(500)
    bg_color = sand = (246, 215, 176)
    screen.fill(bg_color)

    # drawing the buttons
    if main_menu == True:
        if start_button.draw(screen):
            main_menu = False
        if exit_button.draw(screen):
            running = False
    else:

        # animate enemy vehicle
        car2_loc[1] += speed
        if car2_loc[1] > height:
            if random.randint(0, 1) == 0:
                car2_loc.center = right_lane, -200
            else:
                car2_loc.center = left_lane, -200

        # increase game difficulty as counter increases
        counter += 2
        if counter == 5000:
            level += 1
            print(f"Level Up! Level {level}, Speed is {speed}.")
            speed += .5
            counter = 0
            # print("level up", speed)

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

        screen.blit(car, car_loc)
        screen.blit(car2, car2_loc)
        screen.blit(car3, car3_loc)

        # end game
        if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 50:
            print("Game Over")
            break
        if car3_loc[0] == car2_loc[0] and car2_loc[1] > car3_loc[1] - 50:
            print("Game Over")
            break

    # event listeners
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in [K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_RIGHT]:
                car_loc = car_loc.move([+int(road_w/2), 0])
            if event.key in [K_a]:
                car3_loc = car3_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d]:
                car3_loc = car3_loc.move([+int(road_w / 2), 0])
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()

#Press Play!!!!