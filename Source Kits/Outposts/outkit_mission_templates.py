#=#######################################
# Lumos: This file contains all the mission templates for the Outposts kit.
#        Place them in module_mission+_templates. At the end is good.
#-#######################################

from header_common import *
from header_operations import *
from header_mission_templates import *
from module_constants import *
from header_music import *
from header_sounds import *

pilgrim_disguise = [itm_pilgrim_hood,itm_pilgrim_disguise,itm_practice_staff, itm_throwing_daggers]


mission_templates = [
#-## Outposts begin
  (
    "fort_visit",0,-1,
    "Fort visit",
    [
     #Player/companions
     (0,mtef_scene_source|mtef_team_0,0,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     
     #Merchants & Guard Captain
     (8,mtef_visitor_source,af_override_horse,0,1,[]),(9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),
     
     #Horses at horse merchant slot
     (13,mtef_visitor_source,0,0,1,[]),
     
     (14,mtef_scene_source,0,0,1,[]),
     
     #These are used for the passages to the tower area
     (15,mtef_visitor_source,af_override_horse,0,1,[]),(16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (19,mtef_visitor_source,af_override_horse,0,1,[]),
     
     #Perimeter patrol entry and waypoints (corners of the map)
     (20,mtef_visitor_source|mtef_team_0,0,0,1,[]),(21,mtef_visitor_source,0,0,1,[]),(22,mtef_visitor_source,0,0,1,[]),(23,mtef_visitor_source,0,0,1,[]),
     
     #Stationary guards
     (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(29,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     
     #Patrol on the central walkway
     (30,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     
     #Walkers
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     
     # Guards & patrols on the front walkways use these slots
     (40,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(43|mtef_team_0,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(47|mtef_team_0,mtef_visitor_source,af_override_horse,aif_start_alarmed,1,[]),
     (48,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),(49,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     
     # Future slots here for enemy starting positions and maybe another cosmetic thing or two, I believe we're allowed up to 60 slots
     ],
    [
      (ti_before_mission_start, 0, 0, [], 
        [
          (call_script, "script_change_banners_and_chest"),
          (call_script, "script_remove_siege_objects"),
          #(scene_prop_disable,"spr_portcullis"),
          #(scene_prop_disable,"spr_ramp_12m"),
        ]),
      (ti_on_agent_spawn, 0, 0, [],
        [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
        ]),
        
      (1, 0, ti_once, [],
        [
           (try_begin),
             (eq, "$g_mt_mode", tcm_default),
             (store_current_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
           (try_end),
           (call_script, "script_init_town_walker_agents"),
           (call_script, "script_init_fort_patrols"),
           #(get_player_agent_no, ":player_agent"),
           #(team_set_leader, 0, ":player_agent"),
           (entry_point_get_position, pos1, 14),
           (scene_prop_get_num_instances, ":num_props", "spr_inventory"),
           (try_for_range, ":instance_no", 0, ":num_props"),	# move the inventory to the central tower
             (scene_prop_get_instance, ":inventory_id", "spr_inventory", ":instance_no"),
             (prop_instance_set_position, ":inventory_id", pos1),
           (try_end),
           (try_begin),
             (eq, "$sneaked_into_town", 1),
             (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
           (else_try),
             (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
           (try_end),
        ]),
      (ti_inventory_key_pressed, 0, 0,
        [
           (try_begin),
             (eq, "$g_mt_mode", tcm_default),
             (set_trigger_result,1),
           (else_try),
             (eq, "$g_mt_mode", tcm_disguised),
             (display_message,"str_cant_use_inventory_disguised"),
           (else_try),
             (display_message, "str_cant_use_inventory_now"),
           (try_end),
        ], []),
        (ti_tab_pressed, 0, 0,
         [
           (try_begin),
             (this_or_next|eq, "$g_mt_mode", tcm_default),
             (eq, "$g_mt_mode", tcm_disguised),
             (set_trigger_result,1),
           (else_try),
             (display_message, "@Cannot leave now."),
           (try_end),
           ], []),
        (ti_on_leave_area, 0, 0,
         [
            (try_begin),
              (eq, "$g_defending_against_siege", 0),
              (assign,"$g_leave_town",1),
            (try_end),
            ], []),

        (0, 0, ti_once, [], 
          [
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (call_script, "script_town_init_doors", 0),
            (try_begin),
              (eq, "$town_nighttime", 0),
              (play_sound, "snd_town_ambiance", sf_looping),
            (try_end),
          ]),
		  
		# Lumos: You can modify the patrol base troops here.
        (3, 0, 0, [
                    (call_script, "script_tick_town_walkers"),
                    (try_for_agents, ":cur_agent"),
                      (agent_get_troop_id, ":cur_troop", ":cur_agent"),
                      (try_begin),
                        (eq, ":cur_troop", "trp_fort_walker"),
                        (call_script, "script_cf_tick_fort_patrol", ":cur_agent", 1),
                      (else_try),
                        (agent_get_entry_no, ":entry_no", ":cur_agent"),
                        (this_or_next|eq, ":cur_troop", "trp_fort_rider"), #mounted patrol refuses to stay mounted and move
                        (eq, ":entry_no", 20), # crude hack atm to get this stupid cavalry to patrol properly
                        (agent_is_human, ":cur_agent"),
                        (call_script, "script_cf_tick_fort_patrol", ":cur_agent", 3),
                      (try_end),
                    (try_end),
                  ], []),
        (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),
        
      
    ],
  ),
#-## Outposts end
]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "mission_templates"
        orig_mission_templates = var_set[var_name_1]
        orig_mission_templates.extend(mission_templates) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)