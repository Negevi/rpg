from dicts import (weapons, enemys)
import random
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class: int): # 1 = melee 2 = mage 3 = assasin
        self.money: int = 20 
        self.xp: int = 0
        self.items: list = [] # default stats
        if chosen_class == 1:
            self.ac: int = 13
            self.hp: int = 22
            self.weapon = weapons["sword"]
            self.abilities = "Rage" # to add player abilities
        elif chosen_class == 2:
            self.a: int = 11
            self.hp: int = 16
            self.weapon = weapons["staff"]
            self.abilities = "Cast Spell"
        elif chosen_class == 3:
            self.ac: int = 14
            self.hp: int = 14
            self.weapon = weapons["dagger"]
            self.abilities = "Assasinate"
            
class Player():
    def __init__(self, chosen_class: int):
        self.stats = Stats(chosen_class)
        
    def __str__(player):
        return f"Max hp: {player.stats.hp}\n" \
           f"XP: {player.stats.xp}\n" \
           f"Armor class: {player.stats.ac}\n" \
           f"Gold: {player.stats.money}\n" \
           f"Equipped weapon: {player.stats.weapon["name"]}\n   {player.stats.weapon["desc"]}\n" \
           f"Item bag: {', '.join(player.stats.items)}"
    
    def turn(self, enemy):
        check = checker_option(2, "What would you like to do?\n [0] use ability\n [1] Atack")
        if check == 0:
            print("use ability!")
        if check == 1:
            if die_roll(1, 20, self.stats.weapon.dmg[0]) >= enemy.ac:
                print("Hit!")
                dmg = Weapons.roll_dmg(self.stats.weapon)
                enemy.hp -= dmg
            else:
                print("Miss!")
           
class Weapons(): # intended for creation of new weapons
    def __init__(self, dmg: tuple, spell_caster: bool, desc: str): # Note that dmg is defined as n + faces + flat modifier in a tuple.
        self.desc = desc
        self.dmg = (dmg[0], dmg[1], dmg[2])
        self.spell_caster = spell_caster
        self.special = None
        
    def dictadd_weapon(self, name: str, dmg: tuple, spell_caster: bool, desc: str): # add special weapon suport
        weapon = Weapons(dmg, spell_caster, desc)
        weapons[name] = {
            "desc": weapon.desc,
            "dmg": weapon.dmg,
            "spell_caster":  weapon.spell_caster,
            "special": None
        }
    
    def roll_dmg(self, weapon):
        roll = die_roll(weapon.dmg[0], weapon.dmg[1]) + weapon.dmg[2]
        print(f"You did {roll} dmg!")
        return roll      

class Enemy():
    def __init__(self):
        enemy = Enemy.get_enemy()
        self.name = enemy["name"]
        self.desc = enemy["desc"]
        self.hp = enemy["hp"]
        self.weapon = enemy["weapon"]
        self.abilities = enemy["abilities"]
        self.ac = enemy["ac"]
        
    def __str__(self):
        return f"{self.name}\n" \
        f"Hp: {self.hp}\n" \
        f"Description: {self.desc}\n" \
        f"Weapon: {self.weapon['name']}\n" \
        f"Ability(s): {self.abilities['name']}\n {self.abilities['desc']}\n"
        
    @staticmethod          
    def get_enemy():
        key_id = 0
        key_randomizer = random.randint(0, 2) # max of monsters
        for key in enemys.keys():
            if key_randomizer == key_id:
                return enemys.get(key)
            else:
                key_id += 1
    
    @staticmethod
    def level(enemy, lvl):
        multiplier =  int(1 + lvl / 4) # to change, dont know yet
        enemy['hp'] * multiplier
        return enemy
    
    @staticmethod    
    def gen_fight(Plvl):
        to_lvl(Plvl)
        hostiles = []
        i = Plvl
        for i in range(0, Plvl):
            hostiles.append(Enemy())
            i -= 1
        return hostiles
    
    @staticmethod
    def print_hostiles(hostiles):
        id = 0
        for enemy in hostiles:
            print(f"{enemy}\n id={id}")
            id += 1

def checker_option(n, statement):
    x = int(input(statement))
    if x < 0 or x >= n:
        checker_option(n, statement)
    else:
        return x

# nDfaces
def die_roll(n, faces):
    die_roll = 0
    p = n
    while n > 0:
        roll = random.randint(1, faces)
        die_roll += roll
        print(f"{p}D{roll},")
        n -= 1
    print(f"total: {die_roll}")
    return die_roll

def adv_roll(x, y):
    if x >= y:
        return x
    else:
        return y

def dsv_roll(x, y):
    if x <= y:
        return x
    else:
        return y
    
def to_lvl(xp):
    lvl = 0
    while xp > 1:
        lvl += round(xp / 2, 0) # lvl up system, xp amount raises by 2x 
    return lvl + 1

def encounter(player):
    print("A fight will begin!")
    hostiles: list = Enemy.gen_fight(player.stats.xp)
    Enemy.print_hostiles(hostiles)
    init = die_roll(1, 20)
    print("init!")
    while (player.stats.hp or hostiles.len()) != 0:
        if init >= 10:
            Player.turn(player, hostiles[0])
            for enemy in hostiles:
                print("enemys turn!")
                hostiles.remove(enemy)


