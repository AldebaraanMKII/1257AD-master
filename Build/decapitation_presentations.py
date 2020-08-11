from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_items import *   # Added for Show all Items presentation.
from module_items import *   # Added for Show all Items presentation.
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

# Manualy add these to module_presentations add 
# these lines from `presentations` to bottom of the file
presentations = [
####################################### NEW v3.0 - DECAP AND DISMEMBERMENT OPTIONS
  ("enhanced_mod_options_decap", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (str_clear, s0),
        (create_text_overlay, "$g_presentation_obj_6", s0, tf_scrollable),
        (position_set_x, pos1, 50),
        (position_set_y, pos1, 50),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (position_set_x, pos1, 550),
        (position_set_y, pos1, 630),
        #(overlay_set_area_size, "$g_presentation_obj_6", pos1),
        #(set_container_overlay, "$g_presentation_obj_6"),


########################################## ROW 1 COLUMN 1
        (position_set_x, pos1, 50),
        (assign, ":value_difference", 35),

        (create_text_overlay, reg0, "@Enable decapitations:", tf_vertical_align_center),
        (store_sub, reg1, 700, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Minimum damage for decapitation:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Negative health required for decapitation:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Decapitation chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Decapitation blood variable 1 strenght:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Decapitation blood variable 2 strenght:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Decapitation blood variable 3 strenght:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Enable dismemberment:", tf_vertical_align_center),
        # (val_sub, reg1, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, reg0, pos1),

########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 420),
        (assign, ":value_difference", 35),
		
        (create_check_box_overlay, "$g_presentation_obj_1", "mesh_checkbox_off", "mesh_checkbox_on"),
        (store_sub, reg1, 686, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_decap_enabled"),

        (create_number_box_overlay, "$g_presentation_obj_2", 5, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_decap_minimum_damage"),

        (create_number_box_overlay, "$g_presentation_obj_3", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_decap_negative_health"),

        (create_number_box_overlay, "$g_presentation_obj_4", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_decap_chance"),

        (create_number_box_overlay, "$g_presentation_obj_5", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_decap_psys_blood_decapitation"),

        (create_number_box_overlay, "$g_presentation_obj_6", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_decap_psys_game_blood"),

        (create_number_box_overlay, "$g_presentation_obj_7", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_decap_psys_game_blood_2"),
		
        # (create_check_box_overlay, "$g_presentation_obj_8", "mesh_checkbox_off", "mesh_checkbox_on"),
        # (val_sub, reg1, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, "$g_presentation_obj_8", pos1),
        # (overlay_set_val, "$g_presentation_obj_8", "$g_dismemberment_enabled"),

########################### RESET
        (create_game_button_overlay, "$g_presentation_obj_32", "@Reset"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_32", pos1),

######################################### DONE
        (create_game_button_overlay, "$g_presentation_obj_33", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_33", pos1),
      ]),
#########################################
    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_decap_enabled", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_decap_minimum_damage", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_decap_negative_health", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_decap_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_decap_psys_blood_decapitation", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_decap_psys_game_blood", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_decap_psys_game_blood_2", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_dismemberment_enabled", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_32"),
          ############# resets everything to default values
          (assign, "$g_decap_enabled", 1),
          (assign, "$g_decap_minimum_damage", 30),
          (assign, "$g_decap_negative_health", 10),
          (assign, "$g_decap_chance", 20),
          (assign, "$g_decap_psys_blood_decapitation", 40),
          (assign, "$g_decap_psys_game_blood", 10),
          (assign, "$g_decap_psys_game_blood_2", 10),
          (assign, "$g_dismemberment_enabled", 1),
          (presentation_set_duration, 0),
        (else_try),
          (eq, ":object", "$g_presentation_obj_33"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################
]#############################################################################
##############################################################################
def modmerge_presentations(orig_presentations, check_duplicates = False):
    if( not check_duplicates ):
        orig_presentations.extend(presentations) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(presentations)-1):
          find_index = find_object(orig_presentations, presentations[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_presentations.append(presentations[i])
          else:
            orig_presentations[find_index] = presentations[i]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        modmerge_presentations(orig_presentations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)