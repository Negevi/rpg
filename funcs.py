from dicts import weapons, enemys
import random

# Basic stats: AC, HP, XP ( << class), Items (list of item class), weapon, money, and generals (name, race, sex?)
class Stats:
    def __init__(self, chosen_class: int):  # 1 = melee, 2 = mage, 3 = assassin
        self.money: int = 20
        self.xp: int = 0
        self.items: list = []  # default stats
        if chosen_class == 1:
            self.ac: int = 13
            self.hp: int = 22
            self.weapon = weapons["sword"]
            self.abilities = "Rage"  # to add player abilities
        elif chosen_class == 2:
            self.ac: int = 11
            self.hp: int = 16
            self.weapon = weapons["staff"]
            self.abilities = "Cast Spell"
        elif chosen_class == 3:
            self.ac: int = 14
            self.hp: int = 14
            self.weapon = weapons["dagger"]
            self.abilities = "Assassinate"

class Player:
    def __init__(self, chosen_class: int):
        self.stats = Stats(chosen_class)

    def __str__(self):
        return (f"Max hp: {self.stats.hp}\n"
                f"XP: {self.stats.xp}\n"
                f"Armor class: {self.stats.ac}\n"
                f"Gold: {self.stats.money}\n"
                f"Equipped weapon: {self.stats.weapon['name']}\n   {self.stats.weapon['desc']}\n"
                f"Item bag: {', '.join(self.stats.items)}\n")

    def turn(self, enemy):
        check = Engines.checker_option(2, "What would you like to do?\n [0] use ability\n [1] Attack")
        if check == 0:
            print("Use ability!")
        if check == 1:
            if Engines.die_roll(1, 20) + self.stats.weapon["dmg"][0] >= enemy.ac:
                print("Hit!")
                dmg = Weapons.roll_dmg(self.stats.weapon)
                enemy.hp -= dmg
            else:
                print("Miss!")

class Weapons:  # intended for creation of new weapons
    def __init__(self, dmg: tuple, spell_caster: bool, desc: str):  # dmg is defined as (n, faces, flat modifier)
        self.desc = desc
        self.dmg = (dmg[0], dmg[1], dmg[2])
        self.spell_caster = spell_caster
        self.special = None

    @staticmethod
    def dictadd_weapon(name: str, dmg: tuple, spell_caster: bool, desc: str):  # add special weapon support
        weapon = Weapons(dmg, spell_caster, desc)
        weapons[name] = {
            "desc": weapon.desc,
            "dmg": weapon.dmg,
            "spell_caster": weapon.spell_caster,
            "special": None
        }

    @staticmethod
    def roll_dmg(weapon):
        roll = Engines.die_roll(weapon["dmg"][0], weapon["dmg"][1]) + weapon["dmg"][2]
        print(f"{roll} dmg!")
        return roll

class Enemy:
    def __init__(self):
        enemy = Enemy.get_enemy()
        self.name = enemy["name"]
        self.desc = enemy["desc"]
        self.hp = enemy["hp"]
        self.weapon = enemy["weapon"]
        self.abilities = enemy["abilities"]
        self.ac = enemy["ac"]

    def __str__(self):
        return (f"{self.name}\n"
                f"Hp: {self.hp}\n"
                f"Description: {self.desc}\n"
                f"Weapon: {self.weapon['name']}\n"
                f"Ability(s): {self.abilities['name']}\n {self.abilities['desc']}\n")

    def turn(self, player):
        if Engines.die_roll(1, 6) == 6:  # here, if 1d6 = 6, use ability
            print("Ability!")
        else:
            dmg = Weapons.roll_dmg(self.weapon)
            player.stats.hp -= dmg

    @staticmethod
    def get_enemy():
        key_randomizer = random.randint(0, len(enemys) - 1)
        key_id = 0
        for key in enemys.keys():
            if key_randomizer == key_id:
                return enemys.get(key)
            else:
                key_id += 1

    @staticmethod
    def level(enemy, lvl):
        multiplier = int(1 + lvl / 4)  # to change, don't know yet
        enemy['hp'] *= multiplier
        return enemy

    @staticmethod
    def gen_fight(Plvl):
        Engines.to_lvl(Plvl)
        hostiles = []
        for _ in range(Plvl):
            hostiles.append(Enemy())
        return hostiles

    @staticmethod
    def print_hostiles(hostiles):
        for id, enemy in enumerate(hostiles):
            print(f"{enemy}\n id={id}")

def encounter(player):
    hostiles = Enemy.gen_fight(Engines.to_lvl(player.stats.xp))
    init = Engines.die_roll(1, 20)
    print("init!^")
    while player.stats.hp > 0 and len(hostiles) > 0:
        if init >= 10:
            Enemy.print_hostiles(hostiles)
            enemy = hostiles[Engines.checker_option(len(hostiles), "Which enemy will you attack? (Id)\n")]
            player.turn(enemy)
            if enemy.hp <= 0:
                hostiles.remove(enemy)

            for enemy in hostiles:
                print(f"{enemy.name} turn!")
                enemy.turn(player)
        else:
            for enemy in hostiles:
                print(f"{enemy.name} turn!")
                enemy.turn(player)

            Enemy.print_hostiles(hostiles)
            enemy = hostiles[Engines.checker_option(len(hostiles), "Which enemy will you attack? (Id)\n")]
            player.turn(enemy)
            if enemy.hp <= 0:
                hostiles.remove(enemy)

class Engines:
    @staticmethod
    def checker_option(n, statement):
        x = int(input(statement))
        if x < 0 or x >= n:
            return Engines.checker_option(n, statement)
        else:
            return x

    @staticmethod
    def die_roll(n, faces):
        die_roll = 0
        for _ in range(n):
            roll = random.randint(1, faces)
            die_roll += roll
            print(f"{n}D{roll},")
        print(f"total: {die_roll}")
        return die_roll

    @staticmethod
    def adv_roll(x, y):
        return max(x, y)

    @staticmethod
    def dsv_roll(x, y):
        return min(x, y)

    @staticmethod
    def to_lvl(xp):
        lvl = 0
        while xp > 1:
            lvl += round(xp / 2, 1)  # lvl up system, xp amount raises by 2x
            xp /= 2
        return lvl + 1