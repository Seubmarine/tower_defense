import pyxel
from vector import Vector2
from const import TILEMAP_DATA

class Entity:
    def __init__(self, x=0, y=0):
        self.position = Vector2(x, y)
        self.velocity = Vector2.ZERO
        self.direction = "right"

    def get_timemap_pos(self):
        return pyxel.tilemap(0).get(self.position.x, self.position.y)
    
    def update(self):
        self.direction = TILEMAP_DATA.get(self.get_timemap_pos())
        if self.direction == "up":
            self.velocity = Vector2.UP
        elif self.direction == "left":
            self.velocity = Vector2.LEFT
        elif self.direction == "down":
            self.velocity = Vector2.DOWN
        elif self.direction == "right":
            self.velocity = Vector2.RIGHT
        else:
            self.velocity = Vector2.RIGHT
        self.position += self.velocity

        

    def draw(self):
        pyxel.rectb(self.position.x * 8, self.position.y * 8, 8, 8, 7)