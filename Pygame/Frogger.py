import pygame
import random
pygame.init()
tela = pygame.display.set_mode((900, 700))
pygame.display.set_caption("game")

#          RGB
fundo = (30, 30, 30)
running = True

x = 350
y = 100
cor = "green"
vel = 1.7

carros = []  # lista de asteroides ativos
# diferentes tipos de asteroides com tamanho, velocidade, pontos e cor
asteroid_types = [
    {"size": 20, "speed": 3, "points": 15, "color": (200, 200, 255)}]

t = random.choice(asteroid_types)
x_carros = random.choice([300,600, 900])
y_carros = random.choice([100, 700])
carros.append([x, y, t["speed"], t["size"], t["points"], t["color"]])
posicao_carros = random.randint(250, 700)


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

    if x < 0+40:
        x = 0+40
    if x >= 900-40:
        x = 900-40
    if y <0+40:
        y = 0+40
    if y >= 700-40:
        y= 700-40

    pygame.draw.circle(tela, "red", (x_carros,posicao_carros),60)
    tela.fill(fundo)
    pygame.draw.circle(tela, cor,(x,y),40)
    pygame.display.flip()
pygame.quit()