from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

from header_skills import *


#################################################

  
  

############# NEW v1.0
common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_siege_init_ai_and_belfry"),
    ], [])

#run every frame for smooth wheel rotation
common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [ #modified from native
    (call_script, "script_siege_rot_belfry_platform")
    ])

# #this is run when the tower is in the final position
# #(eq, "$belfry_positioned", 1),
# common_siege_rotate_belfry = (
  # 3, 2, ti_once,
  # [(call_script, "script_cf_siege_rotate_belfry_platform")],
  # [(assign, "$belfry_positioned", 3)])
# #native belfry has two stages at most - (assign, "$belfry_positioned", 2), is called from cf script

#the belfry siege mechanism allows 20 seconds after mission start before archer are also allowed to push
#the middle agent loop allows for infantry or cavalry to contribute
#identical destinations allow for a tighter formation of 12, 2 at front, 1 mid, and 3 back
#the player is also allowed to push (higher strenght = faster), although standing on any of the belfry props will cause this to fail
common_siege_assign_men_to_belfry = (
  4, 0, ti_once,
  [(call_script, "script_cf_siege_assign_men_to_belfry")],
    [
      (try_for_agents, ":cur_agent"),
        (agent_is_active, ":cur_agent"),
        (agent_is_alive, ":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_clear_scripted_mode, ":cur_agent"),
        #turns out the stall script really doesn't do anything
        (agent_ai_set_always_attack_in_melee, ":cur_agent", 0),
        (agent_set_speed_limit, ":cur_agent", 100),
      (try_end),
      (set_show_messages, 0),
      #clears out stand ground order
      (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
      #makes sure they do not stall on ladder
      (team_give_order, "$attacker_team", grc_everyone, mordr_use_melee_weapons),
      (set_show_messages, 1),
    ])
##########################################
  
  
  
############################# NEW v1.9 - IMPROVED HORSE ARCHER AI - https://forums.taleworlds.com/index.php/topic,366006.msg8767998.html
improved_horse_archer_ai =  (2, 0, 0, [

          # (eq, "$field_ai_horse_archer",1), ######### will add it later
          
          (try_for_agents, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_non_player, ":agent_no"),
              (agent_get_troop_id, ":troop_id", ":agent_no"),
              (store_skill_level, ":horse_archery_level", "skl_horse_archery", ":troop_id"),
              (ge, ":horse_archery_level", 4),
          (try_end),
  ],
  [       
        (set_fixed_point_multiplier, 1000),
        (try_for_agents, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_non_player, ":agent_no"),
            (neg|agent_slot_eq, ":agent_no", 1003, 1),
            (agent_get_horse, ":horse_no", ":agent_no"),
            (assign, ":melee_weapon", -1),
            (try_begin),
                (agent_slot_eq, ":agent_no", slot_agent_is_running_away, 0),
                (gt, ":horse_no", -1),
                (agent_get_team, ":team_no", ":agent_no"),
                (agent_get_division, ":class_no", ":agent_no"),
                (team_get_weapon_usage_order, ":weapon_usage_order", ":team_no", ":class_no"),
                (team_get_movement_order, ":movement_order", ":team_no", ":class_no"),
                (team_get_hold_fire_order, ":hold_fire", ":team_no", ":class_no"),
                (assign, ":thrown_ammo", 0),
                (assign, ":ranged_weapon", -1),
                (try_for_range, ":item", 0, 4),
                  (agent_get_item_slot, ":item_weapon", ":agent_no", ":item"),
                  (gt, ":item_weapon", 0),
                  (item_get_type, ":item_weapon_type", ":item_weapon"),
                  (try_begin),
                    (eq, ":item_weapon_type", itp_type_thrown),
                    (agent_get_ammo_for_slot, ":ammo_for_slot", ":agent_no", ":item"),
                    (val_add, ":thrown_ammo", ":ammo_for_slot"),
                  (else_try),
                    (this_or_next|eq, ":item_weapon_type", itp_type_bow),
                    (this_or_next|eq, ":item_weapon_type", itp_type_pistol),
                    (eq, ":item_weapon_type", itp_type_musket),
                    (assign, ":ranged_weapon", ":item_weapon"),
                  (else_try),
                    (this_or_next|eq, ":item_weapon_type", itp_type_one_handed_wpn),
                    (this_or_next|eq, ":item_weapon_type", itp_type_two_handed_wpn),
                    (eq, ":item_weapon_type", itp_type_polearm),
                    (assign, ":melee_weapon", ":item_weapon"),
                  (try_end),
                (try_end),
                (gt, ":ranged_weapon", -1),           
                (neg|item_has_property, ":ranged_weapon", itp_cant_reload_on_horseback),
                (neg|item_has_property, ":ranged_weapon", itp_cant_use_on_horseback),
                (agent_get_ammo, ":ammo", ":agent_no", 0),
                (val_sub, ":ammo", ":thrown_ammo"),
                (gt, ":ammo", 0),
                (agent_set_slot, ":agent_no", 1003, 2),
                (neg|eq, ":hold_fire", aordr_hold_your_fire),
                (neg|eq, ":weapon_usage_order", wordr_use_melee_weapons),
                (eq, ":movement_order", mordr_charge),
                (agent_get_position, pos50, ":agent_no"),
                (agent_get_speed, pos31, ":agent_no"),
                (position_get_y, ":speed_y",pos31),
                (assign, ":distance_closest", 100000),#1000m
                (assign, ":enemies_closest", -1),
                (try_for_agents, ":enemies"),
                    (agent_is_alive, ":enemies"),
                    (agent_is_human, ":enemies"),
                    (agent_get_position, pos36, ":enemies"),
                    (agent_get_team, ":enemies_team", ":enemies"),
                    (teams_are_enemies, ":team_no", ":enemies_team"),
                    (get_distance_between_positions, ":distance", pos50, pos36),
                    (try_begin),
                      (agent_slot_eq, ":enemies", slot_agent_is_running_away, 1),
                      (val_add, ":distance", 10000),
                    (try_end),
                    (try_begin),
                      (agent_get_horse, ":enemies_horse", ":enemies"),
                      (gt, ":enemies_horse", -1),
                      (agent_get_speed, pos32, ":enemies"),
                      (position_get_y, ":speed_y_enemies",pos32),
                      (val_sub, ":speed_y_enemies", ":speed_y"),
                      (store_div, ":distance_cavalry", ":speed_y_enemies",5),
                      (val_max, ":distance_cavalry", 0),
                      (val_add, ":distance_cavalry", 500),
                      (val_sub, ":distance", ":distance_cavalry"),
                    (else_try),
                      (agent_get_wielded_item, ":weapon_hold", ":enemies", 1),
                      (neg|gt, ":weapon_hold", 1),
                      (val_sub, ":distance", 500),
                    (try_end),
                    (lt, ":distance", ":distance_closest"),
                    (assign, ":distance_closest", ":distance"),
                    (assign, ":enemies_closest", ":enemies"),
                (try_end),
                (neq, ":enemies_closest", -1),
                (agent_get_position, pos51, ":enemies_closest"),
                (get_distance_between_positions, ":distance_true", pos50, pos51),
                (try_begin),
                  (agent_slot_eq, ":enemies_closest", slot_agent_is_running_away, 0),
                  (gt, ":distance_true",200),
                  (agent_set_wielded_item, ":agent_no", ":ranged_weapon"),
                (else_try),
                  (le, ":distance_true", 200),
                  (gt, ":melee_weapon", -1),
                  (agent_set_wielded_item, ":agent_no", ":melee_weapon"),
                (try_end),
                (assign, ":speed_limit", 1000),
                (try_begin),
                    (agent_get_wielded_item, ":weapon_hold", ":agent_no", 0),
                    (gt, ":weapon_hold", 0),
                    (item_get_type, ":weapon_type", ":weapon_hold"),
                    (this_or_next|eq, ":weapon_type", itp_type_bow),
                    (this_or_next|eq, ":weapon_type", itp_type_pistol),
                    (eq, ":weapon_type", itp_type_musket),
                    (agent_get_bone_position, pos53, ":agent_no", 8, 1),
                    (agent_get_bone_position, pos54, ":enemies_closest", 9, 1),
                    (position_has_line_of_sight_to_position, pos53, pos54),
                    (agent_set_look_target_agent, ":agent_no", ":enemies_closest"),
                    (try_begin),
                      (assign, ":shoot_distance", 4000),
                      (agent_get_attack_action, ":attack_action", ":agent_no"),
                      (eq, ":attack_action", 1),
                      (try_begin),
                        (gt, ":distance_closest", 700),
                        (le, ":distance_closest", ":shoot_distance"),
                        (store_div, ":speed_limit", ":speed_y",2000),#
                        (val_max, ":speed_limit", 0),
                      (try_end),
                      (eq, ":weapon_type", itp_type_bow),
                      (try_begin),
                        (le, ":distance_true", ":shoot_distance"),
                        (agent_set_defend_action, ":agent_no", -2, 1),
                        (agent_set_attack_action, ":agent_no", 3, 0),
                      (else_try),
                        (gt, ":distance_true", ":shoot_distance"),
                        (agent_set_attack_action, ":agent_no", -2, 1),
                        (agent_set_defend_action, ":agent_no", 3, 1),
                      (try_end),
                    (else_try),
                      (eq, ":weapon_type", itp_type_bow),
                      (le, ":distance_true", ":shoot_distance"),#
                      (agent_get_combat_state, ":combat_state", ":agent_no"),
                      (neq, ":combat_state", 8),
                      (agent_set_attack_action, ":agent_no", 3, 1),
                    (try_end),
                (try_end),
                (agent_set_speed_limit, ":agent_no", ":speed_limit"),
                (try_begin),
                  (agent_slot_eq, ":enemies_closest", slot_agent_is_running_away, 0),
                  (lt, ":distance_closest", 10000),
                  (try_begin),
                    (get_scene_boundaries, pos2, pos3),
                    (position_transform_position_to_local, pos4, pos2,pos50),
                    (position_get_x, ":left", pos4),
                    (position_get_y, ":down", pos4),
                    (position_transform_position_to_local, pos4, pos2,pos3),
                    (position_get_x, ":map_width", pos4),
                    (position_get_y, ":map_height", pos4),
                    (store_sub, ":right", ":map_width", ":left"),
                    (store_sub, ":up", ":map_height", ":down"),
                    (position_transform_position_to_local, pos4, pos50, pos51),
                    (position_get_x, ":enemies_x", pos4),
                    (position_get_y, ":enemies_y", pos4),
                    (assign, ":effect", 0),
                    (try_begin),
                      (neg|gt, ":distance_closest", 1000),
                      (assign, ":effect", -78000),
                    (else_try),
                      (gt, ":distance_closest", 2000),#
                      (store_sub, ":effect", ":distance_closest", 0),
                      (val_mul, ":effect", 5),
                      (val_clamp, ":effect", 35000, 90000),
                    (try_end),
                    (assign, ":distance_to_boundary", 30000),
                    (val_min, ":distance_to_boundary", ":left"),
                    (val_min, ":distance_to_boundary", ":up"),
                    (val_min, ":distance_to_boundary", ":right"),
                    (val_min, ":distance_to_boundary", ":down"),
                    (try_begin),
                      (lt, ":distance_to_boundary", 30000),
                      (agent_slot_eq, ":enemies_closest", slot_agent_is_running_away, 0),
                      (store_div, ":map_middle_x", ":map_width", 20),
                      (store_div, ":map_middle_y", ":map_height", 20),
                      (position_copy_origin, pos4, pos2),
                      (position_move_x, pos4, ":map_middle_x", 1),
                      (position_move_y, pos4, ":map_middle_y", 1),
                      (get_distance_between_positions, ":distance_middle", pos4, pos50),
                      (position_transform_position_to_local, pos4, pos50, pos4),
                      (position_get_x, ":map_middle_x", pos4),
                      (position_get_y, ":map_middle_y", pos4),
                      (val_mul, ":map_middle_x", 100),
                      (val_mul, ":map_middle_y", 100),
                      (val_mul, ":enemies_x", 100),
                      (val_mul, ":enemies_y", 100),
                      (store_div, ":cos_middle", ":map_middle_x", ":distance_middle"),
                      (store_div, ":sin_middle", ":map_middle_y", ":distance_middle"),
                      (store_div, ":cos_enemies", ":enemies_x", ":distance_true"),
                      (store_div, ":sin_enemies", ":enemies_y", ":distance_true"),
                      (store_acos, ":angle_cos", ":cos_middle"),
                      (store_asin, ":angle_sin", ":sin_middle"),
                      (store_acos, ":angle_cos_enemies", ":cos_enemies"),
                      (store_asin, ":angle_sin_enemies", ":sin_enemies"),
                      (try_begin),
                        (lt, ":angle_sin", 0),
                        (val_mul, ":angle_cos", -1),
                        (val_add, ":angle_cos", 360000),
                      (try_end),
                      (try_begin),
                        (lt, ":angle_sin_enemies", 0),
                        (val_mul, ":angle_cos_enemies", -1),
                        (val_add, ":angle_cos_enemies", 360000),
                      (try_end),
                      (store_sub, ":k2", ":angle_cos", ":angle_cos_enemies"),
                      (val_sub, ":k2", 270000),
                      (val_sub, ":k2", ":effect"),
                      (store_add, ":effect", ":k2", ":effect"),
                      (try_begin),
                        (lt, ":angle_cos", ":angle_cos_enemies"),
                        (val_add, ":effect", 360000),
                      (try_end),
                      (val_clamp, ":effect",-210000, 15000),
                      (agent_set_attack_action, ":agent_no", -2, 1),
                      (agent_set_defend_action, ":agent_no", 3, 1),
                    (try_end),
                    (store_cos, ":cos", ":effect"),
                    (store_sin, ":sin", ":effect"),
                    (store_mul, ":k_x1", ":cos", ":enemies_y",),
                    (store_mul, ":k_x2", ":sin", ":enemies_x",),
                    (store_mul, ":k_y1", ":sin", ":enemies_y",),
                    (store_mul, ":k_y2", ":cos", ":enemies_x",),
                    (store_add, ":move_x", ":k_x1", ":k_x2"),
                    (store_sub, ":move_y", ":k_y1", ":k_y2"),
                    (position_move_x, pos50, ":move_x", 0),
                    (position_move_y, pos50, ":move_y", 0),
                  (try_end),
                  (agent_set_scripted_destination, ":agent_no", pos50, 1),
                (else_try),
                  (agent_clear_scripted_mode, ":agent_no"),
                  (agent_force_rethink, ":agent_no"),
                (try_end),
            (else_try),
                (try_begin),
                  (agent_slot_eq, ":agent_no", 1003, 0),
                  (agent_set_slot, ":agent_no", 1003, 1),
                (else_try),
                  (agent_slot_eq, ":agent_no", 1003, 2),
                  (this_or_next|agent_slot_eq, ":agent_no", slot_agent_is_running_away, 1),
                  (this_or_next|lt, ":horse_no", 0),
                  (this_or_next|eq, ":ammo", 0),
                  (this_or_next|eq, ":hold_fire", aordr_hold_your_fire),
                  (this_or_next|eq, ":weapon_usage_order", wordr_use_melee_weapons),
                  (neq, ":movement_order", mordr_charge),
                  (agent_clear_scripted_mode, ":agent_no"),
                  (agent_set_speed_limit, ":agent_no", 100),
                  (agent_force_rethink, ":agent_no"),
                  (agent_set_slot, ":agent_no", 1003, 3),
                  (this_or_next|eq, ":hold_fire", aordr_hold_your_fire),
                  (eq, ":ammo", 0),
                  (gt, ":melee_weapon", -1),
                  (agent_set_wielded_item, ":agent_no", ":melee_weapon"),
                (try_end),
            (try_end),
        (try_end),
  ])
##########################################################



############################# NEW v1.9 - Player can reassign archers to their position during sieges
archers_move_to_positions =  (0, 0, 3, [
          (key_clicked, key_numpad_0),
          (get_player_agent_no, ":player_agent"),
          (agent_is_alive, ":player_agent"),
          (agent_is_human, ":player_agent"),
          (agent_is_defender, ":player_agent"),
		  (store_faction_of_party, ":fief_faction", "$current_town"),
		  (this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"), ######### Player is lord of the town
		  (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_marshall, "trp_player"), ######### or is the marshall
		  (faction_slot_eq, ":fief_faction", slot_faction_leader, "trp_player"), ######### or is the king
  ],
  [       
    (call_script, "script_siege_move_archers_to_archer_positions"),
	(display_message, "@Archers! Move to your positions!"),
  ])
##########################################################




############################# NEW v1.9 - Kill count on top left
killcount_and_troop_ratio_bar =  (1, 0, ti_once, 
    [
      (neg|is_presentation_active, "prsnt_killcount"),
      (neg|is_presentation_active, "prsnt_troop_ratio_bar"),
      (neg|is_presentation_active, "prsnt_killcount_and_troop_ratio_bar"),
    ],
    [
########################### NEW v2.1 - kill count + merged troop ratio bar
      (try_begin),
        (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1),
        (start_presentation, "prsnt_killcount"),
      (else_try),
        (eq, "$g_misc_troop_ratio_bar_and_kill_count", 2),
        (start_presentation, "prsnt_troop_ratio_bar"),
      (else_try),
        (eq, "$g_misc_troop_ratio_bar_and_kill_count", 3),
        (start_presentation, "prsnt_killcount_and_troop_ratio_bar"),
      (try_end),
######################################################
      (call_script, "script_party_count_fit_for_battle", "p_main_party"),
      (assign, "$player_count_alive", reg0),
      (call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
      (store_sub, "$ally_count_alive", reg0, "$player_count_alive"),
      (call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
      (assign, "$enemy_count_alive", reg0),
    ])
#######################################################################################




############################# NEW v1.9 - Kill count on top left
troop_count =  (1, 0, ti_once, 
    [
      (neg|is_presentation_active, "prsnt_troop_count"),
    ],
    [
      # (try_begin),
        # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1),
        (start_presentation, "prsnt_troop_count"),
      # (try_end),
######################################################
      (call_script, "script_party_count_fit_for_battle", "p_main_party"),
      (assign, "$player_count_alive2", reg0),
      (call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
      (store_sub, "$ally_count_alive2", reg0, "$player_count_alive2"),
      (call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
      (assign, "$enemy_count_alive2", reg0),
    ])
#######################################################################################


############################# NEW v1.9 - Kill count on top left
# troop_refresh =  (2, 0, 0, 
    # [
      # (neg|is_presentation_active, "prsnt_troop_count"),
    # ],
    # [
      # (try_begin),
        # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1),
        # (start_presentation, "prsnt_troop_count"),
      # (try_end),
    # ])
#######################################################################################





############################# NEW v3.3
killcount_and_troop_ratio_bar_refresh =  (3, 0, 0, 
    [
      # (neg|is_presentation_active, "prsnt_killcount"),
      # (neg|is_presentation_active, "prsnt_troop_ratio_bar"),
      # (neg|is_presentation_active, "prsnt_killcount_and_troop_ratio_bar"),
    ],
    [
    (try_begin),
      (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1),
      (start_presentation, "prsnt_killcount"),
    (else_try),
      (eq, "$g_misc_troop_ratio_bar_and_kill_count", 2),
      (start_presentation, "prsnt_troop_ratio_bar"),
    (else_try),
      (eq, "$g_misc_troop_ratio_bar_and_kill_count", 3),
      (start_presentation, "prsnt_killcount_and_troop_ratio_bar"),
    (try_end),
    ])
#######################################################################################





############################# NEW v1.9 - New deathcam - https://forums.taleworlds.com/index.php/topic,282550.0.html
##BEAN BEGIN - Deathcam
common_init_deathcam = (
   0, 0, ti_once,
   [],
   [
        (assign, "$deathcam_on", 0),
        (assign, "$deathcam_death_pos_x", 0),
        (assign, "$deathcam_death_pos_y", 0),
        (assign, "$deathcam_death_pos_z", 0),

        (assign, "$deathcam_mouse_last_x", 5000),
        (assign, "$deathcam_mouse_last_y", 3750),

        (assign, "$deathcam_mouse_last_notmoved_x", 5000),
        (assign, "$deathcam_mouse_last_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_x", 5000), #Center screen (10k fixed pos)
        (assign, "$deathcam_mouse_notmoved_y", 3750),
        (assign, "$deathcam_mouse_notmoved_counter", 0),

        (assign, "$deathcam_total_rotx", 0),

        (assign, "$deathcam_sensitivity_x", 400), #4:3 ratio may be best
        (assign, "$deathcam_sensitivity_y", 300), #If modified, change values in common_move_deathcam

        (assign, "$deathcam_prsnt_was_active", 0),

        (assign, "$deathcam_keyboard_rotation_x", 0),
        (assign, "$deathcam_keyboard_rotation_y", 0),
        (assign, "$deathcam_flip_y_multiplier", 1),

        (get_player_agent_no, ":player_agent"),
        (agent_get_team, "$deathcam_player_team", ":player_agent"),
   ]
)

common_start_deathcam = (
    0, 4, ti_once, #4 second delay before the camera activates
    [
        (eq, "$enable_deahtcam", 1),
        (main_hero_fallen),
        (eq, "$deathcam_on", 0),
        # (eq, "$pop_camera_on", 0),
	    (assign, "$tom_sand_storm", 0),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (assign, "$deathcam_on", 1),

        (display_message, "@You were defeated.", 0xFF0000),
        (display_message, "@Rotate with the mouse. Move with standard keys."),
        (display_message, "@Shift/Control for Up/Down. Space Bar to increase speed."),
        (display_message, "@Numpad Plus/Minus to change sensitivity. Numpad to rotate."),
        (display_message, "@Home to reset position. End to flip Y rotation"),

        (mission_cam_get_position, pos1), #Death pos
        (position_get_x, reg3, pos1),
        (position_get_y, reg4, pos1),
        (position_get_z, reg5, pos1),
        (assign, "$deathcam_death_pos_x", reg3),
        (assign, "$deathcam_death_pos_y", reg4),
        (assign, "$deathcam_death_pos_z", reg5),
        (position_get_rotation_around_z, ":rot_z", pos1),

        (init_position, pos47),
        (position_copy_origin, pos47, pos1), #Copy X,Y,Z pos
        (position_rotate_z, pos47, ":rot_z"), #Copying X-Rotation is likely possible, but I haven't figured it out yet

        (mission_cam_set_mode, 1, 0, 0), #Manual?

        (mission_cam_set_position, pos47),

        # (team_give_order, "$deathcam_player_team", grc_everyone, mordr_charge),
   ]
)

common_move_deathcam = (
    0, 0, 0,
    [
      (eq, "$enable_deahtcam", 1),
      (this_or_next | eq, "$dmod_move_camera", 1),
      (eq, "$deathcam_on", 1),
      (this_or_next|game_key_is_down, gk_move_forward),
      (this_or_next|game_key_is_down, gk_move_backward),
      (this_or_next|game_key_is_down, gk_move_left),
      (this_or_next|game_key_is_down, gk_move_right),
      (this_or_next|key_is_down, key_left_shift),
      (this_or_next|key_is_down, key_left_control),
      (this_or_next|key_is_down, key_numpad_minus),
      (this_or_next|key_is_down, key_numpad_plus),
      (this_or_next|key_clicked, key_home),
      (key_clicked, key_end),
    ],
    [
        (set_fixed_point_multiplier, 10000),
        (mission_cam_get_position, pos47),

        (try_begin),
        (key_clicked, key_home),
            (position_set_x, pos47, "$deathcam_death_pos_x"),
            (position_set_y, pos47, "$deathcam_death_pos_y"),
            (position_set_z, pos47, "$deathcam_death_pos_z"),
        (try_end),

        (assign, ":move_x", 0),
        (assign, ":move_y", 0),
        (assign, ":move_z", 0),

        (try_begin),
        (game_key_is_down, gk_move_forward),
            (val_add, ":move_y", 10),
        (try_end),
        (try_begin),
        (game_key_is_down, gk_move_backward),
            (val_add, ":move_y", -10),
        (try_end),

        (try_begin),
        (game_key_is_down, gk_move_right),
            (val_add, ":move_x", 10),
        (try_end),
        (try_begin),
        (game_key_is_down, gk_move_left),
            (val_add, ":move_x", -10),
        (try_end),

        (try_begin),
        (key_is_down, key_left_shift),
            (val_add, ":move_z", 10),
        (try_end),
        (try_begin),
        (key_is_down, key_left_control),
            (val_add, ":move_z", -10),
        (try_end),

        (try_begin),
        (key_is_down, key_space),
            (val_mul, ":move_x", 4),
            (val_mul, ":move_y", 4),
            (val_mul, ":move_z", 2),
        (try_end),

        (try_begin),
        (key_is_down, key_end),
            (try_begin),
            (eq, "$deathcam_flip_y_multiplier", 1),
                (assign, "$deathcam_flip_y_multiplier", -1),
                (display_message, "@Y-Rotation Inverted"),
            (else_try),
                (assign, "$deathcam_flip_y_multiplier", 1),
                (display_message, "@Y-Rotation Normal"),
            (try_end),
        (try_end),

        (position_move_x, pos47, ":move_x"),
        (position_move_y, pos47, ":move_y"),
        (position_move_z, pos47, ":move_z"),

        (mission_cam_set_position, pos47),

        (try_begin),
        (key_is_down, key_numpad_minus),
        (ge, "$deathcam_sensitivity_x", 4), #Negative check.
        (ge, "$deathcam_sensitivity_y", 3),
            (val_sub, "$deathcam_sensitivity_x", 4),
            (val_sub, "$deathcam_sensitivity_y", 3),
            (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
            (store_mod, reg7, "$deathcam_sensitivity_y", 75),
            (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
                (assign, reg8, "$deathcam_sensitivity_x"),
                (assign, reg9, "$deathcam_sensitivity_y"),
                (display_message, "@Sensitivity - 25% ({reg8}, {reg9})"),
            (try_end),
        (else_try),
        (key_is_down, key_numpad_plus),
            (val_add, "$deathcam_sensitivity_x", 4),
            (val_add, "$deathcam_sensitivity_y", 3),
            (store_mod, reg6, "$deathcam_sensitivity_x", 100), #25% increments
            (store_mod, reg7, "$deathcam_sensitivity_y", 75),
            (try_begin),
            (eq, reg6, 0),
            (eq, reg7, 0),
                (assign, reg8, "$deathcam_sensitivity_x"),
                (assign, reg9, "$deathcam_sensitivity_y"),
                (display_message, "@Sensitivity + 25% ({reg8}, {reg9})"),
            (try_end),
        (try_end),
   ]
)

common_rotate_deathcam = (
    0, 0, 0,
    [
      (eq, "$enable_deahtcam", 1),
      (eq, "$deathcam_on", 1),
    ],
    [
        (set_fixed_point_multiplier, 10000), #Extra Precision

        (try_begin),
        (this_or_next|is_presentation_active, "prsnt_battle"), #Opened (mouse must move)
        (this_or_next|key_clicked, key_escape), #Menu
        (this_or_next|key_clicked, key_q), #Notes, etc
        (key_clicked, key_tab), #Retreat
        (eq, "$deathcam_prsnt_was_active", 0),
            (assign, "$deathcam_prsnt_was_active", 1),
            (assign, "$deathcam_mouse_last_notmoved_x", "$deathcam_mouse_notmoved_x"),
            (assign, "$deathcam_mouse_last_notmoved_y", "$deathcam_mouse_notmoved_y"),
        (try_end),

        (assign, ":continue", 0),

        (try_begin),
        (neg|is_presentation_active, "prsnt_battle"),
            (mouse_get_position, pos1), #Get and set mouse position
            (position_get_x, reg1, pos1),
            (position_get_y, reg2, pos1),

            (mission_cam_get_position, pos47),

            (try_begin),
            (neq, "$deathcam_prsnt_was_active", 1),
                (try_begin), #Check not moved
                (eq, reg1, "$deathcam_mouse_last_x"),
                (eq, reg2, "$deathcam_mouse_last_y"),
                (this_or_next|neq, reg1, "$deathcam_mouse_notmoved_x"),
                (neq, reg2, "$deathcam_mouse_notmoved_y"),
                    (val_add, "$deathcam_mouse_notmoved_counter", 1),
                    (try_begin), #Notmoved for n cycles
                    (ge, "$deathcam_mouse_notmoved_counter", 15),
                        (assign, "$deathcam_mouse_notmoved_counter", 0),
                        (assign, "$deathcam_mouse_notmoved_x", reg1),
                        (assign, "$deathcam_mouse_notmoved_y", reg2),
                    (try_end),
                (else_try), #Has moved
                    (assign, ":continue", 1),
                    (assign, "$deathcam_mouse_notmoved_counter", 0),
                (try_end),
                (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                (assign, "$deathcam_mouse_last_y", reg2),
            (else_try), #prsnt was active
                (try_begin),
                (neq, reg1, "$deathcam_mouse_last_x"), #Is moving
                (neq, reg2, "$deathcam_mouse_last_y"),
                    (store_sub, ":delta_x2", reg1, "$deathcam_mouse_last_notmoved_x"), #Store pos difference
                    (store_sub, ":delta_y2", reg2, "$deathcam_mouse_last_notmoved_y"),
                (is_between, ":delta_x2", -10, 11), #when engine recenters mouse, there is a small gap
                (is_between, ":delta_y2", -10, 11), #usually 5 pixels, but did 10 to be safe.
                    (assign, "$deathcam_prsnt_was_active", 0),
                    (assign, "$deathcam_mouse_notmoved_x", "$deathcam_mouse_last_notmoved_x"),
                    (assign, "$deathcam_mouse_notmoved_y", "$deathcam_mouse_last_notmoved_y"),
                (else_try),
                    (assign, "$deathcam_mouse_notmoved_x", reg1),
                    (assign, "$deathcam_mouse_notmoved_y", reg2),
                (try_end),
                    (assign, "$deathcam_mouse_last_x", reg1), #Next cycle, this pos = last pos
                    (assign, "$deathcam_mouse_last_y", reg2),
            (try_end),
        (try_end),

        (assign, ":delta_x", 0),
        (assign, ":delta_y", 0),
        (assign, ":rotating_horizontal", 0),
        (assign, ":rotating_vertical", 0),

        (try_begin),
        (key_is_down, key_numpad_4),
            (try_begin),
            (ge, "$deathcam_keyboard_rotation_x", 0),
                (assign, "$deathcam_keyboard_rotation_x", -20),
            (try_end),
            (val_add, "$deathcam_keyboard_rotation_x", -1),
            (assign, ":continue", 2),
            (assign, ":rotating_horizontal", -1),
        (else_try),
        (key_is_down, key_numpad_6),
            (try_begin),
            (le, "$deathcam_keyboard_rotation_x", 0),
                (assign, "$deathcam_keyboard_rotation_x", 20),
            (try_end),
            (val_add, "$deathcam_keyboard_rotation_x", 1),
            (assign, ":continue", 2),
            (assign, ":rotating_horizontal", 1),
        (else_try),
            (assign, "$deathcam_keyboard_rotation_x", 0),
            (assign, ":rotating_horizontal", 0),
        (try_end),

        (try_begin),
        (key_is_down, key_numpad_8),
            (try_begin),
            (le, "$deathcam_keyboard_rotation_y", 0),
                (assign, "$deathcam_keyboard_rotation_y", 15),
            (try_end),
            (val_add, "$deathcam_keyboard_rotation_y", 1),
            (assign, ":continue", 2),
            (assign, ":rotating_vertical", 1),
        (else_try),
        (this_or_next|key_is_down, key_numpad_2),
        (key_is_down, key_numpad_5),
            (try_begin),
            (ge, "$deathcam_keyboard_rotation_y", 0),
                (assign, "$deathcam_keyboard_rotation_y", -15),
            (try_end),
            (val_add, "$deathcam_keyboard_rotation_y", -1),
            (assign, ":continue", 2),
            (assign, ":rotating_vertical", -1),
        (else_try),
            (assign, "$deathcam_keyboard_rotation_y", 0),
            (assign, ":rotating_vertical", 0),
        (try_end),

        (try_begin),
        (eq, ":continue", 1),
            (store_sub, ":delta_x", reg1, "$deathcam_mouse_notmoved_x"), #Store pos difference
            (store_sub, ":delta_y", reg2, "$deathcam_mouse_notmoved_y"),
        (else_try),
        (eq, ":continue", 2),
            (try_begin),
            (neq, ":rotating_horizontal", 0),
                (val_clamp, "$deathcam_keyboard_rotation_x", -80, 80),
                (assign, ":delta_x", "$deathcam_keyboard_rotation_x"),
            (try_end),

            (try_begin),
            (neq, ":rotating_vertical", 0),
                (val_clamp, "$deathcam_keyboard_rotation_y", -45, 45),
                (assign, ":delta_y", "$deathcam_keyboard_rotation_y"),
            (try_end),
        (try_end),

        (try_begin),
        (ge, ":continue", 1),
            (val_mul, ":delta_x", "$deathcam_sensitivity_x"),
            (val_mul, ":delta_y", "$deathcam_sensitivity_y"),
            (val_mul, ":delta_y", "$deathcam_flip_y_multiplier"),

            (val_clamp, ":delta_x", -80000, 80001), #8
            (val_clamp, ":delta_y", -60000, 60001), #6

            (store_mul, ":neg_rotx", "$deathcam_total_rotx", -1),
            (position_rotate_x_floating, pos47, ":neg_rotx"), #Reset x axis to initial state

            (position_rotate_y, pos47, 90), #Barrel roll by 90 degrees to inverse x/z axis
            (position_rotate_x_floating, pos47, ":delta_x"), #Rotate simulated z axis, Horizontal
            (position_rotate_y, pos47, -90), #Reverse

            (position_rotate_x_floating, pos47, "$deathcam_total_rotx"), #Reverse

            (position_rotate_x_floating, pos47, ":delta_y"), #Vertical
            (val_add, "$deathcam_total_rotx", ":delta_y"), #Fix yaw
            (mission_cam_set_position, pos47),
        (try_end),
    ]
)


########################### NEW v2.1
common_check_deathcam = (
        1, 4, ti_once, 
        [
         (main_hero_fallen),
         (assign, ":pteam_alive", 0),
         (try_for_agents, ":agent"), #Check players team is dead
           (neq, ":pteam_alive", 1), #Break loop
           (agent_is_ally, ":agent"),
           (agent_is_alive, ":agent"),
             (assign, ":pteam_alive", 1),
         (try_end),
         (this_or_next|eq, ":pteam_alive", 0),  ##### NEW v2.1
         (eq, "$freelancer_state", 1),              ##### 
        ],
		
        [
         (assign, "$pin_player_fallen", 1),
         (display_message, "str_enhanced_battle_knocked_out_message_1"),
         (display_message, "str_enhanced_battle_knocked_out_message_2"),

         # (str_store_string, s5, "str_retreat"),
         # (call_script, "script_simulate_retreat", 10, 20),
         # (assign, "$g_battle_result", -1),
         # (set_mission_result,-1),
         # (call_script, "script_count_mission_casualties_from_agents"),
         # (finish_mission,0),
        ])
		
		
#####################################################################






##BEAN END - Deathcam
#######################################################################################




############################# CABA`DRIN BODYGUARDS IN SCENES
bodyguard_triggers = [
 (ti_after_mission_start, 0, ti_once, [(neq, "$g_mt_mode", tcm_disguised)], #condition for not sneaking in; to exclude prison-breaks, etc change to (eq, "$g_mt_mode", tcm_default")
   [
    #Get number of bodyguards
    (store_skill_level, ":leadership", skl_leadership, "trp_player"),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":leadership", 3),
    (val_div, ":renown", 400),
    (store_add, ":max_guards", ":renown", ":leadership"),
    (val_min, ":max_guards", 4),
   
    (ge, ":max_guards", 1),

    #Get player info
    (get_player_agent_no, ":player"),
    (agent_get_team, ":playerteam", ":player"),
    (agent_get_horse, ":use_horse", ":player"), #If the player spawns with a horse, the bodyguard will too.

    #Prepare Scene/Mission Template
    (assign, ":entry_point", 0),
    (assign, ":mission_tpl", 0),
    (try_begin),       
        (party_slot_eq, "$current_town", slot_party_type, spt_village),
        (assign, ":entry_point", 11), #Village Elder's Entry
        (assign, ":mission_tpl", "mt_village_center"),
    (else_try),
        (this_or_next|eq, "$talk_context", tc_prison_break),
        (this_or_next|eq, "$talk_context", tc_escape),
        (eq, "$talk_context", tc_town_talk),
        (assign, ":entry_point", 24), #Prison Guard's Entry
        (try_begin),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (assign, ":mission_tpl", "mt_castle_visit"),
        (else_try),
            (assign, ":mission_tpl", "mt_town_center"),
        (try_end),
    (else_try),
        (eq, "$talk_context", tc_tavern_talk),
        (assign, ":entry_point", 17), #First NPC Tavern Entry
    (try_end),
    (try_begin),
        (neq, "$talk_context", tc_tavern_talk),
        (gt, ":use_horse", 0),
        (mission_tpl_entry_set_override_flags, ":mission_tpl", ":entry_point", 0),
    (try_end),
    (store_current_scene, ":cur_scene"),
    (modify_visitors_at_site, ":cur_scene"), 
   
    #Find and Spawn Bodyguards
    (assign, ":bodyguard_count", 0),   
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
        (neq, ":troop_id", "trp_player"),
        (troop_is_hero, ":troop_id"),
        (neg|troop_is_wounded, ":troop_id"),
        (val_add, ":bodyguard_count", 1),
               
        (try_begin), #For prison-breaks
            (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_prison_break),     
            (troop_set_slot, ":troop_id", slot_troop_will_join_prison_break, 1),
        (try_end),

        (add_visitors_to_current_scene, ":entry_point", ":troop_id", 1),

        (eq, ":bodyguard_count", ":max_guards"),
        (assign, ":num_of_stacks", 0), #Break Loop       
    (try_end), #Stack Loop
    (gt, ":bodyguard_count", 0), #If bodyguards spawned...
    (set_show_messages, 0),   
    (team_give_order, ":playerteam", 8, mordr_follow), #Division 8 to avoid potential conflicts
    (set_show_messages, 1),   
   ]),   

 (ti_on_agent_spawn, 0, 0, [],
   [
    (store_trigger_param_1, ":agent"),
    (agent_get_troop_id, ":troop", ":agent"),
    (neq, ":troop", "trp_player"),
    (troop_is_hero, ":troop"),
    (main_party_has_troop, ":troop"),
   
    (get_player_agent_no, ":player"),
    (agent_get_team, ":playerteam", ":player"),
    (agent_get_position,pos1, ":player"),       
   
    (agent_set_team, ":agent", ":playerteam"),
    (agent_set_division, ":agent", 8),
    (agent_add_relation_with_agent, ":agent", ":player", 1),
    (agent_set_is_alarmed, ":agent", 1),
    (store_random_in_range, ":shift", 1, 3),
    (val_mul, ":shift", 100),
    (position_move_y, pos1, ":shift"),
    (store_random_in_range, ":shift", 1, 3),
    (store_random_in_range, ":shift_2", 0, 2),
    (val_mul, ":shift_2", -1),
    (try_begin),
        (neq, ":shift_2", 0),
        (val_mul, ":shift", ":shift_2"),
    (try_end),
    (position_move_x, pos1, ":shift"),
    (agent_set_position, ":agent", pos1),
   ]),
 
 (ti_on_agent_killed_or_wounded, 0, 0, [],
    [
     (store_trigger_param_1, ":dead_agent"),
       
     (agent_get_troop_id, ":troop", ":dead_agent"),
     (neq, ":troop", "trp_player"),
     (troop_is_hero, ":troop"),
     (main_party_has_troop, ":troop"),
     (party_wound_members, "p_main_party", ":troop", 1),
    ]),
 ]
#############################



############################# ORDER: WEAPON TYPE SWITCH 
order_weapon_type_triggers = [     
(0, 0, 1, [(key_clicked, key_for_onehand)], [(call_script, "script_order_weapon_type_switch", onehand)]),
(0, 0, 1, [(key_clicked, key_for_bothhands)], [(call_script, "script_order_weapon_type_switch", bothhands)]),    
(0, 0, 1, [(key_clicked, key_for_ranged)], [(call_script, "script_order_weapon_type_switch", ranged)]),
(0, 0, 1, [(key_clicked, key_for_shield)], [(call_script, "script_order_weapon_type_switch", shield)]),
]
#############################  




############################# ORDER: VOLLEY FIRE!
order_volley_triggers = [
    (0, 0, 1, [(key_clicked, key_for_volley)], [(call_script, "script_order_volley_begin_end")]),
    (1, 0, 0, [(call_script, "script_cf_order_volley_check")], [
        (try_for_range, ":team", 0, 4),
            (try_for_range, ":division", 0, 9),
                (store_add, ":slot", slot_team_d0_order_volley, ":division"),
                (team_slot_ge, ":team", ":slot", 1),
                (team_get_slot, ":volley_counter", ":team", ":slot"),
                (val_add, ":volley_counter", 1),
                (team_set_slot, ":team", ":slot", ":volley_counter"),
            (try_end),
        (try_end),
       
        (try_for_agents, ":agent"),
            (agent_is_non_player, ":agent"),
            (agent_slot_ge, ":agent", slot_agent_volley_fire, 1),
            (agent_get_ammo, ":ammo", ":agent", 1),
            (gt, ":ammo", 0),
           
            (agent_get_team, ":team", ":agent"),
            (agent_get_division, ":division", ":agent"),
            (store_add, ":slot", slot_team_d0_order_volley, ":division"),
            (team_get_slot, ":volley_counter", ":team", ":slot"),
           
            (agent_get_slot, ":volley_wpn_type", ":agent", slot_agent_volley_fire),
            (try_begin),
                (eq, ":volley_wpn_type", itp_type_bow),
                (assign, ":delay", 3),
            (else_try),
                (eq, ":volley_wpn_type", itp_type_crossbow),
                (assign, ":delay", 5),
            (try_end),
            (agent_get_combat_state, ":cs", ":agent"),
            (this_or_next|eq, ":cs", 1),
            (eq, ":cs", 3),
                       
            (store_mod, reg0, ":volley_counter", ":delay"),       
            (try_begin),
                (eq, reg0, 0),
                (agent_set_attack_action, ":agent", 0, 0), #Fire
            (else_try),
                (agent_set_attack_action, ":agent", 0, 1), #Ready and Aim
            (try_end),
        (try_end),
     ]),
 
    (1, 0, ti_once, [(neq, "$g_battle_result", 0)], [   #Disable Volley @ end of battle
        (try_for_range, ":team", 0, 4),
            (try_for_range, ":slot", slot_team_d0_order_volley, slot_team_d0_order_volley + 9),
                (team_set_slot, ":team", ":slot", 0),
            (try_end),
        (try_end),
     ]),
]
#############################





################### NEW v2.1 - moved this here to make things easier to edit
####################################################### ARCHER REASSIGNED TO INFANTRY WHEN OUT OF AMMO
reassign_archers_to_division = [
(ti_on_item_unwielded, 0, 0, [], #Out of Ammo Trigger
   [
    (store_trigger_param_2, ":weapon"),
    (ge, ":weapon", 0),
    (item_get_type, ":type", ":weapon"),
    (this_or_next|eq, ":type", itp_type_bow),
    (eq, ":type", itp_type_crossbow),
   
    (store_trigger_param_1, ":agent"),
    (agent_is_active, ":agent"),
    (agent_is_alive, ":agent"),
    (agent_is_non_player, ":agent"),
   
    (agent_get_ammo, ":ammo", ":agent", 0),
    (le, ":ammo", 0),   
    (agent_get_horse, ":horse", ":agent"),
    (eq, ":horse", -1),
   
    (assign, ":continue", 1),
    (try_begin),
        (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town), #Sieges
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),   
        (agent_get_team, ":team", ":agent"),   
        (this_or_next|eq, ":team", "$defender_team"),
        (eq, ":team", "$defender_team_2"),
        (assign, ":continue", 0), #To not reassign units that will get their ammo refilled.
    (try_end),
    (eq, ":continue", 1),   
 
    (agent_set_division, ":agent", 4),
    (agent_set_slot, ":agent", slot_agent_new_division, 4),
   ]),
   
(ti_on_agent_spawn, 0, 0, [], 
    [
    (store_trigger_param_1, ":agent"),
    (agent_set_slot, ":agent", slot_agent_new_division, -1),
    ]),

(1, 0, 0, [],
   [
    (try_for_agents, ":agent"),
        (agent_is_active, ":agent"),
        (agent_slot_ge, ":agent", slot_agent_new_division, 0),
        (agent_is_alive, ":agent"),
        (agent_get_division, ":division", ":agent"),
        (neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
        (agent_get_slot, ":new_div", ":agent", slot_agent_new_division),
        (agent_set_division, ":agent", ":new_div"),
    (try_end),   
   ]),

]
##########################################################  


reassign_horseless_cavalry_to_division = [     
################################################################ DE HORSED CAVALRY BECOMES INFANTRY
(ti_on_agent_spawn, 0, 0, [], 
[
(store_trigger_param_1, ":agent"),
(agent_set_slot, ":agent", slot_agent_new_division, -1),
]), #De-Horse trigger 0


(ti_on_agent_spawn, 0, 0, [], #De-Horse Trigger 1
  [
    (store_trigger_param_1, ":horse"),
    
    (try_begin),
        (neg|agent_is_human, ":horse"),    
        (agent_get_rider, ":rider", ":horse"),
        (ge, ":rider", 0), #I don't know if any of these checks are necessary
        (agent_is_active, ":rider"),
        (agent_is_alive, ":rider"),
        (agent_is_non_player, ":rider"),
    (else_try),
        (assign, ":rider", -1),
    (try_end),
    
    (agent_set_slot, ":horse", slot_agent_horse_rider, ":rider"),
  ]),

(ti_on_agent_killed_or_wounded, 0, 0, [], #De-Horse Trigger 2
  [
    (store_trigger_param_1, ":dead_horse"),
    (neg|agent_is_human, ":dead_horse"),
    
    (agent_get_slot, ":rider", ":dead_horse", slot_agent_horse_rider),
    (ge, ":rider", 0),
    (agent_is_active, ":rider"),
    (agent_is_alive, ":rider"),
    # (agent_is_non_player, ":rider"),
	
	
    (try_begin),
	  ########## NEW v2.1 - troop riding skill affects chance of being damaged and the amount of damage 
	  (assign, ":chance_of_damage", rider_fall_default_chance_of_damage),
      (agent_get_troop_id, ":rider_id", ":rider"),
      (store_skill_level, ":rider_skill", "skl_riding", ":rider_id"),
	  
      (store_mul, ":chance_reduction", ":rider_skill", rider_fall_chance_of_damage_reduction_by_level_of_riding), #### x% less chance per level
      (val_sub, ":chance_of_damage", ":chance_reduction"), 
	  
      (call_script, "script_rand", 0, 100),
      (le, reg0, ":chance_of_damage"),
	    (call_script, "script_rand", rider_fall_default_damage_min, rider_fall_default_damage_max),
	    (assign, ":damage", reg0),
	    (store_mul, ":damage_reduction", ":rider_skill", rider_fall_damage_reduction_by_level_of_riding), #### x less damage per level
        (val_sub, ":damage", ":damage_reduction"), 
        (agent_deliver_damage_to_agent, ":dead_horse", ":rider", ":damage"),
        (try_begin),
          (neg|agent_is_non_player, ":rider"), ### player
            (display_message, "@You fall down from your horse and sustain some damage!"),
        (try_end),
    (try_end),
	
    (try_begin),
      (agent_is_active, ":rider"),     ### NEW v2.1 - cbeck if he is alive first
      (agent_is_alive, ":rider"),     ### 
        (agent_set_division, ":rider", grc_infantry),
        (agent_set_slot, ":rider", slot_agent_new_division, grc_infantry),
    (try_end),
  ]),

(1, 0, 0, [],
   [
    (try_for_agents, ":agent"),
        (agent_is_active, ":agent"),
        (agent_slot_ge, ":agent", slot_agent_new_division, 0),
        (agent_is_alive, ":agent"),
        (agent_get_division, ":division", ":agent"),
        (neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
        (agent_get_slot, ":new_div", ":agent", slot_agent_new_division),
        (agent_set_division, ":agent", ":new_div"),
    (try_end),   
   ]),

]
##########################################################  



########### NEW v2.5 - apparently 1257 already does this
assign_horse_archers_to_archers = [   
(ti_on_agent_spawn, 0, 0, [], #dckplmc - treat all defending horse archers as archers
 [
 (store_trigger_param_1, ":agent_no"),
 (agent_is_alive, ":agent_no"),
 (agent_is_human, ":agent_no"),
 (agent_is_defender, ":agent_no"),
 # (agent_get_troop_id, ":troop_id", ":agent_no"),
 # (troop_is_guarantee_ranged, ":troop_id"),
 (try_for_range, ":r", "itm_hunting_bow", "itm_arrows"),
   (agent_has_item_equipped, ":agent_no", ":r"),
   (agent_set_division, ":agent_no", grc_archers),
 (try_end),
 #(agent_set_division, ":agent_no", grc_archers),
 ]),
]
##########################################################  







##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

pilgrim_disguise = [itm_priest_robe_1,itm_priest_cap_1,itm_shoes,itm_sword_type_xii, itm_talak_buckler,itm_throwing_daggers]
#af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian
af_castle_lord = af_override_horse | af_override_weapons | af_override_head | af_override_gloves


common_kill_count = (
  ti_on_agent_killed_or_wounded, 0, 0, [],
   [
    (store_trigger_param_1, ":dead_agent_no"),
    (store_trigger_param_2, ":killer_agent_no"),
    #(store_trigger_param_3, ":is_wounded"),
    
    (neg|agent_is_ally, ":dead_agent_no"),
    (agent_is_human, ":dead_agent_no"),
    (eq, ":killer_agent_no", "$fplayer_agent_no"),
    
    (val_add, "$killcount", 1),
   ])



initialise_auxiliary_player = (ti_before_mission_start, 0, 0, 
[
],
[
    #reset global variables
    (assign, "$enable_deahtcam", 1), #enable deathcam
    (assign, "$auxilary_player_active", 0), #variable for player party after party rebalancing
    (eq, "$use_player_auxiliary", 1),  #is active player enabled?
    
    #backup player party
    (assign, "$g_move_heroes", 1),
    (party_clear, "p_temp_casualties_3"),
    (call_script, "script_party_add_party", "p_temp_casualties_3", "p_main_party"),
    (set_player_troop, "trp_player"), #just in case?    
    (assign, "$enable_deahtcam", 0), #disable deathcam, until we can not find any troops to "posses"
])

auxiliary_player_check = (5, 0, 0, 
      [
        (eq, "$use_player_auxiliary", 1),
        (eq, "$enable_deahtcam", 0), #if deatcham is activated, no longer spawn as an auxiliary. TODO: reset camera settings and spawn anyway?
        (get_player_agent_no, ":agent"),
        (neg|agent_is_alive, ":agent"),        
		(neq, "$freelancer_state", 1),  ############ NEW v2.1 - freelancer deathcamera bugfix
      ],
      [
        (set_fixed_point_multiplier, 100),
        (get_player_agent_no, ":p_agent"),
        (agent_get_team, ":player_team", ":p_agent"),
        (agent_get_division, ":player_division", ":p_agent"),
        (assign, ":spawned", 0),
            
        (try_for_agents, ":agent"),
          (eq, ":spawned", 0),
          (agent_is_human, ":agent"),
          (agent_is_alive, ":agent"),
          (agent_get_team, ":agent_team", ":agent"),
          (agent_get_party_id, ":agent_party", ":agent"),
          (eq, ":agent_party", "p_main_party"),
          (agent_get_division, ":agent_division", ":p_agent"),
          (agent_get_group, ":agent_group", ":p_agent"),
          (eq, ":player_team", ":agent_team"),
          (eq, ":player_division", ":agent_division"),
          (agent_get_troop_id, ":troop_id", ":agent"),
          (neg|is_between, ":troop_id", companions_begin, lords_end), #just in case ######## NEW v3.7 reverted this because of bugs
          # (neg|is_between, ":troop_id", lords_begin, lords_end), ### NEW v1.9 - Companions now included
          
          (set_player_troop, ":troop_id"),
          (store_agent_hit_points, ":hp", ":agent",1),
          (agent_get_position, pos1, ":agent"),
          (position_set_z, pos1, -2000), 
          (position_set_x, pos1, 0), 
          (position_set_y, pos1, 0), 
          (agent_get_position, pos0, ":agent"),
          (set_spawn_position, pos0),
          (agent_get_horse, ":horse", ":agent"),
          (try_begin),
            (gt, ":horse", 0),
            (agent_set_position, ":horse",pos1),
            (remove_agent, ":horse"),
          (try_end),
          (agent_set_position, ":agent", pos1),
          (agent_set_slot, ":agent", slot_possessed, 1), 
          (agent_get_slot, ":index", ":agent", slot_index_value), #lance recruitment flag
          (remove_agent, ":agent"),
          (spawn_agent, ":troop_id"),
          (assign, ":p_agent", reg0),
          (agent_set_slot, ":p_agent", slot_index_value, ":index"),
          (agent_set_team, ":p_agent", ":player_team"),
          #(agent_set_division, ":p_agent", ":agent_division"),
          (agent_set_hit_points, ":p_agent" , ":hp",1),
          (agent_set_group, ":p_agent", ":agent_group"),
          (agent_set_slot, ":p_agent", slot_possessed, 2), 
          (agent_set_slot, ":p_agent", slot_real_troop, ":troop_id"),
          (try_begin),
            (agent_get_horse, ":p_horse", ":p_agent"),
            (gt, ":p_horse", 0), #player is mounted
            (lt, ":horse", 0), #AI is not mounted!
            (agent_set_position, ":p_horse",pos1),
            (remove_agent, ":p_horse"),
          (try_end),
          (set_player_troop, "trp_player"),
          (assign, ":spawned", 1),
          (assign, "$auxilary_player_active", 1), #checks that player spawned and will need to manualy correct party

          #(team_set_order_listener, ":player_team", grc_everyone),
          #(team_give_order, ":player_team", grc_everyone, mordr_hold), #tom
        (try_end),  
        (eq, ":spawned", 0),
        (assign, "$enable_deahtcam", 1), #deathcam is active now
      ])

      
	  
############### NEW v2.1 - copy of the above for freelancer fix
auxiliary_player_check_freelancer = (5, 0, 0, 
      [
        (eq, "$use_player_auxiliary", 1),
        (eq, "$enable_deahtcam", 0),
        (get_player_agent_no, ":agent"),
        (neg|agent_is_alive, ":agent"),        
		(eq, "$freelancer_state", 1),  ############ NEW v2.1 - freelancer deathcamera bugfix
      ],
      [
        (assign, "$enable_deahtcam", 1), #deathcam is active now
      ])
############################################################

      
# fog_effects_range = (
    # ti_on_agent_spawn, 0, 0, [],
    # [
        # (store_trigger_param_1, ":agent"),
        # (get_global_haze_amount, ":fog"),
        # (gt, ":fog", 60),
        # (agent_is_human, ":agent"),
        # (get_player_agent_no, ":player"),
        # (neq, ":agent", ":player"),
        
    # ])
    
reset_troop_array_for_combat = (
  ti_before_mission_start, 0, 0,
  [],
  [
    (call_script, "script_clear_troop_array", "trp_lances_troop_in_combat", 0, "$lance_troop_serving"),
  ]
)    
    
check_spawned_troop = (
  ti_on_agent_spawn, 0, 0,
  [],
  [
    (store_trigger_param_1, ":agent"),
    (agent_is_human, ":agent"), #not a horse
    (get_player_agent_no, ":p_agent"),
    (neq, ":agent", ":p_agent"), #not player
    (agent_get_party_id, ":party", ":agent"),
    (eq, ":party", "p_main_party"), #is part of the player party
    (agent_get_troop_id, ":troop", ":agent"),
    (call_script, "script_search_for_troop", ":troop"), 
    (agent_set_slot, ":agent", slot_index_value, reg0),
  ]
)
    
cheer_trigger =  (
  0, 1.5, 0, 
  [
    (key_clicked, key_t),
    (get_player_agent_no, ":player"),
    (agent_is_alive, ":player"),
    (agent_set_animation, ":player", "anim_cheer", 1),
    (agent_play_sound, ":player", "snd_man_victory"),
  ],
  
  [
      (get_player_agent_no, ":player"),
    (agent_get_team, ":team", ":player"),
    (agent_get_position, pos1, ":player"),
    (try_for_agents, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_is_human, ":agent"),
      (agent_get_team, ":agent_team", ":agent"),
      (eq, ":agent_team", ":team"),
      (agent_get_position, pos0, ":agent"),
      (get_distance_between_positions_in_meters, ":distance",pos0, pos1),
      (lt, ":distance", 20),
      (agent_set_animation, ":agent", "anim_cheer", 1),
      (agent_play_sound, ":agent", "snd_man_victory"),
      (agent_get_slot, ":courage", ":agent", slot_agent_courage_score),
      #(assign, reg0, ":courage"),
      #(display_message, "@we have {reg0} courage"),
      (val_add, ":courage", 5),
      (val_min, ":courage", 9600),
      #(assign, reg0, ":courage"),
      #(display_message, "@now we have {reg0} courage"),
      (agent_set_slot, ":agent", slot_agent_courage_score, ":courage"),
      #(display_message,  "@huzzah!"),
    (try_end),
    (display_message,  "@Huzzah! You encourage your nearby troops."),
  ])

command_cheer = (
  0, 1.7, 0, [(eq, "$tom_yell_smelly_peasents", 1)],
   [
     (call_script, "script_tom_command_cheer"),
     (assign, "$tom_yell_smelly_peasents", 0),
    ])        
            
change_weather = (
  ti_before_mission_start, 0, 0, [],
   [
    (assign, "$tom_sand_storm", 0), #tom
    (call_script, "script_change_rain_or_snow"),
    
    # modded2x disable shitty shaders
    #### shaders
    # (set_fixed_point_multiplier, 100),
    # (try_begin),
      # (is_currently_night),
      # (set_shader_param_float, "@vFresnelMultiplier", shader_float_default),
    # (else_try),
      # (set_shader_param_float, "@vFresnelMultiplier", shader_float_day),
    # (try_end),
    #### shaders
    
    #(music_set_culture, mtf_sit_fight),
   ])
   
sand_storm = (     #Tom made
  0, 0, 0, [(eq, "$tom_sand_storm", 1)],
  [    
      (get_player_agent_no, ":player"),
      (agent_get_position, pos0, ":player"),
      (position_set_z_to_ground_level, pos0),
      #(position_move_z, pos3, 350),
           (position_get_z, ":z", pos0),
      (val_add, ":z", 400),
      (position_set_z, pos0, ":z"),
      (particle_system_burst, "psys_desert_storm", pos0,2),
      #(assign, reg26, "$tom_sand_storm_chance"),
          (set_fixed_point_multiplier, 100),
])

blizzard_strom = (     #Tom made
  0, 0, 0, [(eq, "$tom_sand_storm", 2)],
  [    
      (get_player_agent_no, ":player"),
      (agent_get_position, pos0, ":player"),
      (position_set_z_to_ground_level, pos0),
     (position_get_z, ":z", pos0),
      (val_add, ":z", 2000),
      (position_set_z, pos0, ":z"),
      #(position_move_z, pos33, 0 ,350),
      (particle_system_burst, "psys_blizzard", pos0,1),
          (set_fixed_point_multiplier, 100),
])

rain_storm = (     #Tom made
  0, 0, 0, [(eq, "$tom_sand_storm", 3)],
  [    
      (get_player_agent_no, ":player"),
      (agent_get_position, pos0, ":player"),
      (position_set_z_to_ground_level, pos0),
     (position_get_z, ":z", pos0),
      (val_add, ":z", 2100),
      (position_set_z, pos0, ":z"),
      #(position_move_z, pos33, 1 ,850),
      (particle_system_burst, "psys_rain", pos0,1),  
          (set_fixed_point_multiplier, 100),
])

rain_storm_sound = ( #tom made - thunder crap
8, 0, 0, [(eq, "$tom_sand_storm", 3)],
[
    (store_random_in_range, ":random", 0, 100),
    (try_begin),
     (ge, ":random", 90),
      (play_sound, "snd_thunder"),
    (try_end),
    #(get_player_agent_no, ":player"),
    #(agent_play_sound, ":player", "snd_thunder"),
#    (agent_play_sound, ":cur_agent", "snd_cough"),
])

blizzard_sound = ( #tom made - wind crap
0, 0, ti_once, [(eq, "$tom_sand_storm", 2)],
[
    #(get_player_agent_no, ":player"),
    #(agent_play_sound, ":player", "snd_wind"),
    (play_sound, "snd_wind"),
])

desert_storm_sound = ( #tom made - wind crap as well?
0, 0, ti_once, [(eq, "$tom_sand_storm", 1)],
[
    (play_sound, "snd_wind"),
])

coordinator = ( #tom made, debug
  1, 0, 0, [], 
  [
    (get_player_agent_no, ":player"),
    (agent_get_position, pos1, ":player"),
    (position_get_x, ":x", pos1),
    (position_get_y, ":y", pos1),
    (assign, reg0, ":y"),
    (assign, reg1, ":x"),
    (display_message, "@current pos y: {reg0};  x: {reg1}"),
  ])
  
bastards_with_banners = ( #tom made
0, 2, ti_once, [(eq, "$tom_use_banners", 1)],
[
    (call_script, "script_set_flag_carriers"),
    #(set_fixed_point_multiplier, 100),
])

bastards_with_banners_bonus = ( #tom made
10, 0, 0, [(eq, "$tom_use_banners", 1), (eq, "$tom_bonus_banners", 1),],
[
    (get_player_agent_no, ":p_agent"),
    (try_for_range, ":agent"),
      (agent_slot_eq, ":agent", slot_agent_banner, 1),
      (agent_is_alive, ":agent"),
      (agent_is_active, ":agent"),
      (agent_get_team, ":team", ":agent"),
      (agent_get_position, pos1, ":agent"),
      (try_for_range, ":agent2"),
        (neq, ":agent2", ":agent"),
        (agent_get_team, ":team2", ":agent2"),
        (eq, ":team", ":team2"),
        (agent_is_alive, ":agent2"),
        (agent_is_active, ":agent2"),
        (agent_is_human, ":agent2"),
        (agent_get_position, pos2, ":agent2"),
        (get_distance_between_positions_in_meters, ":distance", pos1, pos2),
        (le, ":distance", 10),
        (store_agent_hit_points, ":hp", ":agent2"),
        (val_add, ":hp", 2),
        (val_min, ":hp", 101),
        (agent_set_hit_points, ":agent2", ":hp"),
        (try_begin),
          (eq, ":agent2", ":p_agent"),
          (display_message, "@You feel secured standing near the banner, healing some of your HP.", 0x6495ed),
        (try_end),
      (try_end),
    (try_end),
    
    #player
    (assign, ":agent", ":p_agent"),
    (agent_is_alive, ":agent"),
    (agent_get_wielded_item, ":item", ":agent", 0),
    (is_between, ":item",itm_flag_pole_1,itm_cross +1),
    (agent_get_team, ":team", ":agent"),
    (agent_get_position, pos1, ":agent"),
    (try_for_range, ":agent2"),
      (neq, ":agent2", ":agent"),
      (agent_get_team, ":team2", ":agent2"),
      (eq, ":team", ":team2"),
      (agent_is_alive, ":agent2"),
      (agent_is_active, ":agent2"),
      (agent_is_human, ":agent2"),
      (agent_get_position, pos2, ":agent2"),
      (get_distance_between_positions_in_meters, ":distance", pos1, pos2),
      (le, ":distance", 10),
      (store_agent_hit_points, ":hp", ":agent2"),
      (try_begin), ##cross does extra bonus
        (eq, ":item", itm_cross),
        (val_add, ":hp", 1),
      (try_end),
      (val_add, ":hp", 5),
      (val_max, ":hp", 101),
      (agent_set_hit_points, ":agent2", ":hp"),
    (try_end),
])

##MOVED TO THE MAIN LANCE_USAGE SCRIPT
# force_banners = ( #tom made
  # 1, 5, 0, [(eq, "$tom_use_banners", 1), (eq,0,1),],
   # [
           # (try_for_agents, ":agent"), #if the bastard has a flag, he must carry it.
          # (agent_is_alive, ":agent"),
          # (agent_is_human, ":agent"),
          # (agent_is_non_player, ":agent"),
          # (try_begin),
            # (agent_has_item_equipped, ":agent", "itm_flag_pole_1"),
            # (agent_set_wielded_item, ":agent", "itm_flag_pole_1"),
          # (else_try),
            # (agent_has_item_equipped, ":agent", "itm_flag_pole_2"),
            # (agent_set_wielded_item, ":agent", "itm_flag_pole_2"),
          # (else_try),
            # (agent_has_item_equipped, ":agent", "itm_flag_pole_3"),
            # (agent_set_wielded_item, ":agent", "itm_flag_pole_3"),
          # (try_end),
        # (try_end),
   # ])   
   
football = ( #tom made
  0, 2, ti_once, [],
 [
 (set_fixed_point_multiplier, 100),
    (get_player_agent_no, ":player"),
    (agent_get_position, pos1, ":player"),
    (position_set_z_to_ground_level, pos1),
    (position_get_z, ":z" ,pos1), 
    (val_add, ":z", 2500),
    (position_set_z, pos1, ":z"),
    (set_spawn_position, pos1),
    (spawn_scene_prop, "spr_football_skull"),

    # (prop_instance_enable_physics, reg0, 1),
 ]) 
   
common_charge_refill_ammo = (
  120, 0, 0, [],
  [
    (display_message, "@refilling projectiles", 0x00ff00),
    (try_for_agents, ":cur_agent"),
      #(eq, "$refil_count", 0),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_refill_ammo, ":cur_agent"),
      #(val_add, "$refil_count", 2),
    (try_end),
    #(val_sub, "$refil_count", 1)
  ])
make_them_cough =(
  3, 0, 0, [],
  [
    (display_message, "@forcing a cough", 0x00ff00),
    (try_for_agents, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (store_random_in_range, ":random_number", 0, 100),
      (try_begin),
        (eq, ":random_number", 0),
        (agent_play_sound, ":cur_agent", "snd_cough"),
      #(else_try),
      (try_end),
    (try_end),
  ]),
    
siege_tick =    (
  1, 0, 0, [],
  [
    (val_add, "$do_the_oil", 1),
########################### MAKES THE TROOPS CHARGE, MAKE ARCHERS HOLD POSITION AND ADVANCE 30 PACES (DO THIS ONCE AT START)
    # (try_begin),
      # (eq, "$Reloaded_siege_do_once", 0),
        # (assign, "$Reloaded_siege_do_once", 1),
        # (set_show_messages, 0),
        # (team_give_order, "$attacker_team", grc_everyone, mordr_fire_at_will),
        # (team_give_order, "$attacker_team2", grc_everyone, mordr_fire_at_will),
        # (agent_clear_scripted_mode, ":agent"), #attackers sometimes go funny             
        # (agent_force_rethink, ":agent"), #attackers sometimes go funny
        # (team_give_order, "$attacker_team", grc_archers, mordr_hold),
        # (team_give_order, "$attacker_team", grc_horse_archers, mordr_hold),
        # (team_give_order, "$attacker_team", grc_archers, mordr_stand_closer),
        # (team_give_order, "$attacker_team", grc_horse_archers, mordr_stand_closer),
        ######## ADVANCE 30 PACES
        # (team_give_order, "$attacker_team", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team", grc_horse_archers, mordr_advance),
        # (team_give_order, "$attacker_team", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team", grc_horse_archers, mordr_advance),
        # (team_give_order, "$attacker_team", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team", grc_horse_archers, mordr_advance),
        
        # (team_give_order, "$attacker_team2", grc_archers, mordr_hold),
        # (team_give_order, "$attacker_team2", grc_horse_archers, mordr_hold),
        # (team_give_order, "$attacker_team2", grc_archers, mordr_stand_closer),
        # (team_give_order, "$attacker_team2", grc_horse_archers, mordr_stand_closer),
        ######## ADVANCE 30 PACES       
        # (team_give_order, "$attacker_team2", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team2", grc_horse_archers, mordr_advance),
        # (team_give_order, "$attacker_team2", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team2", grc_horse_archers, mordr_advance),
        # (team_give_order, "$attacker_team2", grc_archers, mordr_advance),
        # (team_give_order, "$attacker_team2", grc_horse_archers, mordr_advance),
        # (agent_clear_scripted_mode, ":agent"), #attackers sometimes go funny             
        # (agent_force_rethink, ":agent"), #attackers sometimes go funny
        # (set_show_messages, 1),
    # (try_end),
    ############# modded 2x siege fix
    (val_add, "$MODDED2x_agentAIReset", 1),
    (try_begin),
      (ge, "$MODDED2x_agentAIReset", MODDED2x_AIAgentResetTimer),
          (assign, "$MODDED2x_agentAIReset", 0),
          #############( (display_message, "@Modded2 debug: Timer reset, NOW"),
    (try_end),
    # (try_begin),
      # (ge, "$MODDED2x_agentAIReset", MODDED2x_AIAgentResetNow),
          #############(display_message, "@Modded2 debug: AI agents reset, NOW"),
    # (try_end),
    # (set_show_messages, 0),
          # (team_give_order, "$attacker_team", grc_everyone, mordr_fire_at_will), #NOTE modde2x: make sure opposing AI is set to "Fire at Will"
          # (team_give_order, "$attacker_team2", grc_everyone, mordr_fire_at_will), #NOTE modde2x: make sure opposing AI is set to "Fire at Will"
    # (set_show_messages, 1),
    ############# modded 2x siege fix
    
    (try_begin),
      (gt, "$do_the_oil", oil_timer),
      (assign, "$do_the_oil", 0),
    (try_end),
    
    (get_player_agent_no, ":p_agent"),
    (try_for_agents, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_get_team, ":team", ":agent"),
      (this_or_next|eq, ":team", 1),
      (eq, ":team", 3),
      (neq, ":agent", ":p_agent"),
      (try_begin),
        (try_begin),
          (ge, "$MODDED2x_agentAIReset", MODDED2x_AIAgentResetNow),
            (agent_clear_scripted_mode, ":agent"), #attackers sometimes go funny             
            (agent_force_rethink, ":agent"), #attackers sometimes go funny
       (try_end),
############################# NEW v1.7 - attackers charge right away
       (try_begin),
         (eq, "$do_once_3", 0),
           (agent_clear_scripted_mode, ":agent"), #attackers sometimes go funny             
           (agent_force_rethink, ":agent"), #attackers sometimes go funny
           (assign, "$do_once_3", 1),
       (try_end),
      (try_end),

        
        
        
      ##boiling oil
      (try_begin),
        (le, "$do_the_oil", oil_timer), #every 5 sec
        (troop_get_slot, ":count", "trp_oil_array", 0),
        (try_for_range, ":slot", 1, ":count"),
          (troop_get_slot, ":prop", "trp_oil_array", ":slot"),
          (scene_prop_has_agent_on_it, ":prop", ":agent"),        
          (scene_prop_set_slot, ":prop", slot_prop_oil, 1),
          #(store_random_in_range, ":dmg", 20, 40),
          #(agent_deliver_damage_to_agent, ":agent", ":agent", ":dmg"),
          (store_agent_hit_points, ":hp", ":agent", 1),
          (val_sub, ":hp", 1),
          (try_begin),
            (gt, ":hp", 1),
            (agent_set_hit_points, ":agent", ":hp", 1),
          (else_try),
            (agent_deliver_damage_to_agent, ":agent", ":agent", 100),
          (try_end),
          (try_begin),
            (eq, ":agent", ":p_agent"),
            (display_message, "@You recieve damage from the hot oil spiled by the defenders on you!"),
          (try_end),
        (try_end),
      (try_end),
      (neq, ":agent", ":p_agent"),
      ##door brakedown
      (agent_get_position,pos0, ":agent"),
      (troop_get_slot, ":count", "trp_temp_array_c", 0),
      (try_for_range, ":slot", 1, ":count"),
        (troop_get_slot, ":prop", "trp_temp_array_c", ":slot"),
        (scene_prop_get_hit_points, ":hp", ":prop"),
        (gt, ":hp", 0),
        (prop_instance_get_position, pos1, ":prop"),
        (get_distance_between_positions_in_meters, ":distance",pos0,pos1),
        (le, ":distance", 1),
        (store_random_in_range, ":random", 0, 101),
        (le, ":random", 60),
        (agent_set_look_target_position, ":agent", pos1),
        (agent_set_attack_action, ":agent", 3, 0),
        (val_div, ":random", 10),
        (prop_instance_receive_damage, ":prop", ":agent", ":random"),
      (try_end),  
    (try_end),
    ##particle effects
    (le, "$do_the_oil", oil_timer), #every 5 sec
    (troop_get_slot, ":count", "trp_oil_array", 0),
    (try_for_range, ":slot", 1, ":count"),
      (troop_get_slot, ":prop", "trp_oil_array", ":slot"),
      (scene_prop_slot_eq, ":prop", slot_prop_oil, 1),
      (prop_instance_get_position, pos1, ":prop"),
      (particle_system_burst, "psys_gourd_smoke", pos1, 100),
      (position_move_z, pos1, 500, 1),
      (particle_system_burst, "psys_oil", pos1, 100),
      (scene_prop_set_slot, ":prop", slot_prop_oil, 0),
    (try_end),
  ])
  
siege_init =    (
  ti_before_mission_start, 0, 0, [],
  [
    (assign, ":slot", 1),
    (scene_prop_get_num_instances, ":count", "spr_1257_earth_gate"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_earth_gate", ":instance"),
      (troop_set_slot, "trp_temp_array_c", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (scene_prop_get_num_instances, ":count", "spr_1257_portcullis"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_portcullis", ":instance"),
      (troop_set_slot, "trp_temp_array_c", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (scene_prop_get_num_instances, ":count", "spr_1257_tavern_door_a"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_tavern_door_a", ":instance"),
      (troop_set_slot, "trp_temp_array_c", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (scene_prop_get_num_instances, ":count", "spr_1257_tavern_door_b"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_tavern_door_b", ":instance"),
      (troop_set_slot, "trp_temp_array_c", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (scene_prop_get_num_instances, ":count", "spr_1257_castle_f_door_a"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_castle_f_door_a", ":instance"),
      (troop_set_slot, "trp_temp_array_c", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (troop_set_slot, "trp_temp_array_c", 0, ":slot"),
    
    ##oils
    (assign, ":slot", 1),
    (scene_prop_get_num_instances, ":count", "spr_1257_hit_spot_2m"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_hit_spot_2m", ":instance"),
      (troop_set_slot, "trp_oil_array", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),
    (scene_prop_get_num_instances, ":count", "spr_1257_hit_spot_4m"),
    (try_for_range, ":instance" , 0, ":count"),
      (scene_prop_get_instance, ":prop", "spr_1257_hit_spot_4m", ":instance"),
      (troop_set_slot, "trp_oil_array", ":slot", ":prop"),
      (val_add, ":slot", 1),
      (scene_prop_set_team, ":prop", 2),
    (try_end),

    (troop_set_slot, "trp_oil_array", 0, ":slot"),
    (assign, "$do_the_oil", 0),
    
    ######## fix archers not firing at start
    # (assign, "$MODDED2x_agentAIReset", 0),
    # (team_give_order, "$attacker_team", grc_everyone, mordr_fire_at_will),
    # (team_give_order, "$attacker_team2", grc_everyone , mordr_fire_at_will),
    
  ]) 
  
siege_attacker_regroup = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent"),
    # (agent_get_team, ":team", ":agent"),
    # (this_or_next|eq, ":team", 1), #attacker 1
    # (eq, ":team", 3), # attacker 2
    # (agent_get_troop_id, ":troop", ":agent"),
    (agent_set_division, ":agent", grc_infantry),
    (try_for_range, ":r", "itm_hunting_bow", "itm_arrows"),
      (agent_has_item_equipped, ":agent", ":r"),
      (agent_set_division, ":agent", grc_archers),
    (try_end),
  ]) 

siege_battle_size_before_battle = (
  ti_before_mission_start, 0, 0, [],
  [

  ]) 
  
 
ad1257_common_triggers = [
  change_weather,
  sand_storm,
  #coordinator,
  #force_banners, ##TODO - main loop
  bastards_with_banners,
  bastards_with_banners_bonus,
  rain_storm,
  blizzard_strom,
  rain_storm_sound,
  blizzard_sound,
  desert_storm_sound,
  cheer_trigger,
  command_cheer,
  common_kill_count,
  reset_troop_array_for_combat,
  check_spawned_troop,
  #test,
  #test2,
  #make_them_cough,
  #common_charge_refill_ammo,
]

auxiliary_player = [
    initialise_auxiliary_player,
    auxiliary_player_check,
    auxiliary_player_check_freelancer,  ########## NEW v2.1
]

sexy_boots_trigger = (
    ti_on_agent_spawn, 0, 0, 
    [], 
    [
       (store_trigger_param_1, ":agent"),
       (call_script, "script_set_matching_sexy_boots", ":agent"),
    ]
)

must_1257_triggers = [
    sexy_boots_trigger,
    #shader_tweaks
    #first_person
]
  
euro_hillside_generator = (     #Tom made
  0, 0, ti_once, 
  [
    (eq, "$tom_generate_euro_hillside", 1)
  ],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_euro_hillside", 0),
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    
    (val_div, ":x_max", 2), #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":y_max", 2), #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    #rocks
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 300),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x",  ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y",  ":y_min", ":y_max"),
         #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2),
        (val_mul, ":pos_y", 2),
        #set random position for the spawn point
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        #(val_add, ":pos_z", 2),
        (lt, ":pos_z", 1500),
        (position_set_z, pos1, ":pos_z"),
        
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #randomize the size of the rock
        (store_random_in_range, ":x",  55, 100), 
        (store_random_in_range, ":y",  55, 100), 
        (store_random_in_range, ":z",  55, 100), 
        #spawn random prop
        (store_random_in_range, ":prop", "spr_rock1", "spr_desert_tree_aa"), #spawn random rock #"spr_valleyRock_rounded_4", "spr_tree_14_a"
        (spawn_scene_prop, ":prop"),
        #rescale the prop
        (prop_instance_set_scale, reg0, ":x", ":y", ":z"),
    (try_end),    
    #bushes
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 500),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #(store_random_in_range, ":prop", "spr_bushes10_a", "spr_bushes10_c"),
        (spawn_scene_prop, "spr_seedy_plant_a"),
    (try_end),
    #tree - bushes
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 300),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        (lt, ":pos_z", 1500),
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        (store_random_in_range, ":prop", "spr_bushes10_a", "spr_bushes10_c"),
        (spawn_scene_prop, ":prop"),
    (try_end),    
])  
  
rocky_generator = (     #Tom made
  0, 0, ti_once, 
  [
    (eq, "$tom_generate_desert", 1)
  ],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_desert", 0),
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    
    (val_div, ":x_max", 2), #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":y_max", 2), #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 1300),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x",  ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y",  ":y_min", ":y_max"),
        (val_mul, ":pos_x", 2), #double the size, or the props will not cover all the scene
        (val_mul, ":pos_y", 2), #double the size, or the props will not cover all the scene
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        #(val_add, ":pos_z", 2),
        (position_set_z, pos1, ":pos_z"),
        
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        
        (store_random_in_range, ":x",  15, 56), #randomize the size of the rock
        (store_random_in_range, ":y",  15, 56), #randomize the size of the rock
        (store_random_in_range, ":z",  20, 56), #randomize the size of the rock
        
        (store_random_in_range, ":prop", "spr_valleyRock_flatRounded_small_1", "spr_tree_14_a"), #spawn random rock
        (spawn_scene_prop, ":prop"),
        (prop_instance_set_scale, reg0, ":x", ":y", ":z"),
    (try_end),
    
])

iberian_generator2 = (     #Tom made
  0, 0, ti_once, [(eq, "$tom_generate_iberian2", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_iberian2", 0),
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    (val_div, ":x_max", 2),
    (val_div, ":y_max", 2), 
    #big pine generate
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 300),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        (store_random_in_range, ":prop", "spr_tree_16_a", "spr_pine_1_b"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    #small pine
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 20),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        (store_random_in_range, ":prop", "spr_pine_1_b", "spr_seedy_plant_a"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    
    #(set_fixed_point_multiplier, 100),
  ]
  )

iberian_generator = (     #Tom made
  0, 0, ti_once, [(eq, "$tom_generate_iberian", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_iberian", 0),
    #get and store the minimum and maximum positions of the scene
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":x_max", 2),
    (val_div, ":y_max", 2), 

    #tree generate
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 130),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        
        (store_random_in_range, ":size",  40, 100), #randomize the size of the tree
        #spawn random prop
        (store_random_in_range, ":prop", "spr_desert_tree_aa", "spr_tree_16_a"),
        (spawn_scene_prop, ":prop"),
        (prop_instance_set_scale, reg0, ":size", ":size", ":size"),
    (try_end),
    #bush generator
    # (val_max, "$tom_generate_reduction", 1),
    # (assign, ":higher_value", 145),
    # (val_div, ":higher_value", "$tom_generate_reduction"),
    # (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        # (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        # (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        ##double the size, or the props will not cover all the scene
        # (val_mul, ":pos_x", 2), 
        # (val_mul, ":pos_y", 2),
        # (position_set_x, pos1, ":pos_x"),
        # (position_set_y, pos1, ":pos_y"),
        # (position_set_z_to_ground_level, pos1),
        # (position_get_z, ":pos_z", pos1),
        # (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        ##rotate it 
        # (store_random_in_range, ":rotation", 0, 360),
        # (position_rotate_z, pos1, ":rotation"),
        # (set_spawn_position, pos1),
        
        # (store_random_in_range, ":size",  70, 100), #randomize the size of the tree
        # (spawn_scene_prop, "spr_small_plant_c"),
        # (prop_instance_set_scale, reg0, ":size", ":size", ":size"),
    # (try_end),
    
    #(set_fixed_point_multiplier, 100),
])

palm_generator = (     #Tom made
  0, 0, ti_once, [(eq, "$tom_generate_desertv2", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_desertv2", 0),
    #get and store the minimum and maximum positions of the scene
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":x_max", 2),
    (val_div, ":y_max", 2), 
    #generate rocks
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 500),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x",  ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y",  ":y_min", ":y_max"),
         #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2),
        (val_mul, ":pos_y", 2),
        #set random position for the spawn point
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        #(val_add, ":pos_z", 2),
        (position_set_z, pos1, ":pos_z"),
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #randomize the size of the rock
        (store_random_in_range, ":x",  15, 66), 
        (store_random_in_range, ":y",  15, 66), 
        (store_random_in_range, ":z",  30, 66), 
        #spawn random prop
        (store_random_in_range, ":prop", "spr_valleyRock_flatRounded_small_1", "spr_tree_14_a"), #spawn random rock #"spr_valleyRock_rounded_4", "spr_tree_14_a"
        (spawn_scene_prop, ":prop"),
        #rescale the prop
        (prop_instance_set_scale, reg0, ":x", ":y", ":z"),
    (try_end),    
    #grass generate
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 900),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_seedy_plant_a", "spr_palm_aa"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 250),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_palm_aa", "spr_valleyRock_flatRounded_small_1"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    
    #(set_fixed_point_multiplier, 100),
])

nile_generator = (     #Tom made
  0, 0, ti_once, [(eq, "$tom_generate_desertv3", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_desertv3", 0),
    #get and store the minimum and maximum positions of the scene
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":x_max", 2),
    (val_div, ":y_max", 2), 
    #generate bush
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 900),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_seedy_plant_a", "spr_palm_aa"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 400),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2),
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        (position_get_z, ":pos_z", pos1),
        (ge, ":pos_z", 1),  #check if not bellow 0, so they would not spam in water.
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_palm_aa", "spr_valleyRock_flatRounded_small_1"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    
    #(set_fixed_point_multiplier, 100),
])

swampy_generator = (     #Tom made
  0, 0, ti_once, [(eq, "$tom_generate_swamp", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    (assign, "$tom_generate_swamp", 0),
    #get and store the minimum and maximum positions of the scene
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":x_max", 2), 
    (val_div, ":y_max", 2),
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 480),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2), 
        #set random position for the spawn point
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_tree_14_a", "spr_tree_8_a"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    #(set_fixed_point_multiplier, 100),
])

snowy_generator = (     #Tom made
  0, 0, ti_once, [(ge, "$tom_generate_snow", 1)],
  [    
    (set_fixed_point_multiplier, 100),
    
    #get and store the minimum and maximum positions of the scene
    (get_scene_boundaries, pos1, pos0),
    (position_get_x, ":x_max", pos0),
    (position_get_y, ":y_max", pos0),
    (position_get_x, ":x_min", pos1),
    (position_get_y, ":y_min", pos1),
    #becouse the map is larger then 16bit int, and stora random only goes as high as a 16bit int.
    (val_div, ":x_max", 2), 
    (val_div, ":y_max", 2),
    (val_max, "$tom_generate_reduction", 1),
    (assign, ":higher_value", 300),
    (try_begin),
      (eq, "$tom_generate_snow", 2), #generate forest
      (assign, ":higher_value", 500),
    (try_end), 
    (assign, "$tom_generate_snow", 0),
    (val_div, ":higher_value", "$tom_generate_reduction"),
    (try_for_range, reg10, 0, ":higher_value"), #how many to generate
        (store_random_in_range, ":pos_x", ":x_min", ":x_max"),
        (store_random_in_range, ":pos_y", ":y_min", ":y_max"),
        #double the size, or the props will not cover all the scene
        (val_mul, ":pos_x", 2), 
        (val_mul, ":pos_y", 2), 
        #set random position for the spawn point
        (position_set_x, pos1, ":pos_x"),
        (position_set_y, pos1, ":pos_y"),
        (position_set_z_to_ground_level, pos1),
        #rotate it 
        (store_random_in_range, ":rotation", 0, 360),
        (position_rotate_z, pos1, ":rotation"),
        (set_spawn_position, pos1),
        #spawn random prop
        (store_random_in_range, ":prop", "spr_tree_snowy_a", "spr_test_helmet"),
        (spawn_scene_prop, ":prop"),
    (try_end),
    #(set_fixed_point_multiplier, 100),
])

ad1257_common_terrain_triggers = [
  palm_generator,
  iberian_generator,
  iberian_generator2,
  rocky_generator,
  swampy_generator,
  euro_hillside_generator,
  nile_generator,
  snowy_generator,
  # euro_forest_generator,
]  

spearwall_trigger_1 = (0.2, 0, ti_once, [], [
        (assign, "$spear_in_position",0),
        (try_for_agents, ":agent"),
          (agent_set_slot, ":agent",slot_agent_spearwall,0),
          (agent_set_slot, ":agent",slot_agent_x,0),
          (agent_set_slot, ":agent",slot_agent_y,0),
          (agent_set_slot, ":agent",slot_agent_z,0),
          (agent_set_slot, ":agent",slot_agent_speed,0),
        (try_end),
        ])

spearwall_trigger_2 = (0.5, 0, 0, [(eq, "$setting_use_spearwall",1)], [
        (set_fixed_point_multiplier, 100),
        (try_for_agents, ":agent"),
          (agent_is_alive, ":agent"),
          (agent_get_slot, ":oldagentx", ":agent",slot_agent_x),
          (agent_get_slot, ":oldagenty", ":agent",slot_agent_y),
          (agent_get_slot, ":oldagentz", ":agent",slot_agent_z),
          (agent_get_position, pos1, ":agent"),
          (position_get_x, ":agentx",pos1),
          (position_get_y, ":agenty",pos1),
          (position_get_z, ":agentz",pos1),
          (position_set_x,pos2, ":oldagentx"),
          (position_set_y,pos2, ":oldagenty"),
          (position_set_z,pos2, ":oldagentz"),
          (position_set_x,pos1, ":agentx"),
          (position_set_y,pos1, ":agenty"),
          (position_set_z,pos1, ":agentz"),
          #(get_distance_between_positions, ":speed",pos1,pos2),

          (agent_get_speed, pos5, ":agent"),
          (call_script, "script_vector_length", pos5),
          (assign, ":speed", reg0),
          (agent_set_slot, ":agent",slot_agent_x, ":agentx"),
          (agent_set_slot, ":agent",slot_agent_y, ":agenty"),
          (agent_set_slot, ":agent",slot_agent_z, ":agentz"),
          (agent_set_slot, ":agent",slot_agent_speed, ":speed"),
        (try_end),
          (set_fixed_point_multiplier, 100),
        ])

spearwall_trigger_3 = (0, 0, 0, [(eq, "$spear_in_position",1),(this_or_next|game_key_clicked, gk_attack),
        (this_or_next|game_key_clicked, gk_defend),(this_or_next|game_key_clicked, gk_defend),
        (this_or_next|game_key_clicked, gk_move_forward),(this_or_next|game_key_clicked, gk_move_backward),
        (this_or_next|game_key_clicked, gk_move_left),(this_or_next|game_key_clicked, gk_move_right),
        (this_or_next|game_key_clicked, gk_equip_primary_weapon),(this_or_next|game_key_clicked, gk_equip_secondary_weapon),
        (this_or_next|game_key_clicked, gk_action),(game_key_clicked, gk_sheath_weapon),
        ],
       [(get_player_agent_no, ":player"),
        (agent_is_alive, ":player"),
        (display_message, "@Releasing spear.",0x6495ed),
        (agent_set_animation, ":player", "anim_release_thrust_staff"),
        (assign, "$spear_in_position",0),
        ])

spearwall_trigger_4 = (0.2, 0, 0, [(eq, "$setting_use_spearwall",1)], [
        (try_for_agents, ":agent"),
          (agent_get_horse, ":horse", ":agent"),
          (neg|gt, ":horse",0),
          (agent_get_slot, ":speartimer", ":agent",slot_agent_spearwall),
          (lt, ":speartimer",10),
          (val_add, ":speartimer",2),
          (agent_set_slot, ":agent",slot_agent_spearwall, ":speartimer"),
        (try_end),
        ])

spearwall_trigger_5 = (3, 0, 0, [(eq, "$spear_in_position",1)],[
        (get_player_agent_no, ":player"),
        (agent_is_alive, ":player"),
        (agent_set_animation, ":player", "anim_spearwall_hold"),
        ])

spearwall_trigger_6 = (0.1, 0, 0, [(eq, "$setting_use_spearwall",1)], [
        (get_player_agent_no, ":player"),
        (agent_get_team, ":playerteam", ":player"),
        (try_for_agents, ":agent"),
           (agent_is_alive, ":agent"),
           (neq, ":agent", ":player"),
           (agent_is_human, ":agent"),
           (agent_get_horse, ":horse", ":agent"),
           (neg|gt, ":horse",0),
           (agent_get_slot, ":speartimer", ":agent",slot_agent_spearwall),
           (ge, ":speartimer",10),
           (agent_get_simple_behavior, ":state", ":agent"),
           (agent_get_team, ":team1", ":agent"),
           (agent_get_class, ":class", ":agent"),
           (team_get_movement_order, ":order", ":team1", ":class"),
           (assign, ":continue",0),
           (try_begin),
              (neq, ":team1", ":playerteam"),
              (this_or_next|eq, ":state",aisb_hold),
              (this_or_next|eq, ":state",aisb_flock),
              (eq, ":state",aisb_go_to_pos),
              (assign, ":continue",1),
           (else_try),
              (this_or_next|eq, ":order",mordr_hold),
              (eq, ":order",mordr_stand_ground),
              (this_or_next|eq, ":state",aisb_hold),
              (this_or_next|eq, ":state",aisb_flock),
              (this_or_next|eq, ":state",aisb_melee),
              (eq, ":state",aisb_go_to_pos),
              (assign, ":continue",1),
           (try_end),
           (eq, ":continue",1),
           (agent_get_troop_id, ":agent_troop", ":agent"),
           (store_proficiency_level, ":polearms", ":agent_troop", wpt_polearm),
           (store_character_level, ":troop_level", ":agent_troop"),
           (ge, ":troop_level", 12),
           (ge, ":polearms", 120),
           (neg|troop_is_mounted, ":agent_troop"),

           (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Isn't routing.
           (assign, ":continue",0),
           (agent_get_wielded_item, ":handone", ":agent", 0),
           (agent_get_wielded_item, ":handtwo", ":agent", 1),
           (assign, ":speardist",145),

           (try_for_range, ":spear", "itm_bamboo_spear", "itm_wooden_shield"),
              (this_or_next|eq, ":handone", ":spear"),
              (eq, ":handtwo", ":spear"),
              (assign, ":continue",1),
              (try_begin),
                (eq, ":spear", "itm_bamboo_spear"),
                (assign, ":speardist", 200),
              (else_try),
                (eq, ":spear", "itm_spear_a"),
                (assign, ":speardist", 156),
              (else_try),
                (eq, ":spear", "itm_spear_b"),
                (assign, ":speardist", 155),
              (else_try),
                (eq, ":spear", "itm_spear_c"),
                (assign, ":speardist", 135),
              (else_try),
                (eq, ":spear", "itm_spear_d"),
                (assign, ":speardist", 143),
              (else_try),
                (eq, ":spear", "itm_spear_e"),
                (assign, ":speardist", 142),
              (else_try),
                (eq, ":spear", "itm_spear_f"),
                (assign, ":speardist", 146),
              (else_try),
                (eq, ":spear", "itm_spear_g"),
                (assign, ":speardist", 142),
              (else_try),
                (eq, ":spear", "itm_spear_h"),
                (assign, ":speardist", 145),
              (else_try),
                (eq, ":spear", "itm_spear_i"),
                (assign, ":speardist", 141),
              (else_try),
                (eq, ":spear", "itm_spear_j"),
                (assign, ":speardist", 170),
              (else_try),
                (eq, ":spear", "itm_spear_k"),
                (assign, ":speardist", 160),
              (else_try),
                (eq, ":spear", "itm_spear_l"),
                (assign, ":speardist", 170),
              (else_try),
                (eq, ":spear", "itm_spear_m"),
                (assign, ":speardist", 160),
              (else_try),
                (eq, ":spear", "itm_spear_n"),
                (assign, ":speardist", 175),
              (else_try),
                (eq, ":spear", "itm_spear_o"),
                (assign, ":speardist", 150),
              (else_try),
                (eq, ":spear", "itm_spear_p"),
                (assign, ":speardist", 160),
              (try_end),
           (try_end),

           (eq, ":continue",1),
           # (try_begin),
             # (this_or_next|eq, ":order",mordr_hold),
              # (eq, ":order",mordr_stand_ground),
             # (agent_set_animation, ":agent", "anim_spearwall_hold"),
           # (try_end),
           (assign, ":victim",-1),
           (agent_get_position,pos1, ":agent"),
           (try_for_agents, ":possible_victim"),
              (agent_is_alive, ":possible_victim"),
              (neg|agent_is_human, ":possible_victim"),
              (agent_get_rider, ":rider", ":possible_victim"),
              (ge, ":rider",0),
              (agent_get_team, ":team2", ":rider"),
              (teams_are_enemies, ":team1", ":team2"),
              (agent_get_position,pos2, ":possible_victim"),
              (get_distance_between_positions, ":dist",pos1,pos2),
              (lt, ":dist", ":speardist"),
              (neg|position_is_behind_position,pos2,pos1),
              (agent_get_slot, ":speed", ":possible_victim",slot_agent_speed),
              (gt, ":speed",0), # Remember to change this if the timing on speed checks changes
              (assign, ":victim", ":possible_victim"),
           (try_end),
           (gt, ":victim",-1),
           #(agent_set_animation, ":agent", "anim_spearwall_hold"),
           #(agent_set_attack_action, ":agent", 0, 1),
           (agent_play_sound, ":victim", "snd_metal_hit_high_armor_high_damage"),
           (store_agent_hit_points, ":hp", ":victim",0),
           (store_agent_hit_points, ":oldhp", ":victim",1),
           (assign, reg22, ":speed"),
           (val_mul, ":speed", 10),
           (val_sub, ":hp", ":speed"),
           (val_max, ":hp",0),
           (agent_set_slot, ":agent",slot_agent_spearwall,0),
           (agent_get_horse, ":playerhorse", ":player"),
           #(agent_set_hit_points, ":victim", ":hp",0),

           (agent_get_position,pos2, ":victim"),
           (agent_set_look_target_position, ":agent", pos2),
           (agent_set_attack_action, ":agent", 0, 0),

           #(agent_deliver_damage_to_agent, ":victim", ":victim"),
           
           (agent_deliver_damage_to_agent, ":agent", ":victim"),
           (agent_deliver_damage_to_agent, ":agent", ":victim"),
           (agent_deliver_damage_to_agent, ":agent", ":victim"),
           (agent_deliver_damage_to_agent, ":agent", ":victim"),
           # (agent_deliver_damage_to_agent, ":agent", ":victim"),
           # (agent_deliver_damage_to_agent, ":agent", ":victim"),
           # (agent_deliver_damage_to_agent, ":agent", ":victim"),
           #(agent_deliver_damage_to_agent, ":agent", ":victim"),

           (agent_get_troop_id, ":agent_troop", ":agent"),
           (str_store_troop_name, s21, ":agent_troop"),
           (agent_get_troop_id, ":victim_troop", ":victim"),
           (str_store_troop_name, s20, ":victim_troop"),
           (store_agent_hit_points, ":hp", ":victim",1),
           (val_sub, ":oldhp", ":hp"),
           (assign,reg1, ":oldhp"),

           # (display_message, "@{s20}'s horse receives {reg1} damage from {s21}'s braced spear! speed {reg22}",info_clr),

           (try_begin),
              (eq, ":victim", ":playerhorse"),
              # (store_agent_hit_points, ":hp", ":victim",1),
              # (val_sub, ":oldhp", ":hp"),
              # (assign,reg1, ":oldhp"),
              (display_message, "@Your horse received {reg1} damage from a braced spear!",0xff4040),
           (try_end),

        (try_end),
        (set_fixed_point_multiplier, 100),
        ])
spearwall_trigger_7 = (0.1, 0, 0, [(eq, "$spear_in_position",1)], [
        (get_player_agent_no, ":player"),
        (agent_is_alive, ":player"),
        (store_agent_hit_points, ":hp", ":player",1),
        (lt, ":hp", "$spear_hp"),
        (display_message, "@The injury causes your grip on the spear to slip!",0xff4040),
        (agent_set_animation, ":player", "anim_release_thrust_staff"),
        (assign, "$spear_in_position",0),
        (set_fixed_point_multiplier, 100),
        ])

spearwall_trigger_8 = (0.1, 0, 0, [(eq, "$spear_in_position",1)], [
        (get_player_agent_no, ":player"),
        (agent_is_alive, ":player"),
        (agent_get_slot, ":speartimer", ":player",slot_agent_spearwall),
        (ge, ":speartimer",10),
        (assign, ":victim",-1),
        (agent_get_position,pos1, ":player"),
        (try_for_agents, ":possible_victim"),
           (agent_is_alive, ":possible_victim"),
           (neg|agent_is_human, ":possible_victim"),
           (agent_get_rider, ":rider", ":possible_victim"),
           (ge, ":rider",0),
           (neg|agent_is_ally, ":rider"),
           (agent_get_position,pos2, ":possible_victim"),
           (get_distance_between_positions, ":dist",pos1,pos2),
           (lt, ":dist", "$spear_dist"),
           (neg|position_is_behind_position,pos2,pos1),
           (agent_get_slot, ":speed", ":possible_victim",slot_agent_speed),
           (ge, ":speed",120), # Remember to change this if the timing on speed checks changes
           (assign, ":victim", ":possible_victim"),
        (try_end),
        (gt, ":victim",-1),
        (agent_play_sound, ":victim", "snd_metal_hit_high_armor_high_damage"),
        (store_agent_hit_points, ":hp", ":victim",0),
        (store_agent_hit_points, ":oldhp", ":victim",1),
        (val_div, ":speed",2), # Remember to change this if the timing on speed checks changes
        (val_sub, ":speed",15),
        (val_sub, ":hp", ":speed"),
        (val_max, ":hp",0),
        (agent_set_hit_points, ":victim", ":hp",0),
        (agent_deliver_damage_to_agent, ":victim", ":victim"),
        (agent_set_slot, ":player",slot_agent_spearwall,0),
        (store_agent_hit_points, ":hp", ":victim",1),
        (val_sub, ":oldhp", ":hp"),
        (assign,reg1, ":oldhp"),
        (display_message, "@Spear-wall dealt {reg1} damage!"),
        (set_fixed_point_multiplier, 100),

        ])
spearwall_trigger_9 = (0, 0, 2, [(key_clicked, key_b),(eq, "$setting_use_spearwall",1)],
       [(assign, ":continue",0),
        (get_player_agent_no, ":player"),
        (agent_is_alive, ":player"),
        (agent_get_wielded_item, ":handone", ":player", 0),
        (agent_get_wielded_item, ":handtwo", ":player", 1),
        (assign, "$spear_dist",145),
        (try_for_range, ":spear", "itm_bamboo_spear", "itm_wooden_shield"),
            (this_or_next|eq, ":handone", ":spear"),
            (eq, ":handtwo", ":spear"),
            (assign, ":continue",1),
              (try_begin),
                (eq, ":spear", "itm_bamboo_spear"),
                (assign, "$spear_dist", 200),
              (else_try),
                (eq, ":spear", "itm_spear_a"),
                (assign, "$spear_dist", 156),
              (else_try),
                (eq, ":spear", "itm_spear_b"),
                (assign, "$spear_dist", 155),
              (else_try),
                (eq, ":spear", "itm_spear_c"),
                (assign, "$spear_dist", 135),
              (else_try),
                (eq, ":spear", "itm_spear_d"),
                (assign, "$spear_dist", 143),
              (else_try),
                (eq, ":spear", "itm_spear_e"),
                (assign, "$spear_dist", 142),
              (else_try),
                (eq, ":spear", "itm_spear_f"),
                (assign, "$spear_dist", 146),
              (else_try),
                (eq, ":spear", "itm_spear_g"),
                (assign, "$spear_dist", 142),
              (else_try),
                (eq, ":spear", "itm_spear_h"),
                (assign, "$spear_dist", 145),
              (else_try),
                (eq, ":spear", "itm_spear_i"),
                (assign, "$spear_dist", 141),
              (else_try),
                (eq, ":spear", "itm_spear_j"),
                (assign, "$spear_dist", 170),
              (else_try),
                (eq, ":spear", "itm_spear_k"),
                (assign, "$spear_dist", 160),
              (else_try),
                (eq, ":spear", "itm_spear_l"),
                (assign, "$spear_dist", 170),
              (else_try),
                (eq, ":spear", "itm_spear_m"),
                (assign, "$spear_dist", 160),
              (else_try),
                (eq, ":spear", "itm_spear_n"),
                (assign, "$spear_dist", 175),
              (else_try),
                (eq, ":spear", "itm_spear_o"),
                (assign, "$spear_dist", 150),
              (else_try),
                (eq, ":spear", "itm_spear_p"),
                (assign, "$spear_dist", 160),
              (try_end),
        (try_end),
        (eq, ":continue",1),
          (agent_get_horse, ":horse", ":player"),
        (neg|gt, ":horse",0),
        (neq, "$spear_in_position", 1),
        (display_message, "@Bracing spear for charge.",0x6495ed),
        (agent_set_animation, ":player", "anim_spearwall_hold"),
        (assign, "$spear_in_position", 1),
        (store_agent_hit_points, "$spear_hp", ":player",1),
        (set_fixed_point_multiplier, 100),
        ])

#spearwall_triggers = spearwall_trigger_1 + spearwall_trigger_2 + spearwall_trigger_3 + spearwall_trigger_4 + spearwall_trigger_5 + spearwall_trigger_6 + spearwall_trigger_7 + spearwall_trigger_8
################################################
## Shield Bash                                ##
## Developed by 'xenoargh' for singleplayer.  ##
## Revamped by 'Sinisterius'. ##
## Animations Copyright (C) 2010 'xenoargh'.  ##
################################################


#####
#Add these following triggers to module_mission_templates.py,
#above all other code. Then simply add:
#sp_shield_bash_1,
#sp_shield_bash_2,
#sp_shield_bash_3,
#To your mission templates to activate the triggers.
sp_shield_bash_triggers = [
  #sp_shield_bash_1 = (
   (0, 0, 0,
   [
       (eq, "$sp_shield_bash", 1),
        (game_key_is_down, gk_defend),
        (game_key_clicked, gk_attack),
   ],
   [
       (get_player_agent_no, ":agent"),
      (agent_is_active, ":agent"),
      (agent_is_alive, ":agent"),
      (neg|agent_slot_ge, ":agent", sp_agent_shield_bash_timer, 1), #Less than.
      (agent_get_wielded_item, ":item", ":agent", 1), #Offhand.
      (is_between, ":item", 1, "itm_items_end"),
      #(gt, ":item", 0),
      (item_get_type, ":type", ":item"),
      (eq, ":type", itp_type_shield), #Shield equipped.
      (agent_get_defend_action, ":action", ":agent"),
      (eq, ":action", 2), #Blocking.
      (agent_get_horse, ":horse", ":agent"),
      (eq, ":horse", -1), #No horse.
      (agent_set_slot, ":agent", sp_agent_shield_bash_timer, 3), #tom was 5
      (agent_set_animation, ":agent", "anim_shield_bash"),
      (agent_get_troop_id, ":troop", ":agent"),
      (troop_get_type, ":type", ":troop"),
      (try_begin),
          (eq, ":type", tf_male),
         (agent_play_sound, ":agent", "snd_man_yell"),
      (else_try),
          (eq, ":type", tf_female),
         (agent_play_sound, ":agent", "snd_woman_yell"),
      (try_end),
      (agent_get_position, pos1, ":agent"),
      (assign, ":victim", -1),
      (assign, ":minimum_distance", 150),
      (try_for_agents, ":suspect"),
         (agent_is_alive, ":suspect"),
         (agent_is_human, ":suspect"),
         (neg|agent_is_ally, ":suspect"),
         (agent_get_position, pos2, ":suspect"),
         (neg|position_is_behind_position, pos2, pos1), #Suspect can't be behind basher.
         (get_distance_between_positions, ":distance", pos1, pos2),
         (le, ":distance", ":minimum_distance"),
         (assign, ":minimum_distance", ":distance"),
         (assign, ":victim", ":suspect"),
      (try_end),
      (ge, ":victim", 0),
      (agent_play_sound, ":victim", "snd_wooden_hit_low_armor_high_damage"),
      (agent_get_defend_action, ":action", ":victim"),
      (try_begin),
         (eq, ":action", 2), #Blocking.
         (neg|position_is_behind_position, pos1, pos2), #If basher isn't behind victim.
         (agent_get_wielded_item, ":item", ":victim", 1), #Offhand.
         (is_between, ":item", 1, "itm_items_end"),
         #(gt, ":item", 0),
         (item_get_type, ":type", ":item"),
         (eq, ":type", itp_type_shield),
         (agent_set_animation, ":victim", "anim_shield_bash"),
      (else_try),
         (agent_set_animation, ":victim", "anim_shield_strike"),
      (try_end),
   ]),

   #sp_shield_bash_2 = (
   (1, 0, 0, [(eq, "$sp_shield_bash", 1)],
   [
       (get_player_agent_no, ":agent"),
      (agent_is_active, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_get_slot, ":timer", ":agent", sp_agent_shield_bash_timer),
      (val_sub, ":timer", 1),
      (val_max, ":timer", 0),
      (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":timer"),
   ]),

  #sp_shield_bash_3 = (
   # (0.25, 0, 0, [(eq, "$sp_shield_bash_ai", 1)],
   (0.4, 0, 0, [(eq, "$sp_shield_bash_ai", 1)],  ######### NEW v2.7 - decreased shield bash timer
   [
      (get_player_agent_no, ":player_agent"),
      (try_for_agents, ":agent"),
        (neq, ":agent", ":player_agent"),
        (agent_is_alive, ":agent"),
        (agent_is_human, ":agent"),
        (agent_get_troop_id, ":troop", ":agent"),
        (store_skill_level, ":level", "skl_shield", ":troop"),
        (store_proficiency_level, ":prof1h", ":troop", wpt_one_handed_weapon),
        (ge, ":level", 4), #If the :level is equal to or greater than to 4, then continue.
        (ge, ":prof1h", 200),
        #(neg | troop_is_mounted, ":troop"),
        (agent_get_horse, ":horse", ":agent"),#tom
        (le, ":horse", 0), #No horse.#tom
        (try_begin),
            (neg|agent_slot_ge, ":agent", sp_agent_shield_bash_timer, 1), #Less than.
            (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Isn't routing.
            (agent_get_wielded_item, ":item", ":agent", 1), #Offhand.
            #(gt, ":item", 0), #tom
            (is_between, ":item", 1, "itm_items_end"), # sometimes the upper range limit was strangely high
            (item_get_type, ":type", ":item"),
            (eq, ":type", itp_type_shield), #Shield equipped.
            (agent_get_attack_action, ":action", ":agent"),
            (eq, ":action", 0), #Free.
            #(agent_get_horse, ":horse", ":agent"),#tom
            #(eq, ":horse", -1), #No horse.#tom
            (agent_get_team, ":team", ":agent"),
            (agent_get_position, pos1, ":agent"),
            (assign, ":victim", -1),
            (assign, ":minimum_distance", 125),
            (try_for_agents, ":suspect"),
                (agent_is_alive, ":suspect"),
               (agent_is_human, ":suspect"),
               (agent_get_position, pos2, ":suspect"),
               (neg|position_is_behind_position, pos2, pos1), #Suspect can't be behind basher.
               (agent_get_team, ":suspect_team", ":suspect"),
               (neq, ":suspect_team", ":team"),
               #tom
               (try_begin),
                 (eq, ":team", 0),
                 (assign, ":ally_team", 2),
               (else_try),
                 (eq, ":team", 2),
                 (assign, ":ally_team", 0),   
               (else_try),
                 (eq, ":team", 1),
                 (assign, ":ally_team", 3),   
               (else_try),
                 (eq, ":team", 3),
                 (assign, ":ally_team", 1),   
               (try_end),
               #tom
               (neq, ":suspect_team", ":ally_team"),
               (get_distance_between_positions, ":distance", pos1, pos2),
               (le, ":distance", ":minimum_distance"),
               (assign, ":minimum_distance", ":distance"),
               (assign, ":victim", ":suspect"),
            (try_end),
            (ge, ":victim", 0),
            (agent_get_horse, ":horse", ":victim"),
            (eq, ":horse", -1),
            # (store_random_in_range, ":rand", 15, 26),
            (store_random_in_range, ":rand", 25, 32),  ######### NEW v2.7 - decreased shield bash timer
             (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":rand"), #20 is 20*0.25=5seconds.
            (agent_set_animation, ":agent", "anim_shield_bash"),
            (agent_get_troop_id, ":troop", ":agent"),
            (troop_get_type, ":type", ":troop"),
            (try_begin),
                (eq, ":type", tf_male),
               (agent_play_sound, ":agent", "snd_man_yell"),
            (else_try),
                (eq, ":type", tf_female),
               (agent_play_sound, ":agent", "snd_woman_yell"),
            (try_end),
            (agent_play_sound, ":victim", "snd_wooden_hit_low_armor_high_damage"),
            (agent_get_defend_action, ":action", ":victim"),
            (try_begin),
               (eq, ":action", 2), #Blocking.
               (neg|position_is_behind_position, pos1, pos2), #If basher isn't behind victim.
               (agent_get_wielded_item, ":item", ":victim", 1), #Offhand.
                 #(gt, ":item", 0),
               (is_between, ":item", 1, "itm_items_end"), # sometimes the upper range limit was strangely high
               (item_get_type, ":type", ":item"),
               (eq, ":type", itp_type_shield),
               (agent_set_animation, ":victim", "anim_shield_bash"),
            (else_try),
                (agent_set_animation, ":victim", "anim_shield_strike"),
            (try_end),
         (try_end),
         (agent_get_slot, ":timer", ":agent", sp_agent_shield_bash_timer),
         (val_sub, ":timer", 1),
         (val_max, ":timer", 0),
         (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":timer"),
      (try_end),
   ])
]

# Formations triggers v3 by motomataru, Warband port
# Global variables    *_formation_type holds type of formation: see "Formation modes" in module_constants
#                    *_formation_move_order hold the current move order for the formation
#                    *_space hold the multiplier of extra space ordered into formation by the player

formations_triggers = [
    (ti_before_mission_start, 0, 0, [], [
        (assign, "$gk_order", 0),
        (assign, "$gk_order_hold_over_there", 0),
        (assign, "$autorotate_at_player", formation_autorotate_at_player),
        (assign, "$fclock", 1),
        
        (try_for_range, ":team", 0, 4),
            (try_for_range, ":slot", slot_team_d0_type, slot_team_d0_type + 9),
                (team_set_slot, ":team", ":slot", sdt_unknown),    
            (try_end),
        (try_end),
        #ensure item slots are loaded whatever save game this is...
        (neq, "$new_session", 1),
        # # Autoloot improved by rubik begin
        (call_script, "script_init_item_score"),
        # # Autoloot improved by rubik end
        (assign, "$new_session", 1),
    ]),

# Start troops in formation
    (0, formation_delay_for_spawn, ti_once, [], [
        (get_player_agent_no, "$fplayer_agent_no"),
        (agent_get_team, "$fplayer_team_no", "$fplayer_agent_no"),
        (call_script, "script_store_battlegroup_data"),
        
        #get team faction
        (try_for_agents, ":cur_agent"),    #this part bogus; we need the mode of agent faction, not the mean. Add four faction slots for teams to help calculate efficiently.
            (agent_is_human, ":cur_agent"),
            (agent_get_team, ":cur_team", ":cur_agent"),
            (agent_get_troop_id, ":cur_troop", ":cur_agent"),
            (store_troop_faction, ":cur_faction", ":cur_troop"),
            (team_get_slot, ":team_avg_faction", ":cur_team", slot_team_faction),
            (val_add, ":team_avg_faction", ":cur_faction"),
            (team_set_slot, ":cur_team", slot_team_faction, ":team_avg_faction"),
        (try_end),
        
        (try_for_range, ":team", 0, 4),
            (team_slot_ge, ":team", slot_team_size, 1),
            (team_get_leader, ":fleader", ":team"),
            (try_begin),
                (ge, ":fleader", 0),
                (agent_get_troop_id, ":fleader_troop", ":fleader"),
                (store_troop_faction, ":team_faction", ":fleader_troop"),
            (else_try),
                (team_get_slot, ":team_size", ":team", slot_team_size),
                (team_get_slot, ":team_avg_faction", ":team", slot_team_faction),
                (store_mul, ":team_faction", ":team_avg_faction", 10),
                (val_div, ":team_faction", ":team_size"),
                (val_add, ":team_faction", 5),
                (val_div, ":team_faction", 10),
            (try_end),        
            (team_set_slot, ":team", slot_team_faction, ":team_faction"),
        (try_end),
        
        (display_message, "@Forming ranks."),
        #keep cavalry on the map
        # (assign, ":largest_mounted_division", -1),
        (assign, ":largest_mounted_division_size", 0),
        (try_for_range, ":division", 0, 9),
            (store_add, ":slot", slot_team_d0_type, ":division"), 
            (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
            (team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
            (store_add, ":slot", slot_team_d0_size, ":division"),
            (team_get_slot, reg0, "$fplayer_team_no", ":slot"),
            (lt, ":largest_mounted_division_size", reg0),
            (assign, ":largest_mounted_division_size", reg0),
            # (assign, ":largest_mounted_division", ":division"),
        (try_end),
        
        (assign, ":depth_cavalry", 0),
        (try_begin),
            (gt, ":largest_mounted_division_size", 0),
            (val_mul, ":largest_mounted_division_size", 2),
            (convert_to_fixed_point, ":largest_mounted_division_size"),
            (store_sqrt, ":depth_cavalry", ":largest_mounted_division_size"),
            (convert_from_fixed_point, ":depth_cavalry"),
            (val_sub, ":depth_cavalry", 1),
            
            # (store_add, ":slot", slot_team_d0_formation_space, ":largest_mounted_division"),
            # (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
            # (store_mul, reg0, ":div_spacing", 50),
            (store_mul, reg0, formation_start_spread_out, 50),
            (val_add, reg0, formation_minimum_spacing_horse_length),
            (val_mul, ":depth_cavalry", reg0),
            # (val_mul, ":depth_cavalry", formation_minimum_spacing_horse_length),    #formation spacing is 0 at start for cavalry
            
            (store_mul, ":depth_infantry", formation_start_spread_out, 50),
            (val_add, ":depth_infantry", formation_minimum_spacing),
            (val_mul, ":depth_infantry", 2),
            (val_sub, ":depth_cavalry", ":depth_infantry"),
            
            (try_begin),
                (gt, ":depth_cavalry", 0),
                (agent_get_position, pos49, "$fplayer_agent_no"),
                (copy_position, pos2, pos49),
                (call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
                (call_script, "script_point_y_toward_position", pos2, pos60),
                (position_move_y, pos2, ":depth_cavalry"),
                (agent_set_position, "$fplayer_agent_no", pos2),    #fake out script_battlegroup_place_around_leader
            (try_end),
        (try_end),

        #initial formations
        # (call_script, "script_division_reset_places"),
        # (try_for_range, ":division", 0, 9),
            # (store_add, ":slot", slot_team_d0_size, ":division"),
            # (team_slot_ge, "$fplayer_team_no", ":slot", 1),
            # (store_add, ":slot", slot_team_d0_type, ":division"), 
            # (try_begin),
                # (team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
                # (call_script, "script_player_attempt_formation", ":division", formation_default),
            # (else_try),
                # (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
                # (team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
                # (call_script, "script_player_attempt_formation", ":division", formation_wedge),
            # (else_try),
                # (call_script, "script_get_default_formation", "$fplayer_team_no"),
                # (call_script, "script_player_attempt_formation", ":division", reg0),
            # (try_end),
        # (try_end),

        # (try_begin),
            # (gt, ":depth_cavalry", 0),
            # (agent_set_position, "$fplayer_agent_no", pos49),
        # (try_end),
    ]),

    (0, .3, 0, [(game_key_clicked, gk_order_1)], [
        (eq, "$gk_order", gk_order_1),    #next trigger set MOVE menu?
        (try_begin),
            (game_key_is_down, gk_order_1),    #BUT player is holding down key?
            (assign, "$gk_order_hold_over_there", 1),
            (assign, "$gk_order", 0),
            (assign, "$holdit", 0),
        (else_try),
            (eq, "$holdit", 1),
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_hold),
            (assign, "$gk_order", 0),
            (assign, "$holdit", 0),
        (try_end),
    ]),

    (0, 0, 0, [(game_key_clicked, gk_order_1)], [
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_1),
            (assign, "$holdit", 0),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #HOLD        
            (assign, "$holdit", 1),
            (call_script, "script_first_formation_member_sound_horn"),  #tom 
            # (assign, "$fclock", 1),    #sent to delayed trigger above to override Native for unformed divisions
            # (call_script, "script_player_order_formations", mordr_hold),
            # (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #ADVANCE
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_advance),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #HOLD FIRE
            (assign, "$gk_order", 0),
        (try_end),
    ]),
    
    (0, 0, 0, [(game_key_clicked, gk_order_2)], [
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_2),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #FOLLOW
            (assign, "$fclock", 1),
            (call_script, "script_first_formation_member_sound_horn"),  #tom 
            (call_script, "script_player_order_formations", mordr_follow),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #FALL BACK
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_fall_back),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #FIRE AT WILL
            (assign, "$gk_order", 0),
        (try_end),
    ]),
    
    (0, 0, 0, [(game_key_clicked, gk_order_3)], [
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_3),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #CHARGE
            (assign, "$fclock", 1),
            (call_script, "script_first_formation_member_sound_horn"),  #tom     
            (call_script, "script_player_order_formations", mordr_charge),
            (assign, "$tom_yell_smelly_peasents", 1),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #SPREAD OUT
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_spread_out),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #BLUNT WEAPONS
            (assign, "$gk_order", 0),
        (try_end),
    ]),
    
    (0, 0, 0, [(game_key_clicked, gk_order_4)], [
        (try_begin),
            (eq, "$gk_order", 0),
            (assign, "$gk_order", gk_order_4),
            (start_presentation, "prsnt_order_display"),
            
        (else_try),
            (eq, "$gk_order", gk_order_1),    #STAND GROUND
            (assign, "$fclock", 1),
            (call_script, "script_first_formation_member_sound_horn"),  #tom     
            (call_script, "script_player_order_formations", mordr_stand_ground),    
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #STAND CLOSER
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_stand_closer),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #ANY WEAPON
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_4),    #FORMATION - RANKS
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", slot_team_d0_size, ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (assign, "$fclock", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_ranks),        
                (call_script, "script_first_formation_member_sound_horn"),  #tom                     
            (try_end),
            (assign, "$gk_order", 0),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),
    
    (0, 0, 0, [(game_key_clicked, gk_order_5)], [
        (try_begin),
            (eq, "$gk_order", gk_order_1),    #RETREAT
            (assign, "$fclock", 1),
            (call_script, "script_first_formation_member_sound_horn"),  #tom     
            (call_script, "script_player_order_formations", mordr_retreat),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #MOUNT
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - SHIELDWALL
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", slot_team_d0_size, ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (assign, "$fclock", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_shield),        
                (call_script, "script_first_formation_member_sound_horn"),  #tom                     
            (try_end),
            (assign, "$gk_order", 0),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),
    
    (0, 0, 0, [(game_key_clicked, gk_order_6)], [
        (try_begin),
            (eq, "$gk_order", gk_order_2),    #DISMOUNT  #### F2
            (assign, "$fclock", 1),
            (call_script, "script_player_order_formations", mordr_dismount),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - WEDGE #### F4
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", slot_team_d0_size, ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (assign, "$fclock", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_wedge),        
                (call_script, "script_first_formation_member_sound_horn"),  #tom                     
            (try_end),
            (assign, "$gk_order", 0),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),
    
    (0, 0, 0, [(key_clicked, key_f7)], [
        (eq, "$gk_order", gk_order_4), #FORMATION - SQUARE
        (call_script, "script_division_reset_places"),
        (try_for_range, ":division", 0, 9),
            (class_is_listening_order, "$fplayer_team_no", ":division"),
            (store_add, ":slot", slot_team_d0_size, ":division"),
            (team_slot_ge, "$fplayer_team_no", ":slot", 1),
            (assign, "$fclock", 1),
            (call_script, "script_player_attempt_formation", ":division", formation_square),    
            (call_script, "script_first_formation_member_sound_horn"),  #tom                 
        (try_end),
        (assign, "$gk_order", 0),
        (start_presentation, "prsnt_order_display"),
    ]),
    
    (0, 0, 0, [(key_clicked, key_f8)], [
        (eq, "$gk_order", gk_order_4), #FORMATION - CANCEL
        (assign, "$fclock", 1),
        (call_script, "script_player_order_formations", mordr_charge),
        (call_script, "script_first_formation_member_sound_horn"),  #tom     
        (assign, "$gk_order", 0),
        (start_presentation, "prsnt_order_display"),
    ]),
    
    (0, 0, 0, [
        (this_or_next|game_key_clicked, gk_group0_hear),
        (this_or_next|game_key_clicked, gk_group1_hear),
        (this_or_next|game_key_clicked, gk_group2_hear),
        (this_or_next|game_key_clicked, gk_group3_hear),
        (this_or_next|game_key_clicked, gk_group4_hear),
        (this_or_next|game_key_clicked, gk_group5_hear),
        (this_or_next|game_key_clicked, gk_group6_hear),
        (this_or_next|game_key_clicked, gk_group7_hear),
        (this_or_next|game_key_clicked, gk_group8_hear),
        (this_or_next|game_key_clicked, gk_reverse_order_group),    #shows up as "unknown 6" on Native screen
        (this_or_next|game_key_clicked, gk_everyone_around_hear),
        (game_key_clicked, gk_everyone_hear),
    ], [
        (assign, "$gk_order", 0),
        (start_presentation, "prsnt_order_display"),
    ]),

    (0, 0, 0, [
        (key_is_down, key_escape),
        (is_presentation_active, "prsnt_order_display"),
    ], [
        (assign, "$gk_order", 0),
        (presentation_set_duration, 0),
    ]),
    
#implement HOLD OVER THERE when player lets go of key
    (.5, 0, 0, [(eq, "$gk_order_hold_over_there", 1),(neg|game_key_is_down, gk_order_1)], [
        (set_fixed_point_multiplier, 100),
        (assign, "$fclock", 1),
        (call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
        (assign, ":num_bgroups", 0),
        (try_for_range, ":division", 0, 9),
            (class_is_listening_order, "$fplayer_team_no", ":division"),
            (store_add, ":slot", slot_team_d0_size, ":division"),
            (team_slot_ge, "$fplayer_team_no", ":slot", 1),
            (val_add, ":num_bgroups", 1),
        (try_end),    
        
        (gt, ":num_bgroups", 0),
        (agent_get_position, pos49, "$fplayer_agent_no"),
        (call_script, "script_division_reset_places"),

        (try_for_range, ":division", 0, 9),
            (class_is_listening_order, "$fplayer_team_no", ":division"),
            (store_add, ":slot", slot_team_d0_size, ":division"),
            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
            (gt, ":troop_count", 0),
            (store_add, ":slot", slot_team_d0_formation, ":division"),
            (team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
            
            (team_get_order_position, pos2, "$fplayer_team_no", ":division"),
            (call_script, "script_point_y_toward_position", pos2, pos60),
            (try_begin),
                (gt, ":num_bgroups", 1),
                (agent_set_position, "$fplayer_agent_no", pos2),    #fake out script_battlegroup_place_around_leader
                (call_script, "script_player_attempt_formation", ":division", ":fformation"),
            (else_try),
                (neq, ":fformation", formation_none),
                (call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos2),
                (store_add, ":slot", slot_team_d0_formation_space, ":division"),
                (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
                (try_begin),
                    (store_add, ":slot", slot_team_d0_type, ":division"),
                    (team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
                    (neq, ":sd_type", sdt_cavalry),
                    (neq, ":sd_type", sdt_harcher),
                    (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
                    (try_begin),
                        (eq, ":sd_type", sdt_archer),
                        (val_mul, reg0, -1),
                        (assign, ":script", "script_form_archers"),
                    (else_try),
                        (assign, ":script", "script_form_infantry"),
                    (try_end),
                    (position_move_x, pos2, reg0),
                (else_try),
                    (assign, ":script", "script_form_cavalry"),
                (try_end),
                (copy_position, pos1, pos2),
                (call_script, ":script", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),        
            (try_end),
            (store_add, ":slot", slot_team_d0_move_order, ":division"),
            (team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),        
        (try_end), #Battle Group Loop #2
        (agent_set_position, "$fplayer_agent_no", pos49),
        (assign, "$gk_order_hold_over_there", 0),
        
        # (call_script, "script_battle_pos_hold", pos2),
    ]),

    (1, 0, 0, [    #attempt to avoid simultaneous formations function calls
        #(neg|key_is_down, key_for_ranks),
        #(neg|key_is_down, key_for_shield),
        #(neg|key_is_down, key_for_wedge),
        #(neg|key_is_down, key_for_square),
        #(neg|key_is_down, key_for_undo),
        (neg|key_is_down, key_f7), #ADDED
        (neg|key_is_down, key_f8), #ADDED
        (neg|game_key_is_down, gk_order_1),
        (neg|game_key_is_down, gk_order_2),
        (neg|game_key_is_down, gk_order_3),
        (neg|game_key_is_down, gk_order_4),
        (neg|game_key_is_down, gk_order_5),
        (neg|game_key_is_down, gk_order_6)
      ], [
        (set_fixed_point_multiplier, 100),
        (store_mod, ":fifth_second", "$fclock", 5),
        (store_mod, ":tenth_second", "$fclock", 10),
        
        (try_begin),    #set up revertible types for type check
            (eq, ":tenth_second", 0),
            (try_for_range, ":team", 0, 4),
                (try_for_range, ":division", 0, 9),
                    (store_add, ":slot", slot_team_d0_type, ":division"),
                    (this_or_next|team_slot_eq, ":team", ":slot", sdt_skirmisher),
                    (team_slot_eq, ":team", ":slot", sdt_harcher),
                    (team_set_slot, ":team", ":slot", sdt_unknown),
                (try_end),
            (try_end),
        (try_end),
        
        (call_script, "script_store_battlegroup_data"),
        (call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
        (try_begin),
            (eq, reg0, 0),    #no more enemies?
            (try_for_range, ":division", 0, 9),
                (call_script, "script_formation_end", "$fplayer_team_no", ":division"),
            (try_end),
        (else_try),
            (assign, "$autorotate_at_player", 0),
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (store_add, ":slot", slot_team_d0_size, ":division"),
                (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
                (gt, ":troop_count", 0),
                (try_begin),
                    (store_add, ":slot", slot_team_d0_move_order, ":division"),
                    (team_slot_eq, "$fplayer_team_no", ":slot", mordr_follow),
                    (call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":division"),
                    (team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),    #override script_battlegroup_place_around_leader
                    
                (else_try),       #periodically reform
                    (eq, ":fifth_second", 0),
                    (store_add, ":slot", slot_team_d0_formation, ":division"),
                    (team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
                    (neq, ":fformation", formation_none),
                    (team_get_movement_order, reg0, "$fplayer_team_no", ":division"),
                    (neq, reg0, mordr_stand_ground),
                    
                    (call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
                    (store_add, ":slot", slot_team_d0_formation_space, ":division"),
                    (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
                    (store_add, ":slot", slot_team_d0_type, ":division"),
                    (team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
                    (try_begin),
                        (neq, ":sd_type", sdt_cavalry),
                        (neq, ":sd_type", sdt_harcher),
                        (position_move_y, pos1, -2000),
                    (try_end),
                    (call_script, "script_point_y_toward_position", pos1, pos60),
                    (try_begin),
                        (neq, ":sd_type", sdt_cavalry),
                        (neq, ":sd_type", sdt_harcher),
                        (position_move_y, pos1, 2000),
                    (try_end),
                    (call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos1),    
                    (try_begin),    
                        (neq, ":sd_type", sdt_cavalry),
                        (neq, ":sd_type", sdt_harcher),                    
                        (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
                        (try_begin),
                            (eq, ":sd_type", sdt_archer),
                            (val_mul, reg0, -1),
                        (try_end),
                        (position_move_x, pos1, reg0),    
                    (try_end),
                    (try_begin),
                        (eq, ":sd_type", sdt_archer),
                        (call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),        
                    (else_try),
                        (this_or_next|eq, ":sd_type", sdt_cavalry),
                        (eq, ":sd_type", sdt_harcher),    
                        (call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing"),
                    (else_try),                
                        (call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":fformation"),    
                    (try_end),
                (try_end),    #Periodic Reform
            (try_end),    #Division Loop
            (assign, "$autorotate_at_player", formation_autorotate_at_player),
        (try_end),
        (val_add, "$fclock", 1),
    ]),
]

#AI triggers v3 for WB by motomataru
AI_triggers = [  
    (ti_before_mission_start, 0, 0, [], [
        (assign, "$cur_casualties", 0),
        (assign, "$prev_casualties", 0),
        (assign, "$ranged_clock", 1),
        (assign, "$battle_phase", BP_Setup),
        (assign, "$clock_reset", 0),
        (try_for_range, ":team_no", 0, 4),
            (team_set_slot, ":team_no", slot_team_default_formation, formation_default),
            #(team_set_slot, ":team_no", slot_team_reinforcement_stage, 0), #Not needed, team slots begin missions reset
        (try_end),
        (init_position, Team0_Cavalry_Destination),
        (init_position, Team1_Cavalry_Destination),
        (init_position, Team2_Cavalry_Destination),
        (init_position, Team3_Cavalry_Destination),
    ]),

    (0, AI_Delay_For_Spawn, ti_once, [], [
        (try_for_agents, ":cur_agent"),
            (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
        (try_end),
        (set_fixed_point_multiplier, 100),
        (call_script, "script_battlegroup_get_position", Team0_Starting_Point, 0, grc_everyone),
        (call_script, "script_battlegroup_get_position", Team1_Starting_Point, 1, grc_everyone),
        (call_script, "script_battlegroup_get_position", Team2_Starting_Point, 2, grc_everyone),
        (call_script, "script_battlegroup_get_position", Team3_Starting_Point, 3, grc_everyone),
        (call_script, "script_field_tactics", 1)
    ]),

    (1, .5, 0, [], [    #delay to offset half a second from formations trigger
        (try_begin),
            (call_script, "script_cf_count_casualties"),
            (assign, "$cur_casualties", reg0),
            (assign, "$battle_phase", BP_Fight),
        (try_end),
        
        (set_fixed_point_multiplier, 100),
        (call_script, "script_store_battlegroup_data"),
        (try_begin),    #reassess ranged position when fighting starts
            (ge, "$battle_phase", BP_Fight),
            (eq, "$clock_reset", 0),
            (call_script, "script_field_tactics", 1),
            (assign, "$ranged_clock", 0),
            (assign, "$clock_reset", 1),
        (else_try),    #reassess ranged position every five seconds after setup
            (ge, "$battle_phase", BP_Jockey),
            (store_mod, reg0, "$ranged_clock", 5),        
            (eq, reg0, 0),
            (call_script, "script_field_tactics", 1),
            (team_set_slot, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),
            (team_set_slot, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
        (else_try),
            (call_script, "script_field_tactics", 0),
        (try_end),

        (try_begin),
            (eq, "$battle_phase", BP_Setup),
            (assign, ":not_in_setup_position", 0),
            (try_for_range, ":bgteam", 0, 4),
                (neq, ":bgteam", "$fplayer_team_no"),
                (team_slot_ge, ":bgteam", slot_team_size, 1),
                (call_script, "script_battlegroup_get_position", pos1, ":bgteam", grc_archers),
                (team_get_order_position, pos0, ":bgteam", grc_archers),
                (get_distance_between_positions, reg0, pos0, pos1),
                (gt, reg0, 500),
                (assign, ":not_in_setup_position", 1),
                #tom
                (try_begin),
                  (store_random_in_range, ":random", 0, 100),
                  (lt, ":random", 15),
                  (play_sound_at_position, "snd_horn", pos1),
                (try_end),
                #tom end
            (try_end),
            (eq, ":not_in_setup_position", 0),    #all AI reached setup position?
            (assign, "$battle_phase", BP_Jockey),
        (try_end),
        
        (val_add, "$ranged_clock", 1),
    ]),
]

# end AI triggers
################################################################
## death cam
################################################################

sw_deathcam_follow_troop = (0, 0, 0,
  [
    (eq, "$enable_deahtcam", 1),
    (gt, "$dmod_current_agent", 0),
    (eq, "$setting_use_dmod", 1),
    (eq, "$dmod_move_camera", 1),
    (agent_get_position, pos1, "$dmod_current_agent"),
    (position_move_z, pos1, 300),
    (position_move_y, pos1, -300),
    (agent_get_horse, ":horse_agent", "$dmod_current_agent"),
    (try_begin),
      (ge, ":horse_agent", 0),
      #(position_move_z, pos1, 0),
    (try_end),
    # (try_begin),
      # (eq, "$pop_camera_on", 1),
      # (assign, "$pop_camera_on", 0),
    # (try_end),

    (mission_cam_set_position, pos1),
    (mission_cam_set_mode, 1),
    (set_fixed_point_multiplier, 100),
  ],[])

sw_deathcam_cycle_fowards =    (0, 0, 0,[
        (eq, "$enable_deahtcam", 1),
        (eq, "$setting_use_dmod", 1),
        (key_clicked, key_mouse_scroll_up), (main_hero_fallen),
        (call_script, "script_dmod_cycle_forwards"),
        ], [])

sw_deathcam_cycle_backwards = (0, 0, 0,[
        (eq, "$enable_deahtcam", 1),
        (eq, "$setting_use_dmod", 1),
        (key_clicked, key_mouse_scroll_down), (main_hero_fallen),
        (call_script, "script_dmod_cycle_backwards"),
        ], [])
# end deathcam ####################################


#tom
########################### Horse archer trigger
force_ranged = [
   (2, 0, 0, [(eq, "$g_battle_won", 0)],
   [
      (set_fixed_point_multiplier, 100),
      (try_for_agents, ":agent"),
        (agent_get_troop_id, ":troop", ":agent"),
        (try_begin), ##special for horse charioteers
          (agent_is_alive, ":agent"),
          (agent_is_human, ":agent"),
          (agent_is_non_player, ":agent"),
          (agent_is_active, ":agent"),
          (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Isn't routing.
          (agent_slot_eq, ":agent", slot_possessed, 0), #not a player spawn
          (agent_get_division, ":division", ":agent"),          
          (agent_get_horse, ":horse", ":agent"),
          (gt, ":horse", 0), #mounted
          (troop_is_guarantee_ranged, ":troop"),
          (agent_get_ammo, ":ammo_left", ":agent"),
          (gt, ":ammo_left", 0),

          (agent_get_team, ":team", ":agent"),
          (team_get_hold_fire_order, ":order", ":team", ":division"),
          (neq, ":order", 1), #mordr_hold_fire
          ##equip script
          (try_begin), ##mounted troops use bows n shit
            (try_for_range, reg0, 0, 4),
              (agent_get_item_slot, ":item", ":agent", reg0),
              (is_between, ":item", 1, "itm_items_end"),
              #(gt, ":item", 0),
              (item_get_type, ":type", ":item"),
              (this_or_next|eq, ":type", itp_type_thrown),
              (eq, ":type", itp_type_bow),
              (agent_set_wielded_item, ":agent", ":item"),
              (assign, reg0, -1), ##break
            (try_end),
          (try_end),
          
          (agent_get_wielded_item, ":item", ":agent", 0),
          (is_between, ":item", 1, "itm_items_end"),
         # (gt, ":item", 0),
          (item_get_type, ":type", ":item"),
          (this_or_next|eq, ":type", itp_type_thrown),
          (eq, ":type", itp_type_bow),
          
          (call_script, "script_get_first_closest_enemy_distance", ":agent", ":team", 200), # Find distance of nearest 3 enemies
          (assign, ":nearest_enemy", reg1),
          (assign, ":closest_agent", reg4),          
          (gt, ":closest_agent", -1),
          
          (try_begin),
            (assign, ":radious", 8500), 
            (assign, ":nearest_enemy_range", 9000), 
            (assign, ":skrimish_angle", 12), 
            #(agent_get_wielded_item, ":item", ":agent", 0),
            (try_begin), #if thrown, reduce by 3
              (eq, ":type", itp_type_thrown),
              (assign, ":nearest_enemy_range", 3000), 
              (assign, ":radious", 3500), 
              (val_mul, ":skrimish_angle", 3), 
            (try_end),
            (team_get_movement_order, reg0, ":team", ":division"),
            (eq, reg0, mordr_charge),
            (call_script, "script_tom_agent_skirmish", ":agent", ":closest_agent", ":nearest_enemy", ":radious", ":nearest_enemy_range", ":skrimish_angle"),        
            (try_begin), ##shooot more often
              (lt, ":nearest_enemy", 9500),
              (store_random_in_range, ":random", 0, 10),
              (le, ":random", 2),
              (agent_get_attack_action, ":action", ":agent"),
              (eq, ":action", 0), #free
              (agent_get_combat_state, ":agent_cs", ":agent"),
              (neq, ":agent_cs", 7), #NEG does not see target
              (this_or_next|eq, ":type", itp_type_thrown),
              (eq, ":type", itp_type_bow),
              #(eq, ":type", itp_type_crossbow),
              (agent_set_attack_action, ":agent", 0, 0),
            (try_end),
            #(assign, ":ok", 0),            
          (try_end),
        (else_try), #clear horse archer skirmisher ai
          (agent_slot_eq, ":agent", slot_agent_scripted_mode, 1),
          (agent_set_slot, ":agent", slot_agent_scripted_mode, 0),
          (agent_clear_scripted_mode, ":agent"),
          #(agent_force_rethink, ":agent"),
        (try_end),        
      (try_end),
   ]),
]

forced_range_archers = [(2, 0, 0, [],
    [
        (get_player_agent_no, ":p_agent"),
        (try_for_agents, ":agent"),
          (agent_is_human, ":agent"),
          (neq, ":p_agent", ":agent"),
          (agent_slot_eq, ":agent", slot_possessed, 0), #not a player spawn
          (agent_is_alive, ":agent"),
                
          (agent_get_ammo, ":ammo_left", ":agent"),
          (gt, ":ammo_left", 0),
          
          #(call_script, "script_get_closest_enemy_distance", ":agent"), # Find distance of nearest 3 enemies
          #(assign, ":nearest_enemy", reg1),
          #(assign, ":closest_agent", reg4),
          
          #(gt, ":closest_agent", -1),
          #(gt, ":nearest_enemy", 100), #1meters.
          
          (agent_get_team, ":team", ":agent"),    
          (this_or_next|neq, ":team", "$attacker_team"),
          (neq, ":team", "$attacker_team_2"),      
              
          (call_script, "script_get_closest_enemy_distance_new", ":agent", ":team", 150),
          (assign, ":nearest_enemy", reg1),
          (gt, ":nearest_enemy", 150), #1meters.
        
          (agent_get_troop_id, ":troop", ":agent"),
          (troop_is_guarantee_ranged, ":troop"),
          
          #(agent_get_team, ":team", ":agent"),
          (agent_get_division, ":division", ":agent"),    
          
          (team_get_hold_fire_order, ":order", ":team", ":division"),
          (neq, ":order", 1), #mordr_hold_fire
          
          (agent_get_wielded_item, ":item", ":agent", 0),
          (is_between, ":item", 1, "itm_items_end"),
          #(gt, ":item", 0),
            
          (item_get_type, ":type", ":item"),            
          (this_or_next|neq, ":type", itp_type_thrown),
          (this_or_next|neq, ":type", itp_type_crossbow),
          (neq, ":type", itp_type_bow),
            
          (assign, ":top", 4),
          (try_for_range, reg0, 0, ":top"),
            (agent_get_item_slot, ":item_no", ":agent", reg0),
            (is_between, ":item_no", 1, "itm_items_end"),
            #(gt, ":item_no", 0),
            
            (item_get_type, ":type", ":item_no"),
            (this_or_next|eq, ":type", itp_type_thrown),
            (this_or_next|eq, ":type", itp_type_bow),
            (eq, ":type", itp_type_crossbow),
            
            (agent_set_wielded_item, ":agent", ":item_no"),
            (assign, ":top", -1),
          (try_end),
        (try_end),
    ]),
]

lance_usage = [
# LANCE USAGE BEGIN
   # Force mounted NPCs to switch to their lance.  This is called once at the
   # start of the battle. If you want lancers to ALWAYS use lances on horseback,
   # replace ti_once with 1. Otherwise they may switch to sword if bogged down
   (ti_on_agent_spawn, 0, 0, [],
   [
      # Run through all active NPCs on the battle field.
      #(display_message, "@DEBUG -- lance usage"),
#(eq, 0,1),
      (store_trigger_param_1, ":agent"), ################# NEW v3.8
      (get_player_agent_no, ":p_agent"),
      # (try_for_agents, ":agent"),
        # Isn't a horse.
        (agent_is_human, ":agent"),
        # Isn't a player.
        #(agent_is_non_player, ":agent"),
        (neq, ":p_agent", ":agent"),
        (agent_slot_eq, ":agent", slot_possessed, 0), #not a player spawn
        # Hasn't been defeated.
        (agent_is_alive, ":agent"),
        # They riding a horse?
        (agent_get_horse, ":horse", ":agent"),
        # Is riding a horse.
        #(gt, ":horse", 0), #TOM SPEAR
        (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Isn't routing.
        (agent_get_troop_id, ":troop_id", ":agent"),
        (agent_get_ammo, ":ammo_left", ":agent"),
        (le, ":ammo_left", 0),
        #(store_troop_faction, ":troop_faction", ":troop_id"),
        (try_begin),
          (gt, ":horse", 0), #Mounted
          (neg | troop_is_guarantee_ranged, ":troop_id"),
          # Get wielded item.
          (agent_get_wielded_item, ":wielded", ":agent", 0),
          # Is it a lance?
          (neg|is_between, ":wielded", "itm_light_lance", "itm_bamboo_spear"), # adjust as needed
          # Force the NPC to wield the lance, but this will only happen if they
          # actually have a lance in their inventory.  Otherwise this does
          # nothing.
          (try_for_range, ":item", "itm_light_lance", "itm_bamboo_spear"), # adjust as needed
            (agent_set_wielded_item, ":agent", ":item"),
          (try_end),    
        (else_try), #WIELD FLAG
          (eq, "$tom_use_banners", 1),
          (try_for_range, ":item",itm_flag_pole_1,itm_cross +1), # adjust as needed
            (agent_set_wielded_item, ":agent", ":item"),
          (try_end),
          (agent_get_wielded_item, ":item", ":agent", 0),
          (is_between, ":item", itm_flag_pole_1, itm_cross + 1),
        (else_try),#no lance on foot
          (neg | troop_is_guarantee_ranged, ":troop_id"),
          (le, ":horse", 0),
          (agent_get_wielded_item, ":wielded", ":agent", 0),
          (is_between, ":wielded", "itm_light_lance", "itm_bamboo_spear"),
          (try_for_range, reg0, 0, 4),
            (agent_get_item_slot, ":item", ":agent", reg0),
            (is_between, ":item", 1, "itm_items_end"),
            #(gt, ":item", 0),
            (neg|is_between, ":item", "itm_light_lance", "itm_bamboo_spear"),
            (item_get_type, ":item_type", ":item"),
            (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
            (this_or_next|eq, ":item_type", itp_type_polearm),
            (eq, ":item_type", itp_type_one_handed_wpn),
            (agent_set_wielded_item, ":agent", ":item"),
          (try_end),    
        (else_try), #TOM - SPEAR USSAGE
          (neg | troop_is_guarantee_ranged, ":troop_id"),
          #(agent_get_horse, ":horse", ":agent"),
          (le, ":horse", 0), #unmounted
          (agent_get_wielded_item, ":wielded", ":agent", 0),
          (neg|is_between, ":wielded", "itm_bamboo_spear", "itm_wooden_shield"),
          #(neg|is_between, ":wielded", "itm_flag_pole_1", "itm_items_end"), #not a flag
          (try_for_range, ":item", "itm_bamboo_spear", "itm_wooden_shield"), # adjust as needed
            #(gt, ":item", 0),
            #(agent_equip_item, ":agent", ":item"),
            (agent_set_wielded_item, ":agent", ":item"),
          (try_end),
        (else_try), #tom - range usage
          (troop_is_guarantee_ranged, ":troop_id"),
          
          (agent_get_team, ":team", ":agent"),
          (agent_get_division, ":division", ":agent"),    
          
          (team_get_hold_fire_order, ":order", ":team", ":division"),
          (neq, ":order", 1), #mordr_hold_fire

          #(gt, ":wielded", 0),
          (is_between, ":wielded", 1, "itm_items_end"),
          (item_get_type, ":type", ":wielded"),            
          (this_or_next|le, ":wielded", -1),
          (this_or_next|neq, ":type", itp_type_thrown),
          (this_or_next|neq, ":type", itp_type_crossbow),
          (neq, ":type", itp_type_bow),
          
          (call_script, "script_get_closest_enemy_distance_new", ":agent", ":team", 300),
          (assign, ":nearest_enemy", reg1),
          (gt, ":nearest_enemy", 300), #7meters.
          
          (assign, ":top", 4),
          (try_for_range, reg0, 0, ":top"),
            (agent_get_item_slot, ":item_no", ":agent", reg0),
            (is_between, ":item_no", 1, "itm_items_end"),
            #(gt, ":item_no", 0),
            
            (item_get_type, ":type", ":item_no"),
            (this_or_next|eq, ":type", itp_type_thrown),
            (this_or_next|eq, ":type", itp_type_bow),
            (eq, ":type", itp_type_crossbow),
            
            (agent_set_wielded_item, ":agent", ":item_no"),
            (assign, ":top", -1),
          (try_end),
        (try_end),
   ]),
]
# LANCE USAGE END

common_weapon_break =  (ti_on_agent_hit, 0.3, 0, [],
  [
    # Trigger Param 1: damage inflicted agent_id
    # Trigger Param 2: damage dealer agent_id
    # Trigger Param 3: inflicted damage
    # Register 0: damage dealer item_id
    # Position Register 0: position of the blow
    #                      rotation gives the direction of the blow

    (store_trigger_param_1, ":hit_agent"),
    (store_trigger_param_2, ":attacker_agent"),
    (store_trigger_param_3, ":damage"),

    (assign, ":item_id", reg0),

    (agent_is_human, ":hit_agent"),
############################################
    (get_player_agent_no, ":player_agent"),
    # durability
    (try_begin), #body armor
      (eq, "$tom_weapon_break", 1), #TOM
      (eq, ":hit_agent", ":player_agent"),
      (store_random_in_range, ":random", 0, 1000), #tom was 100
      (eq, ":random", 1),
      (store_random_in_range, ":slot", ek_head, ek_horse),
      (troop_get_inventory_slot, ":body_item", "trp_player", ":slot"),
      (gt, ":body_item", 0),
      (str_store_item_name, s20, ":body_item"),
      (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot"),
      (try_begin),
        (eq, ":modifier", imod_poor),
        #(display_message, "@Your {s20} falls apart!", 0xff0000),
       # (agent_unequip_item, ":player_agent", ":body_item"),
       # (troop_remove_item, "trp_player", ":body_item"),
       # (troop_remove_item, "trp_broken_items", ":body_item"),
       (display_message, "@Your {s20} is too crapy to fall apart!", 0xff0000),
      (else_try),
        (troop_add_item, "trp_broken_items", ":body_item", ":modifier"),
        (troop_set_inventory_slot_modifier, "trp_player", ":slot", imod_poor),
        (display_message, "@Your {s20} cracks!", 0xff0000),
      (try_end),
    (try_end),
    # durability
############################################
    (try_begin), #weapons
      (eq, "$tom_weapon_break", 1), #TOM
      (eq, ":attacker_agent", ":player_agent"),
      ##(gt, ":item_id", 0),
      (is_between, ":item_id", 1, "itm_items_end"),
      (neg|is_between, ":item_id", "itm_light_lance", "itm_wooden_shield"),
      (item_get_type, ":item_type", ":item_id"),
      (ge, ":damage", 10),
      (neq, ":item_type", itp_type_thrown),
      (neq, ":item_type", itp_type_bow),
      (neq, ":item_type", itp_type_crossbow),
      (neq, ":item_type", itp_type_arrows),
      (neq, ":item_type", itp_type_bolts),
      (store_random_in_range, ":random", 0, 600), #tom was 100
      (eq, ":random", 1),

      (assign, ":slot_to_use", -1),
      (try_for_range, ":slot", ek_item_0, ek_head),
        (troop_get_inventory_slot, ":weapon", "trp_player", ":slot"),
        (eq, ":weapon", ":item_id"),
        (assign, ":slot_to_use", ":slot"),
      (try_end),
      (gt, ":slot_to_use", 0),
      (str_store_item_name, s20, ":item_id"),
      (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":slot_to_use"),
      (try_begin),
        (eq, ":modifier", imod_poor),
        (display_message, "@Your {s20} falls apart!", 0xff0000),
        (agent_unequip_item, ":player_agent", ":item_id"),
        (troop_remove_item, "trp_player", ":item_id"),
        (troop_remove_item, "trp_broken_items", ":item_id"),
      (else_try),
        (troop_add_item, "trp_broken_items", ":item_id", ":modifier"),
        (troop_set_inventory_slot_modifier, "trp_player", ":slot_to_use", imod_poor),
        (display_message, "@Your {s20} cracks!", 0xff0000),
      (try_end),
    (try_end),
############################################
    #(assign, ":has_choice", -1),
    (agent_get_horse, ":mounted", ":attacker_agent"),
    ##(agent_get_troop_id,  ":attacker_troop", ":attacker_agent"),
    (try_begin), #lance
      (eq, "$tom_lance_breaking", 1),
      (gt, ":mounted", 0),
      # (is_between, ":item_id", "itm_light_lance", "itm_spear_a"), # lance
	  ########## NEW v3.8
      (this_or_next|is_between, ":item_id", "itm_light_lance", "itm_bamboo_spear"), 
      (is_between, ":item_id", "itm_crusader_knight_spear_a", "itm_crusader_spear_a"), 
	  ####################
      (ge, ":damage", 50),
      (store_random_in_range, ":chance",0, 100),
      (gt, ":chance", 20),
      (try_begin),
        (eq, ":attacker_agent", ":player_agent"),
        (display_message, "@You broke your lance!", 0xff0000),
      (try_end),
      (agent_play_sound, ":hit_agent", "snd_shield_broken"),
      (agent_unequip_item, ":attacker_agent", ":item_id"),
     # (assign, ":has_choice",0),
    (try_end),
############################################
####################### NEW v1.9 - fixes spears breaking even if weapon break option was turned off
    (try_begin),  #spear
      (eq, "$tom_weapon_break", 1),
      # (is_between, ":item_id", "itm_bamboo_spear", "itm_staff"), # spear!
	  ########## NEW v3.8
      (this_or_next|is_between, ":item_id", "itm_bamboo_spear", "itm_staff"), 
      (is_between, ":item_id", "itm_crusader_spear_a", "itm_mace_6"), 
	  ####################
      (le, ":mounted", 0), #not mounted
      (ge, ":damage", 8),
      (store_random_in_range, ":chance",0, 100),
      (ge, ":chance", 90), #rather small but common enough
      (try_begin),
        (eq, ":attacker_agent", ":player_agent"),
        (display_message, "@You broke your spear!", 0xff0000),
      (try_end),
      #(display_message, "@brokeen spear!", 0xff0000),
      (agent_play_sound, ":hit_agent", "snd_shield_broken"),
      (agent_unequip_item, ":attacker_agent", ":item_id"),
     # (assign, ":has_choice",0),    
    (try_end), 
#####################################################################
    ##(neq, ":attacker_agent", ":player_agent"),
    ##(troop_get_inventory_capacity, ":cap", ":attacker_troop"),
    ##(eq, ":has_choice",0),
    ##(gt, ":cap", 1),
    ##(try_for_range, ":i", 0, ":cap"),
    ##   (troop_get_inventory_slot, ":item", ":attacker_troop", ":i"),
    ##   (is_between, ":item", 1, "itm_items_end"),
    ##   #(gt, ":item", 0),
    ##   (item_get_type, ":item_type", ":item"),
    ##   (neg|is_between, ":item", "itm_light_lance", "itm_spear_a"), # adjust as needed
    ##   (neq, ":item_type", itp_type_polearm),
    ##   (neq, ":item_type", itp_type_shield),
    ##   (neq, ":item_type", itp_type_thrown),
    ##   (neq, ":item_type", itp_type_bow),
    ##   (agent_has_item_equipped, ":attacker_agent", ":item"),
    ##   (assign, ":has_choice",1),
    ##   (assign, ":cap",0),
    ##(try_end),
    # Equip their backup weapon.
    ##(try_begin),
    ##   (eq, ":has_choice",1),
    ##   (agent_set_wielded_item, ":attacker_agent", ":item"),
    ##(try_end),
])

# hold
hold_trigger = [
  (0, 0, ti_once, [], [
    (get_player_agent_no, ":player"),
    (agent_get_team, ":team_no", ":player"),
    (set_show_messages, 0),
    (team_give_order, ":team_no", grc_everyone, mordr_hold),
    # (team_give_order, ":team_no", grc_infantry, mordr_stand_closer),
    # (team_give_order, ":team_no", grc_infantry, mordr_stand_closer),

    # (agent_get_position, pos1, ":player"),

    # (position_move_x, pos1, -2500),      #cavalry set up 5m LEFT of leader
    # (team_set_order_position, ":team_no", grc_cavalry, pos1),

    # (position_move_x, pos1, 2500),      #infantry set up 5m RIGHT of leader
    # (team_set_order_position, ":team_no", grc_infantry, pos1),

    # (position_move_y, pos1, 1000),      #archers set up 10m FRONT of leader
    # (team_set_order_position, ":team_no", grc_archers, pos1),

    # (team_give_order, ":team_no", grc_everyone, mordr_advance),
    # (team_give_order, ":team_no", grc_everyone, mordr_advance),
    (set_show_messages, 1),
  ])
]

charge_trigger = [
  (0, 0, ti_once, [
  (eq, 0, 1), ##AI should take over
  (eq, "$enable_deahtcam", 1),#tom
  (main_hero_fallen),  
  ], [
        (assign, "$fclock", 1),
        (call_script, "script_player_order_formations", mordr_charge),

    (get_player_agent_no, ":player"),
    (agent_get_team, ":team_no", ":player"),
    (team_give_order, ":team_no", grc_everyone, mordr_charge),
  ])
  
]

troop_equip = [
    (ti_on_agent_spawn, 0, 0, [], [
    (store_trigger_param_1, ":agent_no"),

    (agent_is_human, ":agent_no"),
    (agent_is_non_player, ":agent_no"),
    
    (agent_get_troop_id, ":troop_id", ":agent_no"),
    (lt, ":troop_id", "trp_kidnapped_girl"),
    
    (try_for_range, reg0, 0, 4),
      (agent_get_item_slot, ":item_no", ":agent_no", reg0),
      (is_between, ":item_no", 1, "itm_items_end"),
      #(gt, ":item_no", 0),
      (agent_unequip_item, ":agent_no", ":item_no"),
    (try_end),
    (try_for_range, reg0, 0, 2),
      (agent_get_wielded_item, ":item_no", ":agent_no", reg0),
      (is_between, ":item_no", 1, "itm_items_end"),
      #(gt, ":item_no", 0),
      (agent_unequip_item, ":agent_no", ":item_no"),
    (try_end),
    
    (assign, ":main_weapon", 0),
    (assign, ":side_weapon", 25),
    (assign, ":shield", 50),
    (assign, ":two_handed", 75),
    (assign, ":javelin", 100),
    (assign, ":bolts", 125),
    (assign, ":arrows", 150),
    (assign, ":bow", 175),
    (assign, ":crossbow", 200),
    
    (assign, ":equip_main", 0),
    (assign, ":equip_side", 0),
    (assign, ":equip_shield", 0),
    (assign, ":equip_two_handed", 0),
    (assign, ":equip_javelin", 0),
    (assign, ":equip_bolts", 0),
    (assign, ":equip_arrows", 0),
    (assign, ":equip_bow", 0),
    (assign, ":equip_crossbow", 0),
    
    (troop_get_inventory_capacity, ":capacity", ":troop_id"),
    (try_for_range, ":cur_slot", 0, ":capacity"),
      (troop_get_inventory_slot, ":cur_item", ":troop_id", ":cur_slot"),
      (is_between, ":cur_item", 1, "itm_items_end"),
      ##(gt, ":cur_item", 0),
      (item_get_type, ":type", ":cur_item"),
      (try_begin),
        (eq, ":type", itp_type_polearm),
        (val_add, ":main_weapon", 1),
        (troop_set_slot, "trp_items_array", 0, ":main_weapon"),
        (troop_set_slot, "trp_items_array", ":main_weapon", ":cur_item"),
        (assign, ":equip_main", 1),
      (else_try),    
        (eq, ":type", itp_type_one_handed_wpn),
        (val_add, ":side_weapon", 1),
        (troop_set_slot, "trp_items_array", 25, ":side_weapon"),
        (troop_set_slot, "trp_items_array", ":side_weapon", ":cur_item"),    
        (assign, ":equip_side", 1),
      (else_try),    
        (eq, ":type", itp_type_shield),
        (val_add, ":shield", 1),
        (troop_set_slot, "trp_items_array", 50, ":shield"),
        (troop_set_slot, "trp_items_array", ":shield", ":cur_item"),
        (assign, ":equip_shield", 1),    
      (else_try),    
        (eq, ":type", itp_type_two_handed_wpn),
        (val_add, ":two_handed", 1),
        (troop_set_slot, "trp_items_array", 75, ":two_handed"),
        (troop_set_slot, "trp_items_array", ":two_handed", ":cur_item"),
        (assign, ":equip_two_handed", 1),
      (else_try),    
        (eq, ":type", itp_type_thrown),
        (val_add, ":javelin", 1),
        (troop_set_slot, "trp_items_array", 100, ":javelin"),
        (troop_set_slot, "trp_items_array", ":javelin", ":cur_item"),
        (assign, ":equip_javelin", 1),
      (else_try),    
        (eq, ":type", itp_type_bolts),
        (val_add, ":bolts", 1),
        (troop_set_slot, "trp_items_array", 125, ":bolts"),
        (troop_set_slot, "trp_items_array", ":bolts", ":cur_item"),
        (assign, ":equip_bolts", 1),
      (else_try),    
        (eq, ":type", itp_type_arrows),
        (val_add, ":arrows", 1),
        (troop_set_slot, "trp_items_array", 150, ":arrows"),
        (troop_set_slot, "trp_items_array", ":arrows", ":cur_item"),
        (assign, ":equip_arrows", 1),
      (else_try),    
        (eq, ":type", itp_type_bow),
        (val_add, ":bow", 1),
        (troop_set_slot, "trp_items_array", 175, ":bow"),
        (troop_set_slot, "trp_items_array", ":bow", ":cur_item"),
        (assign, ":equip_bow", 1),
      (else_try),    
        (eq, ":type", itp_type_crossbow),
        (val_add, ":crossbow", 1),
        (troop_set_slot, "trp_items_array", 200, ":crossbow"),
        (troop_set_slot, "trp_items_array", ":crossbow", ":cur_item"),
        (assign, ":equip_crossbow", 1),
      (try_end),
    (try_end),  
    
    
    (try_begin),
      (eq, ":equip_main", 1),
      (troop_get_slot, ":amount", "trp_items_array", 0),
      (store_random_in_range, ":slot", 1, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_side", 1),
      (troop_get_slot, ":amount", "trp_items_array", 25),
      (store_random_in_range, ":slot", 26, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_shield", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 50),
      (store_random_in_range, ":slot", 51, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_two_handed", 1),    
      (try_begin),
        (eq, ":equip_side", 1),    #if have and side arm
        (store_random_in_range, ":random", 0, 100),
        (lt, ":random", 65), #small chance for getting a sidearm as well
      (else_try),
        (troop_get_slot, ":amount", "trp_items_array", 75),
        (store_random_in_range, ":slot", 76, ":amount"),
        (troop_get_slot, ":itm", "trp_items_array", ":slot"),
        (agent_equip_item, ":agent_no", ":itm"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":equip_javelin", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 100),
      (store_random_in_range, ":slot", 101, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_bolts", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 125),
      (store_random_in_range, ":slot", 126, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_arrows", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 150),
      (store_random_in_range, ":slot", 151, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_bow", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 175),
      (store_random_in_range, ":slot", 176, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    (try_begin),
      (eq, ":equip_crossbow", 1),    
      (troop_get_slot, ":amount", "trp_items_array", 200),
      (store_random_in_range, ":slot", 201, ":amount"),
      (troop_get_slot, ":itm", "trp_items_array", ":slot"),
      (agent_equip_item, ":agent_no", ":itm"),
    (try_end),
    
    
    # (store_random_in_range, ":random_spear", "itm_spear_a", "itm_wooden_shield"),
    # (try_begin),
      # (agent_get_wielded_item, ":item", ":agent_no", 0),
      # (gt, ":item", 0),
      # (agent_unequip_item, ":agent_no", ":item"),
    # (try_end),
    # (agent_equip_item, ":agent_no", ":random_spear"),
    # (agent_set_wielded_item, ":agent_no", ":random_spear"),
    
    
    
    # (agent_get_division, ":division", ":agent_no"),
    
    # (try_begin),
      # (eq, ":division", grc_spearmen),
      # (agent_set_division, ":agent_no", grc_infantry),
      # (agent_set_division, ":agent_no", grc_archers),
    # (try_end),
    ])
	
]

multiplayer_server_check_belfry_movement = (
  0, 0, 0, [],
  [
    (multiplayer_is_server),
    (set_fixed_point_multiplier, 100),

    (try_for_range, ":belfry_kind", 0, 2),
      (try_begin),
        (eq, ":belfry_kind", 0),
        (assign, ":belfry_body_scene_prop", "spr_belfry_a"),
      (else_try),
        (assign, ":belfry_body_scene_prop", "spr_belfry_b"),
      (try_end),

      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos1, ":belfry_scene_prop_id"), #pos1 holds position of current belfry
        (prop_instance_get_starting_position, pos11, ":belfry_scene_prop_id"),

        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (try_begin),
          (eq, ":belfry_kind", 1),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),

        (val_mul, ":belfry_first_entry_point_id", 10),
        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 10),

        (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id"),
          (entry_point_is_auto_generated, ":entry_point_id"),
          (assign, ":belfry_last_entry_point_id", ":entry_point_id"),
        (try_end),

        (assign, ":belfry_last_entry_point_id_plus_one", ":belfry_last_entry_point_id"),
        (val_sub, ":belfry_last_entry_point_id", 1),
        (assign, reg0, ":belfry_last_entry_point_id"),
        (neg|entry_point_is_auto_generated, ":belfry_last_entry_point_id"),

        (try_begin),
          (get_sq_distance_between_positions, ":dist_between_belfry_and_its_destination", pos1, pos11),
          (ge, ":dist_between_belfry_and_its_destination", 4), #0.2 * 0.2 * 100 = 4 (if distance between belfry and its destination already less than 20cm no need to move it anymore)

          (assign, ":max_dist_between_entry_point_and_belfry_destination", -1), #should be lower than 0 to allow belfry to go last entry point
          (assign, ":belfry_next_entry_point_id", -1),
          (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id_plus_one"),
            (entry_point_get_position, pos4, ":entry_point_id"),
            (get_sq_distance_between_positions, ":dist_between_entry_point_and_belfry_destination", pos11, pos4),
            (lt, ":dist_between_entry_point_and_belfry_destination", ":dist_between_belfry_and_its_destination"),
            (gt, ":dist_between_entry_point_and_belfry_destination", ":max_dist_between_entry_point_and_belfry_destination"),
            (assign, ":max_dist_between_entry_point_and_belfry_destination", ":dist_between_entry_point_and_belfry_destination"),
            (assign, ":belfry_next_entry_point_id", ":entry_point_id"),
          (try_end),

          (try_begin),
            (ge, ":belfry_next_entry_point_id", 0),
            (entry_point_get_position, pos5, ":belfry_next_entry_point_id"), #pos5 holds belfry next entry point target during its path
          (else_try),
            (copy_position, pos5, pos11),
          (try_end),

          (get_distance_between_positions, ":belfry_next_entry_point_distance", pos1, pos5),

          #collecting scene prop ids of belfry parts
          (try_begin),
            (eq, ":belfry_kind", 0),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
            #belfry platform_b
            (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
          (else_try),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),

          #belfry wheel_1
          (store_mul, ":wheel_no", ":belfry_no", 3),
          (try_begin),
            (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
            (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
            (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
            (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
          (try_end),
          (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_2
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_3
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),

          (init_position, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos18, pos1, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos19, pos1, pos17),

          (assign, ":number_of_agents_around_belfry", 0),
          (get_max_players, ":num_players"),
          (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":agent_id", ":player_no"),
            (ge, ":agent_id", 0),
            (agent_get_team, ":agent_team", ":agent_id"),
            (eq, ":agent_team", 1), #only team2 players allowed to move belfry (team which spawns outside the castle (team1 = 0, team2 = 1)),
            (agent_get_horse, ":agent_horse_id", ":agent_id"),
            (eq, ":agent_horse_id", -1),
            (agent_get_position, pos2, ":agent_id"),
            (get_sq_distance_between_positions_in_meters, ":dist_between_agent_and_belfry", pos18, pos2),

            (lt, ":dist_between_agent_and_belfry", multi_distance_sq_to_use_belfry), #must be at most 10m * 10m = 100m away from the player
            (neg|scene_prop_has_agent_on_it, ":belfry_scene_prop_id", ":agent_id"),
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_a_scene_prop_id", ":agent_id"),

            (this_or_next|eq, ":belfry_kind", 1), #there is this_or_next here because belfry_b has no platform_b
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_b_scene_prop_id", ":agent_id"),

            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_1_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_2_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_3_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|position_is_behind_position, pos2, pos19),
            (position_is_behind_position, pos2, pos1),
            (val_add, ":number_of_agents_around_belfry", 1),
          (try_end),

          (val_min, ":number_of_agents_around_belfry", 16),

          (try_begin),
            (scene_prop_get_slot, ":pre_number_of_agents_around_belfry", ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing),
            (scene_prop_get_slot, ":next_entry_point_id", ":belfry_scene_prop_id", scene_prop_next_entry_point_id),
            (this_or_next|neq, ":pre_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),
            (neq, ":next_entry_point_id", ":belfry_next_entry_point_id"),

            (try_begin),
              (eq, ":next_entry_point_id", ":belfry_next_entry_point_id"), #if we are still targetting same entry point subtract
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              (store_mul, ":sqrt_number_of_agents_around_belfry", "$g_last_number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (assign, ":distance", ":belfry_next_entry_point_distance"),
              (val_mul, ":distance", ":sqrt_number_of_agents_around_belfry"),
              (val_div, ":distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":distance", 4), #multiplying with 4 to make belfry pushing process slower,
                                                                 #with 16 agents belfry will go with 4 / 4 = 1 speed (max), with 1 agent belfry will go with 1 / 4 = 0.25 speed (min),
            (try_end),

            (try_begin),
              (ge, ":belfry_next_entry_point_id", 0),

              #up down rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9),
              (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry

              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, 300), #go 3.0 meters right
              (position_transform_position_to_parent, pos10, pos5, pos9),
              (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
              (init_position, pos20),
              (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos23, pos5, pos20),

              #right left rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees.
              (val_mul, ":rotate_angle_of_next_entry_point", -1),

              (init_position, pos20),
              (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos22, pos23, pos20),
            (else_try),
              (copy_position, pos22, pos5),
            (try_end),

            (try_begin),
              (ge, ":number_of_agents_around_belfry", 1), #if there is any agents pushing belfry

              (store_mul, ":sqrt_number_of_agents_around_belfry", ":number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (val_mul, ":belfry_next_entry_point_distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":belfry_next_entry_point_distance", 3), #multiplying with 3 to make belfry pushing process slower,
                                                                 #with 9 agents belfry will go with 3 / 3 = 1 speed (max), with 1 agent belfry will go with 1 / 3 = 0.33 speed (min),
              (val_div, ":belfry_next_entry_point_distance", ":sqrt_number_of_agents_around_belfry"),
              #calculating destination coordinates of belfry parts
              #belfry platform_a
              (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos1, pos6),
              (position_transform_position_to_parent, pos8, pos22, pos7),
              (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
                (position_transform_position_to_local, pos7, pos1, pos6),
                (position_transform_position_to_parent, pos8, pos22, pos7),
                (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              (try_end),
              #wheel rotation
              (store_mul, ":belfry_wheel_rotation", ":belfry_next_entry_point_distance", -25),
              #(val_add, "$g_belfry_wheel_rotation", ":belfry_wheel_rotation"),
              (assign, "$g_last_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),

              #belfry wheel_1
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_1_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry wheel_2
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_2_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry wheel_3
              (prop_instance_get_position, pos13, ":belfry_wheel_3_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_3_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry main body
              (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos22, ":belfry_next_entry_point_distance"),
            (else_try),
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              #belfry platform_a
              (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
              (try_end),
              #belfry wheel_1
              (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
              #belfry wheel_2
              (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
              #belfry wheel_3
              (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
              #belfry main body
              (prop_instance_stop_animating, ":belfry_scene_prop_id"),
            (try_end),

            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, ":number_of_agents_around_belfry"),
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, ":belfry_next_entry_point_id"),
          (try_end),
        (else_try),
          (le, ":dist_between_belfry_and_its_destination", 4),
          (scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),

          (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),

          (try_begin),
            (eq, ":belfry_kind", 0),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          (else_try),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),

          (prop_instance_get_starting_position, pos0, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos0, 400),
        (try_end),
      (try_end),
    (try_end),
    ])

multiplayer_server_spawn_bots = (
  0, 0, 0, [],
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
    (try_begin),
      (gt, ":total_req", 0),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),

      (eq, ":rounded_game_first_round_time_limit_past", 1),

      (store_random_in_range, ":random_req", 0, ":total_req"),
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),
      (try_begin),
        (lt, ":random_req", 0),
        #add to team 1
        (assign, ":selected_team", 0),
      (else_try),
        #add to team 2
        (assign, ":selected_team", 1),
      (try_end),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (player_get_team_no, ":player_team_no", ":player_no"),
        (eq, ":selected_team", ":player_team_no"),

        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
          (player_slot_ge, ":player_no", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0),
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),

      (try_begin),
        (this_or_next|ge, ":selected_group", 0),
        (eq, ":number_of_active_players_wanted_bot", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
          (assign, ":is_horseman", 1),
        (else_try),
          (assign, ":is_horseman", 0),
        (try_end),

        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

          (store_mission_timer_a, ":round_time"),
          (val_sub, ":round_time", "$g_round_start_time"),

          (try_begin),
            (lt, ":round_time", 20), #at start of game spawn at base entry point
            (try_begin),
              (eq, ":selected_team", 0),
              (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 1, ":is_horseman"),
            (else_try),
              (assign, reg0, multi_initial_spawn_point_team_2),
            (try_end),
          (else_try),
            (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"),
          (try_end),
        (else_try),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),

          (try_begin),
            (eq, ":selected_team", 0),
            (assign, reg0, 0),
          (else_try),
            (assign, reg0, 32),
          (try_end),
        (else_try),
          (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"),
        (try_end),

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (try_begin),
          (eq, ":selected_team", 0),
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1),
        (else_try),
          (eq, ":selected_team", 1),
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
        (try_end),
      (try_end),
    (try_end),
    ])

multiplayer_server_manage_bots = (
  3, 0, 0, [],
  [
    (multiplayer_is_server),
    (try_for_agents, ":cur_agent"),
      (agent_is_non_player, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_get_group, ":agent_group", ":cur_agent"),
      (try_begin),
        (neg|player_is_active, ":agent_group"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (else_try),
        (player_get_team_no, ":leader_team_no", ":agent_group"),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (neq, ":leader_team_no", ":agent_team"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (try_end),
    (try_end),
    ])

multiplayer_server_check_polls = (
  1, 5, 0,
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_poll_running", 1),
    (eq, "$g_multiplayer_poll_ended", 0),
    (store_mission_timer_a, ":mission_timer"),
    (store_add, ":total_votes", "$g_multiplayer_poll_no_count", "$g_multiplayer_poll_yes_count"),
    (this_or_next|eq, ":total_votes", "$g_multiplayer_poll_num_sent"),
    (gt, ":mission_timer", "$g_multiplayer_poll_end_time"),
    (call_script, "script_cf_multiplayer_evaluate_poll"),
    ],
  [
    (assign, "$g_multiplayer_poll_running", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_poll_to_show", 0), #change map
      (eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_poll_value_to_show", 1),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])

multiplayer_server_check_end_map = (
  1, 0, 0, [],
  [
    (multiplayer_is_server),
    #checking for restarting the map
    (assign, ":end_map", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
      (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

      (try_begin),
        (eq, "$g_round_ended", 1),

        (store_mission_timer_a, ":seconds_past_till_round_ended"),
        (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
        (store_sub, ":multiplayer_respawn_period_minus_one", "$g_multiplayer_respawn_period", 1),
        (ge, ":seconds_past_till_round_ended", ":multiplayer_respawn_period_minus_one"),

        (store_mission_timer_a, ":mission_timer"),
        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (assign, ":reduce_amount", 90),
        (else_try),
          (assign, ":reduce_amount", 120),
        (try_end),

        (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
        (store_sub, ":game_max_seconds_min_n_seconds", ":game_max_seconds", ":reduce_amount"), #when round ends if there are 60 seconds to map change time then change map without completing exact map time.
        (gt, ":mission_timer", ":game_max_seconds_min_n_seconds"),
        (assign, ":end_map", 1),
      (try_end),

      (eq, ":end_map", 1),
    (else_try),
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #battle mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #fight and destroy mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege), #siege mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #in headquarters mod game cannot limited by time, only can be limited by score.
      (store_mission_timer_a, ":mission_timer"),
      (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
      (gt, ":mission_timer", ":game_max_seconds"),
      (assign, ":end_map", 1),
    (else_try),
      #assuming only 2 teams in scene
      (team_get_score, ":team_1_score", 0),
      (team_get_score, ":team_2_score", 1),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #for not-headquarters mods
        (try_begin),
          (this_or_next|ge, ":team_1_score", "$g_multiplayer_game_max_points"),
          (ge, ":team_2_score", "$g_multiplayer_game_max_points"),
          (assign, ":end_map", 1),
        (try_end),
      (else_try),
        (assign, ":at_least_one_player_is_at_game", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          (player_get_agent_id, ":agent_id", ":player_no"),
          (ge, ":agent_id", 0),
          (neg|agent_is_non_player, ":agent_id"),
          (assign, ":at_least_one_player_is_at_game", 1),
          (assign, ":num_players", 0),
        (try_end),

        (eq, ":at_least_one_player_is_at_game", 1),

        (this_or_next|le, ":team_1_score", 0), #in headquarters game ends only if one team has 0 score.
        (le, ":team_2_score", 0),
        (assign, ":end_map", 1),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":end_map", 1),
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])

multiplayer_once_at_the_first_frame = (
  0, 0, ti_once, [], [
    (start_presentation, "prsnt_multiplayer_welcome_message"),
    ])

multiplayer_battle_window_opened = (
  ti_battle_window_opened, 0, 0, [], [
    (start_presentation, "prsnt_multiplayer_team_score_display"),
    ])


common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

# common_battle_tab_press = (
  # ti_tab_pressed, 0, 0, [],
  # [
    # (try_begin),
      # (eq, "$g_battle_won", 1),
      # (call_script, "script_count_mission_casualties_from_agents"),
      # (finish_mission,0),
    # (else_try),
      # (call_script, "script_cf_check_enemies_nearby"),
      # (question_box, "str_do_you_want_to_retreat"),
    # (else_try),
      # (display_message, "str_can_not_retreat"),
    # (try_end),
    # ])

	
############ NEW v2.1 - substituted deathmod with Zephilinox version https://forums.taleworlds.com/index.php/topic,282550.0.html
common_battle_tab_press = (
    ti_tab_pressed, 0, 0, [],
    [
    (try_begin),
      (eq, "$g_battle_won", 1),
        (call_script, "script_count_mission_casualties_from_agents"),	
        (finish_mission, 0),
    (else_try),
      (eq, "$pin_player_fallen", 1),
        (call_script, "script_simulate_retreat", 0, 0, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result, -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission, 0),
    (else_try),
      (eq, "$deathcam_on", 1),
        (question_box, "str_do_you_want_to_retreat"),
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box, "str_do_you_want_to_retreat"),
    (else_try),
      (display_message, "str_can_not_retreat"),
    (try_end),
    ]
)
############################################################



common_battle_init_banner = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent_no"),
    (agent_get_troop_id, ":troop_no", ":agent_no"),
    (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),
  ])


common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box, "str_give_up_fight"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
      (finish_mission),
    (else_try),
      (question_box, "str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
    #(neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message, "str_msg_battle_won"),
    (assign, "$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen),
    (assign, "$g_battle_result",-1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

####### NEW v3.0-KOMKE START-This trigger is commented out because there is another identical one later
# common_battle_victory_display = (
#   5, 0, 0, [],
#   [
#     (eq, "$g_battle_won",1),
#     (call_script, "script_freelancer_keep_field_loot"),  ########## NEW v2.7 - lets player keep loot that he got from the field
#     (display_message, "str_msg_battle_won"),
#     ])
####### NEW v3.0-KOMKE END- 

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1, ":answer"),
     (eq, ":answer",0),
     (assign, "$pin_player_fallen", 0),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15, 0),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20, 0),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_custom_battle_question_answered = (
   ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1, ":answer"),
     (eq, ":answer",0),
     (assign, "$g_battle_result", -1),
     (call_script, "script_custom_battle_end"),
     (finish_mission),
     ])

common_custom_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_result", 0),
    # (call_script, "script_combat_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_won",0),
    (assign, "$defender_reinforcement_stage",0),
    (assign, "$attacker_reinforcement_stage",0),
    (assign, "$g_defender_reinforcement_limit", "$g_reinforcement_waves"),
    (assign, "$g_attacker_reinforcement_limit", "$g_reinforcement_waves"),
    # deathcam
    (assign, "$dmod_current_agent", -1),
    (assign, "$dmod_move_camera", -1),
    #deathcam

    (call_script, "script_combat_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [  
  # modded2x begin
  (call_script, "script_combat_music_set_situation_with_culture", mtf_sit_fight), #tom
  # modded2x end

  #tom    
  ##(music_set_culture, mtf_culture_all),
    ##(music_set_situation, mtf_sit_fight), 
    #(call_script, "script_combat_music_set_situation_with_culture"), #tom
    ])

########### NEW v2.1 - siege music
common_music_situation_update_siege = (
  30, 0, 0, [],
  [  
  # modded2x begin
  (call_script, "script_combat_music_set_situation_with_culture", mtf_sit_siege), #tom
  # modded2x end

  #tom    
  ##(music_set_culture, mtf_culture_all),
    ##(music_set_situation, mtf_sit_fight), 
    #(call_script, "script_combat_music_set_situation_with_culture"), #tom
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 0),
    (entry_point_get_position, pos10, 10),
    (try_for_range, ":cur_group", 0, grc_everyone),
      (neq, ":cur_group", grc_archers),
      (team_give_order, "$defender_team", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
    (try_end),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10), 
    #tom
    (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
    (team_give_order, "$attacker_team_2", grc_everyone, mordr_charge),
    
    ####### NEW
    # (team_give_order, "$attacker_team", grc_archers, mordr_fire_at_will),
    # (team_give_order, "$attacker_team_2", grc_archers, mordr_fire_at_will),
    # (team_give_order, "$attacker_team", grc_horse_archers, mordr_fire_at_will),
    # (team_give_order, "$attacker_team_2", grc_horse_archers, mordr_fire_at_will),
    # (team_give_order, "$attacker_team", grc_heroes, mordr_fire_at_will),
    # (team_give_order, "$attacker_team_2", grc_heroes, mordr_fire_at_will),
    ########
    # (entry_point_get_position, pos10, 0),
    # (team_set_order_position, "$attacker_team", grc_archers, pos10),
    # (team_set_order_position, "$attacker_team_2", grc_archers, pos10),
    # (team_give_order, "$attacker_team", grc_archers, mordr_hold),
    # (team_give_order, "$attacker_team_2", grc_archers, mordr_hold),
    # (team_give_order, "$attacker_team", grc_archers, mordr_stand_closer),
    # (team_give_order, "$attacker_team", grc_archers, mordr_stand_closer),
    # (team_give_order, "$attacker_team_2", grc_archers, mordr_stand_closer),
    # (team_give_order, "$attacker_team_2", grc_archers, mordr_stand_closer),
    #tom
    (set_show_messages, 1),
    ], [])
    
common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

# common_siege_defender_reinforcement_check = (
  # 3, 0, 5, [],
  # [(lt, "$defender_reinforcement_stage", 7),
   # (store_mission_timer_a, ":mission_time"),
   # (ge, ":mission_time",10),
   # (store_normalized_team_count, ":num_defenders",0),
   # (lt, ":num_defenders",8),
   # (add_reinforcements_to_entry,4, 7),
   # (val_add, "$defender_reinforcement_stage",1),
   # (try_begin),
     # (gt, ":mission_time", 300), #5 minutes, don't let small armies charge
     # (get_player_agent_no, ":player_agent"),
     # (agent_get_team, ":player_team", ":player_agent"),
     # (neq, ":player_team", "$defender_team"), #player should be the attacker
     # (neq, ":player_team", "$defender_team_2"), #player should be the attacker
     # (ge, "$defender_reinforcement_stage", 2),
     # (set_show_messages, 0),
     # (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     # (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     # (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     # (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     # (set_show_messages, 1),
     # (ge, "$defender_reinforcement_stage", 4),
     # (set_show_messages, 0),
     # (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     # (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     # (set_show_messages, 1),
   # (try_end),
   # ])
common_siege_defender_reinforcement_check = (
  3, 0, 0, [],
  ## CC
  [
    (store_mission_timer_a, ":mission_time"),
    (ge, ":mission_time",5),
    (try_begin),
      (store_mul, ":attacker_reinf_stage_mul_2", "$attacker_reinforcement_stage", 2),
      (this_or_next|lt, "$defender_reinforcement_stage", "$g_defender_reinforcement_limit"),
      (le, "$defender_reinforcement_stage", ":attacker_reinf_stage_mul_2"),
      (store_normalized_team_count, ":num_defenders_normalized", 0),
      (lt, ":num_defenders_normalized", 40),
      (add_reinforcements_to_entry,4, 28),
      (val_add, "$defender_reinforcement_stage",1),
    (try_end),
    ## CC
    # (try_begin),
      # (ge, "$defender_reinforcement_stage", 6), ## CC
      # (set_show_messages, 0),
      # (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
      # (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
      # (set_show_messages, 1),
      # (ge, "$defender_reinforcement_stage", 9), ## CC
      # # (set_show_messages, 0),
      # # (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
      # # (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
      # # (set_show_messages, 1),
    # (try_end),
   ])

common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

## CC
common_siege_attacker_reinforcement_check = (
  3, 0, 0,
  [
    (assign, ":continue", 1),
    #tom
    ##(try_begin),
    ##  (ge, "$attacker_reinforcement_stage",3),
    ##  (set_show_messages, 0),
    ##  (team_give_order, "$attacker_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
    ##  (team_give_order, "$attacker_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
    ##  (set_show_messages, 1),
    ##(try_end),
    #tom
    (try_begin),
      (ge, "$attacker_reinforcement_stage",10),
      (store_mul, ":defender_reinf_stage_mul_2", "$defender_reinforcement_stage", 2),
      (gt, "$attacker_reinforcement_stage", ":defender_reinf_stage_mul_2"),
      (assign, ":continue", 0),
    (try_end),
    (eq, ":continue", 1),
    (store_mission_timer_a, ":mission_time"),
    (ge, ":mission_time",5),
    (store_normalized_team_count, ":num_attackers",1),
    (lt, ":num_attackers",30),
    ],
  [
    (add_reinforcements_to_entry, 1, 32),
    (val_add, "$attacker_reinforcement_stage", 1),
    ])
## CC

# common_siege_attacker_reinforcement_check = (
  # 1, 0, 5,
  # [
    # (lt, "$attacker_reinforcement_stage",5),
    # (store_mission_timer_a, ":mission_time"),
    # (ge, ":mission_time",10),
    # (store_normalized_team_count, ":num_attackers",1),
    # (lt, ":num_attackers",6),
    # ],
  # [
    # (add_reinforcements_to_entry, 1, 8),
    # (val_add, "$attacker_reinforcement_stage", 1),
    # ])

# common_siege_attacker_do_not_stall = (
  # 3, 0, ti_once, [],
 # 5, 0, 0, [],
  # [ 
    ###tom
    # (set_show_messages, 0),
    # (try_for_range, ":group", 0, 9),
      # (team_give_order, "$attacker_team", ":group", mordr_hold_fire),
    # (try_end),
    
    # (try_for_range, ":group", 0, 9),
      # (team_give_order, "$attacker_team_2", ":group", mordr_hold_fire),
    # (try_end),
    # (set_show_messages, 1),
    ###tom
    #Make sure attackers do not stall on the ladders...
    #(try_for_agents, ":agent_no"),
    #  (agent_is_human, ":agent_no"),
    #  (agent_is_alive, ":agent_no"),
    #  (agent_get_team, ":agent_team", ":agent_no"),
    #  (this_or_next|eq, ":agent_team", "$attacker_team"),
    #  (eq, ":agent_team", "$attacker_team_2"),
    #  ##tom
    #  # (agent_get_division , ":division", ":agent_no"),
    #  # (team_get_movement_order, ":order", ":agent_team", ":agent_no"),
    #  # (this_or_next|eq, ":division", grc_infantry),
    #  # (eq, ":order", mordr_charge),
    #  ##tom
    #  (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    #(try_end),
    # ])
	
##################### NEW v1.9 - 
common_siege_attacker_do_not_stall = (5, 0, 0, [],
  [
  (try_for_agents, ":agent_no"),   #Make sure attackers do not stall on the ladders...
    (agent_is_human, ":agent_no"),
    (agent_is_alive, ":agent_no"),
    (agent_get_team, ":agent_team", ":agent_no"),
    (this_or_next|eq, ":agent_team", "$attacker_team"),(eq, ":agent_team", "$attacker_team_2"),
    (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
  (try_end),
    ])
###############################################################


common_battle_check_friendly_kills = (
  2, 0, 0, 
  [

  ],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  5, 60, ti_once, ## CC
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
	#(neg|main_hero_fallen, 0),

    (set_mission_result,1),
    (display_message, "str_msg_battle_won"),
    (assign, "$g_battle_won",1),
    (assign, "$g_battle_result", 1),
	####### NEW v3.2 - fixes player receiving the items from the troop he bodyslided into
    (try_begin),        
	  # (get_player_agent_no, ":player"),
	  # (agent_get_troop_id, ":troop_id", ":player"),
      # (eq, ":troop_id", "trp_player"),
	  (eq, "$auxilary_player_active", 0), 
        (call_script, "script_freelancer_keep_field_loot"),  ####### NEW v3.0-KOMKE
    (try_end),
	##############
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (assign, "$do_once_3", 0),  ######### resets the global so it can be used again in next siege
    (finish_mission, 1),
    ])
## deathcam ########################
common_battle_check_defeat_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (main_hero_fallen),
    (assign, ":num_allies", 0),
    (try_for_agents, ":agent"),
        (agent_is_ally, ":agent"),
        (agent_is_alive, ":agent"),
        (val_add, ":num_allies", 1),
    (try_end),
    (eq, ":num_allies", 0), 
    (set_mission_result,-1),
    #(eq, ":num_allies", 0),## tom, moved up
    (display_message, "@Battle lost..."),
    (assign, "$g_battle_won",-1),
    (assign, "$g_battle_result", -1),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (assign, "$do_once_3", 0),  ######### resets the global so it can be used again in next siege
    (finish_mission, 0),
    ])

common_battle_defeat_display = (
  10, 0, 0, [],
  [
    (eq, "$g_battle_won",-1),
    (display_message, "@Battle lost! Press tab key to leave..."),
    ])
## end deathcam ########################

common_battle_victory_display = (
  5, 0, 0, [],
  [
    (eq, "$g_battle_won",1),
    # (call_script, "script_freelancer_keep_field_loot"),  ########## NEW v2.7 - lets player keep loot that he got from the field####### NEW v3.0-KOMKE moved to common_battle_check_victory_condition
    (display_message, "str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    #(get_player_agent_no, ":player_agent"),
    (display_message, "@Refilling defender ammo..."),
    (try_for_agents, ":cur_agent"),
      # rafi refill player? (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])
    
common_siege_refill_ammo_sitd = (
  # 120, 0, 0, [],
  180, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (display_message, "@Refilling defender ammo..."),
    (get_player_agent_no, ":player_agent"),
    (try_for_agents, ":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      #(agent_get_combat_state, ":agent_cs", ":cur_agent"),
      # (try_begin), ##defenders refill
        (this_or_next|eq, ":agent_team", "$defender_team"),
        (eq, ":agent_team", "$defender_team_2"),
        (agent_refill_ammo, ":cur_agent"),
      # (else_try), ##attackers become infantry
        # (agent_get_ammo, ":ammo", ":cur_agent", 0),
        # (call_script, "script_get_closest_enemy_distance", ":cur_agent"),
        # (this_or_next|gt, reg1, 5500),
        # (this_or_next|le, ":ammo", 0),
        # (eq, ":agent_cs", 7), #does not see target
        # (agent_set_division, ":cur_agent", grc_infantry),
        # (agent_ai_set_always_attack_in_melee, ":cur_agent", 1),
      # (try_end),
    (try_end),
    ###player refill
    (try_begin),
      (agent_get_team, ":agent_team", ":player_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":player_agent"),
    (try_end),
    ])

# common_siege_check_defeat_condition = (
  # 1, 4, ti_once,
  # [
    # (main_hero_fallen),
    # ],
  # [
    # (assign, "$pin_player_fallen", 1),
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":agent_team", ":player_agent"),
    # (try_begin),
      # (neq, "$attacker_team", ":agent_team"),
      # (neq, "$attacker_team_2", ":agent_team"),
      # (str_store_string, s5, "str_siege_continues"),
      # (call_script, "script_simulate_retreat", 8, 15, 3),
    # (else_try),
      # (str_store_string, s5, "str_retreat"),
      # (call_script, "script_simulate_retreat", 5, 20, 4),
    # (try_end),
    # (assign, "$g_battle_result", -1),
    # (set_mission_result,-1),
    # (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission,0),
    # ])

# deathcam

common_siege_check_defeat_condition = (
  1, 4, ti_once,
  [
   (eq, "$enable_deahtcam", 1), #TOM auxiliary player
   (main_hero_fallen),
   (assign, ":pteam_alive", 0),
   (try_for_agents, ":agent"), #Check players team is dead
     (neq, ":pteam_alive", 1), #Break loop
     (agent_is_ally, ":agent"),
     (agent_is_alive, ":agent"),
       (assign, ":pteam_alive", 1),
   (try_end),
   (eq, ":pteam_alive", 0),
  ],
	
  [
   (assign, "$pin_player_fallen", 1),
   (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
   (display_message, "@If you choose to watch the fight you can use the mouse scroll up and down to switch between troop view or AWDS keys for free camera view."),
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":agent_team", ":player_agent"),
    # (try_begin),
      # (neq, "$attacker_team", ":agent_team"),
      # (neq, "$attacker_team_2", ":agent_team"),
      # (str_store_string, s5, "str_siege_continues"),
      # (call_script, "script_simulate_retreat", 8, 15),
    # (else_try),
      # (str_store_string, s5, "str_retreat"),
      # (call_script, "script_simulate_retreat", 5, 20),
    # (try_end),
    # (assign, "$g_battle_result", -1),
    # (set_mission_result,-1),
    # (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission,0),
    ])

# deathcam

#TOM ORIGINAL 
common_battle_order_panel = (
   0, 0, 0, [],
   [
     (game_key_clicked, gk_view_orders),
     (neg|is_presentation_active, "prsnt_battle"),
     (start_presentation, "prsnt_battle"),
     ])
##################################################
##### troop_ratio_bar
##################################################
# (0, 0, ti_once, [], [(start_presentation, "prsnt_troop_ratio_bar")]),
##################################################
##### troop_ratio_bar
##################################################



common_battle_order_panel_tick = (
   0.1, 0, 0, [],
   [
     (is_presentation_active, "prsnt_battle"),
     (call_script, "script_update_order_panel_statistics_and_map"),
     ])
#TOM ORIGINAL 

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message, "str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

# common_siege_init_ai_and_belfry = (
  # 0, 0, ti_once,
  # [
    # (call_script, "script_siege_init_ai_and_belfry"),
    # ], [])

# common_siege_move_belfry = (
  # 0, 0, ti_once,
  # [
    # (call_script, "script_cf_siege_move_belfry"),
    # ], [])

# common_siege_rotate_belfry = (
  # 0, 2, ti_once,
  # [
    # (call_script, "script_cf_siege_rotate_belfry_platform"),
    # ],
  # [
    # (assign, "$belfry_positioned", 3),
    # ])

# common_siege_assign_men_to_belfry = (
  # 0, 0, ti_once,
  # [
    # (call_script, "script_cf_siege_assign_men_to_belfry"),
    # ], [])


########################## NEW v2.5
enhanced_siege_lance_spear_fix = (
    0, 0, 5, 
    [], 
    [
       (try_for_agents, ":agent"),
         (agent_get_troop_id, ":troop_id", ":agent"),
         (agent_get_horse, ":horse", ":agent"),
################################
         (try_begin),#no lance on foot
           (neg|troop_is_guarantee_ranged, ":troop_id"),
           (le, ":horse", 0),
           (agent_get_wielded_item, ":wielded", ":agent", 0),
           (this_or_next|is_between, ":wielded", "itm_light_lance", "itm_bamboo_spear"),
           (is_between, ":wielded", "itm_crusader_knight_spear_a", "itm_crusader_spear_a"),
           (assign, ":top", 4),
           (try_for_range, reg0, 0, ":top"),
             (agent_get_item_slot, ":item", ":agent", reg0),
             (is_between, ":item", 1, "itm_items_end"),
             #(gt, ":item", 0),
             (this_or_next|neg|is_between, ":wielded", "itm_light_lance", "itm_bamboo_spear"),
             (neg|is_between, ":wielded", "itm_crusader_knight_spear_a", "itm_crusader_spear_a"),
             (item_get_type, ":item_type", ":item"),
             (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
             (this_or_next|eq, ":item_type", itp_type_polearm),
             (eq, ":item_type", itp_type_one_handed_wpn),
             (agent_set_wielded_item, ":agent", ":item"),
             (assign, ":top", -1),
           (try_end),    
################################
         (else_try), #TOM - SPEAR USSAGE
           (neg|troop_is_guarantee_ranged, ":troop_id"),
           #(agent_get_horse, ":horse", ":agent"),
           (le, ":horse", 0), #unmounted
           (agent_get_wielded_item, ":wielded", ":agent", 0),
           (this_or_next|neg|is_between, ":wielded", "itm_bamboo_spear", "itm_staff"),
           (neg|is_between, ":wielded", "itm_crusader_spear_a", "itm_mace_6"),
           #(neg|is_between, ":wielded", "itm_flag_pole_1", "itm_items_end"), #not a flag
           (try_for_range, ":item", "itm_bamboo_spear", "itm_staff"), # adjust as needed
             #(gt, ":item", 0),
             #(agent_equip_item, ":agent", ":item"),
             (agent_set_wielded_item, ":agent", ":item"),
           (try_end),
################################
         (else_try), #tom - range usage
           (troop_is_guarantee_ranged, ":troop_id"),
           (agent_get_team, ":team", ":agent"),
           (agent_get_division, ":division", ":agent"),    
           (team_get_hold_fire_order, ":order", ":team", ":division"),
           (neq, ":order", 1), #mordr_hold_fire
           (is_between, ":wielded", 1, "itm_items_end"),
           (item_get_type, ":type", ":wielded"),            
           (this_or_next|le, ":wielded", -1),
           (this_or_next|neq, ":type", itp_type_thrown),
           (this_or_next|neq, ":type", itp_type_crossbow),
           (neq, ":type", itp_type_bow),
           (call_script, "script_get_closest_enemy_distance_new", ":agent", ":team", 300),
           (assign, ":nearest_enemy", reg1),
           (gt, ":nearest_enemy", 300), #7 meters.
           (assign, ":top", 4),
           (try_for_range, reg0, 0, ":top"),
             (agent_get_item_slot, ":item_no", ":agent", reg0),
             (is_between, ":item_no", 1, "itm_items_end"),
             (item_get_type, ":type", ":item_no"),
             (this_or_next|eq, ":type", itp_type_thrown),
             (this_or_next|eq, ":type", itp_type_bow),
             (eq, ":type", itp_type_crossbow),
             (agent_set_wielded_item, ":agent", ":item_no"),
             (assign, ":top", -1),
           (try_end),
################################ 
       (try_end),
     (try_end),
    ]
)
####################################################

  
################# NEW v1.3 - added this from Azgad A Story Of Calradia v1.0
enhanced_town_resident_behavior_init = (
  0, 0, ti_once, [], [
	  (assign, ":continue", 1),
	  ####### NEW v3.1 - if fief owner is the player don't activate
      (try_begin),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),  
	      (assign, ":continue", 0),
	  (try_end),
	  #########
	  ########### NEW v3.1 - if bounty quest is active don't activate
      (try_begin),
        (check_quest_active, "qst_bounty_1"),
        (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_2"),
        (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_3"),
        (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_4"),
        (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_5"),
        (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_6"),
        (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_hunt_down_fugitive"),
        (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (try_end),
	  (eq, ":continue", 1),
	  ######################
	  (get_player_agent_no, ":player_agent"),
      (agent_set_team, ":player_agent", 0),
      (team_set_relation, 0, 1, 1),
      (team_set_relation, 0, 2, -1),
      (team_set_relation, 1, 2, 0),
      (try_for_agents, ":cur_agent"),
          (neq, ":cur_agent",  ":player_agent"),
          (agent_set_team, ":cur_agent",  1),
      (try_end),
      (assign, "$town_residents_enraged", 0),
      (assign, "$town_residents_condone_chance", 0),
      (assign, "$town_residents_condoned", 0),
      (assign, "$troop_restore_offset", 1),
  ])
enhanced_town_resident_behavior = (
  0, 0, 0, [], [
	  (assign, ":continue", 1),
	  ####### NEW v3.1 - if fief owner is the player don't activate
      (try_begin),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),  
	      (assign, ":continue", 0),
	  (try_end),
	  #########
	  ########### NEW v3.1 - if bounty quest is active don't activate
      (try_begin),
        (check_quest_active, "qst_bounty_1"),
        (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_2"),
        (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_3"),
        (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_4"),
        (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_5"),
        (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_bounty_6"),
        (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (else_try),
        (check_quest_active, "qst_hunt_down_fugitive"),
        (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
	      (assign, ":continue", 0),
	  (try_end),
	  (eq, ":continue", 1),
	  ######################
      (get_player_agent_no, ":player_agent"),
      (agent_is_alive, ":player_agent"),
      (agent_get_position,pos1, ":player_agent"),
      (agent_get_attack_action, ":attack_action_state",  ":player_agent"),
      (agent_get_defend_action, ":defend_action_state",  ":player_agent"),
      (try_begin),
          (eq, ":attack_action_state", 2),
          (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
			 
              (neq, ":cur_agent",  ":player_agent"),
              (agent_get_position,pos2, ":cur_agent"),
              (agent_get_team, ":cur_agent_team",  ":cur_agent"),
              (eq, ":cur_agent_team", 1),
              (try_begin),
                  (position_is_behind_position,pos2,pos1),
              (else_try), 
                  (get_distance_between_positions, ":dist", pos1,pos2),
                  (lt, ":dist", 100),  
                  
                  (agent_force_rethink, ":cur_agent"),
                  (agent_ai_set_aggressiveness, ":cur_agent", 199),
                  (agent_set_team, ":cur_agent",  2),
              (try_end),
          (try_end),
      (else_try),
          (eq, "$town_residents_enraged", 0),
          (this_or_next|eq, ":defend_action_state", 2),
          (eq, ":defend_action_state", 1),
          (try_begin),
              (ge, "$town_residents_condone_chance", 500),
              (val_sub, "$town_residents_condone_chance", 1),
              (val_add, "$town_residents_condoned", 1),
          (try_end),
          (lt, "$town_residents_condone_chance", 500),
          (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
			  
              (neq, ":cur_agent",  ":player_agent"),
              (agent_get_team, ":cur_agent_team",  ":cur_agent"),
              (eq, ":cur_agent_team", 2),
              (agent_add_relation_with_agent, ":player_agent",  ":cur_agent", 1),
              (agent_force_rethink, ":cur_agent"),
              (agent_ai_set_aggressiveness, ":cur_agent",  0),
              (agent_set_team, ":cur_agent",  1),
              #(display_message, "str_saldiri_1"),
          (try_end),
      (else_try),
          (eq, "$town_residents_enraged", 0),
          (this_or_next|gt, "$town_residents_condoned", 1500),
          (ge, "$town_residents_condone_chance", 2000),
          (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
			  
              (neq, ":cur_agent",  ":player_agent"),
              
              (agent_force_rethink, ":cur_agent"),
              (agent_ai_set_aggressiveness, ":cur_agent", 199),
              (agent_set_team, ":cur_agent",  2),
          (try_end),
          (assign, "$town_residents_enraged", 1),
          (assign, "$town_residents_condoned", 0),
          #(party_get_slot, ":center_relation",  "$current_town", slot_center_player_relation),
         # (val_sub, ":center_relation", 7),
         # (party_set_slot, "$current_town", slot_center_player_relation, ":center_relation"),
          #(party_get_slot, ":town_lord",  "$current_town", slot_town_lord),
         # (call_script, "script_change_player_relation_with_troop",  ":town_lord", -1),
          (display_message, "str_saldiri_2"),
      (else_try),
          (eq, "$town_residents_enraged", 1),
          (agent_get_wielded_item, ":wielded_item",  ":player_agent", 0),
          (neq, ":wielded_item",  -1),
          (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
			  
              (neq, ":cur_agent",  ":player_agent"),
              (agent_get_troop_id, ":troop_type",  ":cur_agent"),
              (agent_get_wielded_item, ":wielded_item",  ":cur_agent", 0),
              (try_begin),
                  (neq, ":wielded_item",  -1),
                  (agent_clear_scripted_mode, ":cur_agent"),
              (try_end),
              (neg|is_between, ":troop_type",  soldiers_begin, soldiers_end),
              # (eq, ":wielded_item",  -1),  ######### 1257 civilians have weapons
              (agent_ai_set_aggressiveness, ":cur_agent",  0),
              (agent_set_speed_limit, ":cur_agent", 10),
              (party_get_slot, ":town_scene",  "$current_town",  slot_town_center),
              (party_get_slot, ":tavern_scene",  "$current_town",  slot_town_tavern),
              (store_current_scene, ":cur_scene"),
              (try_begin),
                  (eq, ":cur_scene",  ":town_scene"),
                  (entry_point_get_position, pos3, 2),
              (else_try),
                  (eq, ":cur_scene",  ":tavern_scene"),
                  (entry_point_get_position, pos3, 0),
              (try_end),
              (agent_set_scripted_destination_no_attack, ":cur_agent", pos3, 1),
              (agent_force_rethink, ":cur_agent"),
              (agent_get_position ,pos2, ":cur_agent"),
              (get_distance_between_positions, ":dist", pos2, pos3),
              (try_begin),
                  (gt, "$town_residents_condoned", 0),
                  (agent_set_team, ":cur_agent",  1),
              (try_end),
              (try_begin),
                  (le, ":dist", 300),
                  (agent_fade_out, ":cur_agent"),
                  (val_add, "$town_residents_condoned", 1),
                  # (try_begin),  ######## added below
                      # (gt, "$town_residents_condoned", 2),
                      # (call_script, "script_return_random_troop_from_garrison", 1),
                      # (assign, ":troop", reg0),
                      # (call_script, "script_remove_troops_from_garrison",  ":troop", 1),
                      # (set_spawn_position, pos3),
                      # (spawn_agent, ":troop"),
                      # (agent_set_team, reg0, 2),
                      # (agent_add_relation_with_agent, ":player_agent",  reg0, -1),
                      # (agent_ai_set_aggressiveness, reg0, 199),
                      # (assign, "$town_residents_condoned", 0),
                      # (display_message, "str_saldiri_3"),
                  # (try_end),
              (try_end),
          (try_end),
      (try_end),
  ])
  
enhanced_town_spawn_guards = (
 2, 0, 3, [], [
	(assign, ":continue", 1),
	####### NEW v3.1 - if fief owner is the player don't activate
    (try_begin),
      (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),  
	    (assign, ":continue", 0),
	(try_end),
	#########
	########### NEW v3.1 - if bounty quest is active don't activate
    (try_begin),
      (check_quest_active, "qst_bounty_1"),
      (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_bounty_2"),
      (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_bounty_3"),
      (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_bounty_4"),
      (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_bounty_5"),
      (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_bounty_6"),
      (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(else_try),
      (check_quest_active, "qst_hunt_down_fugitive"),
      (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
	    (assign, ":continue", 0),
	(try_end),
	(eq, ":continue", 1),
	######################
   (get_player_agent_no, ":player_agent"),
   (agent_is_alive, ":player_agent"),
   (party_get_slot, ":town_scene",  "$current_town",  slot_town_center),
   (party_get_slot, ":tavern_scene",  "$current_town",  slot_town_tavern),
   (store_current_scene, ":cur_scene"),
   (try_begin),
       (eq, ":cur_scene",  ":town_scene"),
       (entry_point_get_position, pos3, 2),
   (else_try),
       (eq, ":cur_scene",  ":tavern_scene"),
       (entry_point_get_position, pos3, 0),
   (try_end),
   # (agent_set_scripted_destination_no_attack, ":cur_agent", pos3, 1),
   # (agent_force_rethink, ":cur_agent"),
   # (agent_get_position ,pos2, ":cur_agent"),
   # (get_distance_between_positions, ":dist", pos2, pos3),
   (try_begin),
       (gt, "$town_residents_condoned", 2),
       (call_script, "script_return_random_troop_from_garrison", 1),
       (assign, ":troop", reg0),
       (gt, ":troop", 0),
       (call_script, "script_remove_troops_from_garrison",  ":troop", 1),
       (set_spawn_position, pos3),
       (spawn_agent, ":troop"),
       (agent_set_team, reg0, 2),
       (agent_add_relation_with_agent, ":player_agent",  reg0, -1),
       (agent_ai_set_aggressiveness, reg0, 199),
       (agent_get_position, pos3, ":player_agent"),
       (agent_set_scripted_destination, reg0, pos3, 1),
       (agent_force_rethink, reg0),
       (val_sub, "$town_residents_condoned", 1),
       (display_message, "str_saldiri_3"),
   (try_end),
 ])
 
enhanced_town_resident_behavior_killed = (
 ti_on_agent_killed_or_wounded, 0, 0, [], [
	 (assign, ":continue", 1),
	 ####### NEW v3.1 - if fief owner is the player don't activate
     (try_begin),
       (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),  
	     (assign, ":continue", 0),
	 (try_end),
	 #########
	 ########### NEW v3.1 - if bounty quest is active don't activate
     (try_begin),
       (check_quest_active, "qst_bounty_1"),
       (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_2"),
       (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_3"),
       (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_4"),
       (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_5"),
       (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_6"),
       (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_hunt_down_fugitive"),
       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (try_end),
	 (eq, ":continue", 1),
	  ######################
     #(store_trigger_param_1, ":dead_agent_no"),
     (store_trigger_param_2, ":killer_agent_no"),
     #(store_trigger_param_3, ":is_wounded"),
     (get_player_agent_no, ":player_agent"),
     (agent_is_alive, ":player_agent"),
     (eq, ":killer_agent_no",  ":player_agent"),
     (try_for_agents, ":cur_agent"),
         (agent_is_human, ":cur_agent"),
         (agent_is_alive, ":cur_agent"),
		 
         (neq, ":cur_agent",  ":player_agent"),
         
         (agent_force_rethink, ":cur_agent"),
         (agent_ai_set_aggressiveness, ":cur_agent", 199),
         (agent_set_team, ":cur_agent",  2),
     (try_end),
     (assign, "$town_residents_enraged", 1),
     # (assign, "$town_residents_condoned", 0),
     (party_get_slot, ":center_relation",  "$current_town", slot_center_player_relation),
     (val_sub, ":center_relation", 1),
     (party_set_slot, "$current_town", slot_center_player_relation, ":center_relation"),
     (display_message, "str_saldiri_2"),
     (val_add, "$town_residents_condoned", 1),
     (party_get_slot, ":town_lord",  "$current_town", slot_town_lord),
     (call_script, "script_change_player_relation_with_troop",  ":town_lord", -1),
    # (party_get_slot, ":town_lord",  "$current_town", slot_town_lord),
     
 ])
enhanced_town_resident_behavior_hit = (
 ti_on_agent_hit, 0, 0, [], [
	 (assign, ":continue", 1),
	 ####### NEW v3.1 - if fief owner is the player don't activate
     (try_begin),
       (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),  
	     (assign, ":continue", 0),
	 (try_end),
	 #########
	 ########### NEW v3.1 - if bounty quest is active don't activate
     (try_begin),
       (check_quest_active, "qst_bounty_1"),
       (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_2"),
       (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_3"),
       (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_4"),
       (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_5"),
       (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_bounty_6"),
       (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (else_try),
       (check_quest_active, "qst_hunt_down_fugitive"),
       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
	     (assign, ":continue", 0),
	 (try_end),
	 (eq, ":continue", 1),
	 ######################
     (store_trigger_param_1, ":hit_agent_no"),
     (store_trigger_param_2, ":attacker_agent_no"),
     #(store_trigger_param_3, ":damage"),
     (get_player_agent_no, ":player_agent"),
     (agent_is_alive, ":player_agent"),
     (eq, ":attacker_agent_no",  ":player_agent"),
     
     (agent_force_rethink, ":hit_agent_no"),
     (agent_ai_set_aggressiveness, ":hit_agent_no", 199),
     (agent_set_team, ":hit_agent_no",  2),
     (val_add, "$town_residents_condone_chance", 1000),
     (eq, "$town_residents_enraged", 0),
     #(display_message, "str_saldiri_4"),
     #(party_get_slot, ":center_relation",  "$current_town", slot_center_player_relation),
    # (val_sub, ":center_relation", 1),
    # (party_set_slot, "$current_town", slot_center_player_relation, ":center_relation"),
     #(party_get_slot, ":town_lord",  "$current_town", slot_town_lord),
     
 ])	
####################################################################
  
  
  


############## NEW v3.8
common_lance_use_spawn = (
   # Just after spawn, mark lancers using a slot.
   # Force lancers to equip lances.
  1, 0, ti_once, [], [(call_script, "script_lance_use_classify_agent")])
   
   
common_lance_use = (
   # Check to make sure there are no lance users on foot, if so force them to
   # switch to their sword. This should also affect troops that were NEVER mounted,
   # but are still equipped with lances, such as Taiga Bandits.
   # For mounted lancers affect their Decision on weapon use, based on if the
   # closest 3 enemies are within 5 meters and if currently attacking/defending.
   2, 0, 0, [],
   [# Run through all active NPCs on the battle field.
   (try_for_agents, ":agent"),
     # Hasn't been defeated.
        (agent_is_alive, ":agent"),
        (agent_get_slot, ":lance", ":agent", slot_agent_lance),
        (gt, ":lance", 0),  # Lancer?
     # Get wielded item.
        (agent_get_wielded_item, ":wielded", ":agent", 0),
      # They riding a horse?
        (agent_get_horse, ":horse", ":agent"),
        (try_begin),
            (le, ":horse", 0), # Isn't riding a horse.
            (agent_set_slot, ":agent", slot_agent_lance, 0), # No longer a lancer
            (eq, ":wielded", ":lance"), # Still using lance?
            (call_script, "script_lance_use_backup_weapon", ":agent"), # Then equip a close weapon
        (else_try),
     # Still mounted
            (agent_get_position, pos1, ":agent"),    
            (agent_get_team, ":team_no", ":agent"),  # Find distance of nearest 3 enemies
            (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", pos1),
            (assign, ":avg_dist", reg0),
            (try_begin),
                (lt, ":avg_dist", 500), # Are the enemies within 5 meters?
                (agent_get_combat_state, ":combat", ":agent"),
                (gt, ":combat", 3), # Agent currently in combat? ...avoids switching before contact
                (eq, ":wielded", ":lance"), # Still using lance?
                (call_script, "script_lance_use_backup_weapon", ":agent"), # Then equip a close weapon
            (else_try),
                (neq, ":wielded", ":lance"), # Enemies farther than 5 meters and/or not fighting, and not using lance?
                (agent_set_wielded_item, ":agent", ":lance"), # Then equip it!
            (try_end),
        (try_end),
   (try_end),
])

lance_use_triggers = [
    common_lance_use_spawn,
    common_lance_use,
    ]
############################


tournament_triggers = [
common_battle_init_banner, #tom
  (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                       (assign, "$g_arena_training_num_agents_spawned", 0)]),
  (ti_inventory_key_pressed, 0, 0, [(display_message, "str_cant_use_inventory_arena")], []),
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      (set_trigger_result, 1),
    (else_try),
      (question_box, "str_give_up_fight"),
    (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1, ":answer"),
    (eq, ":answer",0),
    (try_begin),
      (eq, "$g_mt_mode", abm_tournament),
      #(call_script, "script_end_tournament_fight", 0),
      (call_script, "script_end_tournament_fight_new", 0),
    (else_try),
      (eq, "$g_mt_mode", abm_training),
      (get_player_agent_no, ":player_agent"),
      (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      (get_player_agent_no, ":player_agent"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", ":player_agent"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),

  (0, 0, ti_once, [],
   [
     (eq, "$g_mt_mode", abm_tournament),
     (play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

     ###tom modified
  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   #(this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin), #player won
         #(neg|main_hero_fallen),
         (get_player_agent_no, ":p_agent"),
         (agent_get_team, ":p_team", ":p_agent"),
         (assign, ":player_won", 0),
         (try_for_agents, ":agent"),
           (agent_is_alive, ":agent"),
           (agent_is_human, ":agent"),
           (agent_get_team, ":team", ":agent"),
           (eq, ":team", ":p_team"),
           (assign, ":player_won", 1),
         (try_end),
         (eq, ":player_won", 1),
         #(call_script, "script_end_tournament_fight", 1),
         (stop_all_sounds, 0),  ####### NEW v3.8
         (call_script, "script_end_tournament_fight_new", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try), #player lost
         #(call_script, "script_end_tournament_fight", 0),
         (stop_all_sounds, 0),  ####### NEW v3.8
         (call_script, "script_end_tournament_fight_new", 0),
         (finish_mission),
       (try_end),
    ]), 
    ###tom
    
    ###backup
    # (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   # (this_or_next|main_hero_fallen),
                   # (num_active_teams_le, 1)],
   # [
       # (try_begin),
         # (neg|main_hero_fallen),
         # (call_script, "script_end_tournament_fight", 1),
         # (call_script, "script_play_victorious_sound"),
         # (finish_mission),
       # (else_try),
         # (call_script, "script_end_tournament_fight", 0),
         # (finish_mission),
       # (try_end),
    # ]),

  (ti_battle_window_opened, 0, 0, [], [(eq, "$g_mt_mode", abm_training),(start_presentation, "prsnt_arena_training")]),

  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       (assign, "$g_arena_training_max_opponents", 50), ############ NEW v1.8 - NOW THE FUN BEGINS! 
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most 40 agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       (get_player_agent_no, ":player_agent"),
       (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       # (set_visitor, 35, "trp_veteran_fighter"),
       # (set_visitor, 36, "trp_euro_horse_4"),
       # rafi
       (party_get_slot, ":arena_master", "$current_town", slot_town_arena_master),
       (set_visitor, 52, ":arena_master"),
       #rafi
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
       ]),


  (1, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       (lt, ":num_active_fighters", 20), ############## YES!
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 50),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 1),
       (val_add, ":added_troop", ":added_troop_sequence"),
	   #############  NEW v3.2 - reverted back to vanilla 1257 settings
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),   ############## YES!
	   ##########################
	   # (store_random_in_range, ":added_troop", regular_troops_begin, regular_troops_end), ############# YES!
       (assign, ":end_cond", 10000),
       (get_player_agent_no, ":player_agent"),
       (agent_get_position, pos5, ":player_agent"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 0, 39),
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),
       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
       (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 2), ############## YES!
       (store_div, ":time_reduction", ":new_spawned_count", 4),
       (val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
       ]),

  (0, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", ":player_agent"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           # (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", ":player_agent"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           # (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             # (assign, ":strongest_team", ":t"),
           (try_end),
           # (store_random_in_range, ":rand", 5, 100),
           # (try_begin),
             # (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             # (assign, ":selected_team", ":strongest_team"),
           # (try_end),
           # (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", ":player_agent"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),

       common_weapon_break
  # ] + lance_usage + must_1257_triggers + sp_shield_bash_triggers
  ] + lance_use_triggers + must_1257_triggers + sp_shield_bash_triggers  ####### NEW v3.8
  


########################## NEW v2.0/2.1
enhanced_common_battle_triggers = [
	improved_horse_archer_ai,
	killcount_and_troop_ratio_bar,
	killcount_and_troop_ratio_bar_refresh,  ########## NEW v3.8
	# reassign_archers_to_division,
	# reassign_horseless_cavalry_to_division,
    # order_weapon_type_triggers,    ########## NEW v2.1 - moved those from mission_templates to here and then commented them because they were causing problems with advanced formations
    # order_volley_triggers,    ########## 
] + reassign_archers_to_division + reassign_horseless_cavalry_to_division + lance_use_triggers ####### NEW v3.8

#######################################################################################

########################## NEW v2.5
enhanced_common_siege_triggers = [
	killcount_and_troop_ratio_bar,
	killcount_and_troop_ratio_bar_refresh,  ########## NEW v3.3
	# enhanced_siege_lance_spear_fix,
# ] + lance_usage
] + lance_use_triggers ####### NEW v3.8

#######################################################################################

############ NEW v3.0
fief_civilian_triggers = [
    enhanced_town_resident_behavior_init,
    enhanced_town_resident_behavior,
    enhanced_town_resident_behavior_killed,
    enhanced_town_resident_behavior_hit,
    enhanced_town_spawn_guards,
  ]  
  
############
siege_1257 = [
    siege_tick,
    siege_init,
    siege_attacker_regroup,
    siege_battle_size_before_battle,
	archers_move_to_positions,   ########## NEW v1.9
	common_siege_attacker_do_not_stall,   ########## NEW v2.5
 ]
########################




