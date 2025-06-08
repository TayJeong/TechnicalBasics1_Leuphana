import pygame
import random
import sys


pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⭐avoid star⭐")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
FONT = pygame.font.SysFont("arial", 32)


bomb_img = pygame.image.load("star.png")
bomb_img = pygame.transform.scale(bomb_img, (80, 80))

#
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.size = 40
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.size:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


star_img = pygame.image.load("star.png")
star_img = pygame.transform.scale(star_img, (80, 80))  # 크기 키움


class StarBomb:
    def __init__(self):
        self.size = 80
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = random.randint(6, 10)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -self.size
            self.x = random.randint(0, WIDTH - self.size)
            self.speed = random.randint(6, 12)

    def draw(self):
        screen.blit(bomb_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


# game start
def main():
    player = Player()
    starBombs = [StarBomb() for _ in range(5)]
    score = 0
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw()

        for bomb in starBombs:
            bomb.update()
            bomb.draw()

            if player.get_rect().colliderect(bomb.get_rect()):
                running = False

        score += 1
        score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # gameover screen
    screen.fill(WHITE)
    over_text = FONT.render("💥 Game Over!", True, (200, 0, 0))
    final_score = FONT.render(f"Your Score: {score}", True, (0, 0, 0))
    screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, 300))
    screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, 350))
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    main()
