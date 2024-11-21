# team.py
from hero import Hero 

class Team:
    def __init__(self, name):
        '''Initialize your team with its name and an empty list of heroes.'''
        self.name = name
        self.heroes = list()

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
            print(hero.name) 

    def add_hero(self, hero):
        '''Add Hero object to the heroes list.'''
        self.heroes.append(hero)
