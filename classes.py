from engines import *
from generals import weapons
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class: int): # 1 = melee 2 = mage 3 = assasin
        self.money = 20 # default stats
        self.xp = 0
        self.item = []
        if chosen_class == 1:
            self.ac = 13
            self.hp = 22
            self.weapon = weapons["sword"]
        elif chosen_class == 2:
            self.ac = 11
            self.hp = 16
            self.weapon = weapons["staff"]
        elif chosen_class == 3:
            self.ac = 14
            self.hp = 14
            self.weapon = weapons["dagger"]
            
class Player():
    def __init__(self, chosen_class: int):
        self.stats = Stats(chosen_class)
        
    def __str__(player):
        return f"Max hp: {player.stats.hp} \n Xp: {player.stats.xp} \n Armor class: {player.stats.ac} \n Gold: {player.stats.money} \n Equiped weapon(s): {player.stats.weapon} \n Item bag: {player.stats.item} \n"

class Weapons(): # intended for creation of new weapons
    def __init__(self, dmg: tuple, spell_caster: bool, desc: str): # Note that dmg is defined as n + faces + flat modifier in a tuple.
        self.desc = desc
        self.dmg = (dmg[0], dmg[1], dmg[2])
        self.spell_caster = spell_caster
        self.special = None
        
    def dictadd(self, name: str, dmg: tuple, spell_caster: bool, desc: str): # add special weapon suport
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