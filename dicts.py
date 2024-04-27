weapons = {
    "sword": {
        "name": "Sword",
        "desc": "A simple, rusty, sword. Used mainly for decoration!",
        "dmg": (2, 8, 0),
        "spell_caster":  False,
        "special": None
    }, 
    "staff": {
        "name": "Staff",
        "desc": "Wood. Thats it.",
        "dmg": (1, 9, 0),
        "spell_caster":  True,
        "special": None
    },
    "dagger": {
        "name": "Sagger",
        "desc": "A shitty kitchen knife, scary even to the mightiest tomatoes. who even called this a dagger?",
        "dmg": (4, 4, 0),
        "spell_caster":  False,
        "special": None
    }, 
}
enemys = {
    "goblin": {
        "name": "Goblin",
        "hp": 20,
        "ac": 8,
        "weapon": weapons["dagger"],
        "abilities": None,
    },
    "skeleton": {
        "name": "Skeleton",
        "hp": 15,
        "ac": 12,
        "weapon": weapons["sword"],
        "abilities": {
            "Brones": {
                "name": "Brones",
                "dmg": (1, 4, 0),
                "desc": "once per turn, removes an arm. Takes 4 dmg but cant die by using this. Arm has the same stats, but halfed, as well as base 1d4 dmg.",
                }
            },
    },
    "wraith": {
        "name": "Wraith",
        "hp": 25,
        "ac": 15,
        "weapon": None, # to add
        "abilities": ["Ghost"], # all fisical atacks have disadv.
    },
} # the abilities to this point are merely to integrate battle mechanics, will prob change later