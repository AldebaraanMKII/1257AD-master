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
#-## Outposts begin
  ("outpost_one_one_steppe",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002c678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe"),
  ("outpost_one_one_plain",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("outpost_one_one_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c678e240003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_snow"),
  ("outpost_one_one_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000055878e1ec003f0ff0000445800002b7500007d87",
    [],[],"outer_terrain_desert"),
  ("outpost_one_one_steppe_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe_forest"),
  ("outpost_one_one_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc678e248003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_forest"),
  ("outpost_one_one_snow_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000cc678e1e8003f0ff107a3fff0043c9af00007d87",
    [],[],"outer_terrain_snow_forest"),
  ("outpost_one_one_desert_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000dc678e240003f0ff107a3fff08cbd537000068de",
    [],[],"outer_terrain_desert_forest"),

  ("outpost_one_two_steppe",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002c678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe"),
  ("outpost_one_two_plain",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("outpost_one_two_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",
    [],[],"outer_terrain_snow"),
  ("outpost_one_two_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000055878e1ec003f0ff0000445800002b7500007d87",
    [],[],"outer_terrain_desert"),
  ("outpost_one_two_steppe_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe_forest"),
  ("outpost_one_two_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc678e248003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_forest"),
  ("outpost_one_two_snow_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow_forest"),
  ("outpost_one_two_desert_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000dc678e240003f0ff107a3fff08cbd537000068de",
    [],[],"outer_terrain_desert_forest"),
	
  ("outpost_two_one_steppe",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002c678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe"),
  ("outpost_two_one_plain",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_plain"),
  ("outpost_two_one_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c678e240003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_snow"),
  ("outpost_two_one_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005c678e240003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_desert"),
  ("outpost_two_one_steppe_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe_forest"),
  ("outpost_two_one_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc678e248003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_forest"),
  ("outpost_two_one_snow_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000cc678e1e8003f0ff107a3fff0043c9af00007d87",
    [],[],"outer_terrain_snow_forest"),
  ("outpost_two_one_desert_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000dc678e240003f0ff107a3fff08cbd537000068de",
    [],[],"outer_terrain_desert_forest"),
	
  ("outpost_two_two_steppe",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002c678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe"),
  ("outpost_two_two_plain",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("outpost_two_two_snow",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",
    [],[],"outer_terrain_snow"),
  ("outpost_two_two_desert",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005c678e240003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_desert"),
  ("outpost_two_two_steppe_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000ac678e1e8003f0ff107a3fff00004b7700007d87",
    [],[],"outer_terrain_steppe_forest"),
  ("outpost_two_two_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000bc678e248003f0ff107a3fff08cbd53700007d87",
    [],[],"outer_terrain_forest"),
  ("outpost_two_two_snow_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow"),
  ("outpost_two_two_desert_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000dc678e240003f0ff107a3fff08cbd537000068de",
    [],[],"outer_terrain_desert"),
	
  ("fort",sf_generate,"none", "none", (0,0),(100,100),-100, "0x000000003224dfb20004a92f00001d760000611000005679",
    [],[],"outer_terrain_plain"),
  ("fort_plain",sf_generate,"none", "none", (0,0),(100,100),-100, "0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("fort_snow",sf_generate,"none", "none", (0,0),(100,100),-100, "0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  ("fort_forest",sf_generate,"none", "none", (0,0),(100,100),-100, "0x000000003224dfb20004a92f00001d760000611000005679",
    [],[],"outer_terrain_plain"),
#-## Outposts end
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