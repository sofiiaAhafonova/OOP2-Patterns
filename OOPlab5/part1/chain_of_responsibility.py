import abc


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self._successor = successor
        super().__init__()

    @abc.abstractmethod
    def handle_request(self, req="open a bank account"):
        pass


class Operator(Handler):
    """
    Handle request, otherwise forward it to the successor.
    """
    def __init__(self):
        super().__init__(Manager())

    def handle_request(self, req="open a bank account"):
        if req == "open a bank account":
            print("An operator has handled request:{}".format(req))
        elif self._successor is not None:
            self._successor.handle_request(req)


class Manager(Handler):
    def __init__(self):
        super().__init__(Director())

    def handle_request(self, req="get credit"):
        if req == "get credit":
            print("A manager has handled request:{}".format(req))
        elif self._successor is not None:
            self._successor.handle_request(req)


class Director(Handler):
    def handle_request(self, req="buy bank shares"):
        if req == "buy bank shares":
            print("A Director has handled request:{}".format(req))
        else:
            print("No one can handle request:{}".format(req))


def main():
    concrete_handler_1 = Operator()
    concrete_handler_1.handle_request("open a bank account")


if __name__ == "__main__":
    main()