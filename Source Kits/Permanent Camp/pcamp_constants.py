from module_constants import *

# Cost to build a camp
pcamp_build_cost = 500

# Skill that controls camps
pcamp_build_skill = "skl_leadership"

# First level when you can build one; then increases 1 per level until hard cap
pcamp_build_skill_threshold = 5

# Max allowed distance to nearest center
pcamp_max_center_distance = 10

# Chance for a lord to escape from camp (default for party - 50)
pcamp_lord_escape_chance = 40

# Daily desertion chance of 1% per divisor*10% of debt relative to total wage; max 30/divisor%
pcamp_desertion_divisor = 4

# Percentage of player party's stats that directly carry over to camps
pcamp_player_party_size_percentage = 100
pcamp_player_prisoner_count_percentage = 0

# Number of additional troops per commander leadership level and charisma
pcamp_commander_leadership_size_bonus = 15
pcamp_commander_charisma_size_bonus = 3

# Number of prisoner slots per commander skill and num troops to gain 1 slot
pcamp_commander_prisoner_skill_bonus = 5
pcamp_troop_count_prisoner_divisor = 5

# Internal constants

spt_player_camp = 33 # arbitrary unique number

pcamp_chests_begin = "trp_player_camp_chest_1"
pcamp_chests_end = "trp_player_camp_chest_end"

slot_pcamp_camp_commander = slot_town_elder
slot_pcamp_camp_chest = slot_town_merchant
slot_pcamp_camp_initialized = slot_center_player_relation

slot_pcamp_chest_commander = 33 #slot_troop_guardian
slot_pcamp_chest_party = 60 #slot_troop_home
slot_pcamp_chest_center = 12 #slot_troop_cur_center
slot_pcamp_chest_city = 9 #slot_troop_present_at_event
slot_pcamp_chest_items = 7 #slot_troop_renown
slot_pcamp_chest_value = 11 #slot_troop_wealth
slot_pcamp_chest_sell_prisoners = 16 #slot_troop_player_order_state
