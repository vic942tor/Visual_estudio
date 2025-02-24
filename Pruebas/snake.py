import pygame
import random
import time

# Inicializar pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Definir tamaño de la ventana
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Serpiente")

# Velocidad del juego
clock = pygame.time.Clock()

# Tamaño de los bloques
block_size = 20

# Fuente para el puntaje
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Función para mostrar el puntaje
def display_score(score):
    value = score_font.render("Puntaje: " + str(score), True, WHITE)
    window.blit(value, [0, 0])

# Función para dibujar la serpiente
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Coordenadas iniciales de la serpiente
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Posición inicial de la comida
    foodx = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(BLUE)
            message = font_style.render("¡Perdiste! Presiona Q para salir o C para jugar de nuevo", True, RED)
            window.blit(message, [WIDTH / 6, HEIGHT / 3])
            display_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Verificar si la serpiente toca los bordes
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(BLUE)
        pygame.draw.rect(window, RED, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificar colisión con la propia serpiente
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        # Verificar si la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(15)  # Controlar la velocidad de la serpiente

    pygame.quit()
    quit()

gameLoop()
