import pygame
import time
import sys
import os

pygame.init()

# Экран меню
WIDTH, HEIGHT = 600, 400
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Меню")

# Загрузка изображения (текстуры)
texture_image = pygame.image.load("./assets/texture.jpg") # Замените "texture.png" на путь к вашему изображению

# Отображение текстуры на экране


# Константы основных цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифты
font = pygame.font.SysFont("Comic Sans", 20)
menu_font = pygame.font.SysFont("Comic Sans", 40)

# Переменные для кнопок
play_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)

# Функция отрисовки текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Функция отрисовки меню
def draw_menu():
    screen.fill(WHITE)
    screen.blit(texture_image, (0, 0))
    draw_text("Меню", menu_font, BLACK, screen, WIDTH // 2, 50)

    # Отрисовка кнопок

    pygame.draw.rect(screen, (10, 0, 255), play_button)
    draw_text("Играть", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

    pygame.display.flip()

# Функция для переключения в игру
def play():
    pygame.quit()
    os.system('python main.py')

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button.collidepoint(event.pos):
                    play()
    draw_menu()

pygame.quit()