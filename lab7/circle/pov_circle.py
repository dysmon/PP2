import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("pov_circle")

# Object coordinates
x = 250
y = 250

# Main loop
while True:
    screen.fill("white")
    pygame.draw.circle(screen, "red", (x, y), 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x >= 50:
                x -= 20
            elif event.key == pygame.K_RIGHT and x <= 450:
                x += 20
            elif event.key == pygame.K_DOWN and y <= 450:
                y += 20
            elif event.key == pygame.K_UP and y >= 50:
                y -= 20
    pygame.display.update()

