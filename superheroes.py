import random
from random import randint

class Ability:
    def __init__(self, name, attack_strength):
        self.name = str(name)
        self.attack_strength = int(attack_strength)
    def attack(self):
        attack_strength = randint(2,7)
        return attack_strength


class Armor:
    def __init__(self, name, max_block):
        self.name = str(name)
        self.max_block =int(max_block)
    def block():
        print("Blockin")

class Hero:
    def __init__(self, name, starting_health):
        self.name = str(name)
        self.starting_health = int(starting_health)
    def add_ability():
        print("This add an ability")
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
