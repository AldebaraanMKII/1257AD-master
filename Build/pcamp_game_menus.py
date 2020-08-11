
from header_game_menus import *
from module_constants import *
from header_items import *
from header_parties import *
from header_music import *

from ID_party_templates import *

from util_wrappers import *
from util_scripts import *

init_block_patches = [
	# Report occupation in reports, also preventing the code from activating a return mission
	[
		SD_OP_BLOCK_INSERT,
		"companion_report",
		D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

		(str_store_string, s2, "str_s2_s3"), 0,

		[
			# (else_try),
		  (try_begin),
			(troop_get_slot, ":party", ":companion", slot_troop_leaded_party),
			(party_is_active, ":party"),
			(party_slot_eq, ":party", slot_party_type, spt_player_camp),
			(party_get_slot, ":camp_chest", ":party", slot_pcamp_camp_chest),
			(troop_get_slot, ":camp_center", ":camp_chest", slot_pcamp_chest_center),
			(str_store_party_name, s9, ":camp_center"),
			(str_store_string, s8, "str_pcamp_acting_as_commander"),
			(str_store_string, s5, "str_pcamp_near_s9"),
          (try_end),
		]
	],
	# Fix the original camp menu to redirect to the player camp when appropriate
	[
		SD_OP_BLOCK_INSERT,
		"camp",
		D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_AFTER,

		0, 0,

		[
			(try_begin),
				# We get here when original camp submenus return back to top level
				(eq, "$g_encountered_party_template", "pt_player_camp"),
				(jump_to_menu, "mnu_player_camp"),
			(else_try),
				# If Camp is pressed just near a camp, switch to it
				(call_script, "script_find_closest_player_camp", "p_main_party"),
				(gt, reg0, 0), # camp party
				(eq, reg1, 0), # distance
				(assign, "$auto_enter_town", reg0),
				(change_screen_return),
			(try_end),
		]
	],
]

xx = [
	# patches for two bad calls
	[
		SD_OP_BLOCK_REPLACE,
		"party_size_report",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,

		(call_script, "script_game_get_party_companion_limit"), 0,

		[
			(call_script, "script_game_get_party_companion_limit", "p_main_party")
		]
	],
	[
		SD_OP_BLOCK_REPLACE,
		"reports",
		D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,

		(call_script, "script_game_get_party_companion_limit"), 0,

		[
			(call_script, "script_game_get_party_companion_limit", "p_main_party")
		]
	],
]

player_camp_menu = [
	("action_create_pcamp",
		[ (neg|eq, "$g_encountered_party_template", "pt_player_camp") ],
		"Create a permanent camp.",
		[(jump_to_menu, "mnu_create_pcamp")]),
]

game_menus = [
	 ("create_pcamp", 0,
		"{s5}", "none",
		[
			(assign, ":free_companion", -1),
			(assign, "$g_talk_troop_party", -1),
			(assign, ":num_free_camps", 0),

			# Find a free camp party slot
			(try_for_range_backwards, ":cur_chest", pcamp_chests_begin, pcamp_chests_end),
				(troop_slot_eq, ":cur_chest", slot_pcamp_chest_party, 0),
				(val_add, ":num_free_camps", 1),
				(assign, "$g_talk_troop_party", ":cur_chest"),
			(try_end),

			# Check skill
			(store_sub, ":num_camp_slots", pcamp_chests_end, pcamp_chests_begin),
			(store_sub, ":num_current_camps", ":num_camp_slots", ":num_free_camps"),
			(store_skill_level, ":skill", pcamp_build_skill, "trp_player"),
			(val_sub, ":skill", pcamp_build_skill_threshold-1),
			(val_sub, ":skill", ":num_current_camps"),
			(val_max, ":skill", 0),
			(val_min, ":num_free_camps", ":skill"),

			# Find a companion to command it
			(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
				(troop_is_hero, ":stack_troop"),
				(is_between, ":stack_troop", companions_begin, companions_end),
				(troop_slot_eq, ":stack_troop", slot_troop_prisoner_of_party, -1),
				(assign, ":free_companion", ":stack_troop"),
			(try_end),

			# Find closest center
			(call_script, "script_get_closest_center", "p_main_party"),
			(assign, "$g_talk_troop_faction", reg0),
			(store_distance_to_party_from_party, ":center_distance", "p_main_party", reg0),

			# Check conditions and prepare the message
			(assign, reg5, ":num_free_camps"),
			(store_troop_gold, reg6, "trp_player"),
			(assign, reg7, pcamp_build_cost),
			(str_store_party_name, s0, "$g_talk_troop_faction"),
			(assign, "$g_talk_troop", -1),
			(try_begin),
				(le, "$g_talk_troop_party", 0),
				(str_store_string, s5, "str_pcamp_too_many_camps"),
			(else_try),
				(le, ":free_companion", 0),
				(str_store_string, s5, "str_pcamp_no_free_companions"),
			(else_try),
				(lt, reg6, reg7),
				(str_store_string, s5, "str_pcamp_no_reg7_denars"),
			(else_try),
				(le, ":num_free_camps", 0),
				(str_store_string, s5, "str_pcamp_skill_too_low"),
				(ge, "$cheat_mode", 1),
				(str_store_string, s5, "str_pcamp_s5_cheat_can_do_anyway"),
				(assign, "$g_talk_troop", ":free_companion"),
			(else_try),
				(gt, ":center_distance", pcamp_max_center_distance),
				(str_store_string, s5, "str_pcamp_too_far_from_s0"),
				(ge, "$cheat_mode", 1),
				(str_store_string, s5, "str_pcamp_s5_cheat_can_do_anyway"),
				(assign, "$g_talk_troop", ":free_companion"),
			(else_try),
				(str_store_string, s5, "str_pcamp_can_start_camp_s0_reg5_reg6_reg7"),
				(assign, "$g_talk_troop", ":free_companion"),
			(try_end),
		],
		[("build_camp",
			[
				(ge, "$g_talk_troop", 0),
				(assign, reg7, pcamp_build_cost),
			],
			"Yes, create a permanent camp. ({reg7} denars)",
			[
				(troop_remove_gold, "trp_player", pcamp_build_cost),

				# Spawn the camp
				(set_spawn_radius, 0),
				(spawn_around_party,"p_main_party", "pt_player_camp"),
				(assign, ":camp_party", reg0),
				(assign, "$g_permanent_camp_party", ":camp_party"), ######### NEW v1.0 - sets the global that allow the camp party daily training
				(party_set_slot, ":camp_party", slot_party_type, spt_player_camp),

				# Set up ai to (hopefully) avoid any weird behavior from it
				(party_set_slot, ":camp_party", slot_party_ai_state, spai_undefined),
				(party_set_ai_behavior, ":camp_party", ai_bhvr_hold),
				(party_set_ai_initiative, ":camp_party", 0),
				(party_set_helpfulness, ":camp_party", 0),
				(party_set_aggressiveness, ":camp_party", 0),
				(party_set_courage, ":camp_party", 100), # what is the real max value??
				(party_set_bandit_attraction, ":camp_party", 0),

				# Register links to chest
				(assign, ":camp_chest", "$g_talk_troop_party"),
				(call_script, "script_cleanup_player_camp_slot", ":camp_chest"),
				(troop_set_slot, ":camp_chest", slot_pcamp_chest_party, ":camp_party"),
				(troop_set_slot, ":camp_chest", slot_pcamp_chest_center, "$g_talk_troop_faction"),
				(party_set_slot, ":camp_party", slot_pcamp_camp_chest, ":camp_chest"),

				(call_script, "script_find_closest_town", ":camp_party"),
				(troop_set_slot, ":camp_chest", slot_pcamp_chest_city, reg0),

				# Set the commander; the party should always remain fac_player_faction
				(call_script, "script_set_player_camp_commander", ":camp_party", "$g_talk_troop"),

				# Switch the encounter target
				(assign, "$auto_enter_town", ":camp_party"),
				(change_screen_return),
			]),
		 ("camp_cancel", [], "Return to your regular camp.",
		    [(jump_to_menu, "mnu_camp")])
		]
	),

	("player_camp",mnf_scale_picture,
		"You have arrived at your camp. It is commanded by {s3}. What do you want to do?", "none",
		[
			(assign, "$g_camp_mode", 0),
			(assign, "$g_player_icon_state", pis_normal),
			(set_background_mesh, "mesh_pic_camp"),
			(try_begin),
				(eq, "$g_leave_encounter", 1),
				(assign, "$g_encountered_party_template", -1),
				(change_screen_return),
			(else_try),
				(party_get_slot, "$g_talk_troop", "$g_encountered_party", slot_pcamp_camp_commander),
				(party_get_slot, ":camp_chest", "$g_encountered_party", slot_pcamp_camp_chest),
				# withdraw cash
				(store_troop_gold, ":gold", ":camp_chest"),
				(troop_remove_gold, ":camp_chest", ":gold"),
				(troop_add_gold, "trp_player", ":gold"),
				# update stuff
				(call_script, "script_calc_player_camp_bandit_attraction", "$g_encountered_party"),
				(call_script, "script_set_pcamp_banner_from_troop", "$g_encountered_party", "trp_player"),
				(str_store_troop_name, s3, "$g_talk_troop"),
				# Automatically enter dialog in some cases
				(try_begin),
					(eq, "$new_encounter", 1),
					(assign, "$new_encounter", 0),
					(assign, "$g_mission_result", 0),
				(try_end),
				(try_begin),
					(this_or_next|eq, "$g_mission_result", 1),
					(party_slot_eq, "$g_encountered_party", slot_pcamp_camp_initialized, 0),
					(assign, "$g_mission_result", 0),
					(party_set_slot, "$g_encountered_party", slot_pcamp_camp_initialized, 1),
					(assign, "$talk_context", tc_party_encounter),
					(call_script, "script_setup_party_meeting", "$g_encountered_party"),
				(try_end),
			(try_end),
		],
		[
			("camp_manage",[],"Manage the camp.",
				[
					(assign, "$talk_context", tc_party_encounter),
					(call_script, "script_setup_party_meeting", "$g_encountered_party"),
				]),

			# Original camp menus
			("camp_action",[],"Take an action.",
				[(jump_to_menu, "mnu_camp_action")]),

			("camp_cheat", [(ge, "$cheat_mode", 1)], "CHEAT MENU!",
				[(jump_to_menu, "mnu_camp_cheat")]),

			# Wait in camp etc
			("camp_wait_here",[],"Wait here for some time.",
				[
					(assign, "$g_camp_mode", 1),
					(assign, "$g_infinite_camping", 0),
					(assign, "$auto_enter_town", "$g_encountered_party"),

					# Ensure position is exactly the same to avoid two partially overlapping icons
					# However it doesn't compensate rotation, so there is still mismatch...
					#(assign, "$g_player_icon_state", pis_camping),
					#(party_relocate_near_party, "p_main_party", "$g_encountered_party", 0),

					(rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable

					(assign, "$g_encountered_party_template", -1),
					(change_screen_return),
				]),

			("resume_travelling",[],"Resume travelling.",
				[
					(assign, "$g_encountered_party_template", -1),
					(change_screen_return),
				]),
		]),
]

from util_wrappers import *
from util_common import *

def apply_init_patches(ops, patches):
    tmp = []
    i = 0
    while (i < len(ops)):
        tmp.append((ops[i][0], ops[i][4]))
        i += 1
    process_script_directives(tmp, patches)

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]

        #swy--insert new menu option in the camp menu as its third option!
        try:
          apply_init_patches(orig_game_menus, init_block_patches)

          find_i = list_find_first_match_i(orig_game_menus, "camp_action")
          GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions().insert(3-1,player_camp_menu[0])

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise

        #swy--additional game menus, inserted at the end!
        orig_game_menus.extend(game_menus)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)