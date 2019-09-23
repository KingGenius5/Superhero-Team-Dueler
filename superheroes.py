import random
from random import randint

class Ability:
    def __init__(self, name, attack_strength):
        self.name = str(name)
        self.attack_strength = int(attack_strength)
    def attack(self):
        self = randint(2,7)
        return self


class Armor:
    def __init__(self, name, max_block):
        self.name = str(name)
        self.max_block =int(max_block)
    def block(self):
        self = randint(0, max_block)
        return self


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = str(name)
        self.starting_health = int(starting_health)
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
    def add_ability():
        print("This adds an ability")
    def attack():
        print("This will attack")
    def defend():
        print("Defend from incoming damage")
    def take_damage():
        print("Damage")
    def is_alive():
        print("Alive or not")
    def fight():
        print("This requires an opponent in the hero class")


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
