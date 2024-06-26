import pygame
import sys
import random
import time

pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
RED=(255,0,0)
WHITE=(255,255,255)

SCREEN_WIDTH = 390
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, RED)
background_image = pygame.image.load("s.png")

DEFAULT_IMAGE_SIZE = (800, 800)
DEFAULT_IMAGE_SIZE_PLAYER = (100, 100)
DEFAULT_IMAGE_SIZE_enemy = (50, 100)
enemy_image = pygame.image.load("e.png")
background = pygame.transform.scale(background_image, DEFAULT_IMAGE_SIZE)
enemy = pygame.transform.scale(enemy_image, DEFAULT_IMAGE_SIZE_enemy)
player_image = pygame.image.load("p.png")
player = pygame.transform.scale(player_image, DEFAULT_IMAGE_SIZE_PLAYER)
coin_image = pygame.image.load("Coin.png")
coin = pygame.transform.scale(coin_image, (50, 50))

DISPLAYSURF = pygame.display.set_mode((390, 600))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
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
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

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

P1 = Player()
E1 = Enemy()
C1 = Coin(weight=1)  # Пример монеты с весом 1

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group() 
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
ADD_COIN = pygame.USEREVENT + 2 
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(ADD_COIN, 3000)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == quit:
            pygame.quit()
            game_over=True
        if event.type == ADD_COIN:
            new_coin_weights = [1, 2, 3]  # Веса новых монет
            new_coin = Coin(weight=random.choice(new_coin_weights))
            coins.add(new_coin)
            all_sprites.add(new_coin)

    coin_collected = pygame.sprite.spritecollideany(P1, coins)
    if coin_collected:
        coins.remove(coin_collected)  
        all_sprites.remove(coin_collected)
        SCORE += coin_collected.weight  # Увеличиваем SCORE на вес монеты

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"SCORE: {SCORE}", True, WHITE)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        game_over = True

    pygame.display.update()
    FramePerSec.tick(FPS)

# После завершения игры показываем надпись "Game Over"
DISPLAYSURF.fill(BLACK)
DISPLAYSURF.blit(game_over_text, (50, SCREEN_HEIGHT // 2))
pygame.display.update()
time.sleep(2)  # Даем игроку увидеть результаты перед завершением
pygame.quit()
sys.exit()
