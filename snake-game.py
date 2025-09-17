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

    x1 = COLUMNS/2
    y1 = ROWS/2

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        screen.fill((0,0,0))

        create_block([x1,y1], (SNAKE_COLOR))

        pygame.display.update()

        clock.tick(15)

def create_block(position, color):
    x = position[0] * BLOCKS
    y = position[1] * BLOCKS

    pygame.draw.rect(screen, color, (x, y, BLOCKS, BLOCKS))

gameLoop()
pygame.quit()