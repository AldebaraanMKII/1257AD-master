# -*- coding: utf-8 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *




hai = 1

#weight = 0.018 * length
#speed = 15665.5/(weight * length)

def get_w_weight(length):
  weight = 0.018 * length
  return weight

def get_axe_weight(length):
  weight = 0.025 * length
  return weight

def get_mace_weight(length):
  weight = 0.022 * length
  return weight

def get_1hmace_speed(length):
  weight = get_mace_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_1haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 100 - (weight*weight*weight)
  return (int) (round(speed))

def get_2haxe_speed(length):
  weight = get_axe_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_1hw_speed(length):
  weight = get_w_weight (length)
  speed = 103 - (weight*weight*weight)
  return (int) (round(speed))

def get_2hw_speed(length):
  weight = get_w_weight (length)
  speed = 99 - (weight*weight*weight)
  return (int) (round(speed))

def get_polew_speed(length):
  weight = get_w_weight (length)
  speed = 96 - (weight*weight*weight)
  return (int) (round(speed))

def get_w_price (length, weight, speed, damage_cut, damage_thrust):

  if damage_cut > damage_thrust:
    damage = damage_cut
  if damage_thrust > damage_cut:
    damage = damage_thrust
  price = (damage) * speed * length * length / (weight * 100)
  price = price * price
  price = price /10000000
  return (int) (round(price))

def get_barmour_price (weight, body_a, leg_a):
  #new_weight = weight ** 0.5
  price = 3*(body_a + leg_a)*(body_a + leg_a)/2#/new_weight
  if body_a < 30:
    price = price - price/3 
  if body_a >= 30 and body_a < 50:
    price = price - price/5
  if body_a < 35: #tom reduce - basic armor should be almost free
    price = price/3    
  return (int) (round(price))
 
# def tier_6_body_armor_price:
  # price = get_barmour_price(25, 72, 31)
  # return price
  
def get_footwear_price (armour):
  price = armour * 72
  if armour < 10:
    price = price - price/3
  return (int(round(price)))
  
def get_headgear_price (armour):
  price = armour ** 2
  if armour < 25:
    price = price - price/3
  return (int(round(price)))

def get_gloves_price (armour):
  price = 10 * armour ** 2
  return (int(round(price)))

def get_shield_price (armour, width, height):
  if height == 0:
    width = width/2
    area = 3.14 * width * width
  else:
    area = width * height
  price = area * area * area * armour * armour * armour
  price = price / 10000000000000
  price = price * 2
  
  if armour < 71:
    price = price / 3
  elif armour < 76:
    price = price /2
  elif armour > 80:
    price = price * 1.5
  return (int(round(price)))
  
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn|imodbit_champion
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

imodbits_horse_good = imodbit_spirited|imodbit_heavy|imodbit_champion
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

imodbits_missile_mon = imodbit_bent

warhorse_price = 3800
warhorse_hp = 120 #was 85
warhorse_armour = 45
warhorse_speed = 38 #was 38
warhorse_maneuver = 40
warhorse_charge = 38
warhorse_scale = 110
warhorse_abundance = 10
horse_hp = 65


warhorse_master_price = 8000
warhorse_master_hp = 140 #was 85
warhorse_master_armour = 50
warhorse_master_speed = 38 #was 38
warhorse_master_maneuver = 40
warhorse_master_charge = 45
warhorse_master_scale = 110
warhorse_master_abundance = 3


bastard_abundance = 100

shield_t1_res = 48
shield_t2_res = 55
shield_t3_res = 61
shield_t4_res = 67
shield_t5_res = 75


tier_0_body_armor_price = get_barmour_price(6,17,7)
tier_0_body_armor = weight(6)|abundance(50)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(1)

tier_1_body_armor_price = get_barmour_price(11,21,10)
tier_1_body_armor = weight(11)|abundance(50)|head_armor(0)|body_armor(21)|leg_armor(10)|difficulty(3)

tier_2_body_armor_price = get_barmour_price(14,26,12)
tier_2_body_armor = weight(14)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(12)|difficulty(5)

tier_3_body_armor_price = get_barmour_price(18,33,14)
tier_3_body_armor = weight(18)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(14)|difficulty(8)

tier_4_body_armor_price = get_barmour_price(21,41,17)
tier_4_body_armor = weight(21)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(17)|difficulty(9)

tier_5_body_armor_price = get_barmour_price(26,51,20)
tier_5_body_armor = weight(26)|abundance(60)|body_armor(51)|leg_armor(20)|difficulty(10)

tier_6_body_armor_price = get_barmour_price(31,64,24)
tier_6_body_armor = weight(31)|abundance(40)|body_armor(64)|leg_armor(24)|difficulty(12)

tier_6dot5_body_armor_price = get_barmour_price(33,72,30)
tier_6dot5_body_armor = weight(31)|abundance(10)|body_armor(72)|leg_armor(30)|difficulty(13)

tier_7_body_armor_price = get_barmour_price(36, 80, 29)
tier_7_body_armor = weight(36)|abundance(10)|head_armor(0)|body_armor(80)|leg_armor(29)|difficulty(14)

tier_arena_armor = weight(26)|abundance(60)|body_armor(51)|leg_armor(20)|difficulty(3)
#tier_6_body_armor_price = 2800

#crown, linen coif
head_armor_no_price = get_headgear_price(2)
head_armor_no = weight(0.5)|abundance(30)|head_armor(4)

#fur hats, head wrapings
head_armor_hat_price = get_headgear_price(8)
head_armor_hat = weight(0.5)|abundance(60)|head_armor(8)

#padded hat
head_armor_light_price = get_headgear_price(20)
head_armor_light = weight(1)|abundance(80)|head_armor(20)

#a peasant helmet
head_armor_average_price = get_headgear_price(40)
head_armor_average = weight(1.5)|abundance(100)|head_armor(40)

#a decent peasant helmet - kettlehat
head_armor_decent_price = get_headgear_price(50)
head_armor_decent = weight(1.8)|abundance(80)|head_armor(50)

#proper good helmet
head_armor_proper_price = get_headgear_price(60)
head_armor_proper = weight(2)|abundance(80)|head_armor(60)

#good helmet, covering face - slonim, old great helmets
head_armor_hevy_price = get_headgear_price(70)
head_armor_hevy = weight(2.5)|abundance(60)|head_armor(75)

####### NEW  
head_armor_varangian = weight(2.7)|abundance(45)|head_armor(80)

#bucket
head_armor_full_price = get_headgear_price(90)
head_armor_full = weight(3)|abundance(30)|head_armor(90)




# mongol_factions = [fac_kingdom_3, fac_kingdom_27]
# euro_factions = [fac_kingdom_5, fac_kingdom_6, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
# eastern_factions = [fac_kingdom_8, fac_kingdom_15, fac_kingdom_26, fac_kingdom_29, fac_kingdom_30]
# byzantine_factions = [ fac_kingdom_22 ]
# iberian_factions = [ fac_kingdom_16, fac_kingdom_17, fac_kingdom_18]
# italy_factions = [ fac_papacy, fac_kingdom_24, fac_kingdom_32, fac_kingdom_38, fac_kingdom_39, fac_kingdom_40, fac_kingdom_41]
# balt_factions = [ fac_kingdom_2, fac_kingdom_33 ]
# nordic_factions = [fac_kingdom_4, fac_kingdom_11, fac_kingdom_14]
# gaelic_factions = [fac_kingdom_12, fac_kingdom_13, fac_kingdom_37]
# berber_factions = [fac_kingdom_28, fac_kingdom_31]
# andalusian_factions = berber_factions + [fac_kingdom_20]
# mamluk_factions = [fac_kingdom_25]
# arab_factions = andalusian_factions + mamluk_factions
# latin_factions = iberian_factions + italy_factions
# all_euro_factions = euro_factions + [fac_kingdom_23] + iberian_factions + [fac_kingdom_26] #+ nordic_factions
##new
mongol_factions = [fac_culture_mongol]
euro_factions = [fac_culture_mazovian, fac_culture_teutonic,  fac_culture_western]
eastern_factions = [fac_culture_rus]
byzantine_factions = [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium]
iberian_factions = [fac_culture_iberian]
italy_factions = [fac_culture_italian, fac_culture_anatolian_christian]
balt_factions = [fac_culture_mazovian, fac_culture_baltic]
nordic_factions = [fac_culture_finnish, fac_culture_nordic]
gaelic_factions = [ fac_culture_welsh, fac_culture_gaelic, fac_culture_scotish]
berber_factions = [fac_culture_marinid, fac_culture_andalus]
andalusian_factions = [fac_culture_andalus]
mamluk_factions = [fac_culture_mamluke, fac_culture_anatolian]
arab_factions = [fac_culture_mamluke, fac_culture_anatolian, fac_culture_andalus, fac_culture_marinid]
latin_factions = iberian_factions + italy_factions
crusader_factions = [fac_kingdom_23, fac_culture_templar, fac_culture_hospitaller, fac_culture_teutonic, fac_culture_antioch, fac_culture_tripoli, fac_culture_ibelin, fac_culture_jerusalem]
all_euro_factions = euro_factions + latin_factions + nordic_factions + gaelic_factions  ####### NEW v3.3
anatolian_factions = [fac_culture_serbian, fac_culture_balkan, fac_culture_byzantium, fac_culture_anatolian]  ####### NEW v3.3 
## CC
missile_distance_trigger = [
  (ti_on_missile_hit, 
    [
      (store_trigger_param_1, ":shooter_agent"),
      
      #(eq, "$g_report_shot distance", 1),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (eq, ":shooter_agent", ":player_agent"),
        (agent_get_position, pos2, ":shooter_agent"),
        (agent_get_horse, ":horse_agent", ":player_agent"),
        (try_begin),
          (gt, ":horse_agent", -1),
          (position_move_z, pos2, 220),
        (else_try),
          (position_move_z, pos2, 150),
        (try_end),
        (get_distance_between_positions, ":distance", pos1, pos2),
        (store_div, reg61, ":distance", 100),
        (store_mod, reg62, ":distance", 100),
        (try_begin),
          (lt, reg62, 10),
          (str_store_string, s1, "@{reg61}.0{reg62}"),
        (else_try),
          (str_store_string, s1, "@{reg61}.{reg62}"),
        (try_end),
        (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC),
      (try_end),
    ])]
       










