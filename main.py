import pyxel
from entity import Enemy
from inventory import Inventory

def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()

class App:
    def __init__(self):
        
        pyxel.init(256,256, fps=60)
        pyxel.mouse(True)
        pyxel.load("./assets.pyxres")
        self.entities = [Enemy(0, 6*8)]
        for _ in range(15):
            self.entities.append(Enemy(0,0))
        self.inventory = Inventory(1, 28, 30, 3, pyxel.COLOR_WHITE)
        pyxel.run(update=self.update, draw=self.draw)

    def update(self):
        self.inventory.update()
        update_list(self.entities)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        draw_list(self.entities)
        self.inventory.draw()
    
if __name__ == "__main__":
    App()