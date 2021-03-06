from ID_items import *
from ID_quests import *
from ID_factions import *
from ID_troops import *


##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.
##############################################################

########################################################
##  ITEM SLOTS             #############################
########################################################

slot_item_is_checked               = 0
slot_item_food_bonus               = 1
slot_item_book_reading_progress    = 2
slot_item_book_read                = 3
slot_item_intelligence_requirement = 4

slot_item_amount_available         = 7

slot_item_urban_demand             = 11 #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
slot_item_rural_demand             = 12 #consumer demand in villages, measured in abstract units
slot_item_desert_demand            = 13 #consumer demand in villages, measured in abstract units

slot_item_production_slot          = 14 
slot_item_production_string        = 15 

slot_item_tied_to_good_price       = 20 #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc

slot_item_num_positions            = 22
slot_item_positions_begin          = 23 #reserve around 5 slots after this


slot_item_multiplayer_faction_price_multipliers_begin = 30 #reserve around 10 slots after this

slot_item_primary_raw_material            = 50
slot_item_is_raw_material_only_for      = 51
slot_item_input_number                  = 52 #ie, how many items of inputs consumed per run
slot_item_base_price                    = 53 #taken from module_items
#slot_item_production_site                = 54 #a string replaced with function - Armagan
slot_item_output_per_run                = 55 #number of items produced per run
slot_item_overhead_per_run              = 56 #labor and overhead per run
slot_item_secondary_raw_material        = 57 #in this case, the amount used is only one
slot_item_enterprise_building_cost      = 58 #enterprise building cost


slot_item_multiplayer_item_class   = 60 #temporary, can be moved to higher values
slot_item_multiplayer_availability_linked_list_begin = 61 #temporary, can be moved to higher values

slot_item_needs_two_hands    = 62
slot_item_length    = 63
slot_item_speed    = 64
slot_item_thrust_damage    = 65
slot_item_swing_damage    = 66

slot_item_head_armor    = slot_item_needs_two_hands
slot_item_body_armor    = slot_item_thrust_damage
slot_item_leg_armor    = slot_item_swing_damage

slot_item_horse_speed    = slot_item_needs_two_hands
slot_item_horse_armor    = slot_item_thrust_damage
slot_item_horse_charge    = slot_item_swing_damage
# # Autoloot end


##historical banners
slot_item_banner = 67

# item slots
slot_item_difficulty              = 68
slot_item_weight                  = slot_item_difficulty + 1
slot_armor_type                   = slot_item_difficulty + 2
slot_weapon_proficiency           = slot_item_difficulty + 3
slot_item_modifier_quality        = slot_item_difficulty + 4
slot_item_cant_on_horseback       = slot_item_difficulty + 5
slot_item_type_not_for_sell       = slot_item_difficulty + 6
slot_item_modifier_multiplier     = slot_item_difficulty + 7
slot_item_best_modifier           = slot_item_difficulty + 8
slot_item_flying_missile          = slot_item_difficulty + 9
slot_item_two_hand_one_hand       = slot_item_difficulty + 10
slot_item_head_armor              = slot_item_difficulty + 11
slot_item_body_armor              = slot_item_difficulty + 12
slot_item_leg_armor               = slot_item_difficulty + 13
slot_item_length                  = slot_item_difficulty + 14
slot_item_speed                   = slot_item_difficulty + 15

slot_item_food_portion            = slot_item_difficulty + 16
slot_item_durability              = slot_item_difficulty + 17

  #### Autoloot improved by rubik begin
slot_item_thrust_damage      = slot_item_head_armor
slot_item_swing_damage       = slot_item_body_armor

slot_item_horse_speed        = slot_item_head_armor
slot_item_horse_armor        = slot_item_body_armor
slot_item_horse_charge       = slot_item_length
  #### Autoloot improved by rubik end
########################################################
##  AGENT SLOTS            #############################
########################################################

slot_agent_target_entry_point     = 0
slot_agent_target_x_pos           = 1
slot_agent_target_y_pos           = 2
slot_agent_is_alive_before_retreat= 3
slot_agent_is_in_scripted_mode    = 4
slot_agent_is_not_reinforcement   = 5
slot_agent_tournament_point       = 6
slot_agent_arena_team_set         = 7
slot_agent_spawn_entry_point      = 8
slot_agent_target_prop_instance   = 9
slot_agent_map_overlay_id         = 10
slot_agent_target_entry_point     = 11
slot_agent_initial_ally_power     = 12
slot_agent_initial_enemy_power    = 13
slot_agent_enemy_threat           = 14
slot_agent_is_running_away        = 15
slot_agent_courage_score          = 16
slot_agent_is_respawn_as_bot      = 17
slot_agent_cur_animation          = 18
slot_agent_next_action_time       = 19
slot_agent_state                  = 20
slot_agent_in_duel_with           = 21
slot_agent_duel_start_time        = 22
slot_agent_kill_count             = 23 # rafi
slot_agent_crouching              = 24 # rafi

slot_agent_walker_occupation      = 25

slot_agent_spearwall = 26
slot_agent_x = 27
slot_agent_y = 28
slot_agent_z = 29
slot_agent_speed = 30

sp_agent_shield_bash_timer = 50
    
########################################################
##  FACTION SLOTS          #############################
########################################################
slot_faction_ai_state                   = 4
slot_faction_ai_object                  = 5
slot_faction_ai_rationale               = 6 #Currently unused, can be linked to strings generated from decision checklists


slot_faction_marshall                   = 8
slot_faction_ai_offensive_max_followers = 9

slot_faction_culture                    = 10
slot_faction_leader                     = 11

slot_faction_temp_slot                  = 12

##slot_faction_vassal_of            = 11
slot_faction_banner                     = 15

slot_faction_number_of_parties    = 20
slot_faction_state                = 21

slot_faction_adjective            = 22


slot_faction_player_alarm                 = 30
slot_faction_last_mercenary_offer_time     = 31
slot_faction_recognized_player            = 32

#overriding troop info for factions in quick start mode.
slot_faction_quick_battle_tier_1_infantry      = 41
slot_faction_quick_battle_tier_2_infantry      = 42
slot_faction_quick_battle_tier_1_archer        = 43
slot_faction_quick_battle_tier_2_archer        = 44
slot_faction_quick_battle_tier_1_cavalry       = 45
slot_faction_quick_battle_tier_2_cavalry       = 46

slot_faction_tier_1_troop         = 41
slot_faction_tier_2_troop         = 42
slot_faction_tier_3_troop         = 43
slot_faction_tier_4_troop         = 44
slot_faction_tier_5_troop         = 45

slot_faction_deserter_troop       = 48
slot_faction_guard_troop          = 49
slot_faction_messenger_troop      = 50
slot_faction_prison_guard_troop   = 51
slot_faction_castle_guard_troop   = 52

slot_faction_town_walker_male_troop      = 53
slot_faction_town_walker_female_troop    = 54
slot_faction_village_walker_male_troop   = 55
slot_faction_village_walker_female_troop = 56
slot_faction_town_spy_male_troop         = 57
slot_faction_town_spy_female_troop       = 58


slot_faction_has_rebellion_chance = 60

slot_faction_instability          = 61 #last time measured


#UNIMPLEMENTED FEATURE ISSUES
slot_faction_war_damage_inflicted_when_marshal_appointed = 62 #Probably deprecate
slot_faction_war_damage_suffered_when_marshal_appointed  = 63 #Probably deprecate

slot_faction_political_issue                              = 64 #Center or marshal appointment
slot_faction_political_issue_time                          = 65 #Now is used



#Rebellion changes
#slot_faction_rebellion_target                     = 65
#slot_faction_inactive_leader_location         = 66
#slot_faction_support_base                     = 67
#Rebellion changes



#slot_faction_deserter_party_template       = 62

slot_faction_reinforcements_a        = 77
slot_faction_reinforcements_b        = 78
slot_faction_reinforcements_c        = 79

slot_faction_num_armies              = 80
slot_faction_num_castles             = 81
slot_faction_num_towns               = 82

slot_faction_last_attacked_center    = 85
slot_faction_last_attacked_hours     = 86
slot_faction_last_safe_hours         = 87

slot_faction_num_routed_agents       = 90

#useful for competitive consumption
slot_faction_biggest_feast_score      = 91
slot_faction_biggest_feast_time       = 92
slot_faction_biggest_feast_host       = 93


#Faction AI states
slot_faction_last_feast_concluded       = 94 #Set when a feast starts -- this needs to be deprecated
slot_faction_last_feast_start_time      = 94 #this is a bit confusing


slot_faction_ai_last_offensive_time     = 95 #Set when an offensive concludes
slot_faction_last_offensive_concluded     = 95 #Set when an offensive concludes

slot_faction_ai_last_rest_time          = 96 #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
slot_faction_ai_current_state_started   = 97 #

slot_faction_ai_last_decisive_event     = 98 #capture a fortress or declaration of war

slot_faction_morale_of_player_troops    = 99


slot_faction_tier_1_town_troop    = 100
slot_faction_tier_1_castle_troop  = 101
slot_faction_religion = 102
slot_faction_peasant_rebellion_last = 103
slot_faction_recalculate_ai = 105
slot_faction_last_ai_calculation = 106

slot_faction_lord_count = 107
slot_faction_num_villages = 108

dplmc_slot_faction_policy_time                      = 110 
dplmc_slot_faction_centralization                   = 111  
dplmc_slot_faction_aristocracy                      = 112       
dplmc_slot_faction_serfdom                          = 113 
dplmc_slot_faction_quality                          = 114 
dplmc_slot_faction_patrol_time                = 115


############### NEW v2.1 - Faction statistics
kingdoms_begin_1 = fac_player_faction
kingdoms_end_1 = fac_papacy

kingdoms_begin_2 = fac_papacy
kingdoms_end_2 = fac_enhanced_kingdom_1

kingdoms_begin_3 = fac_enhanced_kingdom_1
kingdoms_end_3 = fac_enhanced_kingdom_21

kingdoms_begin_4 = fac_enhanced_kingdom_21
kingdoms_end_4 = fac_kingdoms_end

slot_faction_days_active = 120
slot_faction_battles_won = 121
slot_faction_battles_lost = 122

slot_faction_enemies_killed = 123
slot_faction_enemies_wounded = 124
slot_faction_enemies_captured = 125

slot_faction_troops_lost_killed = 126
slot_faction_troops_lost_wounded = 127
slot_faction_troops_lost_captured = 128

slot_faction_troops_deployed = 129

slot_faction_lords_lost_battle = 130
slot_faction_lords_lost_assassination = 131
slot_faction_lords_lost_execution = 132
slot_faction_lords_lost_defection = 133
####################################




################## NEW v2.1 - Civil War
enhanced_factions_begin = fac_enhanced_kingdom_1
enhanced_factions_end = fac_kingdoms_end

slot_faction_language = 135    ### used to set a civil war faction nomenclature

hero_titles_begin = "str_hero_titles_none"
hero_specdesc_begin = "str_hero_specdesc_none"

faction_language_finnish = 0 
faction_language_polish = faction_language_finnish + 1 
faction_language_serbian = faction_language_finnish + 2  
faction_language_welsh = faction_language_finnish + 3  
faction_language_german = faction_language_finnish + 4  
faction_language_bulgarian = faction_language_finnish + 5  
faction_language_rus = faction_language_finnish + 6  
faction_language_danish = faction_language_finnish + 7  
faction_language_norwegian = faction_language_finnish + 8  
faction_language_swedish = faction_language_finnish + 9  
faction_language_baltic = faction_language_finnish + 10 
faction_language_arab = faction_language_finnish + 11  
faction_language_greek = faction_language_finnish + 12  
faction_language_spanish = faction_language_finnish + 13  
faction_language_portuguese = faction_language_finnish + 14  
faction_language_italian = faction_language_finnish + 15  
faction_language_gaelic = faction_language_finnish + 16  
faction_language_armenian = faction_language_finnish + 17  
faction_language_turkish = faction_language_finnish + 18  
faction_language_scottish = faction_language_finnish + 19  
faction_language_english = faction_language_finnish + 20  
faction_language_french = faction_language_finnish + 21  
faction_language_hungarian = faction_language_finnish + 22  
faction_language_czech = faction_language_finnish + 23  
faction_language_mongol = faction_language_finnish + 24  
faction_language_mixed_euro = faction_language_finnish + 25  
faction_language_cuman = faction_language_finnish + 26  ########### NEW v3.3
faction_language_custom = faction_language_finnish + 27  
faction_language_end = faction_language_finnish + 28 

slot_faction_rebel_original_faction = 136

culture_titles_male_begin = "str_ee_culture_title_finnish"
# culture_titles_female_begin = "str_faction_title_female_player"

language_titles_male_begin = "str_ee_language_title_finnish"
# language_titles_female_begin = "str_faction_title_female_player"

faction_languages_begin = faction_language_finnish
faction_languages_end = faction_language_end

culture_titles_king_male_begin = "str_ee_culture_title_king_finnish"
# culture_titles_female_begin = "str_faction_title_king_female_player"

language_titles_king_male_begin = "str_ee_language_title_king_finnish"
# language_titles_female_begin = "str_faction_title_king_female_player"
####################################

########### NEW v3.3
slot_faction_heir_1 = 137
slot_faction_heir_2 = 138
slot_faction_heir_3 = 139
######################

########## NEW v3.0 - about 80 slots per item is enough
#diplomacy
slot_faction_truce_days_with_factions_begin             = 160
slot_faction_provocation_days_with_factions_begin         = 220
slot_faction_war_damage_inflicted_on_factions_begin     = 300 #tom 210
slot_faction_sum_advice_about_factions_begin             = 380 #tom 260  
##########

dplmc_slot_faction_attitude_begin             = 460 #Diplomacy 3.2 new line

#tom - for lance recruitment
merc_cost = 1000

#revolts -- notes for self
#type 1 -- minor revolt, aimed at negotiating change without changing the ruler
#type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
    #subtype -- pretender (keeps the same dynasty)
    #"mandate of heaven" -- same basic rules, but a different dynasty
    #alternate/religious
    #alternate/political
#type 3 -- separatist revolt
    # reGonalist/dynastic (based around an alternate ruling house
    # regionalist/republican
    # messianic (ie, Canudos)
    
########################################################
##  PARTY SLOTS            #############################
########################################################
slot_party_type                = 0  #spt_caravan, spt_town, spt_castle

slot_party_retreat_flag        = 2
slot_party_ignore_player_until = 3
slot_party_ai_state            = 4
slot_party_ai_object           = 5
slot_party_ai_rationale        = 6 #Currently unused, but can be used to save a string explaining the lord's thinking

#slot_town_belongs_to_kingdom   = 6
slot_town_lord                 = 7
slot_party_ai_substate         = 8
slot_town_claimed_by_player    = 9

slot_cattle_driven_by_player = slot_town_lord #hack

slot_town_center        = 10
slot_town_castle        = 11
slot_town_prison        = 12
slot_town_tavern        = 13
slot_town_store         = 14
slot_town_arena         = 16
slot_town_alley         = 17
slot_town_walls         = 18
slot_center_culture     = 19

slot_town_tavernkeeper  = 20
slot_town_weaponsmith   = 21
slot_town_armorer       = 22
slot_town_merchant      = 23
slot_town_horse_merchant= 24
slot_town_elder         = 25
slot_center_player_relation = 26

slot_center_siege_with_belfry = 27
slot_center_last_taken_by_troop = 28

# party will follow this party if set:
slot_party_commander_party = 30 #default -1   #Deprecate
slot_party_following_player    = 31
slot_party_follow_player_until_time = 32
slot_party_dont_follow_player_until_time = 33

slot_village_raided_by        = 34
slot_village_state            = 35 #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
slot_village_raid_progress    = 36
slot_village_recover_progress = 37
slot_village_smoke_added      = 38

slot_village_infested_by_bandits   = 39

slot_center_last_visited_by_lord   = 41

slot_center_last_player_alarm_hour = 42

slot_village_player_can_not_steal_cattle = 46

slot_center_accumulated_rents      = 47 #collected automatically by NPC lords
slot_center_accumulated_tariffs    = 48 #collected automatically by NPC lords
slot_town_wealth        = 49 #total amount of accumulated wealth in the center, pays for the garrison
slot_town_prosperity    = 50 #affects the amount of wealth generated
slot_town_player_odds   = 51


slot_party_last_toll_paid_hours = 52
slot_party_food_store           = 53 #used for sieges
slot_center_is_besieged_by      = 54 #used for sieges
slot_center_last_spotted_enemy  = 55

slot_party_cached_strength        = 56
slot_party_nearby_friend_strength = 57
slot_party_nearby_enemy_strength  = 58
slot_party_follower_strength      = 59

slot_town_reinforcement_party_template = 60
slot_center_original_faction           = 61
slot_center_ex_faction                 = 62

slot_party_follow_me                   = 63
slot_center_siege_begin_hours          = 64 #used for sieges
slot_center_siege_hardness             = 65

slot_center_sortie_strength            = 66
slot_center_sortie_enemy_strength      = 67

slot_party_last_in_combat              = 68 #used for AI
slot_party_last_in_home_center         = 69 #used for AI
slot_party_leader_last_courted         = 70 #used for AI
slot_party_last_in_any_center          = 71 #used for AI



slot_castle_exterior    = slot_town_center

#slot_town_rebellion_contact   = 76
#trs_not_yet_approached  = 0
#trs_approached_before   = 1
#trs_approached_recently = 2

argument_none         = 0
argument_claim        = 1 #deprecate for legal
argument_legal        = 1

argument_ruler        = 2 #deprecate for commons
argument_commons      = 2

argument_benefit      = 3 #deprecate for reward
argument_reward       = 3 

argument_victory      = 4
argument_lords        = 5
argument_rivalries    = 6 #new - needs to be added

slot_town_village_product = 76

slot_town_rebellion_readiness = 77
#(readiness can be a negative number if the rebellion has been defeated)

slot_town_arena_melee_mission_tpl = 78
slot_town_arena_torny_mission_tpl = 79
slot_town_arena_melee_1_num_teams = 80
slot_town_arena_melee_1_team_size = 81
slot_town_arena_melee_2_num_teams = 82
slot_town_arena_melee_2_team_size = 83
slot_town_arena_melee_3_num_teams = 84
slot_town_arena_melee_3_team_size = 85
slot_town_arena_melee_cur_tier    = 86
##slot_town_arena_template      = 87

slot_center_npc_volunteer_troop_type   = 88
slot_center_npc_volunteer_troop_amount = 89
slot_center_mercenary_troop_type  = 90
slot_center_mercenary_troop_amount= 91
slot_center_volunteer_troop_type  = 92
slot_center_volunteer_troop_amount= 93

#slot_center_companion_candidate   = 94
slot_center_ransom_broker         = 95
slot_center_tavern_traveler       = 96
slot_center_traveler_info_faction = 97
slot_center_tavern_bookseller     = 98
slot_center_tavern_minstrel       = 99

num_party_loot_slots    = 5
slot_party_next_looted_item_slot  = 109
slot_party_looted_item_1          = 110
slot_party_looted_item_2          = 111
slot_party_looted_item_3          = 112
slot_party_looted_item_4          = 113
slot_party_looted_item_5          = 114
slot_party_looted_item_1_modifier = 115
slot_party_looted_item_2_modifier = 116
slot_party_looted_item_3_modifier = 117
slot_party_looted_item_4_modifier = 118
slot_party_looted_item_5_modifier = 119

slot_village_bound_center         = 120
slot_village_market_town          = 121
slot_village_farmer_party         = 122
slot_party_home_center            = 123 #Only use with caravans and villagers

slot_center_current_improvement   = 124
slot_center_improvement_end_hour  = 125

slot_party_last_traded_center     = 126 


#tom lets change this shit!
slot_center_has_manor            = 130 #village
slot_center_has_fish_pond        = 131 #village
slot_center_has_watch_tower      = 132 #village
slot_center_has_school           = 133 #village
slot_center_has_messenger_post   = 134 #town, castle, village
slot_center_has_prisoner_tower   = 135 #town, castle

village_improvements_begin = slot_center_has_manor
village_improvements_end          = 135

walled_center_improvements_begin = slot_center_has_messenger_post
walled_center_improvements_end               = 136

# slot_center_has_manor            = 401 #village
# slot_center_has_fish_pond        = 402 #village #It's actualy a mill...Grannary
# slot_center_has_watch_tower      = 403 #village Walls
# slot_center_has_school           = 404 #village Slave quarters
# slot_center_has_temple           = 405 #village
# slot_center_has_weaponsmith      = 406 #village
# slot_center_has_armorsmith       = 407 #village
# slot_center_has_stable           = 408 #village
# slot_center_has_market           = 409 #village
# slot_center_has_tavern           = 409 #village
# slot_center_has_messenger_post   = 411 #town, castle, village
# slot_center_has_prisoner_tower   = 412 #town, castle

# village_improvements_begin = slot_center_has_manor
# village_improvements_end          = 412

# walled_center_improvements_begin = slot_center_has_messenger_post
# walled_center_improvements_end               = 413

slot_center_player_enterprise                       = 137 #noted with the item produced
slot_center_player_enterprise_production_order    = 138
slot_center_player_enterprise_consumption_order   = 139 #not used
slot_center_player_enterprise_days_until_complete = 139 #Used instead

slot_center_player_enterprise_balance             = 140 #not used
slot_center_player_enterprise_input_price         = 141 #not used
slot_center_player_enterprise_output_price        = 142 #not used



slot_center_has_bandits                        = 155
slot_town_has_tournament                       = 156
slot_town_tournament_max_teams                 = 157
slot_town_tournament_max_team_size             = 158

slot_center_faction_when_oath_renounced        = 159

slot_center_walker_0_troop                   = 160
slot_center_walker_1_troop                   = 161
slot_center_walker_2_troop                   = 162
slot_center_walker_3_troop                   = 163
slot_center_walker_4_troop                   = 164
slot_center_walker_5_troop                   = 165
slot_center_walker_6_troop                   = 166
slot_center_walker_7_troop                   = 167
slot_center_walker_8_troop                   = 168
slot_center_walker_9_troop                   = 169

slot_center_walker_0_dna                     = 170
slot_center_walker_1_dna                     = 171
slot_center_walker_2_dna                     = 172
slot_center_walker_3_dna                     = 173
slot_center_walker_4_dna                     = 174
slot_center_walker_5_dna                     = 175
slot_center_walker_6_dna                     = 176
slot_center_walker_7_dna                     = 177
slot_center_walker_8_dna                     = 178
slot_center_walker_9_dna                     = 179

slot_center_walker_0_type                    = 180
slot_center_walker_1_type                    = 181
slot_center_walker_2_type                    = 182
slot_center_walker_3_type                    = 183
slot_center_walker_4_type                    = 184
slot_center_walker_5_type                    = 185
slot_center_walker_6_type                    = 186
slot_center_walker_7_type                    = 187
slot_center_walker_8_type                    = 188
slot_center_walker_9_type                    = 189

slot_town_trade_route_1           = 190
slot_town_trade_route_2           = 191
slot_town_trade_route_3           = 192
slot_town_trade_route_4           = 193
slot_town_trade_route_5           = 194
slot_town_trade_route_6           = 195
slot_town_trade_route_7           = 196
slot_town_trade_route_8           = 197
slot_town_trade_route_9           = 198
slot_town_trade_route_10          = 199
slot_town_trade_route_11          = 200
slot_town_trade_route_12          = 201
slot_town_trade_route_13          = 202
slot_town_trade_route_14          = 203
slot_town_trade_route_15          = 204
slot_town_trade_routes_begin = slot_town_trade_route_1
slot_town_trade_routes_end = slot_town_trade_route_15 + 1


num_trade_goods = itm_siege_supply - itm_spice
slot_town_trade_good_productions_begin       = 500 #a harmless number, until it can be deprecated

#These affect production but in some cases also demand, so it is perhaps easier to itemize them than to have separate 

slot_village_number_of_cattle            = 205
slot_center_head_cattle         = 205 #dried meat, cheese, hides, butter
slot_center_head_sheep            = 206 #sausages, wool
slot_center_head_horses             = 207 #horses can be a trade item used in tracking ,but which are never offered for sale

slot_center_acres_pasture       = 208
slot_production_sources_begin = 209
slot_center_acres_grain            = 209 #grain
slot_center_acres_olives        = 210 #nothing for now
slot_center_acres_vineyard        = 211 #fruit
slot_center_acres_flax          = 212 #flax - can be used for sailcloth
slot_center_acres_dates            = 213 #dates

slot_center_fishing_fleet        = 214 #smoked fish
slot_center_salt_pans            = 215 #salt

slot_center_apiaries               = 216 #honey
slot_center_silk_farms            = 217 #silk
slot_center_kirmiz_farms        = 218 #dyes

slot_center_iron_deposits       = 219 #iron
slot_center_fur_traps            = 220 #furs
#timber
#pitch

slot_center_mills                = 221 #bread
slot_center_breweries            = 222 #ale
slot_center_wine_presses        = 223 #wine
slot_center_olive_presses        = 224 #oil

slot_center_linen_looms            = 225 #linen
slot_center_silk_looms          = 226 #velvet
slot_center_wool_looms          = 227 #wool cloth

slot_center_pottery_kilns        = 228 #pottery
slot_center_smithies            = 229 #tools
slot_center_tanneries            = 230 #leatherwork
slot_center_shipyards            = 231 #naval stores - uses timber, pitch, and linen

slot_center_household_gardens   = 232 #cabbages
slot_production_sources_end = 233

slot_center_last_besieger = 235  ######## NEW v3.0 - to store last faction that sieged the center

#all spice comes overland to Tulga
#all dyes come by sea to Jelkala

#chicken and pork are perishable and non-tradeable, and based on grain production
#timber and pitch if we ever have a shipbuilding industry
#limestone and timber for mortar, if we allow building

slot_town_last_nearby_fire_time                         = 240

#slot_town_trade_good_prices_begin            = slot_town_trade_good_productions_begin + num_trade_goods + 1
slot_party_following_orders_of_troop        = 244
slot_party_orders_type                        = 245
slot_party_orders_object                    = 246
slot_party_orders_time                        = 247

slot_party_temp_slot_1                        = 248 #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
slot_party_under_player_suggestion            = 249 #move this up a bit
slot_party_battle_preparation = 250
slot_center_has_fortifications_1 = 251
slot_center_has_fortifications_2 = 252

slot_center_tavern_troop = 253  ######## NEW v3.0

######## NEW v3.1 - moved those slots to here and changed their ID. They were causing script errors with town_merc_respawn script
#manor - party slots
village_slot_manor = 255 #village saves its bound manor
manor_slot_unique = 256 #check if the manor is players development one
#mongol camps - party slots
slot_mongol_camp = 257 #village saves its mongolian camp id
slot_mongol_camp_status = manor_slot_unique # mongolian camp status
slot_mongol_town = village_slot_manor #for the camp, saves its bound town
#feudal recruitment system
slot_feudal_lances = slot_center_volunteer_troop_amount #lances
#slot_garrison_cap = 700 #seems free. 0 - for very low.
slot_garrison_control = 258 #seems free. 0 - for very low.
slot_lances_cap = 259 #for future special buildings, relation bonuses
slot_regional_mercs = 260
slot_regional_mercs_number = 261
slot_regional_party_template = 262
slot_spec_mercs1 = 263
slot_spec_mercs1_number = 264
slot_spec_mercs1_party_template = 265
slot_spec_mercs2 = 266
slot_spec_mercs2_number = 267
slot_spec_mercs2_party_template = 268
slot_regional_mercs_number_npc = 269
slot_spec_mercs1_number_npc = 270
slot_spec_mercs2_number_npc = 271
slot_number_commoner = 272
slot_number_nobles = 273
slot_number_troops_pending = 274
slot_recruitment_type = 275
slot_player_crusade_fief = 276

slot_town_arena_master = 277
slot_town_seneschal = 278

##########################################################
# Test : Tavern Recruitment Begin ########################
##########################################################
slot_town_mercs = 279
merc_parties_begin = "p_town_merc_1"
merc_parties_end = "p_town_merc_end"
#########################################################
# Test : Tavern Recruitment End #########################
#########################################################


############### NEW v2.1 - diplomacy stuff
##diplomacy start+ additional center slots
dplmc_slot_center_ex_lord                     = 280 #The last lord (not counting those who willingly transferred it)
dplmc_slot_center_original_lord               = dplmc_slot_center_ex_lord + 1 #The original lord
dplmc_slot_center_last_transfer_time          = dplmc_slot_center_ex_lord + 2 #The last time it was captured
dplmc_slot_center_last_attacked_time          = dplmc_slot_center_ex_lord + 3 #Last attempted raid or siege
dplmc_slot_center_last_attacker               = dplmc_slot_center_ex_lord + 4 #Last lord who attempted to raid or siege
####################################


################## NEW v2.1 - player village donations
slot_center_donations = 285
####################################

dplmc_slot_party_mission_diplomacy            = 286
dplmc_slot_center_taxation                    = 287

##diplomacy begin 
# recruiter kit begin
dplmc_slot_party_recruiter_needed_recruits = 288           # Amount of recruits the employer ordered.
dplmc_slot_party_recruiter_origin = 289                    # Walled center from where the recruiter was hired.
dplmc_slot_village_reserved_by_recruiter = 290            # This prevents recruiters from going to villages targeted by other recruiters.
dplmc_slot_party_recruiter_needed_recruits_faction = 291   # Alkhadias Master, you forgot this one from the PM you sent me :D
dplmc_slot_party_recruiter_recruitment_type = 292

dplmc_spt_recruiter     = 22
# recruiter kit end





############ NEW v3.2 - slots 295 to 309 is reserved for floris bank

slot_town_trade_good_prices_begin             = 310

slot_center_last_reconnoitered_by_faction_time                 = 380
#slot_center_last_reconnoitered_by_faction_cached_strength     = 360
#slot_center_last_reconnoitered_by_faction_friend_strength     = 370




#slot_party_type values
##spt_caravan            = 1
spt_castle             = 2
spt_town               = 3
spt_village            = 4
spt_forager            = 5
spt_war_party          = 6
spt_patrol             = 7
##spt_messenger          = 8
##spt_raider             = 9
spt_scout              = 10
spt_kingdom_caravan    = 11
spt_prisoner_train     = 12
spt_kingdom_hero_party = 13
##spt_merchant_caravan   = 14
spt_village_farmer     = 15
spt_ship               = 16
spt_cattle_herd        = 17
spt_bandit_lair       = 18
spt_mercenary_company  = 19
#spt_deserter           = 20


kingdom_party_types_begin = spt_kingdom_caravan
kingdom_party_types_end = spt_kingdom_hero_party + 1

#slot_faction_state values
sfs_active                     = 0
sfs_defeated                   = 1
sfs_inactive                   = 2
sfs_inactive_rebellion         = 3
sfs_beginning_rebellion        = 4


#slot_faction_ai_state values
sfai_default                            = 0 #also defending
sfai_gathering_army                     = 1
sfai_attacking_center                   = 2
sfai_raiding_village                    = 3
sfai_attacking_enemy_army               = 4
sfai_attacking_enemies_around_center = 5
sfai_feast                               = 6 #can be feast, wedding, or major tournament
#Social events are a generic aristocratic gathering. Tournaments take place if they are in a town, and hunts take place if they are at a castle.
#Weddings will take place at social events between betrothed couples if they have been engaged for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present


#Rebellion system changes begin
sfai_nascent_rebellion          = 7
#Rebellion system changes end

#slot_party_ai_state values
spai_undefined                  = -1
spai_besieging_center           = 1
spai_patrolling_around_center   = 4
spai_raiding_around_center      = 5
##spai_raiding_village            = 6
spai_holding_center             = 7
##spai_helping_town_against_siege = 9
spai_engaging_army              = 10
spai_accompanying_army          = 11
spai_screening_army             = 12
spai_trading_with_town          = 13
spai_retreating_to_center       = 14
##spai_trading_within_kingdom     = 15
spai_visiting_village           = 16 #same thing, I think. Recruiting differs from holding because NPC parties don't actually enter villages

#slot_village_state values
svs_normal                      = 0
svs_being_raided                = 1
svs_looted                      = 2
svs_recovering                  = 3
svs_deserted                    = 4
svs_under_siege                 = 5

#$g_player_icon_state values
pis_normal                      = 0
pis_camping                     = 1
pis_ship                        = 2


########################################################
##  SCENE SLOTS            #############################
########################################################
slot_scene_visited              = 0
slot_scene_belfry_props_begin   = 10



########################################################
##  TROOP SLOTS            #############################
########################################################
#slot_troop_role         = 0  # 10=Kingdom Lord

slot_troop_occupation          = 2  # 0 = free, 1 = merchant
#slot_troop_duty               = 3  # Kingdom duty, 0 = free
#slot_troop_homage_type         = 45
#homage_mercenary =             = 1 #Player is on a temporary contract
#homage_official =              = 2 #Player has a royal appointment
#homage_feudal   =              = 3 #


slot_troop_state               = 3  
slot_troop_last_talk_time      = 4
slot_troop_met                 = 5 #i also use this for the courtship state -- may become cumbersome
slot_troop_courtship_state     = 5 #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

slot_troop_party_template      = 6
#slot_troop_kingdom_rank        = 7

slot_troop_renown              = 7

##slot_troop_is_prisoner         = 8  # important for heroes only
slot_troop_prisoner_of_party   = 8  # important for heroes only
#slot_troop_is_player_companion = 9  # important for heroes only:::USE  slot_troop_occupation = slto_player_companion

slot_troop_present_at_event    = 9

slot_troop_leaded_party         = 10 # important for kingdom heroes only
slot_troop_wealth               = 11 # important for kingdom heroes only
slot_troop_cur_center           = 12 # important for royal family members only (non-kingdom heroes)

slot_troop_banner_scene_prop    = 13 # important for kingdom heroes and player only

slot_troop_original_faction     = 14 # for pretenders
#slot_troop_loyalty              = 15 #deprecated - this is now derived from other figures
slot_troop_player_order_state   = 16 #Deprecated
slot_troop_player_order_object  = 17 #Deprecated

#troop_player order state are all deprecated in favor of party_order_state. This has two reasons -- 1) to reset AI if the party is eliminated, and 2) to allow the player at a later date to give orders to leaderless parties, if we want that


#Post 0907 changes begin
slot_troop_age                 =  18
slot_troop_age_appearance      =  19

#Post 0907 changes end

slot_troop_does_not_give_quest = 20
slot_troop_player_debt         = 21
slot_troop_player_relation     = 22
#slot_troop_player_favor        = 23
slot_troop_last_quest          = 24
slot_troop_last_quest_betrayed = 25
slot_troop_last_persuasion_time= 26
slot_troop_last_comment_time   = 27
slot_troop_spawned_before      = 28

#Post 0907 changes begin
slot_troop_last_comment_slot   = 29
#Post 0907 changes end

slot_troop_spouse              = 30
slot_troop_father              = 31
slot_troop_mother              = 32
slot_troop_guardian            = 33 #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
slot_troop_betrothed           = 34 #Obviously superseded once slot_troop_spouse is filled
#other relations are derived from one's parents 
#slot_troop_daughter            = 33
#slot_troop_son                 = 34
#slot_troop_sibling             = 35
slot_troop_love_interest_1     = 35 #each unmarried lord has three love interests
slot_troop_love_interest_2     = 36
slot_troop_love_interest_3     = 37
slot_troop_love_interests_end  = 38
#ways to court -- discuss a book, commission/compose a poem, present a gift, recount your exploits, fulfil a specific quest, appear at a tournament
#preferences for women - (conventional - father's friends)
slot_lady_no_messages                          = 37
slot_lady_last_suitor                          = 38
slot_lord_granted_courtship_permission      = 38

slot_troop_betrothal_time                   = 39 #used in scheduling the wedding

slot_troop_trainer_met                       = 30
slot_troop_trainer_waiting_for_result        = 31
slot_troop_trainer_training_fight_won        = 32
slot_troop_trainer_num_opponents_to_beat     = 33
slot_troop_trainer_training_system_explained = 34
slot_troop_trainer_opponent_troop            = 35
slot_troop_trainer_training_difficulty       = 36
slot_troop_trainer_training_fight_won        = 37


slot_lady_used_tournament                    = 40


slot_troop_current_rumor       = 45
slot_troop_temp_slot           = 46
slot_troop_promised_fief       = 47

slot_troop_set_decision_seed       = 48 #Does not change
slot_troop_temp_decision_seed      = 49 #Resets at recalculate_ai
slot_troop_recruitment_random      = 50 #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
#Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
#The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
#The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue

slot_troop_intrigue_impatience = 51
#recruitment changes end

#slot_troop_honorable          = 50
#slot_troop_merciful          = 51
slot_lord_reputation_type               = 52
slot_lord_recruitment_argument        = 53 #the last argument proposed by the player to the lord
slot_lord_recruitment_candidate       = 54 #the last candidate proposed by the player to the lord

slot_troop_change_to_faction          = 55

#slot_troop_readiness_to_join_army     = 57 #possibly deprecate
#slot_troop_readiness_to_follow_orders = 58 #possibly deprecate

# NPC-related constants

#NPC companion changes begin
slot_troop_first_encountered          = 59
slot_troop_home                       = 60

slot_troop_morality_state       = 61
tms_no_problem         = 0
tms_acknowledged       = 1
tms_dismissed          = 2

slot_troop_morality_type = 62
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

slot_troop_morality_value = 63

slot_troop_2ary_morality_type  = 64
slot_troop_2ary_morality_state = 65
slot_troop_2ary_morality_value = 66

slot_troop_town_with_contacts  = 67
slot_troop_town_contact_type   = 68 #1 are nobles, 2 are commons

slot_troop_morality_penalties =  69 ### accumulated grievances from morality conflicts


slot_troop_personalityclash_object     = 71
#(0 - they have no problem, 1 - they have a problem)
slot_troop_personalityclash_state    = 72 #1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
pclash_penalty_to_self  = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both  = 3
#(a string)
slot_troop_personalityclash2_object   = 73
slot_troop_personalityclash2_state    = 74

slot_troop_personalitymatch_object   =  75
slot_troop_personalitymatch_state   =  76

slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash
slot_troop_personalityclash_penalties = 77 ### accumulated grievances from personality clash

slot_troop_home_speech_delivered = 78 #only for companions
slot_troop_discussed_rebellion   = 78 #only for pretenders

#courtship slots
slot_lady_courtship_heroic_recited         = 74
slot_lady_courtship_allegoric_recited     = 75
slot_lady_courtship_comic_recited         = 76
slot_lady_courtship_mystic_recited         = 77
slot_lady_courtship_tragic_recited         = 78



#NPC history slots
slot_troop_met_previously        = 80
slot_troop_turned_down_twice     = 81
slot_troop_playerparty_history   = 82

pp_history_scattered         = 1
pp_history_dismissed         = 2
pp_history_quit              = 3
pp_history_indeterminate     = 4

slot_troop_playerparty_history_string   = 83
slot_troop_return_renown        = 84

slot_troop_custom_banner_bg_color_1      = 85
slot_troop_custom_banner_bg_color_2      = 86
slot_troop_custom_banner_charge_color_1  = 87
slot_troop_custom_banner_charge_color_2  = 88
slot_troop_custom_banner_charge_color_3  = 89
slot_troop_custom_banner_charge_color_4  = 90
slot_troop_custom_banner_bg_type         = 91
slot_troop_custom_banner_charge_type_1   = 92
slot_troop_custom_banner_charge_type_2   = 93
slot_troop_custom_banner_charge_type_3   = 94
slot_troop_custom_banner_charge_type_4   = 95
slot_troop_custom_banner_flag_type       = 96
slot_troop_custom_banner_num_charges     = 97
slot_troop_custom_banner_positioning     = 98
slot_troop_custom_banner_map_flag_type   = 99

#conversation strings -- must be in this order!
slot_troop_intro                         = 101
slot_troop_intro_response_1             = 102
slot_troop_intro_response_2             = 103
slot_troop_backstory_a                     = 104
slot_troop_backstory_b                     = 105
slot_troop_backstory_c                     = 106
slot_troop_backstory_delayed             = 107
slot_troop_backstory_response_1         = 108
slot_troop_backstory_response_2         = 109
slot_troop_signup                       = 110
slot_troop_signup_2                     = 111
slot_troop_signup_response_1             = 112
slot_troop_signup_response_2             = 113
slot_troop_mentions_payment             = 114 #Not actually used
slot_troop_payment_response             = 115 #Not actually used
slot_troop_morality_speech               = 116
slot_troop_2ary_morality_speech         = 117
slot_troop_personalityclash_speech         = 118
slot_troop_personalityclash_speech_b     = 119
slot_troop_personalityclash2_speech     = 120
slot_troop_personalityclash2_speech_b     = 121
slot_troop_personalitymatch_speech         = 122
slot_troop_personalitymatch_speech_b     = 123
slot_troop_retirement_speech             = 124
slot_troop_rehire_speech                 = 125
slot_troop_home_intro                   = 126
slot_troop_home_description                = 127
slot_troop_home_description_2             = 128
slot_troop_home_recap                     = 129
slot_troop_honorific                       = 130
slot_troop_kingsupport_string_1            = 131
slot_troop_kingsupport_string_2            = 132
slot_troop_kingsupport_string_2a        = 133
slot_troop_kingsupport_string_2b        = 134
slot_troop_kingsupport_string_3            = 135
slot_troop_kingsupport_objection_string    = 136
slot_troop_intel_gathering_string        = 137
slot_troop_fief_acceptance_string        = 138
slot_troop_woman_to_woman_string        = 139
slot_troop_turn_against_string            = 140

slot_troop_strings_end                     = 141

slot_troop_payment_request                 = 141

#141, support base removed, slot now available

slot_troop_kingsupport_state            = 142
slot_troop_kingsupport_argument            = 143
slot_troop_kingsupport_opponent            = 144
slot_troop_kingsupport_objection_state  = 145 #0, default, 1, needs to voice, 2, has voiced

slot_troop_days_on_mission                = 151
slot_troop_current_mission                = 152
slot_troop_mission_object               = 153

# call horse
slot_troop_horse = 176
# end call horse


npc_mission_kingsupport                    = 1
npc_mission_gather_intel                = 2
npc_mission_peace_request               = 3
npc_mission_pledge_vassal               = 4
npc_mission_seek_recognition            = 5
npc_mission_test_waters                 = 6
npc_mission_non_aggression              = 7
npc_mission_rejoin_when_possible        = 8
npc_mission_pope_crown                    = 9

#Number of routed agents after battle ends.
slot_troop_player_routed_agents                 = 146
slot_troop_ally_routed_agents                   = 147
slot_troop_enemy_routed_agents                  = 148

#Special quest slots
slot_troop_mission_participation        = 149
mp_unaware                              = 0 
mp_stay_out                             = 1 
mp_prison_break_fight                   = 2 
mp_prison_break_stand_back              = 3 
mp_prison_break_escaped                 = 4 
mp_prison_break_caught                  = 5 

#Below are some constants to expand the political system a bit. The idea is to make quarrels less random, but instead make them serve a rational purpose -- as a disincentive to lords to seek 

slot_troop_controversy                     = 150 #Determines whether or not a troop is likely to receive fief or marshalship
slot_troop_recent_offense_type                = 151 #failure to join army, failure to support colleague
slot_troop_recent_offense_object           = 152 #to whom it happened
slot_troop_recent_offense_time             = 153
slot_troop_stance_on_faction_issue         = 154 #when it happened

tro_failed_to_join_army                    = 1
tro_failed_to_support_colleague            = 2

#CONTROVERSY
#This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
#It is intended to be a limiting factor for players and lords in their ability to intrigue against each other. It represents the embroilment of a lord in internal factional disputes. In contemporary media English, a lord with high "controversy" would be described as "embattled."
#The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
#It is a key political concept because it provides incentive for much of the political activity. For example, Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants. So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.




slot_troop_will_join_prison_break      = 155

dplmc_slot_troop_mission_diplomacy            = 156
dplmc_slot_troop_mission_diplomacy2           = 157
dplmc_slot_troop_political_stance             = 158

slot_troop_traveling = 159


#troop slots:
manor_troop_slot_tax = 160 #in gold or in goods the troop pays taxes
manor_troop_slot_good = 161  #good that the troop sels or pays taxes in
npc_slot_naked = 162

#feudal lance troop slot
slot_troop_culture = manor_troop_slot_tax #301


################### NEW v2.1 - TROOP KILL/WOUNDED COUNT
slot_troop_kill_count = 163
slot_troop_wounded_count = 164
#########################################################


################## NEW v2.1 - Lord generation system
slot_troop_cur_culture = 165

slot_troop_is_alive = 166

slot_troop_original_name = 167
slot_troop_original_surname = 168
slot_troop_original_title_numeral = 169
slot_troop_original_origin = 170
slot_troop_original_title3 = 171
slot_troop_original_title4 = 172
slot_troop_original_title5 = 173

slot_troop_death_cause = 174  ######## 1 = battle, 2 = executed, 3 = assassinated

slot_troop_death_battle_killer = 175

slot_troop_death_execution_killer = 176
slot_troop_death_execution_method = 177   ####### 1 = beheading, 2 = hanging, 3 = burning, 4 = hanged, strung, and quartered

slot_troop_death_assassination_method = 178   ####### 1 = poisoned, 2 = stabbed, 3 = strangled, 4 = ambushed
slot_troop_death_assassination_found_perpetrators = 179

slot_troop_face_type = 180 ####### 1 = european, 2 = arab/turk, 3 = asian/mongol

slot_troop_type_num_in_town = 181

slot_troop_face_key = 182 ########### NEW v3.3 

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################

# These are troops slots
slot_upgrade_armor = 185
slot_upgrade_horse = slot_upgrade_armor + 1

slot_upgrade_wpn_0 = slot_upgrade_armor + 2
slot_upgrade_wpn_1 = slot_upgrade_armor + 3
slot_upgrade_wpn_2 = slot_upgrade_armor + 4
slot_upgrade_wpn_3 = slot_upgrade_armor + 5

## CC
slot_upgrade_wpn_set_sel = slot_upgrade_armor + 6
slot_upgrade_wpn_0_set_2 = slot_upgrade_armor + 7
slot_upgrade_wpn_1_set_2 = slot_upgrade_armor + 8
slot_upgrade_wpn_2_set_2 = slot_upgrade_armor + 9
slot_upgrade_wpn_3_set_2 = slot_upgrade_armor + 10

offset_of_two_sets_slot = slot_upgrade_wpn_0_set_2 - slot_upgrade_wpn_0
## CC
###################################################################################
# End Autoloot
###################################################################################
## CC


#### Moved this here
troop_slots_reserved_for_relations_start        = 200 #this is based on id_troops, and might change

slot_troop_relations_begin                = 200 #this creates an array for relations between troops
                                            #Right now, lords start at 165 and run to around 290, including pretenders
##########################################





########################################################
##  PLAYER SLOTS           #############################
########################################################

slot_player_spawned_this_round                 = 0
slot_player_last_rounds_used_item_earnings     = 1
slot_player_selected_item_indices_begin        = 2
slot_player_selected_item_indices_end          = 11
slot_player_cur_selected_item_indices_begin    = slot_player_selected_item_indices_end
slot_player_cur_selected_item_indices_end      = slot_player_selected_item_indices_end + 9
slot_player_join_time                          = 21
slot_player_button_index                       = 22 #used for presentations
slot_player_can_answer_poll                    = 23
slot_player_first_spawn                        = 24
slot_player_spawned_at_siege_round             = 25
slot_player_poll_disabled_until_time           = 26
slot_player_total_equipment_value              = 27
slot_player_last_team_select_time              = 28
slot_player_death_pos_x                        = 29
slot_player_death_pos_y                        = 30
slot_player_death_pos_z                        = 31
slot_player_damage_given_to_target_1           = 32 #used only in destroy mod
slot_player_damage_given_to_target_2           = 33 #used only in destroy mod
slot_player_last_bot_count                     = 34
slot_player_bot_type_1_wanted                  = 35
slot_player_bot_type_2_wanted                  = 36
slot_player_bot_type_3_wanted                  = 37
slot_player_bot_type_4_wanted                  = 38
slot_player_spawn_count                        = 39


########################################################
##  TEAM SLOTS             #############################
########################################################

slot_team_flag_situation                       = 0




#Rebellion changes end
# character backgrounds
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6
cb_priest = 7

cb2_page = 0
cb2_apprentice = 1
cb2_urchin  = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4

cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss    = 2
cb4_wanderlust =  3
cb4_disown  = 5
cb4_greed  = 6

#NPC system changes end
#Encounter types
enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid   = 2
enctype_player_sally = 3


### Troop occupations slot_troop_occupation
##slto_merchant           = 1
slto_inactive           = 0 #for companions at the beginning of the game

slto_kingdom_hero       = 2

slto_player_companion   = 5 #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady       = 6 #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
slto_kingdom_seneschal  = 7
slto_robber_knight      = 8
slto_inactive_pretender = 9


stl_unassigned          = -1
stl_reserved_for_player = -2
stl_rejected_by_player  = -3

#NPC changes begin
slto_retirement      = 11
#slto_retirement_medium    = 12
#slto_retirement_short     = 13
#NPC changes end

########################################################
##  QUEST SLOTS            #############################
########################################################

slot_quest_target_center            = 1
slot_quest_target_troop             = 2
slot_quest_target_faction           = 3
slot_quest_object_troop             = 4
##slot_quest_target_troop_is_prisoner = 5
slot_quest_giver_troop              = 6
slot_quest_object_center            = 7
slot_quest_target_party             = 8
slot_quest_target_party_template    = 9
slot_quest_target_amount            = 10
slot_quest_current_state            = 11
slot_quest_giver_center             = 12
slot_quest_target_dna               = 13
slot_quest_target_item              = 14
slot_quest_object_faction           = 15

slot_quest_target_state             = 16
slot_quest_object_state             = 17

slot_quest_convince_value           = 19
slot_quest_importance               = 20
slot_quest_xp_reward                = 21
slot_quest_gold_reward              = 22
slot_quest_expiration_days          = 23
slot_quest_dont_give_again_period   = 24
slot_quest_dont_give_again_remaining_days = 25

slot_quest_failure_consequence      = 26
slot_quest_temp_slot                  = 27

########################################################
##  PARTY TEMPLATE SLOTS   #############################
########################################################

# Ryan BEGIN
slot_party_template_num_killed   = 1

slot_party_template_lair_type             = 3
slot_party_template_lair_party            = 4
slot_party_template_lair_spawnpoint     = 5


# Ryan END


########################################################
##  SCENE PROP SLOTS       #############################
########################################################

scene_prop_open_or_close_slot       = 1
scene_prop_smoke_effect_done        = 2
scene_prop_number_of_agents_pushing = 3 #for belfries only
scene_prop_next_entry_point_id      = 4 #for belfries only
scene_prop_belfry_platform_moved    = 5 #for belfries only
scene_prop_slots_end                = 6

########################################################
rel_enemy   = 0
rel_neutral = 1
rel_ally    = 2


#Talk contexts
tc_town_talk                  = 0
tc_court_talk                   = 1
tc_party_encounter            = 2
tc_castle_gate                = 3
tc_siege_commander            = 4
tc_join_battle_ally           = 5
tc_join_battle_enemy          = 6
tc_castle_commander           = 7
tc_hero_freed                 = 8
tc_hero_defeated              = 9
tc_entering_center_quest_talk = 10
tc_back_alley                 = 11
tc_siege_won_seneschal        = 12
tc_ally_thanks                = 13
tc_tavern_talk                = 14
tc_rebel_thanks               = 15
tc_garden                      = 16
tc_courtship                  = 16
tc_after_duel                  = 17
tc_prison_break               = 18
tc_escape                     = 19
tc_give_center_to_fief        = 20
tc_merchants_house            = 21
tc_mongol_camp                  = 22 #tom
tc_camp_talk                    = 23

tc_freelancer_talk                    = 24   ######### NEW v2.1 - talk to freelancer lord

#Troop Commentaries begin
#Log entry types
#civilian
logent_village_raided            = 1
logent_village_extorted          = 2
logent_caravan_accosted          = 3 #in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked        = 3 #in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants           = 4 

logent_party_traded              = 5

logent_castle_captured_by_player              = 10
logent_lord_defeated_by_player                = 11
logent_lord_captured_by_player                = 12
logent_lord_defeated_but_let_go_by_player     = 13
logent_player_defeated_by_lord                = 14
logent_player_retreated_from_lord             = 15
logent_player_retreated_from_lord_cowardly    = 16
logent_lord_helped_by_player                  = 17
logent_player_participated_in_siege           = 18
logent_player_participated_in_major_battle    = 19
logent_castle_given_to_lord_by_player         = 20

logent_pledged_allegiance          = 21
logent_liege_grants_fief_to_vassal = 22


logent_renounced_allegiance      = 23 

logent_player_claims_throne_1                           = 24
logent_player_claims_throne_2                           = 25


logent_troop_feels_cheated_by_troop_over_land           = 26
logent_ruler_intervenes_in_quarrel                     = 27
logent_lords_quarrel_over_land                         = 28
logent_lords_quarrel_over_insult                       = 29
logent_marshal_vs_lord_quarrel                         = 30
logent_lords_quarrel_over_woman                        = 31

logent_lord_protests_marshall_appointment               = 32
logent_lord_blames_defeat                                  = 33

logent_player_suggestion_succeeded                       = 35
logent_player_suggestion_failed                           = 36

logent_liege_promises_fief_to_vassal                   = 37

logent_lord_insults_lord_for_cowardice                 = 38
logent_lord_insults_lord_for_rashness                  = 39
logent_lord_insults_lord_for_abandonment               = 40
logent_lord_insults_lord_for_indecision                = 41
logent_lord_insults_lord_for_cruelty                   = 42
logent_lord_insults_lord_for_dishonor                  = 43




logent_game_start                           = 45 
logent_poem_composed                        = 46 ##Not added
logent_tournament_distinguished             = 47 ##Not added
logent_tournament_won                       = 48 ##Not added

#logent courtship - lady is always actor, suitor is always troop object
logent_lady_favors_suitor                   = 51 #basically for gossip
logent_lady_betrothed_to_suitor_by_choice   = 52
logent_lady_betrothed_to_suitor_by_family   = 53
logent_lady_rejects_suitor                  = 54
logent_lady_father_rejects_suitor           = 55
logent_lady_marries_lord                    = 56
logent_lady_elopes_with_lord                = 57
logent_lady_rejected_by_suitor              = 58
logent_lady_betrothed_to_suitor_by_pressure = 59 #mostly for gossip

logent_lady_and_suitor_break_engagement        = 60
logent_lady_marries_suitor                    = 61

logent_lord_holds_lady_hostages             = 62
logent_challenger_defeats_lord_in_duel      = 63
logent_challenger_loses_to_lord_in_duel     = 64

logent_player_stole_cattles_from_village    = 66

logent_party_spots_wanted_bandits           = 70


logent_border_incident_cattle_stolen          = 72 #possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted         = 73 #possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed       = 74 #possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated    = 75 #possibly add this to rumors for non-player faction

#These supplement caravans accosted and villages burnt, in that they create a provocation. So far, they only refer to the player
logent_border_incident_troop_attacks_neutral  = 76
logent_border_incident_troop_breaks_truce     = 77
logent_border_incident_troop_suborns_lord   = 78


logent_policy_ruler_attacks_without_provocation             = 80
logent_policy_ruler_ignores_provocation                     = 81 #possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon                    = 82
logent_policy_ruler_declares_war_with_justification         = 83
logent_policy_ruler_breaks_truce                            = 84
logent_policy_ruler_issues_indictment_just                  = 85 #possibly add this to rumors for non-player faction
logent_policy_ruler_issues_indictment_questionable          = 86 #possibly add this to rumors for non-player faction

logent_player_faction_declares_war                            = 90 #this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity            = 91
logent_faction_declares_war_to_regain_territory             = 92
logent_faction_declares_war_to_curb_power                    = 93
logent_faction_declares_war_to_respond_to_provocation        = 94
logent_faction_declares_war_due_to_religious_differences        = 95
logent_war_declaration_types_end                            = 96


#logent_lady_breaks_betrothal_with_lord      = 58
#logent_lady_betrothal_broken_by_lord        = 59

#lord reputation type, for commentaries
#"Martial" will be twice as common as the other types
lrep_none           = 0 
lrep_martial        = 1 #chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome    = 2 #spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous  = 3 #coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning        = 4 #coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched      = 5 #spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured    = 6 #chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding     = 7 #moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish        = 8 #used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor     = 9 #used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian      = 10 #used for commons, specifically ex-companions. Tries to maximize fief's earning potential

#lreps specific to dependent noblewomen
lrep_conventional    = 21 #Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous     = 22 #Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly    = 23 #Prone to mysticism, romantic. 
lrep_ambitious       = 24 #Lady Macbeth
lrep_moralist        = 25 #Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa 

#a more complicated system of reputation could include the following...

#successful vs unlucky -- basic gauge of success
#daring vs cautious -- maybe not necessary
#honorable/pious/ideological vs unscrupulous -- character's adherance to an external code of conduct. Fails to capture complexity of people like Aurangzeb, maybe, but good for NPCs
    #(visionary/altruist and orthodox/unorthodox could be a subset of the above, or the specific external code could be another tag)
#generous/loyal vs manipulative/exploitative -- character's sense of duty to specific individuals, based on their relationship. Affects loyalty of troops, etc
#merciful vs cruel/ruthless/sociopathic -- character's general sense of compassion. Sher Shah is example of unscrupulous and merciful (the latter to a degree).
#dignified vs unconventional -- character's adherance to social conventions. Very important, given the times


courtship_poem_tragic      = 1 #Emphasizes longing, Laila and Majnoon
courtship_poem_heroic      = 2 #Norse sagas with female heroines
courtship_poem_comic       = 3 #Emphasis on witty repartee -- Contrasto (Sicilian school satire) 
courtship_poem_mystic      = 4 #Sufi poetry. Song of Songs
courtship_poem_allegoric   = 5 #Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

#courtship gifts currently deprecated







#Troop Commentaries end

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end   = "trp_tutorial_archer_1"

#Walker types: 
walkert_default            = 0
walkert_needs_money        = 1
walkert_needs_money_helped = 2
walkert_spy                = 3
num_town_walkers = 8 # was 8
town_walker_entries_start = 32

# reinforcement_cost_easy = 600
# reinforcement_cost_moderate = 450
# reinforcement_cost_hard = 300
#tom this was rafi set, i bet
# reinforcement_cost_easy = 2400
# reinforcement_cost_moderate = 1800
# reinforcement_cost_hard = 1200

reinforcement_cost_easy = 2000
reinforcement_cost_moderate = 1700
reinforcement_cost_hard = 1500

merchant_toll_duration        = 72 #Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 70


raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"
countersigns_end = names_begin
secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

bandits_begin = "trp_bandit"
bandits_end = "trp_black_khergit_horseman"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

#active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_2_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = "trp_enhanced_rnd_lord_end"  ######### NEW v2.9 - this shall fix some issues

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = kings_begin

active_npcs_begin = "trp_npc1"
active_npcs_end = kingdom_ladies_begin
#"active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
#If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

#Rebellion changes

##rebel_factions_begin = "fac_kingdom_1_rebels"
##rebel_factions_end =   "fac_kingdoms_end"

# pretenders_begin = "trp_kingdom_4_pretender"
# pretenders_end = active_npcs_end
#Rebellion changes

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end   = "trp_kingdom_heroes_including_player_begin"

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end   = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end   = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end   = tavern_travelers_begin

mercenary_troops_begin = "trp_merc_euro_spearman"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_swadian_crossbowman_multiplayer"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_ai_troops_begin = "trp_swadian_crossbowman_multiplayer_ai"
multiplayer_ai_troops_end = multiplayer_troops_begin

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end   = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2   = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end   = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2   = "qst_blank_quest_6"

mayor_quests_begin  = "qst_move_cattle_herd"
mayor_quests_end    = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2   = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end   = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2   = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end   = lady_quests_begin

army_quests_begin_2 = "qst_blank_quest_21"
army_quests_end_2   = "qst_blank_quest_21"

player_realm_quests_begin = "qst_resolve_dispute"
player_realm_quests_end = "qst_blank_quest_1"

player_realm_quests_begin_2 = "qst_blank_quest_26"
player_realm_quests_end_2 = "qst_blank_quest_26"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1_1"
castles_begin = "p_castle_1_1"
villages_begin = "p_village_1_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end   = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end   = castles_end

centers_begin = towns_begin
centers_end   = villages_end

training_grounds_begin   = "p_training_ground"
training_grounds_end     = "p_bridge_1"

scenes_begin = "scn_town_arab_center"
scenes_end = "scn_castle_walls_euro"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin       = "trp_novice_fighter"
regular_troops_end         = "trp_tournament_master"

swadian_merc_parties_begin = "p_town_1_mercs"
swadian_merc_parties_end   = "p_town_8_mercs"

vaegir_merc_parties_begin  = "p_town_8_mercs"
vaegir_merc_parties_end    = "p_zendar"

arena_masters_begin    = "trp_town_1_arena_master"
arena_masters_end      = "trp_town_1_armorer"

training_gound_trainers_begin    = "trp_trainer_1"
training_gound_trainers_end      = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
town_walkers_end = "trp_village_walker_1"

village_walkers_begin = "trp_village_walker_1"
village_walkers_end   = "trp_spy_walker_1"

spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end   = spy_walkers_end

armor_merchants_begin  = "trp_town_1_armorer"
armor_merchants_end    = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end   = "trp_town_1_tavernkeeper"

tavernkeepers_begin    = "trp_town_1_tavernkeeper"
tavernkeepers_end      = "trp_town_1_merchant"

goods_merchants_begin  = "trp_town_1_merchant"
goods_merchants_end    = "trp_town_1_horse_merchant"

horse_merchants_begin  = "trp_town_1_horse_merchant"
horse_merchants_end    = "trp_town_1_mayor"

mayors_begin           = "trp_town_1_mayor"
mayors_end             = "trp_village_1_elder"

village_elders_begin   = "trp_village_1_elder"
village_elders_end     = "trp_merchants_end"

startup_merchants_begin = "trp_merchant_kingdom_1"
startup_merchants_end = "trp_startup_merchants_end"

num_max_items = 10000 #used for multiplayer mode

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

village_prod_min = 0 #was -5
village_prod_max = 20 #was 20

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"
food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"
reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end   = trade_goods_begin
readable_books_begin = "itm_book_tactics"
readable_books_end   = reference_books_begin
books_begin = readable_books_begin
books_end = reference_books_end
horses_begin = "itm_sumpter_horse"
horses_end = "itm_arrows"
weapons_begin = "itm_wooden_stick"
weapons_end = "itm_wooden_shield"
####### NEW v2.9-KOMKE START-Changed 
# ranged_weapons_begin = "itm_jarid"
# ranged_weapons_end = "itm_torch"
# armors_begin = "itm_leather_gloves"
# armors_end = "itm_wooden_stick"
# shields_begin = "itm_wooden_shield"
# shields_end = "itm_jarid"
ranged_weapons_begin = "itm_practice_bow_2"
ranged_weapons_end = "itm_arrows"
armors_begin = "itm_leather_gloves"
armors_end = "itm_wooden_stick"
shields_begin = "itm_wooden_shield"
shields_end = "itm_sumpter_horse"
####### NEW v2.9-KOMKE END- 

# Banner constants

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_x21"

arms_meshes_begin = "mesh_arms_a01"
arms_meshes_end_minus_one = "mesh_arms_x21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_flag_scene_props_begin = "spr_custom_banner_01"
custom_banner_flag_scene_props_end = "spr_banner_a"

custom_banner_map_icons_begin = "icon_custom_banner_01"
custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_462"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_x21"

khergit_banners_begin_offset = 63
khergit_banners_end_offset = 84

sarranid_banners_begin_offset = 105
sarranid_banners_end_offset = 125

banners_end_offset = 483

# Some constants for merchant invenotries
merchant_inventory_space = 18
num_merchandise_goods = 25

num_max_river_pirates = 25
num_max_zendar_peasants = 25
num_max_zendar_manhunters = 10

num_max_dp_bandits = 10
num_max_refugees = 10
num_max_deserters = 10

num_max_militia_bands = 15
num_max_armed_bands = 12

num_max_vaegir_punishing_parties = 20
num_max_rebel_peasants = 25

num_max_frightened_farmers = 50
num_max_undead_messengers  = 20

taiga_bandit_spawn_begin = "p_taiga_bandit_spawn_point_1"
taiga_bandit_spawn_end = "p_steppe_bandit_spawn_point_1"

steppe_bandit_spawn_begin = "p_steppe_bandit_spawn_point_1"
steppe_bandit_spawn_end = "p_forest_bandit_spawn_point_1"

forest_bandit_spawn_begin = "p_forest_bandit_spawn_point_1"
forest_bandit_spawn_end = "p_mountain_bandit_spawn_point_1"

mountain_bandit_spawn_begin = "p_mountain_bandit_spawn_point_1"
mountain_bandit_spawn_end = "p_sea_raider_spawn_point_1"

sea_raider_spawn_begin = "p_sea_raider_spawn_point_1"
sea_raider_spawn_end = "p_desert_bandit_spawn_point_1"

desert_bandit_spawn_begin = "p_desert_bandit_spawn_point_1"
desert_bandit_spawn_end = "p_spawn_points_end"

num_forest_bandit_spawn_points = 2
num_mountain_bandit_spawn_points = 14
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_black_khergit_spawn_points = 1
num_sea_raider_spawn_points = 12

peak_prisoner_trains = 4
peak_kingdom_caravans = 12
peak_kingdom_messengers = 3

bandit_lair_distance_max =35 # max distance to travel to lairs

# Note positions
note_troop_location = 3

#battle tactics
btactic_hold = 1
btactic_follow_leader = 2
btactic_charge = 3
btactic_stand_ground = 4

#default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# Town center modes - resets in game menus during the options
tcm_default         = 0
tcm_disguised         = 1
tcm_prison_break     = 2
tcm_escape          = 3


# Arena battle modes
#abm_fight = 0
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee    = 1
ctm_ranged   = 2
ctm_mounted  = 3
ctm_training = 4

# Village bandits attack modes
vba_normal          = 1
vba_after_training  = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 5
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 10
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 25
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 60
arena_grand_prize = 250


#Additions
price_adjustment = 25 #the percent by which a trade at a center alters price

fire_duration = 4 #fires takes 4 hours

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

dplmc_npc_mission_war_request                 = 9
dplmc_npc_mission_alliance_request            = 10
dplmc_npc_mission_spy_request                 = 11
dplmc_npc_mission_gift_fief_request           = 12
dplmc_npc_mission_gift_horses_request         = 13
dplmc_npc_mission_threaten_request            = 14
dplmc_npc_mission_prisoner_exchange           = 15
dplmc_npc_mission_defensive_request           = 16
dplmc_npc_mission_trade_request               = 17
dplmc_npc_mission_nonaggression_request       = 18
dplmc_spt_spouse                              = 24
dplmc_spt_gift_caravan                        = 23
dplmc_spt_messenger                           = 25 #no prefix since its outcommented in native
spt_patrol                                    = 7 #no prefix since its outcommented in native
##diplomacy end 

# rafi constants
religion_catholic = 0
religion_orthodox = 1
religion_muslim = 2
religion_pagan_balt = 3
religion_pagan_mongol = 4

########### NEW
religion_heretic = 5
religion_pagan_nordic = 6

raf_spt_messenger = 26

mounted_limit = 25
knight_limit = 5
sergeant_limit = 10

# max_war_distance = 45
# religious_effect_aggressive = 20 # religion effect on relationships
# religious_effect_docile = 10

max_war_distance = 45 * 1.5
########### NEW v1.8
religious_effect_very_aggressive = 12 # religion effect on relationships
religious_effect_aggressive = 7 # religion effect on relationships
religious_effect_docile = 3
religious_effect_crusade = 50

info_clr = 0x2d81ff

region_unknown = -1
region_baltic = 1
region_nordic = 2
region_eastern = 3
region_mongol = 4 
region_european = 5
region_teutonic = 6
region_gaelic = 7
region_crusaders = 8
region_byzantine = 9
region_andalusian = 10
region_north_african = 11
region_mamluk = 12
region_latin = 13
region_anatolian = 14
region_balkan = 15
region_scot = 16 #Tom

recruitment_cost_village = 10
recruitment_cost_town = 12
recruitment_cost_castle = 75

time_multiplier = 1

## CC
# constants

armor_cloth                   = 0
armor_armor                   = 1
armor_plate                   = 2

wpn_setting_1                 = 1
wpn_setting_2                 = 2
armor_setting                 = 3
horse_setting                 = 4
  #### Autoloot improved by rubik end
# Formations for Warband by Motomataru
# rel. 05/02/11

#Formation modes
formation_none    = 0
formation_default    = 1
formation_ranks    = 2
formation_shield    = 3
formation_wedge    = 4
formation_square    = 5

#Formation tweaks
formation_minimum_spacing    = 67
formation_minimum_spacing_horse_length    = 300
formation_minimum_spacing_horse_width    = 200
formation_start_spread_out    = 2
formation_min_foot_troops    = 12
formation_min_cavalry_troops    = 5
formation_autorotate_at_player    = 1
formation_native_ai_use_formation = 1
formation_delay_for_spawn    = .4
formation_reequip    = 0 #1 Tom - disable, as we use our formation thing    #TO DO: One-time-on-form option when formation slots integrated

from module_constants import slot_town_rebellion_readiness, slot_town_arena_melee_mission_tpl

#Other constants (not tweaks)
Third_Max_Weapon_Length = 250 / 3
slot_party_cabadrin_order_d0 = slot_town_arena_melee_mission_tpl #78
slot_party_gk_order          = slot_town_rebellion_readiness #77

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
# slot_item_difficulty = 5

# # Autoloot improved by rubik begin
# slot_item_weight                  = 6

# slot_item_cant_on_horseback       = 10
# slot_item_type_not_for_sell       = 11
# slot_item_modifier_multiplier     = 12

#positions used through formations and AI triggers
# Player_Battle_Group3_Pos    = 24    #pos24
# Player_Battle_Group4_Pos    = 25    #pos25
# Player_Battle_Group5_Pos    = 26    #pos26
# Player_Battle_Group6_Pos    = 27    #pos27
# Player_Battle_Group7_Pos    = 28    #pos28
# Player_Battle_Group8_Pos    = 29    #pos29

# Team0_Infantry_Pos    = 30    #pos30
# Team0_Archers_Pos    = 31    #pos31
# Team0_Cavalry_Pos    = 32    #pos32
# Team0_Average_Pos    = 33    #pos33
# Team1_Infantry_Pos    = 34    #pos34
# Team1_Archers_Pos    = 35    #pos35
# Team1_Cavalry_Pos    = 36    #pos36
# Team1_Average_Pos    = 37    #pos37
# Team2_Infantry_Pos    = 38    #pos38
# Team2_Archers_Pos    = 39    #pos39
# Team2_Cavalry_Pos    = 40    #pos40
# Team2_Average_Pos    = 41    #pos41
# Team3_Infantry_Pos    = 42    #pos42
# Team3_Archers_Pos    = 43    #pos43
# Team3_Cavalry_Pos    = 44    #pos44
# Team3_Average_Pos    = 45    #pos45

#keys used for old M&B
from header_triggers import *
key_for_ranks    = key_j
key_for_shieldwall    = key_k
key_for_wedge    = key_l
key_for_square    = key_semicolon
key_for_undo    = key_u

#slots used instead of more global variables
slot_team_faction                      = 1
slot_team_default_formation            = 2    #used for infantry formations
slot_team_reinforcement_stage          = 3
#Reset with every call of Store_Battlegroup_Data
slot_team_size                         = 4
slot_team_adj_size                     = 5 #cavalry double counted for AI considerations
slot_team_level                        = 6
slot_team_num_infantry                 = 7    #these may not be needed anymore (duplicate division size)
slot_team_num_archers                  = 8
slot_team_num_cavalry                  = 9
slot_team_avg_x                        = 10 # **used instead of POS registers
slot_team_avg_y                        = 11 # **used instead of POS registers
slot_team_d0_size                      = 12 #plus 8 more for the other divisions
slot_team_d0_percent_ranged            = 21 #plus 8 more for the other divisions
slot_team_d0_percent_throwers          = 30 #plus 8 more for the other divisions
slot_team_d0_low_ammo                  = 39 #plus 8 more for the other divisions
slot_team_d0_level                     = 48 #plus 8 more for the other divisions
slot_team_d0_weapon_length             = 57 #plus 8 more for the other divisions
slot_team_d0_x                         = 66 #plus 8 more for the other divisions **used instead of POS registers
slot_team_d0_y                         = 75 #plus 8 more for the other divisions **used instead of POS registers
#End Reset Group
slot_team_d0_type                      = 84 #plus 8 more for the other divisions
slot_team_d0_formation                 = 93 #plus 8 more for the other divisions
slot_team_d0_formation_space           = 102 #plus 8 more for the other divisions
slot_team_d0_move_order                = 111 #plus 8 more for the other divisions
slot_team_d0_first_member              = 120 #plus 8 more for the other divisions
slot_team_d0_formation_x               = 129 #plus 8 more for the other divisions
slot_team_d0_formation_y               = 138 #plus 8 more for the other divisions
slot_team_d0_formation_zrot            = 147 #plus 8 more for the other divisions

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_y + 8 + 1

#Slot Division Type definitions
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

#AI variables
AI_long_range    = 13000    #do not put over 130m if you want archers to always fire
AI_firing_distance    = AI_long_range / 2
AI_charge_distance    = 2000
AI_for_kingdoms_only    = 0
Far_Away    = 1000000
Percentage_Cav_For_New_Dest    = 40
Hold_Point    = 100    #archer hold if outnumbered
Advance_More_Point    = 100 - Hold_Point * 100 / (Hold_Point + 100)    #advance 'cause expect other side is holding
AI_Delay_For_Spawn    = formation_delay_for_spawn + .1    #fire AFTER formations init
AI_Max_Reinforcements    =    2    #maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player    =    1

#Battle Phases
BP_Setup    = 1
BP_Jockey    = 2
BP_Fight    = 3

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos    = 32    #pos32
Nearest_Non_Cav_Enemy_Troop_Pos    = 33    #pos33
Nearest_Threat_Pos    = 34    #pos34
Nearest_Target_Pos    = 35    #pos35
Infantry_Pos    = 36    #pos36
Archers_Pos    = 37    #pos37
Cavalry_Pos    = 38    #pos38
Enemy_Team_Pos    = 39    #pos39
Nearest_Enemy_Battlegroup_Pos    = 40    #pos40

#positions used through battle
Team0_Cavalry_Destination    = 41    #pos41
Team1_Cavalry_Destination    = 42    #pos42
Team2_Cavalry_Destination    = 43    #pos43
Team3_Cavalry_Destination    = 44    #pos44
Team0_Starting_Point    = 45    #pos45
Team1_Starting_Point    = 46    #pos46
Team2_Starting_Point    = 47    #pos47
Team3_Starting_Point    = 48    #pos48




##bellow skirmishing distance originaly
#1500
#2500
skirmish_min_distance = 2200 #Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 3200 #Max distance to maintain, in cm. Where agent will stop retreating

#TOM
horn_sound_interval = 40
crusade_cost = 100000
slot_crusade = 255 #party slot
#village manor constants
manor_cost = 10000
manor_farm_cost = 10000
manor_linen_cost = 10000
manor_salt_cost = 12000
manor_furs_cost = 10000
manor_iron_cost = 10000
manor_silk_cost = 25000
#town manor constants
manor_weapon_cost = 10000
manor_armor_cost = 10000
manor_fletchery_cost = 10000
manor_breeder_cost = 10000
manor_monastery_cost = 20000
#commoner constancts
# commoners_begin = "trp_commoner1"
# commoners_end =  "trp_kingdom_heroes_including_player_begin"



#mercenaries(regional):
generic_euro = 1
generic_balt = 2
generic_maghreb = 4 
generic_rus = 5
generic_latin = 6
generic_balkan = 7
generic_scandinavian = 8
generic_gaelic = 9
generic_mamluk = 10

#historical reserved 1-19 for possible future mercs
merc_barbantine = 20
merc_georgians = 21
merc_sicily_muslims = 22
merc_turkopoles = 23
merc_cumans = 24
merc_kwarezmians = 25
merc_mordovians = 26
merc_kipchaks = 27
merc_geonese = 28
merc_welsh = 29
merc_mamlukes = 30
merc_kwarezmian = 31
merc_mordovian = 32
merc_kipchak = 33

#special
merc_varangians = 50
merc_teutons = 51
merc_hospitaliers = 52
merc_templars = 53
merc_lazarus = 54
merc_santiago = 55
merc_calatrava = 56
merc_saint_thomas = 57

#mongol camp status
status_moving = 0
status_stationed = 1
status_migrating = 2

#agent slots:
slot_possessed = 100
slot_real_troop = 101
############skirmishers
#agent slots:
slot_agent_scripted_mode = 104
slot_agent_rotation = 105
slot_agent_direction = 106
slot_agent_banner = 107
#team slots:
team_slot_direction = 200 #rotate to which direction sets
#party slots:


##recruitment types
town_controled = 0
lord_controled = 1
##recruitment constants for price
town_controled_wage_cap = 10000

#houses
manor_slot_houses = 302 #house lvl 
#tier2
manor_slot_marketplace = 303 #70-90 
manor_slot_tavern = 304 #116-119
manor_slot_whorehouse = 305 #110-115
manor_slot_Monastery = 306 #102
manor_slot_well = 307 
#tier1 -farms
manor_slot_grainfarm = 308 #p:90 E:41 81
manor_slot_livestock = 309 #p:91 E:42 82
manor_slot_fruitfarm = 310 #p:92 E:43 83
manor_slot_fisher = 311 #p:93 E:44 84
#tier3
manor_slot_bakery = 312 #p:94 E:45 85
manor_slot_winery = 313 #p:95  E:46 86
manor_slot_brewery = 314 #p96 E:47 87
manor_slot_potter = 315 #97 E:48 88spr_to_castle_courtyard_house_b
manor_slot_blacksmith = 316 #98 E:49 89
manor_slot_butcher = 317 #99 E:50 90
manor_slot_oilmaker = 318 #100 E:51 91
manor_slot_linenworkshop = 319 #101 E:52 92
manor_slot_woolworkshop = 320 #102 E:53 93
manor_slot_tannery = 321 #103 E:54 94
#tier4
manor_slot_prison = 322 #103
manor_slot_armorsmith = 323 #104
manor_slot_weaponsmith = 324 #105
manor_slot_fletcher = 325 #106
manor_slot_breeder = 326 #107
manor_slot_walls = 327 #60-70 50-60
#utility
manor_slot_Monastery_upgrade = 340 #player can enact a crusader order in the manor
manor_slot_taxes = 341 #low-high-medium
manor_slot_population = 342 #cur population
manor_slot_last_tax = 343 #last tax amount
manor_slot_trader = 344 #current trader at the manor
#taxes
manor_slot_tax_grainfarm = 345
manor_slot_tax_livestock = 346
manor_slot_tax_fruitfarm = 347
manor_slot_tax_fisher = 348
manor_slot_tax_bakery = 349
manor_slot_tax_winery = 350
manor_slot_tax_brewery = 351
manor_slot_tax_potter = 352
manor_slot_tax_blacksmith = 353
manor_slot_tax_butcher = 354
manor_slot_tax_oilmaker = 355
manor_slot_tax_linenworkshop = 356
manor_slot_tax_woolworkshop = 357
manor_slot_tax_tannery = 358
manor_slot_tax_armorsmith = 359
manor_slot_tax_weaponsmith = 360
manor_slot_tax_fletcher = 361
manor_slot_tax_breeder = 362
manor_slot_gold = 367

party_slot_original_icon = 600
faction_slot_water_icon = 600
#manor constants
manor_high_taxes =  1
manor_medium_taxes = 0
manor_low_taxes = -1
manor_building_notbuild = 0
manor_building_operational = 1
manor_building_inprogress = 2
manor_building_abandoned = 3
manor_population_tier1 = 200
manor_population_tier2 = 760
manor_population_tier3 = 1000
manor_taxes_tier1 = 30
manor_taxes_tier2 = 50
manor_taxes_tier3 = 80
manor_taxes_tier4 = 100
manor_Monastery_none = 0
manor_Monastery_scriptorium = 1
manor_Monastery_teutons = 2
manor_Monastery_templars = 3
manor_Monastery_lazarus = 4
manor_Monastery_santiago = 5
manor_Monastery_calatrava = 6
manor_Monastery_thomas = 7
manor_Monastery_hospitaliers = 8
#from id_items import *
spt_merc_party = 30
spt_mongol_party = 31

#manor party templates


#manor troop constants
manor_troop_taxes_money = 0
manor_troop_taxes_goods = 1

#feudal lance agent slot
slot_index_value = 102 
#feudal lance constants
finn_culture_start = trp_finn_village_recruit
finn_culture_end = trp_mazovian_town_recruit
mazovian_culture_start = trp_mazovian_town_recruit
mazovian_culture_end = trp_serbian_vil_recruit
serbian_culture_start = trp_serbian_vil_recruit
serbian_culture_end = trp_welsh_recruit
welsh_culture_start = trp_welsh_recruit
welsh_culture_end = trp_teu_village_recruit
teutonic_culture_start = trp_teu_village_recruit
teutonic_culture_end = trp_balkan_vil_1
balkan_culture_start = trp_balkan_vil_1
balkan_culture_end = trp_rus_vil_1
rus_culture_start = trp_rus_vil_1
rus_culture_end = trp_nordic_village_recruit
nordic_culture_start = trp_nordic_village_recruit
nordic_culture_end = trp_balt_recruit
balt_culture_start = trp_balt_recruit
balt_culture_end = trp_marinid_village_rabble
marinid_culture_start = trp_marinid_village_rabble
marinid_culture_end = trp_bedouin_recruit
bedouin_culture_start = trp_bedouin_recruit
bedouin_culture_end = trp_byz_village_1
byz_culture_start = trp_byz_village_1
byz_culture_end = trp_iberian_village_recruit
iberian_culture_start = trp_iberian_village_recruit
iberian_culture_end = trp_italian_village_recruit
italian_culture_start = trp_italian_village_recruit
italian_culture_end = trp_andalus_village_recruit
andalus_culture_start = trp_andalus_village_recruit
andalus_culture_end = trp_gaelic_village_recruit
gaelic_culture_start = trp_gaelic_village_recruit
gaelic_culture_end = trp_anatolian_village_recruit_christ
################## NEW v1.8
anatolian_christian_culture_start = trp_anatolian_village_recruit_christ
anatolian_christian_culture_end = trp_anatolian_village_recruit
anatolian_culture_start = trp_anatolian_village_recruit
anatolian_culture_end = trp_scottish_village_recruit
####################################
scottish_culture_start = trp_scottish_village_recruit
scottish_culture_end = trp_euro_town_recruit
euro_culture_start = trp_euro_town_recruit
euro_culture_end = trp_tatar_tribesman
################## NEW v1.8/2.1 - CWE Factions
mongol_culture_start = trp_tatar_tribesman
mongol_culture_end = trp_euro_town_recruit_templar
templar_culture_start = trp_euro_town_recruit_templar
templar_culture_end = trp_euro_town_recruit_hospitaller
hospitaller_culture_start = trp_euro_town_recruit_hospitaller
hospitaller_culture_end = trp_euro_town_recruit_antioch
antioch_culture_start = trp_euro_town_recruit_antioch
antioch_culture_end = trp_euro_town_recruit_tripoli
tripoli_culture_start = trp_euro_town_recruit_tripoli
tripoli_culture_end = trp_euro_town_recruit_ibelin
ibelin_culture_start = trp_euro_town_recruit_ibelin
ibelin_culture_end = trp_euro_town_recruit_jerusalem
jerusalem_culture_start = trp_euro_town_recruit_jerusalem
jerusalem_culture_end = trp_looter
################## NEW v3.3
crusader_culture_start = trp_euro_town_recruit
crusader_culture_end = trp_tatar_tribesman
cuman_culture_start = trp_cuman_tribesman
cuman_culture_end = trp_crusader_turkopole
player_culture_start = trp_cstm_custom_troop_3_tiers_0_0_0
player_culture_end = trp_cstm_custom_troop_3_tiers_1_0_0
####################################
regulars_begin = trp_finn_village_recruit
regulars_end = trp_looter
traders_begin = trp_trader_hat1
traders_end =  trp_trader_silk4+1
###ECONOMY CONSTANTS
##farm
cost_head_cattle = 1000
cost_head_sheep = 1000
cost_head_horses = 1000
cost_acres_grain = 1000
cost_acres_olives = 1000
cost_acres_vineyard = 1000
cost_acres_flax = 1000
cost_acres_dates = 1000
cost_fishing_fleet = 1000
cost_salt_pans = 1000
cost_apiaries = 1000
cost_silk_farms = 1000
cost_kirmiz_farms = 1000
cost_iron_deposits = 1000
cost_fur_traps = 1000
cost_household_gardens = 1000
###town
cost_mills = 2000
cost_breweries = 2000
cost_wine_presses = 2000
cost_olive_presses = 2000
cost_linen_looms = 2000
cost_silk_looms = 2000
cost_wool_looms = 2000
cost_pottery_kilns = 2000
cost_smithies = 2000
cost_tanneries = 2000
cost_shipyards = 2000

###PROSPERITY SYSTEM 
slot_faction_at_war = 400
slot_center_nobility_law = 800
slot_center_commoner_law = 801
slot_center_focus = 802

rate_very_low = -2
rate_low = -1
rate_average = 0
rate_high = 1
rate_very_high = 2

size_small = 1
size_average = 2
size_large = 3

tier1_dif = 20
tier2_dif = 10
tier3_dif = 5

mongol_relocation_cost = 100
###PROSPERITY SYSTEM 
###SIEGES
##scene props slot
slot_prop_oil = 400
##constants
oil_timer = 5  #in seconds
###SIEGES


#### shaders
shader_float_default = 15
shader_float_day = 50
#### shaders





#################################################### EXTRA WEAPON COMMANDS
ranged    = 0
onehand   = 1
bothhands = 2
shield    = 3

from header_triggers import *
key_for_onehand   = key_f9
key_for_bothhands = key_f10
key_for_ranged    = key_f11
key_for_shield    = key_f8
####################################################



#################################################### VOLLEY FIRE
slot_agent_volley_fire             = 33
slot_team_d0_order_volley     = 10 #plus 8 more for the other divisions

from header_triggers import *
key_for_volley   = key_f12
#####################################################




##################################################### SHOW ME YOUR EQUIPMENT 
# DPLMC_FACTION_STANDING_LEADER = 60
# DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
# DPLMC_FACTION_STANDING_MARSHALL = 40
# DPLMC_FACTION_STANDING_LORD = 30
# DPLMC_FACTION_STANDING_DEPENDENT = 20
# DPLMC_FACTION_STANDING_MEMBER = 10 #includes mercenaries
# DPLMC_FACTION_STANDING_PETITIONER = 5
# DPLMC_FACTION_STANDING_UNAFFILIATED = 0
#####################################################






slot_agent_horse_rider = 45
slot_agent_new_division = 46




################################################## CTT TROOPS
player_culture_start = "trp_cstm_custom_troop_1_tier_0_0_0"
player_culture_end = "trp_cstm_custom_troops_end"
#######################################################################





##################### BRAWL!!!!!!!!! #################################
tavern_goer_begin = "trp_town_walker_1"
tavern_goer_end = "trp_spy_walker_1"
######################################################################



###################### NEW MERC SLOTS
slot_regional_party_template_2 = 710
slot_regional_party_template_3 = 711
slot_regional_mercs_2 = 712
slot_regional_mercs_3 = 713
slot_regional_mercs2_number = 714
slot_regional_mercs3_number = 715
##########################################



################## NEW CULTURE 
cultures_begin = "fac_culture_finnish"
cultures_end = "fac_player_faction"
##########################################




################# BRYTENWALDA TAVERN BOUNTY
# outlaws_begin = "trp_bounty5"
# outlaws_end   = "trp_bounty6"

# rogues_begin = "trp_bounty4"
# rogues_end   = "trp_bounty5"

# goblin_outlaws_begin = "trp_bounty1"
# goblin_outlaws_end   = "trp_bounty4"

# orc_outlaws_begin = "trp_bounty6"
# orc_outlaws_end   = "trp_bounty7"

# elf_outlaws_begin = "trp_bounty8"
# elf_outlaws_end   = "trp_bounty9"

# darkelf_outlaws_begin = "trp_bounty10"
# darkelf_outlaws_end   = "trp_bounty11"

# saracen_outlaws_begin = "trp_bounty12"
# saracen_outlaws_end   = "trp_bounty1"

# fugitives_begin = "trp_fugitive"
# fugitives_end = "trp_belligerent_drunk"

bounties_begin = "qst_bounty_1"
bounties_end   = "qst_kill_local_merchant"
##########################################






###################################### SILVERSTAG IMPROVEMENTS
# native_improvements_begin                       = slot_center_has_manor
# native_improvements_end                         = 136

# slot_center_has_garrison                        = 402 # V
# slot_center_has_crops_of_grain                  = 403 # V, C
# slot_center_has_armoury                         = 404 # C, T
# slot_center_has_small_marketplace               = 405 # V, C, T
# slot_center_has_improved_roads                  = 406 # V, C, T
# slot_center_has_fire_brigade                    = 407 # V, C, T
# slot_center_has_forge                           = 408 # V
# slot_center_has_merc_chapterhouse               = 409 # T
# slot_center_has_escape_tunnels                  = 410 # C, T
# slot_center_has_trade_guilds                    = 411 # T
# slot_center_has_castle_library                  = 412 # C, T
# slot_center_has_training_grounds                = 413 # C, T
# slot_center_has_reinforced_walls                = 414 # C, T
# slot_center_has_fishery                         = 415 # V
# slot_center_has_stables                         = 416 # V, C, T
# slot_center_has_horse_ranch                     = 417 # V
# slot_center_has_royal_forge                     = 418 # C, T
# slot_center_has_moat                            = 419 # C, T

# center_improvements_begin                       = slot_center_has_garrison
# center_improvements_end                         = slot_center_has_moat


############## Mercenary Chapterhouse (409)
# mercenary_chapterhouse_min_troop                = "trp_mercenary_swordsman"
# mercenary_chapterhouse_troop_bonus              = 8
# mercenary_chapterhouse_hiring_discount          = 40 # %



######################## 
MODDED2x_AIAgentResetTimer = 30
MODDED2x_AIAgentResetNow = 29
########################



######################## NEW IMPROVEMENT CONSTANTS

########## cristian knight orders
slot_center_has_chapter_minor_teutonic = 420
slot_center_has_chapter_minor_templar = 421
slot_center_has_chapter_minor_hospitaller = 422
slot_center_has_chapter_minor_saint_lazarus = 423
slot_center_has_chapter_minor_santiago = 424
slot_center_has_chapter_minor_calatrava = 425
slot_center_has_chapter_minor_saint_thomas = 426

slot_center_has_chapter_major_teutonic = 427
slot_center_has_chapter_major_templar = 428
slot_center_has_chapter_major_hospitaller = 429
slot_center_has_chapter_major_saint_lazarus = 430
slot_center_has_chapter_major_santiago = 431
slot_center_has_chapter_major_calatrava = 432
slot_center_has_chapter_major_saint_thomas = 433

slot_center_has_chapter_hq_teutonic = 434
slot_center_has_chapter_hq_templar = 435
slot_center_has_chapter_hq_hospitaller = 436
slot_center_has_chapter_hq_saint_lazarus = 437
slot_center_has_chapter_hq_santiago = 438
slot_center_has_chapter_hq_calatrava = 439
slot_center_has_chapter_hq_saint_thomas = 440

slot_center_has_chapter_major_hq_teutonic = 441
slot_center_has_chapter_major_hq_templar = 442
slot_center_has_chapter_major_hq_hospitaller = 443

##### Muslim
slot_center_has_quarters_minor_mamluk = 444
slot_center_has_quarters_major_mamluk = 445
slot_center_has_quarters_hq_mamluk = 446

######### Byzantine
slot_center_has_quarters_major_varangian = 447
slot_center_has_quarters_hq_varangian = 448

slot_center_has_quarters_minor_cataphract = 449
slot_center_has_quarters_major_cataphract = 450
slot_center_has_quarters_hq_cataphract = 451

######## more mobile mercs 
slot_center_has_camp_minor_cuman = 452
slot_center_has_camp_large_cuman = 453
slot_center_has_camp_major_cuman = 454

slot_center_has_camp_minor_kipchak = 455
slot_center_has_camp_large_kipchak = 456
slot_center_has_camp_major_kipchak = 457

slot_center_has_camp_minor_mongol = 458
slot_center_has_camp_large_mongol = 459
slot_center_has_camp_major_mongol = 460

slot_center_has_camp_minor_georgian = 461
slot_center_has_camp_large_georgian = 462
slot_center_has_camp_major_georgian = 463

slot_center_has_camp_minor_kwarezmian = 464
slot_center_has_camp_large_kwarezmian = 465
slot_center_has_camp_major_kwarezmian = 466

slot_center_has_outpost_minor_crusader_turcopole = 467
slot_center_has_outpost_large_crusader_turcopole = 468
slot_center_has_outpost_major_crusader_turcopole = 469


  
############ other
slot_center_has_quarters_minor_genoese = 470
slot_center_has_quarters_major_genoese = 471
slot_center_has_quarters_hq_genoese = 472

slot_center_has_outpost_minor_finnish = 473
slot_center_has_outpost_large_finnish = 474
slot_center_has_outpost_major_finnish = 475

slot_center_has_quarters_minor_brabantine = 476
slot_center_has_quarters_major_brabantine = 477
slot_center_has_quarters_hq_brabantine = 478

slot_center_has_outpost_minor_welsh_kern = 479
slot_center_has_outpost_large_welsh_kern = 480
slot_center_has_outpost_major_welsh_kern = 481

slot_center_has_outpost_minor_gaelic = 482
slot_center_has_outpost_large_gaelic = 483
slot_center_has_outpost_major_gaelic = 484



############# center improvements
slot_center_has_tier_1_improved_school = 520
slot_center_has_tier_2_university = 521

slot_center_has_tier_1_training_grounds = 522
slot_center_has_tier_2_training_facilities = 523

slot_center_has_tier_1_town_hall = 524
slot_center_has_tier_2_city_hall = 525
slot_center_has_tier_3_governors_palace = 526
slot_center_has_tier_4_royal_palace = 527

slot_center_has_tier_1_brothel = 528
slot_center_has_tier_2_coaching_house = 529
slot_center_has_tier_2_wayfarers_rest = 530
slot_center_has_tier_3_pleasure_palace = 531

slot_center_has_tier_1_dirt_roads = 532
slot_center_has_tier_2_paved_roads  = 533

slot_center_has_tier_1_land_clearance  = 534
slot_center_has_tier_2_communal_farming  = 535
slot_center_has_tier_3_crop_rotation  = 536
slot_center_has_tier_4_irrigation  = 537


slot_center_has_tier_1_jousting_lists  = 540
slot_center_has_tier_2_tournament_grounds  = 541

slot_center_has_tier_1_village_guards  = 545


############# religious buildings
slot_center_has_tier_1_small_church  = 570
slot_center_has_tier_1_small_masjid  = 571
slot_center_has_tier_1_small_balt_temple  = 572
slot_center_has_tier_1_small_mongol_temple  = 573
slot_center_has_tier_1_small_satan_temple  = 574
slot_center_has_tier_1_small_nordic_temple  = 575

slot_center_has_tier_2_church  = 580
slot_center_has_tier_2_masjid  = 581
slot_center_has_tier_2_balt_temple  = 582
slot_center_has_tier_2_mongol_temple  = 583
slot_center_has_tier_2_satan_temple  = 584
slot_center_has_tier_2_nordic_temple  = 585

slot_center_has_tier_3_abbey  = 590
slot_center_has_tier_3_minaret  = 591
slot_center_has_tier_3_large_balt_temple  = 592
slot_center_has_tier_3_large_mongol_temple  = 593
slot_center_has_tier_3_large_satan_temple  = 594
slot_center_has_tier_3_large_nordic_temple  = 595

slot_center_has_tier_4_cathedral  = 600
slot_center_has_tier_4_jama  = 601
slot_center_has_tier_4_huge_balt_temple  = 602
slot_center_has_tier_4_huge_mongol_temple  = 603
slot_center_has_tier_4_huge_satan_temple  = 604
slot_center_has_tier_4_huge_nordic_temple  = 605

slot_center_has_tier_5_huge_cathedral  = 610
slot_center_has_tier_5_great_jama  = 611
slot_center_has_tier_5_great_temple_of_dievas = 612
slot_center_has_tier_5_great_temple_of_tengri  = 613
slot_center_has_tier_5_great_synagogue_of_satan  = 614
slot_center_has_tier_5_great_temple_of_odin  = 615
######################

 
slot_center_has_tier_1_masons_guild  = 620
slot_center_has_tier_2_master_masons_guild  = 621
slot_center_has_tier_3_masons_guild_hq  = 622

slot_center_has_tier_1_fairground  = 630
slot_center_has_tier_2_great_market   = 631
slot_center_has_tier_3_merchants_quarter  = 632

slot_center_has_tier_1_mines  = 640
slot_center_has_tier_2_mining_network   = 641

slot_center_has_tier_1_mercenary_quarters   = 650
slot_center_has_tier_2_mercenary_hq   = 651

slot_center_has_tier_1_village_watch    = 660

slot_center_has_tier_1_garrison_quarters    = 670
slot_center_has_tier_2_drill_square    = 671
slot_center_has_tier_3_barracks   = 672
slot_center_has_tier_4_armoury    = 673


slot_center_has_tier_1_merchants_guild     = 680
slot_center_has_tier_2_master_merchants_guild    = 681
slot_center_has_tier_3_merchants_guild_hq   = 682


slot_center_has_tier_1_small_hospital    = 690
slot_center_has_tier_1_small_bimaristan    = 691
slot_center_has_tier_2_hospital    = 692
slot_center_has_tier_2_bimaristan    = 693
slot_center_has_tier_3_college_of_surgeons    = 694
slot_center_has_tier_3_great_bimaristan    = 695


slot_center_has_tier_1_siege_works    = 700
slot_center_has_tier_2_great_siege_works    = 701

slot_center_has_tier_1_merchants_wharf     = 710
slot_center_has_tier_2_warehouse     = 711
slot_center_has_tier_3_docklands    = 712

slot_center_has_tier_1_small_chapel     = 720
slot_center_has_tier_2_chapel     = 721

slot_center_has_tier_1_sewers    = 730
slot_center_has_tier_2_improved_sewers   = 731

slot_center_has_tier_1_town_plumbers    = 740
slot_center_has_tier_2_city_plumbing_quarters   = 741

slot_center_has_tier_1_village_council_hall = 745

slot_center_has_tier_1_housing_town = 750
slot_center_has_tier_2_housing_town = 751
slot_center_has_tier_3_housing_town = 752
slot_center_has_tier_4_housing_town = 753
slot_center_has_tier_5_housing_town = 754
slot_center_has_tier_6_housing_town = 755
slot_center_has_tier_7_housing_town = 756
slot_center_has_tier_8_housing_town = 757

slot_center_has_tier_1_housing_castle = 765
slot_center_has_tier_2_housing_castle = 766
slot_center_has_tier_3_housing_castle = 767
slot_center_has_tier_4_housing_castle = 768
slot_center_has_tier_5_housing_castle = 769

slot_center_has_tier_1_housing_village = 775
slot_center_has_tier_2_housing_village = 776
slot_center_has_tier_3_housing_village = 777
slot_center_has_tier_4_housing_village = 778
slot_center_has_tier_5_housing_village = 779

########################





############# NEW FIEF CONSTANTS
slot_center_population = 800
slot_center_squalor = 801
slot_center_healthy_percentage = 802
slot_center_unrest = 803
slot_center_population_max = 804
slot_center_faction_support = 805
slot_center_law_level = 806
# slot_center_population_default = 806


slot_center_very_poor_percentage = 810
slot_center_poor_percentage = 811
slot_center_middle_percentage = 812
slot_center_rich_percentage = 813
slot_center_very_rich_percentage = 814

slot_center_catholic_percentage = 820
slot_center_orthodox_percentage = 821
slot_center_muslim_percentage = 823
slot_center_balt_percentage = 822
slot_center_mongol_pagan_percentage = 824
slot_center_heretic_percentage = 825
slot_center_nordic_percentage = 826


slot_center_mandatory_draft = 835
slot_center_mandatory_military_training = 836

slot_center_personnel_doctors = 850
slot_center_personnel_accountants = 851

slot_center_personnel_spies = 852
slot_center_personnel_saboteurs = 853

slot_center_personnel_trainers = 853


slot_center_rebellion_original_faction = 865
slot_center_rebellion_active = 866

slot_faction_population_support = 870

slot_center_food_stores = 875
slot_center_food_production_day = 876
slot_center_food_consumption_day = 877

# slot_center_max_enterprises = 900


################################################




##################### NEW MERC CONSTANTS
slot_spec_mercs_number_genoese = 950
slot_spec_mercs_number_turkopole = 951
slot_spec_mercs_number_georgian = 952
slot_spec_mercs_number_cuman = 953
slot_spec_mercs_number_brabantine = 954
slot_spec_mercs_number_sicily_muslims = 955
slot_spec_mercs_number_welsh_kern = 956
slot_spec_mercs_number_kipchak = 957
slot_spec_mercs_number_mordovians = 958
slot_spec_mercs_number_kwarezmian = 959
slot_spec_mercs_number_mongol = 960
slot_spec_mercs_number_finnish = 961
slot_spec_mercs_number_gaelic = 1032


slot_spec_mercs_number_templar = 962
slot_spec_mercs_number_hospitaller = 963
slot_spec_mercs_number_saint_lazarus = 964
slot_spec_mercs_number_santiago = 965
slot_spec_mercs_number_calatrava = 966
slot_spec_mercs_number_saint_thomas = 967
slot_spec_mercs_number_teutonic = 968
slot_spec_mercs_number_varangian = 969
slot_spec_mercs_number_mamluk = 970
slot_spec_mercs_number_cataphract = 1013


slot_spec_mercs_number_genoese_npc = 971
slot_spec_mercs_number_turkopole_npc = 972
slot_spec_mercs_number_georgian_npc = 973
slot_spec_mercs_number_cuman_npc = 974
slot_spec_mercs_number_brabantine_npc = 975
slot_spec_mercs_number_sicily_muslims_npc = 976
slot_spec_mercs_number_welsh_kern_npc = 977
slot_spec_mercs_number_kipchak_npc = 978
slot_spec_mercs_number_mordovians_npc = 979
slot_spec_mercs_number_kwarezmian_npc = 980
slot_spec_mercs_number_mongol_npc = 981
slot_spec_mercs_number_finnish_npc = 982
slot_spec_mercs_number_gaelic_npc = 1033


slot_spec_mercs_number_templar_npc = 983
slot_spec_mercs_number_hospitaller_npc = 984
slot_spec_mercs_number_saint_lazarus_npc = 985
slot_spec_mercs_number_santiago_npc = 986
slot_spec_mercs_number_calatrava_npc = 987
slot_spec_mercs_number_saint_thomas_npc = 988
slot_spec_mercs_number_teutonic_npc = 989
slot_spec_mercs_number_varangian_npc = 990
slot_spec_mercs_number_mamluk_npc = 991
# slot_spec_mercs_number_kwarezmian = 970
# slot_spec_mercs_number_mongols = 971
slot_spec_mercs_number_cataphract_npc = 1014
slot_spec_mercs_number_teutonic = 968
slot_spec_mercs_number_hospitaller = 963
slot_spec_mercs_number_templar = 962


slot_spec_mercs_genoese = 992
slot_spec_mercs_turkopole = 993
slot_spec_mercs_georgian = 994
slot_spec_mercs_cuman = 995
slot_spec_mercs_brabantine = 996
slot_spec_mercs_sicily_muslims = 997
slot_spec_mercs_welsh_kern = 998
slot_spec_mercs_kipchak = 999
slot_spec_mercs_mordovians = 1000
slot_spec_mercs_kwarezmian = 1001
slot_spec_mercs_mongol = 1002
slot_spec_mercs_finnish = 1003
slot_spec_mercs_gaelic = 1034

slot_spec_mercs_templar = 1004
slot_spec_mercs_hospitaller = 1005
slot_spec_mercs_saint_lazarus = 1006
slot_spec_mercs_santiago = 1007
slot_spec_mercs_calatrava = 1008
slot_spec_mercs_saint_thomas = 1009
slot_spec_mercs_teutonic = 1010
slot_spec_mercs_varangian = 1011
slot_spec_mercs_mamluk = 1012
slot_spec_mercs_cataphract = 1015


slot_spec_mercs_number_teutonic_aux = 1016
slot_spec_mercs_number_templar_aux = 1017
slot_spec_mercs_number_hospitaller_aux = 1018

slot_spec_mercs_number_teutonic_aux_npc = 1019
slot_spec_mercs_number_templar_aux_npc = 1020
slot_spec_mercs_number_hospitaller_aux_npc = 1021

slot_spec_mercs_teutonic_aux = 1022
slot_spec_mercs_templar_aux = 1023
slot_spec_mercs_hospitaller_aux = 1024

slot_spec_mercs_number_tournament_knights = 1030
slot_spec_mercs_number_tournament_knights_npc = 1031


################################################






######################## IMPROVEMENT COSTS
chapter_minor_teutonic_cost = 20000
chapter_minor_templar_cost = 20000
chapter_minor_hospitaller_cost = 20000
chapter_minor_saint_lazarus_cost = 15000
chapter_minor_santiago_cost = 15000
chapter_minor_calatrava_cost = 15000
chapter_minor_saint_thomas_cost = 15000
chapter_minor_teutonic_time = 24
chapter_minor_templar_time = 24
chapter_minor_hospitaller_time = 24
chapter_minor_saint_lazarus_time = 24
chapter_minor_santiago_time = 24
chapter_minor_calatrava_time = 24
chapter_minor_saint_thomas_time = 24


chapter_major_teutonic_cost = 40000
chapter_major_templar_cost = 40000
chapter_major_hospitaller_cost = 40000
chapter_major_saint_lazarus_cost = 30000
chapter_major_santiago_cost = 30000
chapter_major_calatrava_cost = 30000
chapter_major_saint_thomas_cost = 30000
chapter_major_teutonic_time = 45
chapter_major_templar_time = 45
chapter_major_hospitaller_time = 45
chapter_major_saint_lazarus_time = 45
chapter_major_santiago_time = 45
chapter_major_calatrava_time = 45
chapter_major_saint_thomas_time = 45


chapter_hq_teutonic_cost = 60000
chapter_hq_templar_cost = 60000
chapter_hq_hospitaller_cost = 60000
chapter_hq_saint_lazarus_cost = 50000
chapter_hq_santiago_cost = 50000
chapter_hq_calatrava_cost = 50000
chapter_hq_saint_thomas_cost = 50000
chapter_hq_teutonic_time = 60
chapter_hq_templar_time = 60
chapter_hq_hospitaller_time = 60
chapter_hq_saint_lazarus_time = 60
chapter_hq_santiago_time = 60
chapter_hq_calatrava_time = 60
chapter_hq_saint_thomas_time = 60


chapter_major_hq_teutonic_cost = 90000
chapter_major_hq_templar_cost = 90000
chapter_major_hq_hospitaller_cost = 90000
chapter_major_hq_teutonic_time = 90
chapter_major_hq_templar_time = 90
chapter_major_hq_hospitaller_time = 90


##### Muslim
quarters_minor_mamluk_cost = 15000
quarters_major_mamluk_cost = 30000
quarters_hq_mamluk_cost = 50000
quarters_minor_mamluk_time = 25
quarters_major_mamluk_time = 50
quarters_hq_mamluk_time = 75


######### Byzantine
quarters_major_varangian_cost = 25000
quarters_hq_varangian_cost = 40000
quarters_major_varangian_time = 25
quarters_hq_varangian_time = 50


quarters_minor_cataphract_cost = 20000
quarters_major_cataphract_cost = 35000
quarters_hq_cataphract_cost = 50000
quarters_minor_cataphract_time = 25
quarters_major_cataphract_time = 50
quarters_hq_cataphract_time = 75



######## more mobile mercs 
camp_minor_cuman_cost = 18000
camp_large_cuman_cost = 32000
camp_major_cuman_cost = 50000
camp_minor_cuman_time = 14
camp_large_cuman_time = 28
camp_major_cuman_time = 40


camp_minor_kipchak_cost = 15000
camp_large_kipchak_cost = 30000
camp_major_kipchak_cost = 45000
camp_minor_kipchak_time = 14
camp_large_kipchak_time = 28
camp_major_kipchak_time = 40


camp_minor_mongol_cost = 15000
camp_large_mongol_cost = 30000
camp_major_mongol_cost = 45000
camp_minor_mongol_time = 14
camp_large_mongol_time = 28
camp_major_mongol_time = 40


camp_minor_georgian_cost = 15000
camp_large_georgian_cost = 30000
camp_major_georgian_cost = 45000
camp_minor_georgian_time = 14
camp_large_georgian_time = 28
camp_major_georgian_time = 40


camp_minor_kwarezmian_cost = 15000
camp_large_kwarezmian_cost = 30000
camp_major_kwarezmian_cost = 45000
camp_minor_kwarezmian_time = 14
camp_large_kwarezmian_time = 28
camp_major_kwarezmian_time = 40


outpost_minor_crusader_turcopole_cost = 15000
outpost_large_crusader_turcopole_cost = 30000
outpost_major_crusader_turcopole_cost = 50000
outpost_minor_crusader_turcopole_time = 10
outpost_large_crusader_turcopole_time = 20
outpost_major_crusader_turcopole_time = 30



############ other
quarters_minor_genoese_cost = 15000
quarters_major_genoese_cost = 25000
quarters_hq_genoese_cost = 35000
quarters_minor_genoese_time = 14
quarters_major_genoese_time = 26
quarters_hq_genoese_time = 40


outpost_minor_finnish_cost = 15000
outpost_large_finnish_cost = 25000
outpost_major_finnish_cost = 35000
outpost_minor_finnish_time = 14
outpost_large_finnish_time = 26
outpost_major_finnish_time = 40


quarters_minor_brabantine_cost = 15000
quarters_major_brabantine_cost = 25000
quarters_hq_brabantine_cost = 35000
quarters_minor_brabantine_time = 14
quarters_major_brabantine_time = 26
quarters_hq_brabantine_time = 40


outpost_minor_welsh_kern_cost = 15000
outpost_large_welsh_kern_cost = 25000
outpost_major_welsh_kern_cost = 35000
outpost_minor_welsh_kern_time = 14
outpost_large_welsh_kern_time = 26
outpost_major_welsh_kern_time = 40


outpost_minor_gaelic_cost = 15000
outpost_large_gaelic_cost = 25000
outpost_major_gaelic_cost = 35000
outpost_minor_gaelic_time = 14
outpost_large_gaelic_time = 26
outpost_major_gaelic_time = 40



############# center improvements
tier_1_improved_school_cost = 15000
tier_2_university_cost = 30000
tier_1_improved_school_time = 24
tier_2_university_time = 45


tier_1_training_grounds_cost = 8000
tier_2_training_facilities_cost = 15000
tier_1_training_grounds_time = 14
tier_2_training_facilities_time = 30


tier_1_town_hall_cost = 15000
tier_2_city_hall_cost = 30000
tier_3_governors_palace_cost = 60000
tier_4_royal_palace_cost = 100000

tier_1_town_hall_time = 21
tier_2_city_hall_time = 40
tier_3_governors_palace_time = 60
tier_4_royal_palace_time = 90

tier_1_town_hall_reduce_time_costs = 5
tier_2_city_hall_reduce_time_costs = 8
tier_3_governors_palace_reduce_time_costs = 12
tier_4_royal_palace_reduce_time_costs = 15


tier_1_brothel_cost = 8000
tier_2_coaching_house_cost = 20000
tier_2_wayfarers_rest_cost = 20000
tier_3_pleasure_palace_cost = 50000
tier_1_brothel_time = 14
tier_2_coaching_house_time = 30
tier_2_wayfarers_rest_time = 30
tier_3_pleasure_palace_time = 50


tier_1_dirt_roads_cost = 10000
tier_2_paved_roads_cost = 24000
tier_1_dirt_roads_time = 24
tier_2_paved_roads_time = 50


tier_1_land_clearance_cost = 5000
tier_2_communal_farming_cost = 9000
tier_3_crop_rotation_cost = 15000
tier_4_irrigation_cost = 24000
tier_1_land_clearance_time = 7
tier_2_communal_farming_time = 18
tier_3_crop_rotation_time = 35
tier_4_irrigation_time = 50


tier_1_jousting_lists_cost = 15000
tier_2_tournament_grounds_cost = 25000
tier_1_jousting_lists_time = 30
tier_2_tournament_grounds_time = 60


# tier_1_village_guards_cost = 600
# tier_1_village_guards_time = 30


############# religious buildings
tier_1_small_church_cost = 8000
tier_1_small_masjid_cost = 8000
tier_1_small_balt_temple_cost = 8000
tier_1_small_mongol_temple_cost = 8000
tier_1_small_satan_temple_cost = 8000
tier_1_small_nordic_temple_cost = 8000
tier_1_small_church_time = 21
tier_1_small_masjid_time = 21
tier_1_small_balt_temple_time = 21
tier_1_small_mongol_temple_time = 21
tier_1_small_satan_temple_time = 21
tier_1_small_nordic_temple_time = 21


tier_2_church_cost = 15000
tier_2_masjid_cost = 15000
tier_2_balt_temple_cost = 15000
tier_2_mongol_temple_cost = 15000
tier_2_satan_temple_cost = 15000
tier_2_nordic_temple_cost = 15000
tier_2_church_time = 40
tier_2_masjid_time = 40
tier_2_balt_temple_time = 40
tier_2_mongol_temple_time = 40
tier_2_satan_temple_time = 40
tier_2_nordic_temple_time = 40


tier_3_abbey_cost = 24000
tier_3_minaret_cost = 24000
tier_3_large_balt_temple_cost = 24000
tier_3_large_mongol_temple_cost = 24000
tier_3_large_satan_temple_cost = 24000
tier_3_large_nordic_temple_cost = 24000
tier_3_abbey_time = 60
tier_3_minaret_time = 60
tier_3_large_balt_temple_time = 60
tier_3_large_mongol_temple_time = 60
tier_3_large_satan_temple_time = 60
tier_3_large_nordic_temple_time = 60



tier_4_cathedral_cost = 38000
tier_4_jama_cost = 38000
tier_4_huge_balt_temple_cost = 38000
tier_4_huge_mongol_temple_cost = 38000
tier_4_huge_satan_temple_cost = 38000
tier_4_huge_nordic_temple_cost = 38000
tier_4_cathedral_time = 90
tier_4_jama_time = 90
tier_4_huge_balt_temple_time = 90
tier_4_huge_mongol_temple_time = 90
tier_4_huge_satan_temple_time = 90
tier_4_huge_nordic_temple_time = 90



tier_5_huge_cathedral_cost = 60000
tier_5_great_jama_cost = 60000
tier_5_great_temple_of_dievas_cost = 60000
tier_5_great_temple_of_tengri_cost = 60000
tier_5_great_synagogue_of_satan_cost = 60000
tier_5_great_temple_of_odin_cost = 60000
tier_5_huge_cathedral_time = 120
tier_5_great_jama_time = 120
tier_5_great_temple_of_dievas_time = 120
tier_5_great_temple_of_tengri_time = 120
tier_5_great_synagogue_of_satan_time = 120
tier_5_great_temple_of_odin_time = 120
######################

 
tier_1_masons_guild_cost = 8000
tier_2_master_masons_guild_cost = 16000
tier_3_masons_guild_hq_cost = 25000

tier_1_masons_guild_time = 14
tier_2_master_masons_guild_time = 25
tier_3_masons_guild_hq_time = 40

tier_1_masons_guild_cost_time_reduction = 10
tier_2_master_masons_guild_cost_time_reduction = 15
tier_3_masons_guild_hq_cost_time_reduction = 20


tier_1_fairground_cost = 10000
tier_2_great_market_cost = 20000
tier_3_merchants_quarter_cost = 35000

tier_1_fairground_time = 14
tier_2_great_market_time = 30
tier_3_merchants_quarter_time = 50

tier_1_fairground_increase_income = 10
tier_2_great_market_increase_income = 20
tier_3_merchants_quarter_increase_income = 30

tier_1_fairground_increase_merchant_gold = 1500
tier_2_great_market_increase_merchant_gold = 3000
tier_3_merchants_quarter_increase_merchant_gold = 5000


tier_1_mines_cost = 8000
tier_2_mining_network_cost = 20000

tier_1_mines_time = 30
tier_2_mining_network_time = 60

tier_1_mines_pop_divider = 50
tier_2_mining_network_pop_divider = 25


tier_1_mercenary_quarters_cost = 12000
tier_2_mercenary_hq_cost = 25000
tier_1_mercenary_quarters_time = 15
tier_2_mercenary_hq_time = 30


tier_1_garrison_quarters_cost = 10000
tier_2_drill_square_cost = 18000
tier_3_barracks_cost = 32000
tier_4_armoury_cost = 50000
tier_1_garrison_quarters_time = 21
tier_2_drill_square_time = 40
tier_3_barracks_time = 60
tier_4_armoury_time = 90


tier_1_merchants_guild_cost = 12000
tier_2_master_merchants_guild_cost = 20000
tier_3_merchants_guild_hq_cost = 32000
tier_1_merchants_guild_time = 21
tier_2_master_merchants_guild_time = 40
tier_3_merchants_guild_hq_time = 60

tier_1_merchants_guild_income_increase = 5
tier_2_master_merchants_guild_income_increase = 10
tier_3_merchants_guild_hq_income_increase = 15

tier_1_merchants_guild_trade_price_decrease = 6
tier_2_master_merchants_guild_trade_price_decrease = 7
tier_3_merchants_guild_hq_trade_price_decrease = 8

tier_1_merchants_guild_enterprise_income_increase = 20
tier_2_master_merchants_guild_enterprise_income_increase = 35
tier_3_merchants_guild_hq_enterprise_income_increase = 50

# tier_1_merchants_guild_enterprise_max = 5
# tier_2_master_merchants_guild_enterprise_max = 10
# tier_3_merchants_guild_hq_enterprise_max = 15


tier_1_small_hospital_cost = 8000
tier_2_hospital_cost = 14000
tier_3_college_of_surgeons_cost = 30000
tier_1_small_bimaristan_cost = 6000
tier_2_bimaristan_cost = 10000
tier_3_great_bimaristan_cost = 20000
tier_1_small_hospital_time = 18
tier_2_hospital_time = 30
tier_3_college_of_surgeons_time = 45
tier_1_small_bimaristan_time = 15
tier_2_bimaristan_time = 25
tier_3_great_bimaristan_time = 40


tier_1_siege_works_cost = 12000
tier_2_great_siege_works_cost = 20000
tier_1_siege_works_time = 30
tier_2_great_siege_works_time = 45


tier_1_merchants_wharf_cost = 20000
tier_2_warehouse_cost = 35000
tier_3_docklands_cost = 60000
tier_1_merchants_wharf_time = 30
tier_2_warehouse_time = 70
tier_3_docklands_time = 120
tier_1_merchants_wharf_income_increase = 15
tier_2_warehouse_income_increase = 25
tier_3_docklands_income_increase = 40


# tier_1_small_chapel_cost = 720
# tier_2_chapel_cost = 721
# tier_1_small_chapel_time = 720
# tier_2_chapel_time = 721


tier_1_sewers_cost = 20000
tier_2_improved_sewers_cost = 40000
tier_1_sewers_time = 60
tier_2_improved_sewers_time = 90


# tier_1_town_plumbers_cost = 740
tier_2_city_plumbing_quarters_cost = 8000
# tier_1_town_plumbers_time = 740
tier_2_city_plumbing_quarters_time = 14


tier_1_village_council_hall_cost = 8000
tier_1_village_council_hall_time = 14
tier_1_village_council_hall_reduction_costs_time = 20


tier_1_housing_town_cost = 50000
tier_2_housing_town_cost = 80000
tier_3_housing_town_cost = 120000
tier_4_housing_town_cost = 150000
tier_5_housing_town_cost = 180000
tier_6_housing_town_cost = 210000
tier_7_housing_town_cost = 270000
tier_8_housing_town_cost = 360000
tier_1_housing_town_time = 50
tier_2_housing_town_time = 50
tier_3_housing_town_time = 60
tier_4_housing_town_time = 90
tier_5_housing_town_time = 90
tier_6_housing_town_time = 90
tier_7_housing_town_time = 120
tier_8_housing_town_time = 150


tier_1_housing_castle_cost = 20000
tier_2_housing_castle_cost = 30000
tier_3_housing_castle_cost = 50000
tier_4_housing_castle_cost = 60000
tier_5_housing_castle_cost = 80000
tier_1_housing_castle_time = 30
tier_2_housing_castle_time = 40
tier_3_housing_castle_time = 50
tier_4_housing_castle_time = 50
tier_5_housing_castle_time = 60


tier_1_housing_village_cost = 5000
tier_2_housing_village_cost = 10000
tier_3_housing_village_cost = 15000
tier_4_housing_village_cost = 20000
tier_5_housing_village_cost = 30000
tier_1_housing_village_time = 20
tier_2_housing_village_time = 30
tier_3_housing_village_time = 40
tier_4_housing_village_time = 50
tier_5_housing_village_time = 60

########################



#######################
# battle_ratio_multiple = 7000
# max_morale = 35000
# max_ratio = max_morale/2
# initial_morale = 10000

# slot_agent_courage_score_bonus      = 27
# slot_agent_rank_depth              = 28
# slot_agent_rank_closeness          = 29
########################



############## NEW PARTY TYPE SLOTS
slot_faction_party_type_count_forager = 500
slot_faction_party_type_count_scout = 501
slot_faction_party_type_count_patrol = 502
slot_faction_party_type_count_kingdom_caravan = 503
slot_faction_party_type_count_prisoner_train = 504
slot_faction_party_type_count_war_party = 505
slot_faction_party_type_count_mercenary_company = 506
########################


############## 
slot_faction_player_original_template_faction = 250
########################






######################## NEW v2.1 - Floris diplomacy 
##diplomacy start+
#Treaty lengths.  Use these constants instead of "magic numbers" to make it
#obvious what code is supposed to do, and also make it easy to change the
#lengths without having to go through the entire mod.

# Truces (as exist in Native)
dplmc_treaty_truce_days_initial    = 20 
dplmc_treaty_truce_days_expire     =  0

#Trade treaties convert to truces after 20 days.
dplmc_treaty_trade_days_initial    = 40
dplmc_treaty_trade_days_expire     = dplmc_treaty_truce_days_initial

#Defensive alliances convert to trade treaties after 20 days.
dplmc_treaty_defense_days_initial  = 60
dplmc_treaty_defense_days_expire   = dplmc_treaty_trade_days_initial

#Alliances convert to defensive alliances after 20 days.
dplmc_treaty_alliance_days_initial = 80 
dplmc_treaty_alliance_days_expire  = dplmc_treaty_defense_days_initial

#Define these by name to make them more clear in the source code.
#They should not be altered from their definitions.
dplmc_treaty_truce_days_half_done = (dplmc_treaty_truce_days_initial + dplmc_treaty_truce_days_expire) // 2
dplmc_treaty_trade_days_half_done = (dplmc_treaty_trade_days_initial + dplmc_treaty_trade_days_expire) // 2
dplmc_treaty_defense_days_half_done = (dplmc_treaty_defense_days_initial + dplmc_treaty_defense_days_expire) // 2
dplmc_treaty_alliance_days_half_done = (dplmc_treaty_alliance_days_initial + dplmc_treaty_alliance_days_expire) // 2

##diplomacy end+

#########################################################



################### NEW v2.1 - HORSE FALL MODIFIERS
rider_fall_default_chance_of_damage = 70
rider_fall_default_damage_min = 60
rider_fall_default_damage_max = 80
rider_fall_chance_of_damage_reduction_by_level_of_riding = 5
rider_fall_damage_reduction_by_level_of_riding = 7
#########################################################





################## NEW v2.1 
npc_cultures_begin = "fac_culture_finnish"
npc_cultures_end = "fac_player_faction"

npc_cultures_begin_1 = "fac_culture_finnish"
npc_cultures_end_1 = "fac_culture_templar"

npc_cultures_begin_2 = "fac_culture_templar"
npc_cultures_end_2 = "fac_culture_player"
##########################################









########### NEW v3.0 - role variables
role_none = 0
role_adventurer = 1
role_bandit = 2
role_mercenary_captain = 3
role_vassal = 4
role_prince = 5
role_king = 6
######################

# modmerger_start version=201 type=1
try:
    from util_common import logger
    from modmerger_options import mods_active
    modcomp_name = "constants"
    for mod_name in mods_active:
        try:
            logger.info("Importing constants from mod \"%s\"..."%(mod_name))
            code = "from %s_constants import *" % mod_name
            exec code
        except ImportError:
            errstring = "Component \"%s\" not found for mod \"%s\"." % (modcomp_name, mod_name)
            logger.debug(errstring)
except:
    raise
# modmerger_end
