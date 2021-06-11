import pygame

from .components.player import Player
from .components.bullet import Bullet
from .sockets.network import Network
from .helper_functions import shoot


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dual")

    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    bullets = []
    shoot_reset = True

    while run:
        clock.tick(60)

        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shoot_reset:
            bullets.append(shoot(p))
            shoot_reset = False
        elif not keys[pygame.K_SPACE]:
            shoot_reset = True

        p.move(win)

        win.fill((0, 0, 0))

        p.draw(win)
        p2.draw(win)

        for b in bullets:
            b.move(win)
            b.draw(win)

            if p.get_rect().colliderect(b.get_rect()):
                print("Here")

        pygame.display.update()

        if p.health <= 0:
            pygame.quit()
