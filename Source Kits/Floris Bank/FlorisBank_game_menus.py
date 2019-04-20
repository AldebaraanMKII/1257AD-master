from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *
# Manualy add these to module_game_menus search for "town"
# add the lines in `bank_menu` before "walled_center_manage"
game_menus = [
########################################################################################################################
#  FLORIS BANK OVERHAUL START																							   #
########################################################################################################################

########################################################################################################################
#  FLORIS BANK OVERHAUL END																							       #
########################################################################################################################
]

bank_menu = [
########################################################################################################################
#  FLORIS BANK OVERHAUL START																							   #
########################################################################################################################
	#	Floris Bank Overhaul	//	Original Idea by Lazeras
	("town_bank",
       [(party_slot_eq, "$current_town", slot_party_type, spt_town)],
       "Visit the landlords and moneylenders.",
       [	
			(assign, reg10, 0),
			(start_presentation, "prsnt_bank"),
        ]),
########################################################################################################################
#  FLORIS BANK OVERHAUL END																							       #
########################################################################################################################
]

bank_menu_village = [
########################################################################################################################
#  FLORIS BANK OVERHAUL START																							   #
########################################################################################################################
	#	Floris Bank Overhaul	//	Original Idea by Lazeras
	("village_bank",
       [(party_slot_eq, "$current_town", slot_party_type, spt_village)],
       "Visit the landlords.",
       [	
			(assign, reg10, 0),
			(start_presentation, "prsnt_bank_village"),
        ]),
########################################################################################################################
#  FLORIS BANK OVERHAUL END																							       #
########################################################################################################################
]

bank_reports = [
########################################################################################################################
#  FLORIS BANK OVERHAUL START																							   #
########################################################################################################################
	#	Floris Bank Overhaul	//	Original Idea by Lazeras
	("bank_reports",
       [],
       "See bank report.",
       [	
         (start_presentation, "prsnt_bank_quickview"),
       ]),
########################################################################################################################
#  FLORIS BANK OVERHAUL END																							       #
########################################################################################################################
]

from util_common import *
from util_wrappers import *

def modmerge_game_menus(orig_game_menus, check_duplicates = False):
	if( not check_duplicates ):
		orig_game_menus.extend(game_menus) # Use this only if there are no replacements (i.e. no duplicated item names)
	else:
	# Use the following loop to replace existing entries with same id
		for i in range (0,len(game_menus)-1):
			find_index = find_object(orig_game_menus, game_menus[i][0]); # find_object is from header_common.py
			if( find_index == -1 ):
				orig_game_menus.append(game_menus[i])
			else:
				orig_game_menus[find_index] = game_menus[i]
	
	# splice this into "town" menu to call the center management hub.
	find_i = list_find_first_match_i( orig_game_menus, "town" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "walled_center_manage")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, bank_menu)	
	
	# splice this into "village" menu to call the center management hub.
	find_i = list_find_first_match_i( orig_game_menus, "village" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "village_buy_food")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, bank_menu_village)	
	
	# add a option to see the bank report presentation through the report menu
	find_i = list_find_first_match_i( orig_game_menus, "reports" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "view_morale_report")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, bank_reports)	

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)