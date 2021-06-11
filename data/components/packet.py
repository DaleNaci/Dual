class Packet:
    def __init__(self):
        self.player = None
        self.bullets = []


    def unpack(self):
        return (self.player, self.bullets)
