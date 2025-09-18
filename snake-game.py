import pygame
import random

pygame.init()

#Constants for Sizing
COLUMN_SIZE = 60
ROW_SIZE = 40
GRID_SIZE= 10

#Constants for object colors 
SCREEN_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
FONT_COLOR = (0, 255, 0)

#Constant for snake initial speed
SPEED = 10

OVER_FONT = pygame.font.SysFont("arial", 50)
RESTART_FONT = pygame.font.SysFont("arial", 30)
SCORE_FONT = pygame.font.SysFont("arial", 20)


#Initialise game screen
screen = pygame.display.set_mode((COLUMN_SIZE*GRID_SIZE, ROW_SIZE*GRID_SIZE))
pygame.display.set_caption('SNAKE')
clock = pygame.time.Clock()


def gameLoop():
    game_over = False

    #Starts snake in middle of screen 
    snake_pos_x = COLUMN_SIZE//2
    snake_pos_y = ROW_SIZE//2
    snake = [[snake_pos_x, snake_pos_y]]

    #Places first food block at random position within grid
    food_pos_x =  random.randint(0, COLUMN_SIZE -1)
    food_pos_y = random.randint(0, ROW_SIZE - 1)
    food = [food_pos_x, food_pos_y]

    #Dictates snake movement speed 
    speed = SPEED

    score = 0

    #Snake initial movement direction is right
    direction = "RIGHT"


    while not game_over:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            
            direction = detect_movement(direction, event)

        #Implements snake movement based off snake head
        head_pos_x, head_pos_y = snake[0]
        head_pos_x, head_pos_y = move_snake(head_pos_x, head_pos_y, direction)
        new_head = [head_pos_x, head_pos_y]

        #Check for snake collisions
        if detect_collision(new_head, snake):
            game_over = True
            break

        snake.insert(0, new_head)

        #Check if food had been eaten 
        food_eaten, food = detect_food_collision(new_head, food)
        if food_eaten:
            #Updates score when food is eaten
            score += 1
        else:
            snake.pop()

        #Draw Screen
        screen.fill((SCREEN_COLOR))

        #Draws snake
        for snake_pos in snake:
            draw_block(snake_pos, (SNAKE_COLOR))

        #Draws food
        draw_block(food, (FOOD_COLOR))

        pygame.display.update()
        clock.tick(speed)
    
    #Initialize Restart Screen
    game_restart(score)



def draw_block(position, color):
    x = position[0] * GRID_SIZE
    y = position[1] * GRID_SIZE

    pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))

def draw_score(score):
    text = SCORE_FONT.render(f"Score: {score}", True, FONT_COLOR)
    screen.blit(text, (10,10))
    

def detect_movement(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP  and direction != "DOWN":
            return "UP"
        elif event.key == pygame.K_DOWN and direction != "UP":
            return "DOWN"
        elif event.key == pygame.K_LEFT and direction != "RIGHT":
            return "LEFT"
        elif event.key == pygame.K_RIGHT and direction != "LEFT":
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

def detect_food_collision(snake_head, food_pos):
    if snake_head == food_pos:
        new_food = [random.randint(0, COLUMN_SIZE - 1), random.randint(0, ROW_SIZE - 1)]
        return True, new_food
    return False, food_pos

def detect_collision(head, body):
    #Detecting collision with self
    if head in body:
        return True

    #Detecting wall collision
    if (head[0] < 0 or 
        head[0] >= COLUMN_SIZE or
        head[1] < 0 or
        head[1] >= ROW_SIZE):
        return True

    return False

def game_restart(score):
    over_text = OVER_FONT.render("GAME OVER", True, (FONT_COLOR))
    restart_text = RESTART_FONT.render("PRESS R to RESTART or Q to QUIT", True, (FONT_COLOR))
    score_text = SCORE_FONT.render(f"SCORE: {score}", True, (FONT_COLOR))
    
    over_rect = over_text.get_rect(center = (COLUMN_SIZE * GRID_SIZE // 2, ROW_SIZE * GRID_SIZE // 2 - 120))
    restart_rect = restart_text.get_rect(center = (COLUMN_SIZE * GRID_SIZE // 2, ROW_SIZE * GRID_SIZE // 2 + 40))
    score_rect = score_text.get_rect(center = (COLUMN_SIZE * GRID_SIZE // 2, ROW_SIZE * GRID_SIZE // 2 - 30))
    


    waiting = True

    while waiting:
        screen.fill(SCREEN_COLOR)
        screen.blit(over_text, over_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(score_text, score_rect)
        pygame.display.update()

        for event in pygame.event.get():
            #Quits game when event changes to QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            #Changes event based on key stroke
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameLoop()
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return


gameLoop()
pygame.quit()