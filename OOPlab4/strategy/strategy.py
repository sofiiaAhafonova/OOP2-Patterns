class WashStrategy:

    def wash_cloth(self, cloth):
        pass


class Delicate(WashStrategy):

    def wash_cloth(self, cloth):
        cloth.state = "clean"
        return cloth


class CottonWashing(WashStrategy):
    def wash_cloth(self, cloth):
        if cloth.type == "silk":
            cloth.state = "damaged"
        else:
            cloth.state = "clean"
        return cloth


class SilkWashing(WashStrategy):
    def wash_cloth(self, cloth):
        if cloth.type == "cotton":
            cloth.state = "damaged"
        else:
            cloth.state = "clean"
        return cloth


class Cloth:

    list = []

    def __init__(self, name, textile):
        self.name = name
        self.type = textile
        self.state = "dirty"


class WashingMachine:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def wash(self, cloth_list):
        for cloth in cloth_list:
            self._strategy.wash_cloth(cloth)
            print("{} {}".format(cloth.state, cloth.name))


def main():
    delicate = Delicate()
    machine = WashingMachine(delicate)
    machine.set_strategy(delicate)
    list_cloth = [Cloth("skirt", "silk"), Cloth("t-shirt", "cotton"), Cloth("Jeans", "jeans")]
    machine.wash(list_cloth)
    cot = CottonWashing()
    machine.set_strategy(cot)
    machine.wash(list_cloth)


if __name__ == '__main__':
    main()
