import pygame

from .components.player import Player
from .components.bullet import Bullet
from .sockets.network import Network


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def main():
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dual")

    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move(win)

        win.fill((0, 0, 0))
        p.draw(win)
        p2.draw(win)
        pygame.display.update()

        if p.health <= 0:
            pygame.quit()
