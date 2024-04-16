from engines import *
from time import sleep
# Basic stats: AC, HP, Xp ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class): # 1 = melee 2 = mage 3 = ??
        if chose_class == 1:
            xp = 0
            money = 20
            hp = die_roll(6, 8)
            ac = 12
            # weapon = ?
            item = []

class Generals:
    def __init__(self):
        name = input("For which arrangement of letters shall you be called adventurer? \n")
        race = checker_option(3, "Pick a lineage of choice, dear traveler:\n [1] Human \n [2] Elf \n [3] Dwarf \n")
        sex = checker_option(2, "And what are thou exacly?\n [1] Male \n [2] Female \n")
        time.sleep(.4)
        print("Hmm")
        time.sleep(.2)
        print(name)
        time.sleep(.4)
        print("Very well!")

class Player():
    def __init__(self, chosen_class):
        generals = Generals()
        stats = Stats(chosen_class)


