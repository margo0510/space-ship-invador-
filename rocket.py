import pygame 
import random
import time 
import os 

pygame.mixer.init()
pygame.font.init()

pygame.init()

WIDTH, HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invador")

WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
NAVY = (0,0,128)

BORDER = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("assets/Grenade.mp3") #to load sounds
BULLET_FIRE_SOUND = pygame.mixer.Sound("assets/Gun_Silencer.mp3")

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("americantypewriter", 100)

BULLET_VAL = 7 
MAX_BULLETS = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT =  55,40


player_x = 200
player_y = 380

player = pygame.image.load("character.png") #to load images 
bg_image = pygame.image.load("background.png")

yellow_spaceship_image = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
yellow_spaceship = pygame.tranform.rotate(pygame.tranform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

red_spaceship_image = pygame.image.load(os.path.join("assets", "spaceship_red.png"))










keys = [False, False, False, False]

while player_y < 600:
    screen.blit(bg_image, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    #if up button is pressed 
    if keys[0]:
        if player_y > 0:
            player_y -= 7 
    if keys[2]:
        if player_y < 400:
            player_y += 7 
    if keys [1]:
        if player_x > 0:
            player_x -= 2
    if keys[3]:
        if player_x < 480:
            player_x += 2

    
    time.sleep(0.05)

