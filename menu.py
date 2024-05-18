# import pygame
# import time
# import sys
# import os

# pygame.init()

# # Экран меню
# WIDTH, HEIGHT = 600, 400
# SCREEN_SIZE = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(SCREEN_SIZE)
# pygame.display.set_caption("Меню")

# # Загрузка изображения (текстуры)
# texture_image = pygame.image.load("./assets/texture.jpg") # Замените "texture.png" на путь к вашему изображению

# # Отображение текстуры на экране


# # Константы основных цветов
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)

# # Шрифты
# font = pygame.font.SysFont("Comic Sans", 20)
# menu_font = pygame.font.SysFont("Comic Sans", 40)

# # Переменные для кнопок
# play_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)

# # Функция отрисовки текста
# def draw_text(text, font, color, surface, x, y):
#     text_obj = font.render(text, True, color)
#     text_rect = text_obj.get_rect()
#     text_rect.center = (x, y)
#     surface.blit(text_obj, text_rect)

# # Функция отрисовки меню
# def draw_menu():
#     screen.fill(WHITE)
#     screen.blit(texture_image, (0, 0))
#     draw_text("Меню", menu_font, BLACK, screen, WIDTH // 2, 50)

#     # Отрисовка кнопок

#     pygame.draw.rect(screen, (10, 0, 255), play_button)
#     draw_text("Играть", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

#     pygame.display.flip()

# # Функция для переключения в игру
# def play():
#     pygame.quit()
#     os.system('python main.py')

# # Основной игровой цикл
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 if play_button.collidepoint(event.pos):
#                     play()
#     draw_menu()

# pygame.quit()

import time
import sys
import pygame
import os

class Button:
    def __init__(self, text, font, color, x, y, width, height):
        self.text = text
        self.font = font
        self.default_color = tuple(min(max(c, 0), 255) for c in color)
        self.hover_color = tuple(min(max(c - 50, 0), 255) for c in color)
        self.color = self.default_color
        self.rect = pygame.Rect(x, y, width, height)
        self.is_hovered = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            self.color = self.hover_color if self.is_hovered else self.default_color

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Меню")
        self.texture_image = pygame.image.load("./assets/texture_space.jpg")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.font = pygame.font.SysFont("Comic Sans", 20)
        self.menu_font = pygame.font.SysFont("Comic Sans", 40)

        self.play_button = Button("Играть", self.font, (10, 0, 255), width // 2 - 50, height // 2 - 25, 100, 50)

    def draw_menu(self):
        self.screen.fill(self.WHITE)
        self.screen.blit(self.texture_image, (0, 0))
        self.draw_text("Меню", self.menu_font, self.BLACK, self.screen, self.width // 2, 50)
        self.play_button.draw(self.screen)
        pygame.display.flip()

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    def play(self):
        pygame.quit()
        os.system('python gameplay.py')

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.play_button.update(event)
                if self.play_button.clicked(event):
                    self.play()
            self.draw_menu()

if __name__ == "__main__":
    pygame.init()
    menu = Menu(600, 400)
    menu.run()
    pygame.quit()
