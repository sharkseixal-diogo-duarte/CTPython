import pygame, random, os

# ---------------- CONFIGURAÇÃO ----------------
pygame.init()
W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("PONG - Mini")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Highscore simples por jogador direito (guarda em ficheiro)
HIGHSCORE_FILE = "pong_highscore.txt"
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "r") as f:
        highscore = int(f.read() or 0)
else:
    highscore = 0

# ---------------- VARIÁVEIS ----------------
PADDLE_W, PADDLE_H = 12, 100
PADDLE_SPEED = 6
BALL_SIZE = 12
ball_pos = [W // 2, H // 2]
ball_vel = [random.choice([-5,5]), random.choice([-3,3])]
left_paddle = pygame.Rect(30, H//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
right_paddle = pygame.Rect(W - 30 - PADDLE_W, H//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
score_left = 0
score_right = 0

# Estados de jogo
STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU

# ---------------- FUNÇÕES ----------------
def reset_ball(direction=1):
    """Reposiciona a bola no centro e define velocidade inicial."""
    global ball_pos, ball_vel
    ball_pos = [W // 2, H // 2]
    ball_vel = [direction * 5, random.choice([-4, -3, 3, 4])]

def reset_game():
    """Reinicia pontuações e posições."""
    global left_paddle, right_paddle, score_left, score_right
    left_paddle.y = H//2 - PADDLE_H//2
    right_paddle.y = H//2 - PADDLE_H//2
    score_left = 0
    score_right = 0
    reset_ball(random.choice([-1,1]))

def draw_center_line():
    for y in range(0, H, 20):
        pygame.draw.rect(win, (200,200,200), (W//2 - 2, y+5, 4, 10))

# ---------------- LOOP PRINCIPAL ----------------
running = True
reset_ball()

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    keys = pygame.key.get_pressed()

    if game_state == STATE_GAME:
        # Movimento paddles
        if keys[pygame.K_w]:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s]:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP]:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            right_paddle.y += PADDLE_SPEED

        # Limitar dentro do ecrã
        left_paddle.y = max(0, min(H - PADDLE_H, left_paddle.y))
        right_paddle.y = max(0, min(H - PADDLE_H, right_paddle.y))

        # Atualizar bola
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Colisões com topo/baixo
        if ball_pos[1] <= BALL_SIZE//2 or ball_pos[1] >= H - BALL_SIZE//2:
            ball_vel[1] *= -1

        # Colisão com paddles
        ball_rect = pygame.Rect(int(ball_pos[0]-BALL_SIZE//2), int(ball_pos[1]-BALL_SIZE//2), BALL_SIZE, BALL_SIZE)
        if ball_rect.colliderect(left_paddle):
            ball_vel[0] = abs(ball_vel[0]) + 0.5
            # ajustar ângulo conforme posição de impacto
            offset = (ball_pos[1] - left_paddle.centery) / (PADDLE_H/2)
            ball_vel[1] = int(offset * 6)
        if ball_rect.colliderect(right_paddle):
            ball_vel[0] = -abs(ball_vel[0]) - 0.5
            offset = (ball_pos[1] - right_paddle.centery) / (PADDLE_H/2)
            ball_vel[1] = int(offset * 6)

        # Pontuação
        if ball_pos[0] < 0:
            score_right += 1
            reset_ball(direction=1)
        if ball_pos[0] > W:
            score_left += 1
            reset_ball(direction=-1)

        # Condição simples de game over (ex: primeiro a 10)
        if score_left >= 10 or score_right >= 10:
            # atualizar highscore para o vencedor (maior pontuação)
            winner_score = max(score_left, score_right)
            if winner_score > highscore:
                highscore = winner_score
                with open(HIGHSCORE_FILE, "w") as f:
                    f.write(str(highscore))
            game_state = STATE_GAMEOVER

    # ---------------- DESENHAR ----------------
    win.fill((0,0,0))
    if game_state == STATE_MENU:
        title = font.render("PONG - Pressiona ENTER para começar", True, (255,255,255))
        win.blit(title, (W//2 - title.get_width()//2, H//2 - 20))
        hs = font.render(f"Highscore: {highscore}", True, (255,215,0))
        win.blit(hs, (W//2 - hs.get_width()//2, H//2 + 20))
    elif game_state == STATE_GAME:
        draw_center_line()
        pygame.draw.rect(win, (255,255,255), left_paddle)
        pygame.draw.rect(win, (255,255,255), right_paddle)
        pygame.draw.ellipse(win, (255,255,255), (int(ball_pos[0]-BALL_SIZE//2), int(ball_pos[1]-BALL_SIZE//2), BALL_SIZE, BALL_SIZE))
        s = font.render(f"{score_left}    {score_right}", True, (255,255,255))
        win.blit(s, (W//2 - s.get_width()//2, 20))
    else:
        over = font.render("GAME OVER - Pressiona ENTER para reiniciar", True, (255,0,0))
        win.blit(over, (W//2 - over.get_width()//2, H//2 - 20))

    pygame.display.flip()
