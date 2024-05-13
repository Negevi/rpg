import random
from classes import *

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
    
def to_lvl(xp: float):
    while xp < 1:
        lvl = round(xp / 2, 0) # lvl up system, xp amount raises by 2x 
    return lvl + 1

def encounter(player):
    print("A fight will begin!")
    hostiles: list = Enemy.gen_fight(to_lvl(player.stats.xp))
    init = die_roll(1, 20)
    while (player.hp or hostiles.len()) != 0:
        if init >= 10:
            print("Your turn!")    # Player.turn(player)
            for enemy in hostiles:
                print("enemys turn!")   # Enemy.turn(enemy)
                hostiles.remove(enemy)


