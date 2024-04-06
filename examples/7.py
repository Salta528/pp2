import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(100, 10, 60, 60))
done = False
 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
"""
import pygame. Это, конечно же, необходимо для доступа к фреймворку PyGame.
pygame.init(). Этот вызов инициализирует все модули, необходимые для работы с PyGame.
pygame.display.set_mode((width, height)). Это создает окно заданного размера. Возвращаемое значение — это объект Surface, над котором вы будете выполнять графические операции.
pygame.event.get(). Этот вызов очищает очередь событий. Если вы не вызовете его, сообщения от операционной системы начнут накапливаться, и ваша игра станет неотзывчивой.
pygame.QUIT. Это тип события, который генерируется при нажатии на кнопку закрытия в углу окна.
pygame.display.flip(). PyGame использует двойной буфер, а этот вызов обменивает буферы. Вам просто нужно знать, что этот вызов необходим, чтобы любые обновления, которые вы вносите в коде, стали видимыми.
"""
