from funcs import *

# Melee has Rage. Mage has a Eldritch blast mechanic. Assasin can assasinate
# Crit fail and Crit Max mechanic
# Some sort of death save mehcanic?

player = Player(checker_option(2, "Choose class: \n [1] Melee \n [2] Mage \n [3] Rogue\n"))
Enemy.print_hostiles(Enemy.gen_fight(player.stats.xp))