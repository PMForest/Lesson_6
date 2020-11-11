"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
  который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is start'

    def stop(self):
        return f'{self.name} is stop'

    def turn_left(self):
        return f'{self.name} is turn left'

    def turn_right(self):
        return f'{self.name} is turn right'

    def speed(self):
        return f'Show speed {self.name} is {self.speed}'

class TownCar(Car):

    def show_speed(self):
        print(f'car speed of town {self.name} is {self.speed}')

        if self.speed > 60:
            return f'speed of {self.name} to many, slow down!'

        else:
            return f'speed of {self.name} to slow, you are sleeping?'

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print(f'car speed of town {self.name} is {self.speed}')

        if self.speed > 40:
            return f'speed of {self.name} to many, slow down! work not run away!'

        else:
            return f'speed of {self.name} to slow, dont go work!'

class PoliceCar(Car):

    def police(self):
        if self.is_police:
            return f'{self.name} is very good guy, it is a police!'
        else:
            return f'{self.name} is very good guy, but it is not a police!'


Honda = TownCar(55, 'Yellow', 'Honda', False)
BMV = SportCar(290, 'Black', 'BMV', True)
Subaru = WorkCar(15, 'Blue', 'Subaru', False)
peel_P50 = PoliceCar(10, 'Green', 'peel_P50', True)

print(Subaru.show_speed())
print(Honda.show_speed())
print(peel_P50.police())
print(f'If {peel_P50.name} go right, {peel_P50.is_police}')
print(f'{BMV.turn_left()}, but {Subaru.turn_right} ')
print(f'speed {Honda.go()} to many, {Subaru.show_speed()}')

# вар2

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going!'.format(self.name))

    def stop(self):
        print('{} is stoping!'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Касная', 'Спотивная машина', False)
town_car = TownCar(140, 'Серая', 'Городская машина', False)
work_car = WorkCar(90, 'Желтая', 'Рабочая машина', False)
police_car = PoliceCar(210, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')
