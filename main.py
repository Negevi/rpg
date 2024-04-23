from engines import *
from classes import *

# Melee has Rage. Mage has a Eldritch blast mechanic. Assasin can assasinate
# Crit fail and Crit Max mechanic
# Some sort of death save mehcanic?

player = Player(checker_option(3, "Welcome traveler! What class would thou most like to be in this adventure?\n [1] Melee\n [2] Mage\n [3] Assasin\n"))
print(player)