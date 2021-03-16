
#=#######################################
# Lumos: This file contains all the scripts for the Outposts kit.
#        You have to place them in your module_scripts.
#-#######################################

# WHERE TO PUT THIS:
# In the "game_event_party_encounter" script.
# ATTENTION: Copy only the stuff between "Outposts begin" and "Outposts end"
# The rest of the code is just to help you in locating the script's place

from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_items import *
from header_terrain_types import *
from header_mission_templates import *


# start of snippet
thing = [
           (try_begin),
             (lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
             (try_begin),
               (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
               (jump_to_menu, "mnu_castle_outside"),
             (else_try),
               (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
               (jump_to_menu, "mnu_castle_outside"),
             (else_try),
               (party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
               (jump_to_menu, "mnu_ship_reembark"),
             (else_try),
               (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
               (jump_to_menu, "mnu_village"),
             (else_try),
               (party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
               (jump_to_menu, "mnu_cattle_herd"),
        #-## Outposts begin
           (else_try),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_outpost),
             (jump_to_menu, "mnu_outpost"),
           (else_try),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_fort),
             (jump_to_menu, "mnu_fort"),
        #-## Outposts end
             (else_try),
               (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
               (jump_to_menu, "mnu_training_ground"),
             (else_try),
               (eq, "$g_encountered_party", "p_camp_bandits"),
               (jump_to_menu, "mnu_camp"),
             (else_try),
               (eq, "$g_encountered_party", "p_zendar"),
               (jump_to_menu, "mnu_zendar"),
             (else_try),
               (eq, "$g_encountered_party", "p_salt_mine"),
               (jump_to_menu, "mnu_salt_mine"),
             (else_try),

# end of snippet
]

# WHERE TO PUT THIS:
# At the end is good.

scripts = [
#-## Outposts begin
   ("setup_outpost_scene",
    [
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (assign, ":scene_to_use", "scn_outpost_one_two_plain"),
      (try_begin),
        # (eq, ":terrain_type", rt_steppe),
        # (assign, ":scene_to_use", "scn_outpost_one_two_steppe"),
      (else_try),
        # (eq, ":terrain_type", rt_plain),
        # (assign, ":scene_to_use", "scn_outpost_one_one_plain"),
      (else_try),
        (eq, ":terrain_type", rt_snow),
        (assign, ":scene_to_use", "scn_outpost_one_two_snow"),
      (else_try),
        # (eq, ":terrain_type", rt_desert),
        # (assign, ":scene_to_use", "scn_outpost_one_one_desert"),#scn_outpost_scene_desert
      (else_try),
        # (eq, ":terrain_type", rt_steppe_forest),
        # (assign, ":scene_to_use", "scn_outpost_one_one_steppe_forest"),
      (else_try),
        (eq, ":terrain_type", rt_forest),
        (assign, ":scene_to_use", "scn_outpost_one_two_forest"),
      (else_try),
        (eq, ":terrain_type", rt_snow_forest),
        (assign, ":scene_to_use", "scn_outpost_one_two_snow_forest"),
      (else_try),
        # (eq, ":terrain_type", rt_desert_forest),
        # (assign, ":scene_to_use", "scn_outpost_one_one_desert_forest"),
      (try_end),
	  (try_begin),
	    (neq, ":scene_to_use", "scn_random_scene"),
	    (eq, "$g_encountered_party", "p_outpost_2"),
		(val_add, ":scene_to_use", 4),
	  (try_end),
	  (try_begin),
	    (neq, ":scene_to_use", "scn_random_scene"),
	    (party_slot_eq, "$g_encountered_party", slot_outpost_level, 2),
		(val_add, ":scene_to_use", 4),
	  (try_end),
      (assign, reg1, ":scene_to_use"),
      (jump_to_scene,":scene_to_use"),
  ]),
 
  ("setup_fort_scene",
    [
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (assign, ":scene_to_use", "scn_fort"),
      (try_begin), # Lumos: Not all terrains have unique scenes yet
        (eq, ":terrain_type", rt_snow),
        (assign, ":scene_to_use", "scn_fort_snow"),
      (else_try),
        (eq, ":terrain_type", rt_forest),
        (assign, ":scene_to_use", "scn_fort_forest"),
      (try_end),
      (assign, reg1, ":scene_to_use"),
  ]),

  # script_set_walker_to_type
  # Input: arg1 = walker_id, arg2 = troop_id
  # Output: none
  ("set_walker_to_type",
   [
       (store_script_param, ":walker_id", 1),
       (store_script_param, ":troop_id", 2),
       # transfer items
       (try_for_range,":item_no",horses_end,ranged_weapons_end),
          (store_item_kind_count,":num_items",":item_no",":walker_id"),
          (ge,":num_items",1),
          (troop_remove_items,":walker_id",":item_no",":num_items"),
       (try_end),
       (try_for_range,":item_no",horses_end,ranged_weapons_end),
          (store_item_kind_count,":num_items",":item_no",":troop_id"),
          (ge,":num_items",1),
          (store_item_kind_count,":num_items",":item_no",":walker_id"),
          (lt,":num_items",1),
          (troop_add_items,":walker_id",":item_no",1),
       (try_end),
       (troop_equip_items,":walker_id"),
     ]),

  # script_init_fort_patrols
  # Input: none
  # Output: none
  ("init_fort_patrols",
    [
     (try_for_agents, ":cur_agent"),
       (agent_get_troop_id, ":cur_troop", ":cur_agent"),
       (agent_get_entry_no, ":entry_no", ":cur_agent"),
       (try_begin),
         (eq, ":cur_troop", "trp_ee_watchman"),
         (entry_point_get_position, pos1, ":entry_no"),
         (agent_set_position, ":cur_agent", pos1),        # force agents into the proper spot to prevent wonkyness
         (val_add, ":entry_no", 1),
         (agent_set_slot, ":cur_agent", 0, ":entry_no"),
         (entry_point_get_position, pos2, ":entry_no"),
         
         (agent_set_speed_limit, ":cur_agent", 1),
         (agent_set_scripted_destination, ":cur_agent", pos2, 0),
       (else_try),
         (this_or_next|eq, ":cur_troop", "trp_fort_rider"),
         (eq, ":entry_no", 20),
         (agent_is_human, ":cur_agent"),
         (call_script, "script_init_mounted_patrol", ":cur_agent"),
       (try_end),
     (try_end),
  ]),
  
  # script_init_mounted_patrol
  # Input: arg1 = agent number
  # Output: none
  ("init_mounted_patrol",
    [
       (store_script_param, ":cur_agent", 1),
       (agent_get_entry_no, ":entry_no", ":cur_agent"),
       (agent_set_stand_animation, ":cur_agent", "anim_ride_0"),
       (agent_set_walk_forward_animation, ":cur_agent", "anim_ride_1"),
       (agent_set_animation, ":cur_agent", "anim_ride_0"),
       (agent_set_animation_progress, ":cur_agent", 10),
       
       (store_add, ":target_entry_point", ":entry_no", 1),
       (entry_point_get_position, pos1, ":target_entry_point"),
       (agent_set_slot, ":cur_agent", 0, ":target_entry_point"),
       (agent_set_speed_limit, ":cur_agent", mount_patrol_max_speed),
       (agent_set_scripted_destination, ":cur_agent", pos1, 0),
       
  ]),
  
  # script_tick_fort_patrol
  # Input: arg1 = agent_id, arg2 = number of way points
  # Output: none
  ("cf_tick_fort_patrol",
    [
     (store_script_param, ":agent_id", 1),
     (store_script_param, ":num_points", 2),
     
     (agent_get_entry_no, ":entry_no", ":agent_id"),
     (agent_get_slot, ":target_entry_point", ":agent_id", 0),
     (agent_get_class, ":agent_class", ":agent_id"),
     (entry_point_get_position, pos1, ":target_entry_point"),
     (agent_get_position, pos2, ":agent_id"),
     (get_distance_between_positions, ":distance", pos1, pos2),
     (try_begin),
       (eq, ":agent_class", grc_cavalry),
       (lt, ":distance", mount_patrol_closing_dist),
       (store_sub, ":speed_adjust", mount_patrol_closing_dist, ":distance"),
       (val_mul, ":speed_adjust", 100),
       (val_div, ":speed_adjust", mount_patrol_closing_dist),
       (store_sub, ":speed_limit", mount_patrol_max_speed, mount_patrol_min_speed),
       (val_mul, ":speed_limit", -1),
       (val_mul, ":speed_adjust", ":speed_limit"),
       (val_div, ":speed_adjust", 100),
       (val_add, ":speed_adjust", mount_patrol_max_speed), # maxspeed - 10*(6000-dist)/6000 scales from max to min speed as we close to destination
       (agent_set_speed_limit, ":agent_id", ":speed_adjust"), # once agent is within closing distance, it scales down from max speed to min speed as it reaches target
       (assign, reg3, ":agent_id"),
       (assign, reg4, ":speed_adjust"),
       #(display_message, "@Agent #{reg3} reducing max speed to {reg4}."),
     (try_end),
     (lt, ":distance", 400),
     (store_random_in_range, ":random_no", 0, 100),
     (lt, ":random_no", 20),
     (store_add, ":max_point", ":entry_no", ":num_points"),
     (val_add, ":target_entry_point", 1),
     (try_begin),
       (gt, ":target_entry_point", ":max_point"),
       (assign, ":target_entry_point", ":entry_no"),
     (try_end),
     (try_begin),
       (eq, ":agent_class", grc_cavalry),
       (agent_set_speed_limit, ":agent_id", 15),
     (try_end),
     (entry_point_get_position, pos1, ":target_entry_point"),
     (agent_set_slot, ":agent_id", 0, ":target_entry_point"),
     (agent_set_scripted_destination, ":agent_id", pos1, 0),
  ]),
 #-## Outposts end
]


from util_wrappers import *
from util_scripts import *
 
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        
        #swy--append the rest of scripts at the end
        orig_scripts = var_set[var_name_1]
        orig_scripts.extend(scripts) 
        
        
        #swy--inject the fort and outpost encounter hooks after the cattle conditions
        scripts_directives = [
          [
            SD_OP_BLOCK_INSERT,
            "game_event_party_encounter",
            D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,
            
            (jump_to_menu, "mnu_cattle_herd"), 0,
            
            [    #-## Outposts begin
                 (else_try),
                       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_outpost),
                       (jump_to_menu, "mnu_outpost"),
                 (else_try),
                       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_fort),
                 (jump_to_menu, "mnu_fort"),
              #-## Outposts end
            ]
          ]
        ]
        
        process_script_directives(orig_scripts, scripts_directives)
        
        
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)