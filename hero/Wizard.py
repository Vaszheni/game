from hero.Human import Human
class Wizard(Human):
    def __init__(self, name, armor, weapon):
        self.status = 'alive'
        self.type = 'Wizard'
        super().__init__(name, armor, weapon)
        self.set_hp()

    def set_hp(self):
        self._hp = 110

    def min_hp(self, value):
        self._hp -= value
        if self.get_hp() < 0:
            self.status = 'dead'


    def get_name(self):
        return self._name

    hp = property(Human.get_hp, set_hp)
