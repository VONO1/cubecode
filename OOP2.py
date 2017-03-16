from random import randrange


class Ship(object):
    def __init__(self, tp, x=-1, y=-1, rotation=0):
        self.type = tp
        self.x = x
        self.y = y
        self.rotation = rotation

        self.hp = self.type

    def attack(self):
        self.hp -= 1

    def coords(self):
        x = self.x
        y = self.y
        r = self.rotation
        return((x + i *r, y + i * (1 - r)) for i in range(self.type))

    def is_killed(self):
        return not self.hp

class Field(object):
    SHOT_MISSED = 1
    SHOT_INJURED = 2
    SHOT_KILLED = 3
    SHOT_HALO = 4

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.ships = []
        self.shots = {}

    def add_ship(self, ship):
        if not isinstance(ship, Ship):
            return False

        if not self.check_pos(ship):
            return False
        self.ships.append(ship)
        #корабль влез
        return True

    def check_pos(self,ship):
        coords = list(ship.coords())
        if not self.isset_cell(*coords[0]) or not self.issert_cell(coords[-1]):# если первая или последняя ячейка не влезает в полезвёздочка разворачивает последовательности (неименнованые)
            return False
        for x, y in coords:
            #ищем корабль по координатам
            if self.get_ship_by_point(x,y, include_halo = True):
                return False
        return True

    def isset_cell(self,x,y):
        return 0 <= x < self.cols and 0 <= y <= self.rows

    def attack(x,y):
        if (x,y) in self.shots:
            return
        ship = self.get_ship_by_point(x,y)

        if ship:
            ship.attack()
            state = self.SHOT_KILLED if ship.is_killed() else SELF_INJURED
        else:
            state = self.SHOT_MISSED

        points = {}

        if ship and ship.is_killed():
            for point in ship.coords():
                self.shots[point] = points[point] = self.SHOT_KILLED

            for point in ship.halo():
                if point not in self.shots:
                    self.shots[point] = points[point] = self.SHOT_HALO
        self.shots[x,y] = points[x,y] = state

        #возвращаем затронутые точки
        return state, points



    def get_ship_by_point(self, x,y, include_halo = False):
        for ship in self.ships:
            if (x, y) in ship.coords():
                return ship
            #если переключатель установлен искать с ореолом - проверяем ореол
            if include_halo and (x,y) in ship.halo():
                return ship




class Game():
    pass

class View():
    pass
