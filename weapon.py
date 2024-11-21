import random
from ability import Ability  # Assuming Ability class exists

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":
    weapon = Weapon("Lasso of Truth", 90)
    print(f"Weapon attack power: {weapon.attack()}")
