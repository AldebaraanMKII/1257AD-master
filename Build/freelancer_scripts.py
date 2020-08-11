# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_items import *
from header_troops import ca_intelligence
from header_mission_templates import grc_infantry, grc_archers, grc_cavalry

####################################################################################################################
# scripts is a list of script records.
# Each script record contains the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
#+freelancer start
  ("freelancer_attach_party",
    [
        #prepare player to be part of lord's party
        (party_attach_to_party, "p_main_party", "$enlisted_party"),
        (set_camera_follow_party, "$enlisted_party"),
        (party_set_flags, "$enlisted_party", pf_always_visible, 1),
        (disable_party, "p_main_party"),

        #initialize service variable
        (assign, "$freelancer_state", 1),        
    ]),

  ("freelancer_detach_party",
    [
        #removes player from commanders party
        (enable_party, "p_main_party"),
        (party_detach, "p_main_party"),
        
        (try_begin),
            (party_is_active, "$enlisted_party"),
            (party_relocate_near_party, "p_main_party", "$enlisted_party", 2),
            (party_set_flags, "$enlisted_party", pf_always_visible, 0),
        (try_end),    
        
        (troop_set_slot, "trp_player", slot_troop_leaded_party, "p_main_party"),
        
        (set_camera_follow_party, "p_main_party"),
        (assign, "$g_player_icon_state", pis_normal),
    ]),

# ADDS THE PLAYER TO THE LORD'S PARTY  
  ("freelancer_event_player_enlists",
    [
        (party_clear, "p_freelancer_party_backup"),
           (call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
        (remove_member_from_party, "trp_player","p_freelancer_party_backup"),
    
	    ########## NEW v2.7
		(store_current_day, ":cur_day"),
      	(troop_set_slot, "trp_player", slot_troop_freelancer_start_date, ":cur_day"),
		##########
		
        #needed to stop bug where parties attack the old player party
        (call_script, "script_set_parties_around_player_ignore_player", 2, 4),
        #set lord as your commander
        (assign, "$enlisted_lord", "$g_talk_troop"),
        (troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
        #removes troops from player party
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
           (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
           (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
           (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
        (try_end),
        
        #set faction relations to allow player to join battles
        (store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_begin),
            (store_relation, ":player_relation", ":commander_faction", "$players_kingdom"),
            (lt, ":player_relation", 10),
            (call_script, "script_set_player_relation_with_faction", ":commander_faction", 10),
        (try_end),
        (assign, "$players_kingdom", ":commander_faction"),  #### NEW v2.1 - player is part of faction so now he gets to see those message colors related to the faction
        (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
           (neq, ":commander_faction", ":cur_faction"),
           # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
           (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (store_relation, ":player_relation", ":cur_faction", "$players_kingdom"),
           (ge, ":player_relation", 0),
           (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
        (try_end),        

        #adds standard issued equipment
        # (try_begin),
            # (neg|faction_slot_eq, ":commander_faction", slot_faction_freelancer_troop, 0),
            # (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_freelancer_troop),
        # (else_try),
            # (faction_get_slot, "$player_cur_troop", ":commander_faction", slot_faction_tier_1_troop),
        # (try_end),        

####### NEW v3.0-KOMKE START-

# ############ NEW v2.8 - player renown affects which troop he starts as
#         (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
#         (troop_get_slot, ":lord_culture", "$g_talk_troop", slot_troop_cur_culture), ############ NEW v2.8 - troop culture is used instead
#         (try_begin),
#           (is_between, ":lord_culture", cultures_begin, cultures_end), ############ NEW v2.8 - is troop culture is not one of those, skip to next else try
#           (try_begin),
#             (ge, ":player_renown", 300),
#               (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_tier_5_troop),
#           (else_try),
#             (ge, ":player_renown", 200),
#               (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_tier_4_troop),
#           (else_try),
#             (ge, ":player_renown", 100),
#               (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_tier_3_troop),
#           (else_try),
#             (ge, ":player_renown", 50),
#               (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_tier_2_troop),
# 		  ####################################	
#           (else_try),
#             (neg|faction_slot_eq, ":lord_culture", slot_faction_freelancer_troop, 0),
#             (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_freelancer_troop),
#           (else_try),
#             (faction_get_slot, "$player_cur_troop", ":lord_culture", slot_faction_tier_1_troop),
#           (try_end),
# ############ NEW v2.8 - gets faction culture instead
#         (else_try),
#           (neg|is_between, ":lord_culture", cultures_begin, cultures_end),
#           (faction_get_slot, ":faction_culture", "$g_talk_troop_faction", slot_faction_culture), 
#           (try_begin),
#             (ge, ":player_renown", 300),
#               (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_tier_5_troop),
#           (else_try),
#             (ge, ":player_renown", 200),
#               (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_tier_4_troop),
#           (else_try),
#             (ge, ":player_renown", 100),
#               (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_tier_3_troop),
#           (else_try),
#             (ge, ":player_renown", 50),
#               (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_tier_2_troop),
# ################################################	
#           (else_try),
#             (neg|faction_slot_eq, ":faction_culture", slot_faction_freelancer_troop, 0),
#             (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_freelancer_troop),
#           (else_try),
#             (faction_get_slot, "$player_cur_troop", ":faction_culture", slot_faction_tier_1_troop),
#           (try_end),
#         (try_end),
# ################################################



####### NEW v3.0-KOMKE END-

        (call_script, "script_freelancer_equip_troop", "$player_cur_troop"),

        (call_script, "script_freelancer_attach_party"),
        #makes Lords banner the players
        (troop_get_slot, ":banner", "$enlisted_lord", slot_troop_banner_scene_prop),
        (try_begin),
          (this_or_next|eq, "$g_player_banner_granted", 1),
          (eq, "$background_type", cb_noble),
          (troop_get_slot, ":noble_banner", "trp_player", slot_troop_banner_scene_prop),
          (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_banner_backup, ":noble_banner"),
        (else_try),
          (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_banner_backup, 0),
        (try_end),
        (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":banner"),
       # (display_message, "@You have been enlisted!"),    

        
        (str_store_troop_name_link, s13, "$enlisted_lord"),
        (str_store_faction_name_link, s14, ":commander_faction"),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_target_party, "$enlisted_party"),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_importance, 5),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_xp_reward, 1000),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_gold_reward, 100),
        (setup_quest_text, "qst_freelancer_enlisted"),
        (str_clear, s2), #description. necessary?
        (call_script, "script_start_quest", "qst_freelancer_enlisted", "$enlisted_lord"),
        (str_store_troop_name, s5, "$player_cur_troop"),

        (str_store_string, s1, "@Enlisted as a {s5} in the party of {s13} of {s14}."),
        (add_troop_note_from_sreg, "trp_player", 3, s1, 0),

        (str_store_string, s5, "@Current rank: {s5}"),
        (add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),
        
        #initialize service variables
        (call_script, "script_freelancer_get_upgrade_xp", "$player_cur_troop"),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, reg0),
        (troop_get_xp, reg0, "trp_player"),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_start_xp, reg0),
        (store_current_day, reg0), 
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_start_date, reg0),        
        (party_get_morale, reg0, "p_main_party"),
        (quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_orig_morale, reg0),    

        (assign, "$g_infinite_camping", 1),
        (rest_for_hours_interactive, 24 * 365, 5, 1),        
    ]),

#  RUNS IF THE PLAYER LEAVES THE ARMY

  ("freelancer_event_player_discharge",
    [
        #removes faction relation given at enlist
        (store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", 5),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
            (neq, ":commander_faction", ":cur_faction"),
            # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
            (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (store_relation, ":player_relation", ":cur_faction", "$players_kingdom"),
            (lt, ":player_relation", 0),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),
		
        (assign, "$players_kingdom", 0),  #### NEW v2.1 - player no longer part of faction
        # (call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),        
        # (troop_equip_items, "trp_player"),
        
############ NEW v1.0 - Warband Enhanced
		(store_current_day, ":cur_day"),
      	(troop_get_slot, ":service_day_start", "trp_player", slot_troop_freelancer_start_date),
        (store_sub, ":service_length", ":cur_day", ":service_day_start"),
		(try_begin),		
			(gt, ":service_length", 45),
			#(troop_equip_items, "trp_player"),
		(else_try),	
		    (call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),		
		    (troop_equip_items, "trp_player"),
		(try_end),
############	
	
        (try_begin),
            (this_or_next|eq, "$g_player_banner_granted", 1),
            (eq, "$background_type", cb_noble),
            (quest_get_slot, ":noble_banner", "qst_freelancer_enlisted", slot_quest_freelancer_banner_backup),
            (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":noble_banner"),
        (else_try),
            (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
        (try_end),
        (assign, "$freelancer_state", 0),
        (call_script, "script_freelancer_detach_party"),
        (call_script, "script_party_restore"),
        (rest_for_hours, 0,0,0),
        (display_message, "@You have left your commander!"), 

        (store_current_day, ":day"), 
        (quest_get_slot, reg0, "qst_freelancer_enlisted", slot_quest_freelancer_start_date),    
        (val_sub, ":day", reg0),
        (val_mul, ":day", 100),
        (val_div, ":day", 60),

        (call_script, "script_finish_quest", "qst_freelancer_enlisted", ":day"), #percentage of days served, based on 60 days
        (set_show_messages, 0),
        (try_for_range, ":quest", freelancer_quests_begin, freelancer_quests_end),
            (check_quest_active, ":quest"),
            (call_script, "script_cancel_quest", ":quest"),
        (try_end),
        (set_show_messages, 1),
        
        (str_clear, s1),
        (add_troop_note_from_sreg, "trp_player", 3, s1),
    ]),
    
#  RUNS IF THE PLAYER GOES ON VACATION

  ("freelancer_event_player_vacation",
   [
        #removes faction relation given at enlist
        (store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
            (neq, ":commander_faction", ":cur_faction"),
            # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
            (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

        (assign, "$players_kingdom", 0),  #### NEW v2.1 - player no longer part of faction
        (assign, "$freelancer_state", 2),
        (call_script, "script_freelancer_detach_party"),
        (call_script, "script_party_restore"),
        (rest_for_hours, 0,0,0),
        #(display_message, "@You have been granted leave!"),     

        (str_store_troop_name_link, s13, "$enlisted_lord"),
        (str_store_faction_name_link, s14, ":commander_faction"),
        (quest_set_slot, "qst_freelancer_vacation", slot_quest_target_party, "$enlisted_party"),
        #(quest_set_slot, "qst_freelancer_vacation", slot_quest_importance, 0),
        #(quest_set_slot, "qst_freelancer_vacation", slot_quest_xp_reward, 50),
        (quest_set_slot, "qst_freelancer_vacation",    slot_quest_expiration_days, 14),
        (setup_quest_text, "qst_freelancer_vacation"),
        (str_clear, s2), #description. necessary?
        (call_script, "script_start_quest", "qst_freelancer_vacation", "$enlisted_lord"),
        (str_store_string, s5, "@If you do not return to your commander in time, you will be declared a deserter."),
        (add_quest_note_from_sreg, "qst_freelancer_vacation", 3, s5, 0),    
    ]),

# RUNS WHEN PLAYER RETURNS FROM VACATION

  ("freelancer_event_player_returns",
    [
       (store_script_param_1, ":returning_from"),
        
        #needed to stop bug where parties attack the old player party
        (call_script, "script_set_parties_around_player_ignore_player", 2, 4),
        
        (call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
        (remove_member_from_party, "trp_player","p_freelancer_party_backup"),

        #removes troops from player party #Caba--could use party_clear? and then add the player back?
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 1, ":num_stacks"), #lower bound is 1 to ignore player character
           (party_stack_get_troop_id, ":cur_troops", "p_main_party", ":cur_stack"),
           (party_stack_get_size, ":cur_size", "p_main_party", ":cur_stack"),
           (party_remove_members, "p_main_party", ":cur_troops", ":cur_size"),
        (try_end),
        
        #To fix any errors of the lord changing parties
        (troop_get_slot, "$enlisted_party", "$enlisted_lord", slot_troop_leaded_party), 
        
        #set faction relations to allow player to join battles
        (store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
           (neq, ":commander_faction", ":cur_faction"),
           # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
           (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
        (try_end),    
        (try_begin),
            (store_relation, ":player_relation", ":commander_faction", "$players_kingdom"),
            (lt, ":player_relation", 5),
            (call_script, "script_set_player_relation_with_faction", ":commander_faction", 5),
        (try_end),

        (assign, "$players_kingdom", ":commander_faction"),  #### NEW v2.1 - player returns to faction
		
        (call_script, "script_freelancer_attach_party"),
        (display_message, "@You have rejoined your commander!"),         
        (try_begin),
            (eq, ":returning_from", plyr_mission_vacation),
            (call_script, "script_finish_quest", "qst_freelancer_vacation", 100),
        (else_try),
            (eq, ":returning_from", plyr_mission_captured),
            (call_script, "script_finish_quest", "qst_freelancer_captured", 100),
        (try_end),
    ]),

  ("freelancer_event_player_revolts",
   [
    #revert parties to former settings
    (call_script, "script_freelancer_detach_party"),
    (call_script, "script_freelancer_event_player_deserts"),
    
    #to prevent companions from being lost forever
    (call_script, "script_party_restore"), 
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
        (neg|troop_is_hero, ":return_troop"),
        (party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
        (party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
    (try_end),
    
    #adds other troops to join player revolt
    (call_script, "script_get_desert_troops"),
    
    #decreases player relation to his commander and faction
    (call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
    
    (store_troop_faction, ":commander_faction", "$enlisted_lord"),
    (try_begin),
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
        (store_faction_of_party, ":other_faction", ":commander_enemy"),
        (store_relation, ":relation", ":other_faction", ":commander_faction"),
        (store_sub, ":mod_relation", 100, ":relation"),
        (val_add, ":mod_relation", 5),
        (call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", ":mod_relation"),
    (try_end),
    
    (assign, "$players_kingdom", 0),  #### NEW v2.1 - player leaves faction
    (assign, "$freelancer_state", 0),
    
    (str_store_troop_name_link, s13, "$enlisted_lord"),
    (str_store_faction_name_link, s14, ":commander_faction"),
    (quest_set_slot, "qst_freelancer_revolt", slot_quest_target_party, 0), #changed to revolting prisoner's party if player chooses
    (quest_set_slot, "qst_freelancer_revolt", slot_quest_target_troop, "$enlisted_lord"),
    (setup_quest_text, "qst_freelancer_revolt"),
    (str_clear, s2), #description. necessary?
    (call_script, "script_start_quest", "qst_freelancer_revolt", "trp_player"),
    ]),
    
  # RUNS IF PLAYER DESERTS OR IS AWOL
  ("freelancer_event_player_deserts",
   [     
       (try_begin),
        (neg|party_is_active, "p_main_party"),
        (call_script, "script_freelancer_detach_party"),
    (try_end),
    
    (store_troop_faction, ":commander_faction", "$enlisted_lord"),
    (call_script, "script_change_player_relation_with_faction_ex", ":commander_faction", -10), 
    (call_script, "script_change_player_relation_with_troop", "$enlisted_lord", -10),
    (call_script, "script_change_player_honor", -20),
    (assign, "$players_kingdom", 0),  #### NEW v2.1 - player leaves faction
    
    (faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, 0),
    (try_begin),
        (this_or_next|eq, "$g_player_banner_granted", 1),
        (eq, "$background_type", cb_noble),
        (quest_get_slot, ":noble_banner", "qst_freelancer_enlisted", slot_quest_freelancer_banner_backup),
        (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, ":noble_banner"),
    (else_try),
        (troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0),
    (try_end),
    (rest_for_hours, 0,0,0),
    (assign, "$freelancer_state", 0),
    #(display_message, "@You have deserted your commander!"), #Taken care of elsewhere
    (set_show_messages, 0),
    (try_for_range, ":quest", freelancer_quests_begin, freelancer_quests_end),
        (check_quest_active, ":quest"),
        (call_script, "script_fail_quest", ":quest"),
        (call_script, "script_end_quest", ":quest"),
    (try_end),
    (set_show_messages, 1),
    (str_clear, s1),
    (add_troop_note_from_sreg, "trp_player", 3, s1),
   ]),    
   
  ("freelancer_event_player_captured",
    [
        ##bug fix for player getting duplicated when taken prisoner--likely unnecessary & fixed elsewhere
        (try_begin),
            (troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
            (troop_get_slot, ":party_no", "trp_player", slot_troop_prisoner_of_party),
            (call_script, "script_remove_troop_from_prison", "trp_player"),
            (party_is_active, ":party_no"),
            (party_count_prisoners_of_type, reg0, ":party_no", "trp_player"),
            (gt, reg0, 0),
            (party_remove_prisoners, ":party_no", "trp_player", reg0),
            (gt, reg0, 0), #number removed
        (else_try),
            (try_for_parties, ":party_no"),
                (party_count_prisoners_of_type, reg0, ":party_no", "trp_player"),
                (gt, reg0, 0),
                (party_remove_prisoners, ":party_no", "trp_player", reg0),
            (try_end),
        (try_end),

        #removes faction relation given at enlist
        (store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
            (neq, ":commander_faction", ":cur_faction"),
            # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
            (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

        (assign, "$players_kingdom", 0),  #### NEW v2.1 - player no longer part of faction
			
        (call_script, "script_freelancer_detach_party"),
        (call_script, "script_party_restore"),
        #remove non-companions. they are lost if you are defeated
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
            (neg|troop_is_hero, ":return_troop"),
            (party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
            (party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
        (try_end),
        (assign, "$enlisted_party", 0),
        (assign, "$freelancer_state", 2),
        (display_message, "@You have been captured! Escape and rejoin your commander!"),     

        (str_store_troop_name_link, s13, "$enlisted_lord"),
        (str_store_faction_name_link, s14, ":commander_faction"),
        (quest_set_slot, "qst_freelancer_captured", slot_quest_target_troop, "$enlisted_lord"),
        (quest_set_slot, "qst_freelancer_captured", slot_quest_object_center, "$g_enemy_party"),
        (store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
        (quest_set_slot, "qst_freelancer_captured", slot_quest_object_faction, ":enemy_faction"),
        (quest_set_slot, "qst_freelancer_captured", slot_quest_importance, 0),
        (quest_set_slot, "qst_freelancer_captured", slot_quest_xp_reward, 100),
        (quest_set_slot, "qst_freelancer_captured",    slot_quest_expiration_days, 20),
        (setup_quest_text, "qst_freelancer_captured"),
        (str_clear, s2), #description. necessary?
        (call_script, "script_start_quest", "qst_freelancer_captured", "$enlisted_lord"),
        (str_store_string, s5, "@If you do not return to your commander in time, you will be declared a deserter."),
        (add_quest_note_from_sreg, "qst_freelancer_captured", 3, s5, 0),    
    ]),
    
    
  # RETURNS PART OF THE ORIGINAL PARTY
  ("party_restore", 
    [
        (store_current_day, ":cur_day"),
        #formula for soldier desertion chance
        (quest_get_slot, ":service_day_start", "qst_freelancer_enlisted", slot_quest_freelancer_start_date),
        (store_sub, ":service_length", ":cur_day", ":service_day_start"), #gets number of days served
        (quest_get_slot, ":morale", "qst_freelancer_enlisted", slot_quest_freelancer_orig_morale),
        (store_add, ":return_chance", 800, ":morale"), #up to 100
        (val_sub, ":return_chance", ":service_length"), #up to far over 100

        #loop that looks at each troop stack in a party, 
        #then decides if troops of that stack will return, 
        #and randomly assigns a number of troops in that stack to return
        (party_get_num_companion_stacks, ":num_stacks", "p_freelancer_party_backup"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
            (assign, ":stack_amount", 0),
            (party_stack_get_troop_id, ":return_troop", "p_freelancer_party_backup", ":cur_stack"),
            (neq, ":return_troop", "trp_player"),
            (try_begin),
                (troop_is_hero, ":return_troop"), #bugfix for companions (simple, they always return)
                (assign, ":stack_amount", 1),
            (else_try),
                #limit may need changed for more accurate probability
                (store_random_in_range, ":return_random", 0, 1000),
                (is_between, ":return_random", 0, ":return_chance"),
                (party_stack_get_size, ":stack_size", "p_freelancer_party_backup", ":cur_stack"),
                #checks what chance there is that all troops in stack will return
                (store_random_in_range, ":return_random", 0, 1000),
                (try_begin),
                    (is_between, ":return_random", 0, ":return_chance"),
                    (assign, ":stack_amount", ":stack_size"),
                (else_try),
                    #else random number of troops return
                    (store_random_in_range, ":stack_amount", 0, ":stack_size"),
                (try_end),
            (try_end),
            (ge, ":stack_amount", 1),
            (party_add_members, "p_main_party", ":return_troop", ":stack_amount"),
        (try_end),
        (party_clear, "p_freelancer_party_backup"),
        (try_for_range, ":companion", companions_begin, companions_end),
            (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
            (neg|main_party_has_troop, ":companion"),
            (troop_set_slot, ":companion", slot_troop_days_on_mission, 0),
            (troop_set_slot, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
            (troop_set_slot, ":companion", slot_troop_mission_object, 0), 
        (try_end),
    ]),

#  CALCULATES NUMBER OF DESERTING TROOPS

   ("get_desert_troops", #CABA - check this
    [
        (party_get_morale, ":commander_party_morale", "$enlisted_party"), #does this actually get tracked for non-player parties?
        (store_current_day, ":cur_day"),
        #formula for soldier desertion chance
        #gets number of days served
        (quest_get_slot, ":service_day_start", "qst_freelancer_enlisted", slot_quest_freelancer_start_date),
        (store_sub, ":service_length", ":cur_day", ":service_day_start"),
        #inverts the commander's party morale
        (store_sub, ":commander_neg_morale", 100, ":commander_party_morale"), #still a positive number... 100-80 = 20
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        #had to multiply these skills to give them a decent effect on desertion chance
        (val_mul, ":cur_leadership", 10), #up to 100
        (val_mul, ":cur_persuasion", 10), #up to 100
        (store_add, ":desert_chance", ":cur_leadership", ":cur_persuasion"), #up to 200
        (val_add, ":desert_chance", ":service_length"), #up to 400 maybe
        (val_add, ":desert_chance", ":commander_neg_morale"), #up to 450, maybe? if party morale is down to 50
        #loop that looks at each troop stack in a party, 
        #then decides if troops of that stack will desert, 
        #and randomly assigns a number of troops in that stack to desert
        (party_get_num_companion_stacks, ":num_stacks", "$enlisted_party"),
        (try_for_range_backwards, ":cur_stack", 1, ":num_stacks"),
            #limit may need changed for more accurate probability
            (store_random_in_range, ":desert_random", 0, 1000),
            (is_between, ":desert_random", 0, ":desert_chance"),
            #switching deserting troops to player party
            (party_stack_get_troop_id, ":desert_troop", "$enlisted_party", ":cur_stack"),
            (party_stack_get_size, ":stack_size", "$enlisted_party", ":cur_stack"),
            (store_random_in_range, ":stack_amount", 0, ":stack_size"),
            (party_remove_members, "$enlisted_party", ":desert_troop", ":stack_amount"),
            (party_add_members, "p_main_party", ":desert_troop", ":stack_amount"),
        (try_end),                
    ]),
    
  ("freelancer_keep_field_loot",
   [
    (get_player_agent_no, ":player"),
    (try_for_range, ":ek_slot", ek_item_0, ek_head),
        (agent_get_item_slot, ":item", ":player", ":ek_slot"), 
        (gt, ":item", 0),
        (neg|troop_has_item_equipped, "trp_player", ":item"),
        (troop_add_item, "trp_player", ":item"),
		########## NEW v2.7 - displays a message
        (str_store_item_name, s1, ":item"),
        (display_message, "@Received item: {s1}", 0x00ff00),  
		##########
    (try_end),
    (agent_get_horse, ":horse", ":player"),
    (try_begin),
      (gt, ":horse", 0),
      (agent_get_item_id, ":horse", ":horse"),
      (troop_get_inventory_slot, ":old_horse", "trp_player", ek_horse),
      (neq, ":horse", ":old_horse"),
      (try_begin),
        (gt, ":old_horse", 0),
        (troop_get_inventory_slot_modifier, ":horse_imod", "trp_player", ek_horse),
        (troop_add_item, "trp_player", ":old_horse", ":horse_imod"),
      (try_end),
      (troop_set_inventory_slot, "trp_player", ek_horse, ":horse"),
      ########## NEW v2.7 - displays a message
      (str_store_item_name, s1, ":horse"),
      (display_message, "@You got a {s1} from the field.", 0x00ff00),  
      ##########
    (try_end),
   ]),

   #Returns in reg0
  ("freelancer_get_upgrade_xp",
   [
####### NEW v3.0-KOMKE START-
    (store_script_param_1, ":troop_no"),
    (assign, reg0, 0),
##This array stores experience table, substract 1 level to get it right 
    (troop_set_slot, "trp_temp_array_c", 0, 0),
    (troop_set_slot, "trp_temp_array_c", 1, 600),
    (troop_set_slot, "trp_temp_array_c", 2, 1360),
    (troop_set_slot, "trp_temp_array_c", 3, 2296),
    (troop_set_slot, "trp_temp_array_c", 4, 3426),
    (troop_set_slot, "trp_temp_array_c", 5, 4768),
    (troop_set_slot, "trp_temp_array_c", 6, 6345),
    (troop_set_slot, "trp_temp_array_c", 7, 8179),
    (troop_set_slot, "trp_temp_array_c", 8, 10297),
    (troop_set_slot, "trp_temp_array_c", 9, 13010),
    (troop_set_slot, "trp_temp_array_c", 10, 16161),
    (troop_set_slot, "trp_temp_array_c", 11, 19806),
    (troop_set_slot, "trp_temp_array_c", 12, 24007),
    (troop_set_slot, "trp_temp_array_c", 13, 28832),
    (troop_set_slot, "trp_temp_array_c", 14, 34362),
    (troop_set_slot, "trp_temp_array_c", 15, 40682),
    (troop_set_slot, "trp_temp_array_c", 16, 47892),
    (troop_set_slot, "trp_temp_array_c", 17, 56103),
    (troop_set_slot, "trp_temp_array_c", 18, 65441),
    (troop_set_slot, "trp_temp_array_c", 19, 77233),
    (troop_set_slot, "trp_temp_array_c", 20, 90809),
    (troop_set_slot, "trp_temp_array_c", 21, 106425),
    (troop_set_slot, "trp_temp_array_c", 22, 124371),
    (troop_set_slot, "trp_temp_array_c", 23, 144981),
    (troop_set_slot, "trp_temp_array_c", 24, 168636),
    (troop_set_slot, "trp_temp_array_c", 25, 195769),
    (troop_set_slot, "trp_temp_array_c", 26, 226879),
    (troop_set_slot, "trp_temp_array_c", 27, 262533),
    (troop_set_slot, "trp_temp_array_c", 28, 303381),
    (troop_set_slot, "trp_temp_array_c", 29, 350164),
    (troop_set_slot, "trp_temp_array_c", 30, 412091),
    (troop_set_slot, "trp_temp_array_c", 31, 484440),
    (troop_set_slot, "trp_temp_array_c", 32, 568947),
    (troop_set_slot, "trp_temp_array_c", 33, 667638),
    (troop_set_slot, "trp_temp_array_c", 34, 782877),
    (troop_set_slot, "trp_temp_array_c", 35, 917424),
    (troop_set_slot, "trp_temp_array_c", 36, 1074494),
    (troop_set_slot, "trp_temp_array_c", 37, 1257843),
    (troop_set_slot, "trp_temp_array_c", 38, 1471851),
    (troop_set_slot, "trp_temp_array_c", 39, 1721626),
    (troop_set_slot, "trp_temp_array_c", 40, 2070551),
    (troop_set_slot, "trp_temp_array_c", 41, 2489361),
    (troop_set_slot, "trp_temp_array_c", 42, 2992033),
    (troop_set_slot, "trp_temp_array_c", 43, 3595340),
    (troop_set_slot, "trp_temp_array_c", 44, 4319408),
    (troop_set_slot, "trp_temp_array_c", 45, 5188389),
    (troop_set_slot, "trp_temp_array_c", 46, 6231267),
    (troop_set_slot, "trp_temp_array_c", 47, 7482821),
    (troop_set_slot, "trp_temp_array_c", 48, 8984785),
    (troop_set_slot, "trp_temp_array_c", 49, 11236531),
    (troop_set_slot, "trp_temp_array_c", 50, 14051314),
    (troop_set_slot, "trp_temp_array_c", 51, 17569892),
    (troop_set_slot, "trp_temp_array_c", 52, 21968215),
    (troop_set_slot, "trp_temp_array_c", 53, 27466219),
    (troop_set_slot, "trp_temp_array_c", 54, 34338823),
    (troop_set_slot, "trp_temp_array_c", 55, 42929679),
    (troop_set_slot, "trp_temp_array_c", 56, 53668349),
    (troop_set_slot, "trp_temp_array_c", 57, 67091786),
    (troop_set_slot, "trp_temp_array_c", 58, 83871183),
    (troop_set_slot, "trp_temp_array_c", 59, 160204600),
    (troop_set_slot, "trp_temp_array_c", 60, 320304600),
    (troop_set_slot, "trp_temp_array_c", 61, 644046000),
    (troop_set_slot, "trp_temp_array_c", 62, 2050460000),
    (troop_set_slot, "trp_temp_array_c", 63, 2050460000),
    (troop_set_slot, "trp_temp_array_c", 64, 2050460000),
    (troop_set_slot, "trp_temp_array_c", 65, 2050460000),
    (troop_set_slot, "trp_temp_array_c", 66, 2050460000),

    (try_begin),
        (troop_get_upgrade_troop, ":upgrade_troop", ":troop_no", 0),
        (store_character_level, ":player_level", "trp_player"),
        (try_begin),
            (gt, ":upgrade_troop", 1), #if there is an upgrade up the troop tree
            # (call_script, "script_game_get_upgrade_xp", ":troop_no"),######### NEW v3.0-KOMKE replaced this call with code below
            (store_character_level, ":troop_level", ":upgrade_troop"),
            (val_sub, ":troop_level", 1),
            (troop_get_slot, ":troop_experience", "trp_temp_array_c", ":troop_level"),
            (try_begin),
                (gt, ":troop_level", ":player_level"),## if troop to upgrade level > player level
                (troop_get_xp, ":player_experience", "trp_player"),
                (store_sub, ":needed_upgrade_xp", ":troop_experience", ":player_experience"),## experience is the difference
                (assign, reg0, ":needed_upgrade_xp"),
            (else_try),
                (store_character_level, ":enlist_level", ":troop_no"),
                (val_sub, ":enlist_level", 1),
                (troop_get_slot, ":enlist_experience", "trp_temp_array_c", ":enlist_level"),
                (store_sub, ":needed_upgrade_xp", ":troop_experience", ":enlist_experience"),## else substract upgrade troop exp - enlisted troop exp
                (assign, reg0, ":needed_upgrade_xp"),
            (try_end),
        (try_end),
    (try_end),  
####### NEW v3.0-KOMKE END- 
        #ranks for pay levels and to upgrade player equipment based on upgrade troop level times 1000
        # (try_begin),
           # (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
           # (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
           # (store_character_level, ":level", ":upgrade_troop"),
           # (store_pow, ":required_xp", ":level", 2), #square the level and
           # (val_mul, ":required_xp", 100),           #multiply by 100 to get xp
           # (ge, ":service_xp_cur", ":level"),
           # (jump_to_menu, "mnu_upgrade_path"),
        # (try_end),    
           
           ##THIS  BLOCK IS ALMOST DEFINITELY BE BETTER --said someone ?? on the freelancer team
           # (store_character_level, ":cur_level", "$player_cur_troop"),
           # (val_sub, ":cur_level", 1),
           # (get_level_boundary, ":cur_level", ":cur_level"),
           # (store_character_level, ":required_xp", ":upgrade_troop"),
           # (val_sub, ":required_xp", 1),
           # (get_level_boundary, ":required_xp", ":required_xp"),
           # (val_sub, ":required_xp", ":cur_level"),           
           ##    
   ]),
   
   #Returns troop ID in reg0
  ("cf_freelancer_get_reassign_troop",
   [
    (store_script_param_1, ":trp_array"),
    (store_script_param_2, ":division"), 
    
    (troop_get_slot, ":max_slot", ":trp_array", 0),
    (assign, ":end", ":max_slot"),
    (try_for_range, ":i", 1, ":end"),
        (troop_slot_eq, ":trp_array", ":i", "$player_cur_troop"),
        (assign, ":end", ":i"),
    (try_end),
    (lt, ":end", ":max_slot"),
    
    (assign, ":cur_slot", ":max_slot"),
    
    (try_for_range, ":i", 1, ":end"), #troops before current troop--thus lower or same tier
        (troop_get_slot, ":troop", ":trp_array", ":i"),
        (gt, ":troop", 0), #double check
        (assign, ":is_valid", 1),
        (try_begin),
            (eq, ":division", grc_cavalry),
            (troop_is_guarantee_horse, ":troop"),
        (else_try),
            (eq, ":division", grc_archers),
            (neg|troop_is_guarantee_horse, ":troop"),
            (troop_is_guarantee_ranged, ":troop"),
        (else_try),
            (eq, ":division", grc_infantry),
            (neg|troop_is_guarantee_horse, ":troop"),
            (neg|troop_is_guarantee_ranged, ":troop"),
        (else_try),
            (assign, ":is_valid", 0),
        (try_end),
        (eq, ":is_valid", 1),
        (call_script, "script_cf_freelancer_player_can_upgrade", ":troop"),
        (troop_set_slot, ":trp_array", ":cur_slot", ":troop"),
        (val_add, ":cur_slot", 1),
    (try_end),
    (gt, ":cur_slot", ":max_slot"),

    (store_sub, ":num_choices", ":cur_slot", ":max_slot"),
    (try_begin),
        (gt, ":num_choices", 1),
        (store_attribute_level, ":int", "trp_player", ca_intelligence),
        (val_div, ":int", 8),
        (val_sub, ":num_choices", 1),
        (val_min, ":int", ":num_choices"),
        (val_add, ":max_slot", ":int"), #bring up the minimum troop based on intelligence/abilty to adapt
    (try_end),
    (store_random_in_range, ":i", ":max_slot", ":cur_slot"),    
    (troop_get_slot, reg0, ":trp_array", ":i"),  
   ]), 

  ("freelancer_list_faction_troops",
   [
    (store_script_param, ":faction", 1),
    (store_script_param, ":destination_array", 2),
    (store_script_param, ":helper_array", 3), 
    (try_for_range, reg0, 1, 101),
        (troop_set_slot, ":destination_array", reg0, 0),
        (troop_set_slot, ":helper_array", reg0, 0),
    (try_end),
    (faction_get_slot, reg0, ":faction", slot_faction_tier_1_troop),
    (troop_set_slot, ":destination_array", 1, reg0),
    (troop_set_slot, ":helper_array", 0, reg0),
    (assign, ":list_slot", 2),
    (assign, ":check_slot", 1),
    (assign, ":end", 101),
    (try_for_range, ":unused", 0, ":end"),
        (troop_get_slot, ":troop", ":helper_array", 0),
        (gt, ":troop", 0),
        (try_for_range, ":i", 0, 2),
            (troop_get_upgrade_troop, reg0, ":troop", ":i"),
            (gt, reg0, 0),
            (troop_set_slot, ":destination_array", ":list_slot", reg0),
            (troop_set_slot, ":helper_array", ":check_slot", reg0),
            (val_add, ":list_slot", 1),
            (val_add, ":check_slot", 1),
        (try_end),
        (try_for_range, ":i", 1, ":check_slot"),
            (troop_get_slot, reg0, ":helper_array", ":i"),
            (store_sub, ":i_minus_one", ":i", 1),
            (troop_set_slot, ":helper_array", ":i_minus_one", reg0),
        (try_end),
        (troop_set_slot, ":helper_array", ":check_slot", 0),
        (val_sub, ":check_slot", 1),
    (else_try),
        (assign, ":end", 0),
    (try_end),  
    (troop_set_slot, ":destination_array", 0, ":list_slot"),
   ]),        
  
   #s0 outputs reason for failure  
  ("cf_freelancer_player_can_upgrade",
   [
    (store_script_param_1, ":source_troop"),
    
    (str_clear, s0),
    (troop_get_inventory_capacity, ":troop_cap", ":source_troop"),    
    
    (assign, ":type_available", 0),
    (assign, ":type_count", 0),
    (assign, ":end", itp_type_arrows),
    (try_for_range, ":type", itp_type_one_handed_wpn, ":end"),
        #Count Items from Source Troop
        (assign, ":end2", ":troop_cap"),
        (try_for_range, ":inv_slot", 0, ":end2"),
            (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
            (gt, ":item", 0),
            (item_get_type, ":item_type", ":item"),
            (eq, ":item_type", ":type"),
            (val_add, ":type_count", 1),
            (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
            (eq, reg0, 1),        
            (assign, ":type_available", 1),
            (assign, ":end2", 0), #break
        (try_end),
        (eq, ":type_available", 1),
        (assign, ":end", itp_type_one_handed_wpn), #break
    (try_end), #Melee loop
    (try_begin),
        (eq, ":type_available", 0),
        (gt, ":type_count", 0), #only care if there were items possible to equip
        (str_store_string, s0, "@--too weak for required melee weapons"),
    (try_end),
    (str_is_empty, s0),    
    
    (assign, ":type_available", 0),
    (assign, ":type_count", 0),
    (assign, ":end2", ":troop_cap"),
    (try_for_range, ":inv_slot", 0, ":end2"),
        (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
        (gt, ":item", 0),
        (item_get_type, ":item_type", ":item"),
        (eq, ":item_type", itp_type_body_armor),
        (val_add, ":type_count", 1),
        (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
        (eq, reg0, 1),        
        (assign, ":type_available", 1),
        (assign, ":end2", 0), #break
    (try_end),
    (try_begin),
        (eq, ":type_available", 0),
        (gt, ":type_count", 0), #only care if there were items possible to equip
        (str_store_string, s0, "@--too weak for required armor"),
    (try_end),
    (str_is_empty, s0),    
    
    (try_begin),
        (troop_is_guarantee_ranged, ":source_troop"),
        (assign, ":type_available", 0),
        (assign, ":type_count", 0),
        (assign, ":end", itp_type_goods),
        (try_for_range, ":type", itp_type_bow, ":end"),
            #Count Items from Source Troop
            (assign, ":end2", ":troop_cap"),
            (try_for_range, ":inv_slot", 0, ":end2"),
                (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
                (gt, ":item", 0),
                (item_get_type, ":item_type", ":item"),
                (eq, ":item_type", ":type"),
                (val_add, ":type_count", 1),
                (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
                (eq, reg0, 1),        
                (assign, ":type_available", 1),
                (assign, ":end2", 0), #break
            (try_end),
            (eq, ":type_available", 1),
            (assign, ":end", itp_type_bow), #break
        (try_end), #Ranged loop
        (eq, ":type_available", 0),
        (gt, ":type_count", 0), #only care if there were items possible to equip
        (str_store_string, s0, "@--lacking required ranged skill or strength"),
    (try_end),
    (str_is_empty, s0),    
    
    (try_begin),
        (troop_is_guarantee_horse, ":source_troop"),
        (assign, ":type_available", 0),
        (assign, ":type_count", 0),
        (assign, ":end2", ":troop_cap"),
        (try_for_range, ":inv_slot", 0, ":end2"),
            (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
            (gt, ":item", 0),
            (item_get_type, ":item_type", ":item"),
            (eq, ":item_type", itp_type_horse),
            (val_add, ":type_count", 1),
            (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
            (eq, reg0, 1),        
            (assign, ":type_available", 1),
            (assign, ":end2", 0), #break
        (try_end),
        (eq, ":type_available", 0),
        (gt, ":type_count", 0), #only care if there were items possible to equip
        (str_store_string, s0, "@--horsemanship needs improving"),
    (try_end),
    (str_is_empty, s0),

    # (try_begin),
        # (troop_has_flag, ":source_troop", tf_guarantee_shield),##WSE
        # (assign, ":type_available", 0),
        # (assign, ":type_count", 0),
        # (assign, ":end2", ":troop_cap"),
        # (try_for_range, ":inv_slot", 0, ":end2"),
            # (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
            # (gt, ":item", 0),
            # (item_get_type, ":item_type", ":item"),
            # (eq, ":item_type", itp_type_shield),
            # (val_add, ":type_count", 1),
            # (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
            # (eq, reg0, 1),        
            # (assign, ":type_available", 1),
            # (assign, ":end2", 0), #break
        # (try_end),
        # (eq, ":type_available", 0),
        # (gt, ":type_count", 0), #only care if there were items possible to equip
        # (str_store_string, s0, "@--lacking required ranged skill or strength"),
    # (try_end),    
    # (str_is_empty, s0),
   ]),
    
  ("freelancer_equip_troop",
   [
    (store_script_param_1, ":source_troop"),
    
    (str_clear, s2),
    (set_show_messages, 0),
    
    (assign, ":recording_slot", slot_freelancer_equip_start),    
    (troop_get_inventory_capacity, ":troop_cap", ":source_troop"),
    (assign, ":melee_given", 0),
    (assign, ":needs_ammo", 0),
    (assign, ":open_weapon_slot", 0),
    (try_for_range, ":type", itp_type_horse, itp_type_pistol),
        (neq, ":type", itp_type_goods),
        (neq, ":type", itp_type_arrows),
        (neq, ":type", itp_type_bolts),
        
        #Assign Prob. of Getting Type
        (assign, ":continue", 0),
        (try_begin),
            (troop_is_guarantee_horse, ":source_troop"),
            (eq, ":type", itp_type_horse),
            (assign, ":continue", 1),
        (else_try),
            (troop_is_guarantee_ranged, ":source_troop"),
            (this_or_next|eq, ":type", itp_type_bow),
            (this_or_next|eq, ":type", itp_type_crossbow),
            (eq, ":type", itp_type_thrown),
            (assign, ":continue", 1),
        (else_try),
            (this_or_next|eq, ":type", itp_type_shield), #Shields and all armor pieces are guaranteed
            (this_or_next|eq, ":type", itp_type_head_armor), 
            (this_or_next|eq, ":type", itp_type_body_armor), 
            (this_or_next|eq, ":type", itp_type_foot_armor), 
            (eq, ":type", itp_type_hand_armor),
            (assign, ":continue", 1),
        (else_try),
            (neq, ":type", itp_type_horse),
            (lt, ":open_weapon_slot", 4),
            # (store_random_in_range, ":continue", 0, 3), # 1 chance in three of being 1
            (assign, ":continue", 1), ########### NEW v2.8 - now guaranteed
        (try_end),
        (eq, ":continue", 1),        
        
        #Clear Temp Array
        (try_for_range, ":inv_slot", 0, 20),
            (troop_set_slot, "trp_temp_array_a", ":inv_slot", 0),
        (try_end),    
        
        #Collect Items from Source Troop
        (assign, ":type_count", 0),
        (try_for_range, ":inv_slot", 0, ":troop_cap"),
            (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
            (gt, ":item", 0),
            (item_get_type, ":item_type", ":item"),
            (eq, ":item_type", ":type"),
            (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
            (eq, reg0, 1),        
            (troop_set_slot, "trp_temp_array_a", ":type_count", ":item"),
            (val_add, ":type_count", 1),
        (try_end),
        (gt, ":type_count", 0),
        
        #Pick Random Item of Type from Troop
        (try_begin),
            (eq, ":type_count", 1),
            (assign, ":index", 0),
        (else_try),
            (store_random_in_range, ":index", 0, ":type_count"),
        (try_end),
        (troop_get_slot, ":item", "trp_temp_array_a", ":index"),
        (gt, ":item", 0),        
        (str_store_item_name, s3, ":item"),
        (str_store_string, s2, "@{s3}, {s2}"),
        
        #Select correct EK slot to force equip
        (try_begin),
            (eq, ":type", itp_type_horse),
            (assign, ":ek_slot", ek_horse),
        (else_try),
            (is_between, ":type", itp_type_head_armor, itp_type_pistol),
            (store_sub, ":shift", ":type", itp_type_head_armor),
            (store_add, ":ek_slot", ek_head, ":shift"),
        (else_try),
            (store_add, ":ek_slot", ek_item_0, ":open_weapon_slot"),
        (try_end),
        
        #Check for item already there, move it if present
        (try_begin),
          (eq, "$ee_freelancer_upgrade_unequip", 1),
            (troop_get_inventory_slot, ":old_item", "trp_player", ":ek_slot"),
            (gt, ":old_item", 0),
              (troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":ek_slot"),
              (troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
        (try_end),
        
        #Add Item
        (try_begin), 
          (eq, "$ee_freelancer_upgrade_unequip", 1),
            (troop_set_inventory_slot, "trp_player", ":ek_slot", ":item"),
            (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
            (val_add, ":recording_slot", 1),
        (else_try),
          (eq, "$ee_freelancer_upgrade_unequip", 0),
            (troop_add_item, "trp_player", ":item", 0),
            (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
            (val_add, ":recording_slot", 1),
        (try_end),
		
        (try_begin),
            (is_between, ":type", itp_type_one_handed_wpn, itp_type_head_armor), #Uses one of the 4 weapon slots
            (val_add, ":open_weapon_slot", 1),
            (try_begin),
                (is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
                (assign, ":melee_given", 1),
            (else_try),
                (eq, ":type", itp_type_bow),
                (assign, ":needs_ammo", itp_type_arrows),
            (else_try),
                (eq, ":type", itp_type_crossbow),
                (assign, ":needs_ammo", itp_type_bolts),
            (try_end),
        (try_end),
    (try_end), #Item Types Loop
     
    #add ammo for any equipped bow
    (try_begin),
        (neq, ":needs_ammo", 0),        
        #Check for item already in the last slot, move it if present
        (try_begin), 
          (eq, "$ee_freelancer_upgrade_unequip", 1),
            (troop_get_inventory_slot, ":old_item", "trp_player", ek_item_3),
            (gt, ":old_item", 0),
              (troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ek_item_3),
              (troop_add_item, "trp_player", ":old_item", ":old_item_imod"), 
        (try_end),
        
        (assign, ":end", ":troop_cap"),
        (try_for_range, ":inv_slot", 0, ":end"),
          (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
          (gt, ":item", 0),
          (item_get_type, ":type", ":item"),
          (eq, ":type", ":needs_ammo"),
          (try_begin), 
            (eq, "$ee_freelancer_upgrade_unequip", 1),
              (troop_set_inventory_slot, "trp_player", ek_item_3, ":item"),
              (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
              (val_add, ":recording_slot", 1),
              (assign, ":open_weapon_slot", 4),
              (str_store_item_name, s3, ":item"),
              (str_store_string, s2, "@{s3}, {s2}"),
              (assign, ":end", 0),
          (else_try),
            (eq, "$ee_freelancer_upgrade_unequip", 0),
              (troop_add_item, "trp_player", ":item", 0),
              (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
              (val_add, ":recording_slot", 1),
              (assign, ":open_weapon_slot", 4),
              (str_store_item_name, s3, ":item"),
              (str_store_string, s2, "@{s3}, {s2}"),
              (assign, ":end", 0),
          (try_end),
        (try_end),
    (try_end), 
    
    #double check melee was given
    (try_begin),
        (eq, ":melee_given", 0),
        (assign, ":end", ":troop_cap"),
        (try_for_range, ":inv_slot", 0, ":end"),
            (troop_get_inventory_slot, ":item", ":source_troop", ":inv_slot"),
            (gt, ":item", 0),
            (item_get_type, ":type", ":item"),
            (is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows),
            (call_script, freelancer_can_use_item, "trp_player", ":item", 0),
            (eq, reg0, 1),    
            (try_begin),
                (gt, ":open_weapon_slot", 3),
                (assign, ":open_weapon_slot", 2),
            (try_end),
            
            #Check for item already there
            (try_begin),
              (eq, "$ee_freelancer_upgrade_unequip", 1),
                (troop_get_inventory_slot, ":old_item", "trp_player", ":open_weapon_slot"),
                (gt, ":old_item", 0),
                  (troop_get_inventory_slot_modifier, ":old_item_imod", "trp_player", ":open_weapon_slot"),
                  (troop_add_item, "trp_player", ":old_item", ":old_item_imod"),
            (try_end),
            
          (try_begin), 
            (eq, "$ee_freelancer_upgrade_unequip", 1),
              (troop_set_inventory_slot, "trp_player", ":open_weapon_slot", ":item"),        
              (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
              (val_add, ":recording_slot", 1),
              (str_store_item_name, s3, ":item"),
              (str_store_string, s2, "@{s3}, {s2}"),
              (assign, ":end", 0),
          (else_try),
            (eq, "$ee_freelancer_upgrade_unequip", 0),
              (troop_add_item, "trp_player", ":item", 0),
              (party_set_slot, "p_freelancer_party_backup", ":recording_slot", ":item"),
              (val_add, ":recording_slot", 1),
              (str_store_item_name, s3, ":item"),
              (str_store_string, s2, "@{s3}, {s2}"),
              (assign, ":end", 0),
          (try_end),
        (try_end),
    (try_end), 
    
    (set_show_messages, 1),
    (try_begin),
        (neg|str_is_empty, s2),
        (val_sub, ":recording_slot", slot_freelancer_equip_start),
        (party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, ":recording_slot"),    #Record Number of Items Added
        
        (str_store_troop_name, s1, ":source_troop"),
        (display_message, "@The equipment of a {s1}: {s2}is assigned to you."),    
    (try_end),
   ]),
    
  ("freelancer_unequip_troop",
   [
    (store_script_param_1, ":source_troop"),

    (str_clear, s2),    
    (set_show_messages, 0),
    
    (party_get_slot, ":num_items", "p_freelancer_party_backup", slot_freelancer_equip_start - 1), #Num of items previously given
    
    (troop_get_inventory_capacity, ":cap", "trp_player"),        
    (try_for_range, ":i", 0, ":num_items"),
        (store_add, ":slot", slot_freelancer_equip_start, ":i"),
        (party_get_slot, ":given_item", "p_freelancer_party_backup", ":slot"),
        (gt, ":given_item", 0),
        
        (assign, ":end", ":cap"),
        (try_for_range, ":inv_slot", 0, ":end"),
            (troop_get_inventory_slot, ":item", "trp_player", ":inv_slot"),
            (eq, ":item", ":given_item"),            
            (troop_get_inventory_slot_modifier, ":imod", "trp_player", ":inv_slot"),
            (eq, ":imod", 0), #Native troop items never have modifiers
            
            (troop_set_inventory_slot, "trp_player", ":inv_slot", -1),
            (str_store_item_name, s3, ":item"),
            (str_store_string, s2, "@{s3}, {s2}"),
            
            (assign, ":end", 0), #Break
        (try_end), #Player Inventory Loop
    (try_end), #Item Given Slot Loop

    (set_show_messages, 1),
    (try_begin),
        (neg|str_is_empty, s2),
        (party_set_slot, "p_freelancer_party_backup", slot_freelancer_equip_start - 1, 0),    #Reset Number of Items Added
        (str_store_troop_name, s1, ":source_troop"),
        (display_message, "@The equipment of a {s1}: {s2}is taken from you."),
    (try_end),    
    (troop_equip_items, "trp_player"),
   ]), 
   
####################################################################################################################
   
####### NEW v3.0-KOMKE START-   
####### INPUT: arg1: enlistment division: grc_cavalry, grc_archers, grc_infantry
####### OUTPUT: troops in reg1, reg2, reg3 belonging to chosen division. Returns troops with level <= player level
####### NOTES: returns only first 3 valid troops.
  ("freelancer_find_enlist_troops",
  [
    (store_script_param_1, ":division"), 
    (assign, reg51, 0),## Initialize every time so it returns 0 if no troop assigned to that register
    (assign, reg52, 0),
    (assign, reg53, 0),
    (store_character_level, ":player_level", "trp_player"),
    (try_begin),
        (lt, ":player_level", 7),
        (assign, ":player_level", 7),##this way player can start from level 1
    (try_end),
    (troop_get_slot, ":freelancer_culture", "$g_talk_troop", slot_troop_cur_culture),## get lord culture
    (try_begin),
        (neg|is_between, ":freelancer_culture", cultures_begin, cultures_end),## not proper cultures
        (faction_get_slot, ":freelancer_culture", "$g_talk_troop_faction", slot_faction_culture), ## if not proper culture get faction culture
    (else_try),
        (eq, ":freelancer_culture", "fac_culture_player"),## fac_culture_player is custom troops culture included in cultures range
        (faction_get_slot, ":freelancer_culture", "$g_talk_troop_faction", slot_faction_culture), ## if player culture culture get faction culture
    (try_end),
    (try_for_range, ":cur_troop", regulars_begin, regulars_end),
        (troop_get_slot, ":cur_culture", ":cur_troop", slot_troop_culture),
        (eq, ":cur_culture", ":freelancer_culture"),## only troops with culture = freelancer culture
        (store_character_level, ":cur_level", ":cur_troop"),
        (ge, ":player_level", ":cur_level"),## only troops with level <= player level
        (try_begin),
            (eq, ":division", grc_cavalry),
            (troop_is_guarantee_horse, ":cur_troop"),
            (call_script, "script_freelancer_get_highest_values", ":cur_troop"),
        (else_try),
            (eq, ":division", grc_archers),
            (neg|troop_is_guarantee_horse, ":cur_troop"),
            (troop_is_guarantee_ranged, ":cur_troop"),
            (call_script, "script_freelancer_get_highest_values", ":cur_troop"),
        (else_try),
            (eq, ":division", grc_infantry),
            (neg|troop_is_guarantee_horse, ":cur_troop"),
            (neg|troop_is_guarantee_ranged, ":cur_troop"),                
            (call_script, "script_freelancer_get_highest_values", ":cur_troop"),
        (try_end),
    (try_end),
  ]),    
  
####################################################################################################################
   
####### INPUT: arg1: troop number to be compared with reg51, reg52, reg53
####### OUTPUT: none, the 3 highest values from the 4 are stored in the registers
####### NOTES: the lowest value is lost
  ("freelancer_get_highest_values",
  [
    (store_script_param_1, ":number"),
    (assign, ":aux1", 0),
    (assign, ":aux2", 0),
    (try_begin),
        (gt, ":number", reg51),
        (assign, ":aux1", reg51),
        (assign, reg51, ":number"),
    (else_try),
        (gt, ":number", reg52),
        (assign, ":aux1", reg52),
        (assign, reg52, ":number"),
    (else_try),
        (gt, ":number", reg53),
        (assign, ":aux1", reg53),
        (assign, reg53, ":number"),
    (try_end),
    (try_begin),
        (gt, ":aux1", reg51),
        (assign, ":aux2", reg51),
        (assign, reg51, ":aux1"),
    (else_try),
        (gt, ":aux1", reg52),
        (assign, ":aux2", reg52),
        (assign, reg52, ":aux1"),
    (else_try),
        (gt, ":aux1", reg53),
        (assign, ":aux2", reg53),
        (assign, reg53, ":aux1"),
    (try_end),
    (try_begin),
        (gt, ":aux2", reg51),
        (assign, reg51, ":aux2"),
    (else_try),
        (gt, ":aux2", reg52),
        (assign, reg52, ":aux2"),
    (else_try),
        (gt, ":aux2", reg53),
        (assign, reg53, ":aux2"),
    (try_end),
   ]),    
 
####### NEW v3.0-KOMKE END-   

####################################################################################################################
   
#+freelancer end

]


from util_wrappers import *
from util_scripts import *

scripts_directives = [
    # [SD_OP_BLOCK_INSERT, "agent_reassign_team", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,(party_stack_get_troop_id, ":leader_troop_id", ":party_no", 0),0,not_in_party], ### NEW v1.0 - this is removed because the line in the script is commented in dickplo
    [SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(assign, "$g_player_luck", 200),0,
    [
        (assign, "$freelancer_state", 0),
    ]],
    [SD_OP_BLOCK_INSERT, "encounter_init_variables", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (gt, "$g_starting_strength_friends", 0),0,
    [
        #(try_begin), #in the script 
              (eq, "$freelancer_state", 1),
            (store_character_level, "$g_strength_contribution_of_player", "$player_cur_troop"),
            (val_div, "$g_strength_contribution_of_player", 3),
            (val_max, "$g_strength_contribution_of_player", 3), #contribution(scale 0-100) = level/3, min 3 (so about 3-15)
            #(store_character_level, ":freelancer_player_contribution", "$player_cur_troop"),
            #(val_mul, ":freelancer_player_contribution", 6),
            #(val_div, ":freelancer_player_contribution", 5), #level * 1.2 (for a bit of a scaling bump)
            #(val_max, ":freelancer_player_contribution", 10), #and to give a base line
            #(assign, "$g_strength_contribution_of_player", ":freelancer_player_contribution"),
        (else_try),            
    ]],
    [SD_OP_BLOCK_INSERT, "enter_court", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),0,
    [
        (gt, ":stack_troop", 0), #fixes duplicate players in towns
    ]],    
    [SD_OP_BLOCK_INSERT, "game_event_simulate_battle", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(troop_is_hero, ":cur_troop_id"),0,
    [
        (gt, ":cur_troop_id", 0), #fixes problems with player getting added as prisoner
    ]],    
    [SD_OP_BLOCK_INSERT, "abort_quest", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_AFTER,0,0, ##ADD TO END
    [
        (try_begin),
            (is_between, ":quest_no", freelancer_quests_begin, freelancer_quests_end),
            (str_store_troop_name, s13, "$enlisted_lord"),
            (dialog_box, "@You have deserted from the party of {s13}!", "@Notice!"),
            (call_script, "script_freelancer_event_player_deserts"),
        (try_end),
    ]],    
    [SD_OP_BLOCK_REPLACE, "change_troop_faction", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE,(call_script, "script_abort_quest", ":quest", 0),0,
    [
        (try_begin), #prevents cancelling freelancer quests on defection/indictment
            (eq, ":quest", "qst_freelancer_enlisted"), #only do necessary Freelancer stuff once
            (str_store_troop_name, s5, "$player_cur_troop"),    
            (str_store_troop_name_link, s13, "$enlisted_lord"),
            (str_store_faction_name_link, s14, ":faction_no"),
            (str_store_string, s1, "@Enlisted as a {s5} in the party of {s13} of {s14}."),
            (add_troop_note_from_sreg, "trp_player", 3, s1, 0),
            #set faction relations to allow player to join battles
            (try_begin),
                (store_relation, ":player_relation", ":faction_no", "$players_kingdom"),
                (lt, ":player_relation", 10),
                (call_script, "script_set_player_relation_with_faction", ":faction_no", 10),
            (try_end),
            (try_for_range, ":cur_faction", npc_kingdoms_begin, kingdoms_end),####### NEW v3.0-KOMKE npc_kingdoms_begin instead of kingdoms_begin
               (neq, ":faction_no", ":cur_faction"),
               # (neq, "$players_kingdom", ":cur_faction"),####### NEW v2.9-KOMKE don't change relation with player's kingdom
               (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
               (store_relation, ":player_relation", ":cur_faction", "$players_kingdom"),
               (ge, ":player_relation", 0),
               (call_script, "script_set_player_relation_with_faction", ":cur_faction", -5),
            (try_end),            
        (else_try),
            (neg|is_between, ":quest", freelancer_quests_begin, freelancer_quests_end),
            (call_script, "script_abort_quest", ":quest", 0), ##Natively in the script
        (try_end),
    ]],
    ##FLORIS ONLY - Trade with Merchant Caravans
    [SD_OP_BLOCK_INSERT, "party_give_xp_and_gold", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (party_slot_eq, ":enemy_party", slot_party_type, spt_kingdom_caravan),0,not_in_party],    
    ##FLORIS ONLY END    
]
                
def modmerge_scripts(orig_scripts):
    # process script directives first
    process_script_directives(orig_scripts, scripts_directives)
    # add remaining scripts
    add_scripts(orig_scripts, scripts, True)
    
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
        # START do your own stuff to do merging
        
        modmerge_scripts(orig_scripts)

        # END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)