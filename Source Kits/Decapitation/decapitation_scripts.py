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
] # scripts


from util_wrappers import *
from util_scripts import *

# Manualy add these to module_scripts search for "game_start"
# add the lines in at the start of the script block
scripts_directives = [
	[SD_OP_BLOCK_INSERT, "game_start", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER, (call_script, "script_update_party_creation_random_limits"),0,
	[
    (assign, "$g_decap_enabled", 1),
    (assign, "$g_decap_minimum_damage", 30),
    (assign, "$g_decap_negative_health", 10),
    (assign, "$g_decap_chance", 20),
    (assign, "$g_decap_psys_blood_decapitation", 40),
    (assign, "$g_decap_psys_game_blood", 10),
    (assign, "$g_decap_psys_game_blood_2", 10),
    (assign, "$g_dismemberment_enabled", 1),
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
	