import pygame

from .components.player import Player
from .components.bullet import Bullet


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dual")


def main():
    run = True
    clock = pygame.time.Clock()
    starting_health = 250
    p = Player(win, 0, 0, (starting_health, 0, 0), starting_health)
    p2 = Player(win, 450, 450, (0, starting_health, 0), starting_health)
    bullet = Bullet(win)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move()
        p2.move()

        win.fill((0, 0, 0))
        p.draw()
        p2.draw()

        if bullet.is_ready():
            bullet.set_movement(
                p2.x + 22.5,
                p2.y,
                p2.velx,
                6
            )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and bullet.is_ready():
            bullet.ready = False
            bullet.draw()

        if not bullet.is_ready():
            bullet.draw()
            bullet.move()
            if bullet.y + 5 >= p.y and bullet.y < p.y + 50:
                if bullet.x + 5 >= p.x and bullet.x < p.x + 50:
                    p.health -= 50
                    p.colors = (p.health, 0, 0)
                    bullet.ready = True

        pygame.display.update()

        if p.health <= 0:
            pygame.quit()


main()
