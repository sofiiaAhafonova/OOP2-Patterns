class Drink:
    """Abstract product"""
    _cost = 0.0

    def get_drink(self, money):
        if money <= 0:
            print("Money value should be more then 0")
            return False
        elif money < self._cost:
            print("There isn't enough money for drink")
            return False
        return True


class ClassicCoffee(Drink):
    _cost = 3.4

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Classic coffee\n")
        return self._cost


class InstantCoffee(Drink):
    _cost = 0.9

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Instant Coffee\n")
        return self._cost


class Teabag(Drink):
    _cost = 0.8

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Tea Bag\n")
        return self._cost


class LooseTea(Drink):
    _cost = 1.5

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Loose Tea\n")
        return self._cost


class NaturalJuice(Drink):
    _cost = 2.0

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Natural Juice\n")
        return self._cost


class Nectar(Drink):
    _cost = 0.8

    def get_drink(self, money):
        if not super().get_drink(money):
            return None
        print("Nectar\n")
        return self._cost


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class VendingMachine(metaclass=Singleton):
    """Abstract Factory"""
    def make_coffee(self):
        pass

    def make_juice(self):
        pass

    def make_tea(self):
        pass


class CheapDrinksMachine(VendingMachine):
    """Concrete Factory 1"""
    def make_coffee(self):
        return InstantCoffee()

    def make_juice(self):
        return Nectar()

    def make_tea(self):
        return Teabag()


class ExpensiveDrinksMachine(VendingMachine):
    """Concrete Factory 2"""
    def make_coffee(self):
        return ClassicCoffee()

    def make_juice(self):
        return NaturalJuice()

    def make_tea(self):
        return LooseTea()


def main():
    money = 22
    factory = None
    if money < 1:
        factory = CheapDrinksMachine()
    elif money >= 1:
        factory = ExpensiveDrinksMachine()
    cost = factory.make_coffee().get_drink(money)
    if cost is not None:
        print("Your money : {}, cost : {} cash back: {}".format(money, cost, round(money - cost, 2)))


if __name__ == '__main__':
    main()
