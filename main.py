# Фиксируем исходные данные задачи

# Класс, представляющий бойца
class Fighter:
    def __init__(self, name):
        self.name = name            # Имя бойца

    def attack(self, monster):      # Метод атаки монстра
        print(f"{self.name} атакует монстра!")

# Класс, представляющий монстра

class Monster ():
    def __init__(self, name, health):
        self.name = name            # Имя монстра
        self.health = health        # Здоровье (жизненная сила) монстра

    def take_damage(self, damage):  # Метод фиксирования нанесенного ущерба здоровью монстра
        self.health -= damage       # Из уровня здоровья монстра вычитается значение нанесенного ущерба
        if self.health > 0:
            print(f"Уровень здоровья {self.name} - {self.health}.")
        else:
            self.health = 0         # В случае достижения нулевого уровня здоровья и меньше
            print(f"{self.name} побежден!")


    def attack(self):               # Абстрактный метод атаки для реализован в каждом конкретном типе оружия
        pass

# Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):               # Метод атаки для реализации в каждом конкретном типе оружия
        pass