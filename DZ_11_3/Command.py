from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()


class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()

class Light:
    def turn_on(self):
        print("Свет горит")

    def turn_off(self):
        print("Свет выключен")


class Fan:
    def turn_on(self):
        print("Вентилятор включен")

    def turn_off(self):
        print("Вентилятор выключен")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("Команда не задана!")


if __name__ == "__main__":
    # Создаем устройства
    light = Light()
    fan = Fan()

    # Создаем команды для управления устройствами
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    # Создаем пульт управления
    remote = RemoteControl()

    # Тестируем команды
    remote.set_command(light_on)
    remote.press_button()  # Включить свет

    remote.set_command(fan_on)
    remote.press_button()  # Включить вентилятор

    remote.set_command(light_off)
    remote.press_button()  # Выключить свет

    remote.set_command(fan_off)
    remote.press_button()  # Выключить вентилятор
