class SchoolBoy:

    def __init__(self):
        self.task = None

    def set_task(self, task):
        self.task = task

    def set_executor(self, executor):

        if executor is None:
            self.task.execute()
        else:
            self.task.set_executor(executor)

    def do_homework(self):
        if self.task:
            self.task.execute()


class Task:
    def __init__(self):
        self._executor = None

    def set_executor(self, e):
        self._executor = e

    def execute(self):
        if self._executor is not None:
            return self._executor.do_homework()
        else:
            print("Kid has done the homework by himself. The grade is 6")
            return 6


class Executor:
    def do_homework(self):
        pass


class Mother(Executor):
    def do_homework(self):
        print("Mom has done the homework. The grade is 12")
        return 12


class Grandmother(Executor):
    def do_homework(self):
        print("Granny has done the homework. The grade is 10")
        return 10


class Father(Executor):
    def do_homework(self):
        print("Dad has done the homework. The grade is 8")
        return 8


def main():
    mom = Mother()
    granny = Grandmother()
    dad = Father()
    Stiv = SchoolBoy()
    task = Task()
    Stiv.set_task(task)
    Stiv.do_homework()
    Stiv.set_executor(granny)
    Stiv.do_homework()
    Stiv.set_executor(dad)
    Stiv.do_homework()
    Stiv.set_executor(mom)
    Stiv.do_homework()


if __name__ == '__main__':
    main()
