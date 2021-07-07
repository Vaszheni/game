from abc import ABC, abstractmethod

class Arena(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def get_fighter(self):
        pass

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        pass 
