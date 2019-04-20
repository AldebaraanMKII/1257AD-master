from header_common import *
from header_operations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

# Manualy all lines under the `scripts` into the bottom of the module_scripts at the bottom of the file
scripts = [
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################


########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################
] # scripts


from util_wrappers import *
from util_scripts import *

# Manualy add these to module_scripts search for "game_start"
# add the lines in at the start of the script block
scripts_directives = [
	[SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (troop_set_note_available, "trp_player", 1),0,
	[
########################################################################################################################
#  KAOS BANKING KIT START																							   #
########################################################################################################################

	  #Duh Town Population for Land required // Linked to bank system
	  
	  (try_for_range, ":town_no", towns_begin, towns_end),
		# (this_or_next|eq,":town_no","p_town_1"),
		# (this_or_next|eq,":town_no","p_town_5"),
		# (this_or_next|eq,":town_no","p_town_6"),
		# (this_or_next|eq,":town_no","p_town_8"),
		# (this_or_next|eq,":town_no","p_town_10"),
		# (eq,"$current_town","p_town_19"),
		# (store_random_in_range, ":amount", 18000, 22000),
		# (party_set_slot, ":town_no", slot_center_population, ":amount"),
		# (val_div, ":amount", 200),
		# (party_set_slot, ":town_no", slot_town_acres, ":amount"),
	  # (else_try),
		(store_random_in_range, ":amount", 15000, 30000),
		(party_set_slot, ":town_no", slot_center_population, ":amount"),
		(val_div, ":amount", 200),
		(party_set_slot, ":town_no", slot_town_acres, ":amount"),		
	  (try_end),
	  
	  (try_for_range, ":town_no", villages_begin, villages_end),
		(store_random_in_range, ":amount", 800, 2000),
		(party_set_slot, ":town_no", slot_center_population, ":amount"),
		(val_div, ":amount", 200),
		(party_set_slot, ":town_no", slot_town_acres, ":amount"),
	  (try_end),
	  
	  #Duh Over
########################################################################################################################
#  KAOS BANKING KIT END																							       #
########################################################################################################################	
	], 15],

]


# the following is a generic function expected by modmerger
# If not defined, it will only do the basic merging of adding the scripts in "scripts" to the orignal "scripts" in module_scripts.py
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1] # this is the ORIGINAL scripts from module_scripts.py

        # START do your own stuff to do merging

        # modify existing scripts according to scripts_directives  above
        process_script_directives(orig_scripts, scripts_directives )

        add_objects(orig_scripts, scripts) # add new scripts, by default, scripts with same name will be replaced

        # END do your own stuff

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
	