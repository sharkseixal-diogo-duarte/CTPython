import pygame, random, math, os

pygame.init()
W, H = 1000, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
running = True

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU

# player variéveis
players_lives = 3
player1_pos = [20, H/2]
player2_pos = [950, H/2]
player_speed = 1
player_lives = 3

while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player1_pos[1] += player_speed
    if keys[pygame.K_w]:
        player2_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player2_pos[1] += player_speed

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                running = False

    pygame.draw.rect(win,"grey",(player1_pos[0],player1_pos[1],30, 100))
    pygame.draw.rect(win, "grey", (player2_pos[0], player2_pos[1], 30, 100))
    pygame.display.flip()

pygame.quit()