from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

parties = [
	("player_camp","Camp",icon_camp|pf_always_visible|pf_limit_members,0,fac_player_faction,courage_15,[]),
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