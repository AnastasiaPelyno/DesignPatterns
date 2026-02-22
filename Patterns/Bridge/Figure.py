from abc import ABC,abstractmethod
class Figure(ABC):
    def __init__(self,colour):
        self.colour=colour

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass
    def __str__(self):
        pass
