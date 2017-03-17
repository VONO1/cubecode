from random import randrange


class Ship(object):
    def __init__(self, tp, x=-1, y=-1, rotation=0):
        #скольки клеточный корабль
        self.type = tp
        #где находится клетка постоения
        self.x = x
        self.y = y
        #направление
        self.rotation = rotation
        #здоровье (равно типу)
        self.__hp = self.type
        self.field = None
#атака на корабль
    def attack(self):
        self.__hp -= 1
#узнать координаты
    def coords(self):
        x = self.x
        y = self.y
        r = self.rotation
        #возвращаем направление корабля 0 или 1 через хитрую логику
        return((x + i *r, y + i * (1 - r)) for i in range(self.type))
    def halo(self):
        coords = list(self.coord())
        x = self.x - 1
        y = self.y - 1
        r = self.rotation
        #смещаем по ширине корабля
        for i in range(3):
            shift_x = x + i * (1 - r)
            shift_y = y + i * r
            #по длине корабля
            for j in range(self.type + 2):
                x1 = shift_x + j *r
                y1 = shift_y +j *(1 - r)

                if (x1, y1) not in coords and self.field.isset_cell(x1,y1):
                    yield x1, y1

#проверка жив или мёртв
    def is_killed(self):
        return not self.__hp

class Field(object):
    SHOT_MISSED = 1
    SHOT_INJURED = 2
    SHOT_KILLED = 3
    SHOT_HALO = 4

    def __init__(self, rows = 10, cols = 10):
        self.rows = rows
        self.cols = cols

        self.ships = []
        self.shots = {}
# добавить корабль
    def add_ship(self, ship):
        #проверяем, что объект унаследован от класса кораблей
        if not isinstance(ship, Ship):
            return False
#проверяем влезел ли он
        if not self.check_pos(ship):
            #корабль не влез
            return False
        self.ships.append(ship)
        #корабль влез
        return True
#присваиваем кораблю ссылку на поле
        ship.field = self
        self.ships.append(ship)
        #является ли позиция валидной для постановки корабля
    def check_pos(self,ship):
        coords = list(ship.coords())
        #проверяем первую точку корабля и последнюю
        if not self.isset_cell(*coords[0]) or not self.issert_cell(coords[-1]):# если первая или последняя ячейка не влезает в полезвёздочка разворачивает последовательности (неименнованые)
            return False
        for x, y in coords:
            #ищем корабль по координатам/ плюс ореол
            if self.get_ship_by_point(x,y, include_halo = True):
                return False
        return True
#существование ячейки
    def isset_cell(self,x,y):
        return 0 <= x < self.cols and 0 <= y <= self.rows

    def attack(x,y):
        #проверяем не стреляли ли мы туда
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
    def ships_afloast(self):
        #количество живых кораблей
        return sum(1 for ship in self.ships if not ship.is_killed())



class Game(object):
    def __init__(self):
        self.enemyField = None
        self.enemyView = None
        self.started =False

    def start(self):
        self.enemyField = Field(10,10)
        self.random_strategy(self.enemyField)

        self.enemyView = FieldView(
            self.enemyField.rows,
            self.enemyField(cols)
        )
        self.enemyView.render()
        self.started = true
        #инициализация и отрисовка

        self.started = True
        while self.started:
            x,y = self.ask_pint()
            results = self.enemyField.attack(x,y)
            if results is None:
                print('вы уже стреляли в эту точку')
            else:
                state, points = results
                #ПЕРЕРИСОВАТЬ ПОЛЕ
                if state == Field.SHOT_KILLED and self.enemyField.ships_afloat() ==0:
                    self.finish()
    def ask_pint(self):
        x, y = None, None
        msg = 'введите координаты в формате x,y'
        while True:
            try:
            #разбиваем занчения запятой но только на 2 значения
                x, y = [int(1) for i in input(msg).split(',', 1)]
                return x,y
            except ValueError:
                print('некорректный ввод')

    def finish(self):
        self.started = False
        self.enemyField = None
        self.enemyView = None
    @staticmethod
    def random_strategy(field):
        ship_types = [1,1,1,1,2,2,2,3,3,4]
        ship_types.sort(reverse=True)
        for tp in ship_types:
            ship = Ship(tp)
            ok = False

            while not ok:
                ship.x = randrange(field.cols)
                ship.y = randrange(field.cols)
                ship.rotation = randrange(2) if tp > 1 else 0
                ok = field.add_ship(ship)
class FieldView(object):
    CELL_EMPTY = '.'
    CELL_SHIP = '@'
    CELL_MISSED = '0'
    CELL_INJURED = '*'
    CELL_KILLED = 'X'
    CELL_HALO = '#'

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [self.CELL_EMPTY] * rows * cols
    def __point2index(self, x, y):
        return x * self.cols + y

    def __do_update(self, state, points):
        for point in points:
            index = self.__point2index(*point)

            if index < len(self.matrix):
                self.matrix[index] = state
    def update(self, points):
        chars = {
            Field.SHOT_MISSED: self.CELL_MISSED,
            Field.SHOT_KILLED: self.CELL_KILLED,
            Field.SHOT_INJURED: self.CELL_INJURED,
            Field.SHOT_HALO: self.CELL_HALO

        }
        data = {}
        for point, state in points.items():
            if state in chars:
                data.setdefault(chars[state], []).append(point)
        for s, p in data.items():
            self.__do_update(s,p)

    def render(self):
        header = ['{:^3}'.format(i) for i in self.range(self.cols)]
        print('   {}'.format(''.join(header)))

        for i in range(self.rows):
            start =  self.__point2index(i,0)
            to = self.__point2index(i, self.cols)
            line = ['{:^3}'.format(i) for i in self.matrix[start]]
            print('{:^3}{}'.format(i,''.join(line)))

