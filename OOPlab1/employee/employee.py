from abc import ABCMeta, abstractmethod


class OfficeWorker:
    __metaclass__ = ABCMeta

    workplace = 0
    salary = 0
    name = "John"
    surname = "Doe"
    is_working = True
    presence = True

    def get_salary(self, salary):
        if self.is_working:
            self.salary += salary
            print("You've got {0}$", salary)
        else:
            print("You don't have a job")

    def quit(self):
        if self.is_working:
            self.workplace = 0
            self.presence = False
            self.is_working = False
            print("You've quited your job")
        else:
            print("You don't have a job")

    def leave_workplace(self):
        if self.presence:
            self.presence = False
            print("You've left your workplace")
        else:
            print("You haven`t been at work yet")

    def go_to_work(self):
        if not self.presence:
            self.presence = True
            print("You've come to work")
        else:
            print("You've already been at work")

    def get_job(self, workplace):
        if not self.is_working:
            self.workplace = workplace
            self.is_working = True
            print("You're an office worker now")
        else:
            print("You've already have a job")

    @abstractmethod
    def introduction(self):
        pass


class Director(OfficeWorker):

    employees = 1

    def __init__(self, name="John", surname="Doe", salary=100, workplace=1):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.workplace = workplace
        self.is_working = True

    def introduction(self):
        print("I'm a director of the company."
              .format(self.salary))


class SysAdmin(OfficeWorker):

    administratingPCs = 3

    def __init__(self, name="John", surname="Doe", salary=100, workplace=1):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.workplace = workplace
        self.is_working = True

    def introduction(self):
        print("I'm a system administrator of the company."
              .format(self.name, self.surname, self.salary))


class OfficeManager(OfficeWorker):

    offices = 1

    def __init__(self, name="John", surname="Doe", salary=100, workplace=1):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.workplace = workplace
        self.is_working = True

    def introduction(self):
        print("I'm an office manager of the company."
              .format(self.name, self.surname, self.salary))


class Decorator(OfficeWorker):
    """Decorator"""
    def __init__(self, obj):
        self.obj = obj

    def introduction(self):
        print("My name is {} {}.".format(self.obj.name, self.obj.surname))
        self.obj.introduction()
        print("My salary is {}$".format(self.obj.salary))

    def carry_out_duties(self):
        print("I've carried out all my duties today")


class Booking(Decorator):
    """Decorator"""
    def __init__(self, obj):
        super(Booking, self).__init__(obj)

    def introduction(self):
        self.obj.introduction()

    def carry_out_duties(self):
        self.obj.carry_out_duties()
        print("I've booked a dinner for the whole office")


class InstallSoftware(Decorator):
    """Decorator"""
    def __init__(self, obj):
        super(InstallSoftware, self).__init__(obj)

    def introduction(self):
        self.obj.introduction()

    def carry_out_duties(self):
        self.obj.carry_out_duties()
        print("I've installed software for the whole office")


class Negotiate(Decorator):
    """Decorator"""
    def __init__(self, obj):
        super(Negotiate, self).__init__(obj)

    def introduction(self):
        self.obj.introduction()

    def carry_out_duties(self):
        self.obj.carry_out_duties()
        print("I've negotiated with partners")
