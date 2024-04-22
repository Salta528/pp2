import pygame
import sys
import random
import time

pygame.init()

# Задание FPS
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 390
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

background_image = pygame.image.load("s.png")
DEFAULT_IMAGE_SIZE = (800, 800)
background = pygame.transform.scale(background_image, DEFAULT_IMAGE_SIZE)

player_image = pygame.image.load("p.png")
DEFAULT_IMAGE_SIZE_PLAYER = (100, 100)
player = pygame.transform.scale(player_image, DEFAULT_IMAGE_SIZE_PLAYER)

coin_image = pygame.image.load("Coin.png")
coin = pygame.transform.scale(coin_image, (50, 50))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((50, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = SPEED

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, weight):
        super().__init__() 
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = weight  # Добавляем атрибут веса

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

def message(text, color):
    text_surface = font_small.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    DISPLAYSURF.blit(text_surface, text_rect)

def game_over_screen():
    DISPLAYSURF.fill(WHITE)
    message("You lost! Press Q to quit or C to play again", RED)
    pygame.display.update()

def game_loop():
    player = Player()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    for _ in range(5):  # Create 5 enemies initially
        enemy = Enemy()
        enemies.add(enemy)

    for _ in range(3):  # Create 3 coins initially
        coin = Coin(random.randint(1, 3))
        coins.add(coin)

    SCORE = 0
    game_over = False
    game_close = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

        player.move()
        enemies.update()
        coins.update()

        # Check for collisions
        if pygame.sprite.spritecollideany(player, enemies):
            game_over = True
            game_close = True

        coin_collected = pygame.sprite.spritecollideany(player, coins)
        if coin_collected:
            coins.remove(coin_collected)
            SCORE += coin_collected.weight

        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(f"SCORE: {SCORE}", True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        for entity in [player] + list(enemies) + list(coins):
            DISPLAYSURF.blit(entity.image, entity.rect)

        pygame.display.update()
        FramePerSec.tick(FPS)

    while game_close:
        game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

game_loop()
