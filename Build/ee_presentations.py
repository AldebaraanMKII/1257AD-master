from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

## CC
from header_skills import *
from header_items import *
from module_items import *
#from module_my_mod_set import *
## CC

from header_skills import *  ###### NEW v2.1

presentations = [



####################################### PARTY OPTIONS
  ("enhanced_mod_options_party", 0, mesh_load_window, [
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

        (create_text_overlay, reg0, "@Party base size:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Bonus per point of leadership:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Amount of renown needed to increase size by 1:", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Bonus for faction leaders:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Bonus for marshals:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Bonus per castle:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Garrison reinforcement rate:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Garrison max size (castles):", tf_vertical_align_center),
        (position_set_y, pos1, 455),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Garrison max size (towns):", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lord reinforcement rate:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lance refill rate:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max lances per village:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max lances per castle:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max lances per town:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Town mercenary companies refill rate:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),

        ######## checkbox
        (create_text_overlay, reg0, "@NPC lords/fiefs upgrade their troops like the player does:", tf_vertical_align_center),
        (position_set_y, pos1, 175),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Prevent prisoners in fiefs from dying/being ransomed:", tf_vertical_align_center),
        (position_set_y, pos1, 140),
        (overlay_set_position, reg0, pos1),
        ###################


########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 420),

        (create_number_box_overlay, "$g_presentation_obj_1", 10, 1000),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_party_base_size"),

        (create_number_box_overlay, "$g_presentation_obj_2", 0, 1000),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_party_size_leadership_bonus"),


        (create_number_box_overlay, "$g_presentation_obj_3", 1, 1000),
        (position_set_y, pos1, 616),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_party_size_renown_bonus_divider"),


        (create_number_box_overlay, "$g_presentation_obj_4", 0, 1000),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_party_size_king_bonus"),


        (create_number_box_overlay, "$g_presentation_obj_5", 0, 1000),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_party_size_marshall_bonus"),

        (create_number_box_overlay, "$g_presentation_obj_6", 0, 1000),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_party_size_castle_bonus"),


        (create_number_box_overlay, "$g_presentation_obj_7", 4, 1000),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_party_garrison_reinforcement_rate"),

        (create_number_box_overlay, "$g_presentation_obj_8", 100, 10000),
        (position_set_y, pos1, 441),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_8", "$g_party_garrison_max_size_castles"),


        (create_number_box_overlay, "$g_presentation_obj_9", 100, 10000),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_val, "$g_presentation_obj_9", "$g_party_garrison_max_size_towns"),



        (create_number_box_overlay, "$g_presentation_obj_10", 4, 1000),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        (overlay_set_val, "$g_presentation_obj_10", "$g_party_npc_reinforcement_rate"),


        (create_number_box_overlay, "$g_presentation_obj_11", 4, 1000),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_set_val, "$g_presentation_obj_11", "$g_party_player_reinforcement_rate"),


        (create_number_box_overlay, "$g_presentation_obj_12", 1, 100),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_set_val, "$g_presentation_obj_12", "$g_party_lances_max_village"),


        (create_number_box_overlay, "$g_presentation_obj_13", 1, 100),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_set_val, "$g_presentation_obj_13", "$g_party_lances_max_castle"),


        (create_number_box_overlay, "$g_presentation_obj_14", 1, 100),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_set_val, "$g_presentation_obj_14", "$g_party_lances_max_town"),


        (create_number_box_overlay, "$g_presentation_obj_15", 4, 1000),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_set_val, "$g_presentation_obj_15", "$g_party_town_merc_refill_rate"),

        (position_set_y, pos1, 166),
        (create_check_box_overlay, "$g_presentation_obj_16", "mesh_checkbox_off", "mesh_checkbox_on"),
        (overlay_set_position, "$g_presentation_obj_16", pos1),
        (overlay_set_val, "$g_presentation_obj_16", "$g_party_npc_trainer"),

        (position_set_y, pos1, 136),
        (create_check_box_overlay, "$g_presentation_obj_17", "mesh_checkbox_off", "mesh_checkbox_on"),
        (overlay_set_position, "$g_presentation_obj_17", pos1),
        (overlay_set_val, "$g_presentation_obj_17", "$g_prison_culling"),



########################################## ROW 2 COLUMN 1
        (position_set_x, pos1, 520),

        (create_text_overlay, reg0, "@Morale per leadership:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Morale per leadership when king:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max morale:", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Number of men in party affects morale:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),


        # (create_text_overlay, reg0, "@Remove deserter recruit penalty:", tf_vertical_align_center),
        # (position_set_y, pos1, 525),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Max tax inefficiency:", tf_vertical_align_center),
        # (position_set_y, pos1, 490),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 455),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 420),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 385),
        # (overlay_set_position, reg0, pos1),


########################################## ROW 2 COLUMN 2
        (position_set_x, pos1, 850),

        (create_number_box_overlay, "$g_presentation_obj_18", 0, 1000),
        (position_set_y, pos1, 690),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_18", pos1),
        (overlay_set_val, "$g_presentation_obj_18", "$g_party_morale_per_leadership"),

        (create_number_box_overlay, "$g_presentation_obj_19", 0, 1000),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_19", pos1),
        (overlay_set_val, "$g_presentation_obj_19", "$g_party_morale_per_leadership_king"),

        (create_number_box_overlay, "$g_presentation_obj_20", 99, 1000),
        (position_set_y, pos1, 616),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_20", pos1),
        (overlay_set_val, "$g_presentation_obj_20", "$g_party_max_morale"),

        (position_set_y, pos1, 581),
        (create_check_box_overlay, "$g_presentation_obj_21", "mesh_checkbox_off", "mesh_checkbox_on"),
        (overlay_set_position, "$g_presentation_obj_21", pos1),
        (overlay_set_val, "$g_presentation_obj_21", "$g_party_size_affects_morale"),

        (create_number_box_overlay, "$g_presentation_obj_22", 0, 1000),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        # (position_set_x, pos1, 390),
        (overlay_set_position, "$g_presentation_obj_22", pos1),
        (overlay_set_val, "$g_presentation_obj_22", "$g_party_prisoners_per_prisoner_management_point"),




########################### RESET
        (create_game_button_overlay, "$g_presentation_obj_23", "@Reset"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_23", pos1),



######################################### DONE
        (create_game_button_overlay, "$g_presentation_obj_24", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_24", pos1),

      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_party_base_size", ":value"),
          ################## these set the minimum values otherwise weird things would happen
          # (try_begin),
            # (lt, "$g_party_base_size", 10),
            # (assign, "$g_party_base_size", 10),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_party_size_leadership_bonus", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_leadership_bonus", 1),
            # (assign, "$g_party_size_leadership_bonus", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_party_size_renown_bonus_divider", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_renown_bonus_divider", 1),
            # (assign, "$g_party_size_renown_bonus_divider", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_party_size_king_bonus", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_king_bonus", 1),
            # (assign, "$g_party_size_king_bonus", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_party_size_marshall_bonus", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_marshall_bonus", 1),
            # (assign, "$g_party_size_marshall_bonus", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_party_size_castle_bonus", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_castle_bonus", 1),
            # (assign, "$g_party_size_castle_bonus", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_party_garrison_reinforcement_rate", ":value"),
          # (try_begin),
            # (lt, "$g_party_garrison_reinforcement_rate", 4),
            # (assign, "$g_party_garrison_reinforcement_rate", 4),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_party_garrison_max_size_castles", ":value"),
          # (try_begin),
            # (lt, "$g_party_garrison_max_size_castles", 100),
            # (assign, "$g_party_garrison_max_size_castles", 100),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_9"),
          (assign, "$g_party_garrison_max_size_towns", ":value"),
          # (try_begin),
            # (lt, "$g_party_garrison_max_size_towns", 100),
            # (assign, "$g_party_garrison_max_size_towns", 100),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_party_npc_reinforcement_rate", ":value"),
          # (try_begin),
            # (lt, "$g_party_npc_reinforcement_rate", 4),
            # (assign, "$g_party_npc_reinforcement_rate", 4),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (assign, "$g_party_player_reinforcement_rate", ":value"),
          # (try_begin),
            # (lt, "$g_party_player_reinforcement_rate", 4),
            # (assign, "$g_party_player_reinforcement_rate", 4),
          # (try_end),

        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (assign, "$g_party_lances_max_village", ":value"),
          # (try_begin),
            # (lt, "$g_party_lances_max_village", 1),
            # (assign, "$g_party_lances_max_village", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (assign, "$g_party_lances_max_castle", ":value"),
          # (try_begin),
            # (lt, "$g_party_lances_max_castle", 1),
            # (assign, "$g_party_lances_max_castle", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (assign, "$g_party_lances_max_town", ":value"),
          # (try_begin),
            # (lt, "$g_party_lances_max_town", 1),
            # (assign, "$g_party_lances_max_town", 1),
          # (try_end),

        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (assign, "$g_party_town_merc_refill_rate", ":value"),
          # (try_begin),
            # (lt, "$g_party_town_merc_refill_rate", 4),
            # (assign, "$g_party_town_merc_refill_rate", 4),
          # (try_end),

        (else_try),
          (eq, ":object", "$g_presentation_obj_16"),
          (assign, "$g_party_npc_trainer", ":value"),
          # (try_begin),
            # (lt, "$g_party_npc_trainer", 1),
            # (assign, "$g_party_npc_trainer", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_17"),
          (assign, "$g_prison_culling", ":value"),
          # (try_begin),
            # (lt, "$g_prison_culling", 1),
            # (assign, "$g_prison_culling", 1),
          # (try_end),

        (else_try),
          (eq, ":object", "$g_presentation_obj_18"),
          (assign, "$g_party_morale_per_leadership", ":value"),
          # (try_begin),
            # (lt, "$g_party_morale_per_leadership", 1),
            # (assign, "$g_party_morale_per_leadership", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_19"),
          (assign, "$g_party_morale_per_leadership_king", ":value"),
          # (try_begin),
            # (lt, "$g_party_morale_per_leadership_king", 1),
            # (assign, "$g_party_morale_per_leadership_king", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_20"),
          (assign, "$g_party_max_morale", ":value"),
          # (try_begin),
            # (lt, "$g_party_max_morale", 50),
            # (assign, "$g_party_max_morale", 50),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_21"),
          (assign, "$g_party_size_affects_morale", ":value"),
          # (try_begin),
            # (lt, "$g_party_size_affects_morale", 1),
            # (assign, "$g_party_size_affects_morale", 1),
          # (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_22"),
          (assign, "$g_party_prisoners_per_prisoner_management_point", ":value"),
          # (try_begin),
            # (lt, "$g_party_prisoners_per_prisoner_management_point", 1),
            # (assign, "$g_party_prisoners_per_prisoner_management_point", 1),
          # (try_end),


        (else_try),
          (eq, ":object", "$g_presentation_obj_23"),
          ############# resets everything to default values
          (assign, "$g_party_base_size", 30),
          (assign, "$g_party_size_leadership_bonus", 15),
          (assign, "$g_party_size_renown_bonus_divider", 10),
          (assign, "$g_party_size_king_bonus", 150),
          (assign, "$g_party_size_marshall_bonus", 80),
          (assign, "$g_party_size_castle_bonus", 40),
          (assign, "$g_party_garrison_reinforcement_rate", 24),
          (assign, "$g_party_garrison_max_size_castles", 600),
          (assign, "$g_party_garrison_max_size_towns", 800),
          (assign, "$g_party_npc_reinforcement_rate", 24),
          (assign, "$g_party_player_reinforcement_rate", 72),
          (assign, "$g_party_lances_max_village", 12),
          (assign, "$g_party_lances_max_castle", 18),
          (assign, "$g_party_lances_max_town", 15),
          (assign, "$g_party_town_merc_refill_rate", 168),
          (assign, "$g_party_npc_trainer", 1),
          (assign, "$g_prison_culling", 0),
          (assign, "$g_party_morale_per_leadership", 25),
          (assign, "$g_party_morale_per_leadership_king", 35),
          (assign, "$g_party_max_morale", 99),
          (assign, "$g_party_size_affects_morale", 0),
          (assign, "$g_party_prisoners_per_prisoner_management_point", 15),
          (presentation_set_duration, 0),

        (else_try),
          (eq, ":object", "$g_presentation_obj_24"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################








####################################### KINGDOM PARTY OPTIONS
  ("enhanced_mod_options_party_kingdom", 0, mesh_load_window, [
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

        (create_text_overlay, reg0, "@Kingdom parties respawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Forager party spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Scout spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Patrol spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Caravan spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Prisoner train spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@War party spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Mercenary company spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 455),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max forager parties per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max scouts per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max patrols per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max caravans per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max prisoner trains per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max war parties per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max mercenary companies per faction:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),



########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 390),

        (create_number_box_overlay, "$g_presentation_obj_1", 4, 101),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_party_faction_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_2", 0, 101),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_party_faction_parties_spawn_chance_foragers"),

        (create_number_box_overlay, "$g_presentation_obj_3", 0, 101),
        (position_set_y, pos1, 616),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_party_faction_parties_spawn_chance_scouts"),

        (create_number_box_overlay, "$g_presentation_obj_4", 0, 101),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_party_faction_parties_spawn_chance_patrols"),

        (create_number_box_overlay, "$g_presentation_obj_5", 0, 101),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_party_faction_parties_spawn_chance_caravans"),

        (create_number_box_overlay, "$g_presentation_obj_6", 0, 101),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_party_faction_parties_spawn_chance_prisoner_trains"),

        (create_number_box_overlay, "$g_presentation_obj_7", 0, 101),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_party_faction_parties_spawn_chance_war_parties"),

        (create_number_box_overlay, "$g_presentation_obj_8", 0, 101),
        (position_set_y, pos1, 441),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_8", "$g_party_faction_parties_spawn_chance_mercenary_companies"),


        (create_number_box_overlay, "$g_presentation_obj_9", 1, 50),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_val, "$g_presentation_obj_9", "$g_party_faction_max_parties_foragers"),

        (create_number_box_overlay, "$g_presentation_obj_10", 1, 50),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        (overlay_set_val, "$g_presentation_obj_10", "$g_party_faction_max_parties_scouts"),

        (create_number_box_overlay, "$g_presentation_obj_11", 1, 50),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_set_val, "$g_presentation_obj_11", "$g_party_faction_max_parties_patrols"),

        (create_number_box_overlay, "$g_presentation_obj_12", 1, 50),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_set_val, "$g_presentation_obj_12", "$g_party_faction_max_parties_caravans"),

        (create_number_box_overlay, "$g_presentation_obj_13", 1, 50),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_set_val, "$g_presentation_obj_13", "$g_party_faction_max_parties_prisoner_trains"),

        (create_number_box_overlay, "$g_presentation_obj_14", 1, 50),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_set_val, "$g_presentation_obj_14", "$g_party_faction_max_parties_war_parties"),

        (create_number_box_overlay, "$g_presentation_obj_15", 1, 50),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_set_val, "$g_presentation_obj_15", "$g_party_faction_max_parties_mercenary_companies"),



########################################## ROW 2 COLUMN 1
        # (position_set_x, pos1, 520),

########################################## ROW 2 COLUMN 2
        # (position_set_x, pos1, 850),




########################### RESET
        (create_game_button_overlay, "$g_presentation_obj_16", "@Reset"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_16", pos1),



######################################### DONE
        (create_game_button_overlay, "$g_presentation_obj_17", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_17", pos1),

      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_party_faction_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_party_faction_parties_spawn_chance_foragers", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_party_faction_parties_spawn_chance_scouts", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_party_faction_parties_spawn_chance_patrols", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_party_faction_parties_spawn_chance_caravans", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_party_faction_parties_spawn_chance_prisoner_trains", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_party_faction_parties_spawn_chance_war_parties", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_party_faction_parties_spawn_chance_mercenary_companies", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_9"),
          (assign, "$g_party_faction_max_parties_foragers", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_party_faction_max_parties_scouts", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (assign, "$g_party_faction_max_parties_patrols", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (assign, "$g_party_faction_max_parties_caravans", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (assign, "$g_party_faction_max_parties_prisoner_trains", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (assign, "$g_party_faction_max_parties_war_parties", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (assign, "$g_party_faction_max_parties_mercenary_companies", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_16"),
          ############# resets everything to default values
          (assign, "$g_party_faction_respawn_rate", 24),

          (assign, "$g_party_faction_parties_spawn_chance_foragers", 8),
          (assign, "$g_party_faction_parties_spawn_chance_scouts", 15),
          (assign, "$g_party_faction_parties_spawn_chance_patrols", 10),
          (assign, "$g_party_faction_parties_spawn_chance_caravans", 15),
          (assign, "$g_party_faction_parties_spawn_chance_prisoner_trains", 8),
          (assign, "$g_party_faction_parties_spawn_chance_war_parties", 5),
          (assign, "$g_party_faction_parties_spawn_chance_mercenary_companies", 5),


          (assign, "$g_party_faction_max_parties_foragers", 2),
          (assign, "$g_party_faction_max_parties_scouts", 3),
          (assign, "$g_party_faction_max_parties_patrols", 2),
          (assign, "$g_party_faction_max_parties_caravans", 2),
          (assign, "$g_party_faction_max_parties_prisoner_trains", 1),
          (assign, "$g_party_faction_max_parties_war_parties", 1),
          (assign, "$g_party_faction_max_parties_mercenary_companies", 1),

          (presentation_set_duration, 0),

        (else_try),
          (eq, ":object", "$g_presentation_obj_17"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################









####################################### NON KINGDOM PARTY OPTIONS
  ("enhanced_mod_options_party_non_kingdom", 0, mesh_load_window, [
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

        (create_text_overlay, reg0, "@Non kingdom parties respawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Looter spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Pirate spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Mountain bandit spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Steppe bandit spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Taiga bandit spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Forest bandit spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Desert bandit spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 455),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Deserter spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),



        (create_text_overlay, reg0, "@Max looter parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max pirate parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max mountain bandit parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max steppe bandit parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max taiga bandit parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max forest bandit parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max desert bandit parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 175),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max deserter parties on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 140),
        (overlay_set_position, reg0, pos1),






########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 390),

        (create_number_box_overlay, "$g_presentation_obj_1", 4, 1000),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_party_bandit_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_2", 0, 101),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_party_bandit_spawn_chance_looter"),

        (create_number_box_overlay, "$g_presentation_obj_3", 0, 101),
        (position_set_y, pos1, 616),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_party_bandit_spawn_chance_sea_raider"),

        (create_number_box_overlay, "$g_presentation_obj_4", 0, 101),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_party_bandit_spawn_chance_mountain_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_5", 0, 101),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_party_bandit_spawn_chance_steppe_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_6", 0, 101),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_party_bandit_spawn_chance_taiga_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_7", 0, 101),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_party_bandit_spawn_chance_forest_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_8", 0, 101),
        (position_set_y, pos1, 441),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_8", "$g_party_bandit_spawn_chance_desert_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_9", 0, 101),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_val, "$g_presentation_obj_9", "$g_party_bandit_spawn_chance_deserters"),



        (create_number_box_overlay, "$g_presentation_obj_10", 1, 100),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        (overlay_set_val, "$g_presentation_obj_10", "$g_party_bandit_max_parties_looter"),

        (create_number_box_overlay, "$g_presentation_obj_11", 1, 100),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_set_val, "$g_presentation_obj_11", "$g_party_bandit_max_parties_sea_raider"),

        (create_number_box_overlay, "$g_presentation_obj_12", 1, 100),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_set_val, "$g_presentation_obj_12", "$g_party_bandit_max_parties_mountain_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_13", 1, 100),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_set_val, "$g_presentation_obj_13", "$g_party_bandit_max_parties_steppe_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_14", 1, 100),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_set_val, "$g_presentation_obj_14", "$g_party_bandit_max_parties_taiga_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_15", 1, 100),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_set_val, "$g_presentation_obj_15", "$g_party_bandit_max_parties_forest_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_16", 1, 100),
        (position_set_y, pos1, 161),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_16", pos1),
        (overlay_set_val, "$g_presentation_obj_16", "$g_party_bandit_max_parties_desert_bandits"),

        (create_number_box_overlay, "$g_presentation_obj_17", 1, 100),
        (position_set_y, pos1, 126),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_17", pos1),
        (overlay_set_val, "$g_presentation_obj_17", "$g_party_bandit_max_parties_deserters"),



########################################## ROW 2 COLUMN 1
        (position_set_x, pos1, 520),

        (create_text_overlay, reg0, "@Roving knight spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max roving knight parties:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),


        (create_text_overlay, reg0, "@Rogue mercenary company spawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Rogue mercenary company spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max rogue mercenary companies on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),


        (create_text_overlay, reg0, "@Peasant rebellion spawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Peasant rebellion spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max Peasant rebellions on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 455),
        (overlay_set_position, reg0, pos1),


        (create_text_overlay, reg0, "@Well equipped rebellion spawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Well equipped rebellion spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max well equipped rebellions on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),


        (create_text_overlay, reg0, "@Fugitive serf spawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Fugitive serf spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max fugitive serfs on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Mercenary Warband spawn chance:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max Mercenary Warbands on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 175),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Mongol camp respawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 140),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max Mongol camps on the map:", tf_vertical_align_center),
        (position_set_y, pos1, 105),
        (overlay_set_position, reg0, pos1),


########################################## ROW 2 COLUMN 2
        (position_set_x, pos1, 850),


        (create_number_box_overlay, "$g_presentation_obj_18", 0, 101),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_18", pos1),
        (overlay_set_val, "$g_presentation_obj_18", "$g_party_bandit_spawn_chance_roving_knights"),

        (create_number_box_overlay, "$g_presentation_obj_19", 1, 100),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_19", pos1),
        (overlay_set_val, "$g_presentation_obj_19", "$g_party_bandit_max_parties_roving_knights"),

		
        (create_number_box_overlay, "$g_presentation_obj_20", 4, 1000),
        (position_set_y, pos1, 616),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_20", pos1),
        (overlay_set_val, "$g_presentation_obj_20", "$g_party_mercenary_company_spawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_21", 0, 101),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_21", pos1),
        (overlay_set_val, "$g_presentation_obj_21", "$g_party_mercenary_company_spawn_chance"),

        (create_number_box_overlay, "$g_presentation_obj_22", 1, 50),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_22", pos1),
        (overlay_set_val, "$g_presentation_obj_22", "$g_party_mercenary_company_max"),



        (create_number_box_overlay, "$g_presentation_obj_23", 4, 1000),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_23", pos1),
        (overlay_set_val, "$g_presentation_obj_23", "$g_party_rebellion_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_24", 0, 101),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_24", pos1),
        (overlay_set_val, "$g_presentation_obj_24", "$g_party_rebellion_chance"),

        (create_number_box_overlay, "$g_presentation_obj_25", 1, 50),
        (position_set_y, pos1, 441),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_25", pos1),
        (overlay_set_val, "$g_presentation_obj_25", "$g_party_rebellion_max"),



        (create_number_box_overlay, "$g_presentation_obj_26", 4, 1000),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_26", pos1),
        (overlay_set_val, "$g_presentation_obj_26", "$g_party_rebellion_strong_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_27", 0, 101),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_27", pos1),
        (overlay_set_val, "$g_presentation_obj_27", "$g_party_rebellion_strong_chance"),

        (create_number_box_overlay, "$g_presentation_obj_28", 1, 50),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_28", pos1),
        (overlay_set_val, "$g_presentation_obj_28", "$g_party_rebellion_strong_max"),



        (create_number_box_overlay, "$g_presentation_obj_29", 4, 1000),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_29", pos1),
        (overlay_set_val, "$g_presentation_obj_29", "$g_party_fugitive_serf_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_30", 0, 101),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_30", pos1),
        (overlay_set_val, "$g_presentation_obj_30", "$g_party_fugitive_serf_chance"),

        (create_number_box_overlay, "$g_presentation_obj_31", 1, 50),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_31", pos1),
        (overlay_set_val, "$g_presentation_obj_31", "$g_party_fugitive_serf_max"),

        (create_number_box_overlay, "$g_presentation_obj_32", 1, 101),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_32", pos1),
        (overlay_set_val, "$g_presentation_obj_32", "$g_party_mercenary_warband_chance"),

        (create_number_box_overlay, "$g_presentation_obj_33", 1, 50),
        (position_set_y, pos1, 161),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_33", pos1),
        (overlay_set_val, "$g_presentation_obj_33", "$g_party_mercenary_warband_max"),

        (create_number_box_overlay, "$g_presentation_obj_34", 0, 721),
        (position_set_y, pos1, 127),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_34", pos1),
        (overlay_set_val, "$g_presentation_obj_34", "$g_party_mongol_camp_rate"),

        (create_number_box_overlay, "$g_presentation_obj_35", 1, 100),
        (position_set_y, pos1, 92),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_35", pos1),
        (overlay_set_val, "$g_presentation_obj_35", "$g_party_mongol_camp_max"),



########################### RESET
        (create_game_button_overlay, "$g_presentation_obj_39", "@Reset"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_39", pos1),



######################################### DONE
        (create_game_button_overlay, "$g_presentation_obj_40", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_40", pos1),

      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_party_bandit_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_party_bandit_spawn_chance_looter", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_party_bandit_spawn_chance_sea_raider", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_party_bandit_spawn_chance_mountain_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_party_bandit_spawn_chance_steppe_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_party_bandit_spawn_chance_taiga_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_party_bandit_spawn_chance_forest_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_party_bandit_spawn_chance_desert_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_9"),
          (assign, "$g_party_bandit_spawn_chance_deserters", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_party_bandit_max_parties_looter", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (assign, "$g_party_bandit_max_parties_sea_raider", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (assign, "$g_party_bandit_max_parties_mountain_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (assign, "$g_party_bandit_max_parties_steppe_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (assign, "$g_party_bandit_max_parties_taiga_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (assign, "$g_party_bandit_max_parties_forest_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_16"),
          (assign, "$g_party_bandit_max_parties_desert_bandits", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_17"),
          (assign, "$g_party_bandit_max_parties_deserters", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_18"),
          (assign, "$g_party_bandit_spawn_chance_roving_knights", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_19"),
          (assign, "$g_party_bandit_max_parties_roving_knights", ":value"),

        (else_try),
          (eq, ":object", "$g_presentation_obj_20"),
          (assign, "$g_party_mercenary_company_spawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_21"),
          (assign, "$g_party_mercenary_company_spawn_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_22"),
          (assign, "$g_party_mercenary_company_max", ":value"),

        (else_try),
          (eq, ":object", "$g_presentation_obj_23"),
          (assign, "$g_party_rebellion_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_24"),
          (assign, "$g_party_rebellion_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_25"),
          (assign, "$g_party_rebellion_max", ":value"),

        (else_try),
          (eq, ":object", "$g_presentation_obj_26"),
          (assign, "$g_party_rebellion_strong_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_27"),
          (assign, "$g_party_rebellion_strong_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_28"),
          (assign, "$g_party_rebellion_strong_max", ":value"),

        (else_try),
          (eq, ":object", "$g_presentation_obj_29"),
          (assign, "$g_party_fugitive_serf_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_30"),
          (assign, "$g_party_fugitive_serf_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_31"),
          (assign, "$g_party_fugitive_serf_max", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_32"),
          (assign, "$g_party_mercenary_warband_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_33"),
          (assign, "$g_party_mercenary_warband_max", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_34"),
          (assign, "$g_party_mongol_camp_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_35"),
          (assign, "$g_party_mongol_camp_max", ":value"),




        (else_try),
          (eq, ":object", "$g_presentation_obj_39"),
          ############# resets everything to default values
          (assign, "$g_party_bandit_respawn_rate", 36),

          (assign, "$g_party_bandit_spawn_chance_looter", 60),
          (assign, "$g_party_bandit_spawn_chance_sea_raider", 40),
          (assign, "$g_party_bandit_spawn_chance_mountain_bandits", 50),
          (assign, "$g_party_bandit_spawn_chance_steppe_bandits", 50),
          (assign, "$g_party_bandit_spawn_chance_taiga_bandits", 50),
          (assign, "$g_party_bandit_spawn_chance_forest_bandits", 50),
          (assign, "$g_party_bandit_spawn_chance_desert_bandits", 50),
          (assign, "$g_party_bandit_spawn_chance_deserters", 40),

          (assign, "$g_party_bandit_max_parties_looter", 50),
          (assign, "$g_party_bandit_max_parties_sea_raider", 30),
          (assign, "$g_party_bandit_max_parties_mountain_bandits", 40),
          (assign, "$g_party_bandit_max_parties_steppe_bandits", 30),
          (assign, "$g_party_bandit_max_parties_taiga_bandits", 30),
          (assign, "$g_party_bandit_max_parties_forest_bandits", 40),
          (assign, "$g_party_bandit_max_parties_desert_bandits", 30),
          (assign, "$g_party_bandit_max_parties_deserters", 60),

          (assign, "$g_party_bandit_spawn_chance_roving_knights", 30),
          (assign, "$g_party_bandit_max_parties_roving_knights", 10),

          (assign, "$g_party_mercenary_company_spawn_rate", 72),
          (assign, "$g_party_mercenary_company_spawn_chance", 30),
          (assign, "$g_party_mercenary_company_max", 10),

          (assign, "$g_party_rebellion_respawn_rate", 168),
          (assign, "$g_party_rebellion_chance", 10),
          (assign, "$g_party_rebellion_max", 5),

          (assign, "$g_party_rebellion_strong_respawn_rate", 168),
          (assign, "$g_party_rebellion_strong_chance", 5),
          (assign, "$g_party_rebellion_strong_max", 5),

          (assign, "$g_party_fugitive_serf_respawn_rate", 36),
          (assign, "$g_party_fugitive_serf_chance", 20),
          (assign, "$g_party_fugitive_serf_max", 20),

          (assign, "$g_party_mercenary_warband_chance", 40),
          (assign, "$g_party_mercenary_warband_max", 40),
		  
          (assign, "$g_party_mongol_camp_rate", 168),
          (assign, "$g_party_mongol_camp_max", 20),

          (presentation_set_duration, 0),



        (else_try),
          (eq, ":object", "$g_presentation_obj_40"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################









####################################### MERCHANT OPTIONS
  ("enhanced_mod_options_merchants", 0, mesh_load_window, [
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

        (create_text_overlay, reg0, "@Town merchant respawn rate:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Goods merchant item count:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
        (position_set_y, pos1, 630),
        (overlay_set_position, reg0, pos1),

        ############ Armorer
        (create_text_overlay, reg0, "@Armorer body armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer head armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer foot armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer hand armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", tf_vertical_align_center),
        (position_set_y, pos1, 455),
        (overlay_set_position, reg0, pos1),

        ############ Weaponsmith
        (create_text_overlay, reg0, "@Weaponsmith one handed weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith two handed weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith polearm count:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith shield count:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith bow count:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith crossbow count:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith thrown weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith arrow quiver count:", tf_vertical_align_center),
        (position_set_y, pos1, 175),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith bolt quiver count:", tf_vertical_align_center),
        (position_set_y, pos1, 140),
        (overlay_set_position, reg0, pos1),






########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 390),

        (create_number_box_overlay, "$g_presentation_obj_1", 4, 1000),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_misc_merchant_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_2", 0, 61),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_misc_merchant_itp_type_goods"),



        (create_number_box_overlay, "$g_presentation_obj_3", 0, 31),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_misc_merchant_itp_type_body_armor"),

        (create_number_box_overlay, "$g_presentation_obj_4", 0, 31),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_misc_merchant_itp_type_head_armor"),

        (create_number_box_overlay, "$g_presentation_obj_5", 0, 31),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_misc_merchant_itp_type_foot_armor"),

        (create_number_box_overlay, "$g_presentation_obj_6", 0, 31),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_misc_merchant_itp_type_hand_armor"),




        (create_number_box_overlay, "$g_presentation_obj_7", 0, 31),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_misc_merchant_itp_type_one_handed_wpn"),

        (create_number_box_overlay, "$g_presentation_obj_8", 0, 31),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_8", "$g_misc_merchant_itp_type_two_handed_wpn"),

        (create_number_box_overlay, "$g_presentation_obj_9", 0, 31),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_val, "$g_presentation_obj_9", "$g_misc_merchant_itp_type_polearm"),

        (create_number_box_overlay, "$g_presentation_obj_10", 0, 31),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        (overlay_set_val, "$g_presentation_obj_10", "$g_misc_merchant_itp_type_shield"),

        (create_number_box_overlay, "$g_presentation_obj_11", 0, 31),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_set_val, "$g_presentation_obj_11", "$g_misc_merchant_itp_type_bow"),

        (create_number_box_overlay, "$g_presentation_obj_12", 0, 31),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_set_val, "$g_presentation_obj_12", "$g_misc_merchant_itp_type_crossbow"),

        (create_number_box_overlay, "$g_presentation_obj_13", 0, 31),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_set_val, "$g_presentation_obj_13", "$g_misc_merchant_itp_type_thrown"),

        (create_number_box_overlay, "$g_presentation_obj_14", 0, 31),
        (position_set_y, pos1, 161),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_set_val, "$g_presentation_obj_14", "$g_misc_merchant_itp_type_arrows"),

        (create_number_box_overlay, "$g_presentation_obj_15", 0, 31),
        (position_set_y, pos1, 126),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_set_val, "$g_presentation_obj_15", "$g_misc_merchant_itp_type_bolts"),


########################################## ROW 2 COLUMN 1
        (position_set_x, pos1, 480),

        (create_text_overlay, reg0, "@Horse merchant horse count:", tf_vertical_align_center),
        (position_set_y, pos1, 700),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Horse merchant (faction) horse count:", tf_vertical_align_center),
        (position_set_y, pos1, 665),
        (overlay_set_position, reg0, pos1),


        ############ Armorer
        (create_text_overlay, reg0, "@Armorer (faction) body armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 595),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer (faction) head armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 560),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer (faction) foot armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 525),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Armorer (faction) hand armor count:", tf_vertical_align_center),
        (position_set_y, pos1, 490),
        (overlay_set_position, reg0, pos1),



        ############ Weaponsmith
        (create_text_overlay, reg0, "@Weaponsmith (faction) one handed weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 420),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) two handed weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 385),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) polearm count:", tf_vertical_align_center),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) shield count:", tf_vertical_align_center),
        (position_set_y, pos1, 315),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) bow count:", tf_vertical_align_center),
        (position_set_y, pos1, 280),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) crossbow count:", tf_vertical_align_center),
        (position_set_y, pos1, 245),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) thrown weapon count:", tf_vertical_align_center),
        (position_set_y, pos1, 210),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) arrow quiver count:", tf_vertical_align_center),
        (position_set_y, pos1, 175),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Weaponsmith (faction) bolt quiver count:", tf_vertical_align_center),
        (position_set_y, pos1, 140),
        (overlay_set_position, reg0, pos1),


########################################## ROW 2 COLUMN 2
        (position_set_x, pos1, 850),


        (create_number_box_overlay, "$g_presentation_obj_16", 0, 36),
        (position_set_y, pos1, 686),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_16", pos1),
        (overlay_set_val, "$g_presentation_obj_16", "$g_misc_merchant_itp_type_horse"),

        (create_number_box_overlay, "$g_presentation_obj_17", 0, 36),
        (position_set_y, pos1, 651),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_17", pos1),
        (overlay_set_val, "$g_presentation_obj_17", "$g_misc_merchant_faction_itp_type_horse"),



        (create_number_box_overlay, "$g_presentation_obj_18", 0, 31),
        (position_set_y, pos1, 581),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_18", pos1),
        (overlay_set_val, "$g_presentation_obj_18", "$g_misc_merchant_faction_itp_type_body_armor"),

        (create_number_box_overlay, "$g_presentation_obj_19", 0, 31),
        (position_set_y, pos1, 546),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_19", pos1),
        (overlay_set_val, "$g_presentation_obj_19", "$g_misc_merchant_faction_itp_type_head_armor"),

        (create_number_box_overlay, "$g_presentation_obj_20", 0, 31),
        (position_set_y, pos1, 511),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_20", pos1),
        (overlay_set_val, "$g_presentation_obj_20", "$g_misc_merchant_faction_itp_type_foot_armor"),

        (create_number_box_overlay, "$g_presentation_obj_21", 0, 31),
        (position_set_y, pos1, 476),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_21", pos1),
        (overlay_set_val, "$g_presentation_obj_21", "$g_misc_merchant_faction_itp_type_hand_armor"),

        (create_number_box_overlay, "$g_presentation_obj_22", 0, 31),
        (position_set_y, pos1, 406),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_22", pos1),
        (overlay_set_val, "$g_presentation_obj_22", "$g_misc_merchant_faction_itp_type_one_handed_wpn"),

        (create_number_box_overlay, "$g_presentation_obj_23", 0, 31),
        (position_set_y, pos1, 371),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_23", pos1),
        (overlay_set_val, "$g_presentation_obj_23", "$g_misc_merchant_faction_itp_type_two_handed_wpn"),

        (create_number_box_overlay, "$g_presentation_obj_24", 0, 31),
        (position_set_y, pos1, 336),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_24", pos1),
        (overlay_set_val, "$g_presentation_obj_24", "$g_misc_merchant_faction_itp_type_polearm"),

        (create_number_box_overlay, "$g_presentation_obj_25", 0, 31),
        (position_set_y, pos1, 301),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_25", pos1),
        (overlay_set_val, "$g_presentation_obj_25", "$g_misc_merchant_faction_itp_type_shield"),

        (create_number_box_overlay, "$g_presentation_obj_26", 0, 31),
        (position_set_y, pos1, 266),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_26", pos1),
        (overlay_set_val, "$g_presentation_obj_26", "$g_misc_merchant_faction_itp_type_bow"),

        (create_number_box_overlay, "$g_presentation_obj_27", 0, 31),
        (position_set_y, pos1, 231),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_27", pos1),
        (overlay_set_val, "$g_presentation_obj_27", "$g_misc_merchant_faction_itp_type_crossbow"),

        (create_number_box_overlay, "$g_presentation_obj_28", 0, 31),
        (position_set_y, pos1, 196),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_28", pos1),
        (overlay_set_val, "$g_presentation_obj_28", "$g_misc_merchant_faction_itp_type_thrown"),

        (create_number_box_overlay, "$g_presentation_obj_29", 0, 31),
        (position_set_y, pos1, 161),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_29", pos1),
        (overlay_set_val, "$g_presentation_obj_29", "$g_misc_merchant_faction_itp_type_arrows"),

        (create_number_box_overlay, "$g_presentation_obj_30", 0, 31),
        (position_set_y, pos1, 126),   #####TAKE 14 OUT OF attached y
        (overlay_set_position, "$g_presentation_obj_30", pos1),
        (overlay_set_val, "$g_presentation_obj_30", "$g_misc_merchant_faction_itp_type_bolts"),



########################### RESET
        (create_game_button_overlay, "$g_presentation_obj_31", "@Reset"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_31", pos1),



######################################### DONE
        (create_game_button_overlay, "$g_presentation_obj_32", "@Done"),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_32", pos1),

      ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_misc_merchant_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_misc_merchant_itp_type_goods", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_misc_merchant_itp_type_body_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_misc_merchant_itp_type_head_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_misc_merchant_itp_type_foot_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_misc_merchant_itp_type_hand_armor", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_misc_merchant_itp_type_one_handed_wpn", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_misc_merchant_itp_type_two_handed_wpn", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_9"),
          (assign, "$g_misc_merchant_itp_type_polearm", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_misc_merchant_itp_type_shield", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (assign, "$g_misc_merchant_itp_type_bow", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (assign, "$g_misc_merchant_itp_type_crossbow", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (assign, "$g_misc_merchant_itp_type_thrown", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (assign, "$g_misc_merchant_itp_type_arrows", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (assign, "$g_misc_merchant_itp_type_bolts", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_16"),
          (assign, "$g_misc_merchant_itp_type_horse", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_17"),
          (assign, "$g_misc_merchant_faction_itp_type_horse", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_18"),
          (assign, "$g_misc_merchant_faction_itp_type_body_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_19"),
          (assign, "$g_misc_merchant_faction_itp_type_head_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_20"),
          (assign, "$g_misc_merchant_faction_itp_type_foot_armor", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_21"),
          (assign, "$g_misc_merchant_faction_itp_type_hand_armor", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_22"),
          (assign, "$g_misc_merchant_faction_itp_type_one_handed_wpn", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_23"),
          (assign, "$g_misc_merchant_faction_itp_type_two_handed_wpn", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_24"),
          (assign, "$g_misc_merchant_faction_itp_type_polearm", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_25"),
          (assign, "$g_misc_merchant_faction_itp_type_shield", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_26"),
          (assign, "$g_misc_merchant_faction_itp_type_bow", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_27"),
          (assign, "$g_misc_merchant_faction_itp_type_crossbow", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_28"),
          (assign, "$g_misc_merchant_faction_itp_type_thrown", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_29"),
          (assign, "$g_misc_merchant_faction_itp_type_arrows", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_30"),
          (assign, "$g_misc_merchant_faction_itp_type_bolts", ":value"),


        (else_try),
          (eq, ":object", "$g_presentation_obj_31"),
          ############# resets everything to default values
          (assign, "$g_misc_merchant_respawn_rate", 72),

          (assign, "$g_misc_merchant_itp_type_goods", 35),

          (assign, "$g_misc_merchant_itp_type_body_armor", 6),
          (assign, "$g_misc_merchant_itp_type_head_armor", 6),
          (assign, "$g_misc_merchant_itp_type_foot_armor", 4),
          (assign, "$g_misc_merchant_itp_type_hand_armor", 3),

          (assign, "$g_misc_merchant_itp_type_one_handed_wpn", 2),
          (assign, "$g_misc_merchant_itp_type_two_handed_wpn", 2),
          (assign, "$g_misc_merchant_itp_type_polearm", 2),
          (assign, "$g_misc_merchant_itp_type_shield", 2),
          (assign, "$g_misc_merchant_itp_type_bow", 2),
          (assign, "$g_misc_merchant_itp_type_crossbow", 2),
          (assign, "$g_misc_merchant_itp_type_thrown", 1),
          (assign, "$g_misc_merchant_itp_type_arrows", 1),
          (assign, "$g_misc_merchant_itp_type_bolts", 1),

          (assign, "$g_misc_merchant_itp_type_horse", 8),
          (assign, "$g_misc_merchant_faction_itp_type_horse", 16),

          (assign, "$g_misc_merchant_faction_itp_type_body_armor", 12),
          (assign, "$g_misc_merchant_faction_itp_type_head_armor", 12),
          (assign, "$g_misc_merchant_faction_itp_type_foot_armor", 8),
          (assign, "$g_misc_merchant_faction_itp_type_hand_armor", 5),

          (assign, "$g_misc_merchant_faction_itp_type_one_handed_wpn", 10),
          (assign, "$g_misc_merchant_faction_itp_type_two_handed_wpn", 6),
          (assign, "$g_misc_merchant_faction_itp_type_polearm", 8),
          (assign, "$g_misc_merchant_faction_itp_type_shield", 8),
          (assign, "$g_misc_merchant_faction_itp_type_bow", 4),
          (assign, "$g_misc_merchant_faction_itp_type_crossbow", 4),
          (assign, "$g_misc_merchant_faction_itp_type_thrown", 4),
          (assign, "$g_misc_merchant_faction_itp_type_arrows", 4),
          (assign, "$g_misc_merchant_faction_itp_type_bolts", 4),


          (presentation_set_duration, 0),



        (else_try),
          (eq, ":object", "$g_presentation_obj_32"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################






####################################### NEW v2.1 - MISC OPTIONS
  ("enhanced_mod_options_misc", 0, mesh_load_window, [
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

        (create_text_overlay, reg0, "@Lord battle death chance:", tf_vertical_align_center),
        (store_sub, reg1, 700, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@King battle death chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lord assassination chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@King assassination chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lord base execution chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@King execution chance value:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lord execution chance faction relation divider:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Random lord creation rate:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Random lord creation (minimum lords):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Random lord creation (town threshold):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Random lord creation (castle threshold):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Random lord creation (village threshold):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Crusade daily percent chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        ######## checkbox
        (create_text_overlay, reg0, "@Don't disband town garrison when taking control of it:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
        ########

        (create_text_overlay, reg0, "@Tavern mercenary respawn rate:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Tavern mercenary minimum:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Tavern mercenary maximum:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
        ###################


########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 420),
        (assign, ":value_difference", 35),

        (create_number_box_overlay, "$g_presentation_obj_1", 0, 101),
        (store_sub, reg1, 686, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_lord_death_chance_battle"),

        (create_number_box_overlay, "$g_presentation_obj_2", 0, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_lord_death_chance_battle_king"),


        (create_number_box_overlay, "$g_presentation_obj_3", 0, 1001),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_lord_death_chance_assassination"),


        (create_number_box_overlay, "$g_presentation_obj_4", 0, 1001),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_lord_death_chance_assassination_king"),


        (create_number_box_overlay, "$g_presentation_obj_5", 0, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_lord_death_chance_execution_base"),

        (create_number_box_overlay, "$g_presentation_obj_6", -100, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_lord_death_chance_execution_king_variation"),


        (create_number_box_overlay, "$g_presentation_obj_7", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_7", pos1),
        (overlay_set_val, "$g_presentation_obj_7", "$g_lord_death_chance_execution_relation_divider"),

        (create_number_box_overlay, "$g_presentation_obj_8", 0, 721),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_8", pos1),
        (overlay_set_val, "$g_presentation_obj_8", "$g_lord_creation_rate"),


        (create_number_box_overlay, "$g_presentation_obj_9", 0, 6),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_9", pos1),
        (overlay_set_val, "$g_presentation_obj_9", "$g_lord_creation_minimum"),



        (create_number_box_overlay, "$g_presentation_obj_10", 0, 6),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_10", pos1),
        (overlay_set_val, "$g_presentation_obj_10", "$g_lord_creation_threshold_towns"),


        (create_number_box_overlay, "$g_presentation_obj_11", 0, 6),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_11", pos1),
        (overlay_set_val, "$g_presentation_obj_11", "$g_lord_creation_threshold_castles"),


        (create_number_box_overlay, "$g_presentation_obj_12", 0, 6),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_12", pos1),
        (overlay_set_val, "$g_presentation_obj_12", "$g_lord_creation_threshold_villages"),

        (create_number_box_overlay, "$g_presentation_obj_13", 0, 401),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_13", pos1),
        (overlay_set_val, "$g_presentation_obj_13", "$g_misc_crusade_daily_chance"),

        (create_check_box_overlay, "$g_presentation_obj_14", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_14", pos1),
        (overlay_set_val, "$g_presentation_obj_14", "$g_misc_garrison_dont_disband_troops_when_taking_control"),


        (create_number_box_overlay, "$g_presentation_obj_15", 4, 1000),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_15", pos1),
        (overlay_set_val, "$g_presentation_obj_15", "$g_misc_tavern_mercenaries_respawn_rate"),

        (create_number_box_overlay, "$g_presentation_obj_16", 1, 100),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_16", pos1),
        (overlay_set_val, "$g_presentation_obj_16", "$g_misc_tavern_mercenaries_min"),

        (create_number_box_overlay, "$g_presentation_obj_17", 1, 100),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_17", pos1),
        (overlay_set_val, "$g_presentation_obj_17", "$g_misc_tavern_mercenaries_max"),

        # (position_set_y, pos1, 166),
        # (create_check_box_overlay, "$g_presentation_obj_16", "mesh_checkbox_off", "mesh_checkbox_on"),
        # (overlay_set_position, "$g_presentation_obj_16", pos1),
        # (overlay_set_val, "$g_presentation_obj_16", "$g_party_npc_trainer"),

        # (position_set_y, pos1, 136),
        # (create_check_box_overlay, "$g_presentation_obj_17", "mesh_checkbox_off", "mesh_checkbox_on"),
        # (overlay_set_position, "$g_presentation_obj_17", pos1),
        # (overlay_set_val, "$g_presentation_obj_17", "$g_prison_culling"),



########################################## ROW 2 COLUMN 1
        # (position_set_x, pos1, 520),
        (position_set_x, pos1, 510),
        (assign, ":value_difference", 35),

        (create_text_overlay, reg0, "@Troop ratio bar and kill count options:", tf_vertical_align_center),
        (store_sub, reg1, 700, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Max tax innefficiency:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Faction diplomacy rate:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Disable player weekly morale loss (0.5%):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Make parties drop their prisoners to a walled fief:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Civil War chance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Civil War rate:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Civil war lords needed (percent):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Player receives landowner money directly:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Use Native wage system:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Freelancer unequips items when upgrading:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        ########## NEW v2.8
        (create_text_overlay, reg0, "@Cheat menu on:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
        ##########

        ########## NEW v3.5
        (create_text_overlay, reg0, "@Report projectile hit distance:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
        ##########

        # (create_text_overlay, reg0, "@Remove deserter recruit penalty:", tf_vertical_align_center),
        # (position_set_y, pos1, 525),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Max tax inefficiency:", tf_vertical_align_center),
        # (position_set_y, pos1, 490),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 455),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 420),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Prisoners per point of prisoner management:", tf_vertical_align_center),
        # (position_set_y, pos1, 385),
        # (overlay_set_position, reg0, pos1),


########################################## ROW 2 COLUMN 2
        (position_set_x, pos1, 900),
        (assign, ":value_difference", 35),

        # (create_number_box_overlay, "$g_presentation_obj_18", 0, 1000),
        # (position_set_y, pos1, 690),   #####TAKE 14 OUT OF attached y
        # (overlay_set_position, "$g_presentation_obj_18", pos1),
        # (overlay_set_val, "$g_presentation_obj_18", "$g_party_morale_per_leadership"),

        (create_button_overlay, "$g_presentation_obj_18", "@Show:"),
        (try_begin),
          (eq, "$g_misc_troop_ratio_bar_and_kill_count", 0), #disabled
          (overlay_set_text, "$g_presentation_obj_18", "@None"),
        (else_try),
          (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1), #kill count
          (overlay_set_text, "$g_presentation_obj_18", "@Kill count"),
        (else_try),
          (eq, "$g_misc_troop_ratio_bar_and_kill_count", 2),  #troop ratio bar
          (overlay_set_text, "$g_presentation_obj_18", "@Troop ratio bar"),
        (else_try),
          (eq, "$g_misc_troop_ratio_bar_and_kill_count", 3),  #kill count and troop ratio bar
          (overlay_set_text, "$g_presentation_obj_18", "@Both"),
        (else_try),
          (overlay_set_text, "$g_presentation_obj_24", "@Oy! we have a problem!"),
        (try_end),
        (store_sub, reg1, 690, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_18", pos1),
        # (overlay_set_val, "$g_presentation_obj_18", "$g_misc_troop_ratio_bar_and_kill_count"),


        (create_number_box_overlay, "$g_presentation_obj_19", 0, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_19", pos1),
        (overlay_set_val, "$g_presentation_obj_19", "$g_misc_max_tax_inneficiency"),

        (create_number_box_overlay, "$g_presentation_obj_20", 24, 721),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_20", pos1),
        (overlay_set_val, "$g_presentation_obj_20", "$g_misc_faction_diplomacy_rate"),

        (create_check_box_overlay, "$g_presentation_obj_21", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_21", pos1),
        (overlay_set_val, "$g_presentation_obj_21", "$g_misc_disable_renown_weekly_reduction"),

        (create_check_box_overlay, "$g_presentation_obj_22", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_22", pos1),
        (overlay_set_val, "$g_presentation_obj_22", "$g_misc_parties_drop_prisoners_to_walled_fief"),

        (create_number_box_overlay, "$g_presentation_obj_23", 0, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_23", pos1),
        (overlay_set_val, "$g_presentation_obj_23", "$g_misc_civil_war_chance"),

        (create_number_box_overlay, "$g_presentation_obj_24", 72, 721),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_24", pos1),
        (overlay_set_val, "$g_presentation_obj_24", "$g_misc_civil_war_rate"),

        (create_number_box_overlay, "$g_presentation_obj_25", 0, 91),  #### Max 90 - king needs to be exempt
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_25", pos1),
        (overlay_set_val, "$g_presentation_obj_25", "$g_misc_civil_war_lords_required"),

        (create_check_box_overlay, "$g_presentation_obj_26", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_26", pos1),
        (overlay_set_val, "$g_presentation_obj_26", "$g_misc_floris_bank_receive_directly"),

        (create_check_box_overlay, "$g_presentation_obj_27", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_27", pos1),
        (overlay_set_val, "$g_presentation_obj_27", "$native_wages"),

        (create_check_box_overlay, "$g_presentation_obj_28", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_28", pos1),
        (overlay_set_val, "$g_presentation_obj_28", "$ee_freelancer_upgrade_unequip"),

		########### NEW v2.8 - cheat menu
        (create_check_box_overlay, "$g_presentation_obj_29", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_29", pos1),
        (overlay_set_val, "$g_presentation_obj_29", "$cheat_mode"),
        ######################

		########### NEW v3.5 - cheat menu
        (create_check_box_overlay, "$g_presentation_obj_30", "mesh_checkbox_off", "mesh_checkbox_on"),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_30", pos1),
        (overlay_set_val, "$g_presentation_obj_30", "$g_report_shot"),
        ######################


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

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_lord_death_chance_battle", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_lord_death_chance_battle_king", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_lord_death_chance_assassination", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_lord_death_chance_assassination_king", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_lord_death_chance_execution_base", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_lord_death_chance_execution_king_variation", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_7"),
          (assign, "$g_lord_death_chance_execution_relation_divider", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_8"),
          (assign, "$g_lord_creation_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_9"),
          (assign, "$g_lord_creation_minimum", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_10"),
          (assign, "$g_lord_creation_threshold_towns", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_11"),
          (assign, "$g_lord_creation_threshold_castles", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_12"),
          (assign, "$g_lord_creation_threshold_villages", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_13"),
          (assign, "$g_misc_crusade_daily_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_14"),
          (assign, "$g_misc_garrison_dont_disband_troops_when_taking_control", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_15"),
          (assign, "$g_misc_tavern_mercenaries_respawn_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_16"),
          (assign, "$g_misc_tavern_mercenaries_min", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_17"),
          (assign, "$g_misc_tavern_mercenaries_max", ":value"),
          (try_begin),  #### NEW v1.0 - bugfix
            (lt, "$g_misc_tavern_mercenaries_max", "$g_misc_tavern_mercenaries_min"),
            (assign, "$g_misc_tavern_mercenaries_max", "$g_misc_tavern_mercenaries_min"),
          (try_end),

        (else_try),
          (eq, ":object", "$g_presentation_obj_18"),
          (val_sub, "$g_misc_troop_ratio_bar_and_kill_count", 1),
          (try_begin),
            (eq, "$g_misc_troop_ratio_bar_and_kill_count", -1),
            (assign, "$g_misc_troop_ratio_bar_and_kill_count", 3),
          (try_end),
          (try_begin),
            (eq, "$g_misc_troop_ratio_bar_and_kill_count", 0), #disabled
            (overlay_set_text, "$g_presentation_obj_18", "@None"),
          (else_try),
            (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1), #kill count
            (overlay_set_text, "$g_presentation_obj_18", "@Kill count"),
          (else_try),
            (eq, "$g_misc_troop_ratio_bar_and_kill_count", 2),  #troop ratio bar
            (overlay_set_text, "$g_presentation_obj_18", "@Troop ratio bar"),
          (else_try),
            (eq, "$g_misc_troop_ratio_bar_and_kill_count", 3),  #kill count and troop ratio bar
            (overlay_set_text, "$g_presentation_obj_18", "@Both"),
          (else_try),
            (overlay_set_text, "$g_presentation_obj_24", "@Oy! we have a problem!"),
          (try_end),
        (else_try),
          (eq, ":object", "$g_presentation_obj_19"),
          (assign, "$g_misc_max_tax_inneficiency", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_20"),
          (assign, "$g_misc_faction_diplomacy_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_21"),
          (assign, "$g_misc_disable_renown_weekly_reduction", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_22"),
          (assign, "$g_misc_parties_drop_prisoners_to_walled_fief", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_23"),
          (assign, "$g_misc_civil_war_chance", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_24"),
          (assign, "$g_misc_civil_war_rate", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_25"),
          (assign, "$g_misc_civil_war_lords_required", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_26"),
          (assign, "$g_misc_floris_bank_receive_directly", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_27"),
          (assign, "$native_wages", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_28"),
          (assign, "$ee_freelancer_upgrade_unequip", ":value"),
		############### NEW v2.8
        (else_try),
          (eq, ":object", "$g_presentation_obj_29"),
          (assign, "$cheat_mode", ":value"),
        ###############
		############### NEW v3.5
        (else_try),
          (eq, ":object", "$g_presentation_obj_30"),
          (assign, "$g_report_shot", ":value"),
        ###############


        (else_try),
          (eq, ":object", "$g_presentation_obj_32"),
          ############# resets everything to default values
          (assign, "$g_lord_death_chance_battle", 30),
          (assign, "$g_lord_death_chance_battle_king", 15),
          (assign, "$g_lord_death_chance_assassination", 4), ### 1%
          (assign, "$g_lord_death_chance_assassination_king", 2),   ### 0.5%
          (assign, "$g_lord_death_chance_execution_base", 10),
          (assign, "$g_lord_death_chance_execution_king_variation", 10),
          (assign, "$g_lord_death_chance_execution_relation_divider", 3),
          (assign, "$g_lord_creation_rate", 120),
          (assign, "$g_lord_creation_minimum", 3),
          (assign, "$g_lord_creation_threshold_towns", 1),
          (assign, "$g_lord_creation_threshold_castles", 1),
          (assign, "$g_lord_creation_threshold_villages", 2),
          (assign, "$g_misc_crusade_daily_chance", 8),
          (assign, "$g_misc_garrison_dont_disband_troops_when_taking_control", 1),
          (assign, "$g_misc_troop_ratio_bar_and_kill_count", 3),

          (assign, "$g_misc_tavern_mercenaries_respawn_rate", 36),
          (assign, "$g_misc_tavern_mercenaries_min", 4),
          (assign, "$g_misc_tavern_mercenaries_max", 10),

          (assign, "$g_misc_max_tax_inneficiency", 65),
          (assign, "$g_misc_faction_diplomacy_rate", 336),
          (assign, "$g_misc_disable_renown_weekly_reduction", 0),
          (assign, "$g_misc_parties_drop_prisoners_to_walled_fief", 0),
          (assign, "$g_misc_civil_war_chance", 30),
          (assign, "$g_misc_civil_war_rate", 168),
          (assign, "$g_misc_civil_war_lords_required", 40),
          (assign, "$g_misc_floris_bank_receive_directly", 1),
          (assign, "$native_wages", 0),  ### disabled by default
          (assign, "$ee_freelancer_upgrade_unequip", 0),  ### disabled by default
          (assign, "$cheat_mode", 0),
          (assign, "$g_report_shot", 1),  ######### NEW v3.5
          (presentation_set_duration, 0),

        (else_try),
          (eq, ":object", "$g_presentation_obj_33"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################





####################################### NEW v3.8 - MISC OPTIONS #2
  ("enhanced_mod_options_misc_2", 0, mesh_load_window, [
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
		
########################################## ROW 1 COLUMN 1
        (position_set_x, pos1, 50),
        (assign, ":value_difference", 35),

        (create_text_overlay, reg0, "@Custom troop proficiency per level:", tf_vertical_align_center),
        (store_sub, reg1, 700, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@CT proficiency per weapon master level:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@CT proficiency per agility:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@CT skill points base:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@CT budget per level:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Attribute points base:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),


        ######## checkbox
        # (create_text_overlay, reg0, "@Don't disband town garrison when taking control of it:", tf_vertical_align_center),
        # (val_sub, reg1, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, reg0, pos1),
        ########

        ###################


########################################## ROW 1 COLUMN 2
       ######  number boxes
        (position_set_x, pos1, 420),
        (assign, ":value_difference", 35),

        (create_number_box_overlay, "$g_presentation_obj_1", 1, 101),
        (store_sub, reg1, 686, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        (overlay_set_val, "$g_presentation_obj_1", "$g_cstm_proficiency_points_per_level"),

        (create_number_box_overlay, "$g_presentation_obj_2", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_2", pos1),
        (overlay_set_val, "$g_presentation_obj_2", "$g_cstm_proficiency_per_wm"),


        (create_number_box_overlay, "$g_presentation_obj_3", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_3", pos1),
        (overlay_set_val, "$g_presentation_obj_3", "$g_cstm_proficiency_per_agility"),


        (create_number_box_overlay, "$g_presentation_obj_4", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_4", pos1),
        (overlay_set_val, "$g_presentation_obj_4", "$g_cstm_skill_points_start"),


        (create_number_box_overlay, "$g_presentation_obj_5", 1, 10000),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_5", pos1),
        (overlay_set_val, "$g_presentation_obj_5", "$g_cstm_budget_per_level"),


        (create_number_box_overlay, "$g_presentation_obj_6", 1, 101),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, "$g_presentation_obj_6", pos1),
        (overlay_set_val, "$g_presentation_obj_6", "$g_cstm_attribute_points_start"),

        # (position_set_y, pos1, 166),
        # (create_check_box_overlay, "$g_presentation_obj_16", "mesh_checkbox_off", "mesh_checkbox_on"),
        # (overlay_set_position, "$g_presentation_obj_16", pos1),
        # (overlay_set_val, "$g_presentation_obj_16", "$g_party_npc_trainer"),


########################################## ROW 2 COLUMN 1
        # (position_set_x, pos1, 520),
        # (position_set_x, pos1, 510),
        # (assign, ":value_difference", 35),

        # (create_text_overlay, reg0, "@Troop ratio bar and kill count options:", tf_vertical_align_center),
        # (store_sub, reg1, 700, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Max tax innefficiency:", tf_vertical_align_center),
        # (val_sub, reg1, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, reg0, pos1),


########################################## ROW 2 COLUMN 2
        # (position_set_x, pos1, 900),
        # (assign, ":value_difference", 35),

        # (create_number_box_overlay, "$g_presentation_obj_18", 0, 1000),
        # (position_set_y, pos1, 690),   #####TAKE 14 OUT OF attached y
        # (overlay_set_position, "$g_presentation_obj_18", pos1),
        # (overlay_set_val, "$g_presentation_obj_18", "$g_party_morale_per_leadership"),

        # (create_button_overlay, "$g_presentation_obj_18", "@Show:"),
        # (try_begin),
          # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 0), #disabled
          # (overlay_set_text, "$g_presentation_obj_18", "@None"),
        # (else_try),
          # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 1), #kill count
          # (overlay_set_text, "$g_presentation_obj_18", "@Kill count"),
        # (else_try),
          # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 2),  #troop ratio bar
          # (overlay_set_text, "$g_presentation_obj_18", "@Troop ratio bar"),
        # (else_try),
          # (eq, "$g_misc_troop_ratio_bar_and_kill_count", 3),  #kill count and troop ratio bar
          # (overlay_set_text, "$g_presentation_obj_18", "@Both"),
        # (else_try),
          # (overlay_set_text, "$g_presentation_obj_24", "@Oy! we have a problem!"),
        # (try_end),
        # (store_sub, reg1, 690, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, "$g_presentation_obj_18", pos1),
        # (overlay_set_val, "$g_presentation_obj_18", "$g_misc_troop_ratio_bar_and_kill_count"),

		########### NEW v3.5 - report shot
        # (create_check_box_overlay, "$g_presentation_obj_30", "mesh_checkbox_off", "mesh_checkbox_on"),
        # (val_sub, reg1, ":value_difference"),
        # (position_set_y, pos1, reg1),
        # (overlay_set_position, "$g_presentation_obj_30", pos1),
        # (overlay_set_val, "$g_presentation_obj_30", "$g_report_shot"),
        ######################


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

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (assign, "$g_cstm_proficiency_points_per_level", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_cstm_proficiency_per_wm", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_3"),
          (assign, "$g_cstm_proficiency_per_agility", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_4"),
          (assign, "$g_cstm_skill_points_start", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_5"),
          (assign, "$g_cstm_budget_per_level", ":value"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_6"),
          (assign, "$g_cstm_attribute_points_start", ":value"),

        (else_try),
          (eq, ":object", "$g_presentation_obj_32"),
          ############# resets everything to default values
          (assign, "$g_cstm_proficiency_points_per_level", 20),
          (assign, "$g_cstm_proficiency_per_wm", 15),
          (assign, "$g_cstm_proficiency_per_agility", 10), 
          (assign, "$g_cstm_skill_points_start", 1),   
          (assign, "$g_cstm_budget_per_level", 900),
          (assign, "$g_cstm_attribute_points_start", 20),
          (presentation_set_duration, 0),

        (else_try),
          (eq, ":object", "$g_presentation_obj_33"),
          (presentation_set_duration, 0),
        (try_end),
      ]),
    ]),
##############################################################################










################################ NEW v1.9 - kill count and troop ratio bar
  # ("troop_ratio_bar", prsntf_read_only, mesh_null,
  ("troop_ratio_bar", prsntf_read_only, 0,
  [
    (ti_on_presentation_load,
    [
      (presentation_set_duration, 999999),
      (assign, "$presentation_troop_ratio_bar_active", 1),
      (set_fixed_point_multiplier, 1000),
      (create_mesh_overlay, "$g_presentation_obj_1", "mesh_status_troop_ratio_bar"),
      (overlay_set_alpha, "$g_presentation_obj_1", 0x33),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_position, "$g_presentation_obj_1", pos1),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 713),
      (create_mesh_overlay, "$g_presentation_obj_2", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_2", 0xAA1F1F),
      (overlay_set_position, "$g_presentation_obj_2", pos1),
      (create_mesh_overlay, "$g_presentation_obj_3", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_3", 0x1F1FAA),
      (overlay_set_position, "$g_presentation_obj_3", pos1),
      (create_mesh_overlay, "$g_presentation_obj_4", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_4", 0x1FAA1F),
      (overlay_set_position, "$g_presentation_obj_4", pos1),
      (create_mesh_overlay, "$g_presentation_obj_7", "mesh_status_troop_ratio_bar_button"),
      (create_mesh_overlay, "$g_presentation_obj_8", "mesh_status_troop_ratio_bar_button"),
    ]),
    (ti_on_presentation_run,
    [
      (store_trigger_param_1, ":var0"),
      (set_fixed_point_multiplier, 1000),
      (assign, ":var1", 0),
      (assign, ":var2", 0),
      (assign, ":var3", 0),
      (assign, ":var4", 0),
      (try_begin),
        (neq, "$g_option_ratio_bar_is_global", 1),
        (try_for_agents, ":var5"),
          (agent_is_human, ":var5"),
          (agent_is_alive, ":var5"),
          (agent_get_party_id, ":var6", ":var5"),
          (try_begin),
            (eq, ":var6", "p_main_party"),
            (val_add, ":var1", 1),
          (else_try),
            (agent_is_ally, ":var5"),
            (val_add, ":var2", 1),
          (else_try),
            (val_add, ":var3", 1),
          (try_end),
        (try_end),
      (else_try),
        (assign, ":var1", "$player_count_alive"),
        (assign, ":var2", "$ally_count_alive"),
        (assign, ":var3", "$enemy_count_alive"),
      (try_end),
      (val_add, ":var4", ":var1"),
      (val_add, ":var4", ":var2"),
      (val_add, ":var4", ":var3"),
      (position_set_x, pos1, 12000),
      (position_set_y, pos1, 300),
      (overlay_set_size, "$g_presentation_obj_2", pos1),
      (store_add, ":var7", ":var1", ":var2"),
      (val_mul, ":var7", 12000),
      (val_div, ":var7", ":var4"),
      (position_set_x, pos1, ":var7"),
      (position_set_y, pos1, 300),
      (overlay_set_size, "$g_presentation_obj_3", pos1),
      (store_mul, ":var8", ":var1", 12000),
      (val_div, ":var8", ":var4"),
      (position_set_x, pos1, ":var8"),
      (position_set_y, pos1, 300),
      (overlay_set_size, "$g_presentation_obj_4", pos1),
      (store_add, ":var9", ":var1", ":var2"),
      (val_mul, ":var9", 910),
      (val_div, ":var9", ":var4"),
      (val_add, ":var9", 705),
      (position_set_x, pos1, ":var9"),
      (position_set_y, pos1, 700),
      (overlay_set_position, "$g_presentation_obj_7", pos1),
      (store_mul, ":var10", ":var1", 240),
      (val_div, ":var10", ":var4"),
      (val_add, ":var10", 705),
      (position_set_x, pos1, ":var10"),
      (position_set_y, pos1, 700),
      (overlay_set_position, "$g_presentation_obj_8", pos1),
      (try_begin),
        (eq, "$presentation_troop_ratio_bar_active", 1),
        (gt, ":var0", 200),
        (game_key_clicked, gk_view_orders),
        (assign, "$presentation_troop_ratio_bar_active", 0),
        (presentation_set_duration, 0),
        (start_presentation, "prsnt_battle"),
      (try_end),
    ]),
  ]),



  # ("killcount", prsntf_read_only, mesh_null,
  ("killcount", prsntf_read_only, 0,
  [
    (ti_on_presentation_load,
    [
      (presentation_set_duration, 999999),
      (set_fixed_point_multiplier, 1000),
      (get_player_agent_no, ":var0"),
      (agent_get_horse, ":var1", ":var0"),
      (troop_get_inventory_slot, ":var2", "trp_player", ek_horse),
      (try_begin),
        (ge, ":var2", 0),
        (neg|is_between, "$g_encountered_party", walled_centers_begin, walled_centers_end),
        (neg|is_between, "$g_encountered_party_2", walled_centers_begin, walled_centers_end),
        (neq, "$g_encounter_type", 1),
        (neq, "$g_encounter_type", 2),
        (party_get_template_id, ":var3", "$g_encountered_party"),
        (neg|is_between, ":var3", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"),
        (lt, ":var1", 0),
      (else_try),
        (assign, "$killcount_player_horse", ":var1"),
      (try_end),
      (str_store_string, s1, "@0 kills"),
      (create_text_overlay, "$g_presentation_obj_1", s1),
      (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),
      (position_set_x, pos1, 5),
      (position_set_y, pos1, 710),
      (overlay_set_position, "$g_presentation_obj_1", pos1),
      (create_mesh_overlay, "$g_presentation_killcountbg", "mesh_killcount"),
      (position_set_x, pos2, 0),
      (position_set_y, pos2, 768),
      (overlay_set_position, "$g_presentation_killcountbg", pos2),
    ]),
    (ti_on_presentation_run,
    [
      (try_begin),
        (game_key_clicked, gk_view_orders),
        (presentation_set_duration, 0),
        (start_presentation, "prsnt_battle"),
      (else_try),
        (get_player_agent_no, ":var0"),
        (agent_get_kill_count, reg0, ":var0"),
        (agent_get_kill_count, reg1, ":var0", 1),
        (store_add, reg3, reg0, reg1),
        (try_begin),
          (gt, "$killcount_player_horse", 0),
          (agent_get_kill_count, reg7, "$killcount_player_horse", 1),
          (val_add, reg3, reg7),
          (agent_get_kill_count, reg8, "$killcount_player_horse"),
          (val_add, reg3, reg8),
        (else_try),
          (assign, reg7, 0),
          (assign, reg8, 0),
        (try_end),
        (try_begin),
          (eq, reg3, 1),
          (str_store_string, s1, "@{reg3} kill"),
        (else_try),
          (str_store_string, s1, "@{reg3} kills"),
        (try_end),
        (assign, "$current_killcount", reg0),
        (val_add, "$current_killcount", reg8),
        (assign, "$current_woundcount", reg1),
        (val_add, "$current_woundcount", reg7),
        (overlay_set_text, "$g_presentation_obj_1", s1),
        (assign, reg25, "$killcount_player_horse"),
        (assign, reg26, ":var0"),
      (try_end),
    ]),
  ]),




  # ("killcount_and_troop_ratio_bar", prsntf_read_only, mesh_null,
  ("killcount_and_troop_ratio_bar", prsntf_read_only, 0,
  [
    (ti_on_presentation_load,
    [
      (presentation_set_duration, 999999),
      (set_fixed_point_multiplier, 1000),
      (get_player_agent_no, ":var0"),
      (agent_get_horse, ":var1", ":var0"),
      (troop_get_inventory_slot, ":var2", "trp_player", ek_horse),
      (try_begin),
        (ge, ":var2", 0),
        (neg|is_between, "$g_encountered_party", walled_centers_begin, walled_centers_end),
        (neg|is_between, "$g_encountered_party_2", walled_centers_begin, walled_centers_end),
        (neq, "$g_encounter_type", 1),
        (neq, "$g_encounter_type", 2),
        (party_get_template_id, ":var3", "$g_encountered_party"),
        (neg|is_between, ":var3", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"),
        (lt, ":var1", 0),
      (else_try),
        (assign, "$killcount_player_horse", ":var1"),
      (try_end),
      (str_store_string, s1, "@0 kills"),
      (create_text_overlay, "$g_presentation_obj_9", s1),
      (overlay_set_color, "$g_presentation_obj_9", 0xFFFFFF),
      (position_set_x, pos1, 5),
      (position_set_y, pos1, 710),
      (overlay_set_position, "$g_presentation_obj_9", pos1),
      (create_mesh_overlay, "$g_presentation_killcountbg", "mesh_killcount"),
      (position_set_x, pos2, 0),
      (position_set_y, pos2, 768),
      (overlay_set_position, "$g_presentation_killcountbg", pos2),
      (assign, "$presentation_troop_ratio_bar_active", 1),
      (create_mesh_overlay, "$g_presentation_obj_1", "mesh_status_troop_ratio_bar"),
      (overlay_set_alpha, "$g_presentation_obj_1", 0x33),
      (position_set_x, pos10, 700),
      (position_set_y, pos10, 700),
      (overlay_set_position, "$g_presentation_obj_1", pos10),
      (position_set_x, pos10, 705),
      (position_set_y, pos10, 713),
      (create_mesh_overlay, "$g_presentation_obj_2", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_2", 0xAA1F1F),
      (overlay_set_position, "$g_presentation_obj_2", pos10),
      (create_mesh_overlay, "$g_presentation_obj_3", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_3", 0x1F1FAA),
      (overlay_set_position, "$g_presentation_obj_3", pos10),
      (create_mesh_overlay, "$g_presentation_obj_4", "mesh_white_plane"),
      (overlay_set_color, "$g_presentation_obj_4", 0x1FAA1F),
      (overlay_set_position, "$g_presentation_obj_4", pos10),
      (create_mesh_overlay, "$g_presentation_obj_7", "mesh_status_troop_ratio_bar_button"),
      (create_mesh_overlay, "$g_presentation_obj_8", "mesh_status_troop_ratio_bar_button"),
      (call_script, "script_collect_friendly_parties"),
    ]),
    (ti_on_presentation_run,
    [
      (store_trigger_param_1, ":var0"),
      (set_fixed_point_multiplier, 1000),
      (assign, ":var1", 0),
      (assign, ":var2", 0),
      (assign, ":var3", 0),
      (assign, ":var4", 0),
      (try_begin),
        (neq, "$g_option_ratio_bar_is_global", 1),
        (try_for_agents, ":var5"),
          (agent_is_human, ":var5"),
          (agent_is_alive, ":var5"),
          (agent_get_party_id, ":var6", ":var5"),
          (try_begin),
            (eq, ":var6", "p_main_party"),
            (val_add, ":var1", 1),
          (else_try),
            (agent_is_ally, ":var5"),
            (val_add, ":var2", 1),
          (else_try),
            (val_add, ":var3", 1),
          (try_end),
        (try_end),
      (else_try),
        (assign, ":var1", "$player_count_alive"),
        (assign, ":var2", "$ally_count_alive"),
        (assign, ":var3", "$enemy_count_alive"),
      (try_end),
      (val_add, ":var4", ":var1"),
      (val_add, ":var4", ":var2"),
      (val_add, ":var4", ":var3"),
      (position_set_x, pos10, 12000),
      (position_set_y, pos10, 300),
      (overlay_set_size, "$g_presentation_obj_2", pos10),
      (store_add, ":var7", ":var1", ":var2"),
      (val_mul, ":var7", 12000),
      (val_div, ":var7", ":var4"),
      (position_set_x, pos10, ":var7"),
      (position_set_y, pos10, 300),
      (overlay_set_size, "$g_presentation_obj_3", pos10),
      (store_mul, ":var8", ":var1", 12000),
      (val_div, ":var8", ":var4"),
      (position_set_x, pos10, ":var8"),
      (position_set_y, pos10, 300),
      (overlay_set_size, "$g_presentation_obj_4", pos10),
      (store_add, ":var9", ":var1", ":var2"),
      (val_mul, ":var9", 910),
      (val_div, ":var9", ":var4"),
      (val_add, ":var9", 705),
      (position_set_x, pos10, ":var9"),
      (position_set_y, pos10, 700),
      (overlay_set_position, "$g_presentation_obj_7", pos10),
      (store_mul, ":var10", ":var1", 240),
      (val_div, ":var10", ":var4"),
      (val_add, ":var10", 705),
      (position_set_x, pos10, ":var10"),
      (position_set_y, pos10, 700),
      (overlay_set_position, "$g_presentation_obj_8", pos10),
      (try_begin),
        (eq, "$presentation_troop_ratio_bar_active", 1),
        (gt, ":var0", 200),
        (game_key_clicked, gk_view_orders),
        (assign, "$presentation_troop_ratio_bar_active", 0),
        (presentation_set_duration, 0),
        (start_presentation, "prsnt_battle"),
      (else_try),
        (get_player_agent_no, ":var11"),
        (agent_get_kill_count, reg0, ":var11"),
        (agent_get_kill_count, reg1, ":var11", 1),
        (store_add, reg3, reg0, reg1),
        (try_begin),
          (gt, "$killcount_player_horse", 0),
          (agent_get_kill_count, reg7, "$killcount_player_horse", 1),
          (val_add, reg3, reg7),
          (agent_get_kill_count, reg8, "$killcount_player_horse"),
          (val_add, reg3, reg8),
        (else_try),
          (assign, reg7, 0),
          (assign, reg8, 0),
        (try_end),
        (try_begin),
          (eq, reg3, 1),
          (str_store_string, s1, "@{reg3} kill"),
        (else_try),
          (str_store_string, s1, "@{reg3} kills"),
        (try_end),
        (assign, "$current_killcount", reg0),
        (val_add, "$current_killcount", reg8),
        (assign, "$current_woundcount", reg1),
        (val_add, "$current_woundcount", reg7),
        (overlay_set_text, "$g_presentation_obj_9", s1),
        (assign, reg25, "$killcount_player_horse"),
        (assign, reg26, ":var11"),
      (try_end),
    ]),
  ]),
##############################################################################





########################## NEW v2.1 - RUBIK'S PERFECT TROOP TREE PRESENTATION
 ("faction_troop_trees_1", 0, 0, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (create_mesh_overlay, reg1, "mesh_load_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),

        ## combo_button
        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 690),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        # factions
        (store_sub, ":num_factions", npc_cultures_end_1, npc_cultures_begin_1),
        (assign, ":num_pages", ":num_factions"),

        ## page names, from bottom to top
        # (overlay_add_item, "$g_presentation_obj_1", "@Others"),
        # (overlay_add_item, "$g_presentation_obj_1", "@Outlaws"),
        # (overlay_add_item, "$g_presentation_obj_1", "@Mercenary"),
        (try_for_range_backwards, ":page_no", 0, ":num_factions"),
          (store_add, ":faction_no", ":page_no", npc_cultures_begin_1),
          (str_store_faction_name, s0, ":faction_no"),
          (overlay_add_item, "$g_presentation_obj_1", s0),
        (try_end),
        (store_sub, ":presentation_obj_val", ":num_pages", "$g_selected_page"),
        (val_sub, ":presentation_obj_val", 1),
        (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),

        ## back
        (create_game_button_overlay, "$g_presentation_obj_2", "@Close"),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 685),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        ## tips
        (create_text_overlay, reg1, "@Click the center button to toggle faction^Click the avatars to view details of them", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg1, pos1),

        ## pic_arms
        # (try_begin),
          # (is_between, "$g_selected_page", 0, ":num_factions"),
          # (store_add, ":pic_arms", "mesh_pic_arms_swadian", "$g_selected_page"),
          # (create_mesh_overlay, reg1, ":pic_arms"),
          # (position_set_x, pos1, 120),
          # (position_set_y, pos1, 100),
          # (overlay_set_position, reg1, pos1),
          # (position_set_x, pos1, 300),
          # (position_set_y, pos1, 300),
          # (overlay_set_size, reg1, pos1),
        # (try_end),

        # detect_total_max_tier, calculate offset_x
        (assign, ":total_max_tier", 1),
        (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
          (neg|troop_is_hero, ":cur_troop"),
          # can upgrade
          (troop_get_upgrade_troop, ":upgrade_troop", ":cur_troop", 0),
          (gt, ":upgrade_troop", 0),
          # page_no_for_cur_troop
          (call_script, "script_get_page_no_of_troop_tree_for_troop_on_1", ":cur_troop"),
          (assign, ":page_no_for_cur_troop", reg0),
          # on current page_no
          (eq, ":page_no_for_cur_troop", "$g_selected_page"),
          (assign, reg0, 1), # reg0: init max_tier to 1
          (call_script, "script_troop_tree_recursive_detect_max_tier", ":cur_troop", 1),
          (assign, ":cur_max_tier", reg0),
          (try_begin),
            (gt, ":cur_max_tier", ":total_max_tier"),
            (assign, ":total_max_tier", ":cur_max_tier"),
          (try_end),
        (try_end),
        (val_sub, ":total_max_tier", 1),
        (val_max, ":total_max_tier", 1),
        (store_div, ":offset_x", 700, ":total_max_tier"),
        (val_min, ":offset_x", 120),

        (str_clear, s0),
        (create_text_overlay, reg1, s0, tf_scrollable),
        (position_set_x, pos1, 15),
        (position_set_y, pos1, 15),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 660),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, "$g_cur_slot_no", 0),
        (assign, reg2, 75),
        # find all root troops of selected faction
        (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
          (neg|troop_is_hero, ":cur_troop"),
          # can upgrade
          (troop_get_upgrade_troop, ":upgrade_troop", ":cur_troop", 0),
          (gt, ":upgrade_troop", 0),
          # page_no_for_cur_troop
          (call_script, "script_get_page_no_of_troop_tree_for_troop_on_1", ":cur_troop"),
          (assign, ":page_no_for_cur_troop", reg0),
          # on current page_no
          (eq, ":page_no_for_cur_troop", "$g_selected_page"),
          # can't be upgraded from other troops of the same page
          (assign, ":is_root_troop", 1),
          (assign, ":end_cond", soldiers_end),
          (try_for_range, ":loop_troop", soldiers_begin, ":end_cond"),
            (neg|troop_is_hero, ":loop_troop"),
            # page_no_for_loop_troop
            (call_script, "script_get_page_no_of_troop_tree_for_troop_on_1", ":loop_troop"),
            (assign, ":page_no_for_loop_troop", reg0),
            # on current page_no
            (eq,  ":page_no_for_loop_troop", "$g_selected_page"),
            (troop_get_upgrade_troop, ":upgrade_troop_1", ":loop_troop", 0),
            (troop_get_upgrade_troop, ":upgrade_troop_2", ":loop_troop", 1),
            (this_or_next|eq, ":upgrade_troop_1", ":cur_troop"),
            (eq, ":upgrade_troop_2", ":cur_troop"),
            (assign, ":is_root_troop", 0),
            (assign, ":end_cond", 0), #break
          (try_end),
####### NEW v3.0-KOMKE START-dirty fix to mongol troop tree
          (try_begin),
            (eq, ":cur_troop", "trp_tatar_tribesman"),
            (assign, ":is_root_troop", 1),
          (else_try),
            (gt, ":cur_troop", "trp_tatar_horseman"),
            (assign, ":is_root_troop", 0),
          (try_end),
####### NEW v3.0-KOMKE END- 
          (eq, ":is_root_troop", 1), # draw troop tree of cur root_troop
          (call_script, "script_troop_tree_recursive_backtracking", ":cur_troop", 50, reg2, ":offset_x"),
          (val_add, reg2, 160),
        (try_end),

        (set_container_overlay, -1),

        ## draw selected_troop: Attributes, Skills, Equipments,
        (try_begin),
          (gt, "$g_selected_troop", 0),
          (store_mul, ":cur_troop", "$g_selected_troop", 2), #with weapons
          (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
          (position_set_x, pos1, 450),
          (position_set_y, pos1, 600),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, 810),
          (position_set_y, pos1, 550),
          (overlay_set_position, reg1, pos1),

          # pos2: text size
          (position_set_x, pos2, 750),
          (position_set_y, pos2, 750),
          # pos2: title text size
          (position_set_x, pos3, 900),
          (position_set_y, pos3, 900),
          # Name
          (str_store_troop_name, s1, "$g_selected_troop"),
          (create_text_overlay, reg1, s1, tf_center_justify),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 710),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # level and HP
          (store_character_level, reg3, "$g_selected_troop"),
          (assign, ":troop_hp", 35),
          (store_skill_level, ":skill", skl_ironflesh, "$g_selected_troop"),
          (store_attribute_level, ":strength", "$g_selected_troop", ca_strength),
          (val_mul, ":skill", 2),
          (val_add, ":troop_hp", ":skill"),
          (val_add, ":troop_hp", ":strength"),
          (assign, reg4, ":troop_hp"),
          (create_text_overlay, reg1, "@Level: {reg3}^Health: {reg4}", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 665),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Attributes
          (create_text_overlay, reg1, "@Attributes", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 630),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@STR^AGI^INT^CHA", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 570),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range, ":attrib_id", 0, 4),
            (try_begin),
              (eq, ":attrib_id", 0),
              (store_attribute_level, reg2, "$g_selected_troop", ":attrib_id"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (store_attribute_level, reg2, "$g_selected_troop", ":attrib_id"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          # (position_set_x, pos1, 980),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 570),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Skills
          (create_text_overlay, reg1, "@Skills", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 527),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@Ironflesh^Power Strike^Power Throw^Power Draw^Shield^Athletics^Riding^Horse Archery", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 415),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range_backwards, ":skill_id", 0, 42),
            (try_begin),
              (eq, ":skill_id", "skl_ironflesh"),
              (store_skill_level, reg2, ":skill_id", "$g_selected_troop"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (this_or_next|eq, ":skill_id", "skl_power_strike"),
              (this_or_next|eq, ":skill_id", "skl_power_throw"),
              (this_or_next|eq, ":skill_id", "skl_power_draw"),
              (this_or_next|eq, ":skill_id", "skl_shield"),
              (this_or_next|eq, ":skill_id", "skl_athletics"),
              (this_or_next|eq, ":skill_id", "skl_riding"),
              (eq, ":skill_id", "skl_horse_archery"),
              (store_skill_level, reg2, ":skill_id", "$g_selected_troop"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 415),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Weapon Proficiencies
          (create_text_overlay, reg1, "@Proficiencies", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 370),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@1H Weapons^2H Weapons^Polearms^Archery^Crossbows^Throwing", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 285),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range, ":wp_id", 0, 6),
            (try_begin),
              (eq, ":wp_id", wpt_one_handed_weapon),
              (store_proficiency_level, reg2, "$g_selected_troop", ":wp_id"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (is_between, ":wp_id", wpt_two_handed_weapon, wpt_firearm),
              (store_proficiency_level, reg2, "$g_selected_troop", ":wp_id"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 285),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Equipments
          (create_text_overlay, reg1, "@Equipments", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 235),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (str_clear, s0),
          (create_text_overlay, "$g_presentation_obj_3", s0, tf_scrollable),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 30),
          (overlay_set_position, "$g_presentation_obj_3", pos1),
          (position_set_x, pos1, 138),
          (position_set_y, pos1, 202),
          (overlay_set_area_size, "$g_presentation_obj_3", pos1),
          (set_container_overlay, "$g_presentation_obj_3"),

          (troop_clear_inventory, "trp_temp_array_a"),
          (troop_get_inventory_capacity, ":inv_cap", "$g_selected_troop"),
          (try_for_range, ":i_slot", 0, ":inv_cap"),
            (troop_get_inventory_slot, ":item", "$g_selected_troop", ":i_slot"),
            (gt, ":item", -1),
            (troop_get_inventory_slot_modifier, ":imod", "$g_selected_troop", ":i_slot"),
            (troop_add_item, "trp_temp_array_a", ":item", ":imod"),
          (try_end),

          (assign, ":pos_x", 0),
          (assign, ":pos_y", 840),
          (assign, ":slot_no", 10),
          # (try_for_range, ":unused_height", 0, 8),
		  (store_div, ":max_height", ":inv_cap", 3),
          (try_for_range, ":unused_height", 0, ":max_height"),
            (try_for_range, ":unused_width", 0, 3),
              (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
              (position_set_x, pos1, 320),
              (position_set_y, pos1, 320),
              (overlay_set_size, reg1, pos1),
              (position_set_x, pos1, ":pos_x"),
              (position_set_y, pos1, ":pos_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
              (create_mesh_overlay, reg1, "mesh_inv_slot"),
              (position_set_x, pos1, 400),
              (position_set_y, pos1, 400),
              (overlay_set_size, reg1, pos1),
              (position_set_x, pos1, ":pos_x"),
              (position_set_y, pos1, ":pos_y"),
              (overlay_set_position, reg1, pos1),
              (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
              (val_max, ":item_no", 0),
              (create_mesh_overlay_with_item_id, reg1, ":item_no"),
              (position_set_x, pos1, 400),
              (position_set_y, pos1, 400),
              (overlay_set_size, reg1, pos1),
              (store_add, ":item_x", ":pos_x", 20),
              (store_add, ":item_y", ":pos_y", 20),
              (position_set_x, pos1, ":item_x"),
              (position_set_y, pos1, ":item_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_b", ":slot_no", reg1),
              (val_add, ":pos_x", 40),
              (val_add, ":slot_no", 1),
            (try_end),
            (assign, ":pos_x", 0),
            (val_sub, ":pos_y", 40),
          (try_end),
          (set_container_overlay, -1),
        (try_end),
      ]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (gt, "$g_selected_troop", 0),
        (try_begin),
          (eq, ":enter_leave", 0),
          (try_for_range, ":slot_no", 10, 106),
            (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
            (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
            (troop_get_inventory_slot_modifier, ":cur_imod", "trp_temp_array_a", ":slot_no"),
            (try_begin),
              (gt, ":item_no", -1),
              (troop_get_slot, ":target_obj", "trp_temp_array_b", ":slot_no"),
              (overlay_get_position, pos0, ":target_obj"),
              (show_item_details_with_modifier, ":item_no", ":cur_imod", pos0, 100),
              (assign, "$g_current_opened_item_details", ":slot_no"),
            (try_end),
          (try_end),
        (else_try),
          (try_for_range, ":slot_no", 10, 106),
            (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
            (try_begin),
              (eq, "$g_current_opened_item_details", ":slot_no"),
              (close_item_details),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_for_range, ":slot_no", 0, "$g_cur_slot_no"),
          (troop_slot_eq, "trp_stack_selection_amounts", ":slot_no", ":object"),
          (troop_get_slot, "$g_selected_troop", "trp_stack_selection_ids", ":slot_no"),
          (start_presentation, "prsnt_faction_troop_trees_1"),
        (try_end),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (store_sub, ":num_pages", npc_cultures_end_1, npc_cultures_begin_1),
          # (val_add, ":num_pages", 3),
          (store_sub, "$g_selected_page", ":num_pages", ":value"),
          (val_sub, "$g_selected_page", 1),
          (assign, "$g_selected_troop", 0),
          (start_presentation, "prsnt_faction_troop_trees_1"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_selected_troop", 0),
          (assign, "$g_selected_page", 0),
          (presentation_set_duration, 0),
        (try_end),
      ]),
  ]),




################## since all the cultures don't fit into a single presentation there's this one
("faction_troop_trees_2", 0, 0, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (create_mesh_overlay, reg1, "mesh_load_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),

        ## combo_button
        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 690),
        (overlay_set_position, "$g_presentation_obj_1", pos1),
        # factions
        (store_sub, ":num_factions", npc_cultures_end_2, npc_cultures_begin_2),
        (store_add, ":num_pages", ":num_factions", 3),

        ## page names, from bottom to top
        (overlay_add_item, "$g_presentation_obj_1", "@Others"),
        (overlay_add_item, "$g_presentation_obj_1", "@Outlaws"),
        (overlay_add_item, "$g_presentation_obj_1", "@Mercenary"),
        (try_for_range_backwards, ":page_no", 0, ":num_factions"),
          (store_add, ":faction_no", ":page_no", npc_cultures_begin_2),
          (str_store_faction_name, s0, ":faction_no"),
          (overlay_add_item, "$g_presentation_obj_1", s0),
        (try_end),
        (store_sub, ":presentation_obj_val", ":num_pages", "$g_selected_page"),
        (val_sub, ":presentation_obj_val", 1),
        (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),

        ## back
        (create_game_button_overlay, "$g_presentation_obj_2", "@Close"),
        (position_set_x, pos1, 750),
        (position_set_y, pos1, 685),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

        ## tips
        (create_text_overlay, reg1, "@Click the center button to toggle faction^Click the avatars to view details of them", tf_left_align),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 800),
        (overlay_set_size, reg1, pos1),
        (position_set_x, pos1, 30),
        (position_set_y, pos1, 690),
        (overlay_set_position, reg1, pos1),

        ## pic_arms
        # (try_begin),
          # (is_between, "$g_selected_page", 0, ":num_factions"),
          # (store_add, ":pic_arms", "mesh_pic_arms_swadian", "$g_selected_page"),
          # (create_mesh_overlay, reg1, ":pic_arms"),
          # (position_set_x, pos1, 120),
          # (position_set_y, pos1, 100),
          # (overlay_set_position, reg1, pos1),
          # (position_set_x, pos1, 300),
          # (position_set_y, pos1, 300),
          # (overlay_set_size, reg1, pos1),
        # (try_end),

        # detect_total_max_tier, calculate offset_x
        (assign, ":total_max_tier", 1),
        (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
          (neg|troop_is_hero, ":cur_troop"),
          # can upgrade
          (troop_get_upgrade_troop, ":upgrade_troop", ":cur_troop", 0),
          (gt, ":upgrade_troop", 0),
          # page_no_for_cur_troop
          (call_script, "script_get_page_no_of_troop_tree_for_troop_on_2", ":cur_troop"),
          (assign, ":page_no_for_cur_troop", reg0),
          # on current page_no
          (eq, ":page_no_for_cur_troop", "$g_selected_page"),
          (assign, reg0, 1), # reg0: init max_tier to 1
          (call_script, "script_troop_tree_recursive_detect_max_tier", ":cur_troop", 1),
          (assign, ":cur_max_tier", reg0),
          (try_begin),
            (gt, ":cur_max_tier", ":total_max_tier"),
            (assign, ":total_max_tier", ":cur_max_tier"),
          (try_end),
        (try_end),
        (val_sub, ":total_max_tier", 1),
        (val_max, ":total_max_tier", 1),
        (store_div, ":offset_x", 700, ":total_max_tier"),
        (val_min, ":offset_x", 120),

        (str_clear, s0),
        (create_text_overlay, reg1, s0, tf_scrollable),
        (position_set_x, pos1, 15),
        (position_set_y, pos1, 15),
        (overlay_set_position, reg1, pos1),
        (position_set_x, pos1, 800),
        (position_set_y, pos1, 660),
        (overlay_set_area_size, reg1, pos1),
        (set_container_overlay, reg1),

        (assign, "$g_cur_slot_no", 0),
        (assign, reg2, 75),
        # find all root troops of selected faction
        (try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
          (neg|troop_is_hero, ":cur_troop"),
          # can upgrade
          (troop_get_upgrade_troop, ":upgrade_troop", ":cur_troop", 0),
          (gt, ":upgrade_troop", 0),
          # page_no_for_cur_troop
          (call_script, "script_get_page_no_of_troop_tree_for_troop_on_2", ":cur_troop"),
          (assign, ":page_no_for_cur_troop", reg0),
          # on current page_no
          (eq, ":page_no_for_cur_troop", "$g_selected_page"),
          # can't be upgraded from other troops of the same page
          (assign, ":is_root_troop", 1),
          (assign, ":end_cond", soldiers_end),
          (try_for_range, ":loop_troop", soldiers_begin, ":end_cond"),
            (neg|troop_is_hero, ":loop_troop"),
            # page_no_for_loop_troop
            (call_script, "script_get_page_no_of_troop_tree_for_troop_on_2", ":loop_troop"),
            (assign, ":page_no_for_loop_troop", reg0),
            # on current page_no
            (eq,  ":page_no_for_loop_troop", "$g_selected_page"),
            (troop_get_upgrade_troop, ":upgrade_troop_1", ":loop_troop", 0),
            (troop_get_upgrade_troop, ":upgrade_troop_2", ":loop_troop", 1),
            (this_or_next|eq, ":upgrade_troop_1", ":cur_troop"),
            (eq, ":upgrade_troop_2", ":cur_troop"),
            (assign, ":is_root_troop", 0),
            (assign, ":end_cond", 0), #break
          (try_end),
          (eq, ":is_root_troop", 1), # draw troop tree of cur root_troop
          (call_script, "script_troop_tree_recursive_backtracking", ":cur_troop", 50, reg2, ":offset_x"),
          (val_add, reg2, 160),
        (try_end),

        (set_container_overlay, -1),

        ## draw selected_troop: Attributes, Skills, Equipments,
        (try_begin),
          (gt, "$g_selected_troop", 0),
          (store_mul, ":cur_troop", "$g_selected_troop", 2), #with weapons
          (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
          (position_set_x, pos1, 450),
          (position_set_y, pos1, 600),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, 810),
          (position_set_y, pos1, 550),
          (overlay_set_position, reg1, pos1),

          # pos2: text size
          (position_set_x, pos2, 750),
          (position_set_y, pos2, 750),
          # pos2: title text size
          (position_set_x, pos3, 900),
          (position_set_y, pos3, 900),
          # Name
          (str_store_troop_name, s1, "$g_selected_troop"),
          (create_text_overlay, reg1, s1, tf_center_justify),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 710),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # level and HP
          (store_character_level, reg3, "$g_selected_troop"),
          (assign, ":troop_hp", 35),
          (store_skill_level, ":skill", skl_ironflesh, "$g_selected_troop"),
          (store_attribute_level, ":strength", "$g_selected_troop", ca_strength),
          (val_mul, ":skill", 2),
          (val_add, ":troop_hp", ":skill"),
          (val_add, ":troop_hp", ":strength"),
          (assign, reg4, ":troop_hp"),
          (create_text_overlay, reg1, "@Level: {reg3}^Health: {reg4}", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 665),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Attributes
          (create_text_overlay, reg1, "@Attributes", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 630),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@STR^AGI^INT^CHA", tf_left_align),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 570),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range, ":attrib_id", 0, 4),
            (try_begin),
              (eq, ":attrib_id", 0),
              (store_attribute_level, reg2, "$g_selected_troop", ":attrib_id"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (store_attribute_level, reg2, "$g_selected_troop", ":attrib_id"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          # (position_set_x, pos1, 980),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 570),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Skills
          (create_text_overlay, reg1, "@Skills", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 527),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@Ironflesh^Power Strike^Power Throw^Power Draw^Shield^Athletics^Riding^Horse Archery", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 415),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range_backwards, ":skill_id", 0, 42),
            (try_begin),
              (eq, ":skill_id", "skl_ironflesh"),
              (store_skill_level, reg2, ":skill_id", "$g_selected_troop"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (this_or_next|eq, ":skill_id", "skl_power_strike"),
              (this_or_next|eq, ":skill_id", "skl_power_throw"),
              (this_or_next|eq, ":skill_id", "skl_power_draw"),
              (this_or_next|eq, ":skill_id", "skl_shield"),
              (this_or_next|eq, ":skill_id", "skl_athletics"),
              (this_or_next|eq, ":skill_id", "skl_riding"),
              (eq, ":skill_id", "skl_horse_archery"),
              (store_skill_level, reg2, ":skill_id", "$g_selected_troop"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 415),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Weapon Proficiencies
          (create_text_overlay, reg1, "@Proficiencies", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 370),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (create_text_overlay, reg1, "@1H Weapons^2H Weapons^Polearms^Archery^Crossbows^Throwing", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 285),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          (try_for_range, ":wp_id", 0, 6),
            (try_begin),
              (eq, ":wp_id", wpt_one_handed_weapon),
              (store_proficiency_level, reg2, "$g_selected_troop", ":wp_id"),
              (str_store_string, s1, "@{reg2}"),
            (else_try),
              (is_between, ":wp_id", wpt_two_handed_weapon, wpt_firearm),
              (store_proficiency_level, reg2, "$g_selected_troop", ":wp_id"),
              (str_store_string, s1, "@{s1}^{reg2}"),
            (try_end),
          (try_end),
          (create_text_overlay, reg1, s1, tf_right_align),
          (position_set_x, pos1, 970),
          (position_set_y, pos1, 285),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos2),

          # Equipments
          (create_text_overlay, reg1, "@Equipments", tf_left_align),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 235),
          (overlay_set_position, reg1, pos1),
          (overlay_set_size, reg1, pos3),
          (str_clear, s0),
          (create_text_overlay, "$g_presentation_obj_3", s0, tf_scrollable),
          (position_set_x, pos1, 840),
          (position_set_y, pos1, 30),
          (overlay_set_position, "$g_presentation_obj_3", pos1),
          (position_set_x, pos1, 138),
          (position_set_y, pos1, 202),
          (overlay_set_area_size, "$g_presentation_obj_3", pos1),
          (set_container_overlay, "$g_presentation_obj_3"),

          (troop_clear_inventory, "trp_temp_array_a"),
          (troop_get_inventory_capacity, ":inv_cap", "$g_selected_troop"),
          (try_for_range, ":i_slot", 0, ":inv_cap"),
            (troop_get_inventory_slot, ":item", "$g_selected_troop", ":i_slot"),
            (gt, ":item", -1),
            (troop_get_inventory_slot_modifier, ":imod", "$g_selected_troop", ":i_slot"),
            (troop_add_item, "trp_temp_array_a", ":item", ":imod"),
          (try_end),

          # (store_free_inventory_capacity, ":num_free_slots", "$g_selected_troop"),
          # (store_sub, ":num_items", ":inv_cap", ":num_free_slots"),

          (assign, ":pos_x", 0),
          (assign, ":pos_y", 280),
          (assign, ":slot_no", 10),
          (try_for_range, ":unused_height", 0, 8),
          # (store_div, ":cur_troop_capacity", ":num_items", 3),
          # (store_mul, ":cur_troop_capacity_pos", ":cur_troop_capacity", 40),
          # (try_for_range, ":unused_height", 0, ":cur_troop_capacity"),
            (try_for_range, ":unused_width", 0, 3),
              (create_mesh_overlay, reg1, "mesh_mp_inventory_choose"),
              (position_set_x, pos1, 320),
              (position_set_y, pos1, 320),
              (overlay_set_size, reg1, pos1),
              (position_set_x, pos1, ":pos_x"),
              (position_set_y, pos1, ":pos_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
              (create_mesh_overlay, reg1, "mesh_inv_slot"),
              (position_set_x, pos1, 400),
              (position_set_y, pos1, 400),
              (overlay_set_size, reg1, pos1),
              (position_set_x, pos1, ":pos_x"),
              (position_set_y, pos1, ":pos_y"),
              (overlay_set_position, reg1, pos1),
              (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
              (val_max, ":item_no", 0),
              (create_mesh_overlay_with_item_id, reg1, ":item_no"),
              (position_set_x, pos1, 400),
              (position_set_y, pos1, 400),
              (overlay_set_size, reg1, pos1),
              (store_add, ":item_x", ":pos_x", 20),
              (store_add, ":item_y", ":pos_y", 20),
              (position_set_x, pos1, ":item_x"),
              (position_set_y, pos1, ":item_y"),
              (overlay_set_position, reg1, pos1),
              (troop_set_slot, "trp_temp_array_b", ":slot_no", reg1),
              (val_add, ":pos_x", 40),
              (val_add, ":slot_no", 1),
            (try_end),
            (assign, ":pos_x", 0),
            (val_sub, ":pos_y", 40),
          (try_end),
          (set_container_overlay, -1),
        (try_end),
      ]),

    (ti_on_presentation_mouse_enter_leave,
      [
      (store_trigger_param_1, ":object"),
      (store_trigger_param_2, ":enter_leave"),

      (try_begin),
        (gt, "$g_selected_troop", 0),
        (try_begin),
          (eq, ":enter_leave", 0),
          (try_for_range, ":slot_no", 10, 106),
            (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
            (troop_get_inventory_slot, ":item_no", "trp_temp_array_a", ":slot_no"),
            (troop_get_inventory_slot_modifier, ":cur_imod", "trp_temp_array_a", ":slot_no"),
            (try_begin),
              (gt, ":item_no", -1),
              (troop_get_slot, ":target_obj", "trp_temp_array_b", ":slot_no"),
              (overlay_get_position, pos0, ":target_obj"),
              (show_item_details_with_modifier, ":item_no", ":cur_imod", pos0, 100),
              (assign, "$g_current_opened_item_details", ":slot_no"),
            (try_end),
          (try_end),
        (else_try),
          (try_for_range, ":slot_no", 10, 106),
            (troop_slot_eq, "trp_temp_array_a", ":slot_no", ":object"),
            (try_begin),
              (eq, "$g_current_opened_item_details", ":slot_no"),
              (close_item_details),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
    ]),

    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_for_range, ":slot_no", 0, "$g_cur_slot_no"),
          (troop_slot_eq, "trp_stack_selection_amounts", ":slot_no", ":object"),
          (troop_get_slot, "$g_selected_troop", "trp_stack_selection_ids", ":slot_no"),
          (start_presentation, "prsnt_faction_troop_trees_2"),
        (try_end),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
          (store_sub, ":num_pages", npc_cultures_end_2, npc_cultures_begin_2),
          (val_add, ":num_pages", 3),
          (store_sub, "$g_selected_page", ":num_pages", ":value"),
          (val_sub, "$g_selected_page", 1),
          (assign, "$g_selected_troop", 0),
          (start_presentation, "prsnt_faction_troop_trees_2"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_2"),
          (assign, "$g_selected_troop", 0),
          (assign, "$g_selected_page", 0),
          (presentation_set_duration, 0),
        (try_end),
      ]),
  ]),
##############################################################################




####################################### FACTION STATISTICS
  ("ee_faction_statistics", 0, mesh_load_window, [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (create_mesh_overlay, reg1, "mesh_load_window"),
        (position_set_x, pos1, 0),
        (position_set_y, pos1, 0),
        (overlay_set_position, reg1, pos1),

        ## combo_button
        (create_combo_button_overlay, "$g_presentation_obj_1"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 690),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

        (try_begin),
          (eq, "$g_misc_current_statistics_menu", 1),
            (assign, ":faction_lower_range", kingdoms_begin_1),
            (assign, ":faction_upper_range", kingdoms_end_1),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 2),
            (assign, ":faction_lower_range", kingdoms_begin_2),
            (assign, ":faction_upper_range", kingdoms_end_2),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 3),
            (assign, ":faction_lower_range", kingdoms_begin_3),
            (assign, ":faction_upper_range", kingdoms_end_3),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 4),
            (assign, ":faction_lower_range", kingdoms_begin_4),
            (assign, ":faction_upper_range", kingdoms_end_4),
        (try_end),

        (assign, ":num_pages", 0),
        # factions
        (store_sub, ":num_factions", ":faction_upper_range", ":faction_lower_range"),
        (val_add, ":num_pages", ":num_factions"),

        ## page names, from bottom to top
        (try_for_range_backwards, ":page_no", 0, ":num_factions"),
          (store_add, ":faction_no", ":page_no", ":faction_lower_range"),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),  ### is still active
          # (neq, ":faction_no", "fac_player"),  ### NEW v3.9
            (str_store_faction_name, s0, ":faction_no"),
            (overlay_add_item, "$g_presentation_obj_1", s0),
        (try_end),
        (store_sub, ":presentation_obj_val", ":num_pages", "$g_selected_page"),
        (val_sub, ":presentation_obj_val", 1),
        (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),


########################################## ROW 1 COLUMN 1
        (position_set_x, pos1, 50),
        (assign, ":value_difference", 35),

        (create_text_overlay, reg0, "@Days active:", tf_vertical_align_center),
        (store_sub, reg1, 686, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
#########################
        (create_text_overlay, reg0, "@Battles won:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Battles lost:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
#########################

#########################
        (create_text_overlay, reg0, "@Enemies Killed:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Enemies Wounded:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Enemies captured:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),
#########################

#########################
        (create_text_overlay, reg0, "@Troops lost (killed):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Troops lost (wounded):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Troops lost (captured):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Troops deployed:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Number of Towns:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Number of Castles:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Number of Villages:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Weaponsmith arrow quiver count:", tf_vertical_align_center),
        # (position_set_y, pos1, 175),
        # (overlay_set_position, reg0, pos1),

        # (create_text_overlay, reg0, "@Weaponsmith bolt quiver count:", tf_vertical_align_center),
        # (position_set_y, pos1, 140),
        # (overlay_set_position, reg0, pos1),

########################################## ROW 1 COLUMN 2
        ## number boxes
        (position_set_x, pos1, 390),
        (assign, ":value_difference", 35),

        (store_add, ":faction_no", "$g_selected_page", ":faction_lower_range"),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_days_active),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (store_sub, reg1, 686, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_battles_won),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_battles_lost),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_enemies_killed),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_enemies_wounded),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_enemies_captured),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_troops_lost_killed),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_troops_lost_wounded),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_troops_lost_captured),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_troops_deployed),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_num_towns),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_num_castles),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_num_villages),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),

########################################## ROW 2 COLUMN 1
        (position_set_x, pos1, 480),
        (assign, ":value_difference", 35),

        (create_text_overlay, reg0, "@Current Lord count:", tf_vertical_align_center),
        (store_sub, reg1, 686, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lords lost (killed in battle):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lords lost (assassinated):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lords lost (executed):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Lords lost (defection):", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),

        (create_text_overlay, reg0, "@Total Lords in faction history:", tf_vertical_align_center),
        (val_sub, reg1, ":value_difference"),
        (position_set_y, pos1, reg1),
        (overlay_set_position, reg0, pos1),



########################################## ROW 2 COLUMN 2
        (position_set_x, pos1, 850),

        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lord_count),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (store_sub, reg1, 686, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lords_lost_battle),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lords_lost_assassination),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lords_lost_execution),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lords_lost_defection),
          (create_text_overlay, reg0, "@{reg5}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),
        (try_begin),
          (faction_get_slot, reg5, ":faction_no", slot_faction_lord_count),
          (faction_get_slot, reg6, ":faction_no", slot_faction_lords_lost_battle),
          (faction_get_slot, reg7, ":faction_no", slot_faction_lords_lost_assassination),
          (faction_get_slot, reg8, ":faction_no", slot_faction_lords_lost_execution),
          (faction_get_slot, reg9, ":faction_no", slot_faction_lords_lost_defection),
          (store_add, reg10, reg5),
          (val_add, reg10, reg6),
          (val_add, reg10, reg7),
          (val_add, reg10, reg8),
          (val_add, reg10, reg9),
          (create_text_overlay, reg0, "@{reg10}", tf_vertical_align_center),
          (val_sub, reg1, ":value_difference"),
          (position_set_y, pos1, reg1),
          (overlay_set_position, reg0, pos1),
        (try_end),


########################### DONE
        (create_game_button_overlay, "$g_presentation_obj_31", "@Done"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_31", pos1)

#########################################
      ]),


    (ti_on_presentation_event_state_change,
      [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
          (eq, "$g_misc_current_statistics_menu", 1),
            (assign, ":faction_lower_range", kingdoms_begin_1),
            (assign, ":faction_upper_range", kingdoms_end_1),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 2),
            (assign, ":faction_lower_range", kingdoms_begin_2),
            (assign, ":faction_upper_range", kingdoms_end_2),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 3),
            (assign, ":faction_lower_range", kingdoms_begin_3),
            (assign, ":faction_upper_range", kingdoms_end_3),
        (else_try),
          (eq, "$g_misc_current_statistics_menu", 4),
            (assign, ":faction_lower_range", kingdoms_begin_4),
            (assign, ":faction_upper_range", kingdoms_end_4),
        (try_end),

        (try_begin),
          (eq, ":object", "$g_presentation_obj_1"),
            (store_sub, ":num_pages", ":faction_upper_range", ":faction_lower_range"),
            (store_sub, "$g_selected_page", ":num_pages", ":value"),
            (val_sub, "$g_selected_page", 1),
            (start_presentation, "prsnt_ee_faction_statistics"),
        (else_try),
          (eq, ":object", "$g_presentation_obj_31"),
            (assign, "$g_selected_page", 0),
            (presentation_set_duration, 0),
        (try_end),
      ]),

    ]),
##############################################################################



######################## NEW v2.1 - Debug testing troops using custom battle as template
  ("ee_custom_battle_designer", prsntf_manual_end_only, mesh_cb_ui_main, [
    (ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),

      (create_text_overlay, reg0, "str_player", tf_center_justify|tf_single_line|tf_with_outline),
      (overlay_set_color, reg0, 0xFFFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, 700),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_enemy",  tf_center_justify|tf_single_line|tf_with_outline),
      (overlay_set_color, reg0, 0xFFFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, 700),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_character", tf_center_justify),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, 670),
      (overlay_set_position, reg0, pos1),

      (create_combo_label_overlay, "$g_presentation_obj_custom_battle_designer_18"),
      (position_set_x, pos1, 800),
      (position_set_y, pos1, 800),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_18", pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, 635),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_18", pos1),
      (try_for_range, ":cur_troop", quick_battle_troops_begin, quick_battle_troops_end),
        (str_store_troop_name, s0, ":cur_troop"),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_18", s0),
      (try_end),
      (store_sub, ":cur_troop", "$g_quick_battle_troop", quick_battle_troops_begin),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_18", ":cur_troop"),

      (store_mul, ":cur_troop", "$g_quick_battle_troop", 2), #with weapons
      (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":cur_troop"),
      (position_set_x, pos1, 25),
      (position_set_y, pos1, 370),
      (overlay_set_position, reg0, pos1),

      (try_begin),
        (faction_get_slot, ":cur_troop", "$g_quick_battle_team_2_faction", slot_faction_tier_5_troop),  ######### gets the highest tier troop
      (try_end),

      (try_begin),
        (gt, ":cur_troop", 0),
      (else_try),
        (neg|gt, ":cur_troop", 0),
          (assign, ":cur_troop", "trp_taiga_bandit"),  #### if none set this
      (try_end),

      (val_mul, ":cur_troop", 2), #with weapons
      (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":cur_troop"),
      (position_set_x, pos1, 670),
      (position_set_y, pos1, 370),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_biography", tf_center_justify),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 700),
      (overlay_set_position, reg0, pos1),

      (store_sub, ":cur_troop_text", "$g_quick_battle_troop", quick_battle_troops_begin),
      (val_add, ":cur_troop_text", quick_battle_troop_texts_begin),
      (create_text_overlay, reg0, ":cur_troop_text", tf_scrollable),
      (position_set_x, pos1, 850),
      (position_set_y, pos1, 850),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 320),
      (position_set_y, pos1, 560),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 360),
      (position_set_y, pos1, 130),
      (overlay_set_area_size, reg0, pos1),

      (create_text_overlay, reg0, "str_map_basic", tf_center_justify),
      (overlay_set_color, reg0, 0xFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 450),
      (overlay_set_position, reg0, pos1),

      (create_combo_label_overlay, "$g_presentation_obj_custom_battle_designer_1"),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_1", pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 415),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_1", pos1),
      (try_begin),
        (eq, "$g_quick_battle_game_type", 0), #battle
        (try_for_range, ":cur_scene", quick_battle_battle_scenes_begin, quick_battle_battle_scenes_end),
          (store_sub, ":cur_scene_name", ":cur_scene", quick_battle_scenes_begin),
          (val_add, ":cur_scene_name", quick_battle_scene_names_begin),
          (overlay_add_item, "$g_presentation_obj_custom_battle_designer_1", ":cur_scene_name"),
        (try_end),
        (try_begin),
          (is_between, "$g_quick_battle_map", quick_battle_battle_scenes_begin, quick_battle_battle_scenes_end),
          (store_sub, ":cur_map", "$g_quick_battle_map", quick_battle_battle_scenes_begin),
          (overlay_set_val, "$g_presentation_obj_custom_battle_designer_1", ":cur_map"),
        (else_try),
          (overlay_set_val, "$g_presentation_obj_custom_battle_designer_1", 0),
          (assign, "$g_quick_battle_map", quick_battle_battle_scenes_begin),
        (try_end),
      (else_try),
        (try_for_range, ":cur_scene", quick_battle_siege_scenes_begin, quick_battle_siege_scenes_end),
          (store_sub, ":cur_scene_name", ":cur_scene", quick_battle_scenes_begin),
          (val_add, ":cur_scene_name", quick_battle_scene_names_begin),
          (overlay_add_item, "$g_presentation_obj_custom_battle_designer_1", ":cur_scene_name"),
        (try_end),
        (try_begin),
          (is_between, "$g_quick_battle_map", quick_battle_siege_scenes_begin, quick_battle_siege_scenes_end),
          (store_sub, ":cur_map", "$g_quick_battle_map", quick_battle_siege_scenes_begin),
          (overlay_set_val, "$g_presentation_obj_custom_battle_designer_1", ":cur_map"),
        (else_try),
          (overlay_set_val, "$g_presentation_obj_custom_battle_designer_1", 0),
          (assign, "$g_quick_battle_map", quick_battle_siege_scenes_begin),
        (try_end),
      (try_end),

      (store_sub, ":cur_mesh", "$g_quick_battle_map", quick_battle_scenes_begin),
      (val_add, ":cur_mesh", quick_battle_scene_images_begin),
      (create_mesh_overlay, reg0, ":cur_mesh"),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 380),
      (position_set_y, pos1, 220),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_game_type_basic", tf_center_justify),
      (overlay_set_color, reg0, 0xFFFFFF),
      (position_set_x, pos1, 1500),
      (position_set_y, pos1, 1500),
      (overlay_set_size, reg0, pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 180),
      (overlay_set_position, reg0, pos1),

      (create_combo_label_overlay, "$g_presentation_obj_custom_battle_designer_23"),
      (position_set_x, pos1, 700),
      (position_set_y, pos1, 700),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_23", pos1),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 150),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_23", pos1),
      (overlay_add_item, "$g_presentation_obj_custom_battle_designer_23", "str_battle"),
      (overlay_add_item, "$g_presentation_obj_custom_battle_designer_23", "str_siege_offense"),
      (overlay_add_item, "$g_presentation_obj_custom_battle_designer_23", "str_siege_defense"),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_23", "$g_quick_battle_game_type"),

      (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_24", "str_randomize"),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 60),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_24", pos1),

      (assign, ":cur_y", 330),
      (assign, ":cur_y", 350),
      (assign, ":cur_y_adder", 40),

      (create_text_overlay, reg0, "str_faction", tf_center_justify),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_faction", tf_center_justify),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (create_combo_label_overlay, "$g_presentation_obj_custom_battle_designer_4"),
##      (position_set_x, pos1, 800),
##      (position_set_y, pos1, 800),
##      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_4", pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_4", pos1),
      (try_begin),
        (is_trial_version),
        (str_store_faction_name, s0, npc_kingdoms_begin),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_4", s0),
        (store_add, ":cur_faction", npc_kingdoms_begin, 1),
        (str_store_faction_name, s0, ":cur_faction"),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_4", s0),
      (else_try),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, "fac_enhanced_kingdom_1"),
          (str_store_faction_name, s0, ":cur_faction"),
          (overlay_add_item, "$g_presentation_obj_custom_battle_designer_4", s0),
        (try_end),
        (str_store_faction_name, s0, "fac_outlaws"),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_4", s0),
      (try_end),
      (try_begin),
        (eq, "$g_quick_battle_team_1_faction", "fac_outlaws"),
        (store_sub, ":overlay_value", "fac_enhanced_kingdom_1", npc_kingdoms_begin),
        (overlay_set_val, "$g_presentation_obj_custom_battle_designer_4", ":overlay_value"),
      (else_try),
        (store_sub, ":team_1_faction", "$g_quick_battle_team_1_faction", npc_kingdoms_begin),
        (overlay_set_val, "$g_presentation_obj_custom_battle_designer_4", ":team_1_faction"),
      (try_end),

      (create_combo_label_overlay, "$g_presentation_obj_custom_battle_designer_5"),
##      (position_set_x, pos1, 800),
##      (position_set_y, pos1, 800),
##      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_5", pos1),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_5", pos1),
      (try_begin),
        (is_trial_version),
        (str_store_faction_name, s0, npc_kingdoms_begin),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_5", s0),
        (store_add, ":cur_faction", npc_kingdoms_begin, 1),
        (str_store_faction_name, s0, ":cur_faction"),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_5", s0),
      (else_try),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, "fac_enhanced_kingdom_1"),
          (str_store_faction_name, s0, ":cur_faction"),
          (overlay_add_item, "$g_presentation_obj_custom_battle_designer_5", s0),
        (try_end),
        (str_store_faction_name, s0, "fac_outlaws"),
        (overlay_add_item, "$g_presentation_obj_custom_battle_designer_5", s0),
      (try_end),
      (try_begin),
        (eq, "$g_quick_battle_team_2_faction", "fac_outlaws"),
        (store_sub, ":overlay_value", "fac_enhanced_kingdom_1", npc_kingdoms_begin),
        (overlay_set_val, "$g_presentation_obj_custom_battle_designer_5", ":overlay_value"),
      (else_try),
        (store_sub, ":team_2_faction", "$g_quick_battle_team_2_faction", npc_kingdoms_begin),
        (overlay_set_val, "$g_presentation_obj_custom_battle_designer_5", ":team_2_faction"),
      (try_end),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (create_text_overlay, reg0, "str_army_composition", tf_center_justify),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_army_composition", tf_center_justify),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (try_begin),
        (eq, "$g_presentation_obj_custom_battle_designer_6_last_value", 0),
        (eq, "$g_presentation_obj_custom_battle_designer_7_last_value", 0),
        (eq, "$g_presentation_obj_custom_battle_designer_8_last_value", 0),
        (eq, "$g_presentation_obj_custom_battle_designer_9_last_value", 0),
        (eq, "$g_presentation_obj_custom_battle_designer_10_last_value", 0),
        (eq, "$g_presentation_obj_custom_battle_designer_11_last_value", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", 34),
        (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", 33),
        (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 33),
        (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", 34),
        (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", 33),
        (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 33),
        (assign, "$g_presentation_obj_custom_battle_designer_6_locked", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_7_locked", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_8_locked", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_9_locked", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_10_locked", 0),
        (assign, "$g_presentation_obj_custom_battle_designer_11_locked", 0),
      (try_end),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_infantry"),
      (position_set_x, pos1, 5),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_infantry"),
      (position_set_x, pos1, 650),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_6", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_6", pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_6", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_6_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_12", "str_reg0_percent", 0),
      (position_set_x, pos1, 295),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_12", pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_9", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_9", pos1),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_9", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_9_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_15", "str_reg0_percent", 0),
      (position_set_x, pos1, 940),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_15", pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_archer"),
      (position_set_x, pos1, 15),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_archer"),
      (position_set_x, pos1, 660),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_7", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_7", pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_7", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_7_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_13", "str_reg0_percent", 0),
      (position_set_x, pos1, 295),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_13", pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_10", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_10", pos1),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_10", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_10_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_16", "str_reg0_percent", 0),
      (position_set_x, pos1, 940),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_16", pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_horseman"),
      (position_set_x, pos1, 10),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_mesh_overlay, reg0, "mesh_cb_ui_icon_horseman"),
      (position_set_x, pos1, 655),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 400),
      (overlay_set_size, reg0, pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_8", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_8", pos1),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_8", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_8_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_14", "str_reg0_percent", 0),
      (position_set_x, pos1, 295),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_14", pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_11", 0, 100),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_11", pos1),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_11", pos1),

      (assign, reg0, "$g_presentation_obj_custom_battle_designer_11_last_value"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_17", "str_reg0_percent", 0),
      (position_set_x, pos1, 940),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_17", pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (create_text_overlay, reg0, "str_army_size", tf_center_justify),
      (position_set_x, pos1, 175),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (create_text_overlay, reg0, "str_army_size", tf_center_justify),
      (position_set_x, pos1, 820),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, reg0, pos1),

      (val_sub, ":cur_y", ":cur_y_adder"),

      (try_begin),
        (is_trial_version),
        (val_min, "$g_quick_battle_army_1_size", 25),
        (val_min, "$g_quick_battle_army_2_size", 25),
      (try_end),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_2", 0, 100),
      (overlay_set_boundaries, "$g_presentation_obj_custom_battle_designer_2", 1000, 75000),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_2", "$g_quick_battle_army_1_size"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_2", pos1),
      (position_set_x, pos1, 135),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_2", pos1),

      (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_1_size"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_21", "str_reg0_men", 0),
      (position_set_x, pos1, 255),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_21", pos1),

      (create_slider_overlay, "$g_presentation_obj_custom_battle_designer_3", 300),
      (overlay_set_boundaries, "$g_presentation_obj_custom_battle_designer_3", 1000, 75000),
      (overlay_set_val, "$g_presentation_obj_custom_battle_designer_3", "$g_quick_battle_army_2_size"),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, 1000),
      (overlay_set_size, "$g_presentation_obj_custom_battle_designer_3", pos1),
      (position_set_x, pos1, 780),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_3", pos1),

      (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_2_size"),
      (create_text_overlay, "$g_presentation_obj_custom_battle_designer_22", "str_reg0_men", 0),
      (position_set_x, pos1, 900),
      (position_set_y, pos1, ":cur_y"),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_22", pos1),

      (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_19", "str_start", 0),
      (position_set_x, pos1, 415),
      (position_set_y, pos1, 10),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_19", pos1),

      (create_game_button_overlay, "$g_presentation_obj_custom_battle_designer_20", "str_back", 0),
      (position_set_x, pos1, 585),
      (position_set_y, pos1, 10),
      (overlay_set_position, "$g_presentation_obj_custom_battle_designer_20", pos1),

      (presentation_set_duration, 999999),
      ]),

    (ti_on_presentation_event_state_change,
     [
       (store_trigger_param_1, ":object"),
       (store_trigger_param_2, ":value"),
       (try_begin),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_1"),
         (try_begin),
           (eq, "$g_quick_battle_game_type", 0),
           (store_add, "$g_quick_battle_map", ":value", quick_battle_battle_scenes_begin),
         (else_try),
           (store_add, "$g_quick_battle_map", ":value", quick_battle_siege_scenes_begin),
         (try_end),
         (presentation_set_duration, 0),
         (start_presentation, "prsnt_ee_custom_battle_designer"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_23"),
         (assign, "$g_quick_battle_game_type", ":value"),
         (presentation_set_duration, 0),
         (start_presentation, "prsnt_ee_custom_battle_designer"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_24"),
         (store_random_in_range, "$g_quick_battle_game_type", 0, 3),
         (store_random_in_range, "$g_quick_battle_troop", quick_battle_troops_begin, quick_battle_troops_end),
         (try_begin),
           (is_trial_version),
           (store_random_in_range, "$g_quick_battle_team_1_faction", 0, 2),
           (try_begin),
             (eq, "$g_quick_battle_team_1_faction", 0),
             (assign, "$g_quick_battle_team_2_faction", 1),
           (else_try),
             (assign, "$g_quick_battle_team_2_faction", 0),
           (try_end),
           (val_add, "$g_quick_battle_team_1_faction", npc_kingdoms_begin),
           (val_add, "$g_quick_battle_team_2_faction", npc_kingdoms_begin),
           (store_random_in_range, "$g_quick_battle_army_1_size", 10, 16),
           (store_random_in_range, ":random_army_size", 0, 6),
           (val_add, "$g_quick_battle_army_1_size", ":random_army_size"),
           (store_random_in_range, ":random_army_size", 0, 6),
           (val_add, "$g_quick_battle_army_1_size", ":random_army_size"),
         (else_try),
           (store_sub, ":num_factions", "fac_enhanced_kingdom_1", npc_kingdoms_begin),
           (val_add, ":num_factions", 1),
           (store_random_in_range, "$g_quick_battle_team_1_faction", 0, ":num_factions"),
           (try_begin),
             (eq, "$g_quick_battle_team_1_faction", 0),
             (assign, "$g_quick_battle_team_1_faction", "fac_outlaws"),
           (else_try),
             (val_add, "$g_quick_battle_team_1_faction", npc_kingdoms_begin),
             (val_sub, "$g_quick_battle_team_1_faction", 1),
           (try_end),
           (assign, ":end_cond", 1000),
           (try_for_range, ":unused", 0, ":end_cond"),
             (store_random_in_range, "$g_quick_battle_team_2_faction", 0, ":num_factions"),
             (try_begin),
               (eq, "$g_quick_battle_team_2_faction", 0),
               (assign, "$g_quick_battle_team_2_faction", "fac_outlaws"),
             (else_try),
               (val_add, "$g_quick_battle_team_2_faction", npc_kingdoms_begin),
               (val_sub, "$g_quick_battle_team_2_faction", 1),
             (try_end),
             (neq, "$g_quick_battle_team_1_faction", "$g_quick_battle_team_2_faction"),
             (assign, ":end_cond", 0),
           (try_end),
           (store_random_in_range, "$g_quick_battle_army_1_size", 10, 21),
           (store_random_in_range, ":random_army_size", 0, 11),
           (val_add, "$g_quick_battle_army_1_size", ":random_army_size"),
           (store_random_in_range, ":random_army_size", 0, 11),
           (val_add, "$g_quick_battle_army_1_size", ":random_army_size"),
         (try_end),
         (assign, "$g_quick_battle_army_2_size", "$g_quick_battle_army_1_size"),
         (try_begin),
           (eq, "$g_quick_battle_game_type", 0), #battle
           (store_random_in_range, "$g_quick_battle_map", quick_battle_battle_scenes_begin, quick_battle_battle_scenes_end),
           (store_random_in_range, ":random_type", 0, 3),
           (store_random_in_range, ":random_type_2", 0, 2),
           (store_random_in_range, ":random_composition", 0, 100),
           (store_sub, ":left_max", 100, ":random_composition"),
           (store_random_in_range, ":random_composition_2", 0, ":left_max"),
           (store_sub, ":random_composition_3", ":left_max", ":random_composition_2"),
           (try_begin),
             (eq, ":random_type", 0),
             (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":random_composition_3"),
             (try_end),
           (else_try),
             (eq, ":random_type", 1),
             (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":random_composition_3"),
             (try_end),
           (else_try),
             (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":random_composition_3"),
             (try_end),
           (try_end),
           (store_random_in_range, ":random_type", 0, 3),
           (store_random_in_range, ":random_type_2", 0, 2),
           (store_random_in_range, ":random_composition", 0, 100),
           (store_sub, ":left_max", 100, ":random_composition"),
           (store_random_in_range, ":random_composition_2", 0, ":left_max"),
           (store_sub, ":random_composition_3", ":left_max", ":random_composition_2"),
           (try_begin),
             (eq, ":random_type", 0),
             (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":random_composition_3"),
             (try_end),
           (else_try),
             (eq, ":random_type", 1),
             (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":random_composition_3"),
             (try_end),
           (else_try),
             (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":random_composition"),
             (try_begin),
               (eq, ":random_type_2", 0),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":random_composition_3"),
             (else_try),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":random_composition_2"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":random_composition_3"),
             (try_end),
           (try_end),
         (else_try),
           (eq, "$g_quick_battle_game_type", 1), #siege offense
           (store_random_in_range, "$g_quick_battle_map", quick_battle_siege_scenes_begin, quick_battle_siege_scenes_end),
           #defender is enemy
           (store_random_in_range, "$g_presentation_obj_custom_battle_designer_10_last_value", 30, 100), #min 30% archer
           (store_sub, "$g_presentation_obj_custom_battle_designer_9_last_value", 100, "$g_presentation_obj_custom_battle_designer_10_last_value"),
           (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 0), #no cavalry
           (store_random_in_range, "$g_presentation_obj_custom_battle_designer_6_last_value", 20, 100), #min 20% infantry
           (store_sub, "$g_presentation_obj_custom_battle_designer_7_last_value", 100, "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 0), #no cavalry
         (else_try),
           #siege defense
           (store_random_in_range, "$g_quick_battle_map", quick_battle_siege_scenes_begin, quick_battle_siege_scenes_end),
           #defender is player
           (store_random_in_range, "$g_presentation_obj_custom_battle_designer_7_last_value", 30, 100), #min 30% archer
           (store_sub, "$g_presentation_obj_custom_battle_designer_6_last_value", 100, "$g_presentation_obj_custom_battle_designer_7_last_value"),
           (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 0), #no cavalry
           (store_random_in_range, "$g_presentation_obj_custom_battle_designer_9_last_value", 20, 100), #min 20% infantry
           (store_sub, "$g_presentation_obj_custom_battle_designer_10_last_value", 100, "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 0), #no cavalry
         (try_end),
         (presentation_set_duration, 0),
         (start_presentation, "prsnt_ee_custom_battle_designer"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_2"),
         (assign, "$g_quick_battle_army_1_size", ":value"),
         (try_begin),
           (is_trial_version),
           (gt, "$g_quick_battle_army_1_size", 25),
           (assign, "$g_quick_battle_army_1_size", 25),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_2", 25),
         (try_end),
         (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_1_size"),
         (overlay_set_text, "$g_presentation_obj_custom_battle_designer_21", "str_reg0_men"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_3"),
         (assign, "$g_quick_battle_army_2_size", ":value"),
         (try_begin),
           (is_trial_version),
           (gt, "$g_quick_battle_army_2_size", 25),
           (assign, "$g_quick_battle_army_2_size", 25),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_3", 25),
         (try_end),
         (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_2_size"),
         (overlay_set_text, "$g_presentation_obj_custom_battle_designer_22", "str_reg0_men"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_4"),
         (try_begin),
           (store_sub, ":outlaw_index", "fac_enhanced_kingdom_1", npc_kingdoms_begin),
           (eq, ":value", ":outlaw_index"),
           (assign, "$g_quick_battle_team_1_faction", "fac_outlaws"),
         (else_try),
           (store_add, "$g_quick_battle_team_1_faction", ":value", npc_kingdoms_begin),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_5"),
         (try_begin),
           (store_sub, ":outlaw_index", "fac_enhanced_kingdom_1", npc_kingdoms_begin),
           (eq, ":value", ":outlaw_index"),
           (assign, "$g_quick_battle_team_2_faction", "fac_outlaws"),
         (else_try),
           (store_add, "$g_quick_battle_team_2_faction", ":value", npc_kingdoms_begin),
         (try_end),
         (presentation_set_duration, 0),
         (start_presentation, "prsnt_ee_custom_battle_designer"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_18"),
         (store_add, "$g_quick_battle_troop", ":value", quick_battle_troops_begin),
         (presentation_set_duration, 0),
         (start_presentation, "prsnt_ee_custom_battle_designer"),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_6"),
         (try_begin),
           (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
           (neq, ":value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
         (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_6_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_7_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_8_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_7_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_8_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_12", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_7_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_13", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_14", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_7"),
         (try_begin),
           (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
           (neq, ":value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
         (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_7_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_6_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_8_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_6_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_8_last_value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_8_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_12", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_7_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_13", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_14", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_8"),
           (try_begin),
             (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
             (neq, ":value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_8", "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_8_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_8_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_8_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_7_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_6_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_7_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_6_last_value", "$g_presentation_obj_custom_battle_designer_7_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_7_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_6_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_7_last_value", "$g_presentation_obj_custom_battle_designer_6_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_6_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_7", "$g_presentation_obj_custom_battle_designer_7_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_6", "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_6_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_12", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_7_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_13", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_8_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_14", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_9"),
         (try_begin),
           (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
           (neq, ":value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
         (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_9_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_10_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_11_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_10_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_11_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_15", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_10_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_16", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_17", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_10"),
         (try_begin),
           (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
           (neq, ":value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
         (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_10_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_9_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_11_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_9_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_11_last_value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_11_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_15", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_10_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_16", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_17", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_11"),
         (try_begin),
           (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
           (neq, ":value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (overlay_set_val, "$g_presentation_obj_custom_battle_designer_11", "$g_presentation_obj_custom_battle_designer_11_last_value"),
         (else_try),
           (try_begin),
             (lt, ":value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
             (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_11_last_value", ":value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":value"),
             (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", ":first_dif"),
             (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", ":second_dif"),
             (try_begin),
               (gt, "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", 100),
             (else_try),
               (gt, "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
               (store_sub, ":dif", "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
               (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", ":dif"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", 100),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (else_try),
             (gt, ":value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
             (store_sub, ":dif", ":value", "$g_presentation_obj_custom_battle_designer_11_last_value"),
             (try_begin),
               (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
               (assign, ":first_dif", 0),
               (assign, ":second_dif", ":dif"),
             (else_try),
               (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
               (assign, ":first_dif", ":dif"),
               (assign, ":second_dif", 0),
             (else_try),
               (store_div, ":first_dif", ":dif", 2),
               (store_sub, ":second_dif", ":dif", ":first_dif"),
               (try_begin),
                 (neq, ":first_dif", ":second_dif"),
                 (store_random_in_range, ":random_no", 0, 2),
                 (eq, ":random_no", 0),
                 (val_sub, ":second_dif", 1),
                 (val_add, ":first_dif", 1),
               (try_end),
             (try_end),
             (assign, "$g_presentation_obj_custom_battle_designer_11_last_value", ":value"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_10_last_value", ":first_dif"),
             (val_sub, "$g_presentation_obj_custom_battle_designer_9_last_value", ":second_dif"),
             (try_begin),
               (lt, "$g_presentation_obj_custom_battle_designer_10_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_9_last_value", "$g_presentation_obj_custom_battle_designer_10_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_10_last_value", 0),
             (else_try),
               (lt, "$g_presentation_obj_custom_battle_designer_9_last_value", 0),
               (val_add, "$g_presentation_obj_custom_battle_designer_10_last_value", "$g_presentation_obj_custom_battle_designer_9_last_value"),
               (assign, "$g_presentation_obj_custom_battle_designer_9_last_value", 0),
             (try_end),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_10", "$g_presentation_obj_custom_battle_designer_10_last_value"),
             (overlay_set_val, "$g_presentation_obj_custom_battle_designer_9", "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (try_end),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_9_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_15", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_10_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_16", "str_reg0_percent"),
           (assign, reg0, "$g_presentation_obj_custom_battle_designer_11_last_value"),
           (overlay_set_text, "$g_presentation_obj_custom_battle_designer_17", "str_reg0_percent"),
         (try_end),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_19"),
         (assign, "$g_is_quick_battle", 1),
         (assign, ":cur_scene", "$g_quick_battle_map"),
         (try_begin),
           (eq, "$g_quick_battle_game_type", 0), #battle
           (assign, ":cur_mission_template", "mt_quick_battle_battle"),
           (modify_visitors_at_site, ":cur_scene"),
           (call_script, "script_spawn_quick_battle_army", 0, "$g_quick_battle_team_1_faction", "$g_presentation_obj_custom_battle_designer_6_last_value", "$g_presentation_obj_custom_battle_designer_7_last_value", "$g_presentation_obj_custom_battle_designer_8_last_value", 0, 1),
           (call_script, "script_spawn_quick_battle_army", 16, "$g_quick_battle_team_2_faction", "$g_presentation_obj_custom_battle_designer_9_last_value", "$g_presentation_obj_custom_battle_designer_10_last_value", "$g_presentation_obj_custom_battle_designer_11_last_value", 0, 0),
         (else_try),
           (eq, "$g_quick_battle_game_type", 1), #siege offense
           (assign, ":cur_mission_template", "mt_quick_battle_siege"),
           (modify_visitors_at_site, ":cur_scene"),
           (call_script, "script_spawn_quick_battle_army", 16, "$g_quick_battle_team_1_faction", "$g_presentation_obj_custom_battle_designer_6_last_value", "$g_presentation_obj_custom_battle_designer_7_last_value", "$g_presentation_obj_custom_battle_designer_8_last_value", 0, 1),
           (call_script, "script_spawn_quick_battle_army", 0, "$g_quick_battle_team_2_faction", "$g_presentation_obj_custom_battle_designer_9_last_value", "$g_presentation_obj_custom_battle_designer_10_last_value", "$g_presentation_obj_custom_battle_designer_11_last_value", 1, 0),
         (else_try),
           #siege defense
           (assign, ":cur_mission_template", "mt_quick_battle_siege"),
           (modify_visitors_at_site, ":cur_scene"),
           (call_script, "script_spawn_quick_battle_army", 0, "$g_quick_battle_team_1_faction", "$g_presentation_obj_custom_battle_designer_6_last_value", "$g_presentation_obj_custom_battle_designer_7_last_value", "$g_presentation_obj_custom_battle_designer_8_last_value", 1, 1),
           (call_script, "script_spawn_quick_battle_army", 16, "$g_quick_battle_team_2_faction", "$g_presentation_obj_custom_battle_designer_9_last_value", "$g_presentation_obj_custom_battle_designer_10_last_value", "$g_presentation_obj_custom_battle_designer_11_last_value", 0, 0),
         (try_end),
         (set_jump_mission, ":cur_mission_template"),
         (jump_to_menu, "mnu_custom_battle_end"),
         (jump_to_scene, ":cur_scene"),
         (change_screen_mission),
         (presentation_set_duration, 0),
       (else_try),
         (eq, ":object", "$g_presentation_obj_custom_battle_designer_20"),
         (presentation_set_duration, 0),
       (try_end),
      ]),
    (ti_on_presentation_mouse_enter_leave,
     [
       (store_trigger_param_1, ":object"),
       (store_trigger_param_2, ":enter_leave"),
       (this_or_next|eq, ":object", "$g_presentation_obj_custom_battle_designer_6"),
       (this_or_next|eq, ":object", "$g_presentation_obj_custom_battle_designer_7"),
       (this_or_next|eq, ":object", "$g_presentation_obj_custom_battle_designer_8"),
       (this_or_next|eq, ":object", "$g_presentation_obj_custom_battle_designer_9"),
       (this_or_next|eq, ":object", "$g_presentation_obj_custom_battle_designer_10"),
       (eq, ":object", "$g_presentation_obj_custom_battle_designer_11"),
       (try_begin),
         (eq, ":enter_leave", 1),
         (try_begin),
           (eq, ":object", "$g_presentation_obj_custom_battle_last_mouse_over_object"),
           (assign, "$g_presentation_obj_custom_battle_last_mouse_over_object", -1),
         (try_end),
       (else_try),
         (assign, "$g_presentation_obj_custom_battle_last_mouse_over_object", ":object"),
       (try_end),
       ]),
    (ti_on_presentation_run,
     [
      (try_begin),
        (this_or_next|key_clicked, key_escape),
        (key_clicked, key_xbox_start),
        (presentation_set_duration, 0),
      (else_try),
        (key_clicked, key_right_mouse_button),
        (neq, "$g_presentation_obj_custom_battle_last_mouse_over_object", -1),
        (try_begin),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_6"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_6_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_6_locked", 1),
            (assign, "$g_presentation_obj_custom_battle_designer_7_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_8_locked", 0),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_6_locked", 0),
          (try_end),
        (else_try),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_7"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_7_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_6_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_7_locked", 1),
            (assign, "$g_presentation_obj_custom_battle_designer_8_locked", 0),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_7_locked", 0),
          (try_end),
        (else_try),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_8"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_8_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_6_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_7_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_8_locked", 1),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_8_locked", 0),
          (try_end),
        (else_try),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_9"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_9_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_9_locked", 1),
            (assign, "$g_presentation_obj_custom_battle_designer_10_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_11_locked", 0),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_9_locked", 0),
          (try_end),
        (else_try),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_10"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_10_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_9_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_10_locked", 1),
            (assign, "$g_presentation_obj_custom_battle_designer_11_locked", 0),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_10_locked", 0),
          (try_end),
        (else_try),
          (eq, "$g_presentation_obj_custom_battle_last_mouse_over_object", "$g_presentation_obj_custom_battle_designer_11"),
          (try_begin),
            (eq, "$g_presentation_obj_custom_battle_designer_11_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_9_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_10_locked", 0),
            (assign, "$g_presentation_obj_custom_battle_designer_11_locked", 1),
          (else_try),
            (assign, "$g_presentation_obj_custom_battle_designer_11_locked", 0),
          (try_end),
        (try_end),
      (try_end),
      ]),
    ]),
##############################################################################


########################## NEW v3.3 - new vassal player king notification
  ("lord_vassalage_notify", 0, mesh_load_window,
  [
    (ti_on_presentation_load,
    [
      (presentation_set_duration, 999999),
      (set_fixed_point_multiplier, 1000),
      (create_text_overlay, reg1, "@A new lord wants to join your kingdom!", tf_center_justify),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 695),
      (overlay_set_position, reg1, pos1),
	  
##################### First column
      (create_text_overlay, reg1, "@Name:", tf_left_align),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@Age:", tf_left_align),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 580),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@Renown:", tf_left_align),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 560),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@Controversy:", tf_left_align),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 540),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@Culture:", tf_left_align),
      (position_set_x, pos1, 400),
      (position_set_y, pos1, 520),
      (overlay_set_position, reg1, pos1),
	  
      # (create_text_overlay, reg1, "@Personality:", tf_center_justify),
      # (position_set_x, pos1, 400),
      # (position_set_y, pos1, 580),
      # (overlay_set_position, reg1, pos1),
#####################

##################### Second column
      (str_store_troop_name, s1, "$g_ee_cur_troop"),
      (troop_get_slot, reg20, "$g_ee_cur_troop", slot_troop_age),
      (troop_get_slot, reg21, "$g_ee_cur_troop", slot_troop_renown),
      (troop_get_slot, reg22, "$g_ee_cur_troop", slot_troop_controversy),
	  
      (troop_get_slot, ":troop_culture", "$g_ee_cur_troop", slot_troop_cur_culture),
      (assign, ":culture", "str_culture_1_adjective"),
      (val_add, ":culture", ":troop_culture"),
      (val_sub, ":culture", 6),
      (str_store_string, s2, ":culture"),
	  
      (create_text_overlay, reg1, s1, tf_left_align),
      (position_set_x, pos1, 490),
      (position_set_y, pos1, 600),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@{reg20}", tf_left_align),
      (position_set_x, pos1, 490),
      (position_set_y, pos1, 580),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@{reg21}", tf_left_align),
      (position_set_x, pos1, 490),
      (position_set_y, pos1, 560),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, "@{reg22}", tf_left_align),
      (position_set_x, pos1, 490),
      (position_set_y, pos1, 540),
      (overlay_set_position, reg1, pos1),
	  
      (create_text_overlay, reg1, s2, tf_left_align),
      (position_set_x, pos1, 490),
      (position_set_y, pos1, 520),
      (overlay_set_position, reg1, pos1),
##########################################
	  
##########################################
      # (create_mesh_overlay_with_tableau_material, reg1, -1, "tableau_lord_vassalage_notify", "$g_ee_cur_troop"),
      # (position_set_x, pos1, 200),
      # (position_set_y, pos1, 180),
      # (overlay_set_position, reg1, pos1),
      # (position_set_x, pos1, 900),
      # (position_set_y, pos1, 900),
      # (overlay_set_size, reg1, pos1),
	  
      (create_button_overlay, "$g_presentation_obj_1", "@Accept.", tf_center_justify),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 120),
      (overlay_set_position, "$g_presentation_obj_1", pos1),
	  
      (create_button_overlay, "$g_presentation_obj_2", "@Refuse.", tf_center_justify),
      (position_set_x, pos1, 500),
      (position_set_y, pos1, 90),
      (overlay_set_position, "$g_presentation_obj_2", pos1),
    ]),
    (ti_on_presentation_event_state_change,
    [
      (store_trigger_param_1, ":var0"),
      (try_begin),
        (eq, ":var0", "$g_presentation_obj_1"),
          (call_script, "script_ee_spawn_lord_party", "$g_ee_cur_troop", "$g_ee_cur_faction"), 
          (presentation_set_duration, 0),
          (change_screen_return),
      (else_try),
        (eq, ":var0", "$g_presentation_obj_2"),
          # (call_script, "script_recycle_lord", "$g_ee_cur_troop", "$g_ee_cur_faction"), 
          (presentation_set_duration, 0),
          (change_screen_return),
      (try_end),
    ]),
  ]),
########################### NEW v3.5
  ("troop_count", prsntf_read_only, 0,
  [
    (ti_on_presentation_load,
    [
      (presentation_set_duration, 999999),
      (set_fixed_point_multiplier, 1000),
	  #####################################
      (str_store_string, s1, "@Player: 0"),
      (create_text_overlay, "$g_presentation_obj_1", s1),
      (overlay_set_color, "$g_presentation_obj_1", 0xFFFFFF),
      (position_set_x, pos1, 505),
      (position_set_y, pos1, 710),
      (overlay_set_position, "$g_presentation_obj_1", pos1),
      (create_mesh_overlay, "$g_presentation_countbg1", "mesh_killcount"),
      (position_set_x, pos2, 500),
      (position_set_y, pos2, 768),
      (overlay_set_position, "$g_presentation_countbg1", pos2),
	  #####################################
      (str_store_string, s2, "@Ally: 0"),
      (create_text_overlay, "$g_presentation_obj_2", s2),
      (overlay_set_color, "$g_presentation_obj_2", 0xFFFFFF),
      (position_set_x, pos1, 705),
      (position_set_y, pos1, 710),
      (overlay_set_position, "$g_presentation_obj_2", pos1),
      (create_mesh_overlay, "$g_presentation_countbg2", "mesh_killcount"),
      (position_set_x, pos2, 700),
      (position_set_y, pos2, 768),
      (overlay_set_position, "$g_presentation_countbg2", pos2),
	  #####################################
      (str_store_string, s3, "@Enemy: 0"),
      (create_text_overlay, "$g_presentation_obj_3", s3),
      (overlay_set_color, "$g_presentation_obj_3", 0xFFFFFF),
      (position_set_x, pos1, 905),
      (position_set_y, pos1, 710),
      (overlay_set_position, "$g_presentation_obj_3", pos1),
      (create_mesh_overlay, "$g_presentation_countbg3", "mesh_killcount"),
      (position_set_x, pos2, 900),
      (position_set_y, pos2, 768),
      (overlay_set_position, "$g_presentation_countbg3", pos2),
	  #####################################
    ]),
    (ti_on_presentation_run,
    [
      (store_trigger_param_1, ":var0"),
      (set_fixed_point_multiplier, 1000),
      (assign, ":var1", 0),
      (assign, ":var2", 0),
      (assign, ":var3", 0),
      # (assign, ":var4", 0),
      (try_begin),
        (neq, "$g_option_ratio_bar_is_global", 1),
        (try_for_agents, ":var5"),
          (agent_is_human, ":var5"),
          (agent_is_alive, ":var5"),
          (agent_get_party_id, ":var6", ":var5"),
          (try_begin),
            (eq, ":var6", "p_main_party"),
            (val_add, ":var1", 1),
          (else_try),
            (agent_is_ally, ":var5"),
            (val_add, ":var2", 1),
          (else_try),
            (val_add, ":var3", 1),
          (try_end),
        (try_end),
      (else_try),
        (assign, ":var1", "$player_count_alive2"),
        (assign, ":var2", "$ally_count_alive2"),
        (assign, ":var3", "$enemy_count_alive2"),
      (try_end),
      (try_begin),
        (assign, reg3, "$player_count_alive2"),
        (assign, reg4, "$ally_count_alive2"),
        (assign, reg5, "$enemy_count_alive2"),
        (try_begin),
          (str_store_string, s1, "@Player: {reg3}"),
          (str_store_string, s2, "@Ally: {reg4}"),
          (str_store_string, s3, "@Enemy: {reg5}"),
        (try_end),
        (overlay_set_text, "$g_presentation_obj_1", s1),
        (overlay_set_text, "$g_presentation_obj_2", s2),
        (overlay_set_text, "$g_presentation_obj_3", s3),
      (try_end),
    ]),
  ]),
#################################################################


######################
]#####################
######################
# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        orig_presentations.extend(presentations) 
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)