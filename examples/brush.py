import pygame
import sys

pygame.init()

# Устанавливаем размеры окна и панели
height = 600
panel_height = 100
width = 800

# Создаем окно и поверхности
window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height - panel_height))
panel = pygame.Surface((width, panel_height))

# Переменная для хранения текущего цвета
COLOR = (0, 0, 255)  # Синий цвет
fill_color = COLOR

# Переменные для хранения координат мыши
prev_pos = None
mouse_pressed = False

# Функция для создания прямоугольника
def draw_cross(x, y, size, color):
    pygame.draw.line(screen, color, (x - size, y - size), (x + size, y + size), 1)
    pygame.draw.line(screen, color, (x - size, y + size), (x + size, y - size), 1)

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                prev_pos = event.pos
                mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    panel.fill((50, 50, 50))  # Задаем цвет панели
    panel.blit(pygame.font.SysFont('Arial', 24).render('Draw a Cross', True, (255, 255, 255)), (10, 40))  # Надпись на панели

    pos = pygame.mouse.get_pos()
    if mouse_pressed:
        draw_cross(pos[0], pos[1] - panel_height, 10, COLOR)

    window.fill((255, 255, 255))  # Задаем цвет окна
    window.blit(panel, (0, 0))
    window.blit(screen, (0, panel_height))

    pygame.display.flip()

pygame.quit()
sys.exit()
