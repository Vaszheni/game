from hero import Hero
class Knight(Hero):
    def __init__(self):
        pass

    def set_hp(self):
        self.hp = 100

    def min_hp(self, value):
        self.hp -= value
