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
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(Armor(armor.name, armor.max_block))

    def defend(self):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked

    def take_damage(self, damage):
        damage_taken = damage - self.defend()
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
            self.add_kill(1)
            opponent.add_deaths(1)
        else:
            print(opponent.name + " Wins!")
            self.add_deaths(1)
            opponent.add_kill(1)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

class Weapon(Ability):
    def attack(self):
        ''' Returns a random value between one half to the full attack power '''
        return randint(self.attack_strength//2, self.attack_strength)


class Team:
    def __init__(self, team_name):
        '''
            team_name: String
            heroes: List
        '''
        self.name = team_name
        self.heroes = []

    def remove_hero(self, name):
        for i, hero in enumerate(self.heroes):
            if hero.name == name:
                self.heroes.pop(i)
                break
        #Hero not found
        else:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, opposing_team):

        while len([h for h in self.heroes if h.is_alive()]) > 0 and len([h for h in opposing_team.heroes if h.is_alive()]) > 0:
            ally = random.choice([h for h in self.heroes if h.is_alive()])
            opp = random.choice([h for h in opposing_team.heroes if h.is_alive()])
            ally.fight(opp)


    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health


    def stats(self):
        for hero in self.heroes:
            print(hero.kills, hero.deaths)

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
