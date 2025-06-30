import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Get away from Cactus")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("arial", 32)

background = pygame.Surface((WIDTH, HEIGHT))

for y in range(HEIGHT):
    ratio = y / HEIGHT
    r = int((135 * (1 - ratio)) + (237 * ratio))
    g = int((206 * (1 - ratio)) + (201 * ratio))
    b = int((235 * (1 - ratio)) + (175 * ratio))
    pygame.draw.line(background, (r, g, b), (0, y), (WIDTH, y))

for _ in range(500):
    x = random.randint(0, WIDTH - 1)
    y = random.randint(HEIGHT // 2, HEIGHT - 1)
    color_variation = random.randint(-20, 20)
    base_color = (237, 201, 175)
    dot_color = (
        max(0, min(255, base_color[0] + color_variation)),
        max(0, min(255, base_color[1] + color_variation)),
        max(0, min(255, base_color[2] + color_variation)),
    )
    background.set_at((x, y), dot_color)



player_original = pygame.image.load("dino_s.png").convert_alpha()
player_img = pygame.transform.scale(player_original, (50, 60))
cactus_original = pygame.image.load("cactus.png").convert_alpha()
cactus_img = pygame.transform.scale(cactus_original, (40, 60))

hit_sound = pygame.mixer.Sound("sound_effect.mp3")

player_rect = player_img.get_rect(midleft=(100, HEIGHT // 2))
cactus_rect = cactus_img.get_rect(midright=(WIDTH + 40, random.randint(60, HEIGHT - 60)))

score = 0
hits = 0
cactus_speed = 15
max_speed = 25

running = True
game_over = False
while running:
    clock.tick(FPS)
    win.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 키 입력
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_rect.move_ip(0, -5)
        if keys[pygame.K_DOWN]:
            player_rect.move_ip(0, 5)

        player_rect.clamp_ip(win.get_rect())

        # 선인장 이동
        cactus_rect.move_ip(-cactus_speed, 0)

        if cactus_rect.right < 0:
            cactus_rect.left = WIDTH + random.randint(50, 200)
            cactus_rect.top = random.randint(60, HEIGHT - 60)

        # 충돌 감지
        if player_rect.colliderect(cactus_rect):
            hit_sound.play()  # 충돌 시 효과음 재생

            score += 1
            hits += 1
            cactus_speed = min(cactus_speed + 0.5, max_speed)

            cactus_rect.left = WIDTH + random.randint(50, 200)
            cactus_rect.top = random.randint(60, HEIGHT - 60)

            if hits >= 3:
                game_over = True

        # 렌더링
        win.blit(player_img, player_rect)
        win.blit(cactus_img, cactus_rect)

        score_text = font.render(f"Score: {score}", True, BLACK)
        speed_text = font.render(f"Speed: {cactus_speed:.1f}", True, BLACK)
        hits_text = font.render(f"Hits: {hits}/3", True, BLACK)
        win.blit(score_text, (10, 10))
        win.blit(speed_text, (10, 50))
        win.blit(hits_text, (10, 90))

    else:
        over_text = font.render("Game Over! You hit 3 cacti!", True, (200, 0, 0))
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
