import pyxel
from entity import Entity

def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()

class App:
    def __init__(self):
        pyxel.init(255,255, fps=60)
        pyxel.load("./assets.pyxres")
        self.entities = [Entity(0, 8), Entity(4, 8)]
        pyxel.run(update=self.update, draw=self.draw)

    def update(self):
        update_list(self.entities)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        draw_list(self.entities)
    
if __name__ == "__main__":
    App()