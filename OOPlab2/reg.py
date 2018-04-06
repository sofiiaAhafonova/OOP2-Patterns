import sys
from PyQt5.QtWidgets import QApplication, QDialog
from signupwindow import window


class AppDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = window.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class IForm:
    """Интерфейс для прокси и реального субъекта"""
    def add_name(self, name):
        raise NotImplementedError()

    def add_surname(self, surname):
        raise NotImplementedError()

    def add_photo(self, photo):
        raise NotImplementedError()


class Form(IForm):
    """Реальный субъект"""
    name = ""
    surname = ""
    photo = ""

    def add_name(self, name):
        self.name = name

    def add_surname(self, surname):
        self.surname = surname

    def add_photo(self, photo):
        self.photo = photo

    def has_personal_data(self):
        return len(self.name) and len(self.surname)

class Proxy(IForm):
    """Прокси"""
    def __init__(self):
        self.form = None

    # Быстрые операции - не требуют реального субъекта

    def add_name(self, name):
        if not self.client:
            self.form = Form()
        return self.form.add_name(name)

    def add_surname(self, surname):
        if not self.client:
            self.form = Form()
        return self.form.add_surname(surname)

    def add_photo(self, photo):
        if self.form.has_personal_data():
            self.form.add_photo(photo)
        else:
            print("You can`t add photo, add personal data first")


def main():
    pass


if __name__ == '__main__':
    main()


