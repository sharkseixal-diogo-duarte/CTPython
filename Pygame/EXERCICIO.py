import pygame

pygame.init()
tela = pygame.display.set_mode((900, 700))
pygame.display.set_caption("game")

#          RGB
fundo = (30, 30, 30)
running = True

x = 100
y = 100
cor = "white"
vel = 1.7
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                running = False
            if evento.key == pygame.K_F1:
                cor = "green"

    if x < 0+40:
        x = 0+40
    if x >= 900-40:
        x = 900-40
    if y <0+40:
        y = 0+40
    if y >= 700-40:
        y= 700-40

    if x == 0+40:
        cor = "blue"
    if x == 900-40:
        cor = "red"
    if y == 700-40:
        cor = "white"
    if y == 0+40:
        cor = "pink"

    tela.fill(fundo)
    pygame.draw.circle(tela, cor,(x,y),40)
    pygame.display.flip()
pygame.quit()