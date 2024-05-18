import pygame
import sys
import random
import os

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 1000, 800
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("game")
clock = pygame.time.Clock()
FPS = 60

texture_image = pygame.image.load("./assets/texture_space.jpg")



player_radius = 10
player_x = HEIGHT // 2
player_y = WIDTH // 2
player_speed = 5

enemy_count = 10
enemy_radius = 50
enemies_x = [random.randint(0, WIDTH) for _ in range(enemy_count)]
enemies_y = [random.randint(0, HEIGHT) for _ in range(enemy_count)]
enemies_speed = 2
enemies_direction_x = [random.choice(['left', 'right']) for _ in range(enemy_count)]
enemies_direction_y = [random.choice(['up', 'down']) for _ in range(enemy_count)]


 

# Добавим переменную для отслеживания времени
current_time = 0

def playing_field():
    screen.fill(BLACK)

def player(x, y):
    pygame.draw.circle(screen, (0, 255, 0), (x, y), player_radius)

def enemy(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), enemy_radius)

def check_collision(x1, y1, r1, x2, y2, r2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance <= r1 + r2

playing_field()
pygame.display.update()

score = 0

running = True

class Coin:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.radius)

    def check_collision(self, player_x, player_y, player_radius):
        distance = ((self.x - player_x) ** 2 + (self.y - player_y) ** 2) ** 0.5
        return distance <= self.radius + player_radius

coins = []
coin_spawn_interval = 2.0
coin_remove_interval = 60.0

def spawn_coin():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = 5
    coin = Coin(x, y, radius)
    coins.append(coin)

coin_spawn_timer = 0
coin_remove_timer = 0

def generate_enemy_coordinates(player_x, player_y, min_distance):
    # Генерируем случайные координаты для врага
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)

    # Проверяем расстояние между врагом и игроком
    distance_to_player = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5

    # Если расстояние меньше минимального допустимого, генерируем новые координаты
    while distance_to_player < min_distance:
        enemy_x = random.randint(0, WIDTH)
        enemy_y = random.randint(0, HEIGHT)
        distance_to_player = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5

    return enemy_x, enemy_y

# Используем функцию generate_enemy_coordinates для генерации координат врагов
for i in range(enemy_count):
    enemies_x[i], enemies_y[i] = generate_enemy_coordinates(player_x, player_y, player_radius + enemy_radius)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    elif keys[pygame.K_d]:
        player_x += player_speed
    elif keys[pygame.K_w]:
        player_y -= player_speed
    elif keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
    elif keys[pygame.K_UP]:
        player_y -= player_speed
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Проверка на границы окна для игрока
    if player_x < player_radius:
        player_x = player_radius
    elif player_x > WIDTH - player_radius:
        player_x = WIDTH - player_radius
    if player_y < player_radius:
        player_y = player_radius
    elif player_y > HEIGHT - player_radius:
        player_y = HEIGHT - player_radius
    
    for i in range(enemy_count):
        if enemies_direction_x[i] == 'left':
            enemies_x[i] -= enemies_speed
        elif enemies_direction_x[i] == 'right':
            enemies_x[i] += enemies_speed

        if enemies_direction_y[i] == 'up':
            enemies_y[i] -= enemies_speed
        elif enemies_direction_y[i] == 'down':
            enemies_y[i] += enemies_speed

        if enemies_x[i] < 0:
            enemies_x[i] = 0
            enemies_direction_x[i] = 'right'
        elif enemies_x[i] > WIDTH:
            enemies_x[i] = WIDTH
            enemies_direction_x[i] = 'left'

        if enemies_y[i] < 0:
            enemies_y[i] = 0
            enemies_direction_y[i] = 'down'
        elif enemies_y[i] > HEIGHT:
            enemies_y[i] = HEIGHT
            enemies_direction_y[i] = 'up'

    coin_spawn_timer += 1 / FPS
    coin_remove_timer += 1 / FPS
    if coin_spawn_timer >= coin_spawn_interval:
        spawn_coin()
        coin_spawn_timer = 0

    if coin_remove_timer >= coin_remove_interval:
        coins.clear()
        coin_remove_timer = 0
    
    

    playing_field()
    player(player_x, player_y)
    for i in range(enemy_count):
        enemy(enemies_x[i], enemies_y[i])
        # Проверка столкновения игрока с противником
        if check_collision(player_x, player_y, player_radius, enemies_x[i], enemies_y[i], enemy_radius):
            print("Game Over!")
            running = False
    


    for coin in coins:
        coin.draw(screen)
        if coin.check_collision(player_x, player_y, player_radius):
            score += 1
            coins.remove(coin)


    # Увеличиваем время на один кадр
    current_time += 1 / FPS

    # Отображаем время в углу окна
    font = pygame.font.SysFont("Comic Sans", 36)
    time_text = font.render(f"Время: {int(current_time)}", True, WHITE)
    screen.blit(time_text, (10, 10))

    score_text = font.render(f"Счёт: {int(score)}", True, WHITE)
    screen.blit(score_text, (850, 10))

    pygame.display.update()

    clock.tick(FPS)
    

pygame.quit()
os.system("python menu.py")
sys.exit()

