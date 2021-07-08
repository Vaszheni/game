from abc import ABC, abstractmethod

class Human(ABC):

    def __init__(self, name:str, armor:int, weapon:str):
        self._name = name
        self._armor = armor
        self._weapon = weapon

    @abstractmethod
    def set_hp(self):
        pass

    def get_hp(self):
        return self._hp
    
    #создаем классы для реализации ранга героя
    def set_rank(self, rank:int):
        '''если ранг не может быть меньше одного и больше 3 '''
        if rank < 1:
            self._rank = 1
        elif rank > 3: 
            self._rank = 3
        else:
            self._rank = int(rank)
            
    def get_rank(self):
        return self._rank
    
    def up_rank(self):
        rank += 1
            
    rank = property(get_rank, set_rank)
        
    








