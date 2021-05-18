import time

from network import Network
from testobj import TestObj


def main():
    run = True
    n = Network()
    p = n.getP()

    while run:
        p2 = n.send(p)
        time.sleep(1)

        print(p.getName())


main()
