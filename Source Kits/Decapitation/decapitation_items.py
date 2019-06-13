from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

from compiler import *

################### NEW v1.0 - import definitions from newly created module_troops_def.py file
from module_troops_def import *
# Dismember Items - Add These Items To Your Module_Items.py, just before
# the end (before "items_end").

### Dismemberment Mod Kit Items ###
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent


############################
items = [
### Body Parts ###
["invisiblegloves","Invisiblegloves", [("invisiblegloves",0)], itp_type_hand_armor,0, 550, weight(0)|abundance(5)|body_armor(0)|difficulty(0),imodbits_armor],
["looter_bully_handless_body", "Ragged Stolen Brigandine", [("looter_bully_handless_body",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 27 , weight(2)|abundance(5)|head_armor(0)|body_armor(27)|leg_armor(10), imodbits_none ],
["looter_thug_armless_body", "Ragged Cloak", [("looter_thug_armless_body",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 27 , weight(2)|abundance(5)|head_armor(0)|body_armor(27)|leg_armor(10), imodbits_none ],
["thin_looter_armless_body", "Leather Outfit", [("thin_looter_armless_body",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 27 , weight(2)|abundance(5)|head_armor(0)|body_armor(17)|leg_armor(6), imodbits_none ],  
["fat_peasant_handless_body", "Large Peasant Apron", [("fat_peasant_handless_body",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 27 , weight(2)|abundance(5)|head_armor(0)|body_armor(18)|leg_armor(8), imodbits_none ], 
["severedhand", "Severed Hand", [("severedhand",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 42 , weight(2)|abundance(50)|hit_points(2)|body_armor(20)|spd_rtng(100)|weapon_length(3),imodbits_none ],
["fatseveredarm", "Severed Arm", [("fatseveredarm",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 42 , weight(2)|abundance(50)|hit_points(10)|body_armor(25)|spd_rtng(100)|weapon_length(8),imodbits_none ],  
["severedarm", "Severed Arm", [("severedarm",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 42 , weight(2)|abundance(50)|hit_points(3)|body_armor(15)|spd_rtng(100)|weapon_length(8),imodbits_none ],  

["invisible_head", "Headless", [("invalid_item",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["cut_off_head_male", "Bloody Male Head", [("cut_off_head_male",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["cut_off_head_female", "Bloody Female Head", [("cut_off_head_female",0)], itp_type_head_armor|itp_covers_head   ,0, 0 , weight(4)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

["default_male_no_right_arm", "Your right arm is missing!", [("man_body_right_arm_gone",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 0 , weight(0)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none ], 
["default_male_no_left_arm", "Your left arm is missing!", [("man_body_left_arm_gone",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 0 , weight(0)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none ], 
["default_male_no_arms", "Your arms are missing!", [("man_body_both_arms_gone",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0, 0 , weight(0)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none ], 
### Body parts END ###


### Debug weapons ###
["supercrossbow", "Semi-Automatic Crossbow", [("crossbow_b",0)], itp_type_crossbow|itp_primary|itp_two_handed|itp_extra_penetration ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 10, weight(3)|abundance(10)|difficulty(0)|spd_rtng(68)|accuracy(240)|shoot_speed(110) | thrust_damage(70 ,  pierce)|max_ammo(30),imodbits_crossbow ],
["super_bolts","Super Bolts", [("bolt",0),("bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 10,weight(2)|abundance(5)|weapon_length(63)|thrust_damage(60,pierce)|max_ammo(200),imodbits_missile],
["supersledge", "Power-Sledge", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_bonus_against_shield|itp_can_knock_down|itp_primary|itp_two_handed, itc_nodachi|itcf_carry_spear, 1000 , weight(10)|spd_rtng(100) | weapon_length(90)|swing_damage(150, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
### Debug weapons END ###

]############################
 

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "items"
        orig_items = var_set[var_name_1]
        orig_items.extend(items) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
		
		
		
		
 