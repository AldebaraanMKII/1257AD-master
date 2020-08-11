from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *
from header_parties import *
from ID_troops import *
from ID_party_templates import *

dialogs = [
	# Initiating conversation
	[party_tpl|pt_player_camp|auto_proceed, "start",
		[
			(eq, "$talk_context", tc_party_encounter),
		],
		"{!}", "player_camp_start", []],

	[anyone, "start",
		[
			(is_between, "$g_talk_troop", companions_begin, companions_end),
			(troop_get_slot, ":party", "$g_talk_troop", slot_troop_leaded_party),
			(party_is_active, ":party"),
			(party_slot_eq, ":party", slot_party_type, spt_player_camp),
			(try_begin),
				(eq, "$talk_context", tc_ally_thanks),
				(str_store_string, s0, "str_pcamp_thanks_help"),
			(else_try),
				(assign, reg0, "$talk_context"),
				(str_store_string, s0, "str_pcamp_unexpected_context"),
			(try_end),
		],
		"{s0}", "close_window", []],

	# Main menu
	[anyone, "player_camp_start",
		[
			(troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
			(str_store_string, s5, ":honorific"),
		],
		"Good day, {s5}. What can I do for you?", "player_camp_choice",[]],

	[anyone|plyr, "player_camp_choice", [],
		"Let's review the troop list.", "player_camp_start",
		[
			(change_screen_exchange_members, 0)
		] ],

	[anyone|plyr, "player_camp_choice", [],
		"I want to store a few items here for a while.", "player_camp_items", [] ],

	[anyone, "player_camp_items", [],
		"I'll keep them for you, {s5}, but please be sure to leave enough men to discourage bandits.",
		"player_camp_start",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(change_screen_loot, ":chest")
		] ],

	[anyone|plyr, "player_camp_choice",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(neg|troop_slot_eq, ":chest", slot_pcamp_chest_sell_prisoners, 1),
			(troop_get_slot, ":city", ":chest", slot_pcamp_chest_city),
			(str_store_party_name, s0, ":city"),
		],
		"I want you to ransom all prisoners in {s0} whenever possible.", "player_camp_ransom_on",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(troop_set_slot, ":chest", slot_pcamp_chest_sell_prisoners, 1),
		] ],

	[anyone, "player_camp_ransom_on", [],
		"Very well, I will do that whenever there is a broker in the city.", "player_camp_start", [] ],

	[anyone|plyr, "player_camp_choice",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(troop_slot_eq, ":chest", slot_pcamp_chest_sell_prisoners, 1),
		],
		"I want you to stop ransoming all prisoners on your own.", "player_camp_ransom_off",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(troop_set_slot, ":chest", slot_pcamp_chest_sell_prisoners, 0),
		] ],

	[anyone, "player_camp_ransom_off", [],
		"Very well, I will keep them safe here in the camp.", "player_camp_start", [] ],

	[anyone|plyr, "player_camp_choice",
		[
			(assign, ":num_free", 0),
			(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
				(troop_is_hero, ":stack_troop"),
				(is_between, ":stack_troop", companions_begin, companions_end),
				(val_add, ":num_free", 1),
			(try_end),
			(gt, ":num_free", 0),
		],
		"I wish to appoint a different commander.", "player_camp_replace_cmd", []],

	[anyone|plyr, "player_camp_choice", [],
		"I want to disband the camp.", "player_camp_disband_test_items", []],

	[anyone|plyr, "player_camp_choice", [],
		"That'll be all.", "close_window", []],

	# Replace commander
	[anyone, "player_camp_replace_cmd", [],
		"I see. who is your new choice?", "player_camp_replace_sel", []],

	[anyone|plyr|repeat_for_troops, "player_camp_replace_sel",
		[
			(store_repeat_object, ":troop_no"),
			(is_between, ":troop_no", companions_begin, companions_end),
			(main_party_has_troop, ":troop_no"),
			(troop_slot_eq, ":troop_no", slot_troop_prisoner_of_party, -1),
			(str_store_troop_name, s4, ":troop_no"),
		],
		"{s4}", "player_camp_replace_confirm",
		[
			(store_repeat_object, "$g_emissary_selected"),
		]],

	[anyone|plyr, "player_camp_replace_sel", [],
		"Actually, nevermind.", "player_camp_start", []],

	[anyone, "player_camp_replace_confirm",
		[
			(str_store_troop_name, s4, "$g_emissary_selected"),
		],
		"Very well {s5}, I will transfer command to {s4} at once.", "close_window",
		[
			(call_script, "script_replace_player_camp_commander", "$g_talk_troop_party", "$g_emissary_selected"),
			(assign, "$g_mission_result", 1),
		]],

	# Disband
	[anyone, "player_camp_disband_test_items",
		[
			(call_script, "script_calc_player_camp_bandit_attraction", "$g_talk_troop_party"),
			(gt, reg0, 0),
		],
		"Do you remember that you have {reg0} items worth approximately {reg1} denars stored here?",
		"player_camp_disband_has_items", []],

	[anyone|auto_proceed, "player_camp_disband_test_items", [],
		"{!}", "player_camp_disband_test_join", [] ],

	[anyone|plyr, "player_camp_disband_has_items", [],
		"Let's see what they are.", "player_camp_disband_test_join",
		[
			(party_get_slot, ":chest", "$g_talk_troop_party", slot_pcamp_camp_chest),
			(change_screen_loot, ":chest")
		] ],

	[anyone|plyr, "player_camp_disband_has_items", [],
		"I'm sure there is nothing important.", "player_camp_disband_test_join", [] ],

	[anyone|plyr, "player_camp_disband_has_items", [],
		"I guess it's too early to leave.", "player_camp_start", [] ],

	[anyone, "player_camp_disband_test_join",
		[
			(party_can_join_party,"$g_talk_troop_party","p_main_party")
		],
		"Your party can accomodate all members of the camp, {s5}, so there is no problem disbanding it immediately.",
		"player_camp_disband_full", []],

	[anyone|plyr, "player_camp_disband_full", [],
		"Yes, let's break camp at once.", "player_camp_disband_finish",
		[
			(assign, "$g_move_heroes", 1),
			(call_script, "script_party_add_party", "p_main_party", "$g_talk_troop_party"),
		] ],

	[anyone|plyr, "player_camp_disband_full", [],
		"No, I changed my mind.", "player_camp_start", [] ],

	[anyone, "player_camp_disband_test_join",
		[
			(party_get_free_companions_capacity, ":ccap", "p_main_party"),
			(party_get_free_prisoners_capacity, ":pcap", "p_main_party"),
			(party_get_num_companions, ":cnum", "$g_talk_troop_party"),
			(party_get_num_prisoners, ":pnum", "$g_talk_troop_party"),
			(assign, reg0, ":ccap"),
			(assign, reg2, ":cnum"),
			(try_begin),
				(ge, ":ccap", ":cnum"),
				(assign, ":ccap", -1),
				(str_store_string, s0, "str_pcamp_can_accomodate_all_reg2"),
			(else_try),
				(gt, ":ccap", 0),
				(str_store_string, s0, "str_pcamp_can_accomodate_reg0_of_reg2"),
			(else_try),
				(str_store_string, s0, "str_pcamp_can_accomodate_none_of_reg2"),
			(try_end),
			(assign, reg3, ":pnum"),
			(try_begin),
				(eq, ":pnum", 0),
				(str_store_string, s1, "str_pcamp_no_prisoners"),
			(else_try),
				(ge, ":pcap", ":pnum"),
				(str_store_string, s1, "str_pcamp_can_keep_all_reg3_prisoners"),
			(else_try),
				(gt, ":pcap", 0),
				(assign, reg1, ":pcap"),
				(str_store_string, s1, "str_pcamp_can_keep_reg1_of_reg3_prisoners"),
			(else_try),
				(str_store_string, s1, "str_pcamp_can_keep_none_of_reg3_prisoners"),
			(try_end),
			(assign, "$g_emissary_selected", ":ccap"),
		],
		"{!}{s0} {s1}",
		"player_camp_disband_partial", []],

	[anyone|plyr, "player_camp_disband_partial", [],
		"Let's look over the troop lists one more time.", "player_camp_disband_recheck",
		[
			(change_screen_exchange_members, 0),
		] ],

	[anyone, "player_camp_disband_recheck", [],
		"Let me consider your changes for a while...", "player_camp_disband_test_join", [] ],

	[anyone|plyr, "player_camp_disband_partial",
		[
			(try_begin),
				(eq, "$g_emissary_selected", 0),
				(str_store_string, s0, "str_pcamp_disband_leave"),
			(else_try),
				(eq, "$g_emissary_selected", 1),
				(str_store_string, s0, "str_pcamp_disband_one"),
			(else_try),
				(eq, "$g_emissary_selected", -1),
				(str_store_string, s0, "str_pcamp_disband_max_prisoners"),
			(else_try),
				(assign, reg0, "$g_emissary_selected"),
				(str_store_string, s0, "str_pcamp_disband_top_reg0"),
			(try_end),
		],
		"All right, {s0}.", "player_camp_disband_finish",
		[
			(assign, "$g_move_heroes", 1),
			(assign, "$g_permanent_camp_party", -1), #### NEW v1.0 - camp party global
			(call_script, "script_add_party_until_capacity", "p_main_party", "$g_talk_troop_party"),
		] ],

	[anyone|plyr, "player_camp_disband_partial", [],
		"No, I changed my mind.", "player_camp_start", [] ],

	[anyone, "player_camp_disband_finish", [],
		"Very well, I will relay your orders to the troops immediately.", "close_window",
		[
			(assign, "$g_permanent_camp_party", -1), #### NEW v1.0 - camp party global
			(call_script, "script_disband_player_camp", "$g_talk_troop_party"),
			(assign, "$g_leave_encounter", 1),
		] ],
]

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]

    #swy--add our new dialogs just before the generic fallbacks
		pos = 0
		while (pos < len(orig_dialogs)):
			item = orig_dialogs[pos]
			if (item[0] == anyone|plyr and item[1] == "member_castellan_talk"):
				break;
			pos += 1

		OpBlockWrapper(orig_dialogs).InsertAfter(pos, dialogs)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)