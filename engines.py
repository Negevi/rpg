import random

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
    
