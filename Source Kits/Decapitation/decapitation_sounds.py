from header_sounds import *
from compiler import *

# Alter the "shield_broken" line(s) in "module_sounds.py" to match this one (remember to save a backup):

sounds = [
### Dismemberment Mod Kit - modified line ###
 ("shield_broken",sf_priority_9, ["shield_broken.ogg","shield_broken1.ogg","shield_broken2.ogg"]),
#################
 
# Paste these lines near the bottom of the "module_sounds.py" -file:
### Dismemberment Mod Kit Sound Effects ###
 ("decapitation",sf_priority_9|sf_vol_11, ["decap1.ogg","decap2.ogg","decap3.ogg","decap4.ogg"]),
]
#################




# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "sounds"
        orig_sounds = var_set[var_name_1]
        orig_sounds.extend(sounds) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)





