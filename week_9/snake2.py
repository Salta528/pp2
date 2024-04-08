import pygame
import sys
import random

pygame.init()

possible_possition = [(i, j) for i in range(34) for j in range(24)]
possible_possition.append((-1, -1))

window = pygame.display.set_mode((850, 600))

# Функция для движения змейки в зависимости от направления
def snake_move(direct, snake):
    if direct == 0:
        snake.insert(0, (snake[0][0]+1, snake[0][1]))  # Движение вправо
    elif direct == 1:
        snake.insert(0, (snake[0][0], snake[0][1]+1))  # Движение вниз
    elif direct == 2:
        snake.insert(0, (snake[0][0]-1, snake[0][1]))  # Движение влево
    else:
        snake.insert(0, (snake[0][0], snake[0][1]-1))  # Движение вверх
    try:
        possible_possition.remove(snake[0])
    except:
        return True  # Возвращаем True, если змейка упирается в саму себя
    possible_possition.append(snake[-1])
    snake.pop()

GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake = [(6, 4), (5, 4)]  # Изначальное положение змейки
for i in snake:
    possible_possition.remove(i)

ax = 4  # Координаты для отображения яблока
ay = 18

direct = 0  # Направление движения змейки (0 - вправо, 1 - вниз, 2 - влево, 3 - вверх)

clock = pygame.time.Clock()
fps = 5  # Количество кадров в секунду

fail = False  # Переменная для проверки проигрыша

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and direct != 1:
                direct = 3  # Движение вверх
            elif e.key == pygame.K_DOWN and direct != 3:
                direct = 1  # Движение вниз
            elif e.key == pygame.K_LEFT and direct != 0:
                direct = 2  # Движение влево
            elif e.key == pygame.K_RIGHT and direct != 2:
                direct = 0  # Движение вправо

    fail = snake_move(direct, snake)  # Проверка на проигрыш

    if snake[0][0] == ax and snake[0][1] == ay:  # Если змейка достигла яблока
        snake.append((-1, -1))  # Добавляем новый сегмент змейки
        possible_possition.remove((-1, -1))
        a = random.choice(possible_possition)
        ax = a[0]
        ay = a[1]

    while fail:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    window.fill((0, 0, 0))  # Заливка окна черным цветом
    pygame.draw.rect(window, RED, (25*ax, 25*ay, 25, 25))  # Отображение яблока
    for i in range(len(snake)):
            pygame.draw.rect(window, GREEN, (snake[i][0]*25, snake[i][1]*25, 25, 25))  # Отображение змейки
    pygame.display.update()  # Обновление экрана
    clock.tick(fps)  # Ограничение кадров в секунду
