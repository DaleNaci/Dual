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

        playerX_change = movementX(p, p2)
        playerY_change = movementY(p, p2)

        win.fill((0, 0, 0))
        p.draw()
        p2.draw()

        if bullet.is_ready():
            bullet.set_movement(
                p2.x + 22.5,
                p2.y,
                playerX_change,
                playerY_change + 6
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


def movementX(p, p2):
    keys = pygame.key.get_pressed()
    retVal = 0

    if keys[pygame.K_LEFT]:
        if (p.x >= p.vel_x):
            p.x -= p.vel_x
    if keys[pygame.K_RIGHT]:
        if (p.x <= 450-p.vel_x):
            p.x += p.vel_x

    if keys[pygame.K_a]:
        if (p2.x >= p.vel_x):
            p2.x -= p2.vel_x
            retVal = -p2.vel_x
    if keys[pygame.K_d]:
        if (p2.x <= 450-p.vel_x):
            p2.x += p2.vel_x
            retVal = p2.vel_x

    return retVal


def movementY(p, p2):
    keys = pygame.key.get_pressed()
    retVal = 0

    if keys[pygame.K_DOWN]:
        if (p.y <= 200-p.vel_y):
            p.y += p.vel_y
    if keys[pygame.K_UP]:
        if (p.y >= p.vel_y):
            p.y -= p.vel_y

    if keys[pygame.K_s]:
        if (p2.y <= 450-p.vel_y):
            p2.y += p2.vel_y
            retVal = -p2.vel_y/2
    if keys[pygame.K_w]:
        if (p2.y >= 250+p.vel_y):
            p2.y -= p2.vel_y
            retVal = p2.vel_y/2

    return retVal


main()
