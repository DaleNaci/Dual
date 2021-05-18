import pygame

from network import Network
from player import Player


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dual")


def main():
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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            p.x -= p.vel
        if keys[pygame.K_RIGHT]:
            p.x += p.vel
        if keys[pygame.K_DOWN]:
            p.y += p.vel
        if keys[pygame.K_UP]:
            p.y -= p.vel

        win.fill((0, 0, 0))
        pygame.draw.rect(win, p.colors, p.get_dimensions())
        pygame.draw.rect(win, p2.colors, p2.get_dimensions())
        pygame.display.update()


main()
