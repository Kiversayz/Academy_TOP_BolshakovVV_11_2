from abc import ABC,abstractmethod

class Builder (ABC):
    """Абстрактный строитель, определяющий интерфейс для всех рабочих."""
    
    @abstractmethod
    def prepare_floors(self):
        """Подготовить полы"""
        pass

    @abstractmethod
    def lay_tiles(self):
        """Уложить плитку"""
        pass

    @abstractmethod
    def apply_putty(self):
        """Нанести шпаклевку"""
        pass

    @abstractmethod
    def plaster_walls(self):
        """Оштукатурить стены"""
        pass

    @abstractmethod
    def prime_walls(self):
        """Загрунтовать стены"""
        pass

    @abstractmethod
    def paint_walls(self):
        """Покрасить стены"""
        pass

    @abstractmethod
    def get_result(self):
        """Получить итоговый результат"""
        pass

class TileWorker(Builder):
    def prepare_floors(self):
        print("Подготовка пола: убрали старое покрытие, выровняли поверхность.")

    def lay_tiles(self):
        print("Укладка плитки: плитка уложена, швы затерты.")

    def apply_putty(self):
        pass  # Отделочник

    def plaster_walls(self):
        pass  # Отделочник

    def prime_walls(self):
        pass  # Маляр

    def paint_walls(self):
        pass  # Маляр

    def get_result(self):
        return "Полы готовы!"

class Finisher(Builder):
    def prepare_floors(self):
        pass  # Плиточник

    def lay_tiles(self):
        pass  # Плиточник

    def apply_putty(self):
        print("Наносим шпаклевку на стены.")

    def plaster_walls(self):
        print("Оштукатуриваем стены.")

    def prime_walls(self):
        pass  # Маляр

    def paint_walls(self):
        pass  # Маляр

    def get_result(self):
        return "Стены подготовлены: зашпаклеваны и оштукатурены."

class Painter(Builder):
    def prepare_floors(self):
        pass  # Плиточник

    def lay_tiles(self):
        pass  # Плиточник

    def apply_putty(self):
        pass  # Отделочник

    def plaster_walls(self):
        pass  # Отделочник

    def prime_walls(self):
        print("Грунтуем стены перед покраской.")

    def paint_walls(self):
        print("Красим стены в выбранный цвет.")

    def get_result(self):
        return "Стены загрунтованы и покрашены."

class Foreman:
    """Директор (прораб), управляющий процессом ремонта."""

    def make_floors(self, builder: Builder):
        """ Плиточник делает полы и укладывает плитку"""
        builder.prepare_floors()
        builder.lay_tiles()

    def level_walls(self, builder: Builder):
        """ Отделочник наносит шпаклевку и оштукатуривает стены """
        builder.apply_putty()
        builder.plaster_walls()

    def paint_walls(self, builder: Builder):
        """ Маляр грунтует стены и красит стены"""
        builder.prime_walls()
        builder.paint_walls()

    def full_repair(self):
        """Выполнить полный цикл ремонта."""
        
        tile_worker = TileWorker()
        self.make_floors(tile_worker)

        finisher = Finisher()
        self.level_walls(finisher)

        painter = Painter()
        self.paint_walls(painter)

        print("Ремонт под ключ завершен!\n")


if __name__ == "__main__":
    foreman = Foreman()

    print("Работа плиточника:")
    tile_worker = TileWorker()
    foreman.make_floors(tile_worker)
    print(tile_worker.get_result())

    print("\nРабота отделочника:")
    finisher = Finisher()
    foreman.level_walls(finisher)
    print(finisher.get_result())

    print("\nРабота маляра:")
    painter = Painter()
    foreman.paint_walls(painter)
    print(painter.get_result())

    print("\nПолный ремонт:")
    foreman.full_repair()

