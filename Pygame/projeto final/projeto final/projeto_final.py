import pygame, random, os

# ---------------- CONFIGURAÇÃO ----------------
pygame.init()
W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("PONG - Configurável")
clock = pygame.time.Clock()

# Fontes: normal e específicas para o menu (maiores)
font = pygame.font.SysFont(None, 32)
menu_title_font = pygame.font.SysFont(None, 96)   # título grande no menu
menu_button_font = pygame.font.SysFont(None, 40)  # texto maior nos botões
menu_sub_font = pygame.font.SysFont(None, 28)

# Ficheiro de settings
SETTINGS_FILE = "pong_settings.txt"

# ---------------- VALORES POR DEFEITO ----------------
DEFAULT_P1_W, DEFAULT_P1_H = 12, 100
DEFAULT_P2_W, DEFAULT_P2_H = 12, 100
DEFAULT_BALL_SIZE = 12
PADDLE_SPEED = 6

# Valores atuais (inicializam com os defaults)
P1_W, P1_H = DEFAULT_P1_W, DEFAULT_P1_H
P2_W, P2_H = DEFAULT_P2_W, DEFAULT_P2_H
BALL_SIZE = DEFAULT_BALL_SIZE

# Tenta carregar settings guardados
if os.path.exists(SETTINGS_FILE):
    try:
        with open(SETTINGS_FILE, "r") as f:
            parts = f.read().strip().split(",")
            if len(parts) >= 5:
                P1_W = int(parts[0]); P1_H = int(parts[1])
                P2_W = int(parts[2]); P2_H = int(parts[3])
                BALL_SIZE = int(parts[4])
    except Exception:
        pass

# ---------------- VARIÁVEIS DO JOGO ----------------
ball_pos = [W // 2, H // 2]
ball_vel = [random.choice([-5, 5]), random.choice([-3, 3])]
left_paddle = pygame.Rect(30, H // 2 - P1_H // 2, P1_W, P1_H)
right_paddle = pygame.Rect(W - 30 - P2_W, H // 2 - P2_H // 2, P2_W, P2_H)
score_left = 0
score_right = 0

# Estados
STATE_MENU = 0
STATE_SETTINGS = 1
STATE_GAME = 2
STATE_GAMEOVER = 3
game_state = STATE_MENU

# ---------------- FUNÇÕES AUXILIARES ----------------
def save_settings():
    try:
        with open(SETTINGS_FILE, "w") as f:
            f.write(f"{P1_W},{P1_H},{P2_W},{P2_H},{BALL_SIZE}")
    except Exception:
        pass

def reset_ball(direction=1):
    global ball_pos, ball_vel
    ball_pos = [W // 2, H // 2]
    ball_vel = [direction * 5, random.choice([-4, -3, 3, 4])]

def reset_game():
    global left_paddle, right_paddle, score_left, score_right
    left_paddle = pygame.Rect(30, H // 2 - P1_H // 2, P1_W, P1_H)
    right_paddle = pygame.Rect(W - 30 - P2_W, H // 2 - P2_H // 2, P2_W, P2_H)
    score_left = 0
    score_right = 0
    reset_ball(random.choice([-1, 1]))

def draw_center_line():
    for y in range(0, H, 20):
        pygame.draw.rect(win, (200, 200, 200), (W // 2 - 2, y + 5, 4, 10))

def draw_button(rect, text, color=(70,70,70), hover_color=(100,100,100), use_menu_font=False):
    mx, my = pygame.mouse.get_pos()
    is_hover = rect.collidepoint(mx, my)
    col = hover_color if is_hover else color
    pygame.draw.rect(win, col, rect, border_radius=8)
    f = menu_button_font if use_menu_font else font
    txt = f.render(text, True, (255,255,255))
    win.blit(txt, (rect.x + rect.width//2 - txt.get_width()//2, rect.y + rect.height//2 - txt.get_height()//2))
    return is_hover

def draw_label(x, y, text, color=(220,220,220), use_small=False):
    f = font if not use_small else menu_sub_font
    lbl = f.render(text, True, color)
    win.blit(lbl, (x, y))

# ---------------- LOOP PRINCIPAL ----------------
running = True
reset_ball()

# Temporários para settings (mostrados no ecrã de configurações)
temp_p1_w = P1_W
temp_p1_h = P1_H
temp_p2_w = P2_W
temp_p2_h = P2_H
temp_ball_size = BALL_SIZE

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state == STATE_SETTINGS:
                    temp_p1_w, temp_p1_h = P1_W, P1_H
                    temp_p2_w, temp_p2_h = P2_W, P2_H
                    temp_ball_size = BALL_SIZE
                    game_state = STATE_MENU
                elif game_state == STATE_GAME:
                    running = False
                elif game_state == STATE_MENU:
                    running = False
            if event.key == pygame.K_RETURN:
                if game_state == STATE_MENU:
                    reset_game()
                    game_state = STATE_GAME
                elif game_state == STATE_GAMEOVER:
                    reset_game()
                    game_state = STATE_GAME

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            # Menu: Jogar e Configurações (botões maiores)
            if game_state == STATE_MENU:
                play_rect = pygame.Rect(W//2 - 180, H//2 - 80, 360, 80)   # maior
                settings_rect = pygame.Rect(W//2 - 180, H//2 + 20, 360, 80) # maior
                if play_rect.collidepoint(mx, my):
                    reset_game()
                    game_state = STATE_GAME
                elif settings_rect.collidepoint(mx, my):
                    temp_p1_w, temp_p1_h = P1_W, P1_H
                    temp_p2_w, temp_p2_h = P2_W, P2_H
                    temp_ball_size = BALL_SIZE
                    game_state = STATE_SETTINGS

            # Settings interactions
            if game_state == STATE_SETTINGS:
                p1w_minus = pygame.Rect(180, 160, 40, 40)
                p1w_plus  = pygame.Rect(360, 160, 40, 40)
                p1h_minus = pygame.Rect(180, 210, 40, 40)
                p1h_plus  = pygame.Rect(360, 210, 40, 40)

                p2w_minus = pygame.Rect(180, 270, 40, 40)
                p2w_plus  = pygame.Rect(360, 270, 40, 40)
                p2h_minus = pygame.Rect(180, 320, 40, 40)
                p2h_plus  = pygame.Rect(360, 320, 40, 40)

                bs_minus = pygame.Rect(180, 380, 40, 40)
                bs_plus  = pygame.Rect(360, 380, 40, 40)

                apply_rect = pygame.Rect(W//2 - 220, 440, 140, 50)
                cancel_rect = pygame.Rect(W//2 - 70, 440, 140, 50)
                reset_rect = pygame.Rect(W//2 + 80, 440, 140, 50)

                if p1w_minus.collidepoint(mx, my):
                    temp_p1_w = max(6, temp_p1_w - 2)
                elif p1w_plus.collidepoint(mx, my):
                    temp_p1_w = min(60, temp_p1_w + 2)
                elif p1h_minus.collidepoint(mx, my):
                    temp_p1_h = max(30, temp_p1_h - 10)
                elif p1h_plus.collidepoint(mx, my):
                    temp_p1_h = min(400, temp_p1_h + 10)
                elif p2w_minus.collidepoint(mx, my):
                    temp_p2_w = max(6, temp_p2_w - 2)
                elif p2w_plus.collidepoint(mx, my):
                    temp_p2_w = min(60, temp_p2_w + 2)
                elif p2h_minus.collidepoint(mx, my):
                    temp_p2_h = max(30, temp_p2_h - 10)
                elif p2h_plus.collidepoint(mx, my):
                    temp_p2_h = min(400, temp_p2_h + 10)
                elif bs_minus.collidepoint(mx, my):
                    temp_ball_size = max(6, temp_ball_size - 2)
                elif bs_plus.collidepoint(mx, my):
                    temp_ball_size = min(80, temp_ball_size + 2)
                elif apply_rect.collidepoint(mx, my):
                    P1_W, P1_H = temp_p1_w, temp_p1_h
                    P2_W, P2_H = temp_p2_w, temp_p2_h
                    BALL_SIZE = temp_ball_size
                    save_settings()
                    reset_game()
                    game_state = STATE_MENU
                elif cancel_rect.collidepoint(mx, my):
                    temp_p1_w, temp_p1_h = P1_W, P1_H
                    temp_p2_w, temp_p2_h = P2_W, P2_H
                    temp_ball_size = BALL_SIZE
                    game_state = STATE_MENU
                elif reset_rect.collidepoint(mx, my):
                    temp_p1_w, temp_p1_h = DEFAULT_P1_W, DEFAULT_P1_H
                    temp_p2_w, temp_p2_h = DEFAULT_P2_W, DEFAULT_P2_H
                    temp_ball_size = DEFAULT_BALL_SIZE

    keys = pygame.key.get_pressed()

    # -------- LÓGICA DO JOGO -----------
    if game_state == STATE_GAME:
        if keys[pygame.K_w]:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s]:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP]:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            right_paddle.y += PADDLE_SPEED

        left_paddle.width, left_paddle.height = P1_W, P1_H
        right_paddle.width, right_paddle.height = P2_W, P2_H

        left_paddle.y = max(0, min(H - P1_H, left_paddle.y))
        right_paddle.y = max(0, min(H - P2_H, right_paddle.y))

        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if ball_pos[1] <= BALL_SIZE // 2 or ball_pos[1] >= H - BALL_SIZE // 2:
            ball_vel[1] *= -1

        left_rect = pygame.Rect(left_paddle.x, left_paddle.y, P1_W, P1_H)
        right_rect = pygame.Rect(right_paddle.x, right_paddle.y, P2_W, P2_H)
        ball_rect = pygame.Rect(int(ball_pos[0] - BALL_SIZE // 2), int(ball_pos[1] - BALL_SIZE // 2), BALL_SIZE, BALL_SIZE)

        if ball_rect.colliderect(left_rect):
            ball_vel[0] = abs(ball_vel[0]) + 0.5
            offset = (ball_pos[1] - left_rect.centery) / (P1_H / 2)
            ball_vel[1] = int(offset * 6)
        if ball_rect.colliderect(right_rect):
            ball_vel[0] = -abs(ball_vel[0]) - 0.5
            offset = (ball_pos[1] - right_rect.centery) / (P2_H / 2)
            ball_vel[1] = int(offset * 6)

        if ball_pos[0] < 0:
            score_right += 1
            reset_ball(direction=1)
        if ball_pos[0] > W:
            score_left += 1
            reset_ball(direction=-1)

        if score_left >= 10 or score_right >= 10:
            game_state = STATE_GAMEOVER

    # ---------------- DESENHAR ----------------
    win.fill((12, 12, 12))

    if game_state == STATE_MENU:
        # Título grande
        title = menu_title_font.render("PONG", True, (255, 255, 255))
        win.blit(title, (W//2 - title.get_width()//2, 40))

        # Botões maiores (use_menu_font=True para texto maior)
        play_rect = pygame.Rect(W//2 - 180, H//2 - 80, 360, 80)
        settings_rect = pygame.Rect(W//2 - 180, H//2 + 20, 360, 80)
        draw_button(play_rect, "JOGAR", color=(30,120,30), hover_color=(50,160,50), use_menu_font=True)
        draw_button(settings_rect, "CONFIGURAÇÕES", color=(30,90,160), hover_color=(60,130,200), use_menu_font=True)

        # Subtexto menor
        hint = font.render("W/S = Paddle 1   SETA_CIMA/SETA_BAIXO = Paddle 2   Esc = Sair", True, (180,180,180))
        win.blit(hint, (W//2 - hint.get_width()//2, H - 40))

    elif game_state == STATE_SETTINGS:
        header = font.render("CONFIGURAÇÕES", True, (255,255,255))
        win.blit(header, (W//2 - header.get_width()//2, 30))

        # Paddle 1
        draw_label(240, 140, f"Paddle 1-Largura: {temp_p1_w}")
        p1w_minus = pygame.Rect(180, 160, 40, 40)
        p1w_plus  = pygame.Rect(360, 160, 40, 40)
        draw_button(p1w_minus, "-", color=(120,40,40), hover_color=(160,60,60))
        draw_button(p1w_plus, "+", color=(40,120,40), hover_color=(60,160,60))

        draw_label(240, 190, f"Paddle 1 - Altura: {temp_p1_h}")
        p1h_minus = pygame.Rect(180, 210, 40, 40)
        p1h_plus  = pygame.Rect(360, 210, 40, 40)
        draw_button(p1h_minus, "-", color=(120,40,40), hover_color=(160,60,60))
        draw_button(p1h_plus, "+", color=(40,120,40), hover_color=(60,160,60))

        # Paddle 2
        draw_label(240, 250, f"Paddle 2 - Largura: {temp_p2_w}")
        p2w_minus = pygame.Rect(180, 270, 40, 40)
        p2w_plus  = pygame.Rect(360, 270, 40, 40)
        draw_button(p2w_minus, "-", color=(120,40,40), hover_color=(160,60,60))
        draw_button(p2w_plus, "+", color=(40,120,40), hover_color=(60,160,60))

        draw_label(240, 300, f"Paddle 2 - Altura: {temp_p2_h}")
        p2h_minus = pygame.Rect(180, 320, 40, 40)
        p2h_plus  = pygame.Rect(360, 320, 40, 40)
        draw_button(p2h_minus, "-", color=(120,40,40), hover_color=(160,60,60))
        draw_button(p2h_plus, "+", color=(40,120,40), hover_color=(60,160,60))

        # Ball size
        draw_label(240, 360, f"Tamanho Bola: {temp_ball_size}")
        bs_minus = pygame.Rect(180, 380, 40, 40)
        bs_plus  = pygame.Rect(360, 380, 40, 40)
        draw_button(bs_minus, "-", color=(120,40,40), hover_color=(160,60,60))
        draw_button(bs_plus, "+", color=(40,120,40), hover_color=(60,160,60))

        # Aplicar / Cancelar / Reset
        apply_rect = pygame.Rect(W//2 - 220, 440, 140, 50)
        cancel_rect = pygame.Rect(W//2 - 70, 440, 140, 50)
        reset_rect = pygame.Rect(W//2 + 80, 440, 140, 50)
        draw_button(apply_rect, "APLICAR", color=(30,100,200), hover_color=(60,140,240))
        draw_button(cancel_rect, "CANCELAR", color=(100,30,30), hover_color=(140,60,60))
        draw_button(reset_rect, "RESETAR PADRÕES", color=(80,80,80), hover_color=(120,120,120))

        # Preview dos dois paddles e bola
        preview_x = W - 220
        preview_y = 150
        pygame.draw.rect(win, (200,200,200), (preview_x, preview_y, temp_p1_w, temp_p1_h))
        pygame.draw.rect(win, (200,200,200), (preview_x + 80, preview_y, temp_p2_w, temp_p2_h))
        pygame.draw.circle(win, (255,255,255), (preview_x + 40, preview_y + max(temp_p1_h, temp_p2_h) + 60), temp_ball_size // 2)

    elif game_state == STATE_GAME:
        draw_center_line()
        pygame.draw.rect(win, (255,255,255), (left_paddle.x, left_paddle.y, P1_W, P1_H))
        pygame.draw.rect(win, (255,255,255), (right_paddle.x, right_paddle.y, P2_W, P2_H))
        pygame.draw.ellipse(win, (255,255,255), (int(ball_pos[0] - BALL_SIZE // 2), int(ball_pos[1] - BALL_SIZE // 2), BALL_SIZE, BALL_SIZE))
        s = font.render(f"{score_left}    {score_right}", True, (255,255,255))
        win.blit(s, (W//2 - s.get_width()//2, 20))

    else:  # GAMEOVER
        over = font.render("GAME OVER - Pressiona ENTER para reiniciar", True, (255,0,0))
        win.blit(over, (W//2 - over.get_width()//2, H//2 - 20))

    pygame.display.flip()

pygame.quit()
