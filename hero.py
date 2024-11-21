# hero.py
from random import choice
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
            deaths: Integer
            kills: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0  # Track the number of deaths
        self.kills = 0   # Track the number of kills

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

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update self.deaths by num_deaths amount'''
        self.deaths += num_deaths

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
                self.add_kill(1)  # Self gains a kill if the opponent dies
                opponent.add_death(1)  # Opponent gains a death
                print(f"{self.name} won!")
                return

            self.take_damage(opponent_damage)

            if not self.is_alive():
                opponent.add_kill(1)  # Opponent gains a kill if self dies
                self.add_death(1)  # Self gains a death
                print(f"{opponent.name} won!")
                return
