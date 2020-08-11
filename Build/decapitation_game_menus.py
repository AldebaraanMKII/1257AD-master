from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *
# Manualy add these to module_game_menus search for "town"
# add the lines in `bank_menu` before "walled_center_manage"
game_menus = []

camp_menu = [
      ("enhanced_mod_options_7",[], "Decapitation options.",
       [
           (start_presentation, "prsnt_enhanced_mod_options_decap"),
        ]
       ),
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
	find_i = list_find_first_match_i( orig_game_menus, "enhanced_mod_options" )
	menuoptions = GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions()
	find_i = list_find_first_match_i(menuoptions, "enhanced_mod_options_6")		
	OpBlockWrapper(menuoptions).InsertAfter(find_i, camp_menu)	
	
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        modmerge_game_menus(orig_game_menus)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)