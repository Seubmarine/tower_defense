import pyxel
import random
from vector import Vector2
from const import TILEMAP_DATA

class Entity:
    def __init__(self, x=0, y=0):
        self.position = Vector2(x, y)
        # self.speed = random.uniform(0.1, 0.9)
        self.velocity = Vector2.ZERO
        self.direction = "right"

    def get_timemap_pos(self):
        return pyxel.tilemap(0).get(self.position.x / 8, self.position.y / 8)
    
    def random_direction(self, choice1, choise2):
        if bool(random.getrandbits(1)):
                self.velocity = choice1
        else:
            self.velocity = choise2

    def change_velocity(self):
        if self.direction == "up":
            self.velocity = Vector2.UP
        elif self.direction == "left":
            self.velocity = Vector2.LEFT
        elif self.direction == "down":
            self.velocity = Vector2.DOWN
        elif self.direction == "right":
            self.velocity = Vector2.RIGHT
        elif self.direction == "up_down":
            self.random_direction(Vector2.UP, Vector2.DOWN)
        elif self.direction == "left_right":
            self.random_direction(Vector2.RIGHT, Vector2.LEFT)
        elif self.direction == "down_left":
            self.random_direction(Vector2.DOWN, Vector2.LEFT)
        elif self.direction == "down_right":
            self.random_direction(Vector2.DOWN, Vector2.RIGHT)
        elif self.direction == "up_left":
            self.random_direction(Vector2.UP, Vector2.LEFT)
        elif self.direction == "up_right":
            self.random_direction(Vector2.UP, Vector2.RIGHT)
        else:
            self.velocity = Vector2.ZERO

    def update(self):
        if self.position.x % 8 == 0 and self.position.y % 8 == 0:
            self.direction = TILEMAP_DATA.get(self.get_timemap_pos())
            self.change_velocity()
        self.position += self.velocity #* self.speed

    def draw(self):
        pyxel.rectb(self.position.x, self.position.y, 8, 8, 7)