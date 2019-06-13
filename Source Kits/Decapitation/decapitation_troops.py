import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *


################### NEW v1.0 - import definitions from newly created module_troops_def.py file
from module_troops_def import *
#########################

troops = [
# Add these troops to "module_troops.py" just near the bottom of the file (right under the last troop entry: "relative_of_merchants_end").

### Dismemberment Mod Kit Troops ###
["looter_bully_handless","Looter Bully","Looter Bullies",tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_neutral,
  # [],
  [itm_cudgel,itm_invisiblegloves,
    itm_looter_bully_handless_body,itm_leather_boots,itm_severedhand],
   def_attrib|level(15),wp_melee(90),knows_common|knows_shield_4|knows_power_strike_1|knows_ironflesh_2,bandit_face1, bandit_face2, nord_face_young_1, nord_face_old_2],

["looter_thug_armless","Looter Thug","Looter Thug",tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_neutral,
  # [],
  [itm_falchion,itm_invisiblegloves,
    itm_looter_thug_armless_body,itm_leather_boots,itm_fatseveredarm],
   def_attrib|level(15),wp_melee(90),knows_common|knows_shield_9|knows_power_strike_2|knows_ironflesh_1,bandit_face1, bandit_face2, nord_face_young_1, nord_face_old_2],

["thin_looter_armless","Looter Thief","Looter Thief",tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_neutral,
  # [],
  [itm_falchion,itm_invisiblegloves,
    itm_thin_looter_armless_body,itm_leather_boots,itm_severedarm],
   def_attrib|level(19),wp_melee(90),knows_common|knows_shield_4|knows_power_strike_1|knows_ironflesh_3,bandit_face1, bandit_face2, nord_face_young_1, nord_face_old_2],

["fat_peasant_handless","Fat Peasant","Fat Peasants",tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_neutral,
   # [],
   [itm_cleaver,itm_invisiblegloves,
    itm_fat_peasant_handless_body,itm_hide_boots,itm_severedhand],
   def_attrib|level(6),wp_melee(60),knows_common|knows_shield_4|knows_power_strike_1|knows_ironflesh_1,man_face_middle_1, man_face_old_2],
### Dismemberment Mod Kit Troops END ###
]########################
#########################


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "troops"
        orig_troops = var_set[var_name_1]
        orig_troops.extend(troops) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)



