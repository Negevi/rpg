# Start of a long journey, to S

from engines import *
from classes import *

# Melee has extra Hp and. Mage has a Eldritch blast mechanic. 
# Crit fail and Crit Max mechanic
# Some sort of death save mehcanic?

x = checker_option(2, "What would thou aspire to be in this adventure?\n [1] Melee \n [2] Mage \n [3] to be implemented\n ")
player = Player(x)
Player.statcheck(player)