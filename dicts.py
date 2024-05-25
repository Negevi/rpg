weapons = {
    "none": {
        "name": "None",
        "desc": "No weapon equiped",
        "dmg": (1, 4, 0),
        "spell_caster": False,
        "special": None
    },
    "sword": {
        "name": "Sword",
        "desc": "A simple, rusty, sword. Used mainly for decoration!",
        "dmg": (2, 8, 0),
        "spell_caster": False,
        "special": None
    }, 
    "staff": {
        "name": "Staff",
        "desc": "Wood. Thats it.",
        "dmg": (1, 9, 0),
        "spell_caster": True,
        "special": None
    },
    "dagger": {
        "name": "Dagger",
        "desc": "A shitty kitchen knife, scary even to the mightiest tomatoes. who even called this a dagger?",
        "dmg": (4, 4, 0),
        "spell_caster": False,
        "special": None
    },
}
abilities = {
    "none": {
        "name": "None",
        "desc": "No special abilities."
    },
    "brones": {
        "name": "Brones",
        "desc": "once per turn, removes an arm. Takes 4 dmg but can't die by using this. Arm has the same stats as the skelly, but halfed, as well as base 1d4 dmg.",
    },
    "ghost": {
        "name": "Ghost",
        "desc": "Enemy gets + 2 AC and has advantadge on all fisical atack type atack rolls.",
    },
}
enemys = {
    "goblin": {
        "name": "Goblin",
        "desc": "Oh no! somebody call the goblin slayer!",
        "hp": 20,
        "ac": 8,
        "weapon": weapons["dagger"],
        "abilities": abilities["none"],
    },
    "skeleton": {
        "name": "Skeleton",
        "desc": "Spooky scary",
        "hp": 15,
        "ac": 12,
        "weapon": weapons["sword"],
        "abilities": abilities["brones"],
    },
    "skeleton-arm": {
        "name": "Helping-hand",
        "desc": "Need a hand?",
        "hp": 8,
        "ac": 10,
        "weapon": weapons["none"],
        "dmg": (1, 4, 0),
    },
    "wraith": {
        "name": "Wraith",
        "desc": "A ghost! my sword probably isn't gonna be able to cut him...",
        "hp": 25,
        "ac": 13,
        "weapon": weapons["none"],
        "abilities": abilities["ghost"],
    }
} # the abilities to this point are merely to integrate battle mechanics, will prob change later