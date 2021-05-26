import pygame

from player import Player


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dual")


def main():
    run = True
    clock = pygame.time.Clock()
    pHealth = 250
    p2Health = 250
    p = Player(0, 0, (pHealth, 0, 0))
    p2 = Player(450, 450, (0, p2Health, 0))
    bullet_state = "ready"
    while run:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        playerX_change = movementX(p, p2)
        playerY_change = movementY(p, p2)

        win.fill((0, 0, 0))
        pygame.draw.rect(win, p.colors, p.get_dimensions())
        pygame.draw.rect(win, p2.colors, p2.get_dimensions())

        if bullet_state is "ready":
            bulletX = p2.x + 22.5
            bulletY = p2.y
            bulletX_change = playerX_change
            bulletY_change = 6 + playerY_change

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and bullet_state is "ready":
            bullet_state = "fire"
            fireBullet(bulletX, bulletY)

        if bullet_state is "fire":
            fireBullet(bulletX, bulletY)
            bulletX += bulletX_change
            bulletY -= bulletY_change
            if bulletX < 0 or bulletX > 500 or bulletY < 0:
                bullet_state = "ready"
            if bulletY + 5 >= p.y and bulletY < p.y + 50:
                if bulletX + 5 >= p.x and bulletX < p.x + 50:
                    pHealth -= 50
                    p.colors = (pHealth, 0, 0)
                    bullet_state = "ready"

        pygame.display.update()

        if pHealth <= 0:
            pygame.quit()


def movementX(p, p2):
    keys = pygame.key.get_pressed()
    retVal = 0

    if keys[pygame.K_LEFT]:
        if (p.x >= p.vel):
            p.x -= p.vel
    if keys[pygame.K_RIGHT]:
        if (p.x <= 450-p.vel):
            p.x += p.vel

    if keys[pygame.K_a]:
        if (p2.x >= p.vel):
            p2.x -= p2.vel
            retVal = -p2.vel
    if keys[pygame.K_d]:
        if (p2.x <= 450-p.vel):
            p2.x += p2.vel
            retVal = p2.vel

    return retVal


def movementY(p, p2):
    keys = pygame.key.get_pressed()
    retVal = 0

    if keys[pygame.K_DOWN]:
        if (p.y <= 200-p.vel):
            p.y += p.vel
    if keys[pygame.K_UP]:
        if (p.y >= p.vel):
            p.y -= p.vel

    if keys[pygame.K_s]:
        if (p2.y <= 450-p.vel):
            p2.y += p2.vel
            retVal = -p2.vel/2
    if keys[pygame.K_w]:
        if (p2.y >= 250+p.vel):
            p2.y -= p2.vel
            retVal = p2.vel/2

    return retVal


def fireBullet(x,y):
    #global bullet_state
    #bullet_state = "fire"
    pygame.draw.rect(win, (0,255,0), (x, y, 5, 5))


main()
