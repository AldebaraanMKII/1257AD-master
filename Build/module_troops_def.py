
# -*- coding: utf-8 -*-

import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *



# Some constant and function declarations to be used below...

def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

tf_guarantee_all = tf_guarantee_shield | tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_horse| tf_guarantee_ranged| tf_guarantee_helmet| tf_guarantee_gloves
  
  
  
#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_10|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7|agi_5|int_4|cha_4
def_attrib_multiplayer = str_14|agi_14|int_4|cha_4

knows_lord_1 = knows_riding_10|knows_trade_3|knows_inventory_management_10|knows_tactics_8|knows_prisoner_management_4|knows_leadership_10|knows_engineer_10

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_10
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_10 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_10

lord_attrib = str_30|agi_19|int_19|cha_21|level(48)
lord_wp = wp_one_handed(400)|wp_two_handed(400)|wp_polearm(400)|wp_archery(300)|wp_crossbow(250)|wp_throwing(250)
lord_skills = knows_riding_8|knows_trade_4|knows_inventory_management_10|\
              knows_tactics_8|knows_prisoner_management_6|knows_leadership_8|\
              knows_engineer_9|knows_ironflesh_10|knows_power_strike_10|knows_power_draw_10|\
              knows_athletics_6|knows_trainer_8|knows_surgery_6|knows_horse_archery_8|knows_shield_10

knight_attrib_1 = str_18|agi_12|int_6|cha_12|level(30)
knight_attrib_2 = str_21|agi_15|int_9|cha_15|level(35)
knight_attrib_3 = str_24|agi_18|int_12|cha_18|level(40)
knight_attrib_4 = str_27|agi_19|int_15|cha_21|level(45)
knight_attrib_5 = str_30|agi_22|int_18|cha_24|level(50)
####### NEW v3.1-KOMKE START-
# knight_skills_1 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_1|knows_tactics_1|knows_prisoner_management_1|knows_leadership_2|knows_engineer_5|knows_trainer_2|knows_tactics_1|knows_shield_5|knows_surgery_1
# knight_skills_2 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_1|knows_tactics_1|knows_prisoner_management_2|knows_leadership_3|knows_engineer_6|knows_trainer_3|knows_tactics_2|knows_shield_6|knows_surgery_2
# knight_skills_3 = knows_riding_6|knows_ironflesh_5|knows_power_strike_5|knows_athletics_2|knows_tactics_2|knows_prisoner_management_2|knows_leadership_4|knows_engineer_7|knows_trainer_4|knows_tactics_3|knows_shield_7|knows_surgery_3
# knight_skills_4 = knows_riding_7|knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_tactics_3|knows_prisoner_management_3|knows_leadership_5|knows_engineer_8|knows_trainer_5|knows_tactics_4|knows_shield_8|knows_surgery_4
# knight_skills_5 = knows_riding_8|knows_ironflesh_7|knows_power_strike_7|knows_athletics_3|knows_tactics_4|knows_prisoner_management_3|knows_leadership_6|knows_engineer_9|knows_trainer_6|knows_tactics_5|knows_shield_9|knows_surgery_5
knight_skills_1 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_1|knows_prisoner_management_1|knows_leadership_2|knows_engineer_5|knows_trainer_2|knows_tactics_1|knows_shield_5|knows_surgery_1
knight_skills_2 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_1|knows_prisoner_management_2|knows_leadership_3|knows_engineer_6|knows_trainer_3|knows_tactics_2|knows_shield_6|knows_surgery_2
knight_skills_3 = knows_riding_6|knows_ironflesh_5|knows_power_strike_5|knows_athletics_2|knows_prisoner_management_2|knows_leadership_4|knows_engineer_7|knows_trainer_4|knows_tactics_3|knows_shield_7|knows_surgery_3
knight_skills_4 = knows_riding_7|knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_prisoner_management_3|knows_leadership_5|knows_engineer_8|knows_trainer_5|knows_tactics_4|knows_shield_8|knows_surgery_4
knight_skills_5 = knows_riding_8|knows_ironflesh_7|knows_power_strike_7|knows_athletics_3|knows_prisoner_management_3|knows_leadership_6|knows_engineer_9|knows_trainer_6|knows_tactics_5|knows_shield_9|knows_surgery_5
####### NEW v3.1-KOMKE END- 
knight_wp_1 = wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)| wp_archery(200)|wp_crossbow(200)|wp_throwing(200)
knight_wp_2 = wp_one_handed(260)|wp_two_handed(260)|wp_polearm(260)| wp_archery(240)|wp_crossbow(240)|wp_throwing(240)
knight_wp_3 = wp_one_handed(320)|wp_two_handed(320)|wp_polearm(320)| wp_archery(280)|wp_crossbow(280)|wp_throwing(280)
knight_wp_4 = wp_one_handed(380)|wp_two_handed(380)|wp_polearm(380)| wp_archery(320)|wp_crossbow(320)|wp_throwing(320)
knight_wp_5 = wp_one_handed(440)|wp_two_handed(440)|wp_polearm(440)| wp_archery(360)|wp_crossbow(360)|wp_throwing(360)



# skill/attrib definitions
foot_attrib_1 = str_6|agi_6|int_5|cha_4|level(4)                        # serf
foot_attrib_2 = str_9|agi_7|int_6|cha_5|level(7)                       # militia
foot_attrib_3 = str_12|agi_9|int_6|cha_6|level(12)                      # footman
foot_attrib_4 = str_15|agi_12|int_6|cha_6|level(18)                     # regular
foot_attrib_5 = str_18|agi_14|int_9|cha_9|level(24)                     # veteran
foot_attrib_elite = str_21 |agi_16|int_12|cha_12|level(28)              # sergeant

ranged_attrib_3     = str_9  |agi_6 |int_6  |cha_6  |level(12)                      # rangedman
ranged_attrib_4     = str_12 |agi_10 |int_6  |cha_6  |level(19)                     # regular
ranged_attrib_5     = str_14 |agi_14 |int_9  |cha_9  |level(24)                     # veteran
ranged_attrib_elite = str_16 |agi_18 |int_12 |cha_12 |level(28)     # sergeant

horse_attrib_1 = str_9|agi_9|int_6|cha_5|level(4)                     # noble recruit
horse_attrib_2 = str_12|agi_12|int_7|cha_8|level(8)                   # noble horsemen
horse_attrib_3 = str_15|agi_15|int_6|cha_7|level(14)                   # light cav
horse_attrib_4 = str_18|agi_16|int_6|cha_10|level(20)                   # medium cav
horse_attrib_5 = str_21|agi_18|int_9|cha_15|level(25)                   # heavy lancers
horse_attrib_elite = str_25 |agi_18|int_12|cha_20|level(30)   # knight

################# NEW v1.8
horse_attrib_elite_veteran = str_28 |agi_21|int_16|cha_24|level(36)   # veteran knight


######################################################### MERC ATTRIBUTES
foot_merc_attrib_1 = str_15|agi_9|int_6|cha_4|level(16)                        # regular
foot_merc_attrib_2 = str_18|agi_12|int_8|cha_6|level(22)                       # veteran
foot_merc_attrib_3 = str_21|agi_15|int_10|cha_8|level(28)                      # elite

ranged_merc_attrib_1 = str_12|agi_10|int_6|cha_4|level(16)                   # regular
ranged_merc_attrib_2 = str_14|agi_14|int_8|cha_6|level(22)                 # veteran
ranged_merc_attrib_3 = str_16|agi_18|int_10|cha_8|level(28)                  # elite

horse_merc_attrib_1 = str_16|agi_12|int_6|cha_5|level(16)                   # regular
horse_merc_attrib_2 = str_19|agi_14|int_8|cha_8|level(22)                # veteran
horse_merc_attrib_3 = str_22|agi_16|int_10|cha_12|level(28)                # elite




serf_skills               = knows_ironflesh_1|knows_weapon_master_1|knows_athletics_1|knows_power_strike_1|knows_shield_1|knows_inventory_management_10
serf_wp                   = wp_one_handed(80)|wp_two_handed(60)|wp_polearm(80)|wp_archery(80)|wp_crossbow(80)|wp_throwing(60)

militia_skills            = knows_ironflesh_2|knows_weapon_master_2|knows_athletics_1|knows_power_strike_2|knows_shield_1|knows_inventory_management_10
militia_wp                = wp_one_handed(80)|wp_two_handed(60)|wp_polearm(80)|wp_archery(80)|wp_crossbow(80)|wp_throwing(60)

####### NEW v2.6 
mamluk_slave_skills            = knows_ironflesh_2|knows_weapon_master_2|knows_athletics_1|knows_power_strike_2|knows_shield_1|knows_inventory_management_10
mamluk_slave_wp                = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(100)|wp_archery(80)|wp_crossbow(60)|wp_throwing(60)

mamluk_ghulam_skills            = knows_ironflesh_3|knows_weapon_master_3|knows_athletics_2|knows_power_strike_3|knows_shield_2|knows_inventory_management_10
mamluk_ghulam_wp                = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(160)|wp_archery(120)|wp_crossbow(60)|wp_throwing(80)




# foot melee soldiers
footman_skills            = knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_2|knows_shield_2|knows_power_throw_2|knows_inventory_management_10
footman_wp                = wp_one_handed(140)|wp_two_handed(100)|wp_polearm(140)|wp_archery(60)|wp_crossbow(60)|wp_throwing(80)


swords_regulars_skills    = knows_ironflesh_4|knows_power_strike_5|knows_athletics_2|knows_weapon_master_5|knows_shield_4|knows_power_throw_2|knows_inventory_management_10
swords_veteran_skills     = knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_weapon_master_7|knows_shield_5|knows_power_throw_2|knows_inventory_management_10
swords_sergeant_skills    = knows_ironflesh_8|knows_power_strike_7|knows_athletics_4|knows_weapon_master_8|knows_shield_6|knows_power_throw_2|knows_inventory_management_10
swords_regulars_wp        = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
swords_veteran_wp         = wp_one_handed(300)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
swords_sergeant_wp        = wp_one_handed(380)|wp_two_handed(60)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)


pikes_regulars_skills     = knows_ironflesh_4|knows_power_strike_6|knows_athletics_1|knows_weapon_master_5|knows_inventory_management_10
pikes_veteran_skills      = knows_ironflesh_5|knows_power_strike_7|knows_athletics_2|knows_weapon_master_7|knows_inventory_management_10
pikes_sergeant_skills     = knows_ironflesh_6|knows_power_strike_8|knows_athletics_3|knows_weapon_master_8|knows_inventory_management_10
pikes_regulars_wp         = wp_one_handed(60)|wp_two_handed(220)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
pikes_veteran_wp          = wp_one_handed(60)|wp_two_handed(300)|wp_polearm(300)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
pikes_sergeant_wp         = wp_one_handed(60)|wp_two_handed(380)|wp_polearm(380)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)


spears_regulars_skills     = knows_ironflesh_3|knows_power_strike_5|knows_athletics_4|knows_weapon_master_5|knows_shield_3|knows_power_throw_1|knows_inventory_management_10
spears_veteran_skills      = knows_ironflesh_4|knows_power_strike_6|knows_athletics_5|knows_weapon_master_7|knows_shield_4|knows_power_throw_2|knows_inventory_management_10
spears_sergeant_skills     = knows_ironflesh_5|knows_power_strike_7|knows_athletics_6|knows_weapon_master_8|knows_shield_5|knows_power_throw_2|knows_inventory_management_10
spears_regulars_wp         = wp_one_handed(160) |wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
spears_veteran_wp          = wp_one_handed(220) |wp_two_handed(60)|wp_polearm(300)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
spears_sergeant_wp         = wp_one_handed(280) |wp_two_handed(60)|wp_polearm(380)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)




# foot ranged soldiers
skirmisher_skills         = knows_athletics_1|knows_weapon_master_1|knows_power_throw_2|knows_power_draw_2|knows_power_strike_1|knows_inventory_management_10
skirmisher_wp             = wp_one_handed(80)|wp_two_handed(60)|wp_polearm(60)|wp_archery(120)|wp_crossbow(120)|wp_throwing(120)


crossbow_regulars_skills  = knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_weapon_master_5|knows_shield_2|knows_inventory_management_10
crossbow_veteran_skills   = knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_weapon_master_7|knows_shield_3|knows_inventory_management_10
crossbow_sergeant_skills  = knows_ironflesh_4|knows_power_strike_4|knows_athletics_3|knows_weapon_master_8|knows_shield_3|knows_inventory_management_10
crossbow_regulars_wp      = wp_one_handed(120)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(200)|wp_throwing(60)
crossbow_veteran_wp       = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(270)|wp_throwing(60)
crossbow_sergeant_wp      = wp_one_handed(200)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(340)|wp_throwing(60)


archer_regulars_skills    = knows_ironflesh_1|knows_power_strike_2|knows_athletics_2|knows_weapon_master_5|knows_shield_1|knows_power_draw_3|knows_inventory_management_10
archer_veteran_skills     = knows_ironflesh_2|knows_power_strike_3|knows_athletics_3|knows_weapon_master_7|knows_shield_2|knows_power_draw_4|knows_inventory_management_10
archer_sergeant_skills    = knows_ironflesh_3|knows_power_strike_3|knows_athletics_4|knows_weapon_master_8|knows_shield_2|knows_power_draw_5|knows_inventory_management_10
archer_regulars_wp        = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(60)|wp_archery(200)|wp_crossbow(60)|wp_throwing(60)
archer_veteran_wp         = wp_one_handed(140)|wp_two_handed(60)|wp_polearm(60)|wp_archery(280)|wp_crossbow(60)|wp_throwing(60)
archer_sergeant_wp        = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(60)|wp_archery(360)|wp_crossbow(60)|wp_throwing(60)


thrown_regulars_skills    = knows_ironflesh_2|knows_power_strike_3|knows_athletics_2|knows_power_throw_3|knows_shield_2|knows_weapon_master_2|knows_inventory_management_10
thrown_veteran_skills     = knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_power_throw_4|knows_shield_3|knows_weapon_master_4|knows_inventory_management_10
thrown_sergeant_skills    = knows_ironflesh_4|knows_power_strike_5|knows_athletics_4|knows_power_throw_5|knows_shield_4|knows_weapon_master_5|knows_inventory_management_10
thrown_regulars_wp        = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(180)
thrown_veteran_wp         = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(260)
thrown_sergeant_wp        = wp_one_handed(280)|wp_two_handed(60)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(340)



test_ps1            = knows_ironflesh_1|knows_power_strike_1|knows_power_draw_1|knows_power_throw_1|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps2            = knows_ironflesh_1|knows_power_strike_2|knows_power_draw_2|knows_power_throw_2|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps3            = knows_ironflesh_1|knows_power_strike_3|knows_power_draw_3|knows_power_throw_3|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps4            = knows_ironflesh_1|knows_power_strike_4|knows_power_draw_4|knows_power_throw_4|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps5            = knows_ironflesh_1|knows_power_strike_5|knows_power_draw_5|knows_power_throw_5|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps6            = knows_ironflesh_1|knows_power_strike_6|knows_power_draw_6|knows_power_throw_6|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps7            = knows_ironflesh_1|knows_power_strike_7|knows_power_draw_7|knows_power_throw_7|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps8            = knows_ironflesh_1|knows_power_strike_8|knows_power_draw_8|knows_power_throw_8|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps9            = knows_ironflesh_1|knows_power_strike_9|knows_power_draw_9|knows_power_throw_9|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4
test_ps10            = knows_ironflesh_1|knows_power_strike_10|knows_power_draw_10|knows_power_throw_10|knows_horse_archery_4|knows_athletics_2|knows_weapon_master_4

test_ps1_wp         = wp(130)
test_ps2_wp         = wp(160)
test_ps3_wp         = wp(190)
test_ps4_wp         = wp(220)
test_ps5_wp         = wp(250)
test_ps6_wp         = wp(280)
test_ps7_wp         = wp(310)
test_ps8_wp         = wp(340)
test_ps9_wp         = wp(370)
test_ps10_wp         = wp(400)

bandit_attrib             = str_12|agi_9|int_6|cha_6|level(15)
bandit_skills            = knows_ironflesh_1|knows_power_strike_2|knows_power_draw_2|knows_power_throw_2|knows_horse_archery_2|knows_athletics_2|knows_weapon_master_2|knows_shield_1|knows_inventory_management_10
bandit_wp                = wp_one_handed(90)|wp_two_handed(90)|wp_polearm(90)|wp_archery(90)|wp_crossbow(90)|wp_throwing(90)
# mounted soldiers

nbl_recruit_skills        = knows_ironflesh_1|knows_weapon_master_2|knows_riding_3|knows_horse_archery_2|knows_power_strike_4| knows_pathfinding_1|knows_shield_2|knows_inventory_management_10
nbl_recruit_wp            = wp_one_handed(140)|wp_two_handed(120)|wp_polearm(140)|wp_archery(100)|wp_crossbow(100)|wp_throwing(100)

nbl_horsemen_skills       = knows_ironflesh_1|knows_power_strike_5|knows_athletics_3|knows_weapon_master_3|knows_riding_4|knows_horse_archery_3| knows_pathfinding_1|knows_shield_2|knows_power_throw_1|knows_inventory_management_10
nbl_horsemen_wp           = wp_one_handed(140)|wp_two_handed(140)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(140)

nbl_skirmisher_skills     = knows_ironflesh_1|knows_power_strike_4|knows_athletics_2|knows_weapon_master_4|knows_riding_5|knows_pathfinding_1|knows_shield_3|knows_power_throw_2|knows_inventory_management_10
nbl_skirmisher_wp         = wp_one_handed(140)|wp_two_handed(140)|wp_polearm(150)|wp_archery(60)|wp_crossbow(60)|wp_throwing(180)

nbl_skirmisher2_skills    = knows_ironflesh_1|knows_power_strike_5|knows_athletics_1|knows_power_draw_1|knows_weapon_master_5|knows_riding_6| knows_pathfinding_1|knows_shield_4|knows_power_throw_3|knows_inventory_management_10
nbl_skirmisher2_wp        = wp_one_handed(200)|wp_two_handed(200)|wp_polearm(200)|wp_archery(60)|wp_crossbow(60)|wp_throwing(260)

nbl_lcv_skills            = knows_ironflesh_1|knows_power_strike_4|knows_athletics_2|knows_weapon_master_3|knows_riding_4|knows_pathfinding_1|knows_shield_3|knows_inventory_management_10
nbl_mcv_skills            = knows_ironflesh_2|knows_power_strike_5|knows_athletics_2|knows_weapon_master_5|knows_riding_5|knows_pathfinding_2|knows_shield_4|knows_inventory_management_10
nbl_hlan_skills           = knows_ironflesh_3|knows_power_strike_6|knows_athletics_2|knows_weapon_master_6|knows_riding_6|knows_pathfinding_2|knows_shield_5|knows_leadership_1
nbl_knight_skills         = knows_ironflesh_4|knows_power_strike_7|knows_athletics_2|knows_weapon_master_8|knows_riding_7|knows_pathfinding_3|knows_tactics_4|knows_prisoner_management_1|knows_leadership_3|knows_shield_6|knows_inventory_management_10

nbl_lcv_wp                = wp_one_handed(140)|wp_two_handed(140)|wp_polearm(140)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
nbl_mcv_wp                = wp_one_handed(220)|wp_two_handed(220)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
nbl_hlan_wp               = wp_one_handed(290)|wp_two_handed(290)|wp_polearm(290)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
nbl_knight_wp             = wp_one_handed(360)|wp_two_handed(360)|wp_polearm(360)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)


nbl_knight_veteran_skills         = knows_ironflesh_6|knows_power_strike_8|knows_athletics_3|knows_weapon_master_9|knows_riding_8|knows_tactics_6|knows_pathfinding_4|knows_prisoner_management_3|knows_leadership_5|knows_shield_7|knows_inventory_management_10
nbl_knight_veteran_wp             = wp_one_handed(420)|wp_two_handed(420)|wp_polearm(420)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)


cav_thrower_1_skills     = knows_weapon_master_3|knows_ironflesh_1|knows_riding_2|knows_power_throw_2|knows_power_strike_2|knows_shield_1|knows_inventory_management_10
cav_thrower_2_skills     = knows_weapon_master_5|knows_ironflesh_1|knows_riding_3|knows_power_throw_3|knows_power_strike_3|knows_shield_2|knows_inventory_management_10
cav_thrower_3_skills     = knows_weapon_master_6|knows_ironflesh_2|knows_riding_4|knows_power_throw_4|knows_power_strike_4|knows_shield_3|knows_inventory_management_10
cav_thrower_4_skills     = knows_weapon_master_8|knows_ironflesh_3|knows_riding_5|knows_power_throw_5|knows_power_strike_5|knows_shield_4|knows_inventory_management_10

cav_thrower_1_wp         = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(100)|wp_archery(60)|wp_crossbow(60)|wp_throwing(160)
cav_thrower_2_wp         = wp_one_handed(140)|wp_two_handed(60)|wp_polearm(140)|wp_archery(60)|wp_crossbow(60)|wp_throwing(220)
cav_thrower_3_wp         = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(180)|wp_archery(60)|wp_crossbow(60)|wp_throwing(280)
cav_thrower_4_wp         = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(340)


# mongol horse archers
cum_tribesman_skills      = knows_weapon_master_1|knows_ironflesh_1|knows_riding_2|knows_horse_archery_2|knows_power_throw_2|knows_power_draw_1|knows_inventory_management_10
cum_tribesman_wp          = wp_one_handed(35)|wp_two_handed(60)|wp_polearm(35)|wp_archery(120)|wp_crossbow(60)|wp_throwing(120)

cum_skirmisher_skills     = knows_weapon_master_3|knows_ironflesh_1|knows_riding_3|knows_horse_archery_2|knows_power_throw_3|knows_power_strike_1|knows_power_draw_2|knows_shield_1|knows_inventory_management_10
cum_horseman_skills       = knows_weapon_master_5|knows_ironflesh_1|knows_riding_4|knows_horse_archery_3|knows_power_throw_4|knows_power_strike_2|knows_power_draw_3|knows_shield_2|knows_inventory_management_10
cum_harcher_skills        = knows_weapon_master_7|knows_ironflesh_2|knows_riding_5|knows_horse_archery_4|knows_power_throw_5|knows_power_strike_3|knows_power_draw_4|knows_shield_2|knows_inventory_management_10
cum_vharcher_skills       = knows_weapon_master_9|knows_ironflesh_3|knows_riding_6|knows_horse_archery_5|knows_power_throw_6|knows_power_strike_4|knows_power_draw_5|knows_shield_3|knows_inventory_management_10
cum_lancer_skills         = knows_ironflesh_4|knows_athletics_2|knows_weapon_master_5|knows_riding_6|knows_power_strike_5|knows_shield_5|knows_inventory_management_10
cum_hlancer_skills        = knows_ironflesh_5|knows_athletics_3|knows_weapon_master_6|knows_riding_7|knows_power_strike_6|knows_shield_6|knows_inventory_management_10

cum_skirmisher_wp         = wp_one_handed(80)|wp_two_handed(60)|wp_polearm(80)|wp_archery(130)|wp_crossbow(60)|wp_throwing(150)
cum_horseman_wp           = wp_one_handed(140)|wp_two_handed(60)|wp_polearm(140)|wp_archery(180)|wp_crossbow(60)|wp_throwing(200)
cum_harcher_wp            = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(180)|wp_archery(250)|wp_crossbow(60)|wp_throwing(250)
cum_vharcher_wp           = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(320)|wp_crossbow(60)|wp_throwing(300)
cum_lancer_wp             = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
cum_hlancer_wp            = wp_one_handed(300)|wp_two_handed(60)|wp_polearm(300)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)



genoese_crossbowman_skills   = knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_6|knows_shield_4|knows_inventory_management_10
genoese_crossbowman_commander_skills   = knows_ironflesh_4|knows_power_strike_5|knows_athletics_4|knows_weapon_master_8|knows_shield_6|knows_inventory_management_10

genoese_crossbowman_wp    = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(60)|wp_archery(100)|wp_crossbow(280)|wp_throwing(60)
genoese_crossbowman_commander_wp    = wp_one_handed(240)|wp_two_handed(60)|wp_polearm(60)|wp_archery(100)|wp_crossbow(360)|wp_throwing(60)


varangian_skills     = knows_ironflesh_8| knows_power_strike_7|knows_athletics_6|knows_weapon_master_7|knows_pathfinding_1|knows_shield_6|knows_inventory_management_10
varangian_wp         = wp_one_handed(350)|wp_two_handed(350)|wp_polearm(350)|wp_archery(60)|wp_crossbow(60)|wp_throwing(250)


####################### LE INDOMITABLE MERCENARY
merc_meele_skills_1    = knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_weapon_master_3|knows_shield_3|knows_inventory_management_10
merc_meele_skills_2    = knows_ironflesh_5|knows_power_strike_5|knows_athletics_3|knows_weapon_master_5|knows_shield_4|knows_inventory_management_10
merc_meele_skills_3    = knows_ironflesh_7|knows_power_strike_7|knows_athletics_4|knows_weapon_master_6|knows_shield_5|knows_inventory_management_10

merc_meele_wp_1      = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_meele_wp_2      = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_meele_wp_3       = wp_one_handed(280)|wp_two_handed(60)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)


merc_meele_two_handed_skills_1  = knows_ironflesh_4|knows_power_strike_4|knows_athletics_2|knows_weapon_master_3|knows_inventory_management_10
merc_meele_two_handed_skills_2  = knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_weapon_master_5|knows_inventory_management_10
merc_meele_two_handed_skills_3  = knows_ironflesh_8|knows_power_strike_8|knows_athletics_4|knows_weapon_master_6|knows_inventory_management_10

merc_meele_two_handed_wp_1      = wp_one_handed(60)|wp_two_handed(160)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_meele_two_handed_wp_2      = wp_one_handed(60)|wp_two_handed(220)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_meele_two_handed_wp_3      = wp_one_handed(60)|wp_two_handed(280)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)



merc_archer_skills_1   = knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_4|knows_shield_2|knows_power_draw_3|knows_inventory_management_10
merc_archer_skills_2   = knows_ironflesh_4|knows_power_strike_3|knows_athletics_4|knows_weapon_master_5|knows_shield_3|knows_power_draw_4|knows_inventory_management_10
merc_archer_skills_3   = knows_ironflesh_5|knows_power_strike_4|knows_athletics_5|knows_weapon_master_6|knows_shield_3|knows_power_draw_5|knows_inventory_management_10

merc_archer_wp_1    = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(60)|wp_archery(160)|wp_crossbow(60)|wp_throwing(60)
merc_archer_wp_2    = wp_one_handed(130)|wp_two_handed(60)|wp_polearm(60)|wp_archery(220)|wp_crossbow(60)|wp_throwing(60)
merc_archer_wp_3    = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(60)|wp_archery(280)|wp_crossbow(60)|wp_throwing(60)


merc_crossbowman_skills_1   = knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_weapon_master_4|knows_shield_2|knows_inventory_management_10
merc_crossbowman_skills_2   = knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_5|knows_shield_3|knows_inventory_management_10
merc_crossbowman_skills_3   = knows_ironflesh_5|knows_power_strike_4|knows_athletics_4|knows_weapon_master_6|knows_shield_4|knows_inventory_management_10
     
merc_crossbowman_wp_1   = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(160)|wp_throwing(60)
merc_crossbowman_wp_2   = wp_one_handed(150)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(220)|wp_throwing(60)
merc_crossbowman_wp_3   = wp_one_handed(200)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(280)|wp_throwing(60)


merc_thrower_skills_1   = knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_weapon_master_4|knows_shield_2|knows_power_throw_3|knows_inventory_management_10
merc_thrower_skills_2   = knows_ironflesh_5|knows_power_strike_4|knows_athletics_3|knows_weapon_master_5|knows_shield_3|knows_power_throw_4|knows_inventory_management_10
merc_thrower_skills_3   = knows_ironflesh_7|knows_power_strike_5|knows_athletics_4|knows_weapon_master_6|knows_shield_4|knows_power_throw_5|knows_inventory_management_10
     
merc_thrower_wp_1   = wp_one_handed(130)|wp_two_handed(60)|wp_polearm(130)|wp_archery(60)|wp_crossbow(60)|wp_throwing(160)
merc_thrower_wp_2   = wp_one_handed(190)|wp_two_handed(60)|wp_polearm(190)|wp_archery(60)|wp_crossbow(60)|wp_throwing(220)
merc_thrower_wp_3   = wp_one_handed(250)|wp_two_handed(60)|wp_polearm(250)|wp_archery(60)|wp_crossbow(60)|wp_throwing(280)


merc_mounted_skills_1   = knows_ironflesh_2|knows_power_strike_3|knows_athletics_2|knows_weapon_master_4|knows_riding_3|knows_shield_2|knows_inventory_management_10
merc_mounted_skills_2   = knows_ironflesh_3|knows_power_strike_5|knows_athletics_3|knows_weapon_master_5|knows_riding_5|knows_shield_3|knows_inventory_management_10
merc_mounted_skills_3   = knows_ironflesh_5|knows_power_strike_6|knows_athletics_3|knows_weapon_master_6|knows_riding_6|knows_shield_4|knows_inventory_management_10

merc_mounted_wp_1   = wp_one_handed(160)|wp_two_handed(160)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_mounted_wp_2   = wp_one_handed(220)|wp_two_handed(220)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)
merc_mounted_wp_3   = wp_one_handed(280)|wp_two_handed(280)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)

light_infantry_skills_1     = knows_ironflesh_2|knows_power_strike_3|knows_athletics_4|knows_power_throw_4|knows_shield_3|knows_weapon_master_4|knows_inventory_management_10
light_infantry_skills_2     = knows_ironflesh_4|knows_power_strike_4|knows_athletics_5|knows_power_throw_4|knows_shield_4|knows_weapon_master_5|knows_inventory_management_10
light_infantry_skills_3     = knows_ironflesh_6|knows_power_strike_5|knows_athletics_6|knows_power_throw_5|knows_shield_5|knows_weapon_master_6|knows_inventory_management_10

light_infantry_wp_1         = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(160)|wp_archery(60)|wp_crossbow(60)|wp_throwing(160)
light_infantry_wp_2         = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(220)|wp_archery(60)|wp_crossbow(60)|wp_throwing(220)
light_infantry_wp_3         = wp_one_handed(280)|wp_two_handed(60)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(280)


gaelic_spearman_skills_1     = knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_weapon_master_4 |knows_shield_3|knows_power_throw_1|knows_inventory_management_10
gaelic_spearman_skills_2     = knows_ironflesh_6|knows_power_strike_6|knows_athletics_5|knows_weapon_master_5|knows_shield_4|knows_power_throw_2|knows_inventory_management_10
gaelic_spearman_skills_3     = knows_ironflesh_8|knows_power_strike_8|knows_athletics_6|knows_weapon_master_6|knows_shield_5|knows_power_throw_2|knows_inventory_management_10

gaelic_spearman_wp_1   = wp_one_handed(100)|wp_two_handed(60)|wp_polearm(210)|wp_archery(60)|wp_crossbow(60)|wp_throwing(40)
gaelic_spearman_wp_2   = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(280)|wp_archery(60)|wp_crossbow(60)|wp_throwing(50)
gaelic_spearman_wp_3   = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(350)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)



gaelic_axeman_skills_1   = knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_weapon_master_4 |knows_shield_3|knows_power_throw_1|knows_inventory_management_10
gaelic_axeman_skills_2   = knows_ironflesh_6|knows_power_strike_6|knows_athletics_5|knows_weapon_master_5|knows_shield_4|knows_power_throw_2|knows_inventory_management_10
gaelic_axeman_skills_3   = knows_ironflesh_8|knows_power_strike_8|knows_athletics_6|knows_weapon_master_6|knows_shield_5|knows_power_throw_2|knows_inventory_management_10

gaelic_axeman_wp_1   = wp_one_handed(60)|wp_two_handed(210)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(40)
gaelic_axeman_wp_2   = wp_one_handed(100)|wp_two_handed(280)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(50)
gaelic_axeman_wp_3   = wp_one_handed(140)|wp_two_handed(350)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(60)



welsh_archer_skills            = knows_athletics_3|knows_power_draw_5|knows_weapon_master_5|knows_ironflesh_2|knows_power_strike_2|knows_inventory_management_10
welsh_veteran_archer_skills    = knows_athletics_4|knows_power_draw_6|knows_weapon_master_6|knows_ironflesh_3|knows_power_strike_3|knows_inventory_management_10
welsh_elite_archer_skills      = knows_athletics_5|knows_power_draw_7|knows_weapon_master_7|knows_ironflesh_4|knows_power_strike_3|knows_inventory_management_10

welsh_archer_wp                = wp_one_handed(120)|wp_two_handed(60)|wp_polearm(60)|wp_archery(250)|wp_crossbow(60)|wp_throwing(60)
welsh_veteran_archer_wp        = wp_one_handed(150)|wp_two_handed(60)|wp_polearm(60)|wp_archery(300)|wp_crossbow(60)|wp_throwing(60)
welsh_elite_archer_wp          = wp_one_handed(180)|wp_two_handed(60)|wp_polearm(60)|wp_archery(350)|wp_crossbow(60)|wp_throwing(60)


merc_kern_skills            = knows_athletics_3|knows_weapon_master_4|knows_ironflesh_3|knows_power_strike_3|knows_inventory_management_10
merc_veteran_kern_skills    = knows_athletics_4|knows_weapon_master_5|knows_ironflesh_4|knows_power_strike_4|knows_inventory_management_10
merc_elite_kern_skills      = knows_athletics_5|knows_weapon_master_6|knows_ironflesh_6|knows_power_strike_6|knows_inventory_management_10

merc_kern_wp                = wp_one_handed(170)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(150)
merc_veteran_kern_wp        = wp_one_handed(250)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(200)
merc_elite_kern_wp          = wp_one_handed(330)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(60)|wp_throwing(250)


watchman_attrib            = str_12|agi_8|int_5|cha_6
watchman_skills            = knows_athletics_2|knows_weapon_master_3|knows_ironflesh_2|knows_power_strike_2|knows_inventory_management_10
watchman_wp                = wp_one_handed(120)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(120)|wp_throwing(60)



#################### CTT ATTRIBUTES
def_ctt_attrib = str_5|agi_5|int_4|cha_4
def_ctt_wp = wp_one_handed(0)|wp_two_handed(0)|wp_polearm(0)| wp_archery(0)|wp_crossbow(0)|wp_throwing(0)



#################### NEW KNIGHT ORDER TROOPS
knight_order_spearman_wp                = wp_one_handed(200)|wp_two_handed(60)|wp_polearm(240)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)
knight_order_spearman_serjeant_wp                = wp_one_handed(280)|wp_two_handed(60)|wp_polearm(320)|wp_archery(60)|wp_crossbow(60)|wp_throwing(100)

knight_order_spearman_skills            = knows_ironflesh_6|knows_power_strike_5|knows_athletics_4|knows_weapon_master_5|knows_shield_4|knows_power_throw_2|knows_inventory_management_10
knight_order_spearman_serjeant_skills            = knows_ironflesh_8|knows_power_strike_7|knows_athletics_5|knows_weapon_master_7|knows_shield_5|knows_power_throw_3|knows_inventory_management_10


knight_order_crossbow_wp                = wp_one_handed(160)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(240)|wp_throwing(100)
knight_order_crossbow_serjeant_wp                = wp_one_handed(220)|wp_two_handed(60)|wp_polearm(60)|wp_archery(60)|wp_crossbow(320)|wp_throwing(100)

knight_order_crossbow_skills            = knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_weapon_master_5|knows_shield_4|knows_inventory_management_10
knight_order_crossbow_serjeant_skills            = knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_weapon_master_7|knows_shield_5|knows_inventory_management_10



companion_noble = str_14|agi_10|int_6|cha_10|level(8)
companion_engineer = str_8|agi_8|int_10|cha_8|level(8)
companion_priest = str_6|agi_6|int_12|cha_10|level(8)
companion_trader = str_7|agi_6|int_10|cha_12|level(8)
companion_pathfinder = str_8|agi_12|int_8|cha_6|level(8)
companion_trainer = str_12|agi_8|int_12|cha_6|level(8)
companion_noble_wp = wp_one_handed(110) | wp_two_handed(110) | wp_polearm(110) | wp_archery(80) | wp_crossbow(80) | wp_throwing(80)
companion_engineer_wp = wp_one_handed(60) | wp_two_handed(35) | wp_polearm(35) | wp_archery(35) | wp_crossbow(100) | wp_throwing(35)
companion_priest_wp = wp_one_handed(35) | wp_two_handed(35) | wp_polearm(80) | wp_archery(35) | wp_crossbow(35) | wp_throwing(60)
companion_trader_wp = wp_one_handed(80) | wp_two_handed(35) | wp_polearm(35) | wp_archery(35) | wp_crossbow(60) | wp_throwing(35)
companion_pathfinder_wp = wp_one_handed(60) | wp_two_handed(35) | wp_polearm(35) | wp_archery(100) | wp_crossbow(100) | wp_throwing(100)
companion_trainer_wp = wp_one_handed(80) | wp_two_handed(80) | wp_polearm(80) | wp_archery(80) | wp_crossbow(80) | wp_throwing(80)
companion_noble_skills = knows_weapon_master_3|knows_power_strike_3|knows_riding_4|knows_leadership_3
companion_engineer_skills = knows_weapon_master_1|knows_power_strike_1|knows_engineer_4
companion_priest_skills = knows_first_aid_3|knows_surgery_3|knows_wound_treatment_3
companion_trader_skills = knows_weapon_master_1|knows_power_strike_1|knows_inventory_management_5|knows_trade_2|knows_athletics_3
companion_pathfinder_skills = knows_spotting_3|knows_tracking_2|knows_pathfinding_3|knows_power_draw_2|knows_power_throw_2
companion_trainer_skills = knows_weapon_master_3|knows_power_strike_2|knows_athletics_3|knows_trainer_3|knows_leadership_1




equipment_tier_1_foot = [
  itm_spiked_club,
  itm_scythe,
  itm_hatchet,
  itm_club,
  itm_pitch_fork,
  itm_pickaxe,

  itm_1257_hood,
  itm_woolen_cap,
  itm_leather_cap,
  itm_straw_hat,


  itm_peasant_tunic_a,
  itm_peasant_b,
  itm_peasant_c,
  itm_peasant_d,
  itm_tunic_with_green_cape,
  
  itm_peasant_f,
  itm_peasant_g,

  
  
  itm_woolen_hose,
  itm_wrapping_boots,
]


############# NEW v2.8 - Komke's edits
##KOMKE NOTES EQUIPMENT FOR VETERAN AND ELITE MERCENARIES
##-Veteran: tier 3 (70%) tier 4 (30%) Elite: tier 4 (70%) tier 5 (30%) Mounted Vets: coursers Elites: (30%) caparisoned hunters
##-helmets, boots and gloves included in gear
##-helmets t3=40 t4=50 t5=60
balt_vet_armors = [itm_thomas_padded_armour,itm_thomas_padded_armour,itm_thomas_padded_armour,itm_bulgar_warrior_b,itm_bulgar_warrior_b,itm_bulgar_warrior_b,itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c]

balt_elite_armors = [itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c,itm_balt_lamellar_vest_c,itm_bulgar_warrior_a,itm_bulgar_warrior_a]

balt_vet_gear = [itm_balt_footman_helmet,itm_balt_helmet_a,itm_leather_gloves,itm_leather_fur_boots]

balt_elite_gear = [itm_balt_spiked_helmet,itm_balt_helmet_b,itm_balt_helmet_c,itm_baltic_ponted_helmet,itm_curonian_helmet,itm_mail_mittens,itm_splinted_greaves_long]

balt_vet_horses = [itm_little_samogitian]

balt_elite_horses = [itm_little_samogitian]


mamluke_vet_armors = [itm_kau_arab_aketon_blue,itm_kau_arab_mail_shirt_d,itm_arabian_lamellar,itm_mamluk_jawshan_leather,itm_kau_arab_aketon_blue,itm_kau_arab_mail_shirt_d,itm_arabian_lamellar,itm_mamluk_jawshan_leather,itm_sarranid_cavalry_robe,itm_arabian_armor_b]

mamluke_elite_armors = [itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_mamluk_shirt_b,itm_mamluk_shirt_c,itm_mamluk_shirt_d,itm_mamluk_shirt_f]

mamluke_vet_gear = [itm_sarranid_mail_coif,itm_sarranid_horseman_helmet,itm_faris_helmet,itm_mamluk_helm_b,itm_mamluke_helm_ventail,itm_mamluke_helm_b,itm_leather_gloves,itm_mamluke_boots]

mamluke_elite_gear = [itm_arab_helmet_c,itm_arab_helmet_b,itm_arab_mail_coif,itm_mamluke_helm_b,itm_arab_helmet_d,itm_mail_mittens,itm_sarranid_boots_d_long]

mamluke_vet_horses = [itm_arabian_horse_a]

mamluke_elite_horses = [itm_arabian_horse_b]


maghreb_vet_armors = [itm_berber_tunic_b,itm_berber_tunic_b,itm_buff_leather,itm_buff_leather,itm_sarranid_cavalry_robe]

maghreb_elite_armors = [itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_sarranid_cavalry_robe,itm_arabian_armor_b,itm_berber_mail_b,itm_berber_mail_a]

maghreb_vet_gear = [itm_sarranid_mail_coif,itm_sarranid_horseman_helmet,itm_african_spangen,itm_megreb_spangen,itm_faris_helmet,itm_kufia_berber_black,itm_leather_gloves,itm_sarranid_boots_b_long]

maghreb_elite_gear = [itm_kufia_berber_black,itm_kufia_berber_black,itm_kufia_berber_black,itm_kufia_berber_black,itm_kufia_berber_black,itm_berber_white_turban,itm_berber_helmet_g,itm_mail_mittens,itm_sarranid_boots_d_long]

maghreb_vet_horses = [itm_arabian_horse_a]

maghreb_elite_horses = [itm_arabian_horse_b]


rus_vet_armors = [itm_kau_rus_d,itm_kau_rus_mail_shirt_b,itm_rus_leather_scale_b,itm_rus_padded,itm_kau_rus_d,itm_kau_rus_mail_shirt_b,itm_rus_leather_scale_b,itm_rus_padded,itm_kau_rus_c,itm_kau_rus_mail_shirt_a,itm_rus_mail_shirt_c]

rus_elite_armors = [itm_kau_rus_a,itm_kau_rus_c,itm_kau_rus_mail_shirt_a,itm_rus_mail_shirt_c,itm_rus_noble_mail,itm_rus_leather_scale,itm_kau_rus_noble_b,itm_kau_rus_lamellar_vest,itm_kau_rus_noble_a]

rus_vet_gear = [itm_rus_infantry_helmet,itm_rus_infantry_helmet,itm_rus_infantry_helmet,itm_rus_infantry_helmet,itm_rus_militia_helmet,itm_bulgar_helm_b,itm_leather_gloves,itm_rus_boots_b]

rus_elite_gear = [itm_rus_militia_helmet,itm_bulgar_helm_b,itm_rus_militia_helmet,itm_bulgar_helm_b,itm_rus_militia_helmet,itm_bulgar_helm_b,itm_rus_helm_a,itm_rus_helmet_b,itm_rus_helmet_a,itm_mail_mittens,itm_splinted_greaves_long]

rus_vet_horses = [itm_hunter,itm_horse_d,itm_horse_e]

rus_elite_horses = [itm_hunter,itm_horse_d,itm_horse_e,itm_hunter,itm_horse_d,itm_horse_e,itm_rnd_horse_01,itm_rnd_horse_10,itm_rnd_horse_20]


latin_vet_armors = [itm_iberian_leather_armour_a,itm_iberian_leather_armour_b,itm_iberian_leather_armour_c,itm_genoa_padded_a,itm_genoa_padded_c,itm_genoa_mail_c,itm_man_at_arms_b,itm_man_at_arms_a]

latin_elite_armors = [itm_man_at_arms_b,itm_man_at_arms_a,itm_man_at_arms_b,itm_man_at_arms_a,itm_man_at_arms_b,itm_man_at_arms_a,itm_mail_with_surcoat,itm_surcoat_over_mail]

latin_vet_gear = [itm_elm5,itm_elm2,itm_flat_kettle_hat,itm_footman_helmet,itm_kettle_cloth,itm_almogavar_helmet,itm_raf_spangen,itm_rhodok_kettle_hat_c,itm_norman_coif_a,itm_leather_gloves,itm_leather_boots]

latin_elite_gear = [itm_raf_spangen,itm_rhodok_kettle_hat_c,itm_norman_coif_a,itm_raf_spangen,itm_rhodok_kettle_hat_c,itm_norman_coif_a,itm_kau_urgell_helmet,itm_kau_pons_helmet,itm_kau_epyres_helmet,itm_kau_alego_helmet,itm_mail_mittens,itm_splinted_leather_greaves]

latin_vet_horses = [itm_hunter,itm_horse_d,itm_horse_e]

latin_elite_horses = [itm_hunter,itm_horse_d,itm_horse_e,itm_hunter,itm_horse_d,itm_horse_e,itm_rnd_horse_02,itm_rnd_horse_11,itm_rnd_horse_21]


balkan_vet_armors = [itm_byz_lamellar_a,itm_byz_lamellar_b,itm_byz_padded_leather,itm_byz_lamellar_a,itm_byz_lamellar_b,itm_byz_padded_leather,itm_byz_footman_a,itm_byz_footman_c,itm_byz_swordsman_3]

balkan_elite_armors = [itm_byz_footman_a,itm_byz_footman_c,itm_byz_swordsman_2,itm_byz_swordsman_3,itm_byz_swordsman_4,itm_byz_mail_a,itm_byz_mail_b]

balkan_vet_gear = [itm_byz_yoman_c,itm_byz_helmet_b,itm_byz_yoman_c,itm_byz_helmet_b,itm_byz_yoman_c,itm_byz_helmet_b,itm_byz_yoman_d,itm_byz_yoman_d,itm_leather_gloves,itm_byz_boots_c]

balkan_elite_gear = [itm_byz_yoman_d,itm_byz_yoman_d,itm_byz_yoman_d,itm_byz_yoman_d,itm_byz_yoman_d,itm_byz_yoman_d,itm_elm10,itm_byz_helmet_golden,itm_byz_helmet_a,itm_mail_mittens,itm_byzantine_greaves]

balkan_vet_horses = [itm_hunter,itm_horse_d,itm_horse_e]

balkan_elite_horses = [itm_hunter,itm_horse_d,itm_horse_e,itm_hunter,itm_horse_d,itm_horse_e,itm_rnd_horse_03,itm_rnd_horse_12,itm_rnd_horse_22]


scan_vet_armors = [itm_kau_mail_shirt_c,itm_bulgar_warrior_b,itm_kau_mail_shirt_c,itm_bulgar_warrior_b,itm_kau_mail_shirt_c,itm_bulgar_warrior_b,itm_kau_mail_b,itm_kau_mail_a]

scan_elite_armors = [itm_kau_mail_b,itm_kau_mail_a,itm_kau_mail_shirt_b,itm_scale_shirt_a,itm_man_at_arms_c,itm_man_at_arms_b,itm_veteran_surcoat_c,itm_veteran_surcoat_e]

scan_vet_gear = [itm_vik_spangen_b,itm_vik_norman_helmet_e,itm_vik_spangen_a,itm_vik_spangen_b,itm_vik_norman_helmet_e,itm_vik_spangen_a,itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_leather_gloves,itm_leather_fur_boots]

scan_elite_gear = [itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_vik_norman_helmet_b,itm_vik_norman_helmet_a,itm_vik_norman_helmet_c,itm_mail_mittens,itm_raf_mail_chausses]

scan_vet_horses = [itm_hunter,itm_horse_d,itm_horse_e]

scan_elite_horses = [itm_hunter,itm_horse_d,itm_horse_e,itm_hunter,itm_horse_d,itm_horse_e,itm_rnd_horse_04,itm_rnd_horse_13,itm_rnd_horse_23]


gaelic_vet_armors = [itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a]

gaelic_elite_armors = [itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_galloglass_mail,itm_galloglass_mail]

gaelic_vet_gear = [itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_leather_gloves,itm_highlander_boots_1]

gaelic_elite_gear = [itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettlehat_d,itm_kettlehat_e,itm_mail_mittens,itm_kau_mail_boots_dark_long]


welsh_vet_armors = [itm_welsh_archer,itm_welsh_archer,itm_welsh_archer,itm_welsh_archer,itm_welsh_archer,itm_welsh_archer,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a]

welsh_elite_armors = [itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_galloglass_mail,itm_galloglass_mail]

welsh_vet_gear = [itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_maciejowski_kettle_hat_a,itm_maciejowski_kettle_hat_b,itm_leather_gloves,itm_highlander_boots_1]

welsh_elite_gear = [itm_maciejowski_kettle_hat_a,itm_maciejowski_kettle_hat_b,itm_maciejowski_kettle_hat_a,itm_maciejowski_kettle_hat_b,itm_maciejowski_kettle_hat_a,itm_maciejowski_kettle_hat_b,itm_modded_helmet_kettle_mail_4,itm_modded_helmet_kettle_mail_5,itm_mail_mittens,itm_kau_mail_boots_dark_long]


kern_vet_armors = [itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_galloglass_padded,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a]

kern_elite_armors = [itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_gaelic_mail_shirt_b,itm_studden_leather_armour_a,itm_galloglass_mail,itm_galloglass_mail]

kern_vet_gear = [itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_gaelic_helmet_a,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_leather_gloves,itm_highlander_boots_1]

kern_elite_gear = [itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettle_cloth_cape,itm_kettle_cloth_cape_b,itm_kettlehat_d,itm_kettlehat_e,itm_mail_mittens,itm_kau_mail_boots_dark_long]
#############


#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x00000007cc051243178974d4e8aea6b500000000001e350a0000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x000000000000000336db6db6db6db6db00000000001db6db0000000000000000#0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x00000003c000000336db6db6db6db6db00000000001db6db0000000000000000#x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x000000078000000336db6db6db6db6db00000000001db6db0000000000000000#0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000b0000000336db6db6db6db6db00000000001db6db0000000000000000#0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000e4000000336db6db6db6db6db00000000001db6db0000000000000000#0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x000000000300104436db6db6db6db6db00000000001db6db0000000000000000#0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x000000038300104436db6db6db6db6db00000000001db6db0000000000000000#0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x000000070300104436db6db6db6db6db00000000001db6db0000000000000000#0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000b8300104436db6db6db6db6db00000000001db6db0000000000000000#0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000e8300104436db6db6db6db6db00000000001db6db0000000000000000#0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x000000001c00101027233536622ea85b00000000001f52de0000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

arab_face_1 = 0x00000000f908629137598db44be65b0e00000000001e445b0000000000000000
arab_face_2 = 0x0000000fff006248756563492595d95500000000001ea7730000000000000000

arab_face_3 = 0x000000001c0c31d134a391e76255c4dc00000000001e28ac0000000000000000
arab_face_4 = 0x0000000edc0c424034a391e76255c4dc00000000001e28ac0000000000000000

berber_face_1 = 0x000000003308f0006ee2883dd4f3f0d800000000001fbde50000000000000000
berber_face_2 = 0x00000000330900006ee28bbdd4f3f0d800000000001fbde50000000000000000

berber_face_3 = 0x00000000330900007ee23bbdd48760e800000000001d4de50000000000000000
berber_face_4 = 0x000000003308f0007ee23bbdd48760e800000000001d4de50000000000000000

morrocan_face_1 = 0x000000097f00e1463418776ad972335200000000001e36db0000000000000000
morrocan_face_2 = 0x000000097f00e1c7061013b4e36d934100000000001db3190000000000000000

euro_face_1 = 0x000000015c04200259156eb6e1b5a6eb00000000001f2e540000000000000000
euro_face_2 = 0x0000000a3f08300654856b4852a656db00000000001e451b0000000000000000

euro_face_3 = 0x00000000000c314458e36fd8d292379a00000000001d42ac0000000000000000
euro_face_4 = 0x0000000f7a0c300458e36fd8d292379a00000000001d42ac0000000000000000

latin_face_1 = 0x000000002a0430103b8d31c6ea2e3b4a00000000001f1d0b0000000000000000
latin_face_2 = 0x0000000dcc0c33ce372c89aa82512add00000000001eb9110000000000000000

mong_face_1 = 0x000000001a04830736db6db6db6db6db00000000001db6db0000000000000000
mong_face_2 = 0x000000073f00a38c36db6db6db6db6db00000000001db6db0000000000000000
#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield




