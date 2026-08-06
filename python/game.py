import random

class Character_attributes:
    def __init__(self, name, hp , attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack
    
    def is_alive(self):
        return self.hp > 0

class Player(Character_attributes):

    def attack(self, target):
        self.attack_dmg = random.randint(self.attack_power - 4, self.attack_power + 2)
        print(f"{self.name} has attacked {target.name}, dealing {self.attack_dmg} damage!\n")        
    
    def take_dmg(self, damage, attacker_name):
        self.dmg_taken = damage
        self.hp -= self.dmg_taken
        if self.hp <= 0:
            self.hp = 0
        print(f"{self.name} has been attacked by {attacker_name} losing {self.dmg_taken} HP!\n HP: {self.hp}/{self.max_hp}\n")

class Enemy(Character_attributes):
    def attack(self, target):
        self.attack_dmg = random.randint(self.attack_power - 1, self.attack_power + 4)
        print(f"{self.name} has attacked {target.name}, dealing {self.attack_dmg} damage!\n")
    
    def take_dmg(self, damage, attacker_name):
        self.dmg_taken = damage
        self.hp -= self.dmg_taken
        if self.hp <= 0:
            self.hp = 0
        print(f"{self.name} has been attacked by {attacker_name} losing {self.dmg_taken} HP!\n HP: {self.hp}/{self.max_hp}\n")
    
class Battle:
    def start_battle(self, player, enemy):
        print(f"A battle has started between {player.name} and {enemy.name}\n")

Player_1 = Player("Billy", 50, 5)
Enemy_1 = Enemy("Goblin", 30, 6)
battle = Battle()

battle.start_battle(Player_1, Enemy_1)

while Player_1.is_alive() and Enemy_1.is_alive():
    Enemy_1.attack(Player_1)
    Player_1.take_dmg(Enemy_1.attack_dmg, Enemy_1.name)
    if not Player_1.is_alive():
        print(f"{Enemy_1.name} has won!")
        break
    
    Player_1.attack(Enemy_1)
    Enemy_1.take_dmg(Player_1.attack_dmg, Player_1.name)
    if not Enemy_1.is_alive():
        print(f"{Player_1.name} has won!")
        break



    #def heal(self):
        #self.heal_amount = random.randint(5,11)
        #self.hp += self.heal_amount
        #print(f"{self.name} has healed for {self.heal_amount} HP!\n HP: {self.hp}/{self.max_hp}")