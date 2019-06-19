from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from header_skills import *
from module_constants import *

from compiler import *
# This is where the scripts themsleves are at. Modify to your liking, but remember to read the comments first to get an idea of what it is you're changing. ;)


#To use the custom triggers in a mission template simply choose the ones you want from the list below (for example "dismemberment_mod_decap," without the ") and insert that piece of text (not the whole trigger, but you can do that too!) somewhere among that mission's other triggers. Just make sure it's not inside another one, but between the existing ones and/or the script block markers).

# Paste all of the text below this line just above the "multiplayer_server_check_belfry_movement = (" -line in your "module_mission_templates.py". 
#_________________



### Dismemberment Mod Kit Commons ### 

# List of commons:
# 
# dismemberment_mod_decap,
# dismemberment_mod_hands1,
# dismemberment_mod_hands2,
# dismemberment_mod_arms1,
# dismemberment_mod_arms2,
# dismemberment_mod_hotkeys,


### Commons start ###


###_______________________________________________________________________________________
###
### Dismemberment mod: Decapitations
###

dismemberment_mod_decap = (

# Trigger Param 1: damage inflicted agent_id
# Trigger Param 2: damage dealer agent_id
# Trigger Param 3: inflicted damage
# Register 0: damage dealer item_id
# Position Register 0: position of the blow rotation gives the direction of the blow

ti_on_agent_hit, 0, 0, [(eq, "$g_decap_enabled", 1),],
[
   (store_trigger_param_1, ":victim_agent"),
   (store_trigger_param_2, ":attacker_agent"),
   (store_trigger_param_3, ":damage"),
   
   (agent_is_non_player, ":victim_agent"),  ######## NEW v3.0 - fixes player being decapitated
   ######## NEW v3.0 - fixes heroes being decapitated
   (agent_get_troop_id, ":troop_id", ":victim_agent"),  
   (neg|troop_is_hero, ":troop_id"),  
   ################ 
		  
   (assign, ":attacker_item", reg0), ### Transfer the item ID to make sure it dosn't change while the script is running
   (copy_position, pos5, pos0), ### Transfer the position of the hit to make sure it dosn't change while the script is running
   
   (neq, ":victim_agent", -1),
   
   (try_begin), #-- Decapitations --#
      (agent_is_human, ":victim_agent"),
	  (ge, ":attacker_item", 0),
	  
	  
	  (assign, ":run", 0), ### Reset the run test variable
	  (try_begin), ### Special weapons that can decap, ovevrrides the below conditions
		  (this_or_next|eq, ":attacker_item", "itm_supercrossbow"),
		  (eq, ":attacker_item", "itm_supersledge"),
		  (assign, ":run", 1),
	  (else_try),
		  (neq, ":attacker_item", "itm_mace_1"), ### List of weapons that cannot decapitate
		  (neq, ":attacker_item", "itm_mace_2"), ### This would be easier to do with a preperty check (for damage type), but I don't know if that is possible or not
		  (neq, ":attacker_item", "itm_mace_3"),
		  (neq, ":attacker_item", "itm_staff"),
		  
		  (agent_get_action_dir, ":attack_dir", ":attacker_agent"), ### Makes sure the attack is either a left or right swing
		  (this_or_next|eq, ":attack_dir", 1), ### Right swing
		  (eq, ":attack_dir", 2), ### Left swing
		  (assign, ":run", 1),
	  (try_end),
	  (eq, ":run", 1), ### One of the checks were true, continue to run script
	  
	  
	  #(assign, reg1, ":damage"), #Debug messages
	  #(display_message, "@Damage: {reg1}"),
	  
	  (assign, ":run", 0), ### Reset the run test variable
	  (try_begin),
		(ge, ":damage", "$g_decap_minimum_damage"), ### Minimum damage required to decapitate an agent
		(assign, ":run", 1),
		
	  (else_try),  ### If debugging mode is on, this bypasses the damage requirement check
		  (eq,"$g_decapitations_debugging", 1),
		  (assign, ":run", 1),
		  (display_message, "@Decap minimum DMG req bypassed"),
	  (try_end),
	  (eq, ":run", 1),
	  
	  (store_agent_hit_points, ":hp", ":victim_agent", 1),
	  (val_add, ":hp", "$g_decap_negative_health"), ### Victim must have the negative of this hp or below after hit for the script to move on (never put this value below 0 since the agent has to be absolutley positvely dead)!
	  (ge, ":damage", ":hp"),
	  
	  
	  ### Compare the hit position to the agent's position
      (agent_get_position, pos4, ":victim_agent"),
      (get_distance_between_positions, ":distance", pos4, pos5), 
	  (agent_get_horse, ":is_mounted", ":victim_agent"),
	  (try_begin), ### If the agent is on horseback, these values are used (note that these values will not be exactly correct if the horse is very large or very small)
		(ge, ":is_mounted", 0), ### Will be -1 if no horse is to be found, so anything above means that the agent is mounted
		(assign, ":min_distance", 240), ### Minimum distance from the agent's horse's hooves from which the hit is valid (240 is an approximate value)
		(assign, ":max_distance", 260), ### Maximum distance from the agent's horse's hooves to which the hit is valid (260 is an approximate value)
	  (else_try),  ### If the agent is on foot, these values are used
	    (assign, ":min_distance", 160), ### Minimum distance from the agent's feet from which the hit is valid (160 = slightly below the neck)
	    (assign, ":max_distance", 176), ### Maximum distance from the agent's feet to which the hit is valid (176 = near the nose)
	  (try_end),
      (is_between, ":distance", ":min_distance", ":max_distance"), ### Check to see if the hit is within the allowed area
	  
	  
	  (assign, ":run", 0), ### Default variable value before damage test
	  (try_begin),
		  # (store_div, ":chance", ":damage", 4), ### Chance of decap is damage / 4 right now. Lower this value for higher chances of decapitation (or press M+Right Ctrl for debug more if you just want to test easy decaps in-game).
		  # (store_div, ":chance", ":damage", 2), 
		  
		  #(assign, reg1, ":chance"), #Debug messages
		  #(display_message, "@Decap chance is: {reg1}"),
		  (store_random_in_range, ":diceroll", 0, 100), ### Randomizer, 0-100
		  
		  #(assign, reg1, ":diceroll"), #Debug messages
		  #(display_message, "@Diceroll: {reg1}"),
		  (le, ":diceroll", "$g_decap_chance"), ### ":diceroll" must be less than or equal to ":chance", if it is, decapitation occurs!
		  
		  (assign, ":run", 1), ### SUCCESS!
		  
      (else_try),  ### If debugging mode is on, bypass chance calculation
		  (eq,"$g_decapitations_debugging", 1),
		  (assign, ":run", 1),
		  (display_message, "@Decap chance calc bypassed"),
	  (try_end),  
	  (eq, ":run", 1), ### Time for the fun stuff!

	  ### Gender test for spawning the right head type
	  (assign, ":head_type", "itm_cut_off_head_male"),
	  (agent_get_troop_id, ":victim_troop", ":victim_agent"),
	  (try_begin),
	    (ge, ":victim_troop", 0),
		(troop_get_type,":victim_gender",":victim_troop"),
		(eq, ":victim_gender", 1),
		(assign, ":head_type", "itm_cut_off_head_female"),
	  (try_end),
	  
	  ### Randomize the spawned head's and/or helmet's position and orientation
	  (store_random_in_range, ":z_rotation", 0, 360),
	  (store_random_in_range, ":y_rotation", -60, 60),
	  (store_random_in_range, ":x_pos", -90, 90),
	  (store_random_in_range, ":y_pos", -90, 90),
	  (position_rotate_z, pos4,":z_rotation"),
	  (position_rotate_y, pos4,":y_rotation"),
	  (position_move_x, pos4, ":x_pos"),
	  (position_move_y, pos4, ":y_pos"),
	  (position_set_z_to_ground_level, pos4),
	  (position_move_z, pos4, 5),
	  (set_spawn_position, pos4),
	  (assign, ":prunetime", 360), ### This is the time in seconds before the spawned head or helmet gets pruned (removed). Recommended to keep it above 0 to make sure it gets removed eventually or when the scene resets, to prevent performance issues.
	  
	  #(spawn_item, ":head_type", 0, ":prunetime"), ### This is the old way of spawning the head on the ground with the helmet, disabled because of the new dynamic heads. You can comment away (disable) the dynamic heads spawning further down and uncomment this line for a less performance-needing approach (with no physics involved).
	  
	  ### Does the agent have a helmet or hat equipped?
      (agent_get_item_slot, ":item", ":victim_agent", 4), #head slot
      (try_begin),
         (ge, ":item", 1), ### Does it?
         (agent_unequip_item, ":victim_agent", ":item"), ### Yes it does. Unequip it to allow replacement by the invisible helmet further down
		 (try_begin),
			 ### Don't spawn items with "itp_attatch_armature" flag: rigging causes floating bugs
			 ### This would be much better to do with an item flag check, but I haven't found any way to do that
			 #(neq, ":item", "itm_with_itp_attatch_armature"),
			 #(neg|is_between,":item","start_of_itm_range_with_itp_attatch_armature","end_of_itm_range_with_itp_attatch_armature"),
			#(set_spawn_position, pos4),
			(spawn_item, ":item", 0, ":prunetime"), ### Spawns the agent's currently equipped headgear on the dropped head's position
		 (try_end),
      (try_end),
	  
	  (agent_equip_item, ":victim_agent", "itm_invisible_head"), ### Put an invisible helmet on the agent's head to "remove" it
	  
	  
	  (agent_get_position, pos4, ":victim_agent"), ### Refreshes the agent's position
	  (position_move_z, pos4, ":min_distance"), ### Move to the where the neck used to be attached
	  
	  
	  ### Blood effects! The last variable is the strength. Lower or increase it for more/less blood (or tweak the particle effects themselves in "module_particle_systems.py").
      (particle_system_burst, "psys_blood_decapitation", pos4, "$g_decap_psys_blood_decapitation"), 
	  (particle_system_burst, "psys_game_blood", pos4, "$g_decap_psys_game_blood"),
	  (particle_system_burst, "psys_game_blood_2", pos4, "$g_decap_psys_game_blood_2"),
	  
	  (play_sound_at_position, "snd_decapitation", pos4), ### Play some nasty sounds
	  
	  
	  ### Dynamic head spawning! See the bottom of "module_scene_props.py" for physics-related options and more.
	  (position_move_z, pos4, 20),
	  (set_spawn_position, pos4),
	  (assign, ":head_type", "spr_head_dynamic_male"),
	  (try_begin), ### Gender check (for determening the type of head)
		(eq, ":victim_gender", 1),
		(assign, ":head_type", "spr_head_dynamic_female"),
	  (try_end),
	  (spawn_scene_prop, ":head_type"),
	  
	  

	  ### This below is for the text that shows up when somebody is decapitated.
	  
	  ### Who decapitated who?
		(agent_get_troop_id, ":attacker_troop", ":attacker_agent"),
		(str_store_troop_name, s0, ":attacker_troop"),

		(agent_get_troop_id, ":victim_troop", ":victim_agent"),
		(str_store_troop_name, s1, ":victim_troop"),

	  
	  ### Colour check (friend or foe?)
	  (get_player_agent_no, ":my_agent"),
	  (agent_get_team, ":my_team", ":my_agent"),
	  (agent_get_team, ":victim_team", ":victim_agent"),
	  (try_begin), ### Display it!
		  (neq, ":my_team", ":victim_team"),
		  (display_message, "@>>> {s0} decapitated {s1}!", 0xFF33DD11), ## Green
	  (else_try),
		  (display_message, "@>>> {s0} decapitated {s1}!", 0xFFFF4422), ## Red
	  (try_end),
   (try_end), #-- Decapitations END --#
   
   ])

   
###_______________________________________________________________________________________
###
### Dismemberment mod: Handchops
###


dismemberment_mod_hands1 = (

      #Dismemberment of Hands
1, 0, 0, [
      (eq, "$g_dismemberment_enabled", 1),
      (store_mission_timer_a,":cur_time"),
      (ge, ":cur_time", 5), #this gives them time to make sure they equip their 'shield
], [
   (try_for_agents, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
   
      (agent_get_troop_id, ":troop", ":cur_agent"),
      (eq, ":troop", "trp_looter_bully_handless"), #make sure this is the name of the troop
   
      (agent_get_wielded_item,":item",":cur_agent",1),
      (neq, ":item", "itm_severedhand"), #make sure this is the name of the item (their arm)
      (store_agent_hit_points, ":hp", ":cur_agent", 0), #percent
      (val_mul, ":hp", 8), #get 40% of original hp
      (val_div, ":hp", 7), #change if you want
      (agent_set_hit_points, ":cur_agent", ":hp", 0), #again, 0 param = relative
      (get_player_agent_no, ":player"),
      (agent_deliver_damage_to_agent, ":player", ":cur_agent", 1), #param 1 = deal dmg with weapon - usually insta-kills
      #you can make a new agent called "Bleeding" equipped with a 1-dmg wpn and use that instead of the player agent
      (agent_get_position, pos1, ":cur_agent"),
      (position_move_z, pos1, 85), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -32), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, 16), #makes the blood come out severed stump
         (position_rotate_x, pos1, -70), #makes the blood spurt downwards 
         (particle_system_burst, "psys_game_blood_2", pos1, 80), #100 as power.
      (agent_set_animation, ":cur_agent", "anim_handchop"),
   (try_end),
   
   ])

#-----------------------------------------------------------

dismemberment_mod_hands2 = (

1, 0, 0, [
      (eq, "$g_dismemberment_enabled", 1),
      (store_mission_timer_a,":cur_time"),
      (ge, ":cur_time", 5), #this gives them time to make sure they equip their 'shield
], [
   (try_for_agents, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
   
      (agent_get_troop_id, ":troop", ":cur_agent"),
      (eq, ":troop", "trp_fat_peasant_handless"), #make sure this is the name of the troop
   
      (agent_get_wielded_item,":item",":cur_agent",1),
      (neq, ":item", "itm_severedhand"), #make sure this is the name of the item (their arm)
      (store_agent_hit_points, ":hp", ":cur_agent", 0), #percent
      (val_mul, ":hp", 8), #get 40% of original hp
      (val_div, ":hp", 7), #change if you want
      (agent_set_hit_points, ":cur_agent", ":hp", 0), #again, 0 param = relative
      (get_player_agent_no, ":player"),
      (agent_deliver_damage_to_agent, ":player", ":cur_agent", 1), #param 1 = deal dmg with weapon - usually insta-kills
      #you can make a new agent called "Bleeding" equipped with a 1-dmg wpn and use that instead of the player agent
      (agent_get_position, pos1, ":cur_agent"),
      (position_move_z, pos1, 85), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -32), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, 16), #makes the blood come out severed stump
         (position_rotate_x, pos1, -70), #makes the blood spurt downwards 
         (particle_system_burst, "psys_game_blood_2", pos1, 80), #100 as power.
      (agent_set_animation, ":cur_agent", "anim_handchop"),
   (try_end),
   
   ])
   
#-----------------------------------------------------------       


###_______________________________________________________________________________________
###
### Dismemberment mod: Armchops
###


dismemberment_mod_arms1 = (

#Dismemberment of Arms
1, 0, 0, [
      (eq, "$g_dismemberment_enabled", 1),
      (store_mission_timer_a,":cur_time"),
      (ge, ":cur_time", 5), #this gives them time to make sure they equip their 'shield
], [
   (try_for_agents, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
   
      (agent_get_troop_id, ":troop", ":cur_agent"),
      (eq, ":troop", "trp_looter_thug_armless"), #make sure this is the name of the troop
   
      (agent_get_wielded_item,":item",":cur_agent",1),
      (neq, ":item", "itm_fatseveredarm"), #make sure this is the name of the item (their arm)
      (store_agent_hit_points, ":hp", ":cur_agent", 0), #percent
      (val_mul, ":hp", 6), #get 40% of original hp
      (val_div, ":hp", 7), #change if you want
      (agent_set_hit_points, ":cur_agent", ":hp", 0), #again, 0 param = relative
      (get_player_agent_no, ":player"),
      (agent_deliver_damage_to_agent, ":player", ":cur_agent", 1), #param 1 = deal dmg with weapon - usually insta-kills
      #you can make a new agent called "Bleeding" equipped with a 1-dmg wpn and use that instead of the player agent
      (agent_get_position, pos1, ":cur_agent"),
      (position_move_z, pos1, 103), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -35), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, -10), #makes the blood come out severed stump
         (position_rotate_x, pos1, -90), #makes the blood spurt downwards 
         (particle_system_burst, "psys_game_blood_2", pos1, 100), #100 as power.
         (agent_set_animation, ":cur_agent", "anim_armchop"),
   (try_end),
   
   ])

#------------------------------------------------------------


dismemberment_mod_arms2 = (

1, 0, 0, [
      (eq, "$g_dismemberment_enabled", 1),
      (store_mission_timer_a,":cur_time"),
      (ge, ":cur_time", 5), #this gives them time to make sure they equip their 'shield
], [
   (try_for_agents, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
   
      (agent_get_troop_id, ":troop", ":cur_agent"),
      (eq, ":troop", "trp_thin_looter_armless"), #make sure this is the name of the troop
   
      (agent_get_wielded_item,":item",":cur_agent",1),
      (neq, ":item", "itm_severedarm"), #make sure this is the name of the item (their arm)
      (store_agent_hit_points, ":hp", ":cur_agent", 0), #percent
      (val_mul, ":hp", 6), #get 40% of original hp
      (val_div, ":hp", 7), #change if you want
      (agent_set_hit_points, ":cur_agent", ":hp", 0), #again, 0 param = relative
      (get_player_agent_no, ":player"),
      (agent_deliver_damage_to_agent, ":player", ":cur_agent", 1), #param 1 = deal dmg with weapon - usually insta-kills
      #you can make a new agent called "Bleeding" equipped with a 1-dmg wpn and use that instead of the player agent
      (agent_get_position, pos1, ":cur_agent"),
      (position_move_z, pos1, 103), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -35), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, -10), #makes the blood come out severed stump
         (position_rotate_x, pos1, -90), #makes the blood spurt downwards 
         (particle_system_burst, "psys_game_blood_2", pos1, 100), #100 as power.
         (agent_set_animation, ":cur_agent", "anim_armchop"),
   (try_end),
   
   ])
#------------------------------------------------------------
      
#END Arm Dismemberment    


###_______________________________________________________________________________________
###
### Dismemberment mod: Hotkeys
###

dismemberment_mod_hotkeys = (

	0, 0, 1, [(key_clicked, key_right_control)],
  [
   (try_begin), ### Deug mode on/off
		(key_is_down, key_m),
		(try_begin),
			(eq, "$g_decapitations_debugging", 0),
			(assign, "$g_decapitations_debugging", 1),
			(display_message, "@Decapitation debug mode Enabled"),
		(else_try),
			(assign, "$g_decapitations_debugging", 0),
			(display_message, "@Decapitation debug mode Disabled"),
		(try_end),
	(try_end),
	
	(try_begin), ### Spawn dismemeberable enemies
		(key_is_down, key_k),
		
		(get_player_agent_no, ":player_agent"),
		(agent_get_position, pos17, ":player_agent"),
		
		(position_move_y, pos17, 2000),
		
		(position_set_z_to_ground_level, pos17),
		(set_spawn_position, pos17),
		(spawn_agent, "trp_looter_bully_handless"),
		(agent_set_team, reg0, 2),
		
		(position_move_y, pos17, 100),
		(position_set_z_to_ground_level, pos17),
		(set_spawn_position, pos17),
		(spawn_agent, "trp_looter_thug_armless"),
		(agent_set_team, reg0, 2),
		
		(position_move_y, pos17, 100),
		(position_set_z_to_ground_level, pos17),
		(set_spawn_position, pos17),
		(spawn_agent, "trp_thin_looter_armless"),
		(agent_set_team, reg0, 2),
		
		(position_move_y, pos17, 100),
		(position_set_z_to_ground_level, pos17),
		(set_spawn_position, pos17),
		(spawn_agent, "trp_fat_peasant_handless"),
		(agent_set_team, reg0, 2),
	(try_end),
	
	(try_begin), ### Spawn superweapons
		(key_is_down, key_j),
		
		(get_player_agent_no, ":player_agent"),
		(agent_get_position, pos18, ":player_agent"),
		
		(set_spawn_position, pos18),
		(spawn_item, "itm_supersledge"),
		(position_move_x, pos18, 50),
		(position_set_z_to_ground_level, pos18),
		(set_spawn_position, pos18),
		(spawn_item, "itm_supercrossbow"),
		(position_move_x, pos18, 50),
		(position_set_z_to_ground_level, pos18),
		(set_spawn_position, pos18),
		(spawn_item, "itm_super_bolts"),
	(try_end),
	
   ])


### Dismemberment Mod Kit Commons END ### 
###_______________________________________________________________________________________
###_______________________________________________________________________________________

dismemberment_triggers = [
    dismemberment_mod_decap,
    dismemberment_mod_hands1,
    dismemberment_mod_hands2,
    dismemberment_mod_arms1,
    dismemberment_mod_arms2,
    dismemberment_mod_hotkeys,
  ] 
  
  

from util_common import *
from util_wrappers import *

def modmerge_mission_templates(orig_mission_templates):
# 2) Example of adding trigger groups to several  mt
    for n in range(len(orig_mission_templates)):
      mt_name = orig_mission_templates[n][0]
      if (mt_name=="back_alley_revolt" or mt_name=="lead_charge" or mt_name=="village_attack_bandits" or mt_name=="village_raid" or mt_name=="quick_battle_battle" or mt_name=="quick_battle_siege" or mt_name=="castle_attack_walls_belfry" or mt_name=="castle_attack_walls_ladder" or mt_name=="castle_attack_walls_defenders_sally" or mt_name=="bandits_at_night" or mt_name=="bandit_lair" or mt_name=="town_default" or mt_name=="town_center"): # search for the exact name of the mt
        orig_mission_templates[n][5].extend(dismemberment_triggers)

def modmerge(var_set):
   try:
      var_name_1 = "mission_templates"
      orig_mission_templates = var_set[var_name_1]
      modmerge_mission_templates(orig_mission_templates) # perform search-replace function
      
   except KeyError:
      errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
      raise ValueError(errstring)



