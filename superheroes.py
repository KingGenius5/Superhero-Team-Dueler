import random
from random import randint

class Ability:
    def __init__(self, name, attack_strength):
        self.name = str(name)
        self.attack_strength = int(attack_strength)
    def attack(self):
        return randint(0, self.attack_strength)


class Armor:
    def __init__(self, name, max_block):
        self.name = str(name)
        self.max_block =int(max_block)
    def block(self):
        return randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = str(name)
        self.starting_health = int(starting_health)
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(Armor(armor.name, armor.max_block))

    def defend(self, damage_amt):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked

    def take_damage(self, damage):
        damage_taken = damage - self.defend(damage)
        self.current_health -= damage_taken

    def is_alive():
        print("Alive or not")

    def fight():
        print("This requires an opponent in the hero class")


if __name__ == "__main__":

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
