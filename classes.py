from engines import *
from dicts import (weapons, enemys)
import random
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class: int): # 1 = melee 2 = mage 3 = assasin
        self.money = 20 
        self.xp = 0
        self.items = [] # default stats
        if chosen_class == 1:
            self.ac = 13
            self.hp = 22
            self.weapon = weapons["sword"]
            self.abilities = "Rage" # to add player abilities
        elif chosen_class == 2:
            self.ac = 11
            self.hp = 16
            self.weapon = weapons["staff"]
            self.abilities = "Cast Spell"
        elif chosen_class == 3:
            self.ac = 14
            self.hp = 14
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
        self.hp = enemy["hp"]
        self.weapon = enemy["weapon"]
        self.abilities = enemy["abilities"]
        
    def __str__(enemy):
        return f"{enemy.name}\n" \
           f"Hp: {enemy.hp}\n" \
           f"Weapon: {enemy.weapon}\n" \
           f"Abilitiy (s): {enemy.abilities}\n"
                   
    def get_enemy():
        key_id = 0
        key_randomizer = random.randint(0, 2) # max of monsters
        for key in enemys.keys():
            if key_randomizer == key_id:
                return enemys.get(key)
            else:
                key_id += 1
        
    def level(self, lvl):
        multiplier =  int(1 + lvl / 4) # to change, dont know yet
        self.hp * multiplier
        
    def gen_fight(Plvl) -> list:
        hostiles = []
        i = Plvl
        for i in range(0, Plvl):
            hostiles.append(Enemy.level(Enemy.get_enemy(), Plvl))
            i -= 1
        return hostiles