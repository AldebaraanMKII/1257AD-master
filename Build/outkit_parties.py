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