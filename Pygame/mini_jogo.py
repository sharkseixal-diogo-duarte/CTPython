import pygame, random, math, os

pygame.init()
W, H = 800,600
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# Score
HIGHSCORE_FILE = "highscore.txt"

if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE,"r") as f:
        highscore = int(f.read())

else:
    highscore = 0


player_pos = [W/2,H/2]
player_speed = 5
player_lives = 3
score = 0

bullets = []
last_shot = 0
Shot_Cooldown = 300

asteroides = []

asteroides_types = [
    {"size":20, "speed":3, "points":15, "color":(200,200,255)},
    {"size":35, "speed":2, "points":10, "color":(180,180,180)},
    {"size":50, "speed":1.5, "points":5, "color":(150,150,150)}
]


powerup = []
powerup_active = False
powerup_timer = 0

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU


def spawn_asteroid():
    t = random.choice(asteroides_types)
    x = random.randint(0,W)
    y = random.choice([-50,H+50])
    angle = math.atanh(H//2 - y, W//2 -x)
    asteroides.append([x,y,t["speed"],t["size"],angle,t["points"],t["color"]])

def spawn_powerup():
    x = random.randint(50, W-50)
    y = random.randint(50,H-50)
    powerup.append([x,y ,"shield"])

def reset_game():
    global player_pos, player_lives, score, asteroides, bullets, powerup
    player_pos = [W//2, H//2]
    player_lives = 3
    score = 0
    asteroides = []
    bullets = []
    powerup = []
    for _ in range(6):
        spawn_asteroid()

running = True
spawner_time = 0
spawner_interval = 3000
last_powerup = 0
powerup_interval = 10000

while running:
    dt = clock.tick(60)
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    keys = pygame.key.get_pressed()

    if game_state == STATE_GAME:
        if keys[pygame.K_w] or keys[pygame.K_UP]: player_pos[1] -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_pos[1] += player_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_pos[0] -= player_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_pos[0] += player_speed

        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_shot > Shot_Cooldown:
            last_shot = pygame.time.get_ticks()
            bullets.append([player_pos[0], player_pos[1],0, -8])

        for b in bullets:
            b[1] += b[3]
        bullets = [b for b in bullets if 0 < b[1] > H]

        for a in  asteroides:
            a[0] += math.cos(a[4]*a[2])
            a[1] += math.cos(a[4] * a[2])

        spawner_time += dt

        if spawner_time > spawner_interval:
            spawn_asteroid()
            spawner_time = 0
            if spawner_interval > 1000:
                spawner_interval -= 50

        if pygame.time.get_ticks() -last_powerup > powerup_interval:
            spawn_powerup()
            last_powerup = pygame.time.get_ticks()

        if powerup_active and pygame.time.get_ticks() > powerup_timer:
            powerup_active = False


        new_asteroids = []
        for a in asteroides:
            ax, ay, sp, sz, ang, pts, color = a
            hit = False
            for b in bullets:
                if math.hypot(ax - b[0],ay - b[1]) < sz:
                    bullets.remove(b)
                    hit = True
                    break

            if hit:
                score += pts
                spawn_asteroid()
            else:
                new_asteroids.append(a)
        asteroides = new_asteroids

        