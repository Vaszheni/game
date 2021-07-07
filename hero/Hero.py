from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_hp(self):
        pass

    def get_hp(self):
        return self.hp

    hp = property(get_hp, set_hp)




