import pygame, random, math, os

# ---------------- CONFIGURAÇÃO ----------------
pygame.init()
W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini Asteroids Expandido")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Highscore: guarda e carrega o melhor score do ficheiro
HIGHSCORE_FILE = "highscore.txt"
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "r") as f:
        highscore = int(f.read())
else:
    highscore = 0

# ---------------- VARIÁVEIS ----------------
player_pos = [W // 2, H // 2]  # posição inicial do jogador
player_speed = 5  # velocidade do jogador
player_lives = 3  # número de vidas
score = 0  # pontuação atual

bullets = []  # lista de projéteis ativos
last_shot = 0  # registo do último disparo
shot_cooldown = 300  # tempo mínimo entre disparos (ms)

asteroids = []  # lista de asteroides ativos
# diferentes tipos de asteroides com tamanho, velocidade, pontos e cor
asteroid_types = [
    {"size": 20, "speed": 3, "points": 15, "color": (200, 200, 255)},
    {"size": 35, "speed": 2, "points": 10, "color": (180, 180, 180)},
    {"size": 50, "speed": 1.5, "points": 5, "color": (150, 150, 150)}
]

# Power-ups
powerups = []  # lista de power-ups no ecrã
powerup_active = False  # estado do escudo
powerup_timer = 0  # tempo para desligar o escudo

# Estados de jogo
STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU


# ---------------- FUNÇÕES ----------------
def spawn_asteroid():
    """Cria um novo asteroide a partir de um tipo aleatório."""
    t = random.choice(asteroid_types)
    # Aparece no topo ou em baixo do ecrã
    x = random.randint(0, W)
    y = random.choice([-50, H + 50])
    # Ângulo em direção ao centro
    angle = math.atan2(H // 2 - y, W // 2 - x)
    asteroids.append([x, y, t["speed"], t["size"], angle, t["points"], t["color"]])


def spawn_powerup():
    """Cria um power-up em posição aleatória no ecrã."""
    x = random.randint(50, W - 50)
    y = random.randint(50, H - 50)
    powerups.append([x, y, "shield"])


def reset_game():
    """Reinicia o estado do jogo (vidas, score, listas)."""
    global player_pos, player_lives, score, asteroids, bullets, powerups
    player_pos = [W // 2, H // 2]
    player_lives = 3
    score = 0
    asteroids = []
    bullets = []
    powerups = []
    for _ in range(6):  # começa com alguns asteroides
        spawn_asteroid()


# ---------------- LOOP PRINCIPAL ----------------
running = True
spawn_timer = 0
spawn_interval = 3000  # intervalo inicial de criação de asteroides
last_powerup = 0
powerup_interval = 10000  # intervalo entre power-ups

while running:
    dt = clock.tick(60)  # limita FPS e obtém delta time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Começa o jogo a partir do menu
            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            # Recomeça a partir do game over
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    keys = pygame.key.get_pressed()

    # ----------- LÓGICA DO JOGO -----------
    if game_state == STATE_GAME:
        # Movimento do jogador
        if keys[pygame.K_w] or keys[pygame.K_UP]: player_pos[1] -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_pos[1] += player_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_pos[0] -= player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_pos[0] += player_speed

        # Disparo de projéteis
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_shot > shot_cooldown:
            last_shot = pygame.time.get_ticks()
            bullets.append([player_pos[0], player_pos[1], 0, -8])

        # Atualizar projéteis
        for b in bullets:
            b[1] += b[3]
        bullets = [b for b in bullets if 0 < b[1] < H]

        # Atualizar asteroides (movem-se em direção ao centro)
        for a in asteroids:
            a[0] += math.cos(a[4]) * a[2]
            a[1] += math.sin(a[4]) * a[2]

        # Criar novos asteroides periodicamente
        spawn_timer += dt
        if spawn_timer > spawn_interval:
            spawn_asteroid()
            spawn_timer = 0
            # Aumenta a dificuldade reduzindo o intervalo
            if spawn_interval > 1000:
                spawn_interval -= 50

        # Criar power-ups periodicamente
        if pygame.time.get_ticks() - last_powerup > powerup_interval:
            spawn_powerup()
            last_powerup = pygame.time.get_ticks()

        # Controlar tempo do escudo
        if powerup_active and pygame.time.get_ticks() > powerup_timer:
            powerup_active = False

        # Colisões projéteis-asteroides
        new_asteroids = []
        for a in asteroids:
            ax, ay, sp, sz, ang, pts, color = a
            hit = False
            for b in bullets:
                if math.hypot(ax - b[0], ay - b[1]) < sz:
                    bullets.remove(b)
                    hit = True
                    break
            if hit:
                score += pts
                spawn_asteroid()  # substitui por um novo
            else:
                new_asteroids.append(a)
        asteroids = new_asteroids

        # Colisões jogador-asteroides
        for a in asteroids:
            if math.hypot(a[0] - player_pos[0], a[1] - player_pos[1]) < a[3] + 20:
                if not powerup_active:
                    player_lives -= 1
                asteroids.remove(a)
                spawn_asteroid()
                # Verificar se o jogo acabou
                if player_lives <= 0:
                    game_state = STATE_GAMEOVER
                    # Atualizar highscore
                    if score > highscore:
                        highscore = score
                        with open(HIGHSCORE_FILE, "w") as f:
                            f.write(str(highscore))

        # Colisões jogador-powerup
        for p in powerups:
            if math.hypot(p[0] - player_pos[0], p[1] - player_pos[1]) < 30:
                if p[2] == "shield":
                    powerup_active = True
                    powerup_timer = pygame.time.get_ticks() + 5000  # dura 5s
                powerups.remove(p)

    # ---------------- DESENHAR ----------------
    win.fill((0, 0, 20))  # pinta o fundo da tela (RGB: azul bem escuro)

    if game_state == STATE_MENU:
        # Renderiza textos (gera superfícies de texto a partir da fonte)
        title = font.render("MINI ASTEROIDS", True, (255, 255, 255))
        prompt = font.render("Pressiona ENTER para começar", True, (200, 200, 200))
        hs = font.render(f"Highscore: {highscore}", True, (255, 255, 0))

        # win.blit(surface, (x,y)) desenha uma superfície (imagem ou texto) na tela principal (win)
        win.blit(title, (W // 2 - 100, H // 2 - 40))  # desenha o título no centro
        win.blit(prompt, (W // 2 - 180, H // 2))  # desenha a instrução logo abaixo
        win.blit(hs, (W // 2 - 80, H // 2 + 40))  # desenha o highscore um pouco mais abaixo

    elif game_state == STATE_GAME:
        # Desenha o jogador
        pygame.draw.circle(win, (0, 255, 0), player_pos, 20)
        if powerup_active:
            pygame.draw.circle(win, (0, 150, 255), player_pos, 30, 3)

        # Desenha as balas
        for b in bullets:
            pygame.draw.circle(win, (255, 255, 0), (int(b[0]), int(b[1])), 5)

        # Desenha os asteroides
        for a in asteroids:
            pygame.draw.circle(win, a[6], (int(a[0]), int(a[1])), a[3])

        # Desenha os powerups
        for p in powerups:
            pygame.draw.rect(win, (0, 200, 255), (p[0] - 10, p[1] - 10, 20, 20))

        # Renderiza o HUD e desenha com blit
        hud = font.render(f"Score: {score}  Vidas: {player_lives}", True, (255, 255, 255))
        win.blit(hud, (10, 10))  # mostra o texto no canto superior esquerdo

    elif game_state == STATE_GAMEOVER:
        # Renderiza textos para o Game Over
        over = font.render("GAME OVER", True, (255, 0, 0))
        sc = font.render(f"Score final: {score}", True, (255, 255, 255))
        hs = font.render(f"Highscore: {highscore}", True, (255, 255, 0))
        prompt = font.render("Pressiona ENTER para reiniciar", True, (200, 200, 200))

        # win.blit(surface, (x,y)) desenha cada texto no centro da tela
        win.blit(over, (W // 2 - 80, H // 2 - 60))
        win.blit(sc, (W // 2 - 90, H // 2 - 20))
        win.blit(hs, (W // 2 - 90, H // 2 + 20))
        win.blit(prompt, (W // 2 - 180, H // 2 + 60))

    pygame.display.flip()  # atualiza o ecrã com tudo o que foi desenhado

pygame.quit()