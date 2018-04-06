import uuid
from abc import ABCMeta, abstractmethod
import curses


# Implementor
class GUI:

    id = uuid.uuid4()
    age = 0
    card = 0
    name = ""

    __metaclass__ = ABCMeta

    @abstractmethod
    def show_info(self):
        pass

    @abstractmethod
    def menu(self):
        pass


# Abstraction
class UserInterface:

    def __init__(self, obj, name="John", age=20, card="1221-1234-3425-4543"):
        self.obj, self.obj.name, self.obj.age, self.obj.card= obj, name, age, card

    def show_info(self):
        return self.obj.show_info()

    def menu(self):
        return self.obj.menu()


# ConcreteImplementor 1/2 for high-level access
class HighAccessInfo(GUI):
    def show_info(self):
        print("id: {}\nname: {}\nage: {}\ncard number: {}"
              .format(self.id, self.name, self.age, self.card))

    def menu(self):
        print("Menu:\nShow user`s info\nChange card number\nDelete user\n")


# ConcreteImplementor 2/2 for low-level access
class LowAccessInfo(GUI):
    def show_info(self):
        print("name: {}\nage: {}"
              .format(self.name, self.age))

    def menu(self):
        print("Menu:\nShow user`s info\n")


def main():
    print("\nUser 1")
    low = LowAccessInfo()
    abstraction = UserInterface(low, "Helen")
    abstraction.menu()
    abstraction.show_info()
    print("\nUser 2")
    high = HighAccessInfo()
    abstraction = UserInterface(high)
    abstraction.menu()
    abstraction.show_info()


if __name__ == '__main__':
        main()
