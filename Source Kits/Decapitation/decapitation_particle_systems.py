from header_particle_systems import *
from compiler import *

#
# Here are the particle effects used in the Mod Kit. While the decpitation effect is required for the decap script, the other two blood effects are entierly optional but recommended for better visuals (this is personal preference though).
# 
# Simply paste these somewhere in your "module_particle_systems.py", but inside the start "[" and end "]". 
#
# Overwrite the Native "game_blood" effects with the new optional ones if you are going to use those.
# 
# You can always play around with the variables and tweak them for different results.
#


add_block = [
# Required:

    ### Dismemberment Mod Kit Decapitation blood ###
	
	("blood_decapitation", psf_billboard_3d|psf_global_emit_dir|psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_3", 
     230, 2, 0.07, 1.0, 8, 11,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.6), (0.3, 0.6),          #alpha keys
     (0.1, 0.4), (1, 0.5),      #red keys
     (0.1, 0.4), (1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.5),      #blue keys
     (0.1, 0.20),   (1, 1.5),    #scale keys
     (0.05, 0.05, 0.0),           #emit box size
     (0, 0, 3),                 #emit velocity
     0.25,                       #emit dir randomness
     300,                       #rotation speed
     0.5,                       #rotation damping
    ),

	
	
# All below is optional (remember to overwirite the native blood effects):
	
    ### Dismemberment Mod Kit enhanced blood effects ### 
	
    ("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     4500, 2, 2, 1.2, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),          #alpha keys
     (0.1, 0.2), (1, 0.2),      #red keys
     (0.1, 0.15), (1, 0.15),       #green keys
     (0.1, 0.15), (1, 0.15),      #blue keys
     (0.1, 0.02),   (1, 0.06),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.6, 1.0, 1.1),                #emit velocity
     0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     5000, 1.9, 2.75, 1.1, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.17), (0.9, 0.0),          #alpha keys
     (0.1, 0.37), (1, 0.4),      #red keys
     (0.1, 0.37), (1, 0.4),       #green keys
     (0.1, 0.37), (1, 0.4),      #blue keys
     (0.1, 0.3),   (1, 0.75),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.7, 0.1, 0.9 ),                #emit velocity
     0.5,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
	
    ### Dismemberment Mod Kit enhanced blood effects END ### 

	
	
# And in case you want the native effects back but lost them somehow:
	
	### Native blood effects backup ###
	
#	("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
#     500, 0.65, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#     (0.0, 0.7), (0.7, 0.7),          #alpha keys
#     (0.1, 0.7), (1, 0.7),      #red keys
#     (0.1, 0.7), (1, 0.7),       #green keys
#     (0.1, 0.7), (1, 0.7),      #blue keys
#     (0.0, 0.015),   (1, 0.018),  #scale keys
#     (0, 0.05, 0),               #emit box size
#     (0, 1.0, 0.3),                #emit velocity
#     0.9,                       #emit dir randomness
#     0,                         #rotation speed
#     0,                         #rotation damping
#    ),
#    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
#     2000, 0.6, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
#     (0.0, 0.25), (0.7, 0.1),        #alpha keys
#     (0.1, 0.7), (1, 0.7),      #red keys
#     (0.1, 0.7), (1, 0.7),       #green keys
#     (0.1, 0.7), (1, 0.7),      #blue keys
#     (0.0, 0.15),   (1, 0.35),    #scale keys
#     (0.01, 0.2, 0.01),             #emit box size
#     (0.2, 0.3, 0),                 #emit velocity
#     0.3,                         #emit dir randomness
#     150,                       #rotation speed
#     0,                       #rotation damping
#     ),

	### Native blood effects backup END ###
]
	

# Used by modmerger framework version >= 200 to merge stuff

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "particle_systems"
        orig_particle_systems = var_set[var_name_1]
        orig_particle_systems.extend(add_block) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)

	