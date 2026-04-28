import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()
block = 10
speed = 10


x = width // 2
y = height // 2
dx = 0
dy = 0

snake = []
length = 1


food_x = random.randrange(0, width, block)
food_y = random.randrange(0, height, block)

score = 0
font = pygame.font.SysFont(None, 25)

running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -block
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = block
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -block
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = block

    
    x += dx
    y += dy

    
    if x < 0 or x >= width or y < 0 or y >= height:
        running = False

    head = [x, y]
    snake.append(head)

    if len(snake) > length:
        del snake[0]

    
    for segment in snake[:-1]:
        if segment == head:
            running = False

    
    if x == food_x and y == food_y:
        food_x = random.randrange(0, width, block)
        food_y = random.randrange(0, height, block)
        length += 1
        score += 1


    pygame.draw.rect(screen, red, (food_x, food_y, block, block))

    
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], block, block))


    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, [10, 10])

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
