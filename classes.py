from engines import *
import time
from dataclasses import dataclass
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class: int): # 1 = melee 2 = mage 3 = assasin
        self.money = 20 # default stats
        self.xp = 0
        self.item = []
        if chosen_class == 1:
            self.ac = 13
            self.hp = 22
            self.weapon = sword
        elif chosen_class == 2:
            self.ac = 11
            self.hp = 16
            self.weapon = staff
        elif chosen_class == 3:
            self.ac = 14
            self.hp = 14
            self.weapon = dagger
class Player():
    def __init__(self, chosen_class: int):
        self.stats = Stats(chosen_class)
        
    def __str__(player):
        return f"Max hp: {player.stats.hp} \n Xp: {player.stats.xp} \n Armor class: {player.stats.ac} \n Gold: {player.stats.money} \n Equiped weapon(s): {player.stats.weapon} \n Item bag: {player.stats.item} \n"

class Weapons():
    def __init__(self, n: int, faces: int, dmg_mod: int, dual_wield: bool, spell_caster: bool, desc: str): # Note that dmg is defined as n + faces + flat modifier in a tuple.
        self.dual_wield = dual_wield
        self.spell_caster = spell_caster
        self.special = None
        self.desc = desc
        self.dmg = (n, faces, dmg_mod)
        