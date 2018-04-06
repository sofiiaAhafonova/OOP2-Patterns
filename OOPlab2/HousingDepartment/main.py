class Client:
    def __init__(self, name, surname, address):
        self.name, self.surname, self.address = name, surname, address


class Reference:
    """The 'Flyweight' abstract class"""

    def create_reference(self, client):
        pass


class PeopleInApartment(Reference):
    """A 'ConcreteFlyweight' class"""
    def create_reference(self, client):
        n = 2
        pers = "people"
        if n == 1:
            pers = "person"
        return "{0} {1} live in apartment {2}".format(n, pers, client.address)


class OwnApartment(Reference):
    """A 'ConcreteFlyweight' class"""
    def create_reference(self, client):
        return "{0} {1} owns apartment with address {2}".format(client.name, client.surname, client.address)


class BuyApartment(Reference):
    """A 'ConcreteFlyweight' class"""
    def create_reference(self, client):
        return "{0} {1} bought apartment with address {2}".format(client.name, client.surname, client.address)


class Department:
    """The Flyweight Factory Class"""

    _references = ["People In Apartment", "Apartment Owner", "Buy Apartment"]

    def get_reference(self, title):
        a = None
        if not self._references.__contains__(title):
            print("Wrong reference title")
        elif title == "People In Apartment":
            a = PeopleInApartment()
        elif title == "Apartment Owner":
            a = OwnApartment()
        elif title == "Buy Apartment":
            a = BuyApartment()
        return a


def main():
    department = Department()
    client = Client("Jane", "Brown", "Green st, 4")
    ref = department.get_reference("People In Apartment")
    print(ref.create_reference(client))
    ref = department.get_reference("Apartment Owner")
    print(ref.create_reference(client))
    department.get_reference("Bla Bla")


if __name__ == '__main__':
    main()


