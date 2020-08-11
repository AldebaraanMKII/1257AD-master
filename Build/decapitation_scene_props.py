from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

from compiler import *
# These are the dynamic heads that are spawned on decapitation. Insert these entries right before the last "]" of your "module_scene_props.py" -file.

# I reccomend playing around with the randomized physics values! These are the physical forces the object is spawned with.

####################################################
scene_props = [
   
   ### Dismemberment Mod Kit Props ###
   
   ### Heads and Limbs ###
   
   # Default
   ## Heads
   
   ("head_dynamic_male",sokf_moveable|sokf_dynamic_physics,"cut_off_head_male_dynamic","bo_cut_off_head_dynamic", [

	(ti_on_init_scene_prop,
	[
	 (store_trigger_param_1, ":prop_instance_no"),
	
	 #(particle_system_emit,"psys_game_blood",90000), ### Blood originating form the head (test, don't think this worked)
	 #(particle_system_emit,"psys_game_blood_2",90000),
	 #(particle_system_add_new, "psys_game_blood"),
	 
	 (scene_prop_set_prune_time, ":prop_instance_no", 60), ### Don't think this operation works like I would want it to either. Will try to find another way of getting rid of limbs laying around for too long.
	 (set_fixed_point_multiplier, 100),
	 
	 ### Physics Properties
	 (position_set_x, pos0, 1000), # mass = 10.0
	 (position_set_y, pos0, 80), # friction coefficient = 0.8
	 (position_set_z, pos0, 0), # reserved variable
	 (prop_instance_dynamics_set_properties, ":prop_instance_no", pos0), # Set Properties
	 
	 ### Rotational velocities
	 (store_random_in_range, ":rndm", -2000, 2000), ### The final value is a random one between these two values
	 (position_set_x, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_y, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_z, pos0, ":rndm"),
	 (prop_instance_dynamics_set_omega, ":prop_instance_no", pos0), # Set Rotation
	 
	 ### Movement velocities
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_x, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_y, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", 30, 1000),
	 (position_set_z, pos0, ":rndm"),
	 (prop_instance_dynamics_apply_impulse, ":prop_instance_no", pos0), # Set Movement
	]),
	]),
	
   ("head_dynamic_female",sokf_moveable|sokf_dynamic_physics,"cut_off_head_female_dynamic","bo_cut_off_head_dynamic", [

	(ti_on_init_scene_prop,
	[
	 (store_trigger_param_1, ":prop_instance_no"),
	
	 #(particle_system_emit,"psys_game_blood",90000), ### Blood originating form the head (test, don't think this worked)
	 #(particle_system_emit,"psys_game_blood_2",90000),
	 #(particle_system_add_new, "psys_game_blood"),
	 
	 (scene_prop_set_prune_time, ":prop_instance_no", 60), ### Don't think this operation works like I would want it to either. Will try to find another way of getting rid of limbs laying around for too long.
	 (set_fixed_point_multiplier, 100),
	 
	 ### Physics Properties
	 (position_set_x, pos0, 1000), # mass = 10.0
	 (position_set_y, pos0, 80), # friction coefficient = 0.8
	 (position_set_z, pos0, 0), # reserved variable
	 (prop_instance_dynamics_set_properties, ":prop_instance_no", pos0), # Set Properties
	 
	 ### Rotational velocities
	 (store_random_in_range, ":rndm", -2000, 2000), ### The final value is a random one between these two values
	 (position_set_x, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_y, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_z, pos0, ":rndm"),
	 (prop_instance_dynamics_set_omega, ":prop_instance_no", pos0), # Set Rotation
	 
	 ### Movement velocities
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_x, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", -2000, 2000),
	 (position_set_y, pos0, ":rndm"),
	 (store_random_in_range, ":rndm", 30, 800),
	 (position_set_z, pos0, ":rndm"),
	 (prop_instance_dynamics_apply_impulse, ":prop_instance_no", pos0), # Set Movement
    ]),
	]),
	
	## Heads END
	# Default END
]#########################
##########################


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "scene_props"
        orig_scene_props = var_set[var_name_1]
        orig_scene_props.extend(scene_props) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)

