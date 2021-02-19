from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

from util_wrappers import *
from util_scripts import *

import sys

simple_triggers = [
################################################  
(24, ######## Once a day for each for the permanent camp party
[ 
 (try_begin),
   (gt, "$g_permanent_camp_party", 0),
   (try_begin),
     (party_is_active, "$g_permanent_camp_party"),
     (call_script, "script_party_daily_training", "$g_permanent_camp_party"),
   (try_end),
 (try_end),
]),
################################################
]




# Patches in second list are applied to first trigger that contains all operations from first list:

patches = [
	# Let lords escape from camps
	# ([
		# (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "$g_randomly_make_prisoner_heroes_escape_from_party_cur_center", ":chance"),
	 # ],[
		# [
			# SD_OP_BLOCK_INSERT, "",
			# D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_AFTER,
			# 0, 0,
			# [
				# (try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
					# (troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
					# (gt, ":party", 0),
					# (party_is_active, ":party"),
					# (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":party", pcamp_lord_escape_chance),
				# (try_end),
			# ]
		# ],
	 # ]),
	# Make troops desert from camps if unpaid
	# ([
		# (party_get_morale, ":main_party_morale", "p_main_party"),
		# (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
	 # ],[
		# [
			# SD_OP_BLOCK_INSERT, "",
			# D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,

			# (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"), 0,

			# [
					# (try_end),
				# (try_end),
				# (try_begin),
					# (store_div, ":desert_prob", "$g_player_party_morale_modifier_debt", pcamp_desertion_divisor),
					# (gt, ":desert_prob", 0),

					# (try_for_range, ":chest", pcamp_chests_begin, pcamp_chests_end),
						# (troop_get_slot, ":party", ":chest", slot_pcamp_chest_party),
						# (gt, ":party", 0),
						# (party_is_active, ":party"),
						# (call_script, "script_party_inflict_attrition", ":party", ":desert_prob", 1),
						# (party_get_num_companions, ":num_deserters_from_camp", "p_temp_casualties"),
						# (try_begin),
							# (gt, ":num_deserters_from_camp", 0),
							# (str_store_party_name, s3, ":party"),
							# (str_store_string, s2, "str_pcamp_soldiers_from_s3"),
							# (assign, reg0, ":num_deserters_from_camp"),
							# (try_begin),
								# (ge, ":num_deserters_total", 1),
								# (str_store_string, s1, "str_s1_reg0_s2"),
							# (else_try),
								# (str_store_string, s3, s1),
								# (str_store_string, s1, "str_s3_reg0_s2"),
							# (try_end),
							# (val_add, ":num_deserters_total", ":num_deserters_from_camp"),
						# (try_end),
				#######   (try_end), <- from code already there
				#########(try_end),
			# ]
		# ],
	 # ]),
	# Auto-ransom prisoners every 6 hours
	# ([
		# (assign, ":resting_at_manor_or_walled_center", 0),
		# (assign, "$g_half_payment_checkpoint", 0),
	 # ],[
		# [
			# SD_OP_BLOCK_INSERT, "",
			# D_SEARCH_FROM_TOP | D_SEARCH_LINENUMBER | D_INSERT_BEFORE,
			# 0, 0,
			# [
				# (call_script, "script_pcamp_ransom_prisoners"),
			# ]
		# ],
	 # ]),
]

new_triggers = [
]

def apply_patches(orig_triggers, patches):
    for patch in patches:
        found = False
        for trigger in orig_triggers:
            matches = True
            for restriction in patch[0]:
                if restriction not in trigger[1]:
                    matches = False
                    break
            if matches:
                found = True
                tmp = [("", trigger[1])]
                process_script_directives(tmp, patch[1])
                #print_script(tmp, "")
                break
        if not found:
            print "Could not find simple trigger: ", patch[0]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "simple_triggers"

        #swy--append the rest of scripts at the end
        orig_triggers = var_set[var_name_1]

        try:
          apply_patches(orig_triggers, patches)

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise

        orig_triggers.extend(new_triggers)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)
