""" Паттерн Builder. Это позволяет гибко управлять процессом создания пасты, и в дальнейшем легко добавлять новые компоненты. """

from abc import ABC, abstractmethod

class PastaBuilder(ABC):
    """Абстрактный строитель для пасты"""

    @abstractmethod
    def set_type(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_filling(self):
        pass

    @abstractmethod
    def set_additives(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class SpaghettiBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = {}

    def set_type(self):
        self.pasta['Тип'] = "Спагетти"

    def set_sauce(self):
        self.pasta['Соус'] = "Томатный соус"

    def set_filling(self):
        self.pasta['Мясное'] = "Фрикадельки"

    def set_additives(self):
        self.pasta['Добавки'] = "Сыр, Базелик"

    def get_result(self):
        return self.pasta

class FettuccineBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = {}

    def set_type(self):
        self.pasta['Тип'] = "Феттучини"

    def set_sauce(self):
        self.pasta['Соус'] = "соус Альфредо"

    def set_filling(self):
        self.pasta['Мясное'] = "Курца"

    def set_additives(self):
        self.pasta['Добавки'] = "Петрушка, пармезан"

    def get_result(self):
        return self.pasta


class PenneBuilder(PastaBuilder):
    def __init__(self):
        self.pasta = {}

    def set_type(self):
        self.pasta['Тип'] = "Пенне"

    def set_sauce(self):
        self.pasta['Соус'] = "соус Песто"

    def set_filling(self):
        self.pasta['Мясное'] = "Креветка"

    def set_additives(self):
        self.pasta['Добавки'] = "Оливки, нарезанный Чили"

    def get_result(self):
        return self.pasta

class PastaDirector:
    """Менеджер, который управляет процессом создания пасты."""

    def __init__(self, builder: PastaBuilder):
        self.builder = builder

    def prepare_pasta(self):
        """Метод для пошагового приготовления пасты."""
        self.builder.set_type()
        self.builder.set_sauce()
        self.builder.set_filling()
        self.builder.set_additives()
        return self.builder.get_result()

if __name__ == "__main__":
    # Создаём строитель для спагетти
    spaghetti_builder = SpaghettiBuilder()
    director = PastaDirector(spaghetti_builder)
    spaghetti = director.prepare_pasta()
    print("Спагетти:", spaghetti)

    print()

    # Создаём строитель для фетучини
    fettuccine_builder = FettuccineBuilder()
    director = PastaDirector(fettuccine_builder)
    fettuccine = director.prepare_pasta()
    print("Феттучини:", fettuccine)

    print()

    # Создаём строитель для пенне
    penne_builder = PenneBuilder()
    director = PastaDirector(penne_builder)
    penne = director.prepare_pasta()
    print("Пенне:", penne)
