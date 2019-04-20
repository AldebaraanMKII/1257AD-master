
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1143 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from header_operations import *
from header_common import *
from module_constants import *

from util_wrappers import *
from util_common import list_find_first_match_i
def modmerge_scripts(orig_scripts):
    #BUG FIXES--Errors in Coding:
	#remove if....: if you don't want failures to be silent
	try:	
		#Lords respawning when their faction is defeated fix (revert 1.142/3 changes to the state of all prior versions of M&B/Warband)
		find_i = list_find_first_match_i(orig_scripts, "cf_select_random_walled_center_with_faction_and_owner_priority_no_siege")
		opblock = ScriptWrapper(orig_scripts[find_i]).GetOpBlock()
		pos = opblock.FindLineMatching((le, ":no_centers", 0))
		if pos != -1: opblock.InsertBefore(pos-1, [(gt, ":no_centers", 0),]) #pos-1 to skip above the (try_begin)

		#Errors in dialogs with lords (dialog asks for a town name and the lord says a troop name)
		find_i = list_find_first_match_i(orig_scripts, "get_relevant_comment_for_log_entry")
		opblock = ScriptWrapper(orig_scripts[find_i]).GetOpBlock()	
		pos = opblock.FindLineMatching((eq, ":entry_type", logent_troop_feels_cheated_by_troop_over_land))
		if opblock.GetLineContent(pos+2) == (str_store_troop_name, s51, ":center_object"):
			opblock.SetLineContent(pos+2, (str_store_party_name, s51, ":center_object"))

		#Error in re-setting old marshall
		find_i = list_find_first_match_i(orig_scripts, "appoint_faction_marshall")
		opblock = ScriptWrapper(orig_scripts[find_i]).GetOpBlock()		
		pos = opblock.FindLineMatching((faction_get_slot, ":old_marshall", ":faction_no", slot_faction_marshall), 1) #skip first find
		if pos != -1: opblock.RemoveAt(pos)

		#Error in creating screening parties
		find_i = list_find_first_match_i(orig_scripts, "decide_faction_ai")
		opblock = ScriptWrapper(orig_scripts[find_i]).GetOpBlock()	
		pos = opblock.FindLineMatching((troop_get_slot, ":screening_party", ":screen_leader_faction", slot_troop_leaded_party))
		if pos != -1: opblock.SetLineContent(pos, (troop_get_slot, ":screening_party", ":screen_leader", slot_troop_leaded_party))
		
		#Error in getting Marshall's controversy rating for decisions about joining campaign/following
		find_i = list_find_first_match_i(orig_scripts, "npc_decision_checklist_troop_follow_or_not")
		opblock = ScriptWrapper(orig_scripts[find_i]).GetOpBlock()	
		pos = opblock.FindLineMatching((troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall),1) #skip first, go to second
		if pos != -1: opblock.RemoveAt(pos)
		pos = opblock.FindLineMatching((troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall)) #address first finding
		if pos != -1: opblock.SetLineContent(pos, (troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_troop_controversy))
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise

	#CAMPAIGN AI 'FIXES'/TWEAKS--Improvements to Logic--by motomataru:
	##MIGHT add these later