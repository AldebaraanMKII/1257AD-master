from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

parties = [  
  # ("manor", "Manor", icon_manor_icon|pf_label_small|pf_is_static|pf_hide_defenders,0, fac_commoners, bandit_personality, [(trp_manor_master, 1, 2)]),
  ("outpost","Outpost",icon_outpost|pf_is_static|pf_always_visible|pf_label_small,0, fac_commoners,ai_bhvr_hold,[]),
  ("fort","Fort",icon_fort_a|pf_is_static|pf_always_visible|pf_label_medium,0, fac_commoners,ai_bhvr_hold,[]),
]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "party_templates"
        orig_parties = var_set[var_name_1]
        orig_parties.extend(parties)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)