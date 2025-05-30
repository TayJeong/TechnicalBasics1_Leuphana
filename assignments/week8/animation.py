import pygame
import sys
import random
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("More Diverse Circular Orbit Animation")
clock = pygame.time.Clock()


original_img = pygame.image.load("star.png").convert_alpha()
original_img = pygame.transform.scale(original_img, (60, 60))

class AnimatedImage:
    def __init__(self):
        self.image = original_img.copy()


        self.center_x = random.randint(100, 700)
        self.center_y = random.randint(100, 500)
        self.radius = random.randint(50, 200)


        self.angle = random.uniform(0, 2 * math.pi)

        self.angular_speed = random.uniform(0.005, 0.07)

        #start location
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)


        self.alpha = random.randint(80, 255)
        self.alpha_dir = random.choice([-1, 1])

        #image size
        scale_size = random.randint(40, 80)
        self.image = pygame.transform.scale(self.image, (scale_size, scale_size))

    def update(self):
        self.angle += self.angular_speed
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)

        self.alpha += self.alpha_dir * 4
        if self.alpha <= 80 or self.alpha >= 255:
            self.alpha_dir *= -1
            self.alpha = max(80, min(255, self.alpha))

        self.image.set_alpha(int(self.alpha))

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))



images = [AnimatedImage() for _ in range(20)]

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for img in images:
        img.update()
        img.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
