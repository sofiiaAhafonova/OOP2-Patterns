from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def add_money(self):
        pass

    @abstractmethod
    def get_drink(self):
        pass

    @abstractmethod
    def choose_drink(self):
        pass


class OkState(State):
    """product exist, enough money"""
    def add_money(self):
        print("There is enough money for drink")

    def get_drink(self):
        print("Get your drink")

    def choose_drink(self):
        print("Product have already chosen")


class NotEnoughMoneyState(State):
    """product exist, not enough money"""
    def add_money(self):
        print("You've added $")

    def get_drink(self):
        print("There isn't enough money for drink")

    def choose_drink(self):
        print("Product have already chosen")


class TooMuchMoneyState(State):
    """product exist, too much money"""
    def add_money(self):
        print("There is already too much money")

    def get_drink(self):
        print("Get your drink and cash back")

    def choose_drink(self):
        print("Product have already chosen")


class NoProductState(State):
    """product doesn't exist"""
    def add_money(self):
        print("Choose correct product first")

    def get_drink(self):
        print("Choose correct product first")

    def choose_drink(self):
        print("Such product doesn't exist")


class VendingMachine:
    def __init__(self, state: State) -> None:
        self._state = state

    def change_state(self, state: State) -> None:
        self._state = state

    def add_money(self):
        self._execute('add_money')

    def get_drink(self):
        self._execute('get_drink')

    def choose_drink(self):
        self._execute('choose_drink')

    def _execute(self, operation: str) -> None:
        try:
            func = getattr(self._state, operation)
            func()
        except AttributeError:
            print("Machine can't do this")


if __name__ == '__main__':
    ok = OkState()
    not_enough_money = NotEnoughMoneyState()
    no_prod = NoProductState()
    too_much = TooMuchMoneyState()

    machine = VendingMachine(ok)
    print('OUTPUT:')
    machine.get_drink()
    machine.add_money()
    machine.change_state(no_prod)
    machine.get_drink()