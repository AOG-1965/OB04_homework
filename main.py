# Фиксируем исходные данные задачи

# Класс, представляющий бойца
# class Fighter:
#     def __init__(self, name):
#         self.name = name            # Имя бойца
#
#     def attack(self, monster):      # Метод атаки монстра
#         print(f"{self.name} атакует монстра!")

# Класс Fighter после его модифицирования
class Fighter:
    def __init__(self, name):
        self.name = name                    # Имя бойца
        self.weapon = None

    def change_weapon(self, new_weapon):    # Метод для выбора/смены оружия
        self.weapon = new_weapon
        print(f"{self.name} выбрал {self.weapon.__class__.__name__}.")

    def attack(self, monster):              # Метод атаки бойцом монстра, используя выбранное оружие
        if self.weapon is None:             # Проверка наличия оружия
            print(f"{self.name} не имеет оружия.")
        else:
            print(f"{self.name} атакует монстра {monster.name}!")
            damage = self.weapon.attack()   # Вызывается метод атаки у объекта оружия
            monster.take_damage(damage)     # Cохранение урона от использованного оружия

# Класс, представляющий монстра

class Monster ():
    def __init__(self, name, health):
        self.name = name            # Имя монстра
        self.health = health        # Здоровье (жизненная сила) монстра
        print(f"Уровень здоровья монстра {self.name} - {health}")

    def take_damage(self, damage):  # Метод фиксирования нанесенного ущерба здоровью монстра
        self.health -= damage       # Из уровня здоровья монстра вычитается значение нанесенного ущерба
        if self.health > 0:
            print(f"Уровень здоровья монстра {self.name} - {self.health}.")
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

# Создание производных классов, унаследованных от Weapon

# Класс Sword (меч)
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом!")
        return 50                   # Уникальность метода attack в размере урона, который наносит меч

# Класс Bow (лук)
class Bow(Weapon):
    def attack(self):
        print("Боец выпускает стрелу из лука!")
        return 30                   # Уникальность метода attack в размере урона, который наносит лук

# Проверка работы кода
# Создание объектов
fighter = Fighter("Рыцарь")
monster = Monster("Дракон", 100)

# Объекты оружие
sword = Sword()                 # Меч
bow = Bow()                     # Лук

fighter.change_weapon(sword)    # Боец выбирает меч
fighter.attack(monster)         # Боец атакует монстра

fighter.change_weapon(bow)      # Боец выбирает лук
fighter.attack(monster)         # Боец атакует монстра

fighter.attack(monster)         # Боец еще раз атакует монстра из лука