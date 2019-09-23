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

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():

            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
                break

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.current_health > opponent.current_health:
            print(self.name + " Wins!")
        else:
            print(opponent.name + " Wins!")

if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Ares")
    ability1 = Ability("Super Strength", 300)
    ability2 = Ability("Lasso of Truth", 130)
    ability3 = Ability("Wrath of the Gods", 80)
    ability4 = Ability("Sword Swipe", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
