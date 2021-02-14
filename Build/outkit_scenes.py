#=#######################################
# Lumos: This file contains all the scenes for the Outposts kit.
#        Place them in your module_scenes. At the end is good.
#-#######################################

# Version 0.8 note: Only the level two scenes (scn_outpost_*_two_*) for every outpost are new. The level one scenes are still empty.

from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

outposts = [

]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "scenes"
        orig_scenes = var_set[var_name_1]
        orig_scenes.extend(outposts) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)