import pygame

COLUMNS = 60
ROWS = 40
BLOCKS = 10

SNAKE_COLOR = (0, 255, 0)


pygame.init()

screen = pygame.display.set_mode((COLUMNS*BLOCKS, ROWS*BLOCKS))

pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()

def gameLoop():
    game_over = False

    snake_pos_x = COLUMNS/2
    snake_pos_y = ROWS/2

    direction = "RIGHT"
    while not game_over:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            
            direction = detect_movement(direction, event)

        snake_pos_x, snake_pos_y = move_snake(snake_pos_x, snake_pos_y, direction)
        
        screen.fill((0,0,0))

        create_block([snake_pos_x, snake_pos_y], (SNAKE_COLOR))

        pygame.display.update()

        clock.tick(15)

def create_block(position, color):
    x = position[0] * BLOCKS
    y = position[1] * BLOCKS

    pygame.draw.rect(screen, color, (x, y, BLOCKS, BLOCKS))

def detect_movement(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP :
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
        elif event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
    return direction;

def move_snake(pos_x, pos_y, direction):
    if direction == "UP":
        pos_y = pos_y - 1;
    if direction == "DOWN":
        pos_y = pos_y + 1;
    if direction == "LEFT":
        pos_x = pos_x - 1;
    if direction == "RIGHT":
        pos_x = pos_x + 1;

    return[pos_x, pos_y]

gameLoop()
pygame.quit()