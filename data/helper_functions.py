from .components.player import Player
from .components.bullet import Bullet


def shoot(p):
    new_bullet = Bullet()

    vely = -6 if p.id==1 else 6
    new_bullet.set_movement(p.x, p.y, p.velx, vely)

    return new_bullet
