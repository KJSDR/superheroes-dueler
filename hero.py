# hero.py
import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        
        total_health = self.starting_health + opponent.starting_health
        self_chance = self.starting_health / total_health
        opponent_chance = opponent.starting_health / total_health

        
        winner = random.choices([self, opponent], [self_chance, opponent_chance])[0]

        
        print(f"{winner.name} defeats {self.name if winner != self else opponent.name}!")


if __name__ == "__main__":
    
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)

    hero1.fight(hero2)
