import copy
import random
import string


class Car:
    """Prototype"""

    def __init__(self, color, model, body):
        self.__model = model
        self.__body = body
        self.__color = color
        self.__number = None

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def clone(self):
        return copy.copy(self)

    def info(self):
        return "{}\n{}\n{}\n{}\n".format(self.model, self.body, self.color, self.__number)

    def set_number(self):
        self.__number = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
        self.__number += ''.join(random.choice(string.digits) for i in range(4))
        self.__number += ''.join(random.choice(string.ascii_uppercase) for i in range(2))


class Nissan(Car):
    pass


class Jeep(Car):
    pass


class Factory:
    def __init__(self):
        self.__nissan = Nissan("red", "Nissan Note", "hatchback")
        self.__jeep = Jeep("black", "Jeep Liberty", "universal")
        self.__nissan.info()

    def create_nissan(self):
        self.__nissan.set_number()
        return self.__nissan.clone()

    def create_jeep(self):
        self.__jeep.set_number()
        return self.__jeep.clone()


def main():
    factory = Factory()
    print(factory.create_jeep().info())
    print(factory.create_nissan().info())
    print(factory.create_nissan().info())


if __name__ == '__main__':
    main()