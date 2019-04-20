#=#######################################
# Lumos: This file contains all the parties for the Outposts kit.
#        Place 'em in your module_parties.
#-#######################################

from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

no_menu = 0

parties = [
#-## Outposts begin
  ("outpost_1","Outpost",icon_outpost|pf_disabled|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[]),
  ("outpost_2","Outpost",icon_outpost|pf_disabled|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(1, -1),[]),
  ("fort","Fort",icon_fort_a|pf_disabled|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(1, 1),[]),
#-## Outposts end
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "parties"
        orig_parties = var_set[var_name_1]
        orig_parties.extend(parties) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)