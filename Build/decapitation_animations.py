from header_common import *
from header_animations import *
from compiler import *

# Dismember Anims - Paste These Near The Bottom of Your "module_animations.py" (right under "unused_horse_anim_100" and inside the last "]").

### Dismemberment Mod Kit Animations ###

amf_priority_jump           = 2
amf_priority_ride           = 2
amf_priority_continue       = 1
amf_priority_attack         = 10
amf_priority_cancel         = 12
amf_priority_defend         = 14
amf_priority_defend_parry   = amf_priority_defend + 1
amf_priority_throw          = amf_priority_defend + 1
amf_priority_blocked        = amf_priority_defend_parry
amf_priority_parried        = amf_priority_defend_parry
amf_priority_kick           = 33
amf_priority_jump_end       = 33
amf_priority_reload         = 60
amf_priority_mount          = 64
amf_priority_equip          = 70
amf_priority_rear           = 74
amf_priority_striked        = 80
amf_priority_fall_from_horse= 81
amf_priority_die            = 95



horse_move = 10000
combat     = 20000
defend     = 35000
blow       = 40000

attack_parried_duration = 0.6
attack_blocked_duration = 0.3
attack_blocked_duration_thrust = attack_blocked_duration + 0.3
attack_parried_duration_thrust = attack_parried_duration + 0.1
defend_parry_duration_1 = 0.6
defend_parry_duration_2 = 0.6
defend_parry_duration_3 = 0.8
ready_durn     = 0.35
defend_duration = 0.75
defend_keep_duration = 2.0
cancel_duration = 0.25

blend_in_defense = arf_blend_in_3
blend_in_ready = arf_blend_in_6
blend_in_release = arf_blend_in_5
blend_in_parry = arf_blend_in_5
blend_in_parried = arf_blend_in_3


blend_in_walk = arf_blend_in_3
blend_in_continue = arf_blend_in_1


 
add_block = [ # This animation will replace an unused_

 ["handchop", 0, amf_priority_striked|amf_play,
   [1.5, "strikes", 55, 71, arf_blend_in_3], 
 ],

 ["armchop", 0, amf_priority_striked|amf_play,
   [1.6, "strikes", 2284, 2305, arf_blend_in_3], 
 ],

 ]

from util_animations import *

def modmerge(var_set):
    try:
        var_name_1 = "animations"
        orig_animations = var_set[var_name_1]
        modmerge_animations(orig_animations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
      
def modmerge_animations(orig_animations):
    try:
        add_animations(orig_animations, add_block, check_duplicates = True) # replace existing and add new   
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise


 
 
 
 