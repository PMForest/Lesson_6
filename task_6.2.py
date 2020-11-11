"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class MassRoad(Road):
    def __init__(self, _length, _width, depth):
        super().__init__(_length, _width)
        self.depth = depth

i = MassRoad(5000, 20, 5)
print(i.mass())



# вар 2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


my_road = Road(20, 5000)
print(my_road.calc_mass(), 'С‚')