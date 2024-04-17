from engines import *
import time
from dataclasses import dataclass
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class): # 1 = melee 2 = mage 3 = ??
        if chosen_class == 1:
            self.xp = 0
            self.ac = 12
            self.hp = die_roll(6, 8)
            print(f"You have been granted {self.hp} Health Points!")
            self.money = 20
            self.weapon = None # empty vec or no info at all????
            self.item = []

class Generals:
    def __init__(self):
        self.name = input("For which arrangement of letters shall you be called adventurer? \n")
        self.race = checker_option(3, "Pick a lineage of choice, dear traveler:\n [1] Human \n [2] Elf \n [3] Dwarf \n")
        self.sex = checker_option(2, "And what are thou exacly?\n [1] Male \n [2] Female \n")

class Player():
    def __init__(self, chosen_class):
        self.generals = Generals()
        self.stats = Stats(chosen_class)
    def statcheck(player):
        print(f"{player.generals.name}: \n Max hp: {player.stats.hp} \n Xp: {player.stats.xp} \n Armor class: {player.stats.ac} \n Gold: {player.stats.money} \n Equiped weapon(s): {player.stats.weapon} \n Item bag: {player.stats.item} \n")


