import pygame

COLUMNS = 60
ROWS = 40
BLOCKS = 10

pygame.init()

screen = pygame.display.set_mode((COLUMNS*BLOCKS, ROWS*BLOCKS))

pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()

def gameLoop():
    game_over = False

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        screen.fill((0,0,0))

        pygame.display.update()

        clock.tick(15)

gameLoop()
pygame.quit()