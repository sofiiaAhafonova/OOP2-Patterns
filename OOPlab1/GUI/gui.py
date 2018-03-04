import uuid
from abc import ABCMeta, abstractmethod


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


# Abstraction
class UserInterface:

    def __init__(self, obj, name="John", age=20, card="1221-1234-3425-4543"):
        self.obj = obj
        self.obj.name = name
        self.obj.age = age
        self.obj.card = card

    def show_info(self):
        return self.obj.show_info()


# ConcreteImplementor 1/2 for high-level access
class HighAccessInfo(GUI):
    def show_info(self):
        print("\nid: {}\nname: {}\nage: {}\ncard number: {}"
              .format(self.id, self.name, self.age, self.card))


# ConcreteImplementor 2/2 for low-level access
class LowAccessInfo(GUI):
    def show_info(self):
        print("\nname: {}\nage: {}"
              .format(self.name, self.age))


class UserList:

    user_list = []

    def show_user_list(self):
        for l in self.user_list:
            l.show_info()

    def add_user(self, user):
        self.user_list.append(user)


def main():
    print()
    lst = UserList()
    low = LowAccessInfo()
    abstraction = UserInterface(low, "Helen")
    lst.add_user(abstraction)
    abstraction.show_info()
    high = HighAccessInfo()
    abstraction = UserInterface(high)
    abstraction.show_info()
    lst.add_user(abstraction)
    print("---")
    lst.show_user_list()


if __name__ == '__main__':
        main()
