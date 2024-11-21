# hero.py
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors'''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        ''' Add weapon to abilities list (treating weapon like an ability) '''
        self.abilities.append(weapon)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
           return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        blocked_damage = self.defend()
        actual_damage = max(0, damage - blocked_damage) 
        self.current_health -= actual_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        return self.current_health > 0

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        while True:
            if not self.abilities and not opponent.abilities:
                print("Draw")
                return

            self_damage = self.attack()
            opponent_damage = opponent.attack()

            opponent.take_damage(self_damage)

            if not opponent.is_alive():
                print(f"{self.name} won!")
                return

            self.take_damage(opponent_damage)

            if not self.is_alive():
                print(f"{opponent.name} won!")
                return


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())