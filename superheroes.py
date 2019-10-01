import random
from random import randint


class Ability:
    def __init__(self, name, attack_strength):
        '''
        Create Instance Variables:
        name:String
        attack_strength: Integer
        '''
        self.name = str(name)
        self.attack_strength = int(attack_strength)

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage'''
        return randint(0, self.attack_strength)


class Armor:
    def __init__(self, name, max_block):
        '''
        Instantiate instance properties.
        name: String
        max_block: Integer
        '''
        self.name = str(name)
        self.max_block =int(max_block)

    def block(self):
        ''' Return a random value between 0 and max_block'''
        return randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        deaths: Integer
        kills: Integer
        '''
        self.name = str(name)
        self.starting_health = int(starting_health)
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        ''' Add hero ability to abilities list'''
        self.abilities.append(ability)

    def attack(self):
        '''
         Calculate the total damage from all ability attacks
         return: total: Integer
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(Armor(armor.name, armor.max_block))

    def defend(self):
        '''
        Runs 'block' method on each armor.
        Returns sum of all blocks
        '''
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked

    def take_damage(self, damage):
        ''' Updates self.current_health to reflect the damage minus the defense'''
        damage_taken = damage - self.defend()
        self.current_health -= damage_taken

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in'''

        while self.is_alive() and opponent.is_alive():

            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Clash - Both attacks are equal strength! ")#This is displayed in case of a draw
                break

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight

        if self.current_health > opponent.current_health:
            print(self.name + " Wins!")
            self.add_kill(1)
            opponent.add_deaths(1)
        else:
            print(opponent.name + " Wins!")
            self.add_deaths(1)
            opponent.add_kill(1)

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    #def add_relic(self, relic)Will revisit this


class Weapon(Ability):
    def attack(self):
        ''' Returns a random value between one half to the full attack power'''
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
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for i, hero in enumerate(self.heroes):
            if hero.name == name:
                self.heroes.pop(i)
                break
        #Hero not found
        else:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes'''
        self.heroes.append(hero)

    def attack(self, opposing_team):
        ''' Battle each team against each other'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the H

        while len([h for h in self.heroes if h.is_alive()]) > 0 and len([h for h in opposing_team.heroes if h.is_alive()]) > 0:
            ally = random.choice([h for h in self.heroes if h.is_alive()])
            opp = random.choice([h for h in opposing_team.heroes if h.is_alive()])
            ally.fight(opp)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.

        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            print(hero.kills, hero.deaths)


class Arena:
    def __init__(self):
        '''
        Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = Team("Team Good Guy")
        self.team_two = Team("Team Bad Guy")

    def create_ability(self):
        '''
        Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("Enter an ability name: ")
        strength = int(input("Enter ability strength: "))
        return Ability(name, strength)

    def create_weapon(self):
        '''
        Prompt user for Weapon information
        return Weapon with values from user input.
        '''
        name = input("Enter a Weapon Name ")
        strength = int(input("Enter weapon strength: "))
        return Weapon(name, strength)

    def create_armor(self):
        '''
        Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("Enter a Weapon Name ")
        strength = int(input("Enter armor block: "))
        return Armor(name, strength)

    def create_hero(self):
        '''
        Prompt user for Hero information
        return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        name = input("Enter a hero name: ")
        hero = Hero(name)
        hero.add_ability(self.create_ability())
        hero.add_armor(self.create_armor())
        hero.add_weapon(self.create_weapon())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one'''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        count = int(input("Enter # of heroes for team 1: "))

        while(count>0):
            self.team_one.heroes.append(self.create_hero())
            count -= 1

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        count = int(input("Enter # of heroes for team 2: "))
        team_two = Team("Team Two")
        while(count>0):
            team_two.heroes.append(self.create_hero())
            count -= 1

    def team_battle(self):
        '''Battle team_one and team_two together'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def show_stats(self):
         '''Prints team statistics to terminal'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        if len(self.team_one.alive_heroes()) > 0:
            print("Team One Wins!")
        else:
            print("Team Two Wins!")
        self.team_one.stats()
        self.team_two.stats()
        self.team_one.alive_heroes()
        self.team_two.alive_heroes()

'''
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
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
'''

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
