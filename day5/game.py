import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font
font = pygame.font.SysFont(None, 25)

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the clock
clock = pygame.time.Clock()

# Set the snake dimensions
snake_size = 10

# Set the game loop
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = screen_width / 2
    y1 = screen_height / 2
 
    x1_change = 0
    y1_change = 0
 
    food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    # Set the initial snake length
    snake_List = []
    Length_of_snake = 1
    
    while not game_over:
 
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
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
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
 
        # Check for collision with walls
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
 
        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Draw the snake and the food
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        # Draw the snake body
        for segment in snake_List:
            pygame.draw.rect(screen, black, [segment[0], segment[1], snake_size, snake_size])
 
        # Update the score
        score(Length_of_snake - 1)
        pygame.display.update()
 
        # Check for collision with food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1
 
        # Set the game speed
        clock.tick(10)
 
    pygame.quit()
    quit()
 
# Display the message
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])
 
# Display the score
def score(score):
    value = font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0, 0])
 
gameLoop()