import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()

# Задание FPS
FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)

SCREEN_WIDTH = 390
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background_image = pygame.image.load(r"s.png")

DEFAULT_IMAGE_SIZE = (800, 800)
DEFAULT_IMAGE_SIZE_PLAYER = (100, 100)
DEFAULT_IMAGE_SIZE_enemy = (50, 100)
enemy_image = pygame.image.load(r"e.png")
background = pygame.transform.scale(background_image, DEFAULT_IMAGE_SIZE)
enemy = pygame.transform.scale(enemy_image, DEFAULT_IMAGE_SIZE_enemy)
player_image = pygame.image.load(r"p.png")
player = pygame.transform.scale(player_image, DEFAULT_IMAGE_SIZE_PLAYER)
coin_image = pygame.image.load(r"Coin.png")
coin = pygame.transform.scale(coin_image, (50, 50))

DISPLAYSURF = pygame.display.set_mode((390, 600))
pygame.display.set_caption("Game")

# Создание классов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

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
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Создание спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group() 
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Добавление пользовательских событий
INC_SPEED = pygame.USEREVENT + 1
ADD_COIN = pygame.USEREVENT + 2 
pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(ADD_COIN, 3000)

# Игровой цикл
while True:
    # Обработка всех возникающих событий
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == ADD_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    # Проверка на столкновение игрока с монетой
    coin_collected = pygame.sprite.spritecollideany(P1, coins)
    if coin_collected:
        coins.remove(coin_collected)  
        all_sprites.remove(coin_collected)
        SCORE += 1  

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Движение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Обработка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)