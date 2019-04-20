#=#######################################
# Lumos: You have to add the given dialogs in your module_dialogs file.
#-#######################################

# About the placement: in the example build, I've placed the dialogs
#  at the end of module_dialogs. You can place it anywhere, but know that
#  if you have other patrol talks, like Diplomacy's, they might override these.
#  Be sure to have these dialogs placed BEFORE any conflicting others.

# There's also a possible bug with the beginning merchant's dialogs,
# if you put these too much to the start of the file.

# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *
from header_parties import *
from ID_troops import *

#-## Outposts begin
# Lumos: Patrol talks. I added some fuctions
dialogs	= [   
  [anyone ,"start",
    [(this_or_next|party_slot_eq, "p_outpost_1", slot_outpost_patrol, "$g_encountered_party"),
	 (this_or_next|party_slot_eq, "p_outpost_2", slot_outpost_patrol, "$g_encountered_party"),
	 (party_slot_eq, "p_fort", slot_outpost_patrol, "$g_encountered_party"),
	 (neq, "$talk_context", tc_merchants_house), # Bugfix
	# Report current activity:
	(party_get_slot, ":patrol_state", "$g_encountered_party", slot_cattle_driven_by_player),
	(try_begin),
		(eq, ":patrol_state", 1),
		(str_store_string, s1, "@We are currently following you."),
	(else_try),
		(eq, ":patrol_state", 0),
		(str_store_string, s1, "@We are currently holding this location."),
	(else_try), # Assume that patrolling is the normal activity
		(str_store_string, s1, "@We are currently patrolling around the area."),
	(try_end),
	],
   "Good day, {sir/madam}. Is there anything we can do for you? {s1}", "outpost_patrol",[]],
   
  [anyone,"outpost_patrol_pretalk", [], "Anything else?", "outpost_patrol",[]],   
   
	# Lumos: Stolen from the cattle herding. :D
  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_cattle_driven_by_player, 1)], "Follow me.", "outpost_patrol_pretalk",[ 
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
	]],
  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_cattle_driven_by_player, 0)], "Hold this location.", "outpost_patrol_pretalk",[
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
	]], 
  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_cattle_driven_by_player, 2)], "Patrol around this location.", "outpost_patrol_pretalk",[
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 2),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_patrol_location),
		(party_set_ai_object, "$g_encountered_party", "$g_encountered_party"),
	]], 
  [anyone|plyr,"outpost_patrol", [], "I want to give some troops to you.", "outpost_patrol_pretalk",[
        (change_screen_exchange_members, 0),
	]], 
  [anyone|plyr,"outpost_patrol", [], "Continue your activities.", "outpost_patrol_end",[]],
  
  [anyone, "outpost_patrol_end", [(assign, "$g_leave_encounter", 1)], "Aye, {sir/madam}.", "close_window", [(jump_to_menu, "mnu_auto_return")]],
  
  # Fort Captain (should it be a woman called Kelly Chambers? :P )
  [trp_fort_captain ,"start", [], "How may I help you, Commander?", "fort_captain",[]],
  
  [anyone ,"fort_captain_pretalk", [], "Anything else, Commander?", "fort_captain",[]],
  
  [anyone|plyr, "fort_captain", [], "Is there anything I should know?.", "fort_captain_nothing", []],
  
  [anyone|plyr, "fort_captain", [(assign, "$g_leave_encounter", 1)], "That'll be all.", "close_window", [(change_screen_return, 0)]],
  
  [anyone ,"fort_captain_nothing", [], "Nothing right now.", "fort_captain_pretalk",[]],
  
  # Patrol dialogs - not working?
  [trp_fort_walker,"start", [], "Yes {sir/madam}?", "fort_guard_talk",[]],
  [trp_fort_rider,"start", [], "Yes {sir/madam}?", "fort_guard_talk",[]],
  [anyone|plyr,"fort_guard_talk", [], "How goes the watch, soldier?", "fort_guard_talk_2",[]],
  [anyone,"fort_guard_talk_2", [], "All is quiet {sir/madam}. Nothing to report.", "fort_guard_talk_3",[]],
  [anyone|plyr,"fort_guard_talk_3", [], "Good. Keep your eyes open.", "close_window",[]],
#-## Outposts end  
]

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
    
    #swy--add our new dialogs just before the generic fallbacks
		pos = FindDialog_i(orig_dialogs, anyone|plyr, "regular_member_talk")
		OpBlockWrapper(orig_dialogs).InsertAfter(pos, dialogs)
		
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)