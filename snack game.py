# Made By AKShaheen <abdelazizshaheen162@gmail.com> For Python Workshop In Cic
# Forked by 

import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BGCOLOR = (57, 0, 153)
TEXT_COLOR = (255, 255, 179)
FOOD_COLOR = (220,171,107)
SNAKE_COLOR = (255, 0, 84)

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20
SNAKE_BODY = [(WIDTH / 2, HEIGHT / 2)]
SNAKE_DIRECTION = (1, 0)

# Food properties
FOOD_SIZE = 20
food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))

# Score
score = 0
highest_score = 0

# Load font
font = pygame.font.Font(None, 36)

# Function to display score
def display_score():
    score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    WINDOW.blit(score_text, (10, 10))

# Function to display highest score
def display_highest_score():
    highest_score_text = font.render("Highest Score: " + str(highest_score), True, TEXT_COLOR)
    WINDOW.blit(highest_score_text, (WIDTH - highest_score_text.get_width() - 10, 10))

# Function to reset game
def reset_game():
    global SNAKE_BODY, SNAKE_DIRECTION, score, food_pos
    SNAKE_BODY = [(WIDTH / 2, HEIGHT / 2)]
    SNAKE_DIRECTION = (1, 0)
    food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
    # Display Game Over message
    game_over_text = font.render("Game Over", True, TEXT_COLOR)
    game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    WINDOW.blit(game_over_text, game_over_rect)
    # Display final score
    final_score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    final_score_rect = final_score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    WINDOW.blit(final_score_text, final_score_rect)
    # Update highest score
    global highest_score
    if score > highest_score:
        highest_score = score
    # Display highest score
    highest_score_text = font.render("Highest Score: " + str(highest_score), True, TEXT_COLOR)
    highest_score_rect = highest_score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
    WINDOW.blit(highest_score_text, highest_score_rect)
    # Update display
    pygame.display.update()
    # Wait for a few seconds before resetting the game
    pygame.time.wait(3000)
    score = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction based on key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP and SNAKE_DIRECTION != (0, 1):
                SNAKE_DIRECTION = (0, -1)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN and SNAKE_DIRECTION != (0, -1):
                SNAKE_DIRECTION = (0, 1)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT and SNAKE_DIRECTION != (1, 0):
                SNAKE_DIRECTION = (-1, 0)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and SNAKE_DIRECTION != (-1, 0):
                SNAKE_DIRECTION = (1, 0)

    # Move the snake
    new_head = (SNAKE_BODY[0][0] + SNAKE_SPEED * SNAKE_DIRECTION[0],
                SNAKE_BODY[0][1] + SNAKE_SPEED * SNAKE_DIRECTION[1])
    SNAKE_BODY.insert(0, new_head)

    # Check for collision with food
    if pygame.Rect(new_head, (SNAKE_SIZE, SNAKE_SIZE)).colliderect(pygame.Rect(food_pos, (FOOD_SIZE, FOOD_SIZE))):
        score += 1
        if score > highest_score:
            highest_score = score
        food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
    else:
        SNAKE_BODY.pop()

    # Check for collision with walls or itself
    if (SNAKE_BODY[0][0] < 0 or SNAKE_BODY[0][0] >= WIDTH or
        SNAKE_BODY[0][1] < 0 or SNAKE_BODY[0][1] >= HEIGHT or
     len(SNAKE_BODY) != len(set(SNAKE_BODY))):
        reset_game()

    # Draw everything
    WINDOW.fill(BGCOLOR)
    pygame.draw.rect(WINDOW, FOOD_COLOR, (*food_pos, FOOD_SIZE, FOOD_SIZE))

    for segment in SNAKE_BODY:
        pygame.draw.rect(WINDOW, SNAKE_COLOR, (*segment, SNAKE_SIZE, SNAKE_SIZE))

    display_score()
    display_highest_score()
    pygame.display.update()
    clock.tick(10)
pygame.quit()
