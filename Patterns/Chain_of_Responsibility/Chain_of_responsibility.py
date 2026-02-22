from abc import ABC, abstractmethod
from enum import IntEnum
from dataclasses import dataclass

class Seriousness(IntEnum):
    MINOR = 1
    MODERATE = 2
    SERIOUS = 3
    CRITICAL = 4

@dataclass
class Complaint:
    customer: str
    description: str
    Seriousness: Seriousness

class Handler(ABC):
    def __init__(self, name: str, max_Seriousness: Seriousness):
        self.name = name
        self.max_Seriousness = max_Seriousness
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, complaint: Complaint):
        if complaint.Seriousness <= self.max_Seriousness:
            self._resolve(complaint)
        elif self._next:
            print(f'  {self.name}: «Не в моїх силах, передаю далі...»')
            self._next.handle(complaint)

    @abstractmethod
    def _resolve(self, complaint: Complaint):
        pass

class Cashier(Handler):
    def __init__(self):
        super().__init__('Касир Оля', Seriousness.MINOR)
    def _resolve(self, complaint):
        print(f'  {self.name}: Виправлю це на касі для "{complaint.customer}".')

class Manager(Handler):
    def __init__(self):
        super().__init__('Менеджер Сергій', Seriousness.MODERATE)
    def _resolve(self, complaint):
        print(f'  {self.name}: Проведу інструктаж і компенсую "{complaint.customer}".')

class StoreDirector(Handler):
    def __init__(self):
        super().__init__('Директор Наталія', Seriousness.SERIOUS)
    def _resolve(self, complaint):
        print(f'  {self.name}: Повернемо кошти і усунемо порушення для "{complaint.customer}".')

class HeadOffice(Handler):
    def __init__(self):
        super().__init__('Головний офіс', Seriousness.CRITICAL)
    def _resolve(self, complaint):
        print(f'  {self.name}: Розпочато розслідування для "{complaint.customer}".')

def build_chain():
    cashier = Cashier()
    cashier.set_next(Manager()).set_next(StoreDirector()).set_next(HeadOffice())
    return cashier

def main():
    chain = build_chain()
    complaints = [
        Complaint('Іванченко В.', 'На полиці не та цінова картка.', Seriousness.MINOR),
        Complaint('Петренко О.', 'Продавець нагрубіянив.', Seriousness.MODERATE),
        Complaint('Коваленко М.', 'Прострочений товар.', Seriousness.SERIOUS),
        Complaint('Бойко Л.', 'Масове отруєння після корпоративу.', Seriousness.CRITICAL),

    ]
    for c in complaints:
        print(f'\n [{c.customer} | {c.Seriousness.name}] {c.description}')
        chain.handle(c)

if __name__ == '__main__':
    main()
