class Player:
    def __init__(self, x, y, colors, health):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 5
        self.colors = colors
        self.health = health


    def get_dimensions(self):
        return (self.x, self.y, self.width, self.height)
