# team.py
from random import choice
from hero import Hero

class Team:
    def __init__(self, name):
        '''Initialize your team with its name and an empty list of heroes.'''
        self.name = name
        self.heroes = list()  # List to store heroes

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero by name from heroes list.'''
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
                break
        return 0 if not found_hero else 1

    def view_all_heroes(self):
        '''Print out all heroes in the team.'''
        for hero in self.heroes:
            print(hero.name)  # Assuming the Hero class has a 'name' attribute

    def revive_heroes(self, health=100):
        '''Reset all heroes health to their starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            # Calculate kill-to-death ratio
            kd = hero.kills / hero.deaths if hero.deaths > 0 else hero.kills
            print(f"{hero.name} Kill/Deaths: {kd:.2f}")

    def attack(self, other_team):
        '''Battle each team against each other.'''
        living_heroes = [hero for hero in self.heroes if hero.is_alive()]
        living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Randomly select a living hero from each team
            hero1 = choice(living_heroes)
            hero2 = choice(living_opponents)

            # Have them fight
            hero1.fight(hero2)

            # Update living heroes and opponents lists
            if not hero1.is_alive():
                living_heroes.remove(hero1)
            if not hero2.is_alive():
                living_opponents.remove(hero2)

        # Declare winner
        if len(living_heroes) > 0:
            print(f"{self.name} won the battle!")
        else:
            print(f"{other_team.name} won the battle!")
