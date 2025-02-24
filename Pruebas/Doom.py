import pygame
import random
import math
import os
import time

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DOOM 2D Pixelado")

# FPS y reloj
clock = pygame.time.Clock()
FPS = 60

# Tamaño del jugador y enemigos
PLAYER_SIZE = 40
ENEMY_SIZE = 40
POWERUP_SIZE = 30

# Cargar imágenes
directorio_script = os.path.dirname(os.path.abspath(__file__))
BOMBILLA = os.path.join(directorio_script, "Bombilla.png")
ZOMBIE = os.path.join(directorio_script, "zombie.png")
player_image = pygame.image.load(BOMBILLA)
enemy_image = pygame.image.load(ZOMBIE)
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

# Variables del jugador
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_health = 100

# Variables de los enemigos
enemy_speed = 2
enemies = []

# Variables de disparo
bullets = []
bullet_speed = 10

# Variables de mejoras
powerups = []

# Variables para los poderes
has_rotating_squares = False
has_line_power = False
line_timer = 0
rotation_squares = []

# Fuente para el texto
font = pygame.font.SysFont("Arial", 24)

# Variable para el contador de enemigos derrotados
defeated_enemies = 0

# Función para mostrar texto
def draw_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Clase para el enemigo
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50

    def move_towards_player(self):
        angle = math.atan2(player_y - self.y, player_x - self.x)
        self.x += enemy_speed * math.cos(angle)
        self.y += enemy_speed * math.sin(angle)

    def draw(self):
        screen.blit(enemy_image, (self.x, self.y))

# Clase para las balas
class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += bullet_speed * math.cos(self.angle)
        self.y += bullet_speed * math.sin(self.angle)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 5, 5))

# Clase para las mejoras
class PowerUp:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == "rotate":
            pygame.draw.rect(screen, GREEN, (self.x, self.y, POWERUP_SIZE, POWERUP_SIZE))
        elif self.type == "line":
            pygame.draw.rect(screen, GREEN, (self.x, self.y, POWERUP_SIZE, POWERUP_SIZE))
        elif self.type == "heal":
            pygame.draw.rect(screen, GREEN, (self.x, self.y, POWERUP_SIZE, POWERUP_SIZE))

# Función para manejar la entrada del jugador
def handle_input():
    global player_x, player_y
    keys = pygame.key.get_pressed()
    
    # Limitar movimiento dentro de la ventana
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < HEIGHT - PLAYER_SIZE:
        player_y += player_speed

# Función para disparar
def shoot():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - player_y, mouse_x - player_x)
    bullet = Bullet(player_x + PLAYER_SIZE // 2, player_y + PLAYER_SIZE // 2, angle)
    bullets.append(bullet)

# Función para generar enemigos sin que aparezcan cerca del jugador
def generate_enemy():
    while True:
        enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)
        # Asegurarse de que el enemigo no aparezca cerca del jugador
        if abs(enemy_x - player_x) > 100 and abs(enemy_y - player_y) > 100:
            break
    enemies.append(Enemy(enemy_x, enemy_y))

# Función para generar mejoras aleatorias
def generate_powerup():
    powerup_type = random.choice(["rotate", "line", "heal"])
    powerup_x = random.randint(0, WIDTH - POWERUP_SIZE)
    powerup_y = random.randint(0, HEIGHT - POWERUP_SIZE)
    powerups.append(PowerUp(powerup_x, powerup_y, powerup_type))

# Función principal del juego
def game_loop():
    global player_x, player_y, player_health, defeated_enemies, enemies
    global has_rotating_squares, has_line_power, line_timer, rotation_squares

    # Generar enemigos si no hay suficientes enemigos
    while len(enemies) < 3 + defeated_enemies:  # Aumenta el número de enemigos a medida que matas
        generate_enemy()

    # Generar mejoras de vez en cuando
    if random.random() < 0.01:  # Baja probabilidad para evitar demasiadas mejoras
        generate_powerup()

    # Loop principal del juego
    game_running = True
    while game_running:
        screen.fill(BLACK)
        draw_text(f"Health: {player_health}", font, WHITE, 10, 10)
        draw_text(f"Enemies Defeated: {defeated_enemies}", font, WHITE, 10, 40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Tecla espacio para disparar
                    shoot()

        # Movimiento del jugador
        handle_input()

        # Mover enemigos
        for enemy in enemies[:]:
            enemy.move_towards_player()
            enemy.draw()

            # Colisión con el jugador
            if pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE).colliderect(pygame.Rect(enemy.x, enemy.y, ENEMY_SIZE, ENEMY_SIZE)):
                player_health -= 1  # El jugador pierde salud si toca un enemigo

        # Mover balas
        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()

            # Verificar colisión con enemigos
            for enemy in enemies[:]:
                if pygame.Rect(bullet.x, bullet.y, 5, 5).colliderect(pygame.Rect(enemy.x, enemy.y, ENEMY_SIZE, ENEMY_SIZE)):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    defeated_enemies += 1  # Aumentar el contador de enemigos derrotados

                    # Generar nuevos enemigos de forma exponencial
                    additional_enemies = random.randint(1, defeated_enemies)  # Aumentar la cantidad de enemigos
                    for _ in range(additional_enemies):
                        generate_enemy()
                    break

        # Verificar si se recoge una mejora
        for powerup in powerups[:]:
            if pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE).colliderect(pygame.Rect(powerup.x, powerup.y, POWERUP_SIZE, POWERUP_SIZE)):
                powerups.remove(powerup)
                if powerup.type == "rotate":
                    has_rotating_squares = True
                    rotation_squares = [pygame.Rect(player_x, player_y, 5, 5) for _ in range(4)]
                elif powerup.type == "line":
                    has_line_power = True
                    line_timer = time.time()  # Resetear el temporizador
                elif powerup.type == "heal":
                    player_health += 20  # Curar al jugador

        # Dibujar al jugador
        screen.blit(player_image, (player_x, player_y))

        # Rotación de cuadrados alrededor del jugador
        if has_rotating_squares:
            angle = 0
            for rect in rotation_squares:
                rect.x = player_x + math.cos(math.radians(angle)) * 50 - 5
                rect.y = player_y + math.sin(math.radians(angle)) * 50 - 5
                pygame.draw.rect(screen, GREEN, rect)
                angle += 90

        # Línea de destrucción
        if has_line_power:
            line_start = (player_x + PLAYER_SIZE // 2, player_y + PLAYER_SIZE // 2)
            line_end = (line_start[0] + 1000 * math.cos(math.radians(0)), line_start[1] + 1000 * math.sin(math.radians(0)))
            pygame.draw.line(screen, WHITE, line_start, line_end, 5)

            # Verificar colisión de la línea con enemigos
            for enemy in enemies[:]:
                if pygame.Rect(enemy.x, enemy.y, ENEMY_SIZE, ENEMY_SIZE).colliderect(pygame.Rect(line_start[0], line_start[1], line_end[0] - line_start[0], line_end[1] - line_start[1])):
                    enemies.remove(enemy)
                    defeated_enemies += 1
                    # Generar nuevos enemigos de forma exponencial
                    additional_enemies = random.randint(1, defeated_enemies)  # Aumentar la cantidad de enemigos
                    for _ in range(additional_enemies):
                        generate_enemy()

            # Reiniciar el temporizador de la línea de destrucción
            line_timer = time.time()  # Reiniciar el temporizador

        # Verificar si el temporizador de la línea de destrucción ha expirado
        if has_line_power and time.time() - line_timer >= 3:
            has_line_power = False  # Desactivar el poder de línea después de 3 segundos

        # Dibujar mejoras
        for powerup in powerups:
            powerup.draw()

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Iniciar el bucle del juego
if __name__ == "__main__":
    game_loop()
            #
