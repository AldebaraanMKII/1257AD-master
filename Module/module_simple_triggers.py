from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *
from header_terrain_types import *


####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


simple_triggers = [

  ######### (1,
  ######### [
    ######### (str_store_troop_name, s1, "trp_player"),

    ######### (str_store_string, s0, "@Lord"),    
    ###########(str_store_string, s1, "@Thomas"),    
    ######### (troop_set_name, "trp_player", "@{s0} the {s1}"),
  ######### ]
  ######### ),


#### This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead
  (ti_on_party_encounter,
   [
    ]),


#### This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead
  (ti_simulate_battle,
   [
    ]),

####### NEW v2.9-KOMKE START- this trigger commented out, no longer necessary due to later trigger, (see NEW v2.9-KOMKE)
  # (1,
  #  [
  #     ######### rafi what's this?
  #     ######### (try_begin),
  #       ######### (eq, "$training_ground_position_changed", 0),
  #       ######### (assign, "$training_ground_position_changed", 1),
  #       ######### (position_set_x, pos0, 7050),
  #       ######### (position_set_y, pos0, 7200),
  #       ######### (party_set_position, "p_training_ground_3", pos0),
  #     ######### (try_end),
  # 
  #     (gt, "$auto_besiege_town",0),
  #     (gt, "$g_player_besiege_town", 0),
  #     (ge, "$g_siege_method", 1),
  #     (store_current_hours, ":cur_hours"),
  #     (eq, "$g_siege_force_wait", 0),
  #     (ge, ":cur_hours", "$g_siege_method_finish_hours"),
  #     (neg|is_currently_night),
  #     (rest_for_hours, 0, 0, 0), ######stop resting
  #   ]),
####### NEW v2.9-KOMKE END- 
  (0,
   [
      (try_begin),
        (eq, "$bug_fix_version", 0),

        ######fix for hiding test_scene in older savegames
        (disable_party, "p_test_scene"),
        ######fix for correcting town_1 siege type
        ######(party_set_slot, "p_town_1", slot_center_siege_with_belfry, 0),
        ######fix for hiding player_faction notes
        (faction_set_note_available, "fac_player_faction", 0),
        ######fix for hiding faction 0 notes
        (faction_set_note_available, "fac_no_faction", 0),
        ######fix for removing kidnapped girl from party
        (try_begin),
          (neg|check_quest_active, "qst_kidnapped_girl"),
          (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
        (try_end),
        ######fix for not occupied but belong to a faction lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
          (troop_slot_eq, ":cur_troop", slot_troop_is_alive, 1),
            (try_begin),
              (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_inactive),
              (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
              (is_between, ":cur_troop_faction", "fac_kingdom_1", kingdoms_end),
              (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (try_end),
        (try_end),
        ######fix for an error in 1.105, also fills new slot values
        (call_script, "script_initialize_item_info"),

        (assign, "$bug_fix_version", 1),
      (try_end),

      (eq, "$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),

#Auto-menu
  (0,
   [
     (try_begin),
       (gt, "$g_last_rest_center", 0),
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), ######stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge, "$auto_menu",1),
         (jump_to_menu, "$auto_menu"),
         (assign, "$auto_menu",-1),
       (else_try),
         (ge, "$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
       ######### (else_try),        ########### Comment out this entire else_try
         ######### (ge, "$auto_besiege_town",1),
         ######### (start_encounter, "$auto_besiege_town"),
       (else_try),
         (ge, "$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_infinite_camping", 0),
         (assign, "$g_player_icon_state", pis_normal),

         (rest_for_hours, 0, 0, 0), ######stop camping

         (display_message, "@Breaking camp..."),
       (try_end),
     (try_end),
     ]),

####### NEW v2.9-KOMKE this trigger makes the previous no longer necessary(see NEW v2.9-KOMKE)
(0.25,
   [
      (gt, "$auto_besiege_town",0),
      (gt, "$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
   
      (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance / 2),
        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You have broken off your siege of {s1}."),
        (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
        (assign, "$g_player_besiege_town", -1),
        (rest_for_hours, 0, 0, 0), ######stop resting - abort
      (else_try),
        (ge, ":distance", raid_distance / 3),
        (map_free),
        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You cannot maintain your siege of {s1} from this distance. You risk your lines breaking."),
      (else_try),
        (eq, "$g_siege_force_wait", 0),####### NEW v2.9-KOMKE if it's waiting 24 hours don't stop (force wait 1)
        (store_current_hours, ":cur_hours"),
        (ge, ":cur_hours", "$g_siege_method_finish_hours"),
        (neg|is_currently_night),
        (rest_for_hours, 0, 0, 0), ######stop resting, if resting
        (start_encounter, "$auto_besiege_town"),
      (try_end),
]), 

#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
     (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
     (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (jump_to_menu, ":menu_type"),
     (assign, ":end_cond", 2),
     (try_for_range, ":cur_slot", 1, ":end_cond"),
       (try_begin),
         (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
         (val_add, ":end_cond", 1),
       (try_end),
       (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
       (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
     (try_end),
    ]),

  ######Music,
  (3,
   [
    (map_free),         
      (try_begin),        
        (call_script, "script_music_set_situation_with_culture", mtf_sit_travel), 
        ###### (try_begin),
          ###### (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            ###### (store_faction_of_party, ":center_faction", ":center_no"),
            ###### (store_faction_of_party, ":party_faction", "p_main_party"),
            ###### (store_relation, ":cur_relation", ":party_faction", ":center_faction"),
            ###### (try_begin),
              ###### (lt, ":cur_relation", 0),
                ###### (store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
                ###### (lt, ":dist", 10), ######moto chief changes
                  ###### (display_message, "@Entering enemy territory, your party moves more warily.!",0xFFFFAAAA),
                  ###### (call_script, "script_music_set_situation_with_culture", mtf_hostile_teritory), 
            ###### (try_end),
        ###### (try_end),
      (try_end),
      ######(call_script, "script_music_set_situation_with_culture", mtf_sit_travel), 
      
      ######### modded2x disable this:
       ######### TOM, this is not relevant right now
      ###### (call_script, "script_get_closest_center", "p_main_party"),
      ###### (party_get_slot, ":orig_faction", reg0, slot_center_original_faction),
      
      ######TOM
      ###### (music_set_situation, mtf_sit_travel),
      ###### (try_begin),
        ###### (this_or_next |eq, ":orig_faction", "fac_kingdom_20"),
        ###### (this_or_next |eq, ":orig_faction", "fac_kingdom_25"),
        ###### (this_or_next |eq, ":orig_faction", "fac_kingdom_28"),
        ###### (eq, ":orig_faction", "fac_kingdom_31"),
        ###### (music_set_culture, mtf_tom_saracen),
      ###### (else_try),
        ###### (this_or_next |eq, ":orig_faction", "fac_kingdom_28"),
        ###### (eq, ":orig_faction", "fac_kingdom_31"),
        ###### (music_set_culture, mtf_tom_rus),
      ###### (else_try),
        ###### (this_or_next |eq, ":orig_faction", "fac_kingdom_3"),
        ###### (eq, ":orig_faction", "fac_kingdom_27"),
        ###### (music_set_culture, mtf_tom_mong),  
      ###### (else_try),
        ###### (this_or_next | eq, ":orig_faction", "fac_kingdom_4"),
        ###### (this_or_next | eq, ":orig_faction", "fac_kingdom_11"),
        ###### (this_or_next | eq, ":orig_faction", "fac_kingdom_2"),
        ###### (eq, ":orig_faction", "fac_kingdom_14"),
        ###### (music_set_culture, mtf_tom_baltic), 
      ###### (else_try),
        ###### (music_set_culture, mtf_tom_euro),          
      ###### (try_end),
      
      ######tom - rafi original start
      ######### (try_begin),
        ######### (try_begin),
          ######### (this_or_next |eq, ":orig_faction", "fac_kingdom_20"),
          ######### (this_or_next |eq, ":orig_faction", "fac_kingdom_25"),
          ######### (this_or_next |eq, ":orig_faction", "fac_kingdom_28"),
          ######### (eq, ":orig_faction", "fac_kingdom_31"),
          ######### (music_set_situation, mtf_sit_travel),
          ######### (music_set_culture, mtf_culture_saracen),
        ######### (else_try),
          ######### (this_or_next |eq, ":orig_faction", "fac_kingdom_1"),
          ######### (eq, ":orig_faction", "fac_kingdom_23"),
          ######### (music_set_situation, mtf_sit_travel),
          ######### (music_set_culture, mtf_culture_crusader),
        ######### (else_try),
          ######### (this_or_next |eq, ":orig_faction", "fac_kingdom_3"),
          ######### (eq, ":orig_faction", "fac_kingdom_27"),
          ######### (music_set_situation, mtf_culture_mongol),
        ######### (else_try),
          ######### (eq, ":orig_faction", "fac_kingdom_2"),
          ######### (music_set_situation, mtf_culture_baltic),
        ######### (else_try),
          ######### (eq, ":orig_faction", "fac_kingdom_10"),
          ######### (music_set_situation, mtf_culture_france),
        ######### (else_try),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_4"),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_11"),
          ######### (eq, ":orig_faction", "fac_kingdom_14"),
          ######### (music_set_situation, mtf_culture_nordic),
        ######### (else_try),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_8"),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_15"),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_29"),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_30"),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_26"),
          ######### (eq, ":orig_faction", "fac_kingdom_22"),
          ######### (music_set_situation, mtf_sit_travel),
          ######### (music_set_culture, mtf_culture_byzantine),
        ######### (else_try),
          ######### (eq, ":orig_faction", "fac_kingdom_6"),    
          ######### (music_set_situation, mtf_culture_hre),
        ######### (else_try),
          ######### (this_or_next | eq, ":orig_faction", "fac_kingdom_7"),
          ######### (eq, ":orig_faction", "fac_kingdom_5"),    
          ######### (music_set_situation, mtf_sit_travel),
          ######### (music_set_culture, mtf_culture_poland),
        ######### (else_try),
          ######### (music_set_situation, mtf_sit_travel),
          ######### (music_set_culture, mtf_culture_generic),
        ######### (try_end),
      ######### (try_end),
     ######tom - rafi original end
        ]),

  (0,
    [
      ######escort caravan quest auto dialog trigger
      (try_begin),
        (eq, "$caravan_escort_state", 1),
        (party_is_active, "$caravan_escort_party_id"),

        (store_distance_to_party_from_party, ":caravan_distance_to_destination", "$caravan_escort_destination_town", "$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_destination", 2),

        (store_distance_to_party_from_party, ":caravan_distance_to_player", "p_main_party", "$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_player", 5),

        (assign, "$talk_context", tc_party_encounter),
        (assign, "$g_encountered_party", "$caravan_escort_party_id"),
        (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
        (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),

        (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
      (try_end),

        (try_begin),
            (gt, "$g_reset_mission_participation", 1),

            (try_for_range, ":troop", active_npcs_begin, kingdom_ladies_end),
                (troop_set_slot, ":troop", slot_troop_mission_participation, 0),
            (try_end),
        (try_end),
    ]),

(24,
[   ######this was an unused trigger for some strange religion thing - tom
    (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
    (eq, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
    (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),

    (store_current_hours, ":cur_hours"),
    (faction_get_slot, ":fest_hours", "$players_kingdom", slot_faction_ai_current_state_started),
    (val_sub, ":cur_hours", ":fest_hours"),
    (gt, ":cur_hours", 24*7), ######ongoing for a week?
    (call_script, "script_faction_conclude_feast", "$players_kingdom", sfai_feast),
    (display_message, "@Your kingdoms feast have concluded."),
    ######tom
    
    ######### (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
      ######### (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),

      ######### (store_sub, ":divisor", 140, "$player_right_to_rule"),
      ######### (val_div, ":divisor", 14),
      ######### (val_max, ":divisor", 1),

      ######### (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), ######10 is the base, down to 2 for 100 rtr
      ######### (val_sub, ":faction_morale", ":faction_morale_div_10"),

      ######### (faction_set_slot, ":kingdom_no",  slot_faction_morale_of_player_troops, ":faction_morale"),

      ######### rafi
      ######### (faction_set_slot, "fac_kingdom_2",  slot_faction_religion, religion_pagan),
      ######### (faction_get_slot, ":religion", ":kingdom_no",  slot_faction_religion),
      ######### (faction_get_slot, ":player_religion", "$players_kingdom",  slot_faction_religion),

      ######### (try_begin),
        ######### (eq, ":religion", religion_muslim),
        ######### (eq, ":player_religion", religion_catholic),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_muslim),
        ######### (eq, ":religion", religion_catholic),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":religion", religion_pagan),
        ######### (eq, ":player_religion", religion_catholic),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_pagan),
        ######### (eq, ":religion", religion_catholic),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":religion", religion_orthodox),
        ######### (eq, ":player_religion", religion_catholic),
        ######### (assign, ":faction_morale", -500),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_orthodox),
        ######### (eq, ":religion", religion_catholic),
        ######### (assign, ":faction_morale", -500),
      ######### ######### orthodox
      ######### (else_try),
        ######### (eq, ":religion", religion_muslim),
        ######### (eq, ":player_religion", religion_orthodox),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_muslim),
        ######### (eq, ":religion", religion_orthodox),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":religion", religion_pagan),
        ######### (eq, ":player_religion", religion_orthodox),
        ######### (assign, ":faction_morale", -1000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_pagan),
        ######### (eq, ":religion", religion_orthodox),
        ######### (assign, ":faction_morale", -1000),
      ######### ######### muslim
      ######### (else_try),
        ######### (eq, ":religion", religion_pagan),
        ######### (eq, ":player_religion", religion_muslim),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_pagan),
        ######### (eq, ":religion", religion_muslim),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":religion", religion_orthodox),
        ######### (eq, ":player_religion", religion_muslim),
        ######### (assign, ":faction_morale", -1500),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_orthodox),
        ######### (eq, ":religion", religion_muslim),
        ######### (assign, ":faction_morale", -1500),
      ######### ######### pagan
      ######### (else_try),
        ######### (eq, ":religion", religion_muslim),
        ######### (eq, ":player_religion", religion_pagan),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_muslim),
        ######### (eq, ":religion", religion_pagan),
        ######### (assign, ":faction_morale", -2000),
      ######### (else_try),
        ######### (eq, ":religion", religion_orthodox),
        ######### (eq, ":player_religion", religion_pagan),
        ######### (assign, ":faction_morale", -1000),
      ######### (else_try),
        ######### (eq, ":player_religion", religion_orthodox),
        ######### (eq, ":religion", religion_pagan),
        ######### (assign, ":faction_morale", -1000),
      ######### (else_try),
        ######### (assign, ":faction_morale", 0),
      ######### (try_end),

      ######### (str_store_faction_name, s25, ":kingdom_no"),
      ######### (assign, reg25, ":faction_morale"),
      ######### (assign, reg26, ":religion"),
      ######### (assign, reg27, ":player_religion"),
      ######### (display_message, "@morale for {s25} is {reg25} kingdom religion {reg26} player religion {reg27}"),
      ######### (faction_set_slot, ":kingdom_no",  slot_faction_morale_of_player_troops, ":faction_morale"),
    ######### (try_end),
]),


 ######### (4, ######Locate kingdom ladies
   ######### (6, ######Locate kingdom ladies
    ######### [
      ################change location for all ladies
      ######### (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        ######### (neg|troop_slot_ge, ":troop_id", slot_troop_prisoner_of_party, 0),
        ######### (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
        ######### (assign, ":location", reg1),
        ######### (troop_set_slot, ":troop_id", slot_troop_cur_center, ":location"),
      ######### (try_end),
    ######### ]),


############### NEW v1.8 - 06/10/2018 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
(0.057, ######Locate kingdom ladies - once every 24 hours for each of the 420 ladies
[
 (try_begin),
   (lt, "$g_locate_ladies_cur_lady", kingdom_ladies_begin), 
   (assign, "$g_locate_ladies_cur_lady", kingdom_ladies_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_locate_ladies_cur_lady", kingdom_ladies_end), 
   (assign, "$g_locate_ladies_cur_lady", kingdom_ladies_begin),
 (try_end),
 
 ######change location for ONE lady
 (neg|troop_slot_ge, "$g_locate_ladies_cur_lady", slot_troop_prisoner_of_party, 0),
   (call_script, "script_get_kingdom_lady_social_determinants", "$g_locate_ladies_cur_lady"),
   (assign, ":location", reg1),
   (troop_set_slot, "$g_locate_ladies_cur_lady", slot_troop_cur_center, ":location"),
 
   ############# proceeds to the next lady when it's triggered again
   (val_add, "$g_locate_ladies_cur_lady", 1),
]),
####################################################












 ######### (2, ######Error check for multiple parties on the map
    ######### [
    ######### (eq, "$cheat_mode", 1),
    ######### (assign, ":debug_menu_noted", 0),
    ######### (try_for_parties, ":party_no"),
        ######### (gt, ":party_no", "p_spawn_points_end"),
        ######### (party_stack_get_troop_id, ":commander", ":party_no", 0),
        ######### (is_between, ":commander", active_npcs_begin, active_npcs_end),
        ######### (troop_get_slot, ":commander_party", ":commander", slot_troop_leaded_party),
        ######### (neq, ":party_no", ":commander_party"),
        ######### (assign, reg4, ":party_no"),
        ######### (assign, reg5, ":commander_party"),

        ######### (str_store_troop_name, s3, ":commander"),
        ######### (display_message, "@{!}{s3} commander of party ######{reg4} which is not his troop_leaded party {reg5}"),
        ######### (str_store_string, s65, "str_party_with_commander_mismatch__check_log_for_details_"),

        ######### (try_begin),
            ######### (eq, ":debug_menu_noted", 0),
            ######### (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
            ######### (assign, ":debug_menu_noted", 1),
        ######### (try_end),
    ######### (try_end),
    ######### ]),


 (24, ######Kingdom ladies send messages
 [
    (try_begin),
        (neg|check_quest_active, "qst_visit_lady"),
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
        (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),

        (assign, ":lady_not_visited_longest_time", -1),
        (assign, ":longest_time_without_visit", 120), ######five days

        (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),

            ######set up message for ladies the player is courting
            (troop_slot_ge, ":troop_id", slot_troop_met, 2),
            (neg|troop_slot_eq, ":troop_id", slot_troop_met, 4),

            (troop_slot_eq, ":troop_id", slot_lady_no_messages, 0),
            (troop_slot_eq, ":troop_id", slot_troop_spouse, -1),

            (troop_get_slot, ":location", ":troop_id", slot_troop_cur_center),
            (is_between, ":location", walled_centers_begin, walled_centers_end),
            (call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
            (gt, reg0, 1),

            (store_current_hours, ":hours_since_last_visit"),
            (troop_get_slot, ":last_visit_hour", ":troop_id", slot_troop_last_talk_time),
            (val_sub, ":hours_since_last_visit", ":last_visit_hour"),

            (gt, ":hours_since_last_visit", ":longest_time_without_visit"),
            (assign, ":longest_time_without_visit", ":hours_since_last_visit"),
            (assign, ":lady_not_visited_longest_time", ":troop_id"),
            (assign, ":visit_lady_location", ":location"),

        (try_end),

        (try_begin),
            (gt, ":lady_not_visited_longest_time", 0),
            (call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
        (try_end),

    (try_end),
    ]),


#Player raiding a village
#### This trigger will check if player's raid has been completed and will lead control to village menu.
  (1,
   [
      (ge, "$g_player_raiding_village",1),
      (try_begin),
        (neq, "$g_player_is_captive", 0),
        ######(rest_for_hours, 0, 0, 0), ######stop resting - abort
        (assign, "$g_player_raiding_village",0),
      ######### (else_try),          ########Remove this entire Else-Try###
        ######### (map_free), ######we have been attacked during raid
        ######### (assign, "$g_player_raiding_village",0),
      (else_try),
        (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
        (start_encounter, "$g_player_raiding_village"),
        (rest_for_hours, 0),
        (assign, "$g_player_raiding_village",0),
        (assign, "$g_player_raid_complete",1),
      (else_try),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
        ######(rest_for_hours, 3, 5, 1), ######rest while attackable
        ######### rafi
        (rest_for_hours_interactive, 3, 3, 1), ######rest while attackable  ########CHANGE rest_for_hours to rest_for_hours_interactive; ########OPTIONAL COMMENT OUT
        ######### end
      (else_try),
        (rest_for_hours, 0, 0, 0), ######stop resting - abort
        (assign, "$g_player_raiding_village",0),
        (assign, "$g_player_raid_complete",0),
      (try_end),
    ]),
    
(0.25,
   [
      (ge, "$g_player_raiding_village",1),
      (store_distance_to_party_from_party, ":distance", "$g_player_raiding_village", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance),
        (str_store_party_name_link, s1, "$g_player_raiding_village"),
        (display_message, "@You have broken off your raid of {s1}."),
        (call_script, "script_village_set_state", "$current_town", 0),
        (party_set_slot, "$current_town", slot_village_raided_by, -1),
        (assign, "$g_player_raiding_village", 0),
        (rest_for_hours, 0, 0, 0), ######stop resting - abort
      (else_try),
        (ge, ":distance", raid_distance / 2),
        (map_free),
        (jump_to_menu, "mnu_village_loot_continue"),
      (try_end),
]),  
    
#Pay day.
(168,
[ 
################## NEW v1.9 - fixes presentation being displayed a few hours after game start
 (try_begin),
   (eq, "$do_once_budget_presentation", 0),
     (assign, "$do_once_budget_presentation", 1),
     (store_current_hours, "$g_last_payday"),
 (else_try),
   (eq, "$do_once_budget_presentation", 1),
##############
     (assign, "$g_presentation_lines_to_display_begin", 0),
     (assign, "$g_presentation_lines_to_display_end", 15),
     (assign, "$g_apply_budget_report_to_gold", 1),
     (store_current_hours, "$g_last_payday"),
     (try_begin),
       (this_or_next|eq, "$g_infinite_camping", 0),           ####################### NEW v1.9 - bugfix
       (eq, "$freelancer_state", 1),           ####################### NEW v1.9 - bugfix
	   ####### NEW v3.0 - report doesn't display if the player is the only one in the party and cheat menu is on
       (try_begin),
         (eq, "$cheat_mode", 1),
	       (party_get_num_companions, ":num_troops", "p_main_party"),           
           (gt, ":num_troops", 1),           
       (else_try),
         (start_presentation, "prsnt_budget_report"),
       (try_end),
	   ##############
         #######diplomacy begin
         (try_begin),
           (gt, "$g_player_debt_to_party_members", 5000),
           (call_script, "script_add_notification_menu", "mnu_dplmc_deserters",20,0),
         (try_end),
     (try_end),
 (try_end),
]),
################################################################################



  ######### Oath fulfilled -- ie, mercenary contract expired?
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),
      (eq, "$freelancer_state", 0),  ############# NEW v2.8 - fix the menu appearing when player is in freelancer

      (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),

      ######A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
      (assign, ":player_has_marriage_in_faction", 0),
      (try_begin),
        (is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
        (store_faction_of_troop, ":spouse_faction", ":player_spouse"),
        (eq, ":spouse_faction", "$players_kingdom"),
        (assign, ":player_has_marriage_in_faction", 1),
      (try_end),
      (eq, ":player_has_marriage_in_faction", 0),

      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  ######### Reducing luck by 1 in every 180 hours
  ######### (180,
   ######### [
     ######### (val_sub, "$g_player_luck", 1),
     ######### (val_max, "$g_player_luck", 0),
    ######### ]),

    ######courtship reset
  (72,
   [
     (assign, "$lady_flirtation_location", 0),
    ]),

    ######reset time to spare
  (4,
   [
     (assign, "$g_time_to_spare", 1),

    (try_begin),
        (troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
        (assign, "$g_player_banner_granted", 1),
    (try_end),

    ]),


  ######### Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
    (le, "$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
####    (start_presentation, "prsnt_custom_banner"),
    ]),

  ######### Party Morale: Move morale towards target value.
  (24,
   [
      (call_script, "script_get_player_party_morale_values"),

      (assign, ":target_morale", reg0),
      (party_get_morale, ":cur_morale", "p_main_party"),
      (store_sub, ":dif", ":target_morale", ":cur_morale"),
      (store_div, ":dif_to_add", ":dif", 5),
      (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
      (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
          (gt, ":dif", 0),
          (val_add, ":dif_to_add", 1),
        (else_try),
          (val_sub, ":dif_to_add", 1),
        (try_end),
      (try_end),
      (val_add, ":cur_morale", ":dif_to_add"),
      (party_set_morale, "p_main_party", ":cur_morale"),
    ]),


    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#Party AI: pruning some of the prisoners in each center (once a week)
#### (168,
(0.54,       #################### once a week for each of the 311 walled centers
[
 (try_begin),
   (eq, "$g_prison_culling", 0),
   (try_begin),
     (lt, "$g_prison_culling_cur_center", walled_centers_begin), 
     (assign, "$g_prison_culling_cur_center", walled_centers_begin),
   (try_end),
   
   (try_begin),
     (ge, "$g_prison_culling_cur_center", walled_centers_end), 
     (assign, "$g_prison_culling_cur_center", walled_centers_begin),
   (try_end),
   
   (try_begin),
     (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "$g_prison_culling_cur_center"),
######################## NEW VC CODE
     (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
       (party_prisoner_stack_get_troop_id, ":stack_troop", "$g_prison_culling_cur_center", ":stack_no"),
       (neg|troop_is_hero, ":stack_troop"),
         (party_prisoner_stack_get_size, ":stack_size", "$g_prison_culling_cur_center", ":stack_no"),
         (gt, ":stack_size", 0),
           ################ NEW FROM script_sell_all_prisoners
           (call_script, "script_game_get_prisoner_price", ":stack_troop"),
           (assign, ":sell_price", reg0),
           #############
           (store_random_in_range, ":rand_no", 10, 60),#changed from 0..40
           (val_mul, ":stack_size", ":rand_no"),
           (val_div, ":stack_size", 100),
           (try_begin),
             (eq, ":stack_size", 0),
             (val_add, ":stack_size", 1),
           (try_end),
           (party_get_slot, ":cur_wealth", "$g_prison_culling_cur_center", slot_town_wealth),
           (store_mul, ":prisoner_sell", ":stack_size", ":sell_price"), ############# NEW: multiplies stack by value obtained by script_game_get_prisoner_price above
           (val_add, ":cur_wealth", ":prisoner_sell"),
           (party_set_slot, "$g_prison_culling_cur_center", slot_town_wealth, ":cur_wealth"),
           (party_remove_prisoners, "$g_prison_culling_cur_center", ":stack_troop", ":stack_size"),
     (try_end),
###############################################
   (try_end),
   ################ proceeds to the next center when it's triggered again
   (val_add, "$g_prison_culling_cur_center", 1),
   
   ################### DEBUG
   (val_add, "$g_simple_trigger_fire_count_1", 1),
 (try_end),
]),
###########################################################################################




################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#Adding net incomes to heroes (once a week)
#Increasing debts to heroes by 1% (once a week)
#Adding net incomes to centers (once a week) ######tom: this system is too unpredictable, do not do
#### (168,
(0.195,  #################### once a week for each of the 558 active npcs + 300 random lords
[
 ######### (try_for_range, ":center_no", centers_begin, centers_end),
  ######### (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
  ######### (neq, ":town_lord", "trp_player"),
  ######### (is_between, ":town_lord", active_npcs_begin, active_npcs_end),
  ######### (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
  ######### (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
  ######### (troop_get_slot, ":troop_wealth", ":town_lord", slot_troop_wealth),
  ######### (val_add, ":troop_wealth", ":accumulated_rents"),
  ######### (val_add, ":troop_wealth", ":accumulated_tariffs"),
  ######### (troop_set_slot, ":town_lord", slot_troop_wealth, ":troop_wealth"),                
  ######### (party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
  ######### (party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
  ######### (try_begin),
    ######### (eq, "$cheat_mode", 1),
    ######### (assign, reg1, ":troop_wealth"),
    ######### (add_troop_note_from_sreg, ":town_lord", 1, "str_current_wealth_reg1", 0),
  ######### (try_end),
 ######### (try_end),
 (try_begin),
   (lt, "$g_calculate_weekly_income_cur_npc", active_npcs_begin), 
   (assign, "$g_calculate_weekly_income_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_calculate_weekly_income_cur_npc", active_npcs_end), 
   (assign, "$g_calculate_weekly_income_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (troop_slot_eq, "$g_calculate_weekly_income_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (troop_get_slot, ":cur_debt", "$g_calculate_weekly_income_cur_npc", slot_troop_player_debt),#Increasing debt
     (val_mul, ":cur_debt", 101),
     (val_div, ":cur_debt", 100),
     (troop_set_slot, "$g_calculate_weekly_income_cur_npc", slot_troop_player_debt, ":cur_debt"),
     (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", "$g_calculate_weekly_income_cur_npc"),#Adding net income
 (try_end),
 
 ################ proceeds to the next npc when it's triggered again
 (val_add, "$g_calculate_weekly_income_cur_npc", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_2", 1),
]),
####################################################################################

  ######Hiring men with hero wealths (once a day)
  ######Hiring men with center wealths (once a day)
  ######### (24, 
   ######### [

#this is moved up from below , from a 24 x 15 slot to a 24 slot
    ########TOM PROSPERITY
     ######### (try_for_range, ":center_no", centers_begin, centers_end),
       ######### ######(neg|is_between, ":center_no", castles_begin, castles_end),
       ######### (store_random_in_range, ":random", 0, 30),
       ######### (le, ":random", 10),
       
       ######### (call_script, "script_get_center_ideal_prosperity", ":center_no"),
       ######### (assign, ":ideal_prosperity", reg0),
       ######### (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),       
       ######### (try_begin),
         ######### (eq, ":random", 0), ######with 3% probability it will gain +10/-10 prosperity even it has higher prosperity than its ideal prosperity.
         ######### (try_begin),
           ######### (store_random_in_range, ":random", 0, 2),
           ######### (try_begin),
             ######### (eq, ":random", 0),
             ######### (neg|is_between, ":center_no", castles_begin, castles_end), ######castles always gain positive prosperity from surprise income to balance their prosperity.
             ######### (call_script, "script_change_center_prosperity", ":center_no", -10),
             ######### (val_add, "$newglob_total_prosperity_from_convergence", -10),
           ######### (else_try),     
             ######### (call_script, "script_change_center_prosperity", ":center_no", 10),
             ######### (val_add, "$newglob_total_prosperity_from_convergence", 10),
           ######### (try_end),
         ######### (try_end),
       ######### (else_try),
         ######### (gt, ":prosperity", ":ideal_prosperity"),         
         ######### (call_script, "script_change_center_prosperity", ":center_no", -1),
         ######### (val_add, "$newglob_total_prosperity_from_convergence", -1),
       ######### (else_try),
         ######### (lt, ":prosperity", ":ideal_prosperity"),         
         ######### (call_script, "script_change_center_prosperity", ":center_no", 1),
         ######### (val_add, "$newglob_total_prosperity_from_convergence", 1),
       ######### (try_end),
     ######### (try_end),
###TOM PROSPERITY     
    ######### ]),

  ######Converging center prosperity to ideal prosperity once in every 15 days
  ######### (24*15,
   ######### [#(try_for_range, ":center_no", centers_begin, centers_end),
    #########  (call_script, "script_get_center_ideal_prosperity", ":center_no"),
    #########  (assign, ":ideal_prosperity", reg0),
    #########  (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    #########  (try_begin),
    #########    (gt, ":prosperity", ":ideal_prosperity"),
    #########    (call_script, "script_change_center_prosperity", ":center_no", -1),
    #########  (else_try),
    #########    (lt, ":prosperity", ":ideal_prosperity"),
    #########    (call_script, "script_change_center_prosperity", ":center_no", 1),
    #########  (try_end),
    ######(try_end),
    ######### ]),

  ######Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), ######half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (ge, "$g_last_rest_center", 0),
      (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),

#diplomatic indices
  ######### (2, ######TOM WAS 1
    ######### [
      ######(neq, "$g_recalculate_ais", 1), ######tom - why is this here?

      ######(display_message, "@diplomatic indices start...", 0xff0000),

      ######(str_store_faction_name, s25, "$g_diplo_kingdom"),
      ######(display_message, "@--DEBUG-- processing {s25}", 0xff0000),

      ######(assign, ":faction_1", "$g_diplo_kingdom"),



       #######(try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),

      ######### (try_begin),
        ########(neq, ":faction_1", kingdoms_begin),
        ######### (faction_slot_eq, ":faction_1", slot_faction_state, sfs_active),
        ######### (try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
          ######### (neq, ":faction_1", ":faction_2"),
          ######### (faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),

          #######remove provocations
          ######### (store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
          ######### (val_sub, ":slot_truce_days", kingdoms_begin),
          ######### (faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
          ######### (try_begin),
            ######### (ge, ":truce_days", 1),
            ######### (try_begin),
              ######### (eq, ":truce_days", 1),
              ######### (call_script, "script_update_faction_notes", ":faction_1"),
              ######### (lt, ":faction_1", ":faction_2"),
              ######### (call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"),
            ######### (try_end),
            ######### (val_sub, ":truce_days", 1),
            ######### (faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
          ######### (try_end),

          ######### (store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
          ######### (val_sub, ":slot_provocation_days", kingdoms_begin),
          ######### (faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
          ######### (try_begin),
            ######### (ge, ":provocation_days", 1),
            ######### (try_begin),#factions already at war
              ######### (store_relation, ":relation", ":faction_1", ":faction_2"),
              ######### (lt, ":relation", 0),
              ######### (faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
            ######### (else_try), ######Provocation expires
              ######### (eq, ":provocation_days", 1),
              ######### (call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"),
              ######### (faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
            ######### (else_try),
              ######### (val_sub, ":provocation_days", 1),
              ######### (faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
            ######### (try_end),
          ######### (try_end),

          ######### (try_begin), ######at war
            ######### (store_relation, ":relation", ":faction_1", ":faction_2"),
            ######### (lt, ":relation", 0),
            ######### (store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
            ######### (val_sub, ":slot_war_damage", kingdoms_begin),
            ######### (faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
            ######### (val_add, ":war_damage", 1),
            ######### (faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
          ######### (try_end),

        ######### (try_end),
        ######### (call_script, "script_update_faction_notes", ":faction_1"),
      ######### (try_end),


      ######(display_message, "@diplomatic indices end...", 0x00ff00),
    ######### ]
  ######### ),

  
  
  
  
######################## This trigger has been split up. The other half is in the new trigger below.
# (24,  
(8,  ######## NEW v2.6 - 3x more incidents
[
 ##################(display_message, "@incidents start...", 0xff0000),
 (try_begin),
   (call_script, "script_raf_create_incidents"),
   (assign, ":acting_village", reg0),
   (assign, ":target_village", reg1),
   (gt, ":acting_village", 0),
   (gt, ":target_village", 0),
   (store_faction_of_party, ":acting_faction", ":acting_village"),
   (store_faction_of_party, ":target_faction", ":target_village"), ######target faction receives the provocation
   (neq, ":acting_village", ":target_village"),
   (neq, ":acting_faction", ":target_faction"),
     (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
     (eq, reg0, 0),
     
     (try_begin),
       (party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),
         (call_script, "script_create_incidents_new", ":acting_village", -1),
     (else_try),
       (party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),
         (call_script, "script_create_incidents_new", ":acting_village", -1),
     (else_try),
       (set_fixed_point_multiplier, 1),
       (store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
       (lt, ":distance", 25),
         (call_script, "script_create_incidents_new", ":acting_village", ":target_village"),
     (try_end),
 (try_end),
]),
###############################################################
  
  
  
  
  
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### (24,
(0.328,  ################## Once a day for each of the factions + player faction
[   
 (try_begin),
   (lt, "$g_update_faction_notes_cur_fac", kingdoms_begin), 
   (assign, "$g_update_faction_notes_cur_fac", kingdoms_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_update_faction_notes_cur_fac", kingdoms_end), 
   (assign, "$g_update_faction_notes_cur_fac", kingdoms_begin),
 (try_end),
 
 (try_begin),
   (faction_slot_eq, "$g_update_faction_notes_cur_fac", slot_faction_state, sfs_active),
   (try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
     (neq, "$g_update_faction_notes_cur_fac", ":faction_2"),
     (faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),
 
     ########remove provocations
     (store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
     (val_sub, ":slot_truce_days", kingdoms_begin),
     (faction_get_slot, ":truce_days", "$g_update_faction_notes_cur_fac", ":slot_truce_days"),
     (try_begin),
       (ge, ":truce_days", 1),
       (try_begin),
         (eq, ":truce_days", 1),
         (call_script, "script_update_faction_notes", "$g_update_faction_notes_cur_fac"),
         (lt, "$g_update_faction_notes_cur_fac", ":faction_2"),
         ################### NEW v1.9
         (try_begin),
           (this_or_next|eq, "$g_update_faction_notes_cur_fac", "$players_kingdom"),
           (eq, ":faction_2", "$players_kingdom"),
             (call_script, "script_add_notification_menu", "mnu_notification_truce_expired", "$g_update_faction_notes_cur_fac", ":faction_2"),
         (else_try),
           (str_store_faction_name, s1, "$g_update_faction_notes_cur_fac"),
           (str_store_faction_name, s2, ":faction_2"),
           (display_log_message, "@The truce between {s1} and {s2} has expired."),
         (try_end),
     
       (try_end),
       (val_sub, ":truce_days", 1),
       (faction_set_slot, "$g_update_faction_notes_cur_fac", ":slot_truce_days", ":truce_days"),
     (try_end),
 
     (store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
     (val_sub, ":slot_provocation_days", kingdoms_begin),
     (faction_get_slot, ":provocation_days", "$g_update_faction_notes_cur_fac", ":slot_provocation_days"),
     (try_begin),
       (ge, ":provocation_days", 1),
       (try_begin),#factions already at war
         (store_relation, ":relation", "$g_update_faction_notes_cur_fac", ":faction_2"),
         (lt, ":relation", 0),
         (faction_set_slot, "$g_update_faction_notes_cur_fac", ":slot_provocation_days", 0),
       (else_try), ######Provocation expires
         (eq, ":provocation_days", 1),
         ################### NEW v1.9
         (try_begin),
           (this_or_next|eq, "$g_update_faction_notes_cur_fac", "$players_kingdom"),
           (eq, ":faction_2", "$players_kingdom"),
             (call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", "$g_update_faction_notes_cur_fac", ":faction_2"),
         (else_try),
           (str_store_faction_name, s1, "$g_update_faction_notes_cur_fac"),
           (str_store_faction_name, s2, ":faction_2"),
           (faction_get_slot, ":faction_leader", "$g_update_faction_notes_cur_fac", slot_faction_leader),
           (str_store_troop_name, s3, ":faction_leader"),
           (troop_get_type, reg4, ":faction_leader"),
           (display_log_message, "@The {s1} has not responded to the {s2}'s provocations, and {s3} suffers a loss of face among {reg4?her:his} more bellicose subjects...."),
         (try_end),
         (faction_set_slot, "$g_update_faction_notes_cur_fac", ":slot_provocation_days", 0),
       (else_try),
         (val_sub, ":provocation_days", 1),
         (faction_set_slot, "$g_update_faction_notes_cur_fac", ":slot_provocation_days", ":provocation_days"),
       (try_end),
     (try_end),
 
     (try_begin), ######at war
       (store_relation, ":relation", "$g_update_faction_notes_cur_fac", ":faction_2"),
       (lt, ":relation", 0),
       (store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
       (val_sub, ":slot_war_damage", kingdoms_begin),
       (faction_get_slot, ":war_damage", "$g_update_faction_notes_cur_fac", ":slot_war_damage"),
       (val_add, ":war_damage", 1),
       (faction_set_slot, "$g_update_faction_notes_cur_fac", ":slot_war_damage", ":war_damage"),
     (try_end),
 
   (try_end),
   (call_script, "script_update_faction_notes", "$g_update_faction_notes_cur_fac"),
 (try_end),
 
 ################ proceeds to the next faction when it's triggered again
 (val_add, "$g_update_faction_notes_cur_fac", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_3", 1),
]),
##########################################################################################

    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Give some xp to hero parties
#### (24,
(0.028,   ################### Once a day for each of the 858 lord parties
[ 
 (try_begin),
   (eq, "$g_party_npc_trainer", 1),
   (try_begin),
     (lt, "$g_daily_training_cur_lord", active_npcs_begin), ############ NEW v2.1 - fix - now companions and king parties are considered
     (assign, "$g_daily_training_cur_lord", active_npcs_begin),
   (try_end),
   
   (try_begin),
     (ge, "$g_daily_training_cur_lord", active_npcs_end), 
     (assign, "$g_daily_training_cur_lord", active_npcs_begin),
   (try_end),
   
   (try_begin),
     (troop_slot_eq, "$g_daily_training_cur_lord", slot_troop_is_alive, 1),
     (troop_slot_eq, "$g_daily_training_cur_lord", slot_troop_occupation, slto_kingdom_hero),  ######### must be a lord
       (troop_get_slot, ":hero_party", "$g_daily_training_cur_lord", slot_troop_leaded_party),
       (gt, ":hero_party", centers_end),
         (party_is_active, ":hero_party"),
         (call_script, "script_party_daily_training", ":hero_party"),
   (try_end),
   ################ proceeds to the next lord when it's triggered again
   (val_add, "$g_daily_training_cur_lord", 1),
   
   ################### DEBUG
   (val_add, "$g_simple_trigger_fire_count_4", 1),
 (try_end),
]),
##########################################################################################

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Give some xp to centers
#### (24,
(0.07,   ################### Once a day for each of the 311 walled centers
[ 
 (try_begin),
   (eq, "$g_party_npc_trainer", 1),
   (try_begin),
     (lt, "$g_daily_training_cur_center", walled_centers_begin), 
     (assign, "$g_daily_training_cur_center", walled_centers_begin),
   (try_end),
   
   (try_begin),
     (ge, "$g_daily_training_cur_center", walled_centers_end), 
     (assign, "$g_daily_training_cur_center", walled_centers_begin),
   (try_end),
   
   (try_begin),
     ######### Uncomment lines below if you want player's center not be upgraded just like native #######
     ######(party_get_slot, ":center_lord", ":center_no", slot_town_lord),
     ######(neq, ":center_lord", "trp_player"),   
     #############################################################
     (party_slot_eq, "$g_daily_training_cur_center", slot_center_is_besieged_by, -1),           ######### if not being besieged, besieged castle no time to train..
     (call_script, "script_party_daily_training", "$g_daily_training_cur_center"),
   (try_end),
   ############### proceeds to the next center when it's triggered again
   (val_add, "$g_daily_training_cur_center", 1),
   
   ################### DEBUG
   (val_add, "$g_simple_trigger_fire_count_5", 1),
 (try_end),
]),
###########################################################################

      
      
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Process sieges
#### (24,
(0.07, ################ once a day for each of the 311 centers
[
 (try_begin),
   (lt, "$g_process_sieges_cur_center", walled_centers_begin), 
   (assign, "$g_process_sieges_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_process_sieges_cur_center", walled_centers_end), 
   (assign, "$g_process_sieges_cur_center", walled_centers_begin),
 (try_end),
 
 (call_script, "script_process_sieges", "$g_process_sieges_cur_center"),
 
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_process_sieges_cur_center", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_6", 1),
]),
###########################################################################
    
    
    
    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
### Process village raids
### (4,
(0.033,        ########################### once every 2 hours for each of the 423 villages - execute script 7 times
[
 (try_begin),
   (lt, "$g_process_village_raids_cur_village", villages_begin), 
   (assign, "$g_process_village_raids_cur_village", villages_begin),
 (try_end),

 (try_begin),
   (ge, "$g_process_village_raids_cur_village", villages_end), 
   (assign, "$g_process_village_raids_cur_village", villages_begin),
 (try_end),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
 
 (call_script, "script_process_village_raids", "$g_process_village_raids_cur_village"),
 ############## proceeds to the next village 
 (val_add, "$g_process_village_raids_cur_village", 1),
    
 ################# DEBUG
 (val_add, "$g_simple_trigger_fire_count_7", 5),
]),
 
 ###### Process village raids
 ###### (2,
   ###### [
     ###### (call_script, "script_process_village_raids"),
 ###### ]),
###########################################################################




  ######### Decide vassal ai
   ######### (7,
##################### this only calculate party strength now - moved to $g_recalculate_ais_cur_fac simple trigger
   ######### (1,
    ######### [
      ######### (display_message, "@vassal AI start...", 0xff0000),
      ######### (call_script, "script_init_ai_calculation"),
      ######(call_script, "script_decide_kingdom_party_ais"),
      ######### (display_message, "@vassal AI end...", 0x00ff00),
      ######### ]),
########################################################################

##################### Now it's in $g_recalculate_ais_cur_fac simple trigger
   ######### (7,
    ######### [
      ######### (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        ######### (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        ######### (call_script, "script_calculate_troop_ai", ":troop_no"),
      ######### (try_end),
      ######### ]),
########################################################################



########################################################
(24, ######tom made - 1257 utilities
[
 ######walker variables update
 (assign, "$men_are_pleased", 0),
 #######centre culture changes
]),
########################################################

  ######### Hold regular marshall elections for players_kingdom
  ######### (24, ######Disabled in favor of new system
   ######### [
    #########  (val_add, "$g_election_date", 1),
    #########  (ge, "$g_election_date", 90), ######elections holds once in every 90 days.
    #########  (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
    #########  (neq, "$players_kingdom", "fac_player_supporters_faction"),
    #########  (assign, "$g_presentation_input", -1),
    #########  (assign, "$g_presentation_marshall_selection_1_vote", 0),
    #########  (assign, "$g_presentation_marshall_selection_2_vote", 0),

    #########  (assign, "$g_presentation_marshall_selection_max_renown_1", -10000),
    #########  (assign, "$g_presentation_marshall_selection_max_renown_2", -10000),
    #########  (assign, "$g_presentation_marshall_selection_max_renown_3", -10000),
    #########  (assign, "$g_presentation_marshall_selection_max_renown_1_troop", -10000),
    #########  (assign, "$g_presentation_marshall_selection_max_renown_2_troop", -10000),
    #########  (assign, "$g_presentation_marshall_selection_max_renown_3_troop", -10000),
    #########  (assign, ":num_men", 0),
    #########  (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
    #########    (assign, ":cur_troop", ":loop_var"),
    #########    (assign, ":continue", 0),
    #########    (try_begin),
    #########      (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
    #########      (assign, ":cur_troop", "trp_player"),
    #########      (try_begin),
    #########        (eq, "$g_player_is_captive", 0),
    #########        (assign, ":continue", 1),
    #########      (try_end),
    #########    (else_try),
#          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
 #########         (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
 #########         (eq, "$players_kingdom", ":cur_troop_faction"),
  #########        ######(troop_slot_eq, ":cur_troop", slot_troop_is_prisoner, 0),
  #########        (neg|troop_slot_ge, ":cur_troop", slot_troop_prisoner_of_party, 0),
   #########       (troop_slot_ge, ":cur_troop", slot_troop_leaded_party, 1),
    #########      (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
    #########      (neg|faction_slot_eq, ":cur_troop_faction", slot_faction_leader, ":cur_troop"),
    #########      (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
    #########      (gt, ":cur_party", 0),
    #########      (party_is_active, ":cur_party"),
    #########      (call_script, "script_party_count_fit_for_battle", ":cur_party"),
    #########      (assign, ":party_fit_for_battle", reg0),
    #########      (call_script, "script_party_get_ideal_size", ":cur_party"),
    #########      (assign, ":ideal_size", reg0),
    #########      (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
    #########      (val_div, ":relative_strength", ":ideal_size"),
    #########      (ge, ":relative_strength", 25),
    #########      (assign, ":continue", 1),
    #########    (try_end),
    #########    (eq, ":continue", 1),
    #########    (val_add, ":num_men", 1),
    #########    (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
    #########    (try_begin),
    #########      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_1"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_1"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_1", ":renown"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_1_troop"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_1_troop", ":cur_troop"),
    #########    (else_try),
    #########      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_2"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_2", ":renown"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", ":cur_troop"),
    #########    (else_try),
    #########      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_3"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3", ":renown"),
    #########      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", ":cur_troop"),
    #########    (try_end),
    #########  (try_end),
    #########  (ge, "$g_presentation_marshall_selection_max_renown_1_troop", 0),
    #########  (ge, "$g_presentation_marshall_selection_max_renown_2_troop", 0),
    #########  (ge, "$g_presentation_marshall_selection_max_renown_3_troop", 0),
    #########  (gt, ":num_men", 2), ######at least 1 voter
    #########  (assign, "$g_election_date", 0),
    #########  (assign, "$g_presentation_marshall_selection_ended", 0),
    #########  (try_begin),
    #########    (neq, "$g_presentation_marshall_selection_max_renown_1_troop", "trp_player"),
    #########    (neq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
    #########    (start_presentation, "prsnt_marshall_selection"),
    #########  (else_try),
    #########    (jump_to_menu, "mnu_marshall_selection_candidate_ask"),
    #########  (try_end),
   #########   ]),#
   
   
   
   
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################## splitted in half - this is for npcs
#### (24,
(0.028,  ############ once a day for each of the 858 lords
[
 (try_begin),
   (lt, "$g_recalculate_controversy_cur_npc", active_npcs_begin), 
     (assign, "$g_recalculate_controversy_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_recalculate_controversy_cur_npc", active_npcs_end), 
     (assign, "$g_recalculate_controversy_cur_npc", active_npcs_begin),
 (try_end),
   
 (try_begin),
   (troop_slot_eq, "$g_recalculate_controversy_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (troop_get_slot, ":impatience", "$g_recalculate_controversy_cur_npc", slot_troop_intrigue_impatience),
     (val_sub, ":impatience", 5),
     (val_max, ":impatience", 0),
     (troop_set_slot, "$g_recalculate_controversy_cur_npc", slot_troop_intrigue_impatience, ":impatience"),
 (try_end),
 
 (store_random_in_range, ":controversy_deduction", 1, 3),
 (val_min, ":controversy_deduction", 2),
 #####################(assign, ":controversy_deduction", 1),
 
 #####################This reduces controversy by one each round
 (try_begin),
   (troop_get_slot, ":controversy", "$g_recalculate_controversy_cur_npc", slot_troop_controversy),
   (ge, ":controversy", 1),
     (val_sub, ":controversy", ":controversy_deduction"),
     (val_max, ":controversy", 0),
     (troop_set_slot, "$g_recalculate_controversy_cur_npc", slot_troop_controversy, ":controversy"),
 (try_end),
 
 ################ proceeds to the next NPC when it's triggered again
 (val_add, "$g_recalculate_controversy_cur_npc", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_8", 1),
]),
###############

################## other half - this is for the player
(24,  ############ once a day
[
 (store_random_in_range, ":controversy_deduction", 1, 3),
 (val_min, ":controversy_deduction", 2),
 (troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
 (val_sub, ":controversy", ":controversy_deduction"),
 (val_max, ":controversy", 0),
 (troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
]),
###########################################################################




    
    ######POLITICAL TRIGGERS
    ######POLITICAL TRIGGER ######1`
   ######### rafi slowing this down (8, ######increased from 12
   (6, ######TOM was 6
    [
      ######(display_message, "@random political event start...", 0xff0000),
      (call_script, "script_cf_random_political_event"),
      ######Added Nov 2010 begins - do this twice
      (call_script, "script_cf_random_political_event"),
      ######Added Nov 2010 ends
    
      ######(display_message, "@random political event end...", 0xff0000),
      ######This generates quarrels and occasional reconciliations and interventions
    ]),

#Individual lord political calculations
#Check for lords without fiefs, auto-defections, etc
#(0.5, rafi slowing this down
(0.5,
[
 (val_add, "$g_lord_long_term_count", 1),
 (try_begin),
   (neg|is_between, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
   (assign, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin"),
 (try_end),

 (assign, ":troop_no", "$g_lord_long_term_count"),
 
 (try_begin),
   (eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),    
   (assign, ":troop_no", "trp_player"),
 (try_end),

 (try_begin),
   (eq, "$cheat_mode", 1),
   (str_store_troop_name, s9, ":troop_no"),
   (display_message, "@{!}DEBUG -- Doing political calculations for {s9}"),
 (try_end),
 
 ######Penalty for no fief
 (try_begin),
   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ####### NEW v2.7 - fixes bug where random lords that didn't spawn yet got angry at the player for not having a fief. This happens because the no faction (id: 0) doesn't have a leader so it the slot is assigned to 0 in the game start. And 0 is the player.
   (neq, ":troop_no", "trp_player"),
   (assign, ":fief_found", -1),
   (try_for_range, ":center", centers_begin, centers_end),
     (party_slot_eq, ":center", slot_town_lord, ":troop_no"),
     (assign, ":fief_found", ":center"),
   (try_end),
 
   (try_begin),
     (eq, ":fief_found", -1),
     (store_faction_of_troop, ":original_faction", ":troop_no"),
     (faction_get_slot, ":faction_leader", ":original_faction", slot_faction_leader),
     (troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
####################################### NEW v1.8 - pay compensation to vassals instead of losing relations
     (try_begin),
       (neq, ":faction_leader", ":troop_no"),
       (try_begin),
         (eq, "$g_landless_vassals_compensation", 1),
         (eq, ":faction_leader", "trp_player"),
            (assign, ":cost_orig", 2000),
         (assign, ":cost", ":cost_orig"),
         (try_begin),
           (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
           (store_mul, ":cost_reduction_percent", ":player_persuasion_skill", 4),
           (assign, ":cost_temp", ":cost_orig"),
           (val_div, ":cost_temp", 100),
           (val_mul, ":cost_temp", ":cost_reduction_percent"),
           (val_sub, ":cost", ":cost_temp"),
         (try_end),
         
         (try_begin),
           (call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
           (assign, ":cur_relation", reg0),
           (gt, ":cur_relation", 0),
             (store_div, ":cost_reduction_percent", ":cur_relation", 5),
             (assign, ":cost_temp", ":cost_orig"),
             (val_div, ":cost_temp", 100),
             (val_mul, ":cost_temp", ":cost_reduction_percent"),
             (val_sub, ":cost", ":cost_temp"),
         (try_end),
         
         (assign, reg17, ":cost"),

         (store_troop_gold, ":cur_gold", "trp_household_possessions"),
         (ge, ":cur_gold", reg17),
           (call_script, "script_dplmc_withdraw_from_treasury", reg17),
           ######### (troop_remove_gold, "trp_player", reg17),
           (troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
           (val_add, ":cur_wealth", reg17),
           (troop_set_slot, ":troop_no", slot_troop_wealth, ":cur_wealth"),
           (str_store_troop_name_link, s1, ":troop_no"),
           (display_message, "@{reg17} coins were withdraw from your treasury to pay for {s1}'s compensation.", 0x7D7DFF),
           (assign, "$g_no_money_for_compensation", 0),
           
       (else_try),
         (eq, "$g_landless_vassals_compensation", 1),
         (eq, ":faction_leader", "trp_player"),
           (store_troop_gold, ":cur_gold", "trp_household_possessions"),
           (lt, ":cur_gold", reg17),
           (display_message, "@You didn't have the {reg17} coins in the treasury to pay for {s1}'s compensation. Thus you suffer a relation hit!", 0xFF1A1A),
           (assign, "$g_no_money_for_compensation", 1),
           
       (else_try),
         (this_or_next|eq, "$g_landless_vassals_compensation", 0),
         (this_or_next|neq, ":faction_leader", "trp_player"),                  
         (eq, "$g_no_money_for_compensation", 1),
         (this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
         (this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
         (this_or_next|eq, ":troop_reputation", lrep_cunning),
         (eq, ":troop_reputation", lrep_debauched),
           (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -4),
           (val_add, "$total_no_fief_changes", -4),
           
         (try_begin),
           (eq, ":faction_leader", "trp_player"),                  
           (eq, "$g_no_money_for_compensation", 0),
             (str_store_troop_name_link, s1, ":troop_no"),
             (display_message, "@{s1} is angry at you for not having a fief!", 0xFF1A1A),
         (else_try),
           (eq, ":faction_leader", "trp_player"),                  
           (eq, "$g_no_money_for_compensation", 1),
             (assign, "$g_no_money_for_compensation", 0),
         (try_end),

       (else_try),
         (this_or_next|eq, "$g_landless_vassals_compensation", 0),
         (this_or_next|neq, ":faction_leader", "trp_player"),                  
         (eq, "$g_no_money_for_compensation", 1),
         (eq, ":troop_reputation", lrep_martial),
           (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2),
           (val_add, "$total_no_fief_changes", -2),
         (try_begin),
           (eq, ":faction_leader", "trp_player"),                  
           (eq, "$g_no_money_for_compensation", 0),
             (str_store_troop_name_link, s1, ":troop_no"),
             (display_message, "@{s1} is angry at you for not having a fief!", 0xFF1A1A),
         (else_try),
           (eq, ":faction_leader", "trp_player"),                  
           (eq, "$g_no_money_for_compensation", 1),
             (assign, "$g_no_money_for_compensation", 0),
         (try_end),
       (try_end),

####################################################################################################################
     (try_end),
   (try_end),
 (try_end),    
       
 ######Auto-indictment or defection
 (try_begin),
   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   (eq, ":troop_no", "trp_player"),        
   (try_begin),
     (eq, ":troop_no", "trp_player"),
     (assign, ":faction", "$players_kingdom"),
   (else_try),
     (store_faction_of_troop, ":faction", ":troop_no"),
   (try_end),

   (faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
   (neq, ":troop_no", ":faction_leader"),
     
   ######I don't know why these are necessary, but they appear to be
   (neg|is_between, ":troop_no", "trp_kingdom_1_lord", "trp_knight_1_1"),
   (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
   
   (assign, ":num_centers", 0),          
   (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),            
     (store_faction_of_party, ":faction_of_center", ":cur_center"),
     (eq, ":faction_of_center", ":faction"),            
     (val_add, ":num_centers", 1),
   (try_end),

   ######we are counting num_centers to allow defection although there is high relation between faction leader and troop. 
   ######but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
   (try_begin), 
     (this_or_next|eq, ":faction", "$players_kingdom"),
     (eq, ":faction", "fac_player_supporters_faction"),
     (val_add, ":num_centers", 1),
   (try_end),
     
   (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
   ###### (this_or_next|le, reg0, -50), ######was -75
   (this_or_next|le, reg0, -50),  ######## NEW v1.0 - was -30 but since civil wars are also -30 i changed this to -50 (the lord can't take it anymore and there's not enough people to start a rebellion)
   (eq, ":num_centers", 0), ######if there is no walled centers that faction has defection happens 100%.

   (call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), ######Should include battle, prisoner, in a castle with others 
   (store_random_in_range, ":who_moves_first", 0, 2),
     
   (try_begin),
     (this_or_next|eq, ":num_centers", 0), ######Thanks Caba`drin & Osviux
     (neq, ":who_moves_first", 0),
     (neq, ":troop_no", "trp_player"),
         
     ######do a defection
     (try_begin), 
       (neq, ":num_centers", 0), 
       (assign, "$g_give_advantage_to_original_faction", 1), 
     (try_end),
     ######(assign, "$g_give_advantage_to_original_faction", 1),
 
     (store_faction_of_troop, ":orig_faction", ":troop_no"),
     (call_script, "script_lord_find_alternative_faction", ":troop_no"),
     (assign, ":new_faction", reg0),            
     (assign, "$g_give_advantage_to_original_faction", 0),
     (try_begin),
       (neq, ":new_faction", ":orig_faction"),              
     
       (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
       (str_store_troop_name_link, s1, ":troop_no"),
       (str_store_faction_name_link, s2, ":new_faction"),    
       (str_store_faction_name_link, s3, ":faction"),
       (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
       (try_begin),
         (ge, "$cheat_mode", 1),
         (str_store_troop_name, s4, ":troop_no"),
         (display_message, "@{!}DEBUG - {s4} faction changed in defection"), 
       (try_end),    
       (troop_get_type, reg4, ":troop_no"),
       (str_store_string, s4, "str_lord_defects_ordinary"),
       (display_log_message, "@{!}{s4}"),
       ##################### NEW v2.1 - faction statistics
       (faction_get_slot, ":cur_slot_value", ":faction", slot_faction_lords_lost_defection),
       (val_add, ":cur_slot_value", 1),
       (faction_set_slot, ":faction", slot_faction_lords_lost_defection, ":cur_slot_value"),
       #####################
       (try_begin),
         (eq, "$cheat_mode", 1),
         (this_or_next|eq, ":new_faction", "$players_kingdom"),
         (eq, ":faction", "$players_kingdom"),
         (call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
       (try_end),                
     (try_end),
   (else_try),    
     (neq, ":faction_leader", "trp_player"),
     (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
     (le, reg0, -60), ######was -75
     (call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
   (try_end),          
 (else_try),  ######Take a stand on an issue
   (neq, ":troop_no", "trp_player"),
   (store_faction_of_troop, ":faction", ":troop_no"),
   (faction_slot_ge, ":faction", slot_faction_political_issue, 1),
   ######This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway            
   (neg|troop_slot_ge, ":troop_no", slot_troop_stance_on_faction_issue, 1), 
   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_stance_on_faction_issue, -1),
   (neq, "$players_kingdom", ":faction"),
   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   (call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
   (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, reg0),
 (try_end),

 (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
   (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ####### he's alive/active
   (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
   (lt, reg0, 0),
   (assign, ":relation", reg0),
   (store_sub, ":chance_of_convergence", 0, ":relation"),
   (store_random_in_range, ":random", 0, 300),
   (lt, ":random", ":chance_of_convergence"),
   (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
   (val_add, "$total_relation_changes_through_convergence", 1),
 (try_end),        
]),
########################################################################



#TEMPORARILY DISABLED, AS READINESS IS NOW A PRODUCT OF NPC_DECISION_CHECKLIST
  ######### Changing readiness to join army
####   (10,
 #########   [
 #########     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#        (eq, 1, 0),
#        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
####        (assign, ":modifier", 1),
####        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
####        (try_begin),
####          (gt, ":party_no", 0),
####          (party_get_slot, ":commander_party", ":party_no", slot_party_commander_party),
####          (ge, ":commander_party", 0),
####          (store_faction_of_party, ":faction_no", ":party_no"),
####          (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
####          (ge, ":faction_marshall", 0),
####          (troop_get_slot, ":marshall_party", ":faction_marshall", slot_troop_leaded_party),
####          (eq, ":commander_party", ":marshall_party"),
####          (assign, ":modifier", -1),
####        (try_end),
####        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_join_army),
####        (val_add, ":readiness", ":modifier"),
####        (val_clamp, ":readiness", 0, 100),
####        (troop_set_slot, ":troop_no", slot_troop_readiness_to_join_army, ":readiness"),
####        (assign, ":modifier", 1),
####        (try_begin),
####          (gt, ":party_no", 0),
####          (store_troop_faction, ":troop_faction", ":troop_no"),
####          (eq, ":troop_faction", "fac_player_supporters_faction"),
####          (neg|troop_slot_eq, ":troop_no", slot_troop_player_order_state, spai_undefined),
####          (party_get_slot, ":party_ai_state", ":party_no", slot_party_ai_state),
####          (party_get_slot, ":party_ai_object", ":party_no", slot_party_ai_object),
####          ######Check if party is following player orders
####          (try_begin),
####            (troop_slot_eq, ":troop_no", slot_troop_player_order_state, ":party_ai_state"),
####            (troop_slot_eq, ":troop_no", slot_troop_player_order_object, ":party_ai_object"),
####            (assign, ":modifier", -1),
####          (else_try),
####            ######Leaving following player orders if the current party order is not the same.
####            (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
####            (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
####          (try_end),
####        (try_end),
####        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_follow_orders),
####        (val_add, ":readiness", ":modifier"),
####        (val_clamp, ":readiness", 0, 100),
####        (troop_set_slot, ":troop_no", slot_troop_readiness_to_follow_orders, ":readiness"),
####        (try_begin),
####          (lt, ":readiness", 10),
####          (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
####          (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
####        (try_end),
####      (try_end),
 #########     ]),

  ######### Process vassal ai 
  ######(2,
    ######[
     ######(call_script, "script_process_kingdom_parties_ai"), ######moved to below trigger (per 1 hour) in order to allow it processed more frequent.
    ######]),

  ######### Process alarms - perhaps break this down into several groups, with a modula
  ######### raf was 1
   ######### (0.1, ######this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
   ######### [
      ######(neq, "$g_recalculate_ais", 1),

      ######(display_message, "@process alarms start...", 0xff0000),
      ######(call_script, "script_process_alarms"),
      ######(display_message, "@script_process_alarms end...", 0x00ff00),
    ######### ]),
    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
##tom made - new trigger for alarms. they will react only to sieges/raids and will be more effective in response.
#### (3,
(0.024,     #################### once every 3 hours for each of the 733 centers / execute script 6 times to achieve this
[
 (try_begin),
   (lt, "$g_process_alarms_cur_center", centers_begin), 
   (assign, "$g_process_alarms_cur_center", centers_begin),
 (try_end),

 (try_begin),
   (ge, "$g_process_alarms_cur_center", centers_end), 
   (assign, "$g_process_alarms_cur_center", centers_begin),
 (try_end),

 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
                 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
                 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
                 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
                 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
                 
 (try_begin), ######if raided, sieged and only once!
   (this_or_next|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
   (party_slot_eq, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1), ######if this is not set yet
     (call_script, "script_process_alarms_new", "$g_process_alarms_cur_center"),
 (else_try), ######not raided/sieged - reset the sorties
   (this_or_next|neg|party_slot_ge, "$g_process_alarms_cur_center", slot_center_is_besieged_by, 0),
   (neg|party_slot_eq, "$g_process_alarms_cur_center", slot_village_state, svs_being_raided),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_last_spotted_enemy, -1),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_strength, 0),
     (party_set_slot, "$g_process_alarms_cur_center", slot_center_sortie_enemy_strength, 0),
 (try_end),

 ################ proceeds to the next center
 (val_add, "$g_process_alarms_cur_center", 1),
 
 
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_9", 6),
]),
################################################################################
    
    
    
    
(1,
[
  ########(display_message, "@script_allow_vassals_to_join_indoor_battle start...", 0xff0000),
  ###### (call_script, "script_allow_vassals_to_join_indoor_battle"),  ############# NEW v2.1 - MOTO - Now that aggressiveness gets set properly, you can comment out expensive and badly written script_allow_vassals_to_join_indoor_battle
  ########(display_message, "@script_allow_vassals_to_join_indoor_battle end...", 0x00ff00),
  ########(display_message, "@script_process_kingdom_parties_ai start...", 0xff0000),
  (call_script, "script_process_kingdom_parties_ai"),
  ########(display_message, "@script_process_kingdom_parties_ai end...", 0x00ff00),
]),

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Process siege ai
#### (3,
(0.028,         ######################### roughly once every 3 hours for each of the 311 walled centers - executed 3 times to achieve this
[
 (try_begin),
   (lt, "$g_process_sieges_new_cur_center", walled_centers_begin), 
     (assign, "$g_process_sieges_new_cur_center", walled_centers_begin),
 (try_end),

 (try_begin),
   (ge, "$g_process_sieges_new_cur_center", walled_centers_end), 
     (assign, "$g_process_sieges_new_cur_center", walled_centers_begin),
 (try_end),
 
 (call_script, "script_process_sieges_new", "$g_process_sieges_new_cur_center"),
 ############## proceeds to the next center 
 (val_add, "$g_process_sieges_new_cur_center", 1),
 
 (call_script, "script_process_sieges_new", "$g_process_sieges_new_cur_center"),
 ############## proceeds to the next center 
 (val_add, "$g_process_sieges_new_cur_center", 1),
 
 (call_script, "script_process_sieges_new", "$g_process_sieges_new_cur_center"),
 ############## proceeds to the next center 
 (val_add, "$g_process_sieges_new_cur_center", 1),
    
 ################# DEBUG
 (val_add, "$g_simple_trigger_fire_count_10", 3),
 ]),
########################################################################################
    
    
    ######### Decide faction ais
    ######(6, ######it was 23
    ######### (6, ######### rafi and it's now 12 ######TOM was 6
    ######### [
      ######### (assign, "$g_recalculate_ais", 1),
    ######### ]),


    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Decide faction ai flag check
#(0 - rafi too much ...
(0.35, ######TOM was 0.1
[
######################################
 (try_begin),
   (lt, "$g_recalculate_ais_cur_fac", kingdoms_begin), 
     (assign, "$g_recalculate_ais_cur_fac", kingdoms_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_recalculate_ais_cur_fac", kingdoms_end), 
     (assign, "$g_recalculate_ais_cur_fac", kingdoms_begin),
 (try_end),
   
######################################## 
 (try_begin),
   (is_between, "$g_recalculate_ais_cur_fac", kingdoms_begin, kingdoms_end),
   (try_begin),
     (faction_slot_eq, "$g_recalculate_ais_cur_fac", slot_faction_state, sfs_active),
       (call_script, "script_recalculate_ais_for_faction", "$g_recalculate_ais_cur_fac"),
   (else_try),
     (assign, ":cycl_end", kingdoms_end),
     (assign, ":cycl_beg", "$g_recalculate_ais_cur_fac"),
     (try_for_range, ":faction_no", ":cycl_beg", ":cycl_end"),
       (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
         (assign, "$g_recalculate_ais_cur_fac", ":faction_no"),
         (call_script, "script_recalculate_ais_for_faction", "$g_recalculate_ais_cur_fac"),
         (assign, ":cycl_end", 0),
     (try_end),
   (try_end),
 (else_try),
   (assign, "$g_recalculate_ais_cur_fac", kingdoms_begin),
     (call_script, "script_recalculate_ais_for_faction", "$g_recalculate_ais_cur_fac"),
 (try_end),
 (val_add, "$g_recalculate_ais_cur_fac", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_11", 1),
#####################################
]),
##########################################################################################
  
  
  
  
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
###################### init_ai_calculation was split into 4 parts - first part is active npcs - execute script 5 times
(0.029,  ################### roughly once every 5 hours for each of the 858 active npcs
[
 (try_begin),
   (lt, "$g_init_ai_calculation_cur_npc", active_npcs_begin), 
   (assign, "$g_init_ai_calculation_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_init_ai_calculation_cur_npc", active_npcs_end), 
   (assign, "$g_init_ai_calculation_cur_npc", active_npcs_begin),
 (try_end),
       
 (try_begin),
   (troop_slot_eq, "$g_init_ai_calculation_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (call_script, "script_init_ai_calculation_active_npcs", "$g_init_ai_calculation_cur_npc"),
 (try_end),
 ################ proceeds to the next npc 
 (val_add, "$g_init_ai_calculation_cur_npc", 1),
       
 (try_begin),
   (troop_slot_eq, "$g_init_ai_calculation_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (call_script, "script_init_ai_calculation_active_npcs", "$g_init_ai_calculation_cur_npc"),
 (try_end),
 ################ proceeds to the next npc 
 (val_add, "$g_init_ai_calculation_cur_npc", 1),
       
 (try_begin),
   (troop_slot_eq, "$g_init_ai_calculation_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (call_script, "script_init_ai_calculation_active_npcs", "$g_init_ai_calculation_cur_npc"),
 (try_end),
 ################ proceeds to the next npc 
 (val_add, "$g_init_ai_calculation_cur_npc", 1),
       
 (try_begin),
   (troop_slot_eq, "$g_init_ai_calculation_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (call_script, "script_init_ai_calculation_active_npcs", "$g_init_ai_calculation_cur_npc"),
 (try_end),
 ################ proceeds to the next npc 
 (val_add, "$g_init_ai_calculation_cur_npc", 1),
       
 (try_begin),
   (troop_slot_eq, "$g_init_ai_calculation_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (call_script, "script_init_ai_calculation_active_npcs", "$g_init_ai_calculation_cur_npc"),
 (try_end),
 ################ proceeds to the next npc 
 (val_add, "$g_init_ai_calculation_cur_npc", 1),
 
 
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_12", 3),
]),
######################################################################
  
  
################# i'm not sure why ladies are included but whatever
###################### second part is kingdom ladies - execute script 3 times 
(0.036,  ################### roughly once every 5 hours for each of the 420 ladies
[
 (try_begin),
   (lt, "$g_init_ai_calculation_cur_lady", kingdom_ladies_begin), 
   (assign, "$g_init_ai_calculation_cur_lady", kingdom_ladies_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_init_ai_calculation_cur_lady", kingdom_ladies_end), 
   (assign, "$g_init_ai_calculation_cur_lady", kingdom_ladies_begin),
 (try_end),
       
 (try_begin),
   (call_script, "script_init_ai_calculation_ladies", "$g_init_ai_calculation_cur_lady"),
 (try_end),
 ################ proceeds to the next lady 
 (val_add, "$g_init_ai_calculation_cur_lady", 1),
         
 (try_begin),
   (call_script, "script_init_ai_calculation_ladies", "$g_init_ai_calculation_cur_lady"),
 (try_end),
 ################ proceeds to the next lady 
 (val_add, "$g_init_ai_calculation_cur_lady", 1),
         
 (try_begin),
   (call_script, "script_init_ai_calculation_ladies", "$g_init_ai_calculation_cur_lady"),
 (try_end),
 ################ proceeds to the next lady 
 (val_add, "$g_init_ai_calculation_cur_lady", 1),
 
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_13", 3),
]),
##############
  

###################### third part is walled centers - execute script 2 times 
(0.032,############## roughly once every 5 hours for each of the 311 walled centers - execute script 2 times
[
 (try_begin),
   (lt, "$g_init_ai_calculation_cur_center", walled_centers_begin), 
   (assign, "$g_init_ai_calculation_cur_center", walled_centers_begin),
 (try_end),

 (try_begin),
   (ge, "$g_init_ai_calculation_cur_center", walled_centers_end), 
   (assign, "$g_init_ai_calculation_cur_center", walled_centers_begin),
 (try_end),
       
 (try_begin),
   (call_script, "script_party_calculate_strength", "$g_init_ai_calculation_cur_center", 0), ######will update slot_party_cached_strength
   (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "$g_init_ai_calculation_cur_center"),
 (try_end),
 ################ proceeds to the next centers 
 (val_add, "$g_init_ai_calculation_cur_center", 1),
         
 (try_begin),
   (call_script, "script_party_calculate_strength", "$g_init_ai_calculation_cur_center", 0), ######will update slot_party_cached_strength
   (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "$g_init_ai_calculation_cur_center"),
 (try_end),
 ################ proceeds to the next centers 
 (val_add, "$g_init_ai_calculation_cur_center", 1),

 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_14", 2),
]),
##############
  

################# last part - for player party
(5,
[
 (call_script, "script_party_calculate_strength", "p_main_party", 0), ######will update slot_party_cached_strength
 (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "p_main_party"),
]),
####################################################################################
  
  
  
  
  
  
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################## was split in two with the other half below this
#### Count faction armies
#### (24,
(0.33,   #################### once daily for each of the 72 factions + player faction
[
 (try_begin),
   (lt, "$g_faction_recalculate_strenght_cur_fac", kingdoms_begin), 
   (assign, "$g_faction_recalculate_strenght_cur_fac", kingdoms_begin),
 (try_end),

 (try_begin),
   (ge, "$g_faction_recalculate_strenght_cur_fac", kingdoms_end), 
   (assign, "$g_faction_recalculate_strenght_cur_fac", kingdoms_begin),
 (try_end),

 (try_begin),
   (faction_slot_eq, "$g_faction_recalculate_strenght_cur_fac", slot_faction_state, sfs_active), ### NEW v2.1
     (call_script, "script_faction_recalculate_strength", "$g_faction_recalculate_strenght_cur_fac"),
 (try_end),
 
 ################ proceeds to the next faction when it's triggered again
 (val_add, "$g_faction_recalculate_strenght_cur_fac", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_15", 1),
]),
###############

    
################## the other half
(24,
[
 (try_begin),
   # (eq, "$cheat_mode", 4), 
   (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
     (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
     (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_feast),
     (neg|faction_slot_eq, ":active_npc_faction", slot_faction_ai_state, sfai_gathering_army),
     
     (troop_get_slot, ":active_npc_party", ":active_npc", slot_troop_leaded_party),
     (party_is_active, ":active_npc_party"),
     
     (val_add, "$total_vassal_days_on_campaign", 1),
     
     (party_slot_eq, ":active_npc_party", slot_party_ai_state, spai_accompanying_army),
     (val_add, "$total_vassal_days_responding_to_campaign", 1),
   (try_end),
   ################### DEBUG
   (val_add, "$g_simple_trigger_fire_count_16", 1),
 (try_end),
]),
############################################################################## 

    
    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################## was split in two with the other half below this 
#### Reset hero quest status
#### Change hero relation
#### (36,
(0.042,   #################### once every 36 hours for each of the 858 active NPCs
[
 (try_begin),
   (lt, "$g_reset_quest_status_heroes_cur_npc", active_npcs_begin), 
   (assign, "$g_reset_quest_status_heroes_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_reset_quest_status_heroes_cur_npc", active_npcs_end), 
   (assign, "$g_reset_quest_status_heroes_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (troop_slot_eq, "$g_reset_quest_status_heroes_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
     (troop_set_slot, "$g_reset_quest_status_heroes_cur_npc", slot_troop_does_not_give_quest, 0),
 (try_end),
 
 ################ proceeds to the next npc when it's triggered again
 (val_add, "$g_reset_quest_status_heroes_cur_npc", 1),
   
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_17", 1),
]),
###############

    
################## the other half - village elders
(0.085,   #################### once every 36 hours for each of the 423 elders
[
 (try_begin),
   (lt, "$g_reset_quest_status_elders_cur_npc", village_elders_begin), 
     (assign, "$g_reset_quest_status_elders_cur_npc", village_elders_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_reset_quest_status_elders_cur_npc", village_elders_end), 
     (assign, "$g_reset_quest_status_elders_cur_npc", village_elders_begin),
 (try_end),
 
 (try_begin),
   (troop_set_slot, "$g_reset_quest_status_elders_cur_npc", slot_troop_does_not_give_quest, 0),
 (try_end),
  
 ################ proceeds to the next npc when it's triggered again
 (val_add, "$g_reset_quest_status_elders_cur_npc", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_18", 1),
]),
############################################################################## 



################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Refresh merchant inventories
#### (168, 
(0.397,   #################### once every week for each of the 423 villages
[
 (try_begin),
   (lt, "$g_refresh_village_inventory_cur_village", villages_begin), 
   (assign, "$g_refresh_village_inventory_cur_village", villages_begin),
 (try_end),

 (try_begin),
   (ge, "$g_refresh_village_inventory_cur_village", villages_end), 
   (assign, "$g_refresh_village_inventory_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (call_script, "script_refresh_village_merchant_inventory", "$g_refresh_village_inventory_cur_village"),
 (try_end),
 
 ################ proceeds to the next village when it's triggered again
 (val_add, "$g_refresh_village_inventory_cur_village", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_19", 1),
]),
########################################################################
    
    
    
    
    
################# NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
# Refreshing village defenders
# Clearing slot_village_player_can_not_steal_cattle flags
### (48,
(0.113,  ##################### once every 48 hours for each of the 422 villages
[
 (try_begin),
   (lt, "$g_refresh_village_defenders_cur_village", villages_begin), 
   (assign, "$g_refresh_village_defenders_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_refresh_village_defenders_cur_village", villages_end), 
   (assign, "$g_refresh_village_defenders_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (call_script, "script_refresh_village_defenders", "$g_refresh_village_defenders_cur_village"),
   (party_set_slot, "$g_refresh_village_defenders_cur_village", slot_village_player_can_not_steal_cattle, 0),
 (try_end),
 
 ############## proceeds to the next village when it's triggered again
 (val_add, "$g_refresh_village_defenders_cur_village", 1),
  
 ################# DEBUG
 (val_add, "$g_simple_trigger_fire_count_20", 1),
]),
 
# (48,
# [
   ###### (try_for_range, ":village_no", villages_begin, villages_end),
     ###### (call_script, "script_refresh_village_defenders", ":village_no"),
     ###### (party_set_slot, ":village_no", slot_village_player_can_not_steal_cattle, 0),
   ###### (try_end),
 ###### ]),
#######################################################################################
    

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### (168,
(0.229,       ##################### once every week for each of the 422 villages + 111 towns = 533
[
 (try_begin),
   (lt, "$g_calculate_center_production_cur_center", centers_begin), 
   (assign, "$g_calculate_center_production_cur_center", centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_calculate_center_production_cur_center", centers_end), 
   (assign, "$g_calculate_center_production_cur_center", centers_begin),
 (try_end),
 
 (try_begin),
   (neg|is_between, "$g_calculate_center_production_cur_center", castles_begin, castles_end),
   (party_get_slot, ":num_cattle", "$g_calculate_center_production_cur_center", slot_center_head_cattle),
   (party_get_slot, ":num_sheep", "$g_calculate_center_production_cur_center", slot_center_head_sheep),
   (party_get_slot, ":num_acres", "$g_calculate_center_production_cur_center", slot_center_acres_pasture),
   (val_max, ":num_acres", 1),
   
   (store_mul, ":grazing_capacity", ":num_cattle", 400),
   (store_mul, ":sheep_addition", ":num_sheep", 200),
   (val_add, ":grazing_capacity", ":sheep_addition"),
   (val_div, ":grazing_capacity", ":num_acres"),
   
   (store_random_in_range, ":random_no", 0, 100),
   (try_begin), ######Disaster
     (eq, ":random_no", 0),#1% chance of epidemic - should happen once every two years
     (val_min, ":num_cattle", 10),
	 
     (try_begin),
       ##########(eq, "$cheat_mode", 1),
       ##########(str_store_party_name, s1, ":village_no"),
       ##########(display_message, "@{!}Cattle in {s1} are exterminated due to famine."),
       ###############diplomacy start+ Add display message for the player's own fiefs
       ##########(store_distance_to_party_from_party, ":dist", "p_main_party", ":village_no"),
       ##########(this_or_next|lt, ":dist", 30),
       (gt, "$g_player_chamberlain", 0),
       (party_slot_eq, "$g_calculate_center_production_cur_center", slot_town_lord, "trp_player"),
         (party_get_slot, reg4, "$g_calculate_center_production_cur_center", slot_center_head_cattle),
         (val_sub, reg4, ":num_cattle"),
         (gt, reg4, 0),
           (str_store_party_name_link, s4, "$g_calculate_center_production_cur_center"),
           (display_log_message, "@A livestock epidemic has killed {reg4} cattle in {s4}."),
           ###############diplomacy end+
     (try_end),
     
   (else_try), ######Overgrazing
     (gt, ":grazing_capacity", 100),
    
     (val_mul, ":num_sheep", 90), ######10% decrease at number of cattles
     (val_div, ":num_sheep", 100),
    
     (val_mul, ":num_cattle", 90), ######10% decrease at number of sheeps
     (val_div, ":num_cattle", 100),
     
   (else_try), ######superb grazing
     (lt, ":grazing_capacity", 30),
 
     (val_mul, ":num_cattle", 120), ######20% increase at number of cattles
     (val_div, ":num_cattle", 100),
     (val_add, ":num_cattle", 1),
    
     (val_mul, ":num_sheep", 120), ######20% increase at number of sheeps
     (val_div, ":num_sheep", 100),
     (val_add, ":num_sheep", 1),
    
   (else_try), ######very good grazing
     (lt, ":grazing_capacity", 60),
 
     (val_mul, ":num_cattle", 110), ######10% increase at number of cattles
     (val_div, ":num_cattle", 100),
     (val_add, ":num_cattle", 1),
    
     (val_mul, ":num_sheep", 110), ######10% increase at number of sheeps
     (val_div, ":num_sheep", 100),
     (val_add, ":num_sheep", 1),
 
   (else_try), ######good grazing
     (lt, ":grazing_capacity", 100),
     (lt, ":random_no", 50),
 
     (val_mul, ":num_cattle", 105), ######5% increase at number of cattles
     (val_div, ":num_cattle", 100),
     (try_begin), ######if very low number of cattles and there is good grazing then increase number of cattles also by one
       (le, ":num_cattle", 20),
       (val_add, ":num_cattle", 1),
     (try_end),
    
     (val_mul, ":num_sheep", 105), ######5% increase at number of sheeps
     (val_div, ":num_sheep", 100),
     (try_begin), ######if very low number of sheeps and there is good grazing then increase number of sheeps also by one
       (le, ":num_sheep", 20),
       (val_add, ":num_sheep", 1),
     (try_end),        
   (try_end),
 
   (party_set_slot, "$g_calculate_center_production_cur_center", slot_center_head_cattle, ":num_cattle"),
   (party_set_slot, "$g_calculate_center_production_cur_center", slot_center_head_sheep, ":num_sheep"),                  
 (try_end),
 
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_calculate_center_production_cur_center", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_21", 1),
]),
########################################################################################




################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
 ######Accumulate taxes
#### (168,
(0.23,    ##################### once every week for each of the 733 centers
[
 (try_begin),
   (lt, "$g_accumulate_taxes_cur_center", centers_begin), 
   (assign, "$g_accumulate_taxes_cur_center", centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_accumulate_taxes_cur_center", centers_end), 
   (assign, "$g_accumulate_taxes_cur_center", centers_begin),
 (try_end),
 
 ######Collect taxes for another week
 (try_begin),
   (try_begin),
     (party_slot_ge, "$g_accumulate_taxes_cur_center", slot_town_lord, 0), ######unassigned centers do not accumulate rents      
     (party_get_slot, ":accumulated_rents", "$g_accumulate_taxes_cur_center", slot_center_accumulated_rents),
     
     (assign, ":cur_rents", 800),
     (try_begin),
       (party_slot_eq, "$g_accumulate_taxes_cur_center", slot_party_type, spt_village),
       (try_begin),
         (party_slot_eq, "$g_accumulate_taxes_cur_center", slot_village_state, svs_normal),
         (assign, ":cur_rents", 3000), ######2600
       (try_end),
     (else_try),
       (party_slot_eq, "$g_accumulate_taxes_cur_center", slot_party_type, spt_castle),
       (assign, ":cur_rents", 6000), #######tom was 2600 - PROSPERITY SYSTEM CHANGE THIS
     (else_try),  
       (party_slot_eq, "$g_accumulate_taxes_cur_center", slot_party_type, spt_town),
       (assign, ":cur_rents", 10000),
     (try_end),
   
     ######tom multiplayer to 35
     (party_get_slot, ":prosperity", "$g_accumulate_taxes_cur_center", slot_town_prosperity), ######prosperty changes between 0..100     
     (store_add, ":multiplier", 35, ":prosperity"), ######multiplier changes between 20..120
     (val_mul, ":cur_rents", ":multiplier"), 
     (val_div, ":cur_rents", 135),#Prosperity of 100 gives the default values
 
     ######### (try_begin),
       ######### (party_slot_eq, "$g_accumulate_taxes_cur_center", slot_town_lord, "trp_player"),
       
       ######### (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
       ######### (try_begin),
         ######### (eq, ":reduce_campaign_ai", 0), ######hard (less money from rents)
         ######### (val_mul, ":cur_rents", 3),
         ######### (val_div, ":cur_rents", 4),
       ######### (else_try),
         ######### (eq, ":reduce_campaign_ai", 1), ######medium (normal money from rents)
       ######### (else_try),
         ######### (eq, ":reduce_campaign_ai", 2), ######easy (more money from rents)
         ######### (val_mul, ":cur_rents", 4),
         ######### (val_div, ":cur_rents", 3),
       ######### (try_end),                
     ######### (try_end),  
     
     #######PROSPERITY SYSTEM TAXES
     (party_get_slot, ":tax", "$g_accumulate_taxes_cur_center", dplmc_slot_center_taxation),
     (store_mul, ":tax_rents", ":cur_rents", ":tax"),
     (val_div, ":tax_rents", 100),
     (val_add, ":accumulated_rents", ":tax_rents"),
     #######PROSPERITY SYSTEM TAXES
     
     (val_add, ":accumulated_rents", ":cur_rents"), ######cur rents changes between 23..1000
     (party_set_slot, "$g_accumulate_taxes_cur_center", slot_center_accumulated_rents, ":accumulated_rents"),
   (try_end),
   
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_accumulate_taxes_cur_center", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_22", 1),
 (try_end),
]),
##################################################################################


  ######### Offer player to join faction
  ######### Only if the player is male -- female characters will be told that they should seek out a faction through NPCs, possibly
   (32,
   [
     (eq, "$players_kingdom", 0),
     (le, "$g_invite_faction", 0),
     (eq, "$g_player_is_captive", 0),
     (troop_get_type, ":type", "trp_player"),
     (try_begin),
        (eq, ":type", 1),
        (eq, "$npc_with_sisterly_advice", 0),
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (troop_get_type, ":npc_type", ":npc"),
            (eq, ":npc_type", 1),
            (troop_slot_ge, "trp_player", slot_troop_renown, 150),
            (troop_slot_ge, ":npc", slot_troop_woman_to_woman_string, 1),
            (assign, "$npc_with_sisterly_advice", ":npc"),
        (try_end),
     (else_try),
         (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
         (assign, ":min_distance", 999999),
         (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
           (store_faction_of_party, ":center_faction", ":center_no"),
           (eq, ":center_faction", ":kingdom_no"),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
           (val_min, ":min_distance", ":cur_distance"),
         (try_end),
         (lt, ":min_distance", 30),
         (store_relation, ":kingdom_relation", ":kingdom_no", "fac_player_supporters_faction"),
         (faction_get_slot, ":kingdom_lord", ":kingdom_no", slot_faction_leader),
         (call_script, "script_troop_get_player_relation", ":kingdom_lord"),
         (assign, ":lord_relation", reg0),
         ######(troop_get_slot, ":lord_relation", ":kingdom_lord", slot_troop_player_relation),
         (call_script, "script_get_number_of_hero_centers", "trp_player"),
         (assign, ":num_centers_owned", reg0),
         (eq, "$g_infinite_camping", 0),

         (assign, ":player_party_size", 0),
         (try_begin),
           (ge, "p_main_party", 0),
           (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),
         (try_end),

         (try_begin),
           (eq, ":num_centers_owned", 0),
           (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
           (ge, ":player_renown", 160),
           (ge, ":kingdom_relation", 0),
           (ge, ":lord_relation", 0),
           (ge, ":player_party_size", 45),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", 50),
           (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
           (assign, "$g_invite_offered_center", reg0),
           (ge, "$g_invite_offered_center", 0),
           (assign, "$g_invite_faction", ":kingdom_no"),
           (jump_to_menu, "mnu_invite_player_to_faction"),
         (else_try),
           (gt, ":num_centers_owned", 0),
           (neq, "$players_oath_renounced_against_kingdom", ":kingdom_no"),
           (ge, ":kingdom_relation", -40),
           (ge, ":lord_relation", -20),
           (ge, ":player_party_size", 30),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", 20),
           (assign, "$g_invite_faction", ":kingdom_no"),
           (assign, "$g_invite_offered_center", -1),
           (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
         (try_end),
     (try_end),
    ]),

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#recalculate lord random decision seeds once in every week
#### (168,
(2.3,  ##################### once every week for each of the 72 factions + player faction
[
 (try_begin),
   (lt, "$g_recalculate_random_decision_seed_cur_faction", kingdoms_begin), 
   (assign, "$g_recalculate_random_decision_seed_cur_faction", kingdoms_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_recalculate_random_decision_seed_cur_faction", kingdoms_end), 
   (assign, "$g_recalculate_random_decision_seed_cur_faction", kingdoms_begin),
 (try_end),
  
 (assign, ":wars", 0),
 
 (try_begin),
   (faction_slot_eq, "$g_recalculate_random_decision_seed_cur_faction", slot_faction_state, sfs_active),
   (try_for_range, ":kingdom_2", kingdoms_begin, kingdoms_end),
     (faction_slot_eq, ":kingdom_2", slot_faction_state, sfs_active),
     (neq, ":kingdom_2", "$g_recalculate_random_decision_seed_cur_faction"),
     (store_relation, ":relation", "$g_recalculate_random_decision_seed_cur_faction", ":kingdom_2"),
     (lt, ":relation", 0),        
     (val_add, ":wars", 1),
   (try_end),
   
   (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
     (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ####### he's alive/active
     (store_troop_faction, ":faction", ":troop_no"),
     (eq, ":faction", "$g_recalculate_random_decision_seed_cur_faction"),
     (try_begin),
       (eq, ":wars", 2),
       (store_random_in_range, ":random", 3000, 9999),
     (else_try),
       (gt, ":wars", 3),
       (store_random_in_range, ":random", 7000, 9999),
     (else_try),
       (store_random_in_range, ":random", 0, 9999),
     (try_end),
     (troop_set_slot, ":troop_no", slot_troop_temp_decision_seed, ":random"),
   (try_end),
   
 (try_end),
 ################ proceeds to the next faction when it's triggered again
 (val_add, "$g_recalculate_random_decision_seed_cur_faction", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_23", 1),
 
#npcs will only change their minds on issues at least 24 hours after speaking to the player
#(store_current_hours, ":hours"),
#(try_begin),
####  (eq, 1, 0), ######disabled
####  (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
####    (troop_get_slot, ":last_talk", ":npc", slot_troop_last_talk_time),
####    (val_sub, ":hours", ":last_talk"),
####    (ge, ":hours", 24),
####    (store_random_in_range, ":random", 0, 9999),
####    (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":random"),
####  (try_end),
#(try_end),
]),
########################################################################################
    
    
    
  ######### During rebellion, removing troops from player faction randomly because of low relation points
  ######### Deprecated -- should be part of regular political events


  ######### Reset kingdom lady current centers
#####   (28,
#####   [
#####       (try_for_range, ":troop_no", heroes_begin, heroes_end),
#####         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
##
#####         ######### Find the active quest ladies
#####         (assign, ":not_ok", 0),
#####         (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
#####           (eq, ":not_ok", 0),
#####           (check_quest_active, ":quest_no"),
#####           (quest_slot_eq, ":quest_no", slot_quest_object_troop, ":troop_no"),
#####           (assign, ":not_ok", 1),
#####         (try_end),
#####         (eq, ":not_ok", 0),
##
#####         (troop_get_slot, ":troop_center", ":troop_no", slot_troop_cur_center),
#####         (assign, ":is_under_siege", 0),
#####         (try_begin),
#####           (is_between, ":troop_center", walled_centers_begin, walled_centers_end),
#####           (party_get_battle_opponent, ":besieger_party", ":troop_center"),
#####           (gt, ":besieger_party", 0),
#####           (assign, ":is_under_siege", 1),
#####         (try_end),
##
#####         (eq, ":is_under_siege", 0),#### Omit ladies in centers under siege
##
#####         (try_begin),
#####           (store_random_in_range, ":random_num",0, 100),
#####           (lt, ":random_num", 20),
#####           (store_troop_faction, ":cur_faction", ":troop_no"),
#####           (call_script, "script_cf_select_random_town_with_faction", ":cur_faction"),#Can fail
#####           (troop_set_slot, ":troop_no", slot_troop_cur_center, reg0),
#####         (try_end),
##
#####         (store_random_in_range, ":random_num",0, 100),
#####         (lt, ":random_num", 50),
#####         (troop_get_slot, ":lord_no", ":troop_no", slot_troop_father),
#####         (try_begin),
#####           (eq, ":lord_no", 0),
#####           (troop_get_slot, ":lord_no", ":troop_no", slot_troop_spouse),
#####         (try_end),
#####         (gt, ":lord_no", 0),
#####         (troop_get_slot, ":cur_party", ":lord_no", slot_troop_leaded_party),
#####         (gt, ":cur_party", 0),
#####         (party_get_attached_to, ":cur_center", ":cur_party"),
#####         (gt, ":cur_center", 0),
##
#####         (troop_set_slot, ":troop_no", slot_troop_cur_center, ":cur_center"),
#####       (try_end),
#####    ]),



############### NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
############## split into two
#### Attach Lord Parties to the town they are in
#(0.1,
(0.3,
[
  ######(display_message, "@attach lord parties start...", 0xff0000),
 (try_for_range, ":troop_no", heroes_begin, heroes_end),
   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
   (ge, ":troop_party_no", 1),
   (party_is_active, ":troop_party_no"),
     (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
     (lt, ":cur_attached_town", 1),
       (party_get_cur_town, ":destination", ":troop_party_no"),
       (is_between, ":destination", centers_begin, centers_end),
         (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
         (try_begin),
           (ge, reg0, 0),
             (party_attach_to_party, ":troop_party_no", ":destination"),
         (else_try),
           (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
         (try_end),
         
         (try_begin),
           (this_or_next|party_slot_eq, ":destination", slot_party_type, spt_town),
           (party_slot_eq, ":destination", slot_party_type, spt_castle),
             (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
             (store_faction_of_party, ":destination_faction_no", ":destination"),
             (eq, ":troop_faction_no", ":destination_faction_no"),
               (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
               (gt, ":num_stacks", 0),
                 (assign, "$g_move_heroes", 1),
                 (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
                 (assign, "$g_move_heroes", 1),
                 (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
         (try_end),
 (try_end),
 ######(display_message, "@attach lord parties end...", 0x00ff00),
]),
##############


############## other half
# (0.5,
(1,
[
 ##########SB : add spotting check, moved to less time-consuming slot
 (call_script, "script_get_max_skill_of_player_party", "skl_spotting"),
 (store_add, ":spotting", reg0, 3),
 (val_div, ":spotting", 2), ##########1 to 9 now
 (try_for_parties, ":bandit_camp"),
   (gt, ":bandit_camp", "p_spawn_points_end"),
   ######Can't have party is active here, because it will fail for inactive parties
   (party_get_template_id, ":template", ":bandit_camp"),
   (ge, ":template", "pt_steppe_bandit_lair"),
 
   (store_distance_to_party_from_party, ":distance", "p_main_party", ":bandit_camp"),
   ######### NEW v2.9 - spotting skill takes part in the calculation
   (val_add, ":spotting", 2),
   (lt, ":distance", ":spotting"),
   #########
   (party_set_flags, ":bandit_camp", pf_disabled, 0),
   (party_set_flags, ":bandit_camp", pf_always_visible, 1),
 (try_end),
  ######(display_message, "@attach lord parties end...", 0x00ff00),
]),
####################################################################################


    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################# splitted on half, other half is below this
#### Check escape chances of hero prisoners. MOTO chief call more frequently with less chances.
(10,
[
 (assign, ":troop_no", "trp_player"),
 (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
 (assign, ":ratio_chance", 30),
 (val_mul, ":skill", 2), ############### 2% less chance per point in prisoner management
 (val_sub, ":ratio_chance", ":skill"),
 
 ######### (try_begin), ######not on water
 ######### (party_slot_eq, "p_main_party", slot_party_on_water, 0), ######player on land.
 (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", ":ratio_chance"),
 ######### (try_end),
]),
################
    
    
################### other half - now for walled center prisoners
(0.154,  ######################### once every 48 hours for each of 311 walled centers
[
 (try_begin),
   (lt, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", walled_centers_begin), 
   (assign, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", walled_centers_end), 
   (assign, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   # (party_slot_eq, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", slot_town_lord, "trp_player"),
   (assign, ":chance", 30),
   (try_begin),
     (party_slot_eq, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", slot_center_has_prisoner_tower, 1),
     (assign, ":chance", 5),
   (try_end),
   (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", ":chance"),
 (try_end),
 
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", 1),
  
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_24", 1),
]),
################################################################################
    
    
    
  ######### Asking the ownership of captured centers to the player
####  (3,
####   [
####    (assign, "$g_center_taken_by_player_faction", -1),
####    (try_for_range, ":center_no", centers_begin, centers_end),
####      (eq, "$g_center_taken_by_player_faction", -1),
####      (store_faction_of_party, ":center_faction", ":center_no"),
####      (eq, ":center_faction", "fac_player_supporters_faction"),
####      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
####      (this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
####      (party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
####      (assign, "$g_center_taken_by_player_faction", ":center_no"),
####    (try_end),
####    (faction_get_slot, ":leader", "fac_player_supporters_faction", slot_faction_leader),

#    (try_begin),
#        (ge, "$g_center_taken_by_player_faction", 0),

#        (eq, "$cheat_mode", 1),
#        (str_store_party_name, s14, "$g_center_taken_by_player_faction"),
#        (display_message, "@{!}{s14} should be assigned to lord"),
#    (try_end),

####    ]),



################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Respawn hero party after kingdom hero is released from captivity.
#### (24*7, ######48,
#### (168
(0.084, ###################### once every 3 days for each of the 858 active NPCs
[
 (try_begin),
   (lt, "$g_respawn_party_after_release_cur_npc", active_npcs_begin), 
   (assign, "$g_respawn_party_after_release_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_respawn_party_after_release_cur_npc", active_npcs_end), 
   (assign, "$g_respawn_party_after_release_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (troop_slot_eq, "$g_respawn_party_after_release_cur_npc", slot_troop_is_alive, 1),  ####### he's alive/active
   (troop_slot_eq, "$g_respawn_party_after_release_cur_npc", slot_troop_occupation, slto_kingdom_hero),
   (neg|troop_slot_ge, "$g_respawn_party_after_release_cur_npc", slot_troop_prisoner_of_party, 0),
   (neg|troop_slot_ge, "$g_respawn_party_after_release_cur_npc", slot_troop_leaded_party, 1),
 
   (store_troop_faction, ":cur_faction", "$g_respawn_party_after_release_cur_npc"),
   (try_begin),
     (eq, ":cur_faction", "fac_outlaws"), ######Do nothing
     
     
   (else_try),
     (try_begin),
       (eq, "$cheat_mode", 2),
       (str_store_troop_name, s4, "$g_respawn_party_after_release_cur_npc"),
       (display_message, "str_debug__attempting_to_spawn_s4"),
     (try_end),
 
     (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", "$g_respawn_party_after_release_cur_npc"),#Can fail
     (assign, ":center_no", reg0),
 
     (try_begin),
       (eq, "$cheat_mode", 2),
       (assign, reg7, ":center_no"),
       (str_store_party_name, s7, ":center_no"),
       (display_message, "str_debug__s0_is_spawning_around_party__s7"),
     (try_end),
 
     (call_script, "script_create_kingdom_hero_party", "$g_respawn_party_after_release_cur_npc", ":center_no"),
     (try_begin),
       (eq, "$g_there_is_no_avaliable_centers", 0),
       (party_attach_to_party, "$pout_party", ":center_no"),
     (try_end),
 
     ######new
     ######(troop_get_slot, ":party_no", "$g_respawn_party_after_release_cur_npc", slot_troop_leaded_party),
     ######(call_script, "script_npc_decision_checklist_party_ai", "$g_respawn_party_after_release_cur_npc"), ######This handles AI for both marshal and other parties
     ######(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
     ######new end
 
     (troop_get_slot, ":party_no", "$g_respawn_party_after_release_cur_npc", slot_troop_leaded_party),
     (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),
 
   (else_try),
     (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
     (try_begin),
       (is_between, "$g_respawn_party_after_release_cur_npc", kings_begin, kings_end),
       (troop_set_slot, "$g_respawn_party_after_release_cur_npc", slot_troop_change_to_faction, "fac_commoners"),
     (else_try),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", 10),
       (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
       (troop_set_slot, "$g_respawn_party_after_release_cur_npc", slot_troop_change_to_faction, reg0),
     (try_end),
   (try_end),
 (try_end),
  
 ################ proceeds to the next npc when it's triggered again
 (val_add, "$g_respawn_party_after_release_cur_npc", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_25", 1),
]),
########################################

    

  ######### Spawn merchant caravan parties
#####  (3,
#####   [
#####       (try_for_range, ":troop_no", merchants_begin, merchants_end),
#####         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_merchant),
#####         (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
#####         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
##
#####         (call_script, "script_cf_create_merchant_party", ":troop_no"),
#####       (try_end),
#####    ]),


################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Spawn village farmer parties - since 1257AD is so huge villagers don't spawn anymore and instead the trade is done automatically
#### (24, ######was 24
(0.170,   ######once every 72 hours for each of the 422 villages - removed randomization
[
 (try_begin),
   (lt, "$g_village_center_trade_cur_village", villages_begin), 
   (assign, "$g_village_center_trade_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_village_center_trade_cur_village", villages_end), 
   (assign, "$g_village_center_trade_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (party_slot_eq, "$g_village_center_trade_cur_village", slot_village_state, svs_normal),
   ######### (party_get_slot, ":farmer_party", "$g_village_center_trade_cur_village", slot_village_farmer_party),
   ######### (this_or_next|eq, ":farmer_party", 0),
   ######### (neg|party_is_active, ":farmer_party"),
   ###### (store_random_in_range, ":random_no", 0, 100),
   ###### (lt, ":random_no", 60), ######tom was 60
   ######tom
   ######(call_script, "script_create_village_farmer_party", "$g_village_center_trade_cur_village"),
   ######(party_set_slot, "$g_village_center_trade_cur_village", slot_village_farmer_party, reg0),
   ######end of the original village_farmer party code
   ######this is the start of the new code where village trade with center automatically
   (party_get_slot, ":town_no", "$g_village_center_trade_cur_village", slot_village_market_town),
   (party_slot_eq, ":town_no", slot_center_is_besieged_by, -1),
   (call_script, "script_do_villager_center_trade", "$g_village_center_trade_cur_village", ":town_no"),
   (assign, ":total_change", reg0),
   (call_script, "script_do_villager_center_trade", ":town_no", "$g_village_center_trade_cur_village"),
    ########### ######This is roughly 50% of what a caravan would pay
    
   ########### ######Adding tariffs to the town
   (party_get_slot, ":accumulated_tariffs", ":town_no", slot_center_accumulated_tariffs),
   (party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
 
   (assign, ":tariffs_generated", ":total_change"),
   (val_mul, ":tariffs_generated", ":prosperity"),
   (val_div, ":tariffs_generated", 100),
   (val_div, ":tariffs_generated", 20), ######10 for caravans, 20 for villages
   (val_add, ":accumulated_tariffs", ":tariffs_generated"),
   
   (party_set_slot, ":town_no", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
   
   
############################## Increasing food stocks of the town
   (party_get_slot, ":town_food_store", ":town_no", slot_party_food_store),
   (call_script, "script_center_get_food_store_limit", ":town_no"),
   (assign, ":food_store_limit", reg0),
   (val_add, ":town_food_store", 3000), ############# tripled because it's once every 3 days instead of every day
   (val_min, ":town_food_store", ":food_store_limit"),
   (party_set_slot, ":town_no", slot_party_food_store, ":town_food_store"),
#######################
 (try_end),
 
 ################ proceeds to the next village when it's triggered again
 (val_add, "$g_village_center_trade_cur_village", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_26", 1),
]),
##################################################################





################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
   ######### (72,
   ###### (0.098, ######once every 72 hours for each of the 733 centers
   ###### [
    ###### (try_begin),
      ###### (lt, "$g_calculate_player_odds_cur_center", centers_begin), 
      ###### (assign, "$g_calculate_player_odds_cur_center", centers_begin),
    ###### (try_end),

    ###### (try_begin),
      ###### (ge, "$g_calculate_player_odds_cur_center", centers_end), 
      ###### (assign, "$g_calculate_player_odds_cur_center", centers_begin),
    ###### (try_end),
    
    ######## Updating trade good prices according to the productions
    ###### (call_script, "script_update_trade_good_prices", "$g_calculate_player_odds_cur_center"),
       
     ######## Updating player odds
    ###### (try_begin),
      ###### (party_get_slot, ":player_odds", "$g_calculate_player_odds_cur_center", slot_town_player_odds),
      ###### (try_begin),
        ###### (gt, ":player_odds", 1000),
        ###### (val_mul, ":player_odds", 95),
        ###### (val_div, ":player_odds", 100),
        ###### (val_max, ":player_odds", 1000),
      ###### (else_try),
        ###### (lt, ":player_odds", 1000),
        ###### (val_mul, ":player_odds", 105),
        ###### (val_div, ":player_odds", 100),
        ###### (val_min, ":player_odds", 1000),
      ###### (try_end),
      ###### (party_set_slot, "$g_calculate_player_odds_cur_center", slot_town_player_odds, ":player_odds"),
    ###### (try_end),
    
    ############### proceeds to the next center when it's triggered again
    ###### (val_add, "$g_calculate_player_odds_cur_center", 1),
       
      ################## DEBUG
      ###### (val_add, "$g_simple_trigger_fire_count_27", 1),  ###### Updating trade good prices according to the productions
       
       
    # ]),
    

   (72,
   [
  ###### Updating trade good prices according to the productions
       (call_script, "script_update_trade_good_prices"),
 ###### Updating player odds
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (party_get_slot, ":player_odds", ":cur_center", slot_town_player_odds),
         (try_begin),
           (gt, ":player_odds", 1000),
           (val_mul, ":player_odds", 95),
           (val_div, ":player_odds", 100),
           (val_max, ":player_odds", 1000),
         (else_try),
           (lt, ":player_odds", 1000),
           (val_mul, ":player_odds", 105),
           (val_div, ":player_odds", 100),
           (val_min, ":player_odds", 1000),
         (try_end),
         (party_set_slot, ":cur_center", slot_town_player_odds, ":player_odds"),
       (try_end),
    ]),

##################################################################
   
   
  ######Troop AI: Merchants thinking
  (8,
   [
      ######(display_message, "@merchants thinking start...", 0xff0000),
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
         (party_is_in_any_town, ":party_no"),

         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", slot_faction_num_towns),
         (try_begin),
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
           ###################### NEW v2.1 - removes 1 from associated slot
           (faction_get_slot, ":cur_slot_value", ":merchant_faction", slot_faction_party_type_count_kingdom_caravan),
           (val_sub, ":cur_slot_value", 1),
           (faction_set_slot, ":merchant_faction", slot_faction_party_type_count_kingdom_caravan, ":cur_slot_value"),
           ######################
         (else_try),
           (party_get_cur_town, ":cur_center", ":party_no"),

           (store_random_in_range, ":random_no", 0, 100),

           (try_begin),
             (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),

             ######### (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             ######### (try_begin),
               ######### (eq, ":reduce_campaign_ai", 0), ######hard (less money from tariffs)
               ######### (assign, ":tariff_succeed_limit", 35),
             ######### (else_try),
               ######### (eq, ":reduce_campaign_ai", 1), ######medium (normal money from tariffs)
               ######### (assign, ":tariff_succeed_limit", 45),
             ######### (else_try),
               ######### (eq, ":reduce_campaign_ai", 2), ######easy (more money from tariffs)
               ######### (assign, ":tariff_succeed_limit", 60),
             ######### (try_end),
           (else_try),
             (assign, ":tariff_succeed_limit", 45),
           (try_end),

           (lt, ":random_no", ":tariff_succeed_limit"),

           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", slot_party_ai_state),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           (assign, ":target_center", -1),

           (try_begin), ######Make sure escorted caravan continues to its original destination.
             (eq, "$caravan_escort_party_id", ":party_no"),
             (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
             (assign, ":target_center", "$caravan_escort_destination_town"),
           (else_try),
             (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
             (assign, ":target_center", reg0),
           (try_end),
           (is_between, ":target_center", towns_begin, towns_end),
           (neg|party_is_in_town, ":party_no", ":target_center"),

           (try_begin),
             (eq, ":do_trade", 1),
             (str_store_party_name, s7, ":cur_center"),
             (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
             (call_script, "script_refresh_travelling_merchant_inventory", ":party_no"), ####### Floris - Trade with Merchant Caravans
           (try_end),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
         (try_end),
       (try_end),
       ######(display_message, "@merchants thinking end...", 0x00ff00),
    ]),

  ######Troop AI: Village farmers thinking
  (8,
   [
     
     (eq, 0, 1),
      ########(display_message, "@farmers thinking start...", 0xff0000),
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_village_farmer),
         (party_is_in_any_town, ":party_no"),
         (party_get_slot, ":home_center", ":party_no", slot_party_home_center),
         (party_get_cur_town, ":cur_center", ":party_no"),

         (assign, ":can_leave", 1),
         (try_begin),
           (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
           (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
           (assign, ":can_leave", 0),
         (try_end),
         (eq, ":can_leave", 1),

         (try_begin),
           (eq, ":cur_center", ":home_center"),

          ########### ######Peasants trade in their home center
           (call_script, "script_do_party_center_trade", ":party_no", ":home_center", price_adjustment), ######this needs to be the same as the center
           (store_faction_of_party, ":center_faction", ":cur_center"),
           (party_set_faction, ":party_no", ":center_faction"),
           (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":market_town"),
         (else_try),

           (try_begin),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),

             (call_script, "script_do_party_center_trade", ":party_no", ":cur_ai_object", price_adjustment), ######raised from 10
             (assign, ":total_change", reg0),
            ########### ######This is roughly 50% of what a caravan would pay

            ########### ######Adding tariffs to the town
             (party_get_slot, ":accumulated_tariffs", ":cur_ai_object", slot_center_accumulated_tariffs),
             (party_get_slot, ":prosperity", ":cur_ai_object", slot_town_prosperity),

             (assign, ":tariffs_generated", ":total_change"),
             (val_mul, ":tariffs_generated", ":prosperity"),
             (val_div, ":tariffs_generated", 100),
             (val_div, ":tariffs_generated", 20), ######10 for caravans, 20 for villages
             (val_add, ":accumulated_tariffs", ":tariffs_generated"),

             (try_begin),

                (ge, "$cheat_mode", 3),
                (assign, reg4, ":tariffs_generated"),

                (str_store_party_name, s4, ":cur_ai_object"),
                (assign, reg5, ":accumulated_tariffs"),
                (display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
             (try_end),

             (party_set_slot, ":cur_ai_object", slot_center_accumulated_tariffs, ":accumulated_tariffs"),

            ########### ######Increasing food stocks of the town
             (party_get_slot, ":town_food_store", ":cur_ai_object", slot_party_food_store),
             (call_script, "script_center_get_food_store_limit", ":cur_ai_object"),
             (assign, ":food_store_limit", reg0),
             (val_add, ":town_food_store", 1000),
             (val_min, ":town_food_store", ":food_store_limit"),
             (party_set_slot, ":cur_ai_object", slot_party_food_store, ":town_food_store"),

            ########### ######Adding 1 to village prosperity
             (try_begin),
               (store_random_in_range, ":rand", 0, 100),
               (lt, ":rand", 35),
               (call_script, "script_change_center_prosperity", ":home_center", 1),
               (val_add, "$newglob_total_prosperity_from_village_trade", 1),
             (try_end),
           (try_end),

           ##########Moving farmers to their home village
           (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":home_center"),
         (try_end),
       (try_end),
       ##########(display_message, "@farmers thinking end...", 0xff0000),
    ]),

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
 ######Increase castle food stores
  ######### (6,
(0.06,      ###################### once every 12 hours for each of the 200 castles
[
 (try_begin),
   (lt, "$g_increase_castle_food_stores_cur_castle", castles_begin), 
   (assign, "$g_increase_castle_food_stores_cur_castle", castles_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_increase_castle_food_stores_cur_castle", castles_end), 
   (assign, "$g_increase_castle_food_stores_cur_castle", castles_begin),
 (try_end),
 
 (try_begin),
   (party_slot_eq, "$g_increase_castle_food_stores_cur_castle", slot_center_is_besieged_by, -1), ######castle is not under siege
   (party_get_slot, ":center_food_store", "$g_increase_castle_food_stores_cur_castle", slot_party_food_store),
   (val_add, ":center_food_store", 100),
   (call_script, "script_center_get_food_store_limit", "$g_increase_castle_food_stores_cur_castle"),
   (assign, ":food_store_limit", reg0),
   (val_min, ":center_food_store", ":food_store_limit"),
 
   (party_set_slot, "$g_increase_castle_food_stores_cur_castle", slot_party_food_store, ":center_food_store"),
 (try_end),
 
 ################ proceeds to the next castle when it's triggered again
 (val_add, "$g_increase_castle_food_stores_cur_castle", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_28", 1),
]),
######################################################################


 ######cache party strengths (to avoid re-calculating)
#####  (2,
#####   [
#####       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
#####         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
#####         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
#####         (ge, ":cur_party", 0),
#####         (call_script, "script_party_calculate_strength", ":cur_party", 0), ######will update slot_party_cached_strength
#####       (try_end),
#####    ]),
##
#####  (6,
#####   [
#####       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
#####         (call_script, "script_party_calculate_strength", ":cur_center", 0), ######will update slot_party_cached_strength
#####       (try_end),
#####    ]),

#####  (1,
#####   [
#####       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
#####         (store_random_in_range, ":rand", 0, 100),
#####         (lt, ":rand", 10),
#####         (store_faction_of_party, ":center_faction", ":cur_center"),
#####         (assign, ":friend_strength", 0),
#####         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
#####           (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
#####           (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
#####           (gt, ":cur_troop_party", 0),
#####           (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":cur_center"),
#####           (lt, ":distance", 10),
#####           (store_troop_faction, ":army_faction", ":cur_troop"),
#####           (store_relation, ":rel", ":army_faction", ":center_faction"),
#####           (try_begin),
#####             (gt, ":rel", 10),
#####             (party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
#####             (val_add, ":friend_strength", ":str"),
#####           (try_end),
#####         (try_end),
#####         (party_set_slot, ":cur_center", slot_party_nearby_friend_strength, ":friend_strength"),
#####       (try_end),
#####    ]),

  ######### Make heroes running away from someone retreat to friendly centers
  # (0.2, ######TOM was 0.1
  (0.5, 
   [
      ######(display_message, "@heroes running away start...", 0xff0000),

       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
         (gt, ":cur_party", 0),
         (try_begin),
           (party_is_active, ":cur_party"),
           (try_begin),
             (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
             (eq, ":ai_bhvr", ai_bhvr_avoid_party),

             ######Certain lord personalities will not abandon a battlefield to flee to a fortress
             (assign, ":continue", 1),
             (try_begin),
                (this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_upstanding),
                    (troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_martial),
                (get_party_ai_current_object, ":ai_object", ":cur_party"),
                (party_is_active, ":ai_object"),
                (party_get_battle_opponent, ":battle_opponent", ":ai_object"),
                (party_is_active, ":battle_opponent"),
                (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),


             (store_faction_of_party, ":party_faction", ":cur_party"),
             (party_get_slot, ":commander_party", ":cur_party", slot_party_commander_party),
             (faction_get_slot, ":faction_marshall", ":party_faction", slot_faction_marshall),
             (neq, ":faction_marshall", ":cur_troop"),
             (assign, ":continue", 1),
             (try_begin),
               (ge, ":faction_marshall", 0),
               (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
               (party_is_active, ":faction_marshall_party", 0),
               (eq, ":commander_party", ":faction_marshall_party"),
               (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),
             (assign, ":done", 0),
             (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
               (eq, ":done", 0),
               (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
               (store_faction_of_party, ":center_faction", ":cur_center"),
               (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
               (gt, ":cur_relation", 0),
               (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
               (lt, ":cur_distance", 20),
               (party_get_position, pos1, ":cur_party"),
               (party_get_position, pos2, ":cur_center"),
               (neg|position_is_behind_position, pos2, pos1),
               (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
               (assign, ":done", 1),
             (try_end),
           (try_end),
         (else_try),
           (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
         (try_end),
       (try_end),
       ######(display_message, "@heroes running away end...", 0xff0000),
    ]),

  ######### Centers give alarm if the player is around
  ######### (0.5,
   (1,
    [
      ######(display_message, "@player center alarms start...", 0xff0000),
      (store_current_hours, ":cur_hours"),
      (store_mod, ":cur_hours_mod", ":cur_hours", 11),
      (store_sub, ":hour_limit", ":cur_hours", 5),
      (party_get_num_companions, ":num_men", "p_main_party"),
      (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
      (val_add, ":num_men", ":num_prisoners"),
      (convert_to_fixed_point, ":num_men"),
      (store_sqrt, ":num_men_effect", ":num_men"),
      (convert_from_fixed_point, ":num_men_effect"),
      (try_begin),
        (eq, ":cur_hours_mod", 0),
        ######Reduce alarm by 2 in every 11 hours.
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
          (val_sub, ":player_alarm", 1),
          (val_max, ":player_alarm", 0),
          (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
        (try_end),
      (try_end),
      (eq, "$g_player_is_captive", 0),
      (try_for_range, ":cur_center", centers_begin, centers_end),
        (store_faction_of_party, ":cur_faction", ":cur_center"),
        (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
        (lt, ":reln", 0),
        (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
        (lt, ":dist", 5),
        (store_mul, ":dist_sqr", ":dist", ":dist"),
        (store_sub, ":dist_effect", 20, ":dist_sqr"),
        (store_sub, ":reln_effect", 20, ":reln"),
        (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
        (val_mul, ":total_effect", ":num_men_effect"),
        (store_div, ":spot_chance", ":total_effect", 10),
        (store_random_in_range, ":random_spot", 0, 1000),
        (lt, ":random_spot", ":spot_chance"),
        (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
        (val_add, ":player_alarm", 1),
        (val_min, ":player_alarm", 100),
        (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
        (try_begin),
          (neg|party_slot_ge, ":cur_center", slot_center_last_player_alarm_hour, ":hour_limit"),
          (str_store_party_name_link, s1, ":cur_center"),
          (display_message, "@Your party is spotted by {s1}."),
          (party_set_slot, ":cur_center", slot_center_last_player_alarm_hour, ":cur_hours"),
        (try_end),
      (try_end),
      ######(display_message, "@player center alarms end...", 0x00ff00),
    ]),
######################### Consuming food at every 14 hours
(12,
[
 (eq, "$g_player_is_captive", 0),
 (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
 (assign, ":num_men", 0),
 (try_for_range, ":i_stack", 0, ":num_stacks"),
   (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
   (val_add, ":num_men", ":stack_size"),
 (try_end),
 (val_div, ":num_men", 3),
 (try_begin),
   (eq, ":num_men", 0),
   (val_add, ":num_men", 1),
 (try_end),
 
 ########## Jrider + FORAGING v1.0, add foraging
 (call_script, "script_forage_for_food"),
 
 ######### backup original number for message display
 (assign, ":orig_men", ":num_men"),
 (try_begin),
   ######### set min consumption to 1 unit of food in inventory
   (ge, reg4, ":num_men"),
   (assign, ":num_men", 1),
 (else_try),
   ######### else deduct foraged amount from consumed from party size
   (val_sub, ":num_men", reg4),
 (try_end),
 ########## Jrider -
 
 (try_begin),
   (assign, ":number_of_foods_player_has", 0),
   (try_for_range, ":cur_edible", food_begin, food_end),
     (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
     (val_add, ":number_of_foods_player_has", 1),
   (try_end),
   ######### (try_begin),
     ######### (ge, ":number_of_foods_player_has", 6),
     ######### (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),
   ######### (try_end),
 (try_end),
 
 (assign, ":consumption_amount", ":num_men"),
 (assign, ":no_food_displayed", 0),
 
 ################ NEW v1.9 - halves the amount of food consumed when resting in a fief
 (try_begin),
   (eq, "$g_town_visit_after_rest", 1),
     (val_div, ":consumption_amount", 2),
 (try_end),
 ####################################
 
 ################ NEW v2.0 - fixes bug where player didn't consume any food if he was the only member in the party
 (try_begin),
   (eq, ":consumption_amount", 0),
     (assign, ":consumption_amount", 1),
 (try_end),
 ####################################
 
 (try_for_range, ":unused", 0, ":consumption_amount"),
   (assign, ":available_food", 0),
   (try_for_range, ":cur_food", food_begin, food_end),
     (item_set_slot, ":cur_food", slot_item_is_checked, 0),
     (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
     (val_add, ":available_food", 1),
   (try_end),
   (try_begin),
     (gt, ":available_food", 0),
     (store_random_in_range, ":selected_food", 0, ":available_food"),
     (call_script, "script_consume_food", ":selected_food"),
   (else_try),
     (eq, ":no_food_displayed", 0),
     (display_message, "@Party has nothing to eat!", 0xFF0000),
     (call_script, "script_change_player_party_morale", -3),
     (assign, ":no_food_displayed", 1),
#NPC companion changes begin
     (try_begin),
         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (gt, reg0, 0),
         (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
     (try_end),
#NPC companion changes end
   (try_end),
 (try_end),
 ################ NEW v1.9 - display the message that consumption was halved
 (try_begin),
   (eq, "$g_town_visit_after_rest", 1),
   (gt, ":consumption_amount", 1),  ############ NEW v2.1 - if it's 1 don't display anything
     (display_message, "@Party is stationed and therefore consumes half the food required.", 0x3399FF),
 (try_end),
 ####################################
 ########## Jrider + FORAGING v1.0, call food consummed/left script
 (call_script, "script_food_consumption_display_message", ":consumption_amount"),
 ########## Jrider -
 
#### Party Morale: Move morale towards target value.
 (call_script, "script_get_player_party_morale_values"),
 (assign, ":target_morale", reg1),
 (party_get_morale, ":cur_morale", "p_main_party"),
 (store_sub, ":dif", ":target_morale", ":cur_morale"),
 ######### leadership modifier 
 (store_skill_level, ":skill", "skl_leadership", "trp_player"),
 (try_begin),
   (gt, ":dif", 0),
   (store_add, ":morale_change_factor", 20, ":skill"),
 (else_try),
   (store_sub, ":morale_change_factor", 20, ":skill"),
 (try_end),
 (store_mul, ":dif_to_add", ":dif", ":morale_change_factor"),
 (val_div, ":dif_to_add", 100),
 (store_mul, ":dif_to_add_correction", ":dif_to_add", 100),
 (val_div, ":dif_to_add_correction", ":morale_change_factor"),
 ######### leadership modifier 
 (try_begin),#finding ceiling of the value
   (neq, ":dif_to_add_correction", ":dif"),
   (try_begin),
     (gt, ":dif", 0),
     (val_add, ":dif_to_add", 1),
   (else_try),
     (val_sub, ":dif_to_add", 1),
   (try_end),
 (try_end),
 (val_add, ":cur_morale", ":dif_to_add"),
 (val_clamp, ":cur_morale", 0, 100),
 (party_set_morale, "p_main_party", ":cur_morale"),
 (assign, reg1, ":cur_morale"),
]),
#####################################################################################


    
    
  ######### Setting item modifiers for food
  (24,
   [
     (troop_get_inventory_capacity, ":inv_size", "trp_player"),
     (try_for_range, ":i_slot", 0, ":inv_size"),
       (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
       (this_or_next|eq, ":item_id", "itm_cattle_meat"),
       (this_or_next|eq, ":item_id", "itm_chicken"),
       (eq, ":item_id", "itm_pork"),

       (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
       (try_begin),
         (ge, ":modifier", imod_fresh),
         (lt, ":modifier", imod_rotten),
         (val_add, ":modifier", 1),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
       (else_try),
         (lt, ":modifier", imod_fresh),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
       (try_end),
     (try_end),
    ]),

  ######### Assigning lords to centers with no leaders
  ###### (72,
   ###### [
   ######(call_script, "script_assign_lords_to_empty_centers"),
    ###### ]),

  ######### Updating player icon in every frame
  ######### (0,
  (0.2,
   [(troop_get_inventory_slot, ":cur_horse", "trp_player", 8), ######horse slot
    (assign, ":new_icon", -1),
    (try_begin),
      (eq, "$g_player_icon_state", pis_normal),
      (try_begin),
        (ge, ":cur_horse", 0),
        (assign, ":new_icon", "icon_player_horseman"),
      (else_try),
        (assign, ":new_icon", "icon_player"),
      (try_end),
    (else_try),
      (eq, "$g_player_icon_state", pis_camping),
      (assign, ":new_icon", "icon_camp"),
    (else_try),
      (eq, "$g_player_icon_state", pis_ship),
      (assign, ":new_icon", "icon_ship"),
    (try_end),

    (try_begin),
      (call_script, "script_cf_is_party_on_water", "p_main_party"),
      (assign, ":new_icon", "icon_longship"),
    (try_end),

    (neq, ":new_icon", "$g_player_party_icon"),
    (assign, "$g_player_party_icon", ":new_icon"),
    (party_set_icon, "p_main_party", ":new_icon"),
    ]),

 ######Update how good a target player is for bandits
  (4, ######TOM was 2
   [
       (store_troop_gold, ":total_value", "trp_player"),
       (store_div, ":bandit_attraction", ":total_value", (10000/100)), ######10000 gold = excellent_target

       (troop_get_inventory_capacity, ":inv_size", "trp_player"),
       (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
       (try_end),
       (val_clamp, ":bandit_attraction", 0, 100),
       (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),


    ######This is a backup script to activate the player faction if it doesn't happen automatically, for whatever reason
  ######### (3,
  (6,
    [
    (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
    (try_for_range, ":center", walled_centers_begin, walled_centers_end),
      (store_faction_of_party, ":center_faction", ":center"),
      (eq, ":center_faction", "fac_player_supporters_faction"),
        (call_script, "script_activate_player_faction", "trp_player"),
    (try_end),
    ]),

  ######### Checking escape chances of prisoners that joined the party recently.
  (6,
   [(gt, "$g_prisoner_recruit_troop_id", 0),
    (gt, "$g_prisoner_recruit_size", 0),
    (gt, "$g_prisoner_recruit_last_time", 0),
    (is_currently_night),
    (try_begin),
      (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
      (val_mul, ":leadership", 5),
      (store_sub, ":chance", 66, ":leadership"),
      (gt, ":chance", 0),
      (assign, ":num_escaped", 0),
      (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", ":chance"),
        (val_add, ":num_escaped", 1),
      (try_end),
      (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (assign, ":num_escaped", reg0),
      (gt, ":num_escaped", 0),
      (try_begin),
        (gt, ":num_escaped", 1),
        (assign, reg2, 1),
      (else_try),
        (assign, reg2, 0),
      (try_end),
      (assign, reg1, ":num_escaped"),
      (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night."),
    (try_end),
    (assign, "$g_prisoner_recruit_troop_id", 0),
    (assign, "$g_prisoner_recruit_size", 0),
    ]),

  ######### Offering ransom fees for player's prisoner heroes
  (24,
   [(neq, "$g_ransom_offer_rejected", 1),
    (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
    (eq, reg0, 0),#no prisoners offered
    (assign, ":end_cond", walled_centers_end),
    (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
      (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
      (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
      (eq, reg0, 1),#a prisoner is offered
      (assign, ":end_cond", 0),#break
    (try_end),
    ]),

    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### split in two, other half below
#### Exchanging hero prisoners between factions and clearing old ransom offers
(0.23,   ###################### roughly once every 72 hours for each of the 311 walled centers
[
 (try_begin),
   (lt, "$g_exchange_prisoners_cur_center", walled_centers_begin), 
   (assign, "$g_exchange_prisoners_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_exchange_prisoners_cur_center", walled_centers_end), 
   (assign, "$g_exchange_prisoners_cur_center", walled_centers_begin),
 (try_end),
 
 ###### (assign, "$g_ransom_offer_rejected", 0),
 (try_begin),
   (party_get_slot, ":town_lord", "$g_exchange_prisoners_cur_center", slot_town_lord),
   (gt, ":town_lord", 0),
   (party_get_num_prisoner_stacks, ":num_stacks", "$g_exchange_prisoners_cur_center"),
   (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
     (party_prisoner_stack_get_troop_id, ":stack_troop", "$g_exchange_prisoners_cur_center", ":i_stack"),
     (troop_is_hero, ":stack_troop"),
     (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
     (store_random_in_range, ":random_no", 0, 100),
     (try_begin),
       (le, ":random_no", 10),
       (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
       (assign, ":ransom_amount", reg0),
       (troop_get_slot, ":wealth", ":town_lord", slot_troop_wealth),
       (val_add, ":wealth", ":ransom_amount"),
       (troop_set_slot, ":town_lord", slot_troop_wealth, ":wealth"),
       (party_remove_prisoners, "$g_exchange_prisoners_cur_center", ":stack_troop", 1),
       (call_script, "script_remove_troop_from_prison", ":stack_troop"),
       (store_troop_faction, ":faction_no", ":town_lord"),
       (store_troop_faction, ":troop_faction", ":stack_troop"),
       (str_store_troop_name, s1, ":stack_troop"),
       (str_store_faction_name, s2, ":faction_no"),
       (str_store_faction_name, s3, ":troop_faction"),
       ######### rafi
       (store_relation, ":rel", ":troop_faction", "$players_kingdom"),
       (try_begin),
         (this_or_next | lt, ":rel", 0),
         (eq, ":troop_faction", "$players_kingdom"),
         (display_log_message, "@{s1} of {s3} has been released from captivity."),
       (try_end),
       ######### end rafi
     (try_end),
   (try_end),
 (try_end),
 
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_exchange_prisoners_cur_center", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_29", 1),
]),
#####################
    
    
##################### other half 
(72,   
[
 (assign, "$g_ransom_offer_rejected", 0),
]),
#####################
    
    
    
  ######### Adding mercenary troops to the towns #### this is in the enhanced menu simple trigger far below
  ######### (72,
   ######### [
     ######### (call_script, "script_update_mercenary_units_of_towns"),
     ######### ######NPC changes begin
     ######### ######### removes   (call_script, "script_update_companion_candidates_in_taverns"),
     ######### ######NPC changes end
     ######### (call_script, "script_update_ransom_brokers"),
     ######### (call_script, "script_update_tavern_travellers"),
     ######### (call_script, "script_update_tavern_minstrels"),
     ######### (call_script, "script_update_booksellers"),
     ######### (call_script, "script_update_villages_infested_by_bandits"),
     ######### (try_for_range, ":village_no", villages_begin, villages_end),
       ######### (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
       ######### (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
     ######### (try_end),
    ######### ]),
  ######### Adding mercenary troops to the towns

##################### splitted in 3, others are below this
  (72,
   [
   ######### (call_script, "script_update_mercenary_units_of_towns"),
#NPC changes begin
#### removes   (call_script, "script_update_companion_candidates_in_taverns"),
#NPC changes end
    (call_script, "script_update_ransom_brokers"),
    (call_script, "script_update_tavern_travellers"),
    (call_script, "script_update_tavern_minstrels"),
    (call_script, "script_update_booksellers"),
    #################### manors work differently from villages so it's not in the next trigger
    (call_script, "script_update_manor_infested_by_bandits"),     ######TOM
    ]),
#############


################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################ other 1/3 - for villages
(0.17,            ######################## once every 72 hours for each of the 422 villages
[
 (try_begin),
   (lt, "$g_update_villages_cur_village", villages_begin), 
   (assign, "$g_update_villages_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_update_villages_cur_village", villages_end), 
   (assign, "$g_update_villages_cur_village", villages_begin),
 (try_end),
   
 (call_script, "script_update_villages_infested_by_bandits", "$g_update_villages_cur_village"),
 
 (try_begin),
   (eq, "$use_feudal_lance", 0), #######tom - if using old recruitment system
     (call_script, "script_update_volunteer_troops_in_village", "$g_update_villages_cur_village"),
     (call_script, "script_update_npc_volunteer_troops_in_village", "$g_update_villages_cur_village"),
 (try_end),
 (try_begin),
   (eq, "$use_feudal_lance", 0), #######tom - if using old recruitment system
     (call_script, "script_update_volunteer_troops_in_village", "$g_update_villages_cur_village"),
     (call_script, "script_update_npc_volunteer_troops_in_village", "$g_update_villages_cur_village"),
 (try_end),
 
 ################ proceeds to the next village when it's triggered again
 (val_add, "$g_update_villages_cur_village", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_30", 1),
]),
#############
    
    
################ other 1/3 - for castles
(0.36,            ######################## once every 72 hours for each of the 200 castles
[
 (try_begin),
   (eq, "$use_feudal_lance", 0), #######tom - if using old recruitment system
   (try_begin),
     (lt, "$g_update_villages_cur_castle", castles_begin), 
     (assign, "$g_update_villages_cur_castle", castles_begin),
   (try_end),
   
   (try_begin),
     (ge, "$g_update_villages_cur_castle", castles_end), 
     (assign, "$g_update_villages_cur_castle", castles_begin),
   (try_end),
     
         
   (try_begin),
     (call_script, "script_update_volunteer_troops_in_village", "$g_update_villages_cur_castle"),
     (call_script, "script_update_npc_volunteer_troops_in_village", "$g_update_villages_cur_castle"),
   (try_end),
   
   ################ proceeds to the next village when it's triggered again
   (val_add, "$g_update_villages_cur_castle", 1),
    
   ################### DEBUG
   (val_add, "$g_simple_trigger_fire_count_31", 1),
 (try_end),
]),
#################################################################
    
    

  (24,
   [
    (call_script, "script_update_other_taverngoers"),
    ]),

    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Setting random walker types
(0.049,  ########################## once every 36 hours for each of the 733 centers
[
 (try_begin),
   (lt, "$g_set_random_walker_types_cur_center", centers_begin), 
   (assign, "$g_set_random_walker_types_cur_center", centers_begin),
 (try_end),

 (try_begin),
   (ge, "$g_set_random_walker_types_cur_center", centers_end), 
   (assign, "$g_set_random_walker_types_cur_center", centers_begin),
 (try_end),

 (try_begin),
    (this_or_next|party_slot_eq, "$g_set_random_walker_types_cur_center", slot_party_type, spt_town),
    (party_slot_eq, "$g_set_random_walker_types_cur_center", slot_party_type, spt_village),
    (call_script, "script_center_remove_walker_type_from_walkers", "$g_set_random_walker_types_cur_center", walkert_needs_money),
    (call_script, "script_center_remove_walker_type_from_walkers", "$g_set_random_walker_types_cur_center", walkert_needs_money_helped),
    (store_random_in_range, ":rand", 0, 100),
    (try_begin),
      (lt, ":rand", 70),
      (neg|party_slot_ge, "$g_set_random_walker_types_cur_center", slot_town_prosperity, 60),
      (call_script, "script_cf_center_get_free_walker", "$g_set_random_walker_types_cur_center"),
      (call_script, "script_center_set_walker_to_type", "$g_set_random_walker_types_cur_center", reg0, walkert_needs_money),
    (try_end),
 (try_end),
  
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_set_random_walker_types_cur_center", 1),
     
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_32", 1),
]),
###########################################################################
    
    
    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Checking center upgrades
(0.032,   ##################### twice a day for each of the 733 centers - script executed twice
[
 (try_begin),
   (lt, "$g_check_center_improvements_cur_center", centers_begin), 
   (assign, "$g_check_center_improvements_cur_center", centers_begin),
 (try_end),

 (try_begin),
   (ge, "$g_check_center_improvements_cur_center", centers_end), 
   (assign, "$g_check_center_improvements_cur_center", centers_begin),
 (try_end),
    
 (call_script, "script_process_center_upgrades", "$g_check_center_improvements_cur_center"),
 ################ proceeds to the next center
 (val_add, "$g_check_center_improvements_cur_center", 1),
 
 (call_script, "script_process_center_upgrades", "$g_check_center_improvements_cur_center"),
 ################ proceeds to the next center
 (val_add, "$g_check_center_improvements_cur_center", 1),
     
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_33", 2),
]),
#################################################################################

    
    
    
    
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################# splitted in half, other half below this
#### Adding bandits to towns and villages
#### (24,
(0.032,  ################### once a day for each of the 733 centers
[
 (try_begin),
   (lt, "$g_add_bandit_to_fief_cur_fief", centers_begin), 
   (assign, "$g_add_bandit_to_fief_cur_fief", centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_add_bandit_to_fief_cur_fief", centers_end), 
   (assign, "$g_add_bandit_to_fief_cur_fief", centers_begin),
 (try_end),
   
 (call_script, "script_add_bandits_to_towns_and_villages", "$g_add_bandit_to_fief_cur_fief"),
 
 ################ proceeds to the next fief when it's triggered again
 (val_add, "$g_add_bandit_to_fief_cur_fief", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_34", 1),
]), 
####################
    
    
####################### other half
#### Adding tournaments to towns
(24,
[
 (assign, ":num_active_tournaments", 0),
 (try_for_range, ":center_no", towns_begin, towns_end),
   (party_get_slot, ":has_tournament", ":center_no", slot_town_has_tournament),
   (try_begin),
     (eq, ":has_tournament", 1),#tournament ended, simulate
       (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
       (call_script, "script_sort_tournament_participant_troops"),#may not be needed
       (call_script, "script_get_num_tournament_participants"),
       (store_sub, ":needed_to_remove_randomly", reg0, 1),
       (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
       (call_script, "script_sort_tournament_participant_troops"),
       (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
       (try_begin),
         (is_between, ":winner_troop", active_npcs_begin, active_npcs_end),
         (str_store_troop_name_link, s1, ":winner_troop"),
         (str_store_party_name_link, s2, ":center_no"),
         (display_message, "@{s1} has won the tournament at {s2}."),
         (call_script, "script_change_troop_renown", ":winner_troop", 20),
       (try_end),
   (try_end),
   (val_sub, ":has_tournament", 1),
   (val_max, ":has_tournament", 0),
   (party_set_slot, ":center_no", slot_town_has_tournament, ":has_tournament"),
   (try_begin),
     (gt, ":has_tournament", 0),
       (val_add, ":num_active_tournaments", 1),
   (try_end),
 (try_end),
 
 (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
     (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
     (is_between, ":faction_object", towns_begin, towns_end),
     (party_slot_ge, ":faction_object", slot_town_has_tournament, 1),
     ######continue holding tournaments during the feast
       (party_set_slot, ":faction_object", slot_town_has_tournament, 2),
 (try_end),
 
 (try_begin),
   (lt, ":num_active_tournaments", 8),
     (store_random_in_range, ":random_no", 0, 100),
     ######Add new tournaments with a 30% chance if there are less than 3 tournaments going on
     ######(lt, ":random_no", 30),
     ######### rafi reduce the number of tournaments, 6% chance
     (lt, ":random_no", 29),
     ######### end
       (store_random_in_range, ":random_town", towns_begin, towns_end),
       (store_random_in_range, ":random_days", 5, 7),
       (party_set_slot, ":random_town", slot_town_has_tournament, ":random_days"),
       (try_begin),
         (eq, "$cheat_mode", 1),
         (str_store_party_name, s1, ":random_town"),
         (display_message, "@{!}{s1} is holding a tournament."),
       (try_end),
 (try_end),
]),
################################################################################
    
    
    
    
(3,
[
 (assign, "$g_player_tournament_placement", 0),
]),



#(0.1,

#    [
#    (try_begin),
#        (troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
#        (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#        (store_faction_of_troop, ":spouse_faction", ":spouse"),
#        (neq, ":spouse_faction", "$players_kingdom"),
#        (display_message, "@{!}ERROR! Player and spouse are separate factions"),
#    (try_end),
#    ]
#),

  ######### Asking to give center to player
  ######### (8,
   ######### [
####    (assign, ":done", 0),
####    (try_for_range, ":center_no", centers_begin, centers_end),
####      (eq, ":done", 0),
####      (party_slot_eq, ":center_no", slot_town_lord, stl_reserved_for_player),
####      (assign, "$g_center_to_give_to_player", ":center_no"),
 #########     (try_begin),
  #########      (eq, "$g_center_to_give_to_player", "$g_castle_requested_by_player"),
   #########     (assign, "$g_castle_requested_by_player", 0),
    ######    (try_begin),
    ######        (eq, "$g_castle_requested_for_troop", "trp_player"),
    ######        (jump_to_menu, "mnu_requested_castle_granted_to_player"),
    ######    (else_try),
    ######        (jump_to_menu, "mnu_requested_castle_granted_to_player_husband"),
    ######    (try_end),
    #########  (else_try),
    #########    (jump_to_menu, "mnu_give_center_to_player"),
    ######### (try_end),
    #########  (assign, ":done", 1),
    ######(else_try),
    #########  (eq, ":center_no", "$g_castle_requested_by_player"),
    #########  (party_slot_ge, ":center_no", slot_town_lord, active_npcs_begin),
    #########  (assign, "$g_castle_requested_by_player", 0),
    #########  (store_faction_of_party, ":faction", ":center_no"),
    #########  (eq, ":faction", "$players_kingdom"),
    #########  (assign, "$g_center_to_give_to_player", ":center_no"),
    #########  (try_begin),
#        (eq, "$player_has_homage", 1),
#        (jump_to_menu, "mnu_requested_castle_granted_to_another"),
#      (else_try),
#        (jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
#      (try_end),
 #########     (assign, ":done", 1),
  #########  (try_end),
    ######### ]),

  ######### Taking denars from player while resting in not owned centers
  (1,
   [(neg|map_free),
    (is_currently_night),
####    (ge, "$g_last_rest_center", 0),
    (is_between, "$g_last_rest_center", centers_begin, centers_end),
    (neg|party_slot_eq, "$g_last_rest_center", slot_town_lord, "trp_player"),
    (store_faction_of_party, ":last_rest_center_faction", "$g_last_rest_center"),
    (neq, ":last_rest_center_faction", "fac_player_supporters_faction"),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", "$g_last_rest_payment_until"),
    (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
    (store_troop_gold, ":gold", "trp_player"),
    (party_get_num_companions, ":num_men", "p_main_party"),
    (store_div, ":total_cost", ":num_men", 4),
    (val_add, ":total_cost", 1),
    (try_begin),
      (ge, ":gold", ":total_cost"),
      (display_message, "@You pay for accommodation."),
      (troop_remove_gold, "trp_player", ":total_cost"),
    (else_try),
      (gt, ":gold", 0),
      (troop_remove_gold, "trp_player", ":gold"),
    (try_end),
    ]),

    
    ######### (4,
    ######### [
      ##########tom
      ######### (try_begin),
        
        ######### (store_num_parties_of_template, ":num_parties", "pt_crusaders"),
        ######### (display_message, "@Crusade against the infidels have started!"),
        ######### (lt, ":num_parties",1),
        ######### (set_spawn_radius, 5),
        ######### (spawn_around_party, "p_town_21_1", "pt_crusaders"),
        ######### (assign, ":party_id", reg0),
        ########### (party_set_ai_behavior, ":party_id", ai_bhvr_attack_party),
                ############ (party_set_ai_object, ":party_id", "p_town_21_1"),
        ########### (party_set_slot, ":party_id", ai_bhvr_travel_to_party, "p_town_21_1"),
        
        ######### (assign, "$crusader_party_id", ":party_id"),
        ######### (assign, "$crusader_siege", 0),
        ######### (call_script, "script_party_set_ai_state", "$crusader_party_id", spai_besieging_center, "p_town_21_1"),
      ######### (else_try),
        ########(call_script, "script_party_set_ai_state", "$crusader_party_id", spai_besieging_center, "p_town_21_1"),
        ######### (party_get_slot, ":ai_object", "$crusader_party_id", slot_party_ai_object),
        ######### (store_distance_to_party_from_party, ":distance", "$crusader_party_id", ":ai_object"),
        ######### (lt, ":distance", 3),
        ######### (neq, "$crusader_siege", 1),
        ######### (store_current_hours, ":cur_hours"),
        ######### (party_set_slot, ":ai_object", slot_center_is_besieged_by, "$crusader_party_id"), ######gali but kad party pasikeis, ie gaudys kokius pydarus?
        ######### (party_set_slot, ":ai_object", slot_center_siege_begin_hours, ":cur_hours"),
        ########(call_script, "script_begin_assault_on_center", ":ai_object"),
         ######### (party_set_ai_behavior, "$crusader_party_id", ai_bhvr_attack_party),
          ######### (party_set_ai_object, "$crusader_party_id", "p_town_21_1"),
          ######### (party_set_flags, "$crusader_party_id", pf_default_behavior, 1),
          ######### (party_set_slot, "$crusader_party_id", slot_party_ai_substate, 1),
          ######### (assign, "$crusader_siege", 1),    
      ######### (else_try),
         ######### (store_num_parties_of_template, ":num_parties", "pt_crusaders"),
         ######### (lt, ":num_parties",1),
         ######### (eq, "$crusader_siege", 0),    
         ######### (call_script, "script_party_set_ai_state", "$crusader_party_id", spai_besieging_center, "p_town_21_1"), ######refresh this, or not needed?      
      ######### (try_end),
       #######tom
    ######### ]
    ######### ),

  ######### Make parties larger as game progresses.
  (24,
   [
       (call_script, "script_update_party_creation_random_limits"),
    ]),

	
	
	
  ######### Check if a faction is defeated every day
  (24,
   [
    (assign, ":num_active_factions", 0),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_set_slot, ":cur_kingdom", slot_faction_number_of_parties, 0),
    (try_end),
    (try_for_parties, ":cur_party"),
      (store_faction_of_party, ":party_faction", ":cur_party"),
      (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
      (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
        (party_slot_eq, ":cur_party", slot_party_type, spt_kingdom_hero_party),
      (faction_get_slot, ":kingdom_num_parties", ":party_faction", slot_faction_number_of_parties),
      (val_add, ":kingdom_num_parties", 1),
      (faction_set_slot, ":party_faction", slot_faction_number_of_parties, ":kingdom_num_parties"),
    (try_end),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
#####      (try_begin),
#####        (eq, "$cheat_mode", 1),
#####        (str_store_faction_name, s1, ":cur_kingdom"),
#####        (faction_get_slot, reg1, ":cur_kingdom", slot_faction_number_of_parties),
#####        (display_message, "@{!}Number of parties belonging to {s1}: {reg1}"),
#####      (try_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      (val_add, ":num_active_factions", 1),
      (faction_slot_eq, ":cur_kingdom", slot_faction_number_of_parties, 0),
      (assign, ":faction_removed", 0),
      (try_begin),
        (eq, ":cur_kingdom", "fac_player_supporters_faction"),
        (try_begin),
          (le, "$supported_pretender", 0),
          (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_inactive),
          (assign, ":faction_removed", 1),
        (try_end),
      (else_try),
        (neq, "$players_kingdom", ":cur_kingdom"),
        (faction_set_slot, ":cur_kingdom", slot_faction_state, sfs_defeated),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (eq, ":party_faction", ":cur_kingdom"),
          (party_get_slot, ":home_center", ":cur_party", slot_party_home_center),
          (store_faction_of_party, ":home_center_faction", ":home_center"),
          (party_set_faction, ":cur_party", ":home_center_faction"),
        (try_end),
        (assign, ":kingdom_pretender", -1),
        (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
          (troop_slot_eq, ":cur_pretender", slot_troop_original_faction, ":cur_kingdom"),
          (assign, ":kingdom_pretender", ":cur_pretender"),
        (try_end),
        (try_begin),
          (is_between, ":kingdom_pretender", pretenders_begin, pretenders_end),
          (neq, ":kingdom_pretender", "$supported_pretender"),
          (troop_set_slot, ":kingdom_pretender", slot_troop_cur_center, 0), ######remove pretender from the world
        (try_end),
        (assign, ":faction_removed", 1),
        (try_begin),
          (eq, "$players_oath_renounced_against_kingdom", ":cur_kingdom"),
          (assign, "$players_oath_renounced_against_kingdom", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_kingdom", 0),
        (try_end),
        ######This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_kingdom
        (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_kingdom", 0),
      (try_end),
      (try_begin),
        (eq, ":faction_removed", 1),
        (val_sub, ":num_active_factions", 1),
        ######(call_script, "script_store_average_center_value_per_faction"),
      (try_end),
      (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom_2"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":num_active_factions", 1),
      (eq, "$g_one_faction_left_notification_shown", 0),
      (assign, "$g_one_faction_left_notification_shown", 1),
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
        (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_kingdom", 0),
      (try_end),
    (try_end),
    ]),

    
    
    
############### NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
################### cut in half, other half below
(3, ######check to see if player's court has been captured
[
 (try_begin), ######The old court has been lost
  ################ diplomacy begin
    (is_between, "$g_player_court", centers_begin, centers_end),
    (party_slot_eq, "$g_player_court", slot_village_infested_by_bandits, "trp_peasant_woman"),
      (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
  (else_try),
  ################ diplomacy end
    (is_between, "$g_player_court", centers_begin, centers_end),
     (store_faction_of_party, ":court_faction", "$g_player_court"),
     (neq, ":court_faction", "fac_player_supporters_faction"),
     (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
 (else_try),    ######At least one new court has been found
   (lt, "$g_player_court", centers_begin),
   ############### Will by definition not active until a center is taken by the player faction
   ############### Player minister must have been appointed at some point
   (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
   (gt, "$g_player_minister", 0),
     (assign, ":center_found", 0),
     (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
       (eq, ":center_found", 0),
         (store_faction_of_party, ":court_faction", ":walled_center"),
         (eq, ":court_faction", "fac_player_supporters_faction"),
           (assign, ":center_found", ":walled_center"),
     (try_end),
     (ge, ":center_found", 1),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
 (try_end),
 
##### Piggybacking on trigger:
 (try_begin),
   (troop_get_slot, ":betrothed", "trp_player", slot_troop_betrothed),
   (gt, ":betrothed", 0),
   (neg|check_quest_active, "qst_wed_betrothed"),
   (neg|check_quest_active, "qst_wed_betrothed_female"),
     (str_store_troop_name, s5, ":betrothed"),
     (display_message, "@Betrothal to {s5} expires"),
     (troop_set_slot, "trp_player", slot_troop_betrothed, -1),
     (troop_set_slot, ":betrothed", slot_troop_betrothed, -1),
 (try_end),
]),
####################
    
#################### other half
# (3,
(6,
[
#Also, piggy-backing on this -- having bandits go to lairs and back
(try_for_parties, ":bandit_party"),
  (gt, ":bandit_party", "p_spawn_points_end"),
  (party_get_template_id, ":bandit_party_template", ":bandit_party"),
  (is_between, ":bandit_party_template", "pt_steppe_bandits", "pt_deserters"),
  (party_template_get_slot, ":bandit_lair", ":bandit_party_template", slot_party_template_lair_party),
  
  (try_begin),#If party is active and bandit is far away, then move to location
    (gt, ":bandit_lair", "p_spawn_points_end"),
    (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"), ######this is the cause of the error
    (gt, ":distance", 30),
    (lt, ":distance", bandit_lair_distance_max), ######### rafi - no far away bandits
    ######All this needs checking
    (party_set_ai_behavior, ":bandit_party", ai_bhvr_travel_to_point),
    (party_get_position, pos5, ":bandit_lair"),
    (party_set_ai_target_position, ":bandit_party", pos5),

  (else_try), ######Otherwise, act freely
    (get_party_ai_behavior, ":behavior", ":bandit_party"),
    (eq, ":behavior", ai_bhvr_travel_to_point),

    (try_begin),
      (gt, ":bandit_lair", "p_spawn_points_end"),
      (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"),
      (lt, ":distance", 3),
      (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
      (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
      (party_set_ai_object, ":bandit_party", ":spawnpoint"),
      (party_set_ai_patrol_radius, ":bandit_party", 45),

    (else_try),
      (lt, ":bandit_lair", "p_spawn_points_end"),
      (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
      (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
      (party_set_ai_object, ":bandit_party", ":spawnpoint"),
      (party_set_ai_patrol_radius, ":bandit_party", 45),
    (try_end),
  (try_end),
(try_end),
]),
################################################################################
    
    
    
#### Reduce renown slightly by 0.5% every week
(168,
[
 (eq, "$g_misc_disable_renown_weekly_reduction", 0), ######### NEW v2.1
  (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
  (store_div, ":renown_decrease", ":player_renown", 200),  ######## 0.5%
  (val_sub, ":player_renown", ":renown_decrease"),
  (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
]),


  ######### Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
       (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
       (eq, ":book_read", 0),
       (val_add, ":book_reading_progress", 7),
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 1),
         (str_store_string, s2, "@ Your tactics skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 1),
         (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 1),
         (str_store_string, s2, "@ Your leadership skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (str_store_string, s2, "@ Your intelligence has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_trade"),
         (troop_raise_skill, "trp_player", "skl_trade", 1),
         (str_store_string, s2, "@ Your trade skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
         (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 1),
         (str_store_string, s2, "@ Your engineer skill has increased by 1."),
       (try_end),

       (unlock_achievement, ACHIEVEMENT_BOOK_WORM),

       (try_begin),
         (eq, "$g_infinite_camping", 0),
       (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (try_end),

       (assign, "$g_player_reading_book", 0),
       ]),

#### Removing cattle herds if they are way out of range
  (12, [(try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist", ":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              ######Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),


#####!!!!!



################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### Village upgrade triggers
#### School
#### (168,
(0.397,  ################### once a week for each of the 423 villages
 [
 (try_begin),
   (lt, "$g_player_school_bonus_cur_village", villages_begin), 
     (assign, "$g_player_school_bonus_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_player_school_bonus_cur_village", villages_end), 
     (assign, "$g_player_school_bonus_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (party_slot_eq, "$g_player_school_bonus_cur_village", slot_town_lord, "trp_player"),
   (party_slot_eq, "$g_player_school_bonus_cur_village", slot_center_has_school, 1),
     (party_get_slot, ":cur_relation", "$g_player_school_bonus_cur_village", slot_center_player_relation),
     (val_add, ":cur_relation", 1),
     (val_min, ":cur_relation", 100),
     (party_set_slot, "$g_player_school_bonus_cur_village", slot_center_player_relation, ":cur_relation"),
 (try_end),
 
 ################ proceeds to the next village when it's triggered again
 (val_add, "$g_player_school_bonus_cur_village", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_35", 1),
 
]),
##########################################################################################

    

#### Quest triggers:

#### Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),

#### Report to army quest
  (2,
   [
     (eq, "$g_infinite_camping", 0),
     (eq, "$g_player_crusading", 0),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
     (eq, "$g_player_is_captive", 0),

     (try_begin),
        (check_quest_active, "qst_report_to_army"),
        (faction_slot_eq, "$players_kingdom", slot_faction_marshall, -1),
        (call_script, "script_abort_quest", "qst_report_to_army", 0),
     (try_end),

     (faction_get_slot, ":faction_object", "$players_kingdom", slot_faction_ai_object),

     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),

     (assign, ":continue", 1),
     (try_begin),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_enemies_around_center),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
       (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_raiding_village),
       (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
       (assign, ":continue", 0),
     (try_end),
     (eq, ":continue", 1),

     (assign, ":kingdom_is_at_war", 0),
     (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
        (neq, ":faction", "$players_kingdom"),
        (store_relation, ":relation", ":faction", "$players_kingdom"),
        (lt, ":relation", 0),
        (assign, ":kingdom_is_at_war", 1),
     (try_end),
     (eq, ":kingdom_is_at_war", 1),

     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),

     (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),

     (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshall_party", "p_main_party"),
     (le, ":distance_to_marshal", 96),

     (assign, ":has_no_quests", 1),
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", slot_party_type, spt_town),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),

     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
     ######(quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 22),
     (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 15), ######### reduce to 2 weeks
     (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
     ]),


#### Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#Rebellion changes begin
####     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_last_offensive_concluded),
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", slot_troop_does_not_give_quest, 0),
         (try_for_range, ":unused", 0, 20), ######Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
            ######### (eq, 1, 0), ######disables temporarily
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result", "qst_deliver_cattle_to_army"),

               (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 10),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
             (eq, 1, 0),
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_kingdom", slot_faction_ai_object),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               ######army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 2),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", "qst_scout_waypoints"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 7),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
             (try_end),
           (try_end),
         (try_end),

         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", slot_quest_current_state, 0),
           (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshall"),
             (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 15),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
####             (display_message, "str_marshal_warning"),

           (else_try),
             (display_message, "str_marshal_warning"),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_kingdom_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

#### Move cattle herd
  (0.5, [(check_quest_active, "qst_move_cattle_herd"),
         (neg|check_quest_concluded, "qst_move_cattle_herd"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
         (store_distance_to_party_from_party, ":dist", ":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),

    
  ######### (2, 
  (3, 
  [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ####### he's alive/active
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
         (party_is_active, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_following_player, 1),
         (store_current_hours, ":cur_time"),
         (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
         (party_set_slot, ":party_no", slot_party_commander_party, -1),
         (party_set_slot, ":party_no", slot_party_following_player, 0),
         (assign,  ":dont_follow_period", 200),
         (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
       (try_end),
    ]),

#### Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active, "qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
       (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

#### Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 20, ":trainer_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), ######stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

#### Scout waypoints
  (1,
   [
     (check_quest_active, "qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),

#### Kill local merchant

  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
       (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
       (rest_for_hours, 0, 0, 0), ######stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

#### Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),

       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
         (rest_for_hours, 0, 0, 0), ######stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         ######Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values

         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), ######Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),

         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),

#persuade_lords_to_make_peace begin
  (72, [(gt, "$g_force_peace_faction_1", 0),
        (gt, "$g_force_peace_faction_2", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
       ]),

#NPC changes begin
#Resolve one issue each hour
(1,
   [
        (str_store_string, s51, "str_no_trigger_noted"),

        ######### Rejoining party
        (try_begin),
            (gt, "$npc_to_rejoin_party", 0),
            (eq, "$g_infinite_camping", 0),
            (try_begin),
                (neg|main_party_has_troop, "$npc_to_rejoin_party"),
                (neq, "$g_player_is_captive", 1),

                (str_store_string, s51, "str_triggered_by_npc_to_rejoin_party"),

                (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
                (start_map_conversation, "$npc_to_rejoin_party", -1),
            (else_try),
                (troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                (assign, "$npc_to_rejoin_party", 0),
            (try_end),
        ######### Here do NPC that is quitting
        (else_try),
            (gt, "$npc_is_quitting", 0),
            (eq, "$g_infinite_camping", 0),
            (try_begin),
                (main_party_has_troop, "$npc_is_quitting"),
                (neq, "$g_player_is_captive", 1),
                #######diplomacy start+ disable spouse quitting to avoid problems
                (neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$npc_is_quitting"),
                (neg|troop_slot_eq, "$npc_is_quitting", slot_troop_spouse, "trp_player"),
                #######diplomacy end+
                (str_store_string, s51, "str_triggered_by_npc_is_quitting"),
                (start_map_conversation, "$npc_is_quitting", -1),
            (else_try),
                (assign, "$npc_is_quitting", 0),
            (try_end),
        ######NPC with grievance
        (else_try), ############ Grievance
            (gt, "$npc_with_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_grievance"),
                (neq, "$g_player_is_captive", 1),

                (str_store_string, s51, "str_triggered_by_npc_has_grievance"),

                (assign, "$npc_map_talk_context", slot_troop_morality_state),
                (start_map_conversation, "$npc_with_grievance", -1),
            (else_try),
                (assign, "$npc_with_grievance", 0),
            (try_end),
        (else_try),
            (gt, "$npc_with_personality_clash", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
            (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash"),
                (main_party_has_troop, ":object"),
                (neq, "$g_player_is_captive", 1),

                (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
                (str_store_string, s51, "str_triggered_by_npc_has_personality_clash"),
                (start_map_conversation, "$npc_with_personality_clash", -1),
            (else_try),
                (assign, "$npc_with_personality_clash", 0),
            (try_end),
        (else_try), ############ Political issue
            (gt, "$npc_with_political_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_political_grievance"),
                (neq, "$g_player_is_captive", 1),

                (str_store_string, s51, "str_triggered_by_npc_has_political_grievance"),
                (assign, "$npc_map_talk_context", slot_troop_kingsupport_objection_state),
                (start_map_conversation, "$npc_with_political_grievance", -1),
            (else_try),
                (assign, "$npc_with_political_grievance", 0),
            (try_end),
        (else_try),
            (eq, "$disable_sisterly_advice", 0),
            (eq, "$g_infinite_camping", 0),
            (gt, "$npc_with_sisterly_advice", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_sisterly_advice"),
                (neq, "$g_player_is_captive", 1),

                #######diplomacy start+
                (troop_slot_ge, "$npc_with_sisterly_advice", slot_troop_woman_to_woman_string, 1),
                #######diplomacy end+
                (assign, "$npc_map_talk_context", slot_troop_woman_to_woman_string), ######was npc_with_sisterly advice
                (start_map_conversation, "$npc_with_sisterly_advice", -1),
            (else_try),
                (assign, "$npc_with_sisterly_advice", 0),
            (try_end),
        (else_try), ######check for regional background
            (eq, "$disable_local_histories", 0),
            (eq, "$g_infinite_camping", 0),
            (try_for_range, ":npc", companions_begin, companions_end),
                (main_party_has_troop, ":npc"),
                (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
                (troop_get_slot, ":home", ":npc", slot_troop_home),
                (gt, ":home", 0),
                (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
                (lt, ":distance", 7),
                (assign, "$npc_map_talk_context", slot_troop_home),

                (str_store_string, s51, "str_triggered_by_local_histories"),

                (start_map_conversation, ":npc", -1),
            (try_end),
        (try_end),

        ######add pretender to party if not active
        (try_begin),
            (check_quest_active, "qst_rebel_against_kingdom"),
            (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
            (neg|main_party_has_troop, "$supported_pretender"),
            (neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
            (party_add_members, "p_main_party", "$supported_pretender", 1),
        (try_end),

        ######make player marshal of rebel faction
        (try_begin),
            (check_quest_active, "qst_rebel_against_kingdom"),
            (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
            (main_party_has_troop, "$supported_pretender"),
            (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
            (call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
        (try_end),
]),
#NPC changes end

(1,
   [
   (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
      (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ####### he's alive/active
      (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
      (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
      (assign, ":continue", 0),
      (try_begin),
        (le, ":party_no", 0),
        ######(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        ######checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", slot_town_lord, ":troop_no"),

        ######checking if the party is away from his original faction parties
        (assign, ":end_cond", active_npcs_end),
        (try_for_range, ":enemy_troop_no", active_npcs_begin, ":end_cond"),
          (troop_slot_eq, ":enemy_troop_no", slot_troop_is_alive, 1),  ####### he's alive/active
          ########## bugfix - must not include himself
          (neq, ":enemy_troop_no", ":troop_no"),
          ########## bugfix
          (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
          (party_is_active, ":enemy_party_no"),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
      
        (try_begin),
            (ge, "$cheat_mode", 1),
            (str_store_troop_name, s4, ":troop_no"),
            (display_message, "@{!}DEBUG - {s4} faction changed from slot_troop_change_to_faction"), 
        (try_end),      
        
      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
      (try_begin),
        (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (display_message, "@{s1} has switched from {s2} to {s3}."),
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),


#### (1,
   ######### [
     ######### (eq, "$cheat_mode", 1),
     ######### (try_for_range, ":center_no", centers_begin, centers_end),
       ######### (party_get_battle_opponent, ":besieger_party", ":center_no"),
       ######### (try_begin),
         ######### (gt, ":besieger_party", 0),
         ######### (str_store_party_name, s2, ":center_no"),
         ######### (str_store_party_name, s3, ":besieger_party"),
         ######### (display_message, "@{!}DEBUG : {s2} is besieging by {s3}"),
       ######### (try_end),
     ######### (try_end),
     ######### ]),

(1,
   [
     (store_current_day, ":cur_day"),
     (gt, ":cur_day", "$g_last_report_control_day"),
     (store_time_of_day, ":cur_hour"),
     (ge, ":cur_hour", 18),

     (store_random_in_range, ":rand_no", 0, 4),
     (this_or_next|ge, ":cur_hour", 22),
     (eq, ":rand_no", 0),

     (assign, "$g_last_report_control_day", ":cur_day"),

     (store_troop_gold, ":gold", "trp_player"),

     (try_begin),
       (lt, ":gold", 0),
       (store_sub, ":gold_difference", 0, ":gold"),
       (troop_add_gold, "trp_player", ":gold_difference"),
     (try_end),

     (party_get_morale, ":main_party_morale", "p_main_party"),

     ######(assign, ":swadian_soldiers_are_upset_message_showed", 0),
     ######(assign, ":vaegir_soldiers_are_upset_message_showed", 0),
     ######(assign, ":khergit_soldiers_are_upset_message_showed", 0),
     ######(assign, ":nord_soldiers_are_upset_message_showed", 0),
     ######(assign, ":rhodok_soldiers_are_upset_message_showed", 0),

     (try_begin),
       (str_store_string, s1, "str_party_morale_is_low"),
       (str_clear, s2),

       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (assign, ":num_deserters_total", 0),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),

         (store_troop_faction, ":faction_no", ":stack_troop"),

         (assign, ":troop_morale", ":main_party_morale"),
         (try_begin),
           (ge, ":faction_no", npc_kingdoms_begin),
           (lt, ":faction_no", npc_kingdoms_end),

           (faction_get_slot, ":troop_morale_addition", ":faction_no",  slot_faction_morale_of_player_troops),
           (val_div, ":troop_morale_addition", 100),
           (val_add, ":troop_morale", ":troop_morale_addition"),
         (try_end),

         (lt, ":troop_morale", 32),
         (store_sub, ":desert_prob", 36, ":troop_morale"),
         (val_div, ":desert_prob", 4),

         (assign, ":num_deserters_from_that_troop", 0),
         (try_for_range, ":unused", 0, ":stack_size"),
           (store_random_in_range, ":rand_no", 0, 100),
           (lt, ":rand_no", ":desert_prob"),
           (val_add, ":num_deserters_from_that_troop", 1),
           ######p.remove_members_from_stack(i_stack,cur_deserters, &main_party_instances);
           (remove_member_from_party, ":stack_troop", "p_main_party"),
         (try_end),
         (try_begin),
           (ge, ":num_deserters_from_that_troop", 1),
           (str_store_troop_name, s2, ":stack_troop"),
           (assign, reg0, ":num_deserters_from_that_troop"),

####           (try_begin),
####             (lt, ":troop_morale_addition", -2),
####             (ge, ":main_party_morale", 28),
####             (try_begin),
####               (eq, ":faction_no", "fac_kingdom_1"),
####               (eq, ":swadian_soldiers_are_upset_message_showed", 0),
####               (str_store_string, s3, "str_swadian_soldiers_are_upset"),
####               (assign, ":swadian_soldiers_are_upset_message_showed", 1),
####             (else_try),
####               (eq, ":faction_no", "fac_kingdom_2"),
####               (eq, ":vaegir_soldiers_are_upset_message_showed", 0),
####               (str_store_string, s3, "str_vaegir_soldiers_are_upset"),
####               (assign, ":vaegir_soldiers_are_upset_message_showed", 1),
####             (else_try),
####               (eq, ":faction_no", "fac_kingdom_3"),
####               (eq, ":khergit_soldiers_are_upset_message_showed", 0),
####               (str_store_string, s3, "str_khergit_soldiers_are_upset"),
####               (assign, ":khergit_soldiers_are_upset_message_showed", 1),
####             (else_try),
####               (eq, ":faction_no", "fac_kingdom_4"),
####               (eq, ":nord_soldiers_are_upset_message_showed", 0),
####               (str_store_string, s3, "str_nord_soldiers_are_upset"),
####               (assign, ":nord_soldiers_are_upset_message_showed", 1),
####             (else_try),
####               (eq, ":faction_no", "fac_kingdom_5"),
####               (eq, ":rhodok_soldiers_are_upset_message_showed", 0),
####               (str_store_string, s3, "str_rhodok_soldiers_are_upset"),
####               (assign, ":rhodok_soldiers_are_upset_message_showed", 1),
####             (try_end),
####             (str_store_string, s1, "@{!}{s1} {s3}"),
####           (try_end),

           (try_begin),
             (ge, ":num_deserters_total", 1),
             (str_store_string, s1, "str_s1_reg0_s2"),
           (else_try),
             (str_store_string, s3, s1),
             (str_store_string, s1, "str_s3_reg0_s2"),
           (try_end),
           (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, ":num_deserters_total", 1),

         (try_begin),
           (ge, ":num_deserters_total", 2),
           (str_store_string, s2, "str_have_deserted_the_party"),
         (else_try),
           (str_store_string, s2, "str_has_deserted_the_party"),
         (try_end),

         (str_store_string, s1, "str_s1_s2"),

         (eq, "$g_infinite_camping", 0),

         (tutorial_box, s1, "str_weekly_report"),
       (try_end),
     (try_end),
 ]),
 ######### reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.

  ######### (1,
   ######### [
     #######PROSPERITY SYSTEM
     ######(call_script, "script_calculate_castle_prosperities_by_using_its_villages"),
     #######PROSPERITY SYSTEM

     ######### (store_add, ":fac_kingdom_6_plus_one", "fac_kingdom_31", 1),

     ######### (try_for_range, ":faction_1", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
       ######### (try_for_range, ":faction_2", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
         ######### (store_relation, ":faction_relation", ":faction_1", ":faction_2"),
         ######### (str_store_faction_name, s7, ":faction_1"),
         ######### (str_store_faction_name, s8, ":faction_2"),
         ######### (neq, ":faction_1", ":faction_2"),
         ######### (assign, reg1, ":faction_relation"),
         ######(display_message, "@{s7}-{s8}, relation is {reg1}"),
       ######### (try_end),
     ######### (try_end),
     ######### 
     ######### ]),

  (1,
   [
     (try_begin),
       (eq, "$g_player_is_captive", 1),
       (neg|party_is_active, "$capturer_party"),
       (rest_for_hours, 0, 0, 0),
     (try_end),

     (assign, ":village_no", "$next_center_will_be_fired"),
       (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
       (eq, ":is_there_already_fire", 0),
     
     
       (try_begin),
         (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
         (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
         (store_current_hours, ":cur_hours"),
       
       (try_begin),
        (eq, "$cheat_mode", 1),
        (is_between, ":village_no", centers_begin, centers_end),
        (is_between, ":bound_center", centers_begin, centers_end),
        (str_store_party_name, s4, ":village_no"),
        (str_store_party_name, s5, ":bound_center"),
        (store_current_hours, reg3),
        (party_get_slot, reg4, ":bound_center", slot_town_last_nearby_fire_time),
        (display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
       (try_end),


         (eq, ":cur_hours", ":last_nearby_fire_time"),
         (party_add_particle_system, ":village_no", "psys_map_village_fire"),
         (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
       (else_try),
         (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
         (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
         (party_clear_particle_systems, ":village_no"),
       (try_end),
     

   ]),

  (24,
   [
   (val_sub, "$g_dont_give_fief_to_player_days", 1),
   (val_max, "$g_dont_give_fief_to_player_days", -1),
   (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
   (val_max, "$g_dont_give_marshalship_to_player_days", -1),

   ######this to correct string errors in games started in 1.104 or before
   (party_set_name, "p_steppe_bandit_spawn_point_1", "str_the_steppes"),
   (party_set_name, "p_steppe_bandit_spawn_point_2", "str_the_steppes"),
   
   (party_set_name, "p_taiga_bandit_spawn_point_1", "str_the_tundra"),
   (party_set_name, "p_taiga_bandit_spawn_point_2", "str_the_tundra"),
   
   (party_set_name, "p_forest_bandit_spawn_point_1", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_2", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_3", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_4", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_5", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_6", "str_the_forests"),
   (party_set_name, "p_forest_bandit_spawn_point_7", "str_the_forests"),

   (party_set_name, "p_mountain_bandit_spawn_point_1", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_2", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_3", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_4", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_5", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_6", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_7", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_8", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_9", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_10", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_11", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_12", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_13", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_14", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_15", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_16", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_17", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_18", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_19", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_20", "str_the_highlands"),
   (party_set_name, "p_mountain_bandit_spawn_point_21", "str_the_highlands"),

   (party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_3", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_4", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_5", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_6", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_7", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_8", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_9", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_10", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_11", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_12", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_13", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_14", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_15", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_16", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_17", "str_the_coast"),

   (party_set_name, "p_desert_bandit_spawn_point_1", "str_the_deserts"),
   (party_set_name, "p_desert_bandit_spawn_point_2", "str_the_deserts"),
   (party_set_name, "p_desert_bandit_spawn_point_3", "str_the_deserts"),
   (party_set_name, "p_desert_bandit_spawn_point_4", "str_the_deserts"),
   (party_set_name, "p_desert_bandit_spawn_point_5", "str_the_deserts"),

   ######The following scripts are to end quests which should have cancelled, but did not because of a bug
   (try_begin),
   (check_quest_active, "qst_formal_marriage_proposal"),
    (check_quest_failed, "qst_formal_marriage_proposal"),
    (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
   (try_end),

   (try_begin),
    (check_quest_active, "qst_lend_companion"),
    (quest_get_slot, ":giver_troop", "qst_lend_companion", slot_quest_giver_troop),
    (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
    (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"),
    (this_or_next|lt, ":faction_relation", 0),
    (neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end),
    (call_script, "script_abort_quest", "qst_lend_companion", 0),
   (try_end),


   
   (try_begin),
    (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
    (neq, "$players_kingdom", "fac_player_supporters_faction"),
    (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
    (val_add, "$g_player_days_as_marshal", 1),
   (else_try),
    (assign, "$g_player_days_as_marshal", 0),
   (try_end),

   (try_for_range, ":town", towns_begin, towns_end),
    (party_get_slot, ":days_to_completion", ":town", slot_center_player_enterprise_days_until_complete),
    (ge, ":days_to_completion", 1),
    (val_sub, ":days_to_completion", 1),
    (party_set_slot, ":town", slot_center_player_enterprise_days_until_complete, ":days_to_completion"),
   (try_end),
    ]),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),
  ######### (24,
   ######### []),

  ######### low food display
  (12, [
    (eq, "$g_player_is_captive", 0),
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    (val_div, ":num_men", 3),

    (try_begin),
      (eq, ":num_men", 0),
      (val_add, ":num_men", 1),
    (try_end),

    (assign, ":consumption_amount", ":num_men"),

    (assign, ":food_total", 0),

        (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        (try_for_range, ":i_slot", 0, ":inv_cap"),
            (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
      (try_begin),
        (ge, ":item", 0),
        (try_begin),
          (is_between, ":item", food_begin, food_end),
          ######(str_store_item_name, s1, ":item"),
          ######(display_message, "@counting: {s1}", 0xff0000),
          (troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":i_slot"),
          (troop_get_inventory_slot_modifier, ":cur_modifier", "trp_player", ":i_slot"),
          (neq, ":cur_modifier", imod_rotten),
          (val_add, ":food_total", ":cur_amount"),
        (try_end),
      (try_end),
    (try_end),

    (store_mul, ":hrs_food_left", ":food_total", 12),
    (val_div, ":hrs_food_left", ":consumption_amount"),

    (try_begin),
      (le, ":hrs_food_left", 48),
      (gt, ":hrs_food_left", 0),
        (display_message, "@Your party is low on food, less than 48 hours of food remaining", 0xff0000),
    (try_end),
  ]),


  #######diplomacy begin
  ######Troop AI Spouse: Spouse thinking
  ######### (3,
  (8,
   [
    (try_for_parties, ":spouse_party"),
      (party_slot_eq, ":spouse_party", slot_party_type, dplmc_spt_spouse),

      (party_get_slot, ":spouse_target", ":spouse_party", slot_party_orders_object),
      (party_get_slot, ":home_center", ":spouse_party", slot_party_home_center),
      (store_distance_to_party_from_party, ":distance", ":spouse_party", ":spouse_target"),

      ######Moving spouse to home village
      (try_begin),
        (le, ":distance", 1),
        (try_begin),
          (neg|eq, ":spouse_target", ":home_center"),

          (try_begin),
            (is_between, ":spouse_target", villages_begin, villages_end),
            (party_get_slot, ":cur_merchant", ":spouse_target", slot_town_elder),
          (else_try),
            (party_get_slot, ":cur_merchant", ":spouse_target", slot_town_merchant),
          (try_end),
          (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (troop_get_slot, ":amount", ":player_spouse", dplmc_slot_troop_mission_diplomacy),
          (troop_remove_items, ":cur_merchant", "itm_bread", ":amount"),

          (party_set_slot, ":spouse_party", slot_party_ai_object, ":home_center"),
          (party_set_ai_behavior, ":spouse_party", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":spouse_party", ":home_center"),
          (troop_add_items, "trp_household_possessions", "itm_bread", ":amount"),
        (else_try),
          (remove_party, ":spouse_party"),
          (troop_set_slot, ":player_spouse", slot_troop_cur_center, "$g_player_court"),
        (try_end),
      (try_end),
    (try_end),
    ]),

    
#Recruiter kit begin
##### This trigger keeps the recruiters moving by assigning them targets.
 ###### (24*30, ######0.5, tom make them slow 4 now. VERY Slow -recruiters not working anyway
 (3, 
   [
   (gt, "$g_recruiter_count", 0),  ################ NEW v2.0
   (try_for_parties, ":party_no"),
      (party_slot_eq, ":party_no", slot_party_type, dplmc_spt_recruiter),

      (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),

      (party_get_num_companion_stacks, ":stacks", ":party_no"),
      (assign, ":destruction", 1),
      (assign, ":quit", 0),

      (try_for_range, ":stack_no", 0, ":stacks"),
         (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
         (eq, ":troop_id", "trp_dplmc_recruiter"),
         (assign, ":destruction",0),
      (try_end),
      (try_begin),
         (party_get_battle_opponent, ":opponent", ":party_no"),
         (lt, ":opponent", 0),
         (eq, ":destruction", 1),
         (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":needed"),
         (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated!", 0xFF0000),
         (remove_party, ":party_no"),
         (assign, ":quit", 1),
         (val_sub, "$g_recruiter_count", 1),  ################ NEW v2.0
      (try_end),

      ######waihti
      (try_begin),
        (eq, ":quit", 0),
        (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
        (store_faction_of_party, ":origin_faction", ":party_origin"),
        (neq, ":origin_faction", "$players_kingdom"),
        (str_store_party_name_link, s13, ":party_origin"),
        (assign, reg10, ":needed"),
        (display_log_message, "@{s13} has been taken by the enemy and your recruiter who was commissioned to recruit {reg10} recruits vanished  without a trace!", 0xFF0000),
        (remove_party, ":party_no"),
        (assign, ":quit", 1),
        (val_sub, "$g_recruiter_count", 1),  ################ NEW v2.0
      (try_end),
      ######waihti

      (eq, ":quit", 0),

      (party_get_num_companions, ":amount", ":party_no"),
      (val_sub, ":amount", 1),   ######the recruiter himself doesn't count.

   ######daedalus begin
      (party_get_slot, ":recruit_faction", ":party_no", dplmc_slot_party_recruiter_needed_recruits_faction),
   ######daedalus end
      (lt, ":amount", ":needed"),  ######If the recruiter has less troops than player ordered, new village will be set as target.
      (try_begin),
         ######(get_party_ai_current_behavior, ":ai_bhvr", ":party_no"),
         ######(eq, ":ai_bhvr", ai_bhvr_hold),
         (get_party_ai_object, ":previous_target", ":party_no"),
         (get_party_ai_behavior, ":previous_behavior", ":party_no"),
         (try_begin),
            (neq, ":previous_behavior", ai_bhvr_hold),
            (neq, ":previous_target", -1),
            (party_set_slot, ":previous_target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
         (assign, ":min_distance", 999999),
         (assign, ":closest_village", -1),
         (try_for_range, ":village", villages_begin, villages_end),
            (store_distance_to_party_from_party, ":distance", ":party_no", ":village"),
            (lt, ":distance", ":min_distance"),
            (try_begin),
               (store_faction_of_party, ":village_current_faction", ":village"),
               (assign, ":faction_relation", 100),
               (try_begin),
                  (neq, ":village_current_faction", "$players_kingdom"),    ######### faction relation will be checked only if the village doesn't belong to the player's current faction
                  (store_relation, ":faction_relation", "$players_kingdom", ":village_current_faction"),
               (try_end),
               (ge, ":faction_relation", 0),
               (party_get_slot, ":village_relation", ":village", slot_center_player_relation),
               (ge, ":village_relation", 0),
               (party_get_slot, ":volunteers_in_village", ":village", slot_center_volunteer_troop_amount),
               (gt, ":volunteers_in_village", 0),
            ######daedalus begin
               (party_get_slot, ":village_faction", ":village", slot_center_original_faction),
               (assign, ":stop",1),
               (try_begin),
                  (eq, ":recruit_faction",-1),
                  (assign, ":stop",0),
               (else_try),
                  (eq, ":village_faction", ":recruit_faction"),
                  (assign, ":stop",0),
               (try_end),
               (neq, ":stop",1),
            ######daedalus end
               (neg|party_slot_eq, ":village", slot_village_state, svs_looted),
               (neg|party_slot_eq, ":village", slot_village_state, svs_being_raided),
               (neg|party_slot_ge, ":village", slot_village_infested_by_bandits, 1),
               (neg|party_slot_eq, ":village", dplmc_slot_village_reserved_by_recruiter, 1),
               (assign, ":min_distance", ":distance"),
               (assign, ":closest_village", ":village"),
            (try_end),
         (try_end),
         (gt, ":closest_village", -1),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":closest_village"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":closest_village"),
         (party_set_slot, ":closest_village", dplmc_slot_village_reserved_by_recruiter, 1),
      (try_end),
      (party_get_slot, ":target", ":party_no", slot_party_ai_object),
      (gt, ":target", -1),
      (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":target"),
      (try_begin),
         (store_faction_of_party, ":target_current_faction", ":target"),
         (assign, ":faction_relation", 100),
         (try_begin),
            (neq, ":target_current_faction", "$players_kingdom"),    ######### faction relation will be checked only if the target doesn't belong to the player's current faction
            (store_relation, ":faction_relation", "$players_kingdom", ":target_current_faction"),
         (try_end),
         (ge, ":faction_relation", 0),
         (party_get_slot, ":target_relation", ":target", slot_center_player_relation),
         (ge, ":target_relation", 0),
      ######daedalus begin
            ######### (party_get_slot, ":target_faction", ":target", slot_center_original_faction),
            ######### rafi
            (call_script, "script_raf_aor_faction_to_region", ":village_faction"),
            (assign, ":target_region", reg0),
            ######### end rafi
            (assign, ":stop",1),
            (try_begin),
            (eq, ":recruit_faction",-1),
            (assign, ":stop",0),
        (else_try),
            (eq, ":target_region", ":recruit_faction"),
            (assign, ":stop",0),
            (try_end),
            (neq, ":stop",1),
      ######daedalus end
         (neg|party_slot_eq, ":target", slot_village_state, svs_looted),
            (neg|party_slot_eq, ":target", slot_village_state, svs_being_raided),
            (neg|party_slot_ge, ":target", slot_village_infested_by_bandits, 1),
         (le, ":distance_from_target", 0),
         (party_get_slot, ":volunteers_in_target", ":target", slot_center_volunteer_troop_amount),
         (party_get_slot, ":target_volunteer_type", ":target", slot_center_volunteer_troop_type),
         (assign, ":still_needed", ":needed"),
         (val_sub, ":still_needed", ":amount"),
         (try_begin),
            (gt, ":volunteers_in_target", ":still_needed"),
            (assign, ":santas_little_helper", ":volunteers_in_target"),
            (val_sub, ":santas_little_helper", ":still_needed"),
            (assign, ":amount_to_recruit", ":volunteers_in_target"),
            (val_sub, ":amount_to_recruit", ":santas_little_helper"),
            (assign, ":new_target_volunteer_amount", ":volunteers_in_target"),
            (val_sub, ":new_target_volunteer_amount", ":amount_to_recruit"),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, ":new_target_volunteer_amount"),
            (party_add_members, ":party_no", ":target_volunteer_type", ":amount_to_recruit"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (le, ":volunteers_in_target", ":still_needed"),
            (gt, ":volunteers_in_target", 0),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, -1),
            (party_add_members, ":party_no", ":target_volunteer_type", ":volunteers_in_target"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (le, ":volunteers_in_target", 0),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!",0xFF2222),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
      (try_end),
   (try_end),

   (try_for_parties, ":party_no"),
      (party_slot_eq, ":party_no", slot_party_type, dplmc_spt_recruiter),
      (party_get_num_companions, ":amount", ":party_no"),
      (val_sub, ":amount", 1),   ######the recruiter himself doesn't count
      (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),
      (eq, ":amount", ":needed"),
      (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
      (try_begin),
         (neg|party_slot_eq, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":party_origin"),
      (try_end),
      (store_distance_to_party_from_party, ":distance_from_origin", ":party_no", ":party_origin"),
      (try_begin),
         (le, ":distance_from_origin", 0),
         (party_get_num_companion_stacks, ":stacks", ":party_no"),
         (try_for_range, ":stack_no", 1, ":stacks"),
            (party_stack_get_size, ":size", ":party_no", ":stack_no"),
            (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
            (party_add_members, ":party_origin", ":troop_id", ":size"),
         (try_end),
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":amount"),
         (display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", 0x00FF00),
         (remove_party, ":party_no"),
         (val_sub, "$g_recruiter_count", 1),  ################ NEW v2.0
      (try_end),
   (try_end),
   ]),
   
   
   
   
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#This trigger makes sure that no village is left reserved forever.
#### (12,
(0.056, ###################### once a day for each of the 423 villages
[
 (try_begin),
   (lt, "$g_recruiter_reserved_cur_village", villages_begin), 
     (assign, "$g_recruiter_reserved_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_recruiter_reserved_cur_village", villages_end), 
     (assign, "$g_recruiter_reserved_cur_village", villages_begin),
 (try_end),
   
 (try_begin),
   (party_set_slot, "$g_recruiter_reserved_cur_village", dplmc_slot_village_reserved_by_recruiter, 0),
 (try_end),
 
 ################ proceeds to the next faction when it's triggered again
 (val_add, "$g_recruiter_reserved_cur_village", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_36", 1),
]),
#Recruiter kit end
############################################################





#process gift_carvans
 ######### (2, ######tom was 0.5
 (2, ######tom was 0.5
 [
  (eq, "$g_player_chancellor", "trp_dplmc_chancellor"),
  #################### NEW v1.8 - checks a global to see if there's any gift caravan spawned, if there's none don't execute the try_for_parties
  (gt, "$g_gift_caravan_count", 0),
        
  (try_for_parties, ":party_no"),
    (party_slot_eq, ":party_no", slot_party_type, dplmc_spt_gift_caravan),
    (party_is_active, ":party_no"),
    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":target_troop", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),

      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15, ":target_party"),

      (try_begin), ######debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (party_get_slot, ":gift", ":party_no", dplmc_slot_party_mission_diplomacy),
        (str_store_item_name, s12, ":gift"),

        (try_begin),
          (gt, ":target_troop", 0),
          (str_store_troop_name, s13, ":target_troop"),
        (else_try),
          (str_store_party_name, s13, ":target_party"),
        (end_try),
        (display_log_message, "@Your caravan has brought {s12} to {s13}.", 0x00FF00),

        (assign, ":relation_boost", 0),
        (store_faction_of_party, ":target_faction", ":target_party"),

        (try_begin),
          (gt, ":target_troop", 0),
          (faction_slot_eq, ":target_faction",slot_faction_leader, ":target_troop"),
          (try_begin),
            (eq, ":gift", "itm_wine"),
            (assign, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (assign, ":relation_boost", 2),
          (try_end),
        (else_try),
          (store_random_in_range, ":random", 1, 3),
          (try_begin),
            (eq, ":gift", "itm_ale"),
            (val_add, ":relation_boost", ":random"),
          (else_try),
            (eq, ":gift", "itm_wine"),
            (store_add, ":relation_boost", 1, ":random"),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (store_add, ":relation_boost", 2, ":random"),
          (else_try),
            (eq, ":gift", "itm_raw_dyes"),
            (val_add, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_raw_silk"),
            (val_add, ":relation_boost", 2),
          (else_try),
            (eq, ":gift", "itm_velvet"),
            (val_add, ":relation_boost", 4),
          (else_try),
            (eq, ":gift", "itm_smoked_fish"),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_cheese"),
            (val_add, ":relation_boost", 1),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_honey"),
            (val_add, ":relation_boost", 2),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 2),
            (try_end),
          (try_end),
        (try_end),

        (try_begin),
          (this_or_next|eq, ":target_faction", "fac_player_supporters_faction"),
          (eq, ":target_faction", "$players_kingdom"),
          (val_add, ":relation_boost", 1),
        (try_end),

        (try_begin),
          (gt, ":target_troop", 0),
          (call_script, "script_change_player_relation_with_troop", ":target_troop", ":relation_boost"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", ":target_party", ":relation_boost"),
        (try_end),
        (remove_party, ":party_no"),
        ##################### NEW v1.8 - removes 1
        (val_sub, "$g_gift_caravan_count", 1),
      (try_end),
    (else_try),
      (display_log_message, "@Your caravan has lost its way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
      ##################### NEW v1.8 - removes 1
      (val_sub, "$g_gift_caravan_count", 1),
    (try_end),
  (try_end),
 ]),

 
 
 ######process messengers
 (2, ######0.5, ######tom was 2.
 [
  #################### NEW v1.8 - checks a global to see if there's any messenger spawned, if there's none don't execute the try_for_parties
  (gt, "$g_player_messenger_count", 0),
  (try_for_parties, ":party_no"),
    (party_slot_eq, ":party_no", slot_party_type, dplmc_spt_messenger),

    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":orders_object", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15, ":target_party"),

      (try_begin), ######debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (try_begin), ######### returning to p_main_party
          (eq, ":target_party", "p_main_party"),
          (party_get_slot, ":party_leader", ":party_no", slot_party_orders_object),
          (party_get_slot, ":success", ":party_no", dplmc_slot_party_mission_diplomacy),
          (call_script, "script_add_notification_menu", "mnu_dplmc_messenger", ":party_leader", ":success"),
          (remove_party, ":party_no"),
          ##################### NEW v1.8 - removes 1
          (val_sub, "$g_player_messenger_count", 1),
        ######### (else_try), ######### patrols
          ######### (party_slot_eq, ":target_party", slot_party_type, spt_patrol),
          ######### (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),

          ######### (try_begin),
            ######### (eq, ":message", spai_retreating_to_center),
            ######### (remove_party, ":target_party"),
          ######### (else_try),
            ######### (str_store_party_name, s6, ":orders_object"),
            ######### (party_set_name, ":target_party", "@{s6} patrol"),
            ######### (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            ######### (party_set_ai_object, ":target_party", ":orders_object"),
            ######### (party_set_slot, ":target_party", slot_party_ai_object, ":orders_object"),
            ######### (party_set_slot, ":target_party", slot_party_orders_type, ":message"),
          ######### (try_end),

          ######### (remove_party, ":party_no"),
        (else_try), ######### reached any other target
          (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
          (str_store_troop_name, s13, ":party_leader"),

          (try_begin), ######debug
            (eq, "$cheat_mode", 1),
            (display_log_message, "@Your messenger reached {s13}.", 0x00FF00),
            (assign, "$g_talk_troop", ":party_leader"), ######debug
          (try_end),

          (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),
          (assign, ":success", 0),
          (try_begin),
            (party_set_slot, ":target_party", slot_party_commander_party, "p_main_party"),
              (store_current_hours, ":hours"),
              (party_set_slot, ":target_party", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
              (party_set_slot, ":target_party", slot_party_orders_object, ":orders_object"),
              (party_set_slot, ":target_party", slot_party_orders_type, ":message"),

              (party_set_slot, ":target_party", slot_party_orders_time, ":hours"),
            (call_script, "script_npc_decision_checklist_party_ai", ":party_leader"), ######This handles AI for both marshal and other parties


            (try_begin), ######debug
              (eq, "$cheat_mode", 1),
              (display_message, "@{s14}"), ######debug
            (try_end),

            (try_begin),
              (eq, reg0, ":message"),
              (eq, reg1, ":orders_object"),
              (assign, ":success", 1),
            (try_end),
            (call_script, "script_party_set_ai_state", ":target_party", reg0, reg1),
          (try_end),

          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":party_no", "p_main_party"),
          (party_set_slot, ":party_no", slot_party_ai_object, "p_main_party"),
          (party_set_slot, ":party_no", slot_party_orders_object, ":party_leader"),
          (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":success"),
        (try_end),
      (try_end),
    (else_try),
      (display_log_message, "@Your messenger has lost it's way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
      ##################### NEW v1.8 - removes 1
      (val_sub, "$g_player_messenger_count", 1),
    (try_end),
  (try_end),
 ]),
##############################################################################



   ######### Constable training
   ######### (24,
   ######### [
   ######### (eq, "$g_player_constable", "trp_dplmc_constable"),
   ######### (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
   ######### (party_slot_eq, "$g_constable_training_center", slot_town_lord, "trp_player"),

   ######### (store_skill_level, ":trainer_level", skl_trainer, "trp_player"),
   ######### (val_add, ":trainer_level", 4),
   ######### (store_div, ":xp_gain", ":trainer_level", 2),

   ######### (try_for_parties, ":party_no"),
    ######### (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
    ######### (eq, ":party_no", "$g_constable_training_center"),

    ######### (party_get_num_companion_stacks, ":num_stacks", ":party_no"),

    ######### (assign, ":trained", 0),
    ######### (try_for_range, ":i_stack", 0, ":num_stacks"),
      ######### (eq, ":trained", 0),
      ######### (party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
      ######### (neg|troop_is_hero, ":troop_id"),

      ######### (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , "$g_constable_training_type"),
      ######### (try_begin),
       ######### (le, ":upgrade_troop", 0),
       ######### (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id", 0),
      ######### (try_end),

     ######### ######only proceed if troop is upgradable
      ######### (gt, ":upgrade_troop", 0),

      ######### (store_character_level, ":troop_level", ":troop_id"),
      ######### (assign, ":troop_limit" , 6),
      
       ########## rafi
      ######### (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , 0),
      ######### (try_begin),
        ######### (eq, "$g_constable_training_type", 1),
        ######### (neg | troop_is_guarantee_ranged, ":upgrade_troop"),
        ######### (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , 1),
      ######### (else_try),
        ######### (eq, "$g_constable_training_type", 0),
        ######### (troop_is_guarantee_ranged, ":upgrade_troop"),
        ######### (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , 1),
      ######### (try_end),
      ########## end rafi

      ######### (try_begin),
        ######### (eq, "$g_constable_training_improved", 1),
        ######### (assign, ":troop_limit" , 10),
        ######### (try_begin),
          ######### (le, ":troop_level", 6),
          ######### (val_add, ":xp_gain", 2), ######more recruits are trained during improved training
        ######### (try_end),
      ######### (try_end),

      ######### (le, ":troop_level", ":troop_limit"),

      ######### (party_count_members_of_type, ":cur_number", ":party_no", ":troop_id"),
      ######### (val_min, ":xp_gain", ":cur_number"),

      ######### (call_script, "script_game_get_upgrade_cost", ":troop_id"),
      ######### (store_mul, ":upgrade_cost", ":xp_gain", reg0),

      ######### (try_begin),
        ######### (eq, "$g_constable_training_improved", 1),
        ######### (val_add, ":upgrade_cost", 10), ######+10 denars during improved training
      ######### (try_end),

      ######### (store_troop_gold, ":gold", "trp_household_possessions"),
      ######### (try_begin),
        ######### (lt, ":gold", ":upgrade_cost"),
        ######### (store_div, ":money_limit", ":gold", reg0),
        ######### (val_min, ":xp_gain", ":money_limit"),
        ######### (store_mul, ":upgrade_cost", ":xp_gain", reg0),
        ######### (display_message, "@Not enough money in treasury to upgrade troops."),
      ######### (try_end),

      ######### (party_remove_members, ":party_no", ":troop_id", ":xp_gain"),
      ######### (party_add_members, ":party_no", ":upgrade_troop", ":xp_gain"),

      ######### (call_script, "script_dplmc_withdraw_from_treasury", ":upgrade_cost"),

      ######### (assign, reg5, ":xp_gain"),
      ######### (str_store_troop_name, s6, ":troop_id"),
      ######### (str_store_troop_name, s7, ":upgrade_troop"),
      ######### (str_store_party_name, s8, ":party_no"),
      ######### (display_message, "@Your constable upgraded {reg5} {s6} to {s7} in {s8}"),
      ######### (assign, ":trained", 1),
    ######### (try_end),
   ######### (try_end),
    ######### ]),

  ######### Patrol wages
   ###### (168,
   ###### [

    ######### (try_for_parties, ":party_no"),
      ######### (party_slot_eq, ":party_no", slot_party_type, spt_patrol),

      ######### (store_faction_of_party, ":party_faction", ":party_no"),
      ######### (eq, ":party_faction", "fac_player_faction"),

      ######### (try_begin),
        ######### (eq, ":party_faction", "fac_player_faction"),
        ######### (assign, ":total_wage", 0),
        ######### (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        ######### (try_for_range, ":i_stack", 0, ":num_stacks"),
          ######### (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
          ######### (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
          ######### (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
          ######### (val_mul, reg0, ":stack_size"),
          ######### (val_add, ":total_wage", reg0),
        ######### (try_end),
        ######### (store_troop_gold, ":gold", "trp_household_possessions"),
        ######### (try_begin),
          ######### (lt, ":gold", ":total_wage"),
          ######### (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
          ######### (str_store_party_name, s6, ":target_party"),
          ######### (display_log_message, "@Your soldiers patrolling {s6} disbanded because you can't pay the wages!", 0xFF0000),
          ######### (remove_party, ":party_no"),
        ######### (try_end),
      ######### (try_end),
    ######### (try_end),
    ###### ]),



  ######### Patrol ai
   ######### (4, ######TOM was 2 ################## NOW 4
   (6, 
   [

    (try_for_parties, ":party"),
      (party_get_template_id, ":party_template", ":party"),
      (this_or_next | party_slot_eq, ":party", slot_party_type, spt_patrol),
      (this_or_next | eq, ":party_template", "pt_peasant_rebels_euro"),
      (this_or_next | eq, ":party_template", "pt_guelphs"),
      (this_or_next | eq, ":party_template", "pt_ghibellines"),
      (this_or_next | eq, ":party_template", "pt_prussians"),
      (this_or_next | eq, ":party_template", "pt_yotvingians"),
      (this_or_next | eq, ":party_template", "pt_curonians"),
      (this_or_next | eq, ":party_template", "pt_samogitians"),
      (this_or_next | eq, ":party_template", "pt_welsh"),
      (this_or_next | eq, ":party_template", "pt_mongolian_camp"),
################ NEW v1.8
      (this_or_next | eq, ":party_template", "pt_patrol_party"),
      (this_or_next | eq, ":party_template", "pt_rogue_mercenaries"),
      (this_or_next | eq, ":party_template", "pt_rebels"),
################
      (this_or_next | eq, ":party_template", "pt_jihadist_raiders"),
      (this_or_next | eq, ":party_template", "pt_teutonic_raiders"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_iberian"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_scandinavian"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_euro"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_italian"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_welsh"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_gaelic"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_teutonic"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_templar"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_hospitaller"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_saint_lazarus"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_santiago"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_calatrava"),
      (this_or_next | eq, ":party_template", "pt_crusader_raiders_saint_thomas"),
      (eq, ":party_template", "pt_sea_raiders"),
      
      (party_is_active, ":party"),
      (store_party_size_wo_prisoners, ":party_size", ":party"),
      (party_get_battle_opponent, ":opponent", ":party"),

      (try_begin),
        ###### (lt, ":opponent", 0),
        ###### (le, ":party_size", 10),
        ###### (neq, ":party_template", "pt_sea_raiders"),
        ###### (neq, ":party_template", "pt_mongolian_camp"),
        ###### (remove_party, ":party"),
      ###### (else_try),
        (lt, ":opponent", 0),
        (party_get_slot, ":target_party", ":party", slot_party_ai_object),
        (gt, ":target_party", 0),
        (party_is_active, ":target_party"),
        (try_begin),
          (store_distance_to_party_from_party, ":distance", ":party", ":target_party"),
          (gt, ":distance", 15),
          (party_set_ai_behavior, ":party", ai_bhvr_travel_to_point),
          (party_get_position, pos5, ":target_party"),
          (party_set_ai_target_position, ":party", pos5),
        (else_try),
          (get_party_ai_behavior, ":behavior", ":party"),
          (eq, ":behavior", ai_bhvr_travel_to_point),
          (try_begin),
            (store_distance_to_party_from_party, ":distance", ":party", ":target_party"),
            (lt, ":distance", 3),

            (party_set_ai_behavior, ":party", ai_bhvr_patrol_location),
            (party_set_ai_object, ":party", ":target_party"),
            (party_set_ai_patrol_radius, ":party", 15),
            (party_set_slot, ":party", slot_party_ai_object, ":target_party"),
          (try_end),
        (try_end),
      (try_end),
    (try_end),

    ######### (try_for_parties, ":party_no"),
      ######### (party_slot_eq, ":party_no", slot_party_type, spt_patrol),

      ######### (call_script, "script_party_remove_all_prisoners", ":party_no"),

      ######### (try_begin),
        ######### (get_party_ai_behavior, ":ai_behavior", ":party_no"),
        ######### (eq, ":ai_behavior", ai_bhvr_travel_to_party),
        ######### (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
        ######### (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
        ######### (le, ":distance_to_target", 5),
        ######### (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
      ######### (try_end),

      ######### (store_party_size, ":party_size", ":party_no"),
      ######### (try_begin),
        ######### (le, ":party_size", 2),
        ######### (try_begin),
          ######### (store_faction_of_party, ":party_faction", ":party_no"),
          ######### (eq, ":party_faction", "fac_player_faction"),
          ######### (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
          ######### (str_store_party_name, s6, ":target_party"),
          ######### (display_log_message, "@Your soldiers patrolling {s6} disbanded!", 0xFF0000),
        ######### (try_end),
        ######### (remove_party, ":party_no"),
      ######### (try_end),
    ######### (try_end),
    ]),

  ######### Policy
   ######### (30 * 24,
   ######### [
    ######### (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
      ######### (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),

      ######### (faction_get_slot, ":centralization", ":kingdom", dplmc_slot_faction_centralization),
      ######### (faction_get_slot, ":aristocracy", ":kingdom", dplmc_slot_faction_aristocracy),

      ######### (val_mul, ":centralization", ":centralization", -1),
      ######### (val_mul, ":aristocracy", ":aristocracy", 1),
      ######### (store_add, ":relation_change", ":centralization", ":aristocracy"),

      ######### (try_begin),
        ######### (neq, ":relation_change", 0),

        ######### (try_begin),
          ######### (eq, "$cheat_mode", 1),
          ######### (str_store_faction_name, s9, ":kingdom"),
          ######### (display_message, "@{!}DEBUG - relation_change != 0 for {s9}"),
        ######### (try_end),

        ######### (try_for_range, ":troop_no", lords_begin, lords_end),
          ######### (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          ######### (store_troop_faction, ":faction_no", ":troop_no"),
          ######### (eq, ":kingdom", ":faction_no"),
          ######### (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader),
          ######### (call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":troop_no", ":relation_change"),
      ######### (try_end),
    ######### (try_end),

    ######### ]),
  #######diplomacy end



 ######process messengers
 ######### (1, ######TOM was 1
 (2, ######TOM was 1
 [
 ######tom debug
 ######### (store_current_hours, reg0),
 ######### (store_current_day, reg1),
 ######### (display_message, "@current hour {reg0}"),
 ######### (display_message, "@current day {reg1}"),
 
############# NEW v1.8
(gt, "$g_raf_spt_messenger", 0),
  (try_for_parties, ":party_no"),
    (party_slot_eq, ":party_no", slot_party_type, raf_spt_messenger),

    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":companion_no", ":party_no", slot_party_orders_object),
    (troop_get_slot, ":new_target_party", ":companion_no", slot_troop_cur_center),
    (party_get_slot, ":party_home", ":party_no", slot_party_home_center),
    (party_get_slot, ":orig_faction", ":party_no", slot_center_original_faction),

    (try_begin),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", ":orig_faction"),
      (party_set_faction, ":party_no", "$players_kingdom"),
      (party_set_slot, ":party_no", slot_center_original_faction, "$players_kingdom"),
    (else_try),
      (neq, "fac_player_faction", ":orig_faction"),
      (le, "$players_kingdom", 0),
      (party_set_faction, ":party_no", "fac_player_faction"),
      (party_set_slot, ":party_no", slot_center_original_faction, "fac_player_faction"),
    (try_end),

    (try_begin),
      (neq, ":new_target_party", ":target_party"),
      (neq, ":target_party", ":party_home"),
      (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
      (party_set_ai_object, ":party_no", ":new_target_party"),
      (party_set_slot, ":party_no", slot_party_ai_object, ":new_target_party"),
    (else_try),
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (try_begin),
        (le, ":distance_to_target", 1), ######### arrived
        (neq, ":target_party", ":party_home"),
        (str_store_party_name, s25, ":party_home"),
        (str_store_troop_name, s26, ":companion_no"),
        (display_message, "@Your messenger has delivered his message to {s26} and is on his way back to {s25}", 0x00ff00),
        (party_add_members, ":party_no", ":companion_no", 1),
        (troop_set_slot, ":companion_no", slot_troop_cur_center, ":party_no"),
        (troop_set_slot, ":companion_no", slot_troop_traveling, 1),
        (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
        (party_set_ai_object, ":party_no", ":party_home"),
        (party_set_slot, ":party_no", slot_party_ai_object, ":party_home"),
      (else_try),
        (le, ":distance_to_target", 1), ######### arrived
        (eq, ":target_party", ":party_home"),
        (troop_set_slot, ":companion_no", slot_troop_cur_center, ":party_home"),
        (str_store_party_name, s25, ":party_home"),
        (str_store_troop_name, s26, ":companion_no"),
        (display_message, "@{s26} has arrived in {s25} and is awaiting you there.", 0x00ff00),
        (remove_party, ":party_no"),
        ################## NEW v1.8
        (val_sub, "$g_raf_spt_messenger", 1),
      (try_end),
    (try_end),
  (try_end),
 ]),
 
  ###### (0,
  (6,
    [   
    (eq, "$g_battle_preparation_phase", 2),
        
    (party_set_slot, "$g_battle_preparation", slot_party_battle_preparation, 1),
    (try_for_parties, ":party"),
      (str_store_party_name, s20, ":party"),
      (neq, ":party", "$g_battle_preparation"),
      (neq, ":party", "p_main_party"),
      (neg | party_slot_eq, ":party", slot_party_battle_preparation, 1),      
      (this_or_next | party_slot_eq, ":party", slot_party_type, spt_patrol),
      (this_or_next | party_slot_eq, ":party", slot_party_type, spt_merc_party), ######tom
      (party_slot_eq, ":party", slot_party_type, spt_kingdom_hero_party),
      (party_is_active, ":party"),
      (party_get_battle_opponent, ":opponent", ":party"),
      (lt, ":opponent", 0), ######party is not itself involved in a battle
      (party_get_attached_to, ":attached_to", ":party"),
      (lt, ":attached_to", 0), ######party is not attached to another party
      (get_party_ai_behavior, ":behavior", ":party"),      
      (neq, ":behavior", ai_bhvr_in_town),      
      (store_faction_of_party, ":faction_no", ":party"),
      (store_relation, ":rel", "fac_player_supporters_faction", ":faction_no"),
      (this_or_next | eq, ":faction_no", "$players_kingdom"),
      (lt, ":rel", 0),
      (store_distance_to_party_from_party, ":distance", ":party", "p_main_party"),      
      (le, ":distance", 5),      
      (party_set_slot, ":party", slot_party_battle_preparation, 1),
    (try_end),
    
    (try_begin),
      (map_free),
      (rest_for_hours, 12, 3, 0),
    (try_end),

    (store_current_hours, ":cur_hours"),
    (store_sub, ":hours_elapsed", ":cur_hours", "$g_battle_preparation_start"),
    (ge, ":hours_elapsed", 12),
    ######(assign, ":enemy_party", "$g_battle_preparation"),       
    (assign, "$g_battle_preparation_phase", 3),
    (assign, "$g_battle_preparation_start", ":cur_hours"),
    ######(party_stack_get_troop_id, ":leader", "$g_battle_preparation", 0),
    ######(start_map_conversation, ":leader", -1),
    ]),

   (0,
   [
    (is_between, "$g_player_sally_town", centers_begin, centers_end),
    (party_is_active, "$g_player_sallies"),
    (start_encounter, "$g_player_sallies"),
  ]),
  ######### (0,
    ######### [   
    ######### (eq, "$g_battle_preparation_phase", 0),
    ######### (try_for_parties, ":party"),
      ######### (party_slot_eq, ":party", slot_party_battle_preparation, 1),
      ######### (party_set_slot, ":party", slot_party_battle_preparation, -1),
    ######### (try_end),
  ######### ]),
 
 
 (4,
 [  ######tom - weather
        ######(call_script, "script_get_closest_center", "p_main_party"),
        ######(party_get_slot, ":faction_no", reg0, slot_center_original_faction), 
        (party_get_current_terrain, ":terrain_type", "p_main_party"),
        (try_begin),
          (this_or_next|eq, ":terrain_type", rt_snow),
          (eq, ":terrain_type", rt_snow_forest),
          ######### (assign, "$g_rand_rain_limit", 40),
          (assign, "$tom_sand_storm_chance", 20),
          (set_global_haze_amount, 0),
          (store_random_in_range, ":fog", 25, 101), ######autumn - cloudy
          (set_global_cloud_amount, ":fog"),
        (else_try),
          (this_or_next|eq, ":terrain_type", rt_plain),
          (eq, ":terrain_type", rt_forest),
          ######### (assign, "$g_rand_rain_limit", 25),
          (assign, "$tom_sand_storm_chance", 15),
          (store_random_in_range, ":fog", 0, 101),
          (set_global_haze_amount, ":fog"),
          (store_random_in_range, ":fog", 15, 100), ######autumn - cloudy
          (set_global_cloud_amount, ":fog"),
        (else_try),
          (this_or_next|eq, ":terrain_type", rt_steppe),
          (eq, ":terrain_type", rt_steppe_forest),
          ######### (assign, "$g_rand_rain_limit", 10),
          (assign, "$tom_sand_storm_chance", 10),  
          (store_random_in_range, ":fog", 0, 50), ######autumn - not realy cloudy in the warm things
          (set_global_haze_amount, ":fog"),
          (store_random_in_range, ":fog", 0, 80), ######autumn - not realy cloudy in the warm things
          (set_global_cloud_amount, ":fog"),
        (else_try),
          (this_or_next|eq, ":terrain_type", rt_desert),
          (eq, ":terrain_type", rt_desert_forest),
          ######(assign, "$g_rand_rain_limit", 0),
          (assign, "$tom_sand_storm_chance", 25), 
          (set_global_haze_amount, 0),        
          (set_global_cloud_amount, 0),          
        (else_try),
          (assign, "$tom_sand_storm_chance", 15),
          (store_random_in_range, ":fog", 0, 101),
          (set_global_haze_amount, ":fog"),
          (store_random_in_range, ":fog", 0, 101), ######autumn - cloudy
          (set_global_cloud_amount, ":fog"),
        (try_end),
    ]),
    
  
  ########manor trigger
  (168,
  ######(1,
  [
  ######### slot_town_wealth        = 49 ######total amount of accumulated wealth in the center, pays for the garrison
  ######### slot_town_prosperity    = 50 ######affects the amount of wealth generated
    ######TODO: global - bandits
    (troop_get_slot, ":manor_amount", "trp_manor_array", 0),
    (try_for_range, ":troop_slot", 1, ":manor_amount"),
      (troop_get_slot, ":manor_id", "trp_manor_array", ":troop_slot"),
      ######manor center should not be looted
      (party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
      (this_or_next|neg|party_slot_eq, ":village", slot_village_state, svs_looted), 
      (party_slot_eq, ":manor_id", manor_slot_walls, manor_building_operational), ######has walls so does not effect
      ######lets get some basic values
      (party_get_slot, ":village_lord", ":village", slot_town_lord), 
      (party_get_slot, ":cur_prosperity", ":manor_id", slot_town_prosperity),
      (party_get_slot, ":population", ":manor_id", manor_slot_population),
      (party_get_slot, ":taxes", ":manor_id", manor_slot_taxes),
      (party_get_slot, ":manor_gold", ":manor_id", manor_slot_gold),
      (assign, ":gold", 0),
      
      ######change faction
      (try_begin),
        (store_faction_of_party, ":cur_faction", ":village"),
        (party_set_faction, ":manor_id", ":cur_faction"),
        (party_set_slot, ":manor_id", slot_town_lord, ":village_lord"),
      (try_end),
      ######building buildings
      (assign, ":prosperity", 0), ######da fuck is this?
      (try_for_range, ":slot", manor_slot_marketplace, manor_slot_walls + 1),
        (party_slot_eq, ":manor_id", ":slot", manor_building_inprogress),
        (party_set_slot, ":manor_id", ":slot", manor_building_operational),
        (try_begin),
          (this_or_next|eq, ":slot", manor_slot_marketplace),
          (this_or_next|eq, ":slot", manor_slot_Monastery),
          (this_or_next|eq, ":slot", manor_slot_whorehouse),
          (eq, ":slot", manor_slot_tavern),
          (val_add, ":prosperity", 15),
        (else_try),
          (eq, ":slot", manor_slot_well),
          (val_add, ":prosperity", 10),
        (try_end),
        (try_begin),
          (eq, ":village_lord", "trp_player"),
          (try_begin),##renown increase
            (eq, ":slot", manor_slot_whorehouse),
            (display_message, "@Peasants rejoice of your whorehouse in the regional manor. You gain fame!"),
            (call_script, "script_change_troop_renown", "trp_player", 5),
          (else_try),##RTR increase
            (this_or_next|eq, ":slot", manor_slot_prison),
            (this_or_next|eq, ":slot", manor_slot_armorsmith),
            (this_or_next|eq, ":slot", manor_slot_weaponsmith),
            (this_or_next|eq, ":slot", manor_slot_fletcher),
            (this_or_next|eq, ":slot", manor_slot_breeder),
            (eq, ":slot", manor_slot_walls),
            (display_message, "@You gain right to rule for building an important building in your regional manor!"),
            (call_script, "script_change_player_right_to_rule", 2),
          (else_try),##renown increase
            (display_message, "@You gain renown for funding a building in your regional manor"),
            (call_script, "script_change_troop_renown", "trp_player", 1),
          (try_end),
        (try_end),
      (try_end),
      
      ######taxes - buildings
      (try_for_range, ":slot", manor_slot_marketplace, manor_slot_walls + 1),
        (party_slot_eq, ":manor_id", ":slot", manor_building_operational),
        (store_sub, ":troop", ":slot", manor_slot_grainfarm),
        (val_add, ":troop", "trp_manor_grain"),
        (assign, ":tribute", 0),
        (assign, ":goods", -1),
        (assign, ":amount", -1),
        (troop_get_slot, ":tax_slot", ":troop",manor_troop_slot_tax),
        (party_get_slot, ":tax_type", ":manor_id", ":tax_slot"),
        (assign, ":debug_tribute", 0),
        (try_begin), ######tier1
          (is_between, ":slot", manor_slot_grainfarm, manor_slot_bakery),
          (try_begin),
            (this_or_next|neq, ":village_lord", "trp_player"), ######gold if it's not player
            ######(troop_slot_eq, ":troop", manor_troop_slot_tax, manor_troop_taxes_money),
            (eq, ":tax_type", manor_troop_taxes_money),
            (val_add, ":tribute", manor_taxes_tier1),
            (val_add, ":debug_tribute", manor_taxes_tier1),
          (else_try),
            ######(troop_slot_eq, ":troop", manor_troop_slot_tax, manor_troop_taxes_goods),
            (eq, ":tax_type", manor_troop_taxes_goods),
            (troop_get_slot, ":goods", ":troop", manor_troop_slot_good),
            (assign, ":amount", 4),
          (try_end),
        (else_try), ######tier2
          (this_or_next|eq, ":slot", manor_slot_marketplace),
          (this_or_next|eq, ":slot", manor_slot_tavern),
          (eq, ":slot", manor_slot_whorehouse),
          (val_add, ":tribute", manor_taxes_tier2),
          (val_add, ":debug_tribute", manor_taxes_tier2),
        (else_try), ######tier3
          (is_between, ":slot", manor_slot_bakery, manor_slot_prison),
          (try_begin),
            (this_or_next|neq, ":village_lord", "trp_player"), ######gold if it's not player
            ######(troop_slot_eq, ":troop", manor_troop_slot_tax, manor_troop_taxes_money),
            (eq, ":tax_type", manor_troop_taxes_money),
            (val_add, ":tribute", manor_taxes_tier3),
            (val_add, ":debug_tribute", manor_taxes_tier3),
          (else_try),
            (this_or_next|neq, ":village_lord", "trp_player"), ######gold if it's not player
            ######(troop_slot_eq, ":troop", manor_troop_slot_tax, manor_troop_taxes_goods),
            (eq, ":tax_type", manor_troop_taxes_goods),
            (troop_get_slot, ":goods", ":troop", manor_troop_slot_good),
            (assign, ":amount", 3),
          (try_end),
        (else_try), ######tier4
          (is_between, ":slot", manor_slot_armorsmith, manor_slot_walls),
          ######Is this needed?! - no
          ######(troop_slot_eq, ":troop", manor_troop_slot_tax, manor_troop_taxes_money),
          (val_add, ":tribute", manor_taxes_tier4),
        (try_end),
        (try_begin), ######if gold then +/-5.
          (ge, ":tribute", 1),
          (store_random_in_range, ":random", -5, 5),
          (val_add, ":tribute", ":random"),
          (val_add, ":gold", ":tribute"),
          (val_add, ":debug_tribute", ":random"),
        (try_end),
        
        #######debug
        (try_begin),
          (eq, "$cheat_mode", 1),
          (eq, ":village_lord", "trp_player"),
          (str_store_troop_name,s1, ":troop"),
          (assign, reg1, ":debug_tribute"),
          (display_message, "@MANOR troop: {s1} pays {reg1} gold"),
        (try_end),
        #######debug
        
        ######if the troop pays in goods
        (ge, ":amount", 0),
        (ge, ":goods", 0),
        (try_begin),
          (eq, ":taxes", manor_high_taxes),
          (val_div, ":amount", 2),
        (else_try),
          (eq, ":taxes", manor_low_taxes),
          (val_mul, ":amount", 3),
          (val_div, ":amount", 2),
        (try_end),
        (troop_ensure_inventory_space, "trp_manor_array", ":amount"), ######lets add shit to him
        (troop_add_items, "trp_manor_array", ":goods", ":amount"),
      (try_end),
      
      ######things the manor pays for
      (try_begin),
        (party_slot_eq, ":manor_id", manor_slot_walls, manor_building_operational),
        (val_sub, ":gold", 500),
        (lt, ":gold", 0),
        (assign, ":gold", 0),
      (try_end),
      
      ######### (assign, reg0, ":gold"),
      ######### (display_message, "@gold :{reg0}"),
      ######### (assign, reg0, ":population"),
      ######### (display_message, "@population :{reg0}"),
      
      ######population pays taxes too
      (val_add, ":gold", ":population"),
      
      ######(assign, reg0, ":gold"),
      ######(display_message, "@gold :{reg0}"),
      
      ######prosperity and population todo: change based on things
      ######clamp based population
      (try_begin),
        (party_slot_eq, ":manor_id", manor_slot_houses, 0), ######up to 200
        (val_clamp, ":population", 20, manor_population_tier1),
      (else_try),
        (party_slot_eq, ":manor_id", manor_slot_houses, 1), ######Up to 760
        (val_clamp, ":population", 20, manor_population_tier2),
      (else_try),
        (party_slot_eq, ":manor_id", manor_slot_houses, 2), ######rest of it - 1000
        (val_clamp, ":population", 20, manor_population_tier3),
      (try_end),
      
      (store_random_in_range, ":random", -5, 6),
      (val_add, ":population", ":random"),
      (try_begin),
        (eq, ":taxes", manor_high_taxes),
        (val_sub, ":prosperity", 3),
        (val_add, ":population", 15),
        (val_mul, ":gold", 3),
        (val_div, ":gold", 2),
      (else_try),
        (eq, ":taxes", manor_medium_taxes),
        (val_add, ":prosperity", 1),
        (val_add, ":population", 40),
      (else_try),
        (eq, ":taxes", manor_low_taxes),
        (val_add, ":prosperity", 2),
        (val_add, ":population", 50),
        (val_div, ":gold", 2),
      (try_end),
      (val_clamp, ":prosperity", 0, 100),
      
      ######prosperity effects taxes
      (try_begin),
        (assign, ":precent", ":cur_prosperity"),
        (val_clamp, ":precent", 5, 100),
        (val_mul, ":gold", ":precent"),
        (val_div, ":gold", 100),
      (try_end),
      
      ######lets try to get some traders
      (try_begin),
        (party_set_slot, ":manor_id", manor_slot_trader, -1), 
        (party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_operational),
        (ge, ":cur_prosperity", 50),
        (ge, ":population", 700),
        (store_random_in_range, ":trader", "trp_manor_trader_silk", "trp_temp_lord"),
        (party_set_slot, ":manor_id", manor_slot_trader, ":trader"),
        
        (troop_get_slot, ":good", ":trader", manor_troop_slot_good),
        (troop_clear_inventory, ":trader"),
        (store_random_in_range, ":random", 5, 10),
        (troop_add_items, ":trader", ":good", ":random"),
        (store_troop_gold, ":gold_trader", ":trader"),
        (troop_remove_gold, ":trader", ":gold_trader"),
        (store_random_in_range, ":gold_trader", 200, 800),
        (troop_add_gold, ":trader", ":gold_trader"),
      (try_end),
      
      ######Monastery
      (try_begin),
        (party_slot_eq, ":manor_id", manor_slot_Monastery_upgrade, manor_Monastery_scriptorium), 
        
        (store_random_in_range, ":book", "itm_book_tactics", "itm_spice"),
        (troop_clear_inventory, "trp_manor_trader_book"),
        (troop_add_items, "trp_manor_trader_book", ":book", 1), ######one book each week
        (store_troop_gold, ":gold_trader", "trp_manor_trader_book"),
        (troop_remove_gold, "trp_manor_trader_book", ":gold_trader"),
        (store_random_in_range, ":gold_trader", 200, 300),
        (troop_add_gold, "trp_manor_trader_book", ":gold_trader"),
      (try_end),
      
      ######sum the gold amount
      (val_add, ":manor_gold", ":gold"),
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (eq, ":village_lord", "trp_player"),
        (assign, reg0, ":gold"),
        (assign, reg1, ":manor_gold"),
        (display_message, "@final gold :{reg0}, manor gold: {reg1}"),
      (try_end),
      
      ######set the new values
      (val_add, ":prosperity", ":cur_prosperity"),
      (val_clamp, ":prosperity", 0, 100),
      (party_set_slot, ":manor_id", slot_town_prosperity, ":prosperity"),
      (party_set_slot, ":manor_id", manor_slot_population, ":population"),
      (party_set_slot, ":manor_id", manor_slot_last_tax, ":gold"),
      (party_set_slot, ":manor_id", manor_slot_gold, ":manor_gold"),
      ######(troop_add_gold, "trp_manor_seneschal", ":gold"),
    (try_end),
    
  ]),
  
  (168,#developing buildings
  [
    (troop_get_slot, ":amount", "trp_manor_array", 0),
    (try_for_range, ":slot", 1, ":amount"),
      (troop_get_slot, ":manor_id", "trp_manor_array", ":slot"),
      (party_get_slot, ":village", ":manor_id", slot_village_bound_center), 
      (party_get_slot, ":village_lord", ":village", slot_town_lord), 
      (neq, ":village_lord", "trp_player"),
      ######manor center should not be looted
      (neg|party_slot_eq, ":village", slot_village_state, svs_looted), 
      ######(party_slot_eq, ":manor_id", manor_slot_walls, manor_building_operational), ######has walls so does not effect
      ######lets get some basic values
     ######### (party_get_slot, ":cur_prosperity", ":manor_id", slot_town_prosperity),
     ######### (party_get_slot, ":population", ":manor_id", manor_slot_population),
      (party_get_slot, ":taxes", ":manor_id", manor_slot_gold),
      (ge, ":taxes", 2000), 
      (try_begin),
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_grainfarm, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_livestock, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_fruitfarm, manor_building_notbuild), 
        ######### (party_slot_eq, ":manor_id", manor_slot_fisher, manor_building_notbuild), 
        (store_random_in_range, ":random", manor_slot_grainfarm, manor_slot_fisher+1),
        (party_slot_eq, ":manor_id", ":random", manor_building_notbuild), 
        (party_set_slot, ":manor_id", ":random", manor_building_operational),
        (val_sub, ":taxes", 2000),#half of it please
      (else_try),    
        (ge, ":taxes", 3000), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_marketplace, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_well, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_whorehouse, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_Monastery, manor_building_notbuild), 
        ######### (party_slot_eq, ":manor_id", manor_slot_well, manor_building_notbuild), 
        (store_random_in_range, ":random", manor_slot_marketplace, manor_slot_well+1),
        (party_slot_eq, ":manor_id", ":random", manor_building_notbuild), 
        (party_set_slot, ":manor_id", ":random", manor_building_operational),
        (val_sub, ":taxes", 3000),#half of it please
      (else_try),    
        (ge, ":taxes", 6000), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_bakery, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_winery, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_brewery, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_potter, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_blacksmith, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_butcher, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_oilmaker, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_linenworkshop, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_woolworkshop, manor_building_notbuild), 
        ######### (party_slot_eq, ":manor_id", manor_slot_tannery, manor_building_notbuild), 
        (store_random_in_range, ":random", manor_slot_marketplace, manor_slot_well+1),
        (party_slot_eq, ":manor_id", ":random", manor_building_notbuild), 
        (party_set_slot, ":manor_id", ":random", manor_building_operational),
        (val_sub, ":taxes", 6000),#half of it please
      (else_try),    
        (ge, ":taxes", 10000), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_prison, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_armorsmith, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_weaponsmith, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_fletcher, manor_building_notbuild), 
        ######### (this_or_next|party_slot_eq, ":manor_id", manor_slot_breeder, manor_building_notbuild), 
        ######### (party_slot_eq, ":manor_id", manor_slot_walls, manor_building_notbuild), 
        (store_random_in_range, ":random", manor_slot_marketplace, manor_slot_well+1),
        (party_slot_eq, ":manor_id", ":random", manor_building_notbuild), 
        (party_set_slot, ":manor_id", ":random", manor_building_operational),
        (val_sub, ":taxes", 10000),#half of it please
      (try_end),
      (party_set_slot, ":manor_id", manor_slot_gold, ":taxes"),
      #######TODO - population increase?
    (try_end),
  ]),
  

  ######traveling merchant cycle!
  (24*3,
  [
    (try_for_range, ":merchant", traders_begin, traders_end),
      (store_random_in_range, ":town", towns_begin, towns_end),
      (troop_set_slot, ":merchant", slot_troop_cur_center, ":town"),
      
      (troop_clear_inventory, ":merchant"),
      (try_begin),###HATS!
        (is_between, ":merchant", "trp_trader_hat1", "trp_trader_sword1"),
        (try_for_range, reg0, 0, 30),
          # (store_random_in_range, ":itm", "itm_sarranid_head_cloth", "itm_leather_steppe_cap_a"),
          (store_random_in_range, ":itm", "itm_head_wrappings", "itm_wooden_shield"), ##### NEW v2.6 - bugfix
          (troop_add_item, ":merchant", ":itm"),
        (try_end),
      (else_try), ########sword
        (is_between, ":merchant", "trp_trader_sword1", "trp_trader_helmet1"),
        (try_for_range, reg0, 0, 25),
          # (store_random_in_range, ":itm", "itm_sword_type_xii", "itm_spatha"),
		  ############## NEW v2.6 - item ordering was rearranged so this needs a rework
          (store_random_in_range, ":number", 0, 4),
          (try_begin),
            (eq, ":number", 0),
              (store_random_in_range, ":itm", "itm_spatha", "itm_military_cleaver_b"),
              (troop_add_item, ":merchant", ":itm"),
          (else_try),
            (eq, ":number", 1),
              (store_random_in_range, ":itm", "itm_sword_viking_1", "itm_military_hammer"),
              (troop_add_item, ":merchant", ":itm"),
          (else_try),
            (eq, ":number", 2),
              (store_random_in_range, ":itm", "itm_baltic_sword", "itm_iberian_cleaver"),
              (troop_add_item, ":merchant", ":itm"),
          (else_try),
            (eq, ":number", 3),
              (store_random_in_range, ":itm", "itm_alsacian_sword", "itm_modded_club"),
              (troop_add_item, ":merchant", ":itm"),
          (try_end),
		  ##############
        (try_end),
      (else_try),###helmet
        (is_between, ":merchant", "trp_trader_helmet1", "trp_trader_spice1"),
        (try_for_range, reg0, 0, 30),
          # (store_random_in_range, ":itm", "itm_flat_topped_helmet_a", "itm_bill"), ######only great helmets?
          (store_random_in_range, ":itm", "itm_elm8", "itm_african_turban"),  ##### NEW v2.6 - bugfix
          (troop_add_item, ":merchant", ":itm"),
        (try_end),
      (else_try),###spice
        (is_between, ":merchant", "trp_trader_spice1", "trp_trader_silk1"),
        (try_for_range, reg0, 0, 10),
          (troop_add_item, ":merchant", "itm_spice"),
          (troop_add_item, ":merchant", "itm_salt"),
        (try_end),
      (else_try),###silk
        (is_between, ":merchant", "trp_trader_silk1", "trp_maid_1"),
        (try_for_range, reg0, 0, 10),
          (troop_add_item, ":merchant", "itm_raw_silk"),
          (troop_add_item, ":merchant", "itm_velvet"),
        (try_end),
      (try_end),
      (store_troop_gold, reg6, ":merchant"),
      (troop_remove_gold, ":merchant",reg6),
      (store_random_in_range, ":new_gold", 2000, 3500),
      (call_script, "script_troop_add_gold", ":merchant", ":new_gold"),
    (try_end),
    
    
    ##########4 debuging
    ######### (troop_set_slot, "trp_trader_hat1", slot_troop_cur_center, "p_town_2_1"),
    ######### (troop_set_slot, "trp_trader_sword1", slot_troop_cur_center, "p_town_2_1"),
    ######### (troop_set_slot, "trp_trader_helmet1", slot_troop_cur_center, "p_town_2_1"),
    ######### (troop_set_slot, "trp_trader_spice1", slot_troop_cur_center, "p_town_2_1"),
    ######### (troop_set_slot, "trp_trader_silk1", slot_troop_cur_center, "p_town_2_1"),
  ]),
   
 ########PROSPERITY SYSTEM 
 (24,
 [
    (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
      (faction_set_slot, ":faction", slot_faction_at_war, 0),
      (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
      (call_script, "script_check_if_faction_is_at_war", ":faction"),
      (faction_set_slot, ":faction", slot_faction_at_war, reg0),
    (try_end),
 ]),
 
 
 
 
################## NEW v1.8 - https://forums.taleworlds.com/index.php?topic=6575.msg9041351#msg9041351
#### (168,
(0.23,  ########################## once a week for each of the 733 centers
[
 (try_begin),
   (lt, "$g_change_prosperity_cur_center", centers_begin), 
   (assign, "$g_change_prosperity_cur_center", centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_change_prosperity_cur_center", centers_end), 
   (assign, "$g_change_prosperity_cur_center", centers_begin),
 (try_end),
   
 (try_begin),
   (store_faction_of_party, ":faction", "$g_change_prosperity_cur_center"),
   (faction_get_slot, ":war", ":faction", slot_faction_at_war),
   (party_get_slot, ":tax_rate", "$g_change_prosperity_cur_center", dplmc_slot_center_taxation),
   (party_get_slot, ":lord", "$g_change_prosperity_cur_center", slot_town_lord),
   (party_get_slot, ":prosperity", "$g_change_prosperity_cur_center", slot_town_prosperity),
   (assign, reg1, ":prosperity"),
   (try_begin), ######at peace  +20 prosperity
     (eq, ":war", 0),
     (call_script, "script_change_center_prosperity", "$g_change_prosperity_cur_center", 20), ######was 10
   (try_end),
   (call_script, "script_change_center_prosperity", "$g_change_prosperity_cur_center", 5), ######improves prosperity at war as well
   ######### (assign, ":random", 0),
   ######### (try_begin),
     ######### (lt, ":tax_rate", 0),
     ######### (store_random_in_range, ":random", ":tax_rate", 1), ######range -2 0
     ######### (val_mul, ":random", -1), ######positive value to increase
   ######### (else_try),
     ######### (gt, ":tax_rate", 0),
     ######### (val_add, ":tax_rate", 1),
     ######### (store_random_in_range, ":random", 0, ":tax_rate"), ######range 0 2
     ######### (val_mul, ":random", -1), ######negetive value to increase
   ######### (try_end),
   ######### (call_script, "script_change_center_prosperity", "$g_change_prosperity_cur_center", ":random"),
   
   (store_mul, ":tax_prosperity", ":tax_rate", -1),
   (call_script, "script_change_center_prosperity", "$g_change_prosperity_cur_center", ":tax_prosperity"),
   (val_add, ":prosperity", ":tax_prosperity"),    
   
   #######set ai taxes
   (neq, ":lord", "trp_player"),
   (try_begin),
     (le, ":prosperity", 20),
     (gt, ":tax_rate", rate_very_low),
     (val_sub, ":tax_rate", 1),
     (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, ":tax_rate"), 
   (else_try),
     (ge, ":prosperity", 99),
     (lt, ":tax_rate", rate_very_high),
     (val_add, ":tax_rate", 1),
     (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, ":tax_rate"),
   (else_try),
     (store_random_in_range, ":random", 0, 10),
     (eq, ":random", 0),
     ######### (try_begin),
       ######### (is_between, ":prosperity", 0, 25),
       ######### (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, rate_very_low), 
     ######### (else_try),
       ######### (is_between, ":prosperity", 25, 50),
       ######### (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, rate_average), 
     ######### (else_try),
       ######### (is_between, ":prosperity", 50, 75),
       ######### (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, rate_high), 
     ######### (else_try),
       ######### (is_between, ":prosperity", 75, 101),
         ######### (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, rate_very_high), 
     ######### (try_end),
     (store_random_in_range, ":random", rate_very_low, rate_very_high + 1),
     (party_set_slot, "$g_change_prosperity_cur_center", dplmc_slot_center_taxation, ":random"), 
   (try_end),
   #######debug
   ######### (party_get_slot, ":prosperity", ":center", slot_town_prosperity),
   ######### (assign, reg2, ":prosperity"),
   ######### (str_store_party_name, s0, ":center"),
   ######### (store_sub, reg3, reg2, reg1),
   ######### (party_get_slot, reg4, ":center", dplmc_slot_center_taxation),
   ######### (display_message, "@{s0} prosperity before: {reg1}, after: {reg2}, change: {reg3}, tax rate: {reg4}"),
 (try_end),
 
 ################ proceeds to the next center when it's triggered again
 (val_add, "$g_change_prosperity_cur_center", 1),
    
 ################### DEBUG
 (val_add, "$g_simple_trigger_fire_count_37", 1),
]),
###PROSPERITY SYSTEM
################################################################################




 (24,
   [
      ######### Setting food bonuses in every 6 hours again and again because of a bug (we could not find its reason) which decreases especially slot_item_food_bonus slots of items to 0.
      ######Staples
      (item_set_slot, "itm_bread", slot_item_food_bonus, 8), ######brought up from 4
      (item_set_slot, "itm_grain", slot_item_food_bonus, 2), ######new - can be boiled as porridge
      
      ######Fat sources - preserved
      (item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 4),
      (item_set_slot, "itm_dried_meat", slot_item_food_bonus, 5),
      (item_set_slot, "itm_cheese", slot_item_food_bonus, 5),
      (item_set_slot, "itm_sausages", slot_item_food_bonus, 5),
      (item_set_slot, "itm_butter", slot_item_food_bonus, 4), ######brought down from 8

      ######Fat sources - perishable
      (item_set_slot, "itm_chicken", slot_item_food_bonus, 8), ######brought up from 7
      (item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 7), ######brought down from 7
      (item_set_slot, "itm_pork", slot_item_food_bonus, 6), ######brought down from 6
      
      ######Produce
      (item_set_slot, "itm_raw_olives", slot_item_food_bonus, 1),
      (item_set_slot, "itm_cabbages", slot_item_food_bonus, 2),
      (item_set_slot, "itm_raw_grapes", slot_item_food_bonus, 3),
      (item_set_slot, "itm_apples", slot_item_food_bonus, 4), ######brought down from 5

      ######Sweet items
      (item_set_slot, "itm_raw_date_fruit", slot_item_food_bonus, 4), ######brought down from 8
      (item_set_slot, "itm_honey", slot_item_food_bonus, 6), ######brought down from 12
      
      (item_set_slot, "itm_wine", slot_item_food_bonus, 7),
      (item_set_slot, "itm_ale", slot_item_food_bonus, 6),
   ]),
  
  
  
#rubik Source code of Restoration
#### restoration begin
  ######### Note: make sure there is a comma in the entry behind this one
  
  
    (168,
    [
    (try_begin),
      (eq, "$kaos_restore", 1),
      (assign, ":continue", 1),
      (try_for_range, ":cur_troop", "trp_npc1", "trp_knight_1_1_wife"),
        (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":original_faction", ":cur_troop", slot_troop_original_faction),
        (neg|faction_slot_eq, ":original_faction", slot_faction_state, sfs_active),
        (try_begin),
          (eq, "$background_answer_3", 8),
          (try_begin),
            (eq, ":original_faction", "fac_kingdom_1"),
            (eq, "$kaos_kings_kingdom", 1),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_2"),
            (eq, "$kaos_kings_kingdom", 2),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_3"),
            (eq, "$kaos_kings_kingdom", 3),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_4"),
            (eq, "$kaos_kings_kingdom", 4),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_5"),
            (eq, "$kaos_kings_kingdom", 5),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_6"),
            (eq, "$kaos_kings_kingdom", 6),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_7"),
            (eq, "$kaos_kings_kingdom", 7),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_8"),
            (eq, "$kaos_kings_kingdom", 8),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_9"),
            (eq, "$kaos_kings_kingdom", 9),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_10"),
            (eq, "$kaos_kings_kingdom", 10),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_11"),
            (eq, "$kaos_kings_kingdom", 11),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_12"),
            (eq, "$kaos_kings_kingdom", 12),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_13"),
            (eq, "$kaos_kings_kingdom", 13),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_14"),
            (eq, "$kaos_kings_kingdom", 14),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_15"),
            (eq, "$kaos_kings_kingdom", 15),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_16"),
            (eq, "$kaos_kings_kingdom", 16),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_17"),
            (eq, "$kaos_kings_kingdom", 17),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_18"),
            (eq, "$kaos_kings_kingdom", 18),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_19"),
            (eq, "$kaos_kings_kingdom", 19),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_20"),
            (eq, "$kaos_kings_kingdom", 20),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_papacy"),
            (eq, "$kaos_kings_kingdom", 21),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_22"),
            (eq, "$kaos_kings_kingdom", 22),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_23"),
            (eq, "$kaos_kings_kingdom", 23),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_24"),
            (eq, "$kaos_kings_kingdom", 24),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_25"),
            (eq, "$kaos_kings_kingdom", 25),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_26"),
            (eq, "$kaos_kings_kingdom", 26),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_27"),
            (eq, "$kaos_kings_kingdom", 27),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_28"),
            (eq, "$kaos_kings_kingdom", 28),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_29"),
            (eq, "$kaos_kings_kingdom", 29),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_30"),
            (eq, "$kaos_kings_kingdom", 30),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_31"),
            (eq, "$kaos_kings_kingdom", 31),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_32"),
            (eq, "$kaos_kings_kingdom", 32),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_33"),
            (eq, "$kaos_kings_kingdom", 33),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_34"),
            (eq, "$kaos_kings_kingdom", 34),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_35"),
            (eq, "$kaos_kings_kingdom", 35),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_36"),
            (eq, "$kaos_kings_kingdom", 36),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_37"),
            (eq, "$kaos_kings_kingdom", 37),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_38"),
            (eq, "$kaos_kings_kingdom", 38),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_39"),
            (eq, "$kaos_kings_kingdom", 39),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_40"),
            (eq, "$kaos_kings_kingdom", 40),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_41"),
            (eq, "$kaos_kings_kingdom", 41),
            (assign, ":continue", 0),
          (else_try),
            (eq, ":original_faction", "fac_kingdom_42"),
            (eq, "$kaos_kings_kingdom", 42),
            (assign, ":continue", 0),
          (try_end),
        (else_try),
          (is_between, ":original_faction", "fac_player_supporters_faction", "fac_kingdoms_end"),
          (assign, ":continue", 1),
        (try_end),
        (try_begin),
          (eq, ":continue", 1),
          ###################### bugfix
          (store_faction_of_troop, ":faction_no2", ":cur_troop"),
          (neq, ":faction_no2", "fac_player_supporters_faction"),
          ###################
          (store_faction_of_troop, ":faction_no", ":cur_troop"),
          (neq, ":faction_no", ":original_faction"),
          (assign, ":num_walled_centers", 0),
          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":walled_center", slot_town_lord, ":cur_troop"),
            (val_add, ":num_walled_centers", 1),
          (try_end),
          (gt, ":num_walled_centers", 0),
          (store_sub, ":original_king", ":original_faction", fac_kingdom_1),
          (val_add, ":original_king", "trp_kingdom_1_lord"),
          (faction_set_slot, ":original_faction", slot_faction_leader, ":original_king"),
          (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
          (try_for_range, ":cur_troop", "trp_npc1", "trp_knight_1_1_wife"),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (neg|is_between, ":cur_troop", "trp_npc29", "trp_knight_1_1"),
            (neq, ":cur_troop", ":cur_troop"),
            (troop_get_slot, ":original_faction_2", ":cur_troop", slot_troop_original_faction),
            (store_faction_of_troop, ":faction_no", ":cur_troop"),
            (eq, ":original_faction_2", ":original_faction"),
            (neq, ":faction_no", ":original_faction"),
            (troop_set_slot, ":cur_troop", slot_troop_change_to_faction, ":original_faction"),
          (try_end),
          (call_script, "script_add_notification_menu", "mnu_notification_kingdom_restoration", ":cur_troop", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
  ]),
 
 
 
 
 
####################################### TRIGGER THAT CHECKS RATE OF NEW MENU OPTIONS  
(2,
[
############################### CENTER REINFORCEMENT RATE
 (val_add, "$g_party_garrison_reinforcement_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_garrison_reinforcement_rate_hours_passed", "$g_party_garrison_reinforcement_rate"),
     (assign, "$g_party_garrison_reinforcement_rate_hours_passed", 0),
     #######set player lost controled centers to auto recruitmen type
     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
         (party_set_slot, ":center_no", slot_garrison_control, town_controled),
     (try_end),
      
     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       ######(neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), ######center does not belong to player.#tom
       (party_slot_ge, ":center_no", slot_town_lord, 0), ######center belongs to someone. 
       (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), ######center not under siege
       (party_slot_eq, ":center_no", slot_garrison_control, town_controled), ######auto recruitment
   
       ######(store_faction_of_party, ":faction", ":center_no"),
       (assign, ":party_top_size", "$g_party_garrison_max_size_castles"), ######castles
       (try_begin),
         (is_between, ":center_no", towns_begin, towns_end),
         (assign, ":party_top_size", "$g_party_garrison_max_size_towns"),
       (try_end),
       (party_get_num_companions, ":party_size", ":center_no"),
       
       (try_begin),
         (lt, ":party_size", ":party_top_size"),
         (call_script, "script_cf_reinforce_party", ":center_no"),
       (try_end),
     (try_end),
 (try_end),
   
   
   
 
 ################################## LORD REINFORCEMENT RATE
 (val_add, "$g_party_npc_reinforcement_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_npc_reinforcement_rate_hours_passed", "$g_party_npc_reinforcement_rate"),
     (assign, "$g_party_npc_reinforcement_rate_hours_passed", 0),
     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ####### he's alive/active
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
       (ge, ":party_no", 1),
       (party_is_active, ":party_no"),
       (party_get_attached_to, ":cur_attached_party", ":party_no"),
       (is_between, ":cur_attached_party", centers_begin, centers_end),
       (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), ######center not under siege
         (store_faction_of_party, ":party_faction", ":party_no"),
         
       (try_begin),
         (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
         (eq, ":party_faction", "$players_kingdom"),
           (assign, ":num_hiring_rounds", 1),
           (store_random_in_range, ":random_value", 1, 1),
           (val_add, ":num_hiring_rounds", ":random_value"),
       (else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (try_begin),
           (eq, ":reduce_campaign_ai", 0), ######hard (2x reinforcing)
             (assign, ":num_hiring_rounds", 1),
         (else_try),
           (eq, ":reduce_campaign_ai", 1), ######medium (1x or 2x reinforcing)
             (assign, ":num_hiring_rounds", 1),
           ######(store_random_in_range, ":random_value", 0, 2),
           ######(val_add, ":num_hiring_rounds", ":random_value"),
         (else_try),
           (eq, ":reduce_campaign_ai", 2), ######easy (1x reinforcing)
             (assign, ":num_hiring_rounds", 1),
         (try_end),
       (try_end),
     
     (try_begin),
       (faction_slot_eq,  ":party_faction", slot_faction_marshall, ":troop_no"),
         (val_add, ":num_hiring_rounds", 1),
     (try_end),
     
     (try_for_range, ":unused", 0, ":num_hiring_rounds"),
       (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"), ######Hiring men with current wealth
     (try_end),
     
    (try_end),
 (try_end),     
 
 
 ################################## LANCE REFILL RATE 
 (val_add, "$g_party_player_reinforcement_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_player_reinforcement_rate_hours_passed", "$g_party_player_reinforcement_rate"),
     (assign, "$g_party_player_reinforcement_rate_hours_passed", 0),
     (try_for_range, ":village_no", towns_begin, towns_end),
       (call_script, "script_feudal_lance_manpower_update", ":village_no", "$g_party_lances_max_town"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
     (try_end),
     
     (try_for_range, ":village_no", villages_begin, villages_end),
       (call_script, "script_feudal_lance_manpower_update", ":village_no", "$g_party_lances_max_village"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
     (try_end),
     
     (try_for_range, ":village_no", castles_begin, castles_end),
       (call_script, "script_feudal_lance_manpower_update", ":village_no", "$g_party_lances_max_castle"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
     (try_end),
 (try_end),    
 
 
   
 ################################## TOWN MERC REFILL RATE
 (val_add, "$g_party_town_merc_refill_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_town_merc_refill_rate_hours_passed", "$g_party_town_merc_refill_rate"),
     (assign, "$g_party_town_merc_refill_rate_hours_passed", 0),
     (try_begin),
       (call_script, "script_town_merc_respawn"),
     (try_end),  
 (try_end),    
 
 
 
 
 
 ################################## KINGDOM FACTION REINFORCEMENT RATE
 (val_add, "$g_party_faction_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_faction_respawn_rate_hours_passed", "$g_party_faction_respawn_rate"),
     (assign, "$g_party_faction_respawn_rate_hours_passed", 0),
     (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
       (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_foragers", 0), ################# NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_foragers"),
            (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
       (try_end),
         
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_scouts", 0), ################# NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_foragers"),
            (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
       (try_end),
       
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_patrols", 0), ################# NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_patrols"), ######tom was 10
            (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
       (try_end),
       
       ######### (try_begin),
         ######### (store_random_in_range, ":random_no", 0, 100),
         ######### (lt, ":random_no", 10),
         ######### (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
       ######### (try_end),
      
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_caravans", 0),  ################# NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_caravans"),
            (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
       (try_end),
      
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_prisoner_trains", 0), ################# NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_prisoner_trains"),
             (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
       (try_end),
       
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_war_parties", 0), ################# NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_war_parties"),
             (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_war_party),
       (try_end),
       
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_mercenary_companies", 0), ################# NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_mercenary_companies"),
             (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_mercenary_company),
       (try_end),
       
     (try_end),    
 (try_end),    
 
 
 
   
   
 ################################## NON KINGDOM FACTION REINFORCEMENT RATE
 (val_add, "$g_party_bandit_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_bandit_respawn_rate_hours_passed", "$g_party_bandit_respawn_rate"),
     (assign, "$g_party_bandit_respawn_rate_hours_passed", 0),
     ######(call_script, "script_spawn_bandit_lairs"),#tom
     ######### rafi
     ######### (try_begin),
     (call_script, "script_spawn_balts"),
     (call_script, "script_spawn_bandits"),
     (call_script, "script_cf_spawn_crusaders_and_jihadists"),
     ######### (try_end),  
 (try_end),    
 
 
 
 
   
   
 ################################## ROGUE MERCS RESPAWN RATE
 (val_add, "$g_party_mercenary_company_spawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_mercenary_company_spawn_rate_hours_passed", "$g_party_mercenary_company_spawn_rate"),
     (assign, "$g_party_mercenary_company_spawn_rate_hours_passed", 0),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", "$g_party_mercenary_company_spawn_chance"),
         (call_script, "script_spawn_rogue_mercenaries"),
     (try_end),
 (try_end),    
 
 
   
   
 ################################## REBELLIONS RESPAWN RATE    
 (val_add, "$g_party_rebellion_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_rebellion_respawn_rate_hours_passed", "$g_party_rebellion_respawn_rate"),
     (assign, "$g_party_rebellion_respawn_rate_hours_passed", 0),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", "$g_party_rebellion_chance"),
         (call_script, "script_spawn_peasant_rebels"),
     (try_end),
 (try_end),    
 
 
   
 ################################## WELL EQUIPPED REBELLIONS RESPAWN RATE 
 (val_add, "$g_party_rebellion_strong_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_rebellion_strong_respawn_rate_hours_passed", "$g_party_rebellion_strong_respawn_rate"),
     (assign, "$g_party_rebellion_strong_respawn_rate_hours_passed", 0),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", "$g_party_rebellion_strong_chance"),
         (call_script, "script_spawn_rebels"),
     (try_end),
 (try_end),    
 
 
 
   
   
 ################################## FUGITIVE SERF SPAWN RATE 
 (val_add, "$g_party_fugitive_serf_hours_passed", 2),
 (try_begin),
   (ge, "$g_party_fugitive_serf_hours_passed", "$g_party_fugitive_serf_respawn_rate"),
     (assign, "$g_party_fugitive_serf_hours_passed", 0),
     (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
       (lt, ":random_no", "$g_party_fugitive_serf_chance"),
         (call_script, "script_spawn_fugitive_serfs"),
     (try_end),
 (try_end),
 
 
   
 ################################## TOWN MERCHANT RESPAWN RATE  
 (val_add, "$g_misc_merchant_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_misc_merchant_respawn_rate_hours_passed", "$g_misc_merchant_respawn_rate"),
     (assign, "$g_misc_merchant_respawn_rate_hours_passed", 0),
     (try_begin),
       (call_script, "script_refresh_center_inventories"),
       (call_script, "script_refresh_center_armories"),
       (call_script, "script_refresh_center_weaponsmiths"),
       (call_script, "script_refresh_center_stables"),
     (try_end),
 (try_end),    
 
 
 
 
   
   
   
 ################################## TAVERN MERCENARY RESPAWN RATE
 (val_add, "$g_misc_mercenary_respawn_rate_hours_passed", 2),
 (try_begin),
   (ge, "$g_misc_mercenary_respawn_rate_hours_passed", "$g_misc_tavern_mercenaries_respawn_rate"),
     (assign, "$g_misc_mercenary_respawn_rate_hours_passed", 0),
       (call_script, "script_update_mercenary_units_of_towns"),
 (try_end),    
 
   
   
 ################################## LORD RANDOM BUILD
  ###### (val_add, "$g_misc_lord_random_build_hours_passed", 4),
    ###### (try_begin),
      ###### (ge, "$g_misc_lord_random_build_hours_passed", "$g_misc_lord_random_build"),
        ###### (assign, "$g_misc_lord_random_build_hours_passed", 0),
        ###### (call_script, "script_lord_random_build_script"),
    ###### (try_end),   
    
 
 
]),
#################################################################################


  
  
############################# Sending troops from your party to any walled fief you own by Leonion https://forums.taleworlds.com/index.php?topic=348796.0]
(2,
[
 (try_begin),
   (gt, "$send_troops_tweak", 0),
   (party_is_active, "$send_troops_tweak"),
     (get_party_ai_object, ":target_fief", "$send_troops_tweak"),
     (party_is_in_town, "$send_troops_tweak", ":target_fief"),
       (party_get_slot, ":fief_lord", ":target_fief", slot_town_lord),
       (eq, ":fief_lord", "trp_player"),
         (party_get_num_companion_stacks, ":party_stacks", "$send_troops_tweak"),
         (try_for_range, ":current_stack", 0, ":party_stacks"),
           (party_stack_get_size, ":current_stack_size", "$send_troops_tweak", ":current_stack"),
           (party_stack_get_troop_id, ":current_stack_troop_id", "$send_troops_tweak", ":current_stack"),
           (party_add_members, ":target_fief", ":current_stack_troop_id", ":current_stack_size"),
         (try_end),
         (remove_party, "$send_troops_tweak"),
         (assign, "$send_troops_tweak", 0),
 (else_try),
   (neg|party_is_active, "$send_troops_tweak"),
   ######### (neg|133, "$send_troops_tweak"),
     (assign, "$send_troops_tweak", 0),
 (try_end),
]),
##############################################################################


  
############################# New v1.8 
 ###### (12,
   ###### [
  ######### (call_script, "script_add_tavern_troops"),
 ###### ]),  
##############################################################################


############################# NEW v2.1 - FROM VIKING CONQUEST
    ###### Create Deserters when there are more prisoners than troops @Mike
    ###### (36,
      ###### [
        ###### (try_for_parties, ":party_no"),
          ###### (party_get_template_id, ":party_template", ":party_no"),
          ###### (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          ###### (this_or_next|is_between, ":party_template", "pt_looters", "pt_kidnapped_girl"),
          ###### (eq, ":party_template", "pt_village_farmers"),
          ###### (store_party_size_wo_prisoners, ":party_count", ":party_no"),
          ###### (party_get_num_prisoners , ":prisoners_count", ":party_no"),
          ###### (gt, ":prisoners_count", 0),
          ###### (store_sub, ":prisoners_excess", ":prisoners_count", ":party_count"),
          ###### (try_begin),
            ###### (assign, ":check", 4),
          ###### (try_end),
          ###### (gt, ":prisoners_excess", ":check"),
          ###### (try_begin),
            ###### (party_clear, "p_temp_party"),
            ###### (party_clear, "p_temp_party_2"),
            ###### (party_get_num_prisoner_stacks, ":prisoner_stacks", ":party_no"),
            ###### (try_for_range_backwards, ":prisoner_stack_no", 0, ":prisoner_stacks"),
              ###### (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":party_no", ":prisoner_stack_no"),
              ###### (neg|troop_is_hero, ":prisoner_troop_no"),
              ###### (party_prisoner_stack_get_size, ":prisoner_stack_size", ":party_no", ":prisoner_stack_no"),
              ###### (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party"),
              ###### (try_begin),
                ###### (le, ":new_party_count", ":prisoners_count"),
                ###### (party_add_members, "p_temp_party", ":prisoner_troop_no", ":prisoner_stack_size"),
                ###### (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
              ###### (else_try),
                ###### (party_add_members, "p_temp_party_2", ":prisoner_troop_no", ":prisoner_stack_size"),
                ###### (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
              ###### (try_end),
            ###### (try_end),
            ###### (set_spawn_radius, 4),
            ###### (try_begin),
              ###### (spawn_around_party, ":party_no", "pt_deserters"),
            ###### (try_end),
            ###### (assign, ":new_party", reg(0)),
            ###### (call_script, "script_party_add_party", ":new_party", "p_temp_party"),
            ###### (party_set_faction, ":new_party", "fac_deserters"),
            ###### (party_get_position, pos0,  ":new_party"),
            ###### (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
            ###### (party_set_ai_patrol_radius, ":new_party", 40),
            ###### (party_set_ai_target_position, ":new_party", pos0),
            ###### (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
            
            ###### (try_begin),
              ###### (store_party_size_wo_prisoners, ":new_party_count", "p_temp_party_2"),
              ###### (gt,  ":new_party_count", 0),
              ###### (set_spawn_radius, 4),
              ###### (try_begin),
                ###### (spawn_around_party, ":party_no", "pt_deserters"),
              ###### (try_end),
              ###### (assign, ":new_party", reg(0)),
              ###### (call_script, "script_party_add_party", ":new_party", "p_temp_party_2"),
              ###### (party_set_faction, ":new_party", "fac_deserters"),
              ###### (party_get_position, pos0,  ":new_party"),
              ###### (party_set_ai_behavior, ":new_party", ai_bhvr_patrol_location),
              ###### (party_set_ai_patrol_radius, ":new_party", 40),
              ###### (party_set_ai_target_position, ":new_party", pos0),
              ###### (store_party_size_wo_prisoners, ":party_count1", ":new_party"),
            ###### (try_end),
          ###### (try_end),
        ###### (try_end),
    ###### ]),
#######################################################################################



##################################### NEW v2.1 - prisoners escaped from walled fiefs
(0.54,   ###################### roughly once every week for each of the 311 walled centers
[
 (try_begin),
   (lt, "$g_prisoners_escape_cur_center", walled_centers_begin), 
     (assign, "$g_prisoners_escape_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_prisoners_escape_cur_center", walled_centers_end), 
     (assign, "$g_prisoners_escape_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   ###### (neg|party_slot_eq, "$g_prisoners_escape_cur_center", slot_town_lord, "trp_player"),
   (neg|party_slot_eq, "$g_prisoners_escape_cur_center", slot_town_lord, -1),
   (party_get_num_prisoner_stacks, ":prisoner_stack_num", "$g_prisoners_escape_cur_center"),
   (party_get_num_prisoners, ":prisoner_num", "$g_prisoners_escape_cur_center"),
   (try_begin),
     (ge, ":prisoner_num", 400),
     (store_div, ":var3", ":prisoner_num", 100),
     (store_random_in_range, ":random", 0, 100),
     (le, ":random", ":var3"),
     (set_spawn_radius, 2),
     (spawn_around_party, "$g_prisoners_escape_cur_center", "pt_escaped_prisoners_party"),
     (assign, ":spawned_party", reg0),
     (party_clear, ":spawned_party"),
     (party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_location),
     (party_set_aggressiveness, ":spawned_party", 12),
     (try_for_range_backwards, ":cur_prisoner_stack", 0, ":prisoner_stack_num"),
       (party_prisoner_stack_get_troop_id, ":prisoner_troop_id", "$g_prisoners_escape_cur_center", ":cur_prisoner_stack"),
       (neg|troop_is_hero, ":prisoner_troop_id"),
       (party_prisoner_stack_get_size, ":prisoner_stack_size", "$g_prisoners_escape_cur_center", ":cur_prisoner_stack"),
       (party_add_members, ":spawned_party", ":prisoner_troop_id", ":prisoner_stack_size"),
       (party_remove_prisoners, "$g_prisoners_escape_cur_center", ":prisoner_troop_id", ":prisoner_stack_size"),
     (try_end),
     (str_store_party_name_link, s4, "$g_prisoners_escape_cur_center"),
     (display_message, "@There was a massive prisoner break from {s4}!"),
   (try_end),
 (try_end),
 
 ################ proceed to the next center
 (val_add, "$g_prisoners_escape_cur_center", 1),
]),
#######################################################################################



  
######################### New v2.1 - LORD ASSASSINATION ATTEMPTS
(0.084,   ############################# roughly once every 3 days for each of the 858 lords
[
 (try_begin),
   (lt, "$g_assassination_attempt_cur_npc", active_npcs_begin), 
     (assign, "$g_assassination_attempt_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_assassination_attempt_cur_npc", active_npcs_end), 
     (assign, "$g_assassination_attempt_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),   
   (troop_slot_eq, "$g_assassination_attempt_cur_npc", slot_troop_is_alive, 1),
   (troop_slot_eq, "$g_assassination_attempt_cur_npc", slot_troop_occupation, slto_kingdom_hero),
   (store_faction_of_troop, ":troop_faction", "$g_assassination_attempt_cur_npc"),
   (try_begin),
     (call_script, "script_cf_troop_get_random_enemy_lord", "$g_assassination_attempt_cur_npc"),
     (gt, reg0, 0), 
       (assign, ":enemy_lord", reg0),
         (neg|faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_assassination_attempt_cur_npc"),
         (call_script, "script_rand", 0, 1000),
         (lt, reg0, "$g_lord_death_chance_assassination"), ############ Lord chance
           (call_script, "script_rand", 0, 100),
           (try_begin),
             (lt, reg0, 35), ############ 35% chance of discovery
               (call_script, "script_kill_lord_assassination", "$g_assassination_attempt_cur_npc", 1, ":enemy_lord"),
           (else_try),
             (call_script, "script_kill_lord_assassination", "$g_assassination_attempt_cur_npc", 0, 0),
           (try_end),
   (else_try),
     (call_script, "script_cf_troop_get_random_enemy_lord", "$g_assassination_attempt_cur_npc"),
     (gt, reg0, 0), 
       (assign, ":enemy_lord", reg0),
       (faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_assassination_attempt_cur_npc"),
       (call_script, "script_rand", 0, 1000),
       (lt, reg0, "$g_lord_death_chance_assassination_king"),  ############ King chance
         (call_script, "script_rand", 0, 100),
         (try_begin),
           (lt, reg0, 60), ############ 60% chance of discovery
             (call_script, "script_kill_lord_assassination", "$g_assassination_attempt_cur_npc", 1, ":enemy_lord"),
         (else_try),
           (call_script, "script_kill_lord_assassination", "$g_assassination_attempt_cur_npc", 0, 0),
         (try_end),
   (try_end),
 (try_end),
 ################# proceed to the next npc
 (val_add, "$g_assassination_attempt_cur_npc", 1),
]),
####################################################



  
############################# New v2.1 - LORD EXECUTION CHANCE
# (0.54,   ###################### roughly once a week for each of the 311 walled centers
(0.23,   ###################### roughly once every 3 days for each of the 311 walled centers
[
 (try_begin),
   (lt, "$g_execute_lord_cur_center", walled_centers_begin), 
     (assign, "$g_execute_lord_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_execute_lord_cur_center", walled_centers_end), 
     (assign, "$g_execute_lord_cur_center", walled_centers_begin),
 (try_end),
 
 (try_begin),  
   (neq, "$g_lord_death_chance_execution_base", 0), ############### must be greater than this
   (neg|party_slot_eq, "$g_execute_lord_cur_center", slot_town_lord, -1),
   (party_get_num_prisoner_stacks, ":prisoner_stack_num", "$g_execute_lord_cur_center"),
   (try_for_range_backwards, ":cur_prisoner_stack", 0, ":prisoner_stack_num"),
     (party_prisoner_stack_get_troop_id, ":prisoner_troop_id", "$g_execute_lord_cur_center", ":cur_prisoner_stack"),
     (troop_is_hero, ":prisoner_troop_id"), ######### found a lord to execute
       (store_troop_faction, ":prisoner_faction", ":prisoner_troop_id"), ######## gets faction relations - the lower the greater the chance of execution
       (store_faction_of_party, ":center_faction", "$g_execute_lord_cur_center"), 
       (store_relation, ":faction_relation", ":center_faction", ":prisoner_faction"),
       (store_mul, ":chance_of_execution", ":faction_relation", "$g_lord_death_chance_execution_relation_divider"), ######### every 3 minus points increase chance by 1%
       (val_add, ":chance_of_execution", "$g_lord_death_chance_execution_base"), ######### 10% base chance
       
       (troop_get_slot, ":reputation", ":prisoner_troop_id", slot_lord_reputation_type), 
       (try_begin),   ######### asshole lords have a greater chance of going to the block - martial is neutral
         (this_or_next|eq, ":reputation", lrep_quarrelsome),
         (eq, ":reputation", lrep_debauched),  
           (val_add, ":chance_of_execution", 20),  
       (else_try),              
         (eq, ":reputation", lrep_selfrighteous),  
           (val_add, ":chance_of_execution", 13),  
       (else_try),              
         (eq, ":reputation", lrep_cunning),  
           (val_add, ":chance_of_execution", 8),  
       (else_try),              
         (eq, ":reputation", lrep_upstanding),  
           (val_sub, ":chance_of_execution", 5),  
       (else_try),              
         (eq, ":reputation", lrep_goodnatured),  
           (val_sub, ":chance_of_execution", 10),  
       (try_end),  
       
       (try_begin),   ######### kings have different chance
         (val_add, ":chance_of_execution", "$g_lord_death_chance_execution_king_variation"),  
       (try_end),  
       
       (try_begin),
         (call_script, "script_rand", 0, 100),
         (lt, reg0, ":chance_of_execution"),
         (try_begin),   ######### Now determine method of execution
           (lt, ":chance_of_execution", 30),  
             (assign, ":execution_method", 1),  ########### beheading
         (else_try),              
           (ge, ":chance_of_execution", 30),  
           (lt, ":chance_of_execution", 50),  
             (assign, ":execution_method", 2),  ########### hanging
         (else_try),              
           (ge, ":chance_of_execution", 50),  
           (lt, ":chance_of_execution", 80),  
             (assign, ":execution_method", 3),  ########### Burning
         (else_try),              
           (ge, ":chance_of_execution", 80),  
             (assign, ":execution_method", 4),  ########### Hung, Strung and Quartered
         (try_end),  
 
         (party_get_slot, ":town_lord", "$g_execute_lord_cur_center", slot_town_lord),
         (call_script, "script_kill_lord_execution", ":town_lord", ":prisoner_troop_id", "$g_execute_lord_cur_center", ":execution_method"),            
      (try_end),  
 
   (try_end),
 (try_end),
 
 ################ proceed to the next npc
 (val_add, "$g_execute_lord_cur_center", 1),
]),
##############################################################################


  
############################# New v2.1 - LORD EXECUTION BY PLAYER
(72,   
[
 (try_begin),
   (eq, "$g_execution_scheduled", 1),  
     (troop_get_slot, ":cur_prison", "$lord_to_execute", slot_troop_prisoner_of_party),
     (eq, ":cur_prison", "$g_execution_center"), ######## must check that he's still there
       (call_script, "script_kill_lord_execution", "trp_player", "$lord_to_execute", "$g_execution_center", "$g_method_of_execution"),
 (else_try),
   (eq, "$g_execution_scheduled", 1),  
     (troop_get_slot, ":cur_prison", "$lord_to_execute", slot_troop_prisoner_of_party),
     (neq, ":cur_prison", "$g_execution_center"), ######## not there, display notification
      (call_script, "script_add_notification_menu", "mnu_lord_executed_by_player_escaped", "$lord_to_execute", "$g_execution_center", "$g_method_of_execution"),
 (try_end),
]),
##############################################################################


  
############################# New v2.1 - LORD ASSASSINATION BY PLAYER
(168,   
[
 (try_begin),
   (eq, "$g_assassination_scheduled", 1),  
   (troop_slot_eq, "$lord_to_assassinate", slot_troop_is_alive, 1),
     (store_faction_of_troop, ":troop_faction", "$lord_to_assassinate"),
     (call_script, "script_rand", 0, 100),
     (try_begin),
       (neg|faction_slot_eq, ":troop_faction", slot_faction_leader, "$lord_to_assassinate"),
       (lt, reg0, 40), ######## 40%
         (call_script, "script_rand", 0, 100),
         (try_begin),
           (lt, reg0, 35), ######## 35% chance of discovery
           (call_script, "script_kill_lord_assassination", "$lord_to_assassinate", 1, "trp_player"),
           (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_suceeded", "$lord_to_assassinate"),
         (else_try),
           (call_script, "script_kill_lord_assassination", "$lord_to_assassinate", 0, "trp_player"),
           (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_suceeded", "$lord_to_assassinate"),
         (try_end),
     (else_try),
       (faction_slot_eq, ":troop_faction", slot_faction_leader, "$lord_to_assassinate"),
       (lt, reg0, 20), ######## 20% chance for kings
         (call_script, "script_rand", 0, 100),
         (try_begin),
           (lt, reg0, 60), ######## 60% chance of discovery
           (call_script, "script_kill_lord_assassination", "$lord_to_assassinate", 1, "trp_player"),
           (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_suceeded", "$lord_to_assassinate"),
         (else_try),
           (call_script, "script_kill_lord_assassination", "$lord_to_assassinate", 0, "trp_player"),
           (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_suceeded", "$lord_to_assassinate"),
         (try_end),
     (try_end),
 (else_try), 
   (eq, "$g_assassination_scheduled", 1),  
     (troop_slot_eq, "$lord_to_assassinate", slot_troop_is_alive, 1), ######## assassination failed
       (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_failed", "$lord_to_assassinate"),
 (else_try), 
   (eq, "$g_assassination_scheduled", 1),  
     (troop_slot_eq, "$lord_to_assassinate", slot_troop_is_alive, 0), ######## died before assassination attempt
       (call_script, "script_add_notification_menu", "mnu_lord_assassination_by_player_died_before", "$lord_to_assassinate"),
 (try_end),
]),
##############################################################################


          
          
############################### NEW v2.1 - RATE WHICH FACTIONS START WARS AND MAKE PEACE
(0.3,         
[ 
 (val_add, "$g_misc_diplomacy_rate_hours_passed", 0.3*100), ######### trigger rate x 100 for rounding values
 (try_begin),
   (store_mul, ":diplomacy_rate", "$g_misc_faction_diplomacy_rate", 100),  ######### simulates a float number 
   (val_div, ":diplomacy_rate", 73),  ######### 43 factions
   (ge, "$g_misc_diplomacy_rate_hours_passed", ":diplomacy_rate"),
     (assign, "$g_misc_diplomacy_rate_hours_passed", 0),
     (call_script, "script_randomly_start_war_peace_new", 1),
     (store_sub, ":kingdoms_end", kingdoms_end, 1),
     (try_begin),
       (ge, "$g_diplo_kingdom", ":kingdoms_end"),
       (try_begin),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (eq, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
         (assign, "$g_diplo_kingdom", "fac_player_supporters_faction"),
       (else_try),
         ######(assign, "$g_diplo_kingdom", "fac_kingdom_1"),
         (assign, "$g_diplo_kingdom", npc_kingdoms_begin),
       (try_end),
     (else_try),
       (val_add, "$g_diplo_kingdom", 1),
     (try_end),      
 (try_end),
]),
##############################################################


  
############################# New v2.1 - LORD GENERATION
(0.2,   
[
 (gt, "$g_lord_creation_rate", 0),  ######### if set to 0 don't create any
 (val_add, "$g_misc_lord_creation_rate_hours_passed", 0.2*100), ######### trigger rate x 100 for rounding values
 (try_begin),
   (store_mul, ":creation_rate", "$g_lord_creation_rate", 100),  ######### simulates a float number 
   (val_div, ":creation_rate", 73),  ######### 43 original factions but it depends if civil war exist or not
   (ge, "$g_misc_lord_creation_rate_hours_passed", ":creation_rate"),
     (assign, "$g_misc_lord_creation_rate_hours_passed", 0),
     (try_begin),
       (lt, "$g_misc_lord_generation_cur_faction", kingdoms_begin), 
         (assign, "$g_misc_lord_generation_cur_faction", kingdoms_begin),
     (try_end),
     
     (try_begin),
       (ge, "$g_misc_lord_generation_cur_faction", kingdoms_end), 
         (assign, "$g_misc_lord_generation_cur_faction", kingdoms_begin),
     (try_end),
     
     (try_begin),
       # (str_store_faction_name, s1, "$g_misc_lord_generation_cur_faction"),
       (faction_slot_eq, "$g_misc_lord_generation_cur_faction", slot_faction_state, sfs_active),
         # (display_message, "@script_check_faction_lord_threshold called for {s1}!"),
         (call_script, "script_check_faction_lord_threshold", "$g_misc_lord_generation_cur_faction"),
         (eq, reg0, 1),
           # (display_message, "@script_create_new_lord_for_faction called for {s1}!"),
           (call_script, "script_create_new_lord_for_faction", "$g_misc_lord_generation_cur_faction"),
     (try_end),
     ################ proceed to the next faction
     (val_add, "$g_misc_lord_generation_cur_faction", 1),
 (try_end),
]),
##############################################################################

  
############################# New v2.1 - FIEF CULTURE CHANGES TO LORD'S CULTURE
# (0.98,   ###################### roughly once every month for each of the 733 centers
(720,   
[
 # (try_begin),
   # (lt, "$g_change_culture_cur_center", centers_begin), 
   # (assign, "$g_change_culture_cur_center", centers_begin),
 # (try_end),
 
 # (try_begin),
   # (ge, "$g_change_culture_cur_center", centers_end), 
   # (assign, "$g_change_culture_cur_center", centers_begin),
 # (try_end),
 
 # (try_begin),
   # (neg|party_slot_eq, "$g_change_culture_cur_center", slot_town_lord, -1),
   # (neg|party_slot_eq, "$g_change_culture_cur_center", slot_town_lord, "trp_player"),
     # (party_get_slot, ":center_lord", "$g_change_culture_cur_center", slot_town_lord),
     # (troop_get_slot, ":center_lord_culture", ":center_lord", slot_troop_cur_culture),
     # (party_set_slot, "$g_change_culture_cur_center", slot_center_culture, ":center_lord_culture"),
 # (try_end),
 
 ################ proceed to the next center
 # (val_add, "$g_change_culture_cur_center", 1),
]),
#######################################################################################



############################ NEW v2.1 - gives prosperity to villages the player has invested on
(0.056, ###################### roughly once every day for each of the 423 villages
[
 (try_begin),
   (lt, "$g_donation_changes_cur_village", villages_begin), 
   (assign, "$g_donation_changes_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_donation_changes_cur_village", villages_end), 
   (assign, "$g_donation_changes_cur_village", villages_begin),
 (try_end),
  
 (try_begin),
   (party_slot_ge, "$g_donation_changes_cur_village", slot_center_donations, 1),
     (call_script, "script_rand", 200, 501),
     (assign, ":random", reg0),  ######### just in case
     (party_get_slot, ":cur_donation_amount", "$g_donation_changes_cur_village", slot_center_donations),
     (val_min, ":random", ":cur_donation_amount"),
     (store_div, ":prosperity_change", ":random", 100),
     (call_script, "script_change_center_prosperity", "$g_donation_changes_cur_village", ":prosperity_change"),
     (val_sub, ":cur_donation_amount", ":random"),
     (party_set_slot, "$g_donation_changes_cur_village", slot_center_donations, ":cur_donation_amount"),
     (try_begin),
       (eq, "$cheat_menu", 1),
         (assign, reg4, ":prosperity_change"),
         (assign, reg5, ":cur_donation_amount"),
         (str_store_party_name, s3, "$g_donation_changes_cur_village"),
         (display_message, "@{s3} gained {reg4} prosperity. {reg5} money left."),
     (try_end),
 (try_end),
 
 ################ proceed to the next village
 (val_add, "$g_donation_changes_cur_village", 1),
]),
#######################################################################################




############################## NEW v2.1 - Patrols drop prisoners into a walled fief
(48,
[
 (try_begin),
   (eq, "$g_misc_parties_drop_prisoners_to_walled_fief", 1),
   (try_for_parties, ":party"),
     (party_is_active, ":party"),
     (neg|party_slot_eq, ":party", slot_party_type, spt_kingdom_hero_party),
     (party_get_template_id, ":party_template", ":party"),
     (this_or_next|eq, ":party_template", "pt_forager_party"),
     (this_or_next|eq, ":party_template", "pt_scout_party"),
     (this_or_next|eq, ":party_template", "pt_patrol_party"),
     (this_or_next|eq, ":party_template", "pt_war_party"),
     (this_or_next|eq, ":party_template", "pt_mercenary_company"),
     ###### (this_or_next|eq, ":party_template", "pt_mongolian_camp"),
     (this_or_next|eq, ":party_template", "pt_welsh"),
     (this_or_next|eq, ":party_template", "pt_guelphs"),
     (this_or_next|eq, ":party_template", "pt_ghibellines"),
     (this_or_next|eq, ":party_template", "pt_crusaders"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_iberian"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_scandinavian"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_euro"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_italian"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_welsh"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_gaelic"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_teutonic"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_templar"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_hospitaller"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_saint_lazarus"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_santiago"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_calatrava"),
     (this_or_next|eq, ":party_template", "pt_crusader_raiders_saint_thomas"),
     (this_or_next|eq, ":party_template", "pt_jihadist_raiders"),
     (this_or_next|eq, ":party_template", "pt_teutonic_raiders"),
     (this_or_next|eq, ":party_template", "pt_curonians"),
     (this_or_next|eq, ":party_template", "pt_prussians"),
     (this_or_next|eq, ":party_template", "pt_samogitians"),
     (eq, ":party_template", "pt_yotvingians"),
     ###### (party_get_slot, ":var12", ":party", slot_party_home_center),
     (party_get_slot, ":cur_patrol_object", ":party", slot_party_ai_object),
     (try_begin),
       (party_is_in_town, ":party", ":cur_patrol_object"),
       (party_get_num_prisoner_stacks, ":party_prisoner_stacks", ":party"),
       (try_for_range_backwards, ":cur_prisoner_stack", 0, ":party_prisoner_stacks"),
         (party_prisoner_stack_get_troop_id, ":cur_stack_troop_id", ":party", ":cur_prisoner_stack"),
         (party_prisoner_stack_get_size, ":cur_stack_size", ":party", ":cur_prisoner_stack"),
         (party_force_add_prisoners, ":cur_patrol_object", ":cur_stack_troop_id", ":cur_stack_size"),
         (party_remove_prisoners, ":party", ":cur_stack_troop_id", ":cur_stack_size"),
       (try_end),
       (party_set_ai_behavior, ":party", ai_bhvr_patrol_party),
       (party_set_ai_patrol_radius, ":party", 2),
       (party_set_ai_object, ":party", ":cur_patrol_object"),
       (party_set_ai_initiative, ":party", 50),
       (party_set_aggressiveness, ":party", 8),
       (party_set_courage, ":party", 9),
     (else_try),
       (get_party_ai_behavior, ":cur_behavior", ":party"),
       (eq, ":cur_behavior", ai_bhvr_patrol_party),
         (party_get_num_prisoners, ":cur_party_prisoners", ":party"),
         (ge, ":cur_party_prisoners", 50),
           (party_set_ai_behavior, ":party", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party", ":cur_patrol_object"),
     (try_end),
   (try_end),
 (try_end),
]),
#######################################################################################



############################## NEW v2.1 - Civil War
(720,   
[
 (gt, "$g_misc_civil_war_chance", 9999999), ######### if disabled don't do anything
 (val_add, "$g_misc_civil_war_hours_passed", 0.3*100), ######### trigger rate x 100 for rounding values
 (try_begin),
   (store_mul, ":rate", "$g_misc_civil_war_rate", 100),  ######### simulates a float number 
   (val_div, ":rate", 73),  ######### 43 original factions but it depends if civil war exist or not
   (ge, "$g_misc_civil_war_hours_passed", ":rate"),
     (assign, "$g_misc_civil_war_hours_passed", 0),
     (try_begin),
       (lt, "$g_misc_civil_war_cur_faction", kingdoms_begin), 
         (assign, "$g_misc_civil_war_cur_faction", kingdoms_begin),
     (try_end),
     
     (try_begin),
       (ge, "$g_misc_civil_war_cur_faction", kingdoms_end), 
         (assign, "$g_misc_civil_war_cur_faction", kingdoms_begin),
     (try_end),
 
     (try_begin),
       (faction_slot_eq, "$g_misc_civil_war_cur_faction", slot_faction_state, sfs_active),
       (neg|faction_slot_ge, "$g_misc_civil_war_cur_faction", slot_faction_rebel_original_faction, 1),  ############ isn't a rebel faction 
         # (display_message, "@script_check_faction_civil_war_requirements called!"),
         (call_script, "script_check_faction_civil_war_requirements", "$g_misc_civil_war_cur_faction"),
         (eq, reg0, 1),
           (assign, ":upper_bound", reg1),
           (call_script, "script_rand", 0, 100),
           (lt, "$g_misc_civil_war_chance", reg0),
             # (display_message, "@script_initiate_civil_war called!"),
             (call_script, "script_initiate_civil_war", "$g_misc_civil_war_cur_faction", ":upper_bound"),
     (try_end),
     ################ proceed to the next faction
     (val_add, "$g_misc_civil_war_cur_faction", 1),
 (try_end),
]),
#######################################################################################


############################## NEW v2.1 - This runs once every 72 hours to evaluate the amount of factions active
(72,
[  
 (try_begin),
   (assign, "$g_current_factions_active_temp", 0), ######## set it to 0 every time it runs
   (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
     (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
       (val_add, "$g_current_factions_active_temp", 1),
   (try_end),
   (assign, "$g_current_factions_active", "$g_current_factions_active_temp"), 
 (try_end),
]),
#######################################################################################


############################## NEW v2.1 - This runs once every 48 hours to evaluate the amount of lords/npcs alive
# (48,
# [  
 ###### (try_begin),
   ###### (assign, "$g_current_lords_active_temp", 0), ######## set it to 0 every time it runs
   ###### (try_for_range, ":cur_lord", lords_begin, lords_end),
     ###### (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),
       ###### (val_add, "$g_current_lords_active_temp", 1),
   ###### (try_end),
   ###### (assign, "$g_current_lords_active", "$g_current_lords_active_temp"), 
 ###### (try_end),
 
 ###### (try_begin),
   ###### (assign, "$g_current_npcs_active_temp", 0), ######## set it to 0 every time it runs
   ###### (try_for_range, ":cur_lord", active_npcs_begin, active_npcs_end),
     ###### (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),
       ###### (val_add, "$g_current_npcs_active_temp", 1),
   ###### (try_end),
   ###### (assign, "$g_current_npcs_active", "$g_current_npcs_active_temp"), 
 ###### (try_end),
# ]),
#######################################################################################



############################## NEW v2.1 - This runs to check if a rebel faction has defeated its original faction - if yes change its name to the former's name
(48,
[  
 (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
   (try_begin),
     (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),  ######## is still active
     (faction_slot_ge, ":cur_faction", slot_faction_rebel_original_faction, 1),  ######## is a rebel faction that hasn't defeated its original
       (faction_get_slot, ":original_faction", ":cur_faction", slot_faction_rebel_original_faction),
       (neg|faction_slot_eq, ":original_faction", slot_faction_state, sfs_active),
         (str_clear, s1),
         (str_store_faction_name, s1, ":original_faction"),
         (faction_set_name, ":cur_faction", s1),
         (faction_set_slot, ":cur_faction", slot_faction_rebel_original_faction, 0),
   (try_end),
 (try_end),
]),
#######################################################################################


############################## NEW v2.1 - This runs once every 24 hours to count the amount of days a faction has been active
(24,
[  
 (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
     (faction_get_slot, ":days", ":cur_faction", slot_faction_days_active),
     (val_add, ":days", 1),
     (faction_set_slot, ":cur_faction", slot_faction_days_active, ":days"),
 (try_end),
]),
#######################################################################################



################### NEW v1.0 - KINGDOM FACTION REINFORCEMENT RATE
(0.1,
[  
 (val_add, "$g_party_faction_respawn_rate_hours_passed", 0.1*100), ############## trigger rate x 100 for rounding values
 (try_begin),
   (store_mul, ":rate", "$g_party_faction_respawn_rate", 100),  ############## simulates a float number 
   (val_div, ":rate", 73),  ############## 13 original factions but it depends if civil war exist or not
   (ge, "$g_party_faction_respawn_rate_hours_passed", ":rate"),
     (assign, "$g_party_faction_respawn_rate_hours_passed", 0),
     (try_begin),
       (lt, "$g_party_faction_respawn_rate_cur_faction", kingdoms_begin), 
         (assign, "$g_party_faction_respawn_rate_cur_faction", kingdoms_begin),
     (try_end),
     
     (try_begin),
       (ge, "$g_party_faction_respawn_rate_cur_faction", kingdoms_end), 
         (assign, "$g_party_faction_respawn_rate_cur_faction", kingdoms_begin),
     (try_end),
		 
     (try_begin),
       (faction_slot_eq, "$g_party_faction_respawn_rate_cur_faction", slot_faction_state, sfs_active),
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_foragers", 0), ######### NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_foragers"),
            (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_forager),
       (try_end),
         
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_scouts", 0), ######### NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_foragers"),
            (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_scout),
       (try_end),
       
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_patrols", 0), ######### NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_patrols"), ##########tom was 10
            (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_patrol),
       (try_end),
       
       ############ (try_begin),
         ############ (store_random_in_range, ":random_no", 0, 100),
         ############ (lt, ":random_no", 10),
         ############ (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_messenger),
       ############ (try_end),
      
       (try_begin),
        (gt, "$g_party_faction_parties_spawn_chance_caravans", 0),  ######### NEW v1.8
          (call_script, "script_rand", 0, 100),
          (le, reg0, "$g_party_faction_parties_spawn_chance_caravans"),
            (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_kingdom_caravan),
       (try_end),
      
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_prisoner_trains", 0), ######### NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_prisoner_trains"),
             (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_prisoner_train),
       (try_end),
       
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_war_parties", 0), ######### NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_war_parties"),
             (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_war_party),
       (try_end),
       
       (try_begin),
         (gt, "$g_party_faction_parties_spawn_chance_mercenary_companies", 0), ######### NEW v1.8
           (call_script, "script_rand", 0, 100),
           (le, reg0, "$g_party_faction_parties_spawn_chance_mercenary_companies"),
             (call_script, "script_create_kingdom_party_if_below_limit", "$g_party_faction_respawn_rate_cur_faction", spt_mercenary_company),
       (try_end),
       
     (try_end),    
 (try_end),    
]),
##########################################################




############################ NEW v2.1 - mill prosperity
(0.794, ###################### roughly once every two weeks for each of the 423 villages
[
 (try_begin),
   (lt, "$g_mill_prosperity_cur_village", villages_begin), 
   (assign, "$g_mill_prosperity_cur_village", villages_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_mill_prosperity_cur_village", villages_end), 
   (assign, "$g_mill_prosperity_cur_village", villages_begin),
 (try_end),
  
 (try_begin),
   (party_slot_ge, "$g_mill_prosperity_cur_village", slot_center_has_fish_pond, 1),
     (call_script, "script_change_center_prosperity", "$g_mill_prosperity_cur_village", 5),
 (try_end),
 
 ################ proceed to the next village
 (val_add, "$g_mill_prosperity_cur_village", 1),
]),
#######################################################################################



####################### Remove dead lords from notes 
(2.51,   ##### once every 75 days for each of the 858 lords
[
 (try_begin),
   (lt, "$g_remove_from_notes_cur_npc", active_npcs_begin), 
     (assign, "$g_remove_from_notes_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_remove_from_notes_cur_npc", active_npcs_end), 
     (assign, "$g_remove_from_notes_cur_npc", active_npcs_begin),
 (try_end),
 
 (try_begin),   
   (troop_slot_eq, "$g_remove_from_notes_cur_npc", slot_troop_is_alive, 0),  ###### dead
   (troop_slot_eq, "$g_remove_from_notes_cur_npc", slot_troop_occupation, slto_kingdom_hero),
   (troop_set_note_available, "$g_remove_from_notes_cur_npc", 0),  
 (try_end),
 ################# proceed to the next npc
 (val_add, "$g_remove_from_notes_cur_npc", 1),
]),  
##############################################################################



####################### NEW v2.2 - Lords get out of defeated factions ASAP
(0.1958,   ###### once a week for every of the 858 lords
[
 (try_begin),
   (lt, "$g_leave_defeated_faction_cur_lord", lords_begin), 
     (assign, "$g_leave_defeated_faction_cur_lord", lords_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_leave_defeated_faction_cur_lord", lords_end), 
     (assign, "$g_leave_defeated_faction_cur_lord", lords_begin),
 (try_end),
 
 (try_begin),   
   (troop_slot_eq, "$g_leave_defeated_faction_cur_lord", slot_troop_is_alive, 1),  ###### he's alive
   (store_faction_of_troop, ":cur_faction", "$g_leave_defeated_faction_cur_lord"),
   (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_defeated),
     (call_script, "script_lord_find_alternative_faction", "$g_leave_defeated_faction_cur_lord"),
     (assign, ":new_faction", reg0),
     (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
     (neq, ":new_faction", ":cur_faction"),
       (str_store_troop_name_link, s1, "$g_leave_defeated_faction_cur_lord"),
       (str_store_faction_name_link, s2, ":new_faction"),
       (str_store_faction_name_link, s3, ":cur_faction"),
       (call_script, "script_change_troop_faction", "$g_leave_defeated_faction_cur_lord", ":new_faction"),
       (call_script, "script_dplmc_store_troop_is_female", "$g_leave_defeated_faction_cur_lord"),
       (assign, reg4, reg0),
       (str_store_string, s4, "str_ee_lord_defects_ordinary"),
       (display_log_message, "@{!}{s4}"),
       # (try_begin),  
         # (call_script, "script_party_calculate_regular_strength"),
       # (try_end),
 (try_end),
 ################# proceed to the next npc
 (val_add, "$g_leave_defeated_faction_cur_lord", 1),
]),  
##############################################




################# 
(2,   
[
(map_free),
(call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
]),  
#################



#################  NEW v2.7 - makes ladies fall under the protection of someone if they haven't one already or their former protector is dead
(0.4,   ######## once every week for each of the 420 ladies
[
 (try_begin),
   (lt, "$g_place_lady_under_protection_cur_lady", kingdom_ladies_begin), 
     (assign, "$g_place_lady_under_protection_cur_lady", kingdom_ladies_begin),
 (try_end),
 
 (try_begin),
   (ge, "$g_place_lady_under_protection_cur_lady", kingdom_ladies_end), 
     (assign, "$g_place_lady_under_protection_cur_lady", kingdom_ladies_begin),
 (try_end),
 
 (try_begin),   
   (troop_slot_eq, "$g_place_lady_under_protection_cur_lady", slot_troop_is_alive, 1),  ###### she's alive
   (try_begin),   
     (neg|troop_slot_ge, "$g_place_lady_under_protection_cur_lady", slot_troop_spouse, 0),  ###### she's not married
     (neg|troop_slot_ge, "$g_place_lady_under_protection_cur_lady", slot_troop_betrothed, 0),  ###### she's not a bride
     ##### do nothing
   (else_try),
     (troop_slot_ge, "$g_place_lady_under_protection_cur_lady", slot_troop_father, 0),
       (troop_get_slot, ":father", "$g_place_lady_under_protection_cur_lady", slot_troop_father),   
	   (troop_slot_eq, ":father", slot_troop_is_alive, 1),  ###### he's alive
       ##### do nothing
   (else_try),
     (troop_slot_ge, "$g_place_lady_under_protection_cur_lady", slot_troop_guardian, 0),
       (troop_get_slot, ":guardian", "$g_place_lady_under_protection_cur_lady", slot_troop_guardian),   
	   (troop_slot_eq, ":guardian", slot_troop_is_alive, 1),  ###### he's alive
       ##### do nothing
   (else_try),  ######## gets a lord with good relations and of the same faction and make him the guardian
     (store_faction_of_troop, ":faction_lady", "$g_place_lady_under_protection_cur_lady"),
     (assign, ":loop_end", lords_end),
     (try_for_range, ":cur_lord", lords_begin, ":loop_end"),
       (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),  ####### he's alive/active
       (call_script, "script_troop_get_relation_with_troop", "$g_place_lady_under_protection_cur_lady", ":cur_lord"),
       (ge, reg0, 20),  ####### 20 or more
  	   (store_faction_of_troop, ":faction_lord", ":cur_lord"),
         (eq, ":faction_lord", ":faction_lady"),  ####### same faction
           (troop_set_slot, "$g_place_lady_under_protection_cur_lady", slot_troop_guardian, ":cur_lord"),  
           (assign, ":loop_end", -1), ##### breaks loop
     (try_end),
   (try_end),
 (try_end),
 ################# proceed to the next npc
 (val_add, "$g_place_lady_under_protection_cur_lady", 1),
]),  
#################


####### NEW v2.8 - if player doesn't have a minister, assign him a new one
####### NEW v2.9-KOMKE START-
(12,   
# (24,   ##KOMKE Changed to 24 to avoid activation before "party-size-player-king-of-supporters" fix
####### NEW v2.9-KOMKE END-
[
 (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
 (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
 (eq, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
 (le, "$g_player_minister", 0),
 (try_begin),   ############# if player didn't want to assign minister, wait 48 hours before showing the menu again
   (gt, "$g_minister_notification_hours", 0),
     (val_sub, "$g_minister_notification_hours", 12),
 (else_try),
   (eq, "$g_minister_notification_hours", 0),
     (call_script, "script_add_notification_menu", "mnu_ee_minister_appoint"),
 (try_end),
]),  
#################



####################### Empty triggers for savegame compatible changes
####
(24,   
[
]),  
####
(24,   
[
]),  
##############################################################################


	
##########################
]######################### END BRACKET
##########################

#### modmerger_start version=201 type=2
try:
    component_name = "simple_triggers"
    var_set = { "simple_triggers" : simple_triggers }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
#### modmerger_end
