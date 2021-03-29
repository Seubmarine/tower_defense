import pyxel
import random
from vector import Vector2
from const import TILEMAP_DATA

class Entity:
    
    def __init__(self, x=0, y=0):
        self.set_coordinate(x, y)
        self.velocity = Vector2.ZERO

    def set_coordinate(self, x, y):
        self.position = Vector2(x, y)
        self.cell_pos = self.position / 8
        self.ratio_pos = (self.position - self.cell_pos*8) / 8

    def update(self):
        while self.ratio_pos.x > 1:
            self.cell_pos.x += 1
            self.ratio_pos.x -= 1
        
        while self.ratio_pos.x < 0:
            self.cell_pos.x -= 1
            self.ratio_pos.x += 1

        while self.ratio_pos.y > 1:
            self.cell_pos.y += 1
            self.ratio_pos.y -= 1
        
        while self.ratio_pos.y < 0:
            self.cell_pos.y -= 1
            self.ratio_pos.y += 1

        self.position = (self.cell_pos + self.ratio_pos) * 8
            
    def draw(self):
        pyxel.rectb(self.position.x, self.position.y, 8, 8, pyxel.COLOR_WHITE)

class Enemy(Entity):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.last_cell_pos = Vector2(-1,-1)
        self.speed = random.uniform(0.05, 0.1)
        self.velocity = Vector2.ZERO
        self.direction = "down"

    def get_timemap_pos(self):
        return pyxel.tilemap(0).get(self.cell_pos.x, self.cell_pos.y)
    
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
        # print("cell: {}, l_cell {}, same : {}".format( self.cell_pos, self.last_cell_pos, self.last_cell_pos == self.cell_pos))
        # print(self.ratio_pos, (self.ratio_pos <= Vector2(0.1, 0.1)) == (True, True))
        if self.cell_pos != self.last_cell_pos and ((self.ratio_pos <= Vector2(0.1, 0.1)) == (True, True)):
            self.direction = TILEMAP_DATA.get(self.get_timemap_pos())
            self.change_velocity()
            self.last_cell_pos = Vector2(self.cell_pos.x, self.cell_pos.y) # idk why i can't use self.last_cell_pos = self.cell_pos for some reason
        self.ratio_pos += self.velocity * self.speed
        
        super().update()

    def draw(self):
        pyxel.rectb(self.position.x, self.position.y, 8, 8, 7)