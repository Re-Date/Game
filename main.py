# import pygame
# import time
# import sys
# import os

# pygame.init()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)



# # Экран меню
# WIDTH, HEIGHT = 1000, 800
# SCREEN_SIZE = (WIDTH, HEIGHT)
# screen = pygame.display.set_mode(SCREEN_SIZE)
# pygame.display.set_caption("game")
# clock = pygame.time.Clock()
# FPS = 60

# x = HEIGHT // 2
# y = WIDTH // 2

# def playing_field():
#     screen.fill(WHITE)

#     pygame.display.flip()


# def player():
#     pygame.draw.circle(screen, BLACK, (x, y), 20)

# playing_field()
# player()
# pygame.display.update()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False 
            
        


        
#     player()
#     pygame.display.update()
#     keys = pygame.key.get_pressed()
    

#     if keys[pygame.K_a]:
        
#         x -= 3
#     elif keys[pygame.K_d]:
#         x += 3
#     elif keys[pygame.K_w]:
#         y -= 3
#     elif keys[pygame.K_s]:
#         y += 3
    
#     clock.tick(FPS)   


# pygame.quit()



import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 1000, 800
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("game")
clock = pygame.time.Clock()
FPS = 60

x = HEIGHT // 2
y = WIDTH // 2

def playing_field():
    screen.fill(WHITE)

def player(x, y):
    pygame.draw.circle(screen, BLACK, (x, y), 20)

playing_field()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 3
    elif keys[pygame.K_d]:
        x += 3
    elif keys[pygame.K_w]:
        y -= 3
    elif keys[pygame.K_s]:
        y += 3
    
    playing_field()  # Очищаем экран перед перерисовкой
    player(x, y)  # Рисуем новый круг
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
