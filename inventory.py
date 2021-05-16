import pyxel
from vector import Vector2

def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()

def detect_collision(r1, rd1, r2, rd2):
    return r1.x + rd1.x >= r2.x and r1.x <= r2.x + rd2.x and r1.y + rd1.y >= r2.y and r1.y <= r2.y + rd2.y

class Selectable:
    def __init__(self, x, y, w, h, color):
        self.position = Vector2(x, y) * 8
        self.size = Vector2(w, h) * 8
        self.color = color
    
    def check_collision(self, vector2_pos, vector2_size):
        return detect_collision(self.position, self.size, vector2_pos, vector2_size)

    def update(self):
        pass
        # if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON,0,0):
        #     print(Vector2(pyxel.mouse_x, pyxel.mouse_y))
        #     print(self.check_collision(Vector2(pyxel.mouse_x, pyxel.mouse_y), Vector2(0,0)))
            # print(detect_collision( self.position, self.size ))

    def draw(self):
        pyxel.rectb(self.position.x , self.position.y , self.size.x , self.size.y , self.color)

class Item():
    def __init__(self, item_type):
        self.no_sprite = [(0,0)]
        self.simple_arrow_sprite = [(8,0), (16,0), (24,0), (32,0)]
        self.double_arrow_sprite = [(40,0), (48,0), (56,0), (64,0),(72,0),(80,0)]
        self.pusher_sprite = [0,8]
        self.current_sprite_list = self.no_sprite
        self.current_sprite = self.current_sprite_list[0]
        self.index = 0
        self.set_type(item_type)

    def get_sprite(self, index):
        self.index += index
        self.current_sprite = self.current_sprite_list[self.index % len(self.current_sprite_list)]
        self.tilemap_index = (self.current_sprite[0] / 8, self.current_sprite[0] / 8)
    
    def get_timemap_index(self):
        self.tilemap_index = (self.current_sprite[0] / 8, self.current_sprite[0] / 8)
        return self.tilemap_index

    def set_type(self, item_type):
        """Can be "simple_arrow", "double_arrow", "pusher" """
        self.type = item_type
        self.index = 0
        if self.type == None:
            self.current_sprite_list = [(0,0), (0,0), (0,0), (0,0)]
        elif self.type == "simple_arrow":
            self.current_sprite_list = self.simple_arrow_sprite
        elif self.type == "double_arrow":
            self.current_sprite_list = self.double_arrow_sprite
        elif self.type == "pusher":
            self.current_sprite_list = self.pusher_sprite
        self.tilemap_index = (self.current_sprite[0] / 8, self.current_sprite[0] / 8)
        self.get_sprite(0)
    
    def draw(self):
        pyxel.blt(pyxel.mouse_x-8,pyxel.mouse_y-8, 0, self.current_sprite[0], self.current_sprite[1], 8, 8, 0)


class Inventory(Selectable):
    def __init__(self, x, y, w, h, color):
        super().__init__(x,y,w,h,color)
        self.slot = []
        self.selected_item = Item(None)
        self._last_pos = self.position.x + 4
        # for i in range(9):
        #     self.slot.append(Selectable(self._last_pos + i, self.position.y+2, 4, self.size.y, pyxel.COLOR_PEACH))
        #     self._last_pos = self._last_pos + i

    def update(self):
        super().update()
        if pyxel.btnp(pyxel.KEY_R):
            self.selected_item.get_sprite(1)
        elif pyxel.btnp(pyxel.KEY_A):
            self.selected_item.get_sprite(-1)
        elif pyxel.btnp(pyxel.KEY_E):
            self.selected_item.get_sprite(1)

        if pyxel.btnp(pyxel.KEY_1):
            self.selected_item.set_type("simple_arrow")
        elif pyxel.btnp(pyxel.KEY_2):
            self.selected_item.set_type("double_arrow")
        elif pyxel.btnp(pyxel.KEY_2):
            self.selected_item.set_type("pusher")
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            # print(pyxel.tilemap(0).get())
            # pyxel.tilemap(0).set(pyxel.mouse_x//8, pyxel.mouse_y//8, 2)
            # print(*self.selected_item.get_timemap_index(), pyxel.tilemap(0).get(0,0))
            # test = self.selected_item.get_timemap_index()
            test = (16,16)
            print( pyxel.image(0).get(test[0], test[1]) )
            print(pyxel.tilemap(0).refimg)
            pyxel.tilemap(0).set( pyxel.mouse_x//8, pyxel.mouse_y//8, pyxel.image(0).get(test[0], test[1]) )
            
        update_list(self.slot)

    def draw(self):
        super().draw()
        draw_list(self.slot)
        self.selected_item.draw()