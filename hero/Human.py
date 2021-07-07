from abc import ABC, abstractmethod

class Human(ABC):

    def __init__(self, name, armor, weapon):
        self._name = name
        self._armor = armor
        self._weapon = weapon

    @abstractmethod
    def set_hp(self):
        pass

    def get_hp(self):
        return self._hp

    








