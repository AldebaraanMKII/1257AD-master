#=#######################################
# Lumos: This file contains all the map icons for the Outposts kit.
#        Place them in module_map_icons.
#-#######################################

# ATTENTION: If you have problems with compiling, look at 'outkit_ID_map_icons_addon.py'

from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

map_icons = [
#-## Outposts begin
  ("outpost",mcn_no_shadow,"outpost", 0.22,0),
  ("fort_a",mcn_no_shadow,"map_fort_a", 0.22,0),
#-## Outposts end
]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "map_icons"
        var_set[var_name_1].extend(map_icons) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)