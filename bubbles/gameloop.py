import pygame
from random import randint
from classes import Ball, Shooter, Bullet

def game_loop(screen):  # Pass the screen as an argument
    # Game loop initialization
    running = True
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    ball = Ball(pygame.Color('blue'), 100, 100, 25)
    all_sprites.add(ball)
    shooter = Shooter(300, 500)
    all_sprites.add(shooter)

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet(shooter.rect.x + 25, shooter.rect.y + 5)
                all_sprites.add(bullet)
                bullets.add(bullet)

        # Update logic
        ball.rect.x += 1
        ball.rect.y += 1
        shooter.rect.x += shooter.speed
        bullets.update()

        # Check for collisions
        hits = pygame.sprite.spritecollide(ball, bullets, True)
        for hit in hits:
            ball.color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
            ball.image.fill(ball.color)
            ball.image.set_colorkey(ball.color)
            pygame.draw.circle(ball.image, ball.color, [ball.radius, ball.radius], ball.radius)

        # Draw everything
        screen.fill(pygame.Color('white'))
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

    # Game loop cleanup
    pygame.quit()

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

# Call the game loop with the screen as an argument
game_loop(screen)
