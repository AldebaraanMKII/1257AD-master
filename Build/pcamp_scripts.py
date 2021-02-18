from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_items import *
from header_terrain_types import *
from header_mission_templates import *

from util_wrappers import *
from util_scripts import *

script_patches = [
	# Enter correct encounter menu
	[
		SD_OP_BLOCK_INSERT,
		"game_event_party_encounter",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(jump_to_menu, "mnu_cattle_herd"), 0,

		[
			(else_try),
				(party_slot_eq, "$g_encountered_party", slot_party_type, spt_player_camp),
				(jump_to_menu, "mnu_player_camp"),
		]
	],
	# Compute party size limit for the camp
	[
		SD_OP_BLOCK_INSERT,
		"game_get_party_companion_limit",
		D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(val_add, ":limit", ":charisma"), 0,

		[
			(try_begin),
				# some stupid menu code calls the script without parameters,
				# so only use this in the right context to avoid errors
				(eq, "$g_encountered_party_template", "pt_player_camp"),
				#(assign, ":limit", 15), (eq, 1, 0), # debug
				(store_script_param_1, ":camp_party"),
				(party_slot_eq, ":camp_party", slot_party_type, spt_player_camp),

				# keep a percentage of player stats
				(val_mul, ":limit", pcamp_player_party_size_percentage),
				(val_div, ":limit", 100),

				# add bonus from commander skills
				(party_get_slot, ":troop_no", ":camp_party", slot_pcamp_camp_commander),
				(store_skill_level, ":skill", "skl_leadership", ":troop_no"),
				(store_attribute_level, ":charisma", ":troop_no", ca_charisma),
				(val_mul, ":skill", pcamp_commander_leadership_size_bonus),
				(val_mul, ":charisma", pcamp_commander_charisma_size_bonus),
				(val_add, ":limit", ":skill"),
				(val_add, ":limit", ":charisma"),
			(try_end),
		]
	],
	# Compute prisoner count limit for the camp
	[
		SD_OP_BLOCK_INSERT,
		"game_get_party_prisoner_limit",
		D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(store_mul, ":limit", ":skill", "$g_party_prisoners_per_prisoner_management_point"), 0,

		[
			(try_begin),
				(store_script_param_1, ":camp_party"),
				(party_slot_eq, ":camp_party", slot_party_type, spt_player_camp),

				# keep a percentage of player stats
				(val_mul, ":limit", pcamp_player_prisoner_count_percentage),
				(val_div, ":limit", 100),

				# recompute prisoner limit from commander skills and troop count
				(party_get_slot, ":troop_no", ":camp_party", slot_pcamp_camp_commander),
				(store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
				(val_mul, ":skill", pcamp_commander_prisoner_skill_bonus),
				(val_add, ":limit", ":skill"),
				(party_get_num_companions, ":troops", ":camp_party"),
				(val_div, ":troops", pcamp_troop_count_prisoner_divisor),
				(val_add, ":limit", ":troops"),
			(try_end),
		]
	],
	# After a battle ends, check if any camps have been destroyed and clean up
	[
		SD_OP_BLOCK_INSERT,
		"game_event_battle_end",
		D_SEARCH_FROM_TOP | D_SEARCH_LINENUMBER | D_INSERT_BEFORE,

		0, 0,

		[
			(try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
				(troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
				(gt, ":party", 0),
				(neg|party_is_active, ":party"),

				(str_store_troop_name, s0, ":chest"),
				(display_message, "str_pcamp_s0_destroyed", 0xFFFF2222),

				(try_begin),
					(eq, "$auto_enter_town", ":party"),
					(assign, "$auto_enter_town", 0),
				(try_end),

				(troop_get_slot, ":commander", ":chest", slot_pcamp_chest_commander),
				(call_script, "script_cleanup_player_camp_slot", ":chest"),
				(call_script, "script_cleanup_player_camp_commander", ":party", ":commander"),
			(try_end),
		]
	],
	# Compute wage of troops in camps
	[
		SD_OP_BLOCK_INSERT,
		"calculate_player_faction_wage",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(this_or_next|eq, ":party_no", "p_main_party"), 0,

		[
			(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_player_camp),
		]
	],
	# Correctly report companion's occupation in notes
	[
		SD_OP_BLOCK_INSERT,
		"game_get_troop_note",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		# (call_script, "script_companion_get_mission_string", ":companion"), 0,
		(str_store_string, s5, "str_in_your_party"), 0,

		[
			(else_try),
				(troop_get_slot, ":party", ":companion", slot_troop_leaded_party),
				(party_is_active, ":party"),
				(party_slot_eq, ":party", slot_party_type, spt_player_camp),
				(party_get_slot, ":camp_chest", ":party", slot_pcamp_camp_chest),
				(troop_get_slot, ":camp_center", ":camp_chest", slot_pcamp_chest_center),
				(str_store_party_name, s5, ":camp_center"),
				(str_store_string, s0, "str_pcamp_is_commanding_near_s5"),
		]
	],
	# Camps join player's battles that are right on top of them
	[
		SD_OP_BLOCK_INSERT,
		"let_nearby_parties_join_current_battle",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,

		(eq, ":besiege_mode", 0), 0,

		[
				(party_slot_eq, ":party_no", slot_party_type, spt_player_camp),
				(eq, ":besiege_mode", 0),
				(eq, ":dont_add_friends_other_than_accompanying", 0),
				(lt, ":distance", 1),

				(party_quick_attach_to_current_battle, ":party_no", 0),
				(str_store_party_name, s1, ":party_no"),
				(display_message, "str_s1_joined_battle_friend"),
			(else_try),
		]
	],
	# Stop resting at camp if it is attacked
	[
		SD_OP_BLOCK_INSERT,
		"game_event_simulate_battle",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,

		(ge, ":root_defender_party", 0), 0,

		[
				(ge, ":root_defender_party", 1),
				(party_slot_eq, ":root_defender_party", slot_party_type, spt_player_camp),
				(ge, "$g_camp_mode", 1),
				(eq, "$auto_enter_town", ":root_defender_party"),

				(assign, ":trigger_result", 0),

				(assign, "$g_camp_mode", 0),
				(assign, "$g_player_icon_state", pis_normal),
				(rest_for_hours, 0, 0, 0), #stop camping
				(start_encounter, ":root_defender_party"),
			(else_try),
		]
	],
	# Let player command camp troops in battle
	[
		SD_OP_BLOCK_INSERT,
		"agent_reassign_team",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(store_faction_of_party, ":party_faction", ":party_no"), 0,

		[
			# Camps always belong to fac_player_faction, same as p_main_party itself
			(neg|eq, ":party_faction", "fac_player_faction"),
		]
	],
	# Use player's banner for camp troops in battle
	# [
		# SD_OP_BLOCK_INSERT,
		# "agent_troop_get_banner_mesh",
		# D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		# (ge, ":troop_no", 0), 0,  ####### BAH

		# [
        # (try_begin),
          # (agent_get_party_id, ":agent_party", ":agent_no"),
          # (party_get_template_id, ":party_template", ":agent_party"),
		  # (eq, ":party_template", "pt_player_camp"),
		  # (assign, ":banner_troop", "trp_player"),
        # (try_end),
		# ]
	# ],
	# Fix a bug in a native script
	[
		SD_OP_BLOCK_INSERT,
		"party_inflict_attrition",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(lt, ":random", ":chance_of_additional_casualty"), 0,

		[
			# Basically by this point :casualties is the number of already applied
			# _guaranteed_ casualties, and the code tries to randomly add one more
			# to account for the fraction lost by division; but it uses a copy of
			# the same party_add_members line so it just doubles the guaranteed
			# number, which easily can be 0, or possibly greater than 1.
			(assign, ":casualties", 1),
		]
	],
]

new_scripts = [
	("set_player_camp_commander",
		[
			(store_script_param_1, ":camp_party"),
			(store_script_param_2, ":new_commander"),

			# Move the troop to the party; switch limits off just in case
			(party_set_flags, ":camp_party", pf_limit_members, 0),
			(party_add_leader, ":camp_party", ":new_commander"),
			(party_remove_members, "p_main_party", ":new_commander", 1),
			(party_set_flags, ":camp_party", pf_limit_members, 1),

			(party_set_slot, ":camp_party", slot_pcamp_camp_commander, ":new_commander"),
			(troop_set_slot, ":new_commander", slot_troop_leaded_party, ":camp_party"),

			(party_get_slot, ":camp_chest", ":camp_party", slot_pcamp_camp_chest),
			(troop_set_slot, ":camp_chest", slot_pcamp_chest_commander, ":new_commander"),

			(str_store_troop_name, s0, ":new_commander"),
			(str_store_string, s1, "str_pcamp_s0s_camp"),
			(party_set_name, ":camp_party", s1),
			(troop_set_name, ":camp_chest", s1),
		]),

	("replace_player_camp_commander",
		[
			(store_script_param_1, ":camp_party"),
			(store_script_param_2, ":new_commander"),

			# remove the old commander
			(party_get_slot, ":old_commander", ":camp_party", slot_pcamp_camp_commander),
			(party_remove_members, ":camp_party", ":old_commander", 1),
			(troop_set_slot, ":old_commander", slot_troop_leaded_party, -1),
			# add the new commander
			(call_script, "script_set_player_camp_commander", ":camp_party", ":new_commander"),
			# return the old commander to party; this is a pure swap so no limits allowed
			(party_set_flags, "p_main_party", pf_limit_members, 0),
			(party_add_members, "p_main_party", ":old_commander", 1),
			(party_set_flags, "p_main_party", pf_limit_members, 1),
		]),

	("cleanup_player_camp_slot",
		[
			(store_script_param_1, ":chest"),

			(troop_set_slot, ":chest", slot_pcamp_chest_party, 0),
			(troop_set_slot, ":chest", slot_pcamp_chest_commander, 0),
			(troop_set_slot, ":chest", slot_pcamp_chest_sell_prisoners, 0),
			(troop_clear_inventory, ":chest"),
			(store_troop_gold, ":gold", ":chest"),
			(troop_remove_gold, ":chest", ":gold"),
		]),

	("cleanup_player_camp_commander",
		[
			(store_script_param_1, ":camp_party"),
			(store_script_param_2, ":commander"),

			# remove link to party
			(try_begin),
				(troop_slot_eq, ":commander", slot_troop_leaded_party, ":camp_party"),
				(troop_set_slot, ":commander", slot_troop_leaded_party, -1),
			(try_end),

			# if companion, ensure returning to party or properly scatter
			(try_begin),
				(troop_slot_eq, ":commander",  slot_troop_occupation, slto_player_companion),

				(try_begin),
					(this_or_next|main_party_has_troop, ":commander"),
					(troop_slot_ge, ":commander", slot_troop_current_mission, 1),
					# nothing to do if in party or on mission
				(else_try),
					(troop_slot_ge, ":commander", slot_troop_prisoner_of_party, 1),

					(troop_set_slot, ":commander", slot_troop_playerparty_history, pp_history_scattered),
					(troop_set_slot, ":commander", slot_troop_turned_down_twice, 0),
					(troop_set_slot, ":commander", slot_troop_occupation, 0),
				(else_try),
					(troop_set_slot, ":commander", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					(troop_set_slot, ":commander", slot_troop_days_on_mission, 2),
				(try_end),
			(try_end),
		]),

	("disband_player_camp",
		[
			(store_script_param_1, ":camp_party"),

			(party_get_slot, ":old_commander", ":camp_party", slot_pcamp_camp_commander),
			(call_script, "script_cleanup_player_camp_commander", ":camp_party", ":old_commander"),

			(party_get_slot, ":chest", ":camp_party", slot_pcamp_camp_chest),
			(call_script, "script_cleanup_player_camp_slot", ":chest"),

			(remove_party, ":camp_party"),
		]),

	("add_party_until_capacity",
		[
			(store_script_param_1, ":target_party"), #Target Party_id
			(store_script_param_2, ":source_party"), #Source Party_id

			# party_add_members is supposed to check capacity, but seems to be mildly
			# unreliable and may overshoot on the last partially fitting stack
			(party_get_free_companions_capacity, ":capacity", ":target_party"),
			(party_get_num_companion_stacks, ":num_stacks",":source_party"),
			(try_for_range, ":stack_no", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
				(this_or_next|neg|troop_is_hero, ":stack_troop"),
				(eq, "$g_move_heroes", 1),
				(party_stack_get_size, ":stack_size",":source_party",":stack_no"),
				(party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
				# take healthy first
				(store_sub, ":healthy", ":stack_size", ":num_wounded"),
				(val_min, ":stack_size", ":capacity"),
				(val_min, ":healthy", ":capacity"),
				(store_sub, ":num_wounded", ":stack_size", ":healthy"),
				(party_add_members, ":target_party", ":stack_troop", ":stack_size"),
				(party_wound_members, ":target_party", ":stack_troop", ":num_wounded"),
				(val_sub, ":capacity", ":stack_size"),
			(try_end),

			# ditto for prisoners
			(party_get_free_prisoners_capacity, ":capacity", ":target_party"),
			(party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
			(try_for_range, ":stack_no", 0, ":num_stacks"),
				(party_prisoner_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
				(this_or_next|neg|troop_is_hero, ":stack_troop"),
				(eq, "$g_move_heroes", 1),
				(party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
				(val_min, ":stack_size", ":capacity"),
				(party_add_prisoners, ":target_party", ":stack_troop", ":stack_size"),
				(val_sub, ":capacity", ":stack_size"),
			(try_end),
		]),

	("calc_player_camp_bandit_attraction",
		[
			(store_script_param_1, ":camp_party"),

			(party_get_slot, ":chest", ":camp_party", slot_pcamp_camp_chest),
			(store_troop_gold, ":total_value", ":chest"),

			(assign, ":item_count", 0),
			(assign, ":raw_value", 0),

			(troop_get_inventory_capacity, ":inv_size", ":chest"),
			(try_for_range, ":i_slot", 0, ":inv_size"),
				(troop_get_inventory_slot, ":item_id", ":chest", ":i_slot"),
				(ge, ":item_id", 0),
				(store_item_value, ":item_value", ":item_id"),
				# Approximate modifier value
				(troop_get_inventory_slot_modifier, ":mod", ":chest", ":i_slot"),
				(try_begin),
					(eq, ":mod", imod_plain),
				(else_try),
					(eq, ":mod", imod_rotten),
					(assign, ":item_value", 0),
				(else_try),
					(this_or_next|eq, ":mod", imod_cracked),
					(this_or_next|eq, ":mod", imod_rusty),
					(this_or_next|eq, ":mod", imod_tattered),
					(this_or_next|eq, ":mod", imod_lame),
					(this_or_next|eq, ":mod", imod_swaybacked),
					(this_or_next|eq, ":mod", imod_rough),
					(eq, ":mod", imod_smelling),
					(val_div, ":item_value", 2),
				(else_try),
					(this_or_next|eq, ":mod", imod_bent),
					(this_or_next|eq, ":mod", imod_chipped),
					(this_or_next|eq, ":mod", imod_battered),
					(this_or_next|eq, ":mod", imod_poor),
					(this_or_next|eq, ":mod", imod_crude),
					(this_or_next|eq, ":mod", imod_old),
					(eq, ":mod", imod_ragged),
					(val_mul, ":item_value", 3),
					(val_div, ":item_value", 4),
				(else_try),
					(this_or_next|eq, ":mod", imod_fine),
					(this_or_next|eq, ":mod", imod_well_made),
					(this_or_next|eq, ":mod", imod_sharp),
					(this_or_next|eq, ":mod", imod_heavy),
					(this_or_next|eq, ":mod", imod_sturdy),
					(this_or_next|eq, ":mod", imod_thick),
					(this_or_next|eq, ":mod", imod_superb),
					(this_or_next|eq, ":mod", imod_timid),
					(this_or_next|eq, ":mod", imod_meek),
					(eq, ":mod", imod_large_bag),
					(val_mul, ":item_value", 2),
				(else_try),
					(this_or_next|eq, ":mod", imod_balanced),
					(this_or_next|eq, ":mod", imod_strong),
					(this_or_next|eq, ":mod", imod_powerful),
					(eq, ":mod", imod_hardened),
					(val_mul, ":item_value", 4),
				(else_try),
					(this_or_next|eq, ":mod", imod_tempered),
					(this_or_next|eq, ":mod", imod_deadly),
					(this_or_next|eq, ":mod", imod_reinforced),
					(eq, ":mod", imod_spirited),
					(val_mul, ":item_value", 7),
				(else_try),
					(eq, ":mod", imod_lordly),
					(val_mul, ":item_value", 11),
				(else_try),
					(this_or_next|eq, ":mod", imod_exquisite),
					(eq, ":mod", imod_champion),
					(val_mul, ":item_value", 14),
				(else_try),
					(eq, ":mod", imod_masterwork),
					(val_mul, ":item_value", 17),
				(try_end),
				# Sum up values
				(val_add, ":item_count", 1),
				(val_add, ":raw_value", ":item_value"),
				(try_begin),
					(neg|is_between, ":item_id", trade_goods_begin, trade_goods_end),
					(val_div, ":item_value", 5),
				(try_end),
				(val_add, ":total_value", ":item_value"),
			(try_end),

			(troop_set_slot, ":chest", slot_pcamp_chest_items, ":item_count"),
			(troop_set_slot, ":chest", slot_pcamp_chest_value, ":raw_value"),

			(store_div, ":bandit_attraction", ":total_value", (10000/100)), #10000 gold = excellent_target
			(val_clamp, ":bandit_attraction", 0, 100),
			(party_set_bandit_attraction, ":camp_party", ":bandit_attraction"),

			(assign, reg0, ":item_count"),
			(assign, reg1, ":raw_value"),
		]),

	("set_pcamp_banner_from_troop",
		[
			(store_script_param_1, ":party_no"),
			(store_script_param_2, ":troop_no"),

			(troop_get_slot, ":cur_banner", ":troop_no", slot_troop_banner_scene_prop),
			(try_begin),
				(gt, ":cur_banner", 0),
				(val_sub, ":cur_banner", banner_scene_props_begin),
				(val_add, ":cur_banner", banner_map_icons_begin),
				(party_set_banner_icon, ":party_no", ":cur_banner"),
			(try_end),
		]),

	("find_closest_player_camp",
		[
			(store_script_param_1, ":party_no"),

			(assign, ":min_distance", 999999),
			(assign, ":best_camp", -1),

			(try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
				(troop_get_slot, ":camp", ":chest", slot_pcamp_chest_party),
				(gt, ":camp", 0),
				(party_is_active, ":camp"),

				(store_distance_to_party_from_party, ":distance", ":party_no", ":camp"),
				(try_begin),
					(lt, ":distance", ":min_distance"),
					(assign, ":min_distance", ":distance"),
					(assign, ":best_camp", ":camp"),
				(try_end),
			(try_end),

			(assign, reg0, ":best_camp"),
			(assign, reg1, ":min_distance"),
		]),

	("find_closest_town",
		[
			(store_script_param_1, ":party_no"),
			(assign, reg0, -1),
			(assign, reg1, 9999999),
			(try_for_range, ":town_no", towns_begin, towns_end),
				(store_distance_to_party_from_party, ":distance", ":party_no", ":town_no"),
				(lt, ":distance", reg1),
				(assign, reg0, ":town_no"),
				(assign, reg1, ":distance"),
			(try_end),
		]),

	("pcamp_ransom_prisoners",
		[
			(assign, ":old_tt", "$g_talk_troop"),

			(try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
				(troop_slot_eq, ":chest", slot_pcamp_chest_sell_prisoners, 1),

				(troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
				(gt, ":party", 0),
				(party_is_active, ":party"),

				# requires broker in city
				(troop_get_slot, ":city", ":chest", slot_pcamp_chest_city),
				(is_between, ":city", towns_begin, towns_end),
				(party_get_slot, "$g_talk_troop", ":city", slot_center_ransom_broker),
				(gt, "$g_talk_troop", 0),

				# can't sell in enemy cities
				(store_faction_of_party, ":city_faction", ":city"),
				(store_relation, ":faction_rel", ":city_faction", "fac_player_faction"),
				(ge, ":faction_rel", 0),

				(assign, ":total", 0),

				(party_get_num_prisoner_stacks, ":num_stacks", ":party"),
				(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":party",":stack_no"),
					(neg|troop_is_hero, ":stack_troop"),
					(party_prisoner_stack_get_size, ":stack_size",":party",":stack_no"),
					(call_script, "script_game_get_prisoner_price", ":stack_troop"),
					(store_mul, ":price", ":stack_size", reg0),
					(val_add, ":total", ":price"),
					(party_remove_prisoners, ":party", ":stack_troop", ":stack_size"),

					(try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg0, ":price"),
						(assign, reg1, ":stack_size"),
						(str_store_troop_name, s0, ":chest"),
						(str_store_troop_name, s1, ":stack_troop"),
						(display_message, "@{!}DEBUG: {s0} sold {reg1} {s1} for {reg0}"),
					(try_end),
				(try_end),

				(try_begin),
					(gt, ":total", 0),
					(troop_add_gold, ":chest", ":total"),
					(call_script, "script_calc_player_camp_bandit_attraction", ":party"),
				(try_end),
			(try_end),

			(assign, "$g_talk_troop", ":old_tt"),
		]),
]

x = [
	# Stop camps running away from bandits like cowards - if they still do it?..
	("game_get_party_speed_multiplier",
		[
			(store_script_param_1, ":party_no"),
			(assign, ":result", 100),
			(try_begin),
				(party_slot_eq, ":party_no", slot_party_type, spt_player_camp),
				(assign, ":result", 0),
			(try_end),
			(set_trigger_result, ":result"),
		]),
]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "scripts"

        #swy--append the rest of scripts at the end
        orig_scripts = var_set[var_name_1]
        orig_scripts.extend(new_scripts)

        process_script_directives(orig_scripts, script_patches)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)