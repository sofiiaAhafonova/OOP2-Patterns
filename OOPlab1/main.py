from employee import employee


def main():
    print("hello")
    d = employee.Director("Helen", "Parker", 5600)
    om = employee.OfficeManager("Stiv", "Brown", 1200)
    sa = employee.SysAdmin("Frank", "Jakobs", 2500)
    d.introduction()
    om.introduction()
    sa.introduction()
    print()
    d = employee.Decorator(d)
    d.introduction()
    print()
    om = employee.Decorator(om)
    om.introduction()
    print()
    sa = employee.Decorator(sa)
    sa.introduction()
    print()
    print()
    print()
    om = employee.Booking(om)
    om.introduction()
    om.carry_out_duties()
    print()
    d = employee.Negotiate(d)
    d.introduction()
    d.carry_out_duties()
    print()
    sa = employee.InstallSoftware(sa)
    sa.introduction()
    sa.carry_out_duties()


if __name__ == '__main__':
    main()
