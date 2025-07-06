from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *



####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [ #
  ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Welcome to Anno Domini 1257 - Enhanced Edition [v{s22}], a Mount & Blade: Warband mod. This mod attempts to reflect the reality of 13th century Europe. Before starting your game you need to choose the recruitment type for your game. Choose wisely, as you will not be able to change it after you start the game!",
    "none",
    [
    (str_store_string, s22, "str_mod_version"), ### NEW 3.11/3.9.2
    #(str_store_string, s22, "str_revision"),
    ],
    [
    #tom
     ("continue_feudal",[], "Start a new game, with the lance recruitment system.",
       [
       (assign, "$use_feudal_lance", 1),
       #feudal recruitment fill in the lances
       (jump_to_menu, "mnu_start_game_1"),
        ]
       ),
       #tom
       ("continue_native",[], "Start a new game, with the native Warband recruitment system.",
       [
       (assign, "$use_feudal_lance", 0),
       (jump_to_menu, "mnu_start_game_1"),
        ]
       ),
       
      ("go_back",[], "Go back.",
       [
         (change_screen_quit),
       ]),
    ]
  ),

  ("start_phase_2",mnf_disable_all_keys,
    "You hear about Europe, a land torn between rival kingdoms battling each other for supremacy, a haven for knights and mercenaries, cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory... In this land which holds great dangers and even greater opportunities, you believe you may leave your past behind and start a new life. You feel that finally, you hold the key of your destiny in your hands, free to choose as you will, and that whatever course you take, great adventures will await you. Drawn by the stories you hear about Europe and its kingdoms, you...",
    "none",
    [],
    [
      ("town_quest", [(eq, "$current_startup_quest_phase", 0),], "join a merchant caravan to travel to your destination.",
       [
         (try_begin),
           (eq, "$g_start_faction", "fac_kingdom_1"),
           (assign, "$current_town", "p_town_1_1"),
         (else_try),
           # (this_or_next|eq, "$g_start_faction", "fac_kingdom_2"),##KOMKE ????
           (eq, "$g_start_faction", "fac_kingdom_2"),
           (assign, "$current_town", "p_town_2_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_3"),
           (assign, "$current_town", "p_town_3_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_4"),
           (assign, "$current_town", "p_town_4_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_5"),
           (assign, "$current_town", "p_town_5_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_6"),
           (assign, "$current_town", "p_town_6_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_7"),
           (assign, "$current_town", "p_town_7_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_8"),
           (assign, "$current_town", "p_town_8_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_9"),
           (assign, "$current_town", "p_town_9_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_10"),
           (assign, "$current_town", "p_town_10_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_11"),
           (assign, "$current_town", "p_town_11_2"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_12"),
           (assign, "$current_town", "p_town_12_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_13"),
           (assign, "$current_town", "p_town_13_2"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_14"),
           (assign, "$current_town", "p_town_14_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_15"),
           (assign, "$current_town", "p_town_15_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_16"),
           (assign, "$current_town", "p_town_16_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_17"),
           (assign, "$current_town", "p_town_17_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_18"),
           (assign, "$current_town", "p_town_18_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_19"),
           (assign, "$current_town", "p_town_19_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_20"),
           (assign, "$current_town", "p_town_20_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_papacy"),
           (assign, "$current_town", "p_town_21_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_22"),
           (assign, "$current_town", "p_town_22_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_23"),
           (assign, "$current_town", "p_town_23_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_24"),
           (assign, "$current_town", "p_town_24_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_25"),
           (assign, "$current_town", "p_town_25_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_26"),
           (assign, "$current_town", "p_town_26_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_27"),
           (assign, "$current_town", "p_town_27_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_28"),
           (assign, "$current_town", "p_town_28_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_29"),
           (assign, "$current_town", "p_town_29_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_30"),
           (assign, "$current_town", "p_town_30_1"),
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_31"),
           (assign, "$current_town", "p_town_31_1"),  
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_32"),
           (assign, "$current_town", "p_town_32_1"),  
         (else_try),
           (this_or_next|eq, "$g_start_faction", "fac_kingdom_34"),
           (this_or_next|eq, "$g_start_faction", "fac_kingdom_35"),
           (this_or_next|eq, "$g_start_faction", "fac_kingdom_36"),
           (eq, "$g_start_faction", "fac_kingdom_33"),
           (assign, "$current_town", "p_town_2_1"),             
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_37"),
           (assign, "$current_town", "p_town_37_1"),    
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_38"),
           (assign, "$current_town", "p_town_38_1"),    
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_39"),
           (assign, "$current_town", "p_town_39_1"),    
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_40"),
           (assign, "$current_town", "p_town_40_1"),    
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_41"),
           (assign, "$current_town", "p_town_41_1"),    
         (else_try),
           (eq, "$g_start_faction", "fac_kingdom_42"),
           (assign, "$current_town", "p_town_42_1"),   
         (else_try),
           (store_random_in_range, "$current_town", towns_begin, towns_end),
         (try_end),
         (assign, "$g_starting_town", "$current_town"),
         #(assign, "$g_journey_string", "str_journey_to_praven"),
         (jump_to_menu, "mnu_start_phase_2_5"),
       ]),


       
##KAOS START AS NOBLE       
###########################################################################################

      ("town_1_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 1),
        (try_begin),
          (eq, "$teutonic_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_1", "p_castle_1_1", "fac_culture_teutonic", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord", "scn_town_1_room"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_1", "p_town_1_1", "fac_culture_teutonic", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$teutonic_culture", 1),
          (assign, "$current_town", "p_castle_1_1"),
        (else_try),
          (assign, "$current_town", "p_town_1_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_2_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 2),
        (try_begin),
          (eq, "$lithuania_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_2", "p_town_2_4", "fac_culture_baltic", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_2", "p_town_2_1", "fac_culture_baltic", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$lithuania_culture", 1),
          (assign, "$current_town", "p_town_2_4"),
        (else_try),
          (assign, "$current_town", "p_town_2_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_3_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 3),
        (try_begin),
          (eq, "$mongol_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_3", "p_castle_3_1", "fac_culture_mongol", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_3", "p_town_3_1", "fac_culture_mongol", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$mongol_culture", 1),
          (assign, "$current_town", "p_castle_3_1"),
        (else_try),
          (assign, "$current_town", "p_town_3_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_4_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 4),
        (try_begin),
          (eq, "$denmark_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_4", "p_town_4_3", "fac_culture_nordic", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_4", "p_town_4_1", "fac_culture_nordic", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_take_a_ship_home.",
      [
        (try_begin),
          (eq, "$denmark_culture", 1),
          (assign, "$current_town", "p_town_4_3"),
        (else_try),
          (assign, "$current_town", "p_town_4_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_5_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 5),
        (try_begin),
          (eq, "$poland_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_5", "p_castle_5_2", "fac_culture_western", "trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_5", "p_town_5_1", "fac_culture_western", "trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_take_a_ship_to_your_home.",
      [
        (try_begin),
          (eq, "$poland_culture", 1),
          (assign, "$current_town", "p_castle_5_2"),
        (else_try),
          (assign, "$current_town", "p_town_5_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_6_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 6),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_6", "p_town_6_1", "fac_culture_western", "trp_knight_6_1", "trp_knight_7_1", "trp_kingdom_6_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_6_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_7_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 7),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_7", "p_town_7_1", "fac_culture_western", "trp_knight_7_1", "trp_knight_8_1", "trp_kingdom_7_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_7_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_8_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 8),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_8", "p_town_8_1", "fac_culture_rus", "trp_knight_8_1", "trp_knight_9_1", "trp_kingdom_8_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_8_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_9_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 9),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_9", "p_town_9_1", "fac_culture_western", "trp_knight_9_1", "trp_knight_10_1", "trp_kingdom_9_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_9_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_10_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 10),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_10", "p_town_10_1", "fac_culture_western", "trp_knight_10_1", "trp_knight_11_1", "trp_kingdom_10_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_10_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_11_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 11),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_11", "p_town_11_1", "fac_culture_nordic", "trp_knight_11_1", "trp_knight_12_1", "trp_kingdom_11_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_11_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_12_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 12),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_12", "p_town_12_1", "fac_culture_scotish", "trp_knight_12_1", "trp_knight_13_1", "trp_kingdom_12_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_12_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_13_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 13),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_13", "p_town_13_1", "fac_culture_gaelic", "trp_knight_13_1", "trp_knight_14_1", "trp_kingdom_13_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_13_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_14_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 14),
        (try_begin),
          (eq, "$sweden_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_14", "p_town_14_2", "fac_culture_nordic", "trp_knight_14_1", "trp_knight_15_1", "trp_kingdom_14_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_14", "p_town_14_1", "fac_culture_nordic", "trp_knight_14_1", "trp_knight_15_1", "trp_kingdom_14_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$sweden_culture", 1),
          (assign, "$current_town", "p_town_14_2"),
        (else_try),
          (assign, "$current_town", "p_town_14_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_15_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 15),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_15", "p_town_15_1", "fac_culture_rus", "trp_knight_15_1", "trp_knight_16_1", "trp_kingdom_15_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_15_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_16_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 16),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_16", "p_town_16_1", "fac_culture_iberian", "trp_knight_16_1", "trp_knight_17_1", "trp_kingdom_16_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_16_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_17_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 17),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_17", "p_town_17_1", "fac_culture_iberian", "trp_knight_17_1", "trp_knight_18_1", "trp_kingdom_17_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_17_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_18_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 18),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_18", "p_town_18_1", "fac_culture_iberian", "trp_knight_18_1", "trp_knight_19_1", "trp_kingdom_18_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_18_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_19_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 19),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_19", "p_town_19_1", "fac_culture_western", "trp_knight_19_1", "trp_knight_20_1", "trp_kingdom_19_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_19_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_20_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 20),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_20", "p_town_20_1", "fac_culture_andalus", "trp_knight_20_1", "trp_knight_21_1", "trp_kingdom_20_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_20_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_21_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 21),
        (call_script, "script_set_player_kingdom_init", "fac_papacy", "p_town_21_1", "fac_culture_italian", "trp_knight_21_1", "trp_knight_22_1", "trp_pope", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_21_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_22_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 22),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_22", "p_town_22_1", "fac_culture_byzantium", "trp_knight_22_1", "trp_knight_23_1", "trp_kingdom_22_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_22_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_23_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 23),
        (try_begin),
          (eq, "$crusader_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_23", "p_town_23_2", "fac_culture_western", "trp_knight_23_1", "trp_knight_24_1", "trp_kingdom_23_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_23", "p_town_23_1", "fac_culture_western", "trp_knight_23_1", "trp_knight_24_1", "trp_kingdom_23_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$crusader_culture", 1),
          (assign, "$current_town", "p_town_23_2"),
        (else_try),
          (assign, "$current_town", "p_town_23_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_24_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 24),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_24", "p_town_24_1", "fac_culture_italian", "trp_knight_24_1", "trp_knight_25_1", "trp_kingdom_24_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_24_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_25_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 25),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_25", "p_town_25_1", "fac_culture_mamluke", "trp_knight_25_1", "trp_knight_26_1", "trp_kingdom_25_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_25_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_26_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 26),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_26", "p_town_26_1", "fac_culture_byzantium", "trp_knight_26_1", "trp_knight_27_1", "trp_kingdom_26_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_26_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_27_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 27),
        (try_begin),
          (eq, "$illkhanate_culture", 1),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_27", "p_castle_27_1", "fac_culture_mongol", "trp_knight_27_1", "trp_knight_28_1", "trp_kingdom_27_lord", "scn_castle_1_interior"),
        (else_try),
          (call_script, "script_set_player_kingdom_init", "fac_kingdom_27", "p_town_27_1", "fac_culture_mongol", "trp_knight_27_1", "trp_knight_28_1", "trp_kingdom_27_lord", "scn_castle_1_interior"),
        (try_end),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (try_begin),
          (eq, "$illkhanate_culture", 1),
          (assign, "$current_town", "p_castle_27_1"),
        (else_try),
          (assign, "$current_town", "p_town_27_1"),
        (try_end),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_28_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 28),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_28", "p_town_28_1", "fac_culture_marinid", "trp_knight_28_1", "trp_knight_29_1", "trp_kingdom_28_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_28_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_29_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 29),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_29", "p_town_29_1", "fac_culture_serbian", "trp_knight_29_1", "trp_knight_30_1", "trp_kingdom_29_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_29_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_30_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 30),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_30", "p_town_30_1", "fac_culture_balkan", "trp_knight_30_1", "trp_knight_31_1", "trp_kingdom_30_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_30_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_31_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 31),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_31", "p_town_31_1", "fac_culture_marinid", "trp_knight_31_1", "trp_knight_32_1", "trp_kingdom_31_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_31_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_32_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 32),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_32", "p_town_32_1", "fac_culture_iberian", "trp_knight_32_1", "trp_knight_33_1", "trp_kingdom_32_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_32_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_33_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 33),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_33", "p_castle_33_1", "fac_culture_baltic", "trp_knight_33_1", "trp_knight_34_1", "trp_kingdom_33_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_castle_33_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_34_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 34),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_34", "p_castle_34_1", "fac_culture_baltic", "trp_knight_34_1", "trp_knight_35_1", "trp_kingdom_34_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_castle_34_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_35_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 35),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_35", "p_castle_35_1", "fac_culture_baltic", "trp_knight_35_1", "trp_knight_36_1", "trp_kingdom_35_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_castle_35_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_36_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 36),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_36", "p_castle_36_1", "fac_culture_baltic", "trp_knight_36_1", "trp_knight_37_1", "trp_kingdom_36_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_castle_36_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_37_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 37),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_37", "p_town_37_1", "fac_culture_welsh", "trp_knight_37_1", "trp_knight_38_1", "trp_kingdom_37_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_37_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_38_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 38),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_38", "p_town_38_1", "fac_culture_italian", "trp_knight_38_1", "trp_knight_39_1", "trp_kingdom_38_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_38_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_39_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 39),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_39", "p_town_39_1", "fac_culture_italian", "trp_knight_39_1", "trp_knight_40_1", "trp_kingdom_39_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_39_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_40_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 40),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_40", "p_town_40_1", "fac_culture_italian", "trp_knight_40_1", "trp_knight_41_1", "trp_kingdom_40_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_40_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_41_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 41),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_41", "p_town_41_1", "fac_culture_italian", "trp_knight_41_1", "trp_knight_42_1", "trp_kingdom_41_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_41_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_42_king",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_kingdom", 42),
        (call_script, "script_set_player_kingdom_init", "fac_kingdom_42", "p_town_42_1", "fac_culture_western", "trp_knight_42_1", "trp_enhanced_rnd_lord_1", "trp_kingdom_42_lord", "scn_castle_1_interior"),
      ],
      "You_ride_a_caravan_to_your_home.",
      [
        (assign, "$current_town", "p_town_42_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_1_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 1),
        (call_script, "script_set_player_prince_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_1_prince_2",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 1),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_1_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "p_town_1_2", 2),
        (change_screen_return),
      ]
      ),

      ("town_2_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 2),
        (call_script, "script_set_player_prince_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_2_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 2),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_2_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_3_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 3),
        (call_script, "script_set_player_prince_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_3_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 3),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_3_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_4_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 4),
        (call_script, "script_set_player_prince_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_take_a_ship_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_4_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 4),
      ],
      "You_take_a_ship_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_4_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_5_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 5),
        (call_script, "script_set_player_prince_init", "fac_kingdom_5", "trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_take_a_ship_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_5_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 5),
      ],
      "You_take_a_ship_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_5_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_6_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 6),
        (call_script, "script_set_player_prince_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_7_1", "trp_kingdom_6_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_6_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 6),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_6_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_7_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 7),
        (call_script, "script_set_player_prince_init", "fac_kingdom_7", "trp_knight_7_1", "trp_knight_8_1", "trp_kingdom_7_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_7_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 7),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_7_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_8_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 8),
        (call_script, "script_set_player_prince_init", "fac_kingdom_8", "trp_knight_8_1", "trp_knight_9_1", "trp_kingdom_8_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_8_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 8),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_8_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_9_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 9),
        (call_script, "script_set_player_prince_init", "fac_kingdom_9", "trp_knight_9_1", "trp_knight_10_1", "trp_kingdom_9_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_9_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 9),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_9_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_10_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 10),
        (call_script, "script_set_player_prince_init", "fac_kingdom_10", "trp_knight_10_1", "trp_knight_11_1", "trp_kingdom_10_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_10_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 10),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_10_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_11_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 11),
        (call_script, "script_set_player_prince_init", "fac_kingdom_11", "trp_knight_11_1", "trp_knight_12_1", "trp_kingdom_11_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_11_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 11),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_11_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_12_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 12),
        (call_script, "script_set_player_prince_init", "fac_kingdom_12", "trp_knight_12_1", "trp_knight_13_1", "trp_kingdom_12_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_12_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 12),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_12_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_13_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 13),
        (call_script, "script_set_player_prince_init", "fac_kingdom_13", "trp_knight_13_1", "trp_knight_14_1", "trp_kingdom_13_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_13_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 13),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_13_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_14_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 14),
        (call_script, "script_set_player_prince_init", "fac_kingdom_14", "trp_knight_14_1", "trp_knight_15_1", "trp_kingdom_14_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_14_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 14),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_14_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_15_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 15),
        (call_script, "script_set_player_prince_init", "fac_kingdom_15", "trp_knight_15_1", "trp_knight_16_1", "trp_kingdom_15_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_15_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 15),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_15_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_16_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 16),
        (call_script, "script_set_player_prince_init", "fac_kingdom_16", "trp_knight_16_1", "trp_knight_17_1", "trp_kingdom_16_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_16_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 16),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_16_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_17_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 17),
        (call_script, "script_set_player_prince_init", "fac_kingdom_17", "trp_knight_17_1", "trp_knight_18_1", "trp_kingdom_17_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_17_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 17),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_17_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_18_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 18),
        (call_script, "script_set_player_prince_init", "fac_kingdom_18", "trp_knight_18_1", "trp_knight_19_1", "trp_kingdom_18_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_18_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 18),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_18_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_19_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 19),
        (call_script, "script_set_player_prince_init", "fac_kingdom_19", "trp_knight_19_1", "trp_knight_20_1", "trp_kingdom_19_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_19_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 19),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_19_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_20_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 20),
        (call_script, "script_set_player_prince_init", "fac_kingdom_20", "trp_knight_20_1", "trp_knight_21_1", "trp_kingdom_20_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_20_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 20),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_20_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_21_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 21),
        (call_script, "script_set_player_prince_init", "fac_papacy", "trp_knight_21_1", "trp_knight_22_1", "trp_pope"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_21_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 21),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_21_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_22_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 22),
        (call_script, "script_set_player_prince_init", "fac_kingdom_22", "trp_knight_22_1", "trp_knight_23_1", "trp_kingdom_22_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_22_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 22),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_22_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_23_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 23),
        (call_script, "script_set_player_prince_init", "fac_kingdom_23", "trp_knight_23_1", "trp_knight_24_1", "trp_kingdom_23_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_23_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 23),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_23_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_24_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 24),
        (call_script, "script_set_player_prince_init", "fac_kingdom_24", "trp_knight_24_1", "trp_knight_25_1", "trp_kingdom_24_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_24_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 24),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_24_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_25_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 25),
        (call_script, "script_set_player_prince_init", "fac_kingdom_25", "trp_knight_25_1", "trp_knight_26_1", "trp_kingdom_25_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_25_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 25),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_25_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_26_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 26),
        (call_script, "script_set_player_prince_init", "fac_kingdom_26", "trp_knight_26_1", "trp_knight_27_1", "trp_kingdom_26_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_26_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 26),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_26_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_27_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 27),
        (call_script, "script_set_player_prince_init", "fac_kingdom_27", "trp_knight_27_1", "trp_knight_28_1", "trp_kingdom_27_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_27_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 27),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_27_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_28_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 28),
        (call_script, "script_set_player_prince_init", "fac_kingdom_28", "trp_knight_28_1", "trp_knight_29_1", "trp_kingdom_28_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_28_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 28),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_28_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_29_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 29),
        (call_script, "script_set_player_prince_init", "fac_kingdom_29", "trp_knight_29_1", "trp_knight_30_1", "trp_kingdom_29_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_29_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 29),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_29_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_30_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 30),
        (call_script, "script_set_player_prince_init", "fac_kingdom_30", "trp_knight_30_1", "trp_knight_31_1", "trp_kingdom_30_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_30_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 30),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_30_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_31_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 31),
        (call_script, "script_set_player_prince_init", "fac_kingdom_31", "trp_knight_31_1", "trp_knight_32_1", "trp_kingdom_31_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_31_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 31),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_31_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_32_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 32),
        (call_script, "script_set_player_prince_init", "fac_kingdom_32", "trp_knight_32_1", "trp_knight_33_1", "trp_kingdom_32_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_32_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 32),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_32_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_33_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 33),
        (call_script, "script_set_player_prince_init", "fac_kingdom_33", "trp_knight_33_1", "trp_knight_34_1", "trp_kingdom_33_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_33_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 33),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_33_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_34_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 34),
        (call_script, "script_set_player_prince_init", "fac_kingdom_34", "trp_knight_34_1", "trp_knight_35_1", "trp_kingdom_34_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_34_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 34),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_34_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_35_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 35),
        (call_script, "script_set_player_prince_init", "fac_kingdom_35", "trp_knight_35_1", "trp_knight_36_1", "trp_kingdom_35_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_35_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 35),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_35_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_36_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 36),
        (call_script, "script_set_player_prince_init", "fac_kingdom_36", "trp_knight_36_1", "trp_knight_37_1", "trp_kingdom_36_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_36_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 36),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_36_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_37_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 37),
        (call_script, "script_set_player_prince_init", "fac_kingdom_37", "trp_knight_37_1", "trp_knight_38_1", "trp_kingdom_37_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_37_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 37),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_37_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_38_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 38),
        (call_script, "script_set_player_prince_init", "fac_kingdom_38", "trp_knight_38_1", "trp_knight_39_1", "trp_kingdom_38_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_38_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 38),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_38_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_39_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 39),
        (call_script, "script_set_player_prince_init", "fac_kingdom_39", "trp_knight_39_1", "trp_knight_40_1", "trp_kingdom_39_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_39_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 39),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_39_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_40_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 40),
        (call_script, "script_set_player_prince_init", "fac_kingdom_40", "trp_knight_40_1", "trp_knight_41_1", "trp_kingdom_40_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_40_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 40),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_40_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_41_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 41),
        (call_script, "script_set_player_prince_init", "fac_kingdom_41", "trp_knight_41_1", "trp_knight_42_1", "trp_kingdom_41_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_41_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 41),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_41_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_42_prince",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 42),
        (call_script, "script_set_player_prince_init", "fac_kingdom_42", "trp_knight_42_1", "trp_knight_1_1_wife", "trp_kingdom_42_lord"),
        (str_store_party_name, s55, "$kaos_prince_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "$kaos_prince_start"),
        (assign, "$g_starting_town", "$kaos_prince_start"),
        (party_relocate_near_party, "p_main_party", "$kaos_prince_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_42_prince_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_prince", 42),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_42_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),


      ("town_1_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 1),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_1", "trp_knight_1_1", "trp_knight_2_1", "trp_kingdom_1_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_1_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_1_vassal_2",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 1),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_1_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "p_castle_1_2", 2),
        (change_screen_return),
      ]
      ),

      ("town_2_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 2),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_2", "trp_knight_2_1", "trp_knight_3_1", "trp_kingdom_2_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_2_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_2_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 2),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_2_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_3_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 3),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_3", "trp_knight_3_1", "trp_knight_4_1", "trp_kingdom_3_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_3_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_3_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 3),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_3_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_4_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 4),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_4", "trp_knight_4_1", "trp_knight_5_1", "trp_kingdom_4_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_take_a_ship_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_4_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_4_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 4),
      ],
      "You_take_a_ship_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_4_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_5_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 5),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_5", "trp_knight_5_1", "trp_knight_6_1", "trp_kingdom_5_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_take_a_ship_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_5_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_5_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 5),
      ],
      "You_take_a_ship_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_5_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_6_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 6),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_6", "trp_knight_6_1", "trp_knight_7_1", "trp_kingdom_6_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_6_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_6_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 6),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_6_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_7_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 7),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_7", "trp_knight_7_1", "trp_knight_8_1", "trp_kingdom_7_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_7_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_7_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 7),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_7_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_8_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 8),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_8", "trp_knight_8_1", "trp_knight_9_1", "trp_kingdom_8_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_8_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_8_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 8),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_8_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_9_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 9),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_9", "trp_knight_9_1", "trp_knight_10_1", "trp_kingdom_9_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_9_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_9_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 9),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_9_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_10_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 10),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_10", "trp_knight_10_1", "trp_knight_11_1", "trp_kingdom_10_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_10_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_10_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 10),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_10_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_11_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 11),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_11", "trp_knight_11_1", "trp_knight_12_1", "trp_kingdom_11_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_11_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_11_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 11),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_11_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_12_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 12),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_12", "trp_knight_12_1", "trp_knight_13_1", "trp_kingdom_12_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_12_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_12_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 12),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_12_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_13_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 13),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_13", "trp_knight_13_1", "trp_knight_14_1", "trp_kingdom_13_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_13_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_13_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 13),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_13_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_14_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 14),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_14", "trp_knight_14_1", "trp_knight_15_1", "trp_kingdom_14_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_14_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_14_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 14),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_14_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_15_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 15),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_15", "trp_knight_15_1", "trp_knight_16_1", "trp_kingdom_15_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_15_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_15_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 15),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_15_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_16_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 16),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_16", "trp_knight_16_1", "trp_knight_17_1", "trp_kingdom_16_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_16_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_16_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 16),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_16_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_17_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 17),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_17", "trp_knight_17_1", "trp_knight_18_1", "trp_kingdom_17_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_17_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_17_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 17),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_17_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_18_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 18),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_18", "trp_knight_18_1", "trp_knight_19_1", "trp_kingdom_18_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_18_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_18_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 18),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_18_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_19_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 19),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_19", "trp_knight_19_1", "trp_knight_20_1", "trp_kingdom_19_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_19_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_19_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 19),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_19_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_20_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 20),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_20", "trp_knight_20_1", "trp_knight_21_1", "trp_kingdom_20_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_20_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_20_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 20),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_20_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_21_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 21),
        (call_script, "script_set_player_vassal_init", "fac_papacy", "trp_knight_21_1", "trp_knight_22_1", "trp_pope"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_town_21_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_21_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 21),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_21_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_22_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 22),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_22", "trp_knight_22_1", "trp_knight_23_1", "trp_kingdom_22_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_22_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_22_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 22),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_22_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_23_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 23),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_23", "trp_knight_23_1", "trp_knight_24_1", "trp_kingdom_23_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_23_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_23_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 23),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_23_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_24_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 24),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_24", "trp_knight_24_1", "trp_knight_25_1", "trp_kingdom_24_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_24_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_24_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 24),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_24_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_25_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 25),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_25", "trp_knight_25_1", "trp_knight_26_1", "trp_kingdom_25_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_25_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_25_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 25),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_25_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_26_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 26),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_26", "trp_knight_26_1", "trp_knight_27_1", "trp_kingdom_26_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_26_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_26_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 26),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_26_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_27_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 27),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_27", "trp_knight_27_1", "trp_knight_28_1", "trp_kingdom_27_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_27_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_27_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 27),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_27_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_28_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 28),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_28", "trp_knight_28_1", "trp_knight_29_1", "trp_kingdom_28_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_28_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_28_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 28),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_28_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_29_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 29),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_29", "trp_knight_29_1", "trp_knight_30_1", "trp_kingdom_29_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_29_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_29_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 29),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_29_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_30_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 30),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_30", "trp_knight_30_1", "trp_knight_31_1", "trp_kingdom_30_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_30_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_30_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 30),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_30_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_31_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 31),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_31", "trp_knight_31_1", "trp_knight_32_1", "trp_kingdom_31_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_31_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_31_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 31),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_31_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_32_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 32),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_32", "trp_knight_32_1", "trp_knight_33_1", "trp_kingdom_32_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_32_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_32_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 32),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_32_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_33_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 33),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_33", "trp_knight_33_1", "trp_knight_34_1", "trp_kingdom_33_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_33_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_33_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 33),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_33_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_34_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 34),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_34", "trp_knight_34_1", "trp_knight_35_1", "trp_kingdom_34_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_34_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_34_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 34),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_34_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_35_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 35),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_35", "trp_knight_35_1", "trp_knight_36_1", "trp_kingdom_35_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_35_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_35_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 35),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_35_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_36_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 36),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_36", "trp_knight_36_1", "trp_knight_37_1", "trp_kingdom_36_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_36_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_36_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 36),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_36_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_37_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 37),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_37", "trp_knight_37_1", "trp_knight_38_1", "trp_kingdom_37_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_37_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_37_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 37),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_37_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_38_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 38),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_38", "trp_knight_38_1", "trp_knight_39_1", "trp_kingdom_38_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_38_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_38_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 38),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_38_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_39_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 39),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_39", "trp_knight_39_1", "trp_knight_40_1", "trp_kingdom_39_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_castle_39_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_39_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 39),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_castle_39_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_40_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 40),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_40", "trp_knight_40_1", "trp_knight_41_1", "trp_kingdom_40_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_town_40_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_40_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 40),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_40_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_41_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 41),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_41", "trp_knight_41_1", "trp_knight_42_1", "trp_kingdom_41_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_town_41_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_41_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 41),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_41_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),

      ("town_42_vassal",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 42),
        (call_script, "script_set_player_vassal_init", "fac_kingdom_42", "trp_knight_42_1", "trp_knight_1_1_wife", "trp_kingdom_42_lord"),
        (str_store_party_name, s55, "$kaos_vasal_start"),
      ],
      "You_ride_a_caravan_home_to_{s55}.",
      [
        (assign, "$current_town", "p_town_42_1"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$kaos_vasal_start", 2),
        (change_screen_return),
      ]
      ),

      ("town_42_vassal_1",
      [
        (eq, "$current_startup_quest_phase", 0),
        (eq, "$kaos_kings_vassal", 42),
      ],
      "You_ride_a_caravan_to_your_other_home.",
      [
        (assign, "$current_town", "p_town_42_2"),
        (assign, "$g_starting_town", "$current_town"),
        (party_relocate_near_party, "p_main_party", "$g_starting_town", 2),
        (change_screen_return),
      ]
      ),


###########################################################################################       
       
       
       
      ("tutorial_cheat",
      [
        (eq, "$quickstart", 1),
      ],
      "{!}CHEAT!_(Quickstart)",
      [
        (assign, "$cheat_mode", 1),
        (change_screen_map),
        (set_show_messages, 0),
        (troop_raise_skill, "trp_player", 1, 10),
        (party_add_members, "p_main_party", "trp_mamluk_cavalry_2", 100),
        (party_add_members, "p_main_party", "trp_cuman_horse_archer", 60),
        (troop_add_gold, "trp_player", 99799999),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (set_show_messages, 1),
        (try_for_range, ":var0", "scn_town_arab_center", "scn_castle_walls_euro"),
          (scene_set_slot, ":var0", 0, 1),
        (try_end),
        (call_script, "script_get_player_party_morale_values"),
        (party_set_morale, "p_main_party", reg0),
      ]
      ),
    ]
  ),




  ("start_game_3", 0,
    "Choose your scenario:",
    "none",
    [
      (assign, "$g_custom_battle_scenario", 0),
      (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
    ],
    [
      ("go_back",
      [],
      "Go_back.",
      [
        (change_screen_quit),
      ]
      ),
    ],
  ),


  ("tutorial",mnf_disable_all_keys,
    "You approach a field where the locals are training with weapons. You can practice here to improve your combat skills.",
    "none",
    [
      (try_begin),
        (eq, "$g_tutorial_entered", 1),
        (change_screen_quit),
      (else_try),
        (set_passage_menu, "mnu_tutorial"),
##        (try_begin),
##          (eq, "$tutorial_1_finished", 1),
##          (str_store_string, s1, "str_finished"),
##        (else_try),
##          (str_store_string, s1, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_2_finished", 1),
##          (str_store_string, s2, "str_finished"),
##        (else_try),
##          (str_store_string, s2, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_3_finished", 1),
##          (str_store_string, s3, "str_finished"),
##        (else_try),
##          (str_store_string, s3, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_4_finished", 1),
##          (str_store_string, s4, "str_finished"),
##        (else_try),
##          (str_store_string, s4, "str_empty_string"),
##        (try_end),
##        (try_begin),
##          (eq, "$tutorial_5_finished", 1),
##          (str_store_string, s5, "str_finished"),
##        (else_try),
##          (str_store_string, s5, "str_empty_string"),
##        (try_end),
        (assign, "$g_tutorial_entered", 1),
      (try_end),
    ],
    [
##      ("tutorial_1",
##      [(eq,1,0),],
##      "Tutorial #1: Basic movement and weapon selection. {s1}",
##      [
##        #(modify_visitors_at_site, "scn_tutorial_1"),(reset_visitors,0),
####           (set_jump_mission, "mt_tutorial_1"),
####           (jump_to_scene, "scn_tutorial_1"),(change_screen_mission)]),
##      ]),
##
##      ("tutorial_2",[(eq,1,0),], "Tutorial #2: Fighting with a shield. {s2}",[
####           (modify_visitors_at_site, "scn_tutorial_2"),(reset_visitors,0),
####           (set_visitor,1, "trp_tutorial_maceman"),
####           (set_visitor,2, "trp_tutorial_archer"),
####           (set_jump_mission, "mt_tutorial_2"),
####           (jump_to_scene, "scn_tutorial_2"),(change_screen_mission)]),
##           (modify_visitors_at_site, "scn_tutorial_training_ground"),
##           (reset_visitors, 0),
##           (set_player_troop, "trp_player"),
##           (set_visitor,0, "trp_player"),
##           (set_jump_mission, "mt_ai_training"),
##           (jump_to_scene, "scn_tutorial_training_ground"),
##           (change_screen_mission)]),
##
##      ("tutorial_3",[(eq,1,0),], "Tutorial #3: Fighting without a shield. {s3}",[
##           (modify_visitors_at_site, "scn_tutorial_3"),(reset_visitors,0),
##           (set_visitor,1, "trp_tutorial_maceman"),
##           (set_visitor,2, "trp_tutorial_swordsman"),
##           (set_jump_mission, "mt_tutorial_3"),
##           (jump_to_scene, "scn_tutorial_3"),(change_screen_mission)]),
##      ("tutorial_3b",[(eq,0,1)], "Tutorial 3 b",[(try_begin),
##                                                  (ge, "$tutorial_3_state", 12),
##                                                  (modify_visitors_at_site, "scn_tutorial_3"),(reset_visitors,0),
##                                                  (set_visitor,1, "trp_tutorial_maceman"),
##                                                  (set_visitor,2, "trp_tutorial_swordsman"),
##                                                  (set_jump_mission, "mt_tutorial_3_2"),
##                                                  (jump_to_scene, "scn_tutorial_3"),
##                                                  (change_screen_mission),
##                                                (else_try),
##                                                  (display_message, "str_door_locked",0xFFFFAAAA),
##                                                (try_end)], "Next level"),
##      ("tutorial_4",[(eq,1,0),], "Tutorial #4: Riding a horse. {s4}",[
##           (modify_visitors_at_site, "scn_tutorial_training_ground"),
##           (reset_visitors, 0),
##           (set_player_troop, "trp_player"),
##           (assign, "$g_player_troop", "trp_player"),
##           (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
##           (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
##           (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
##           (troop_raise_skill, "$g_player_troop", skl_shield, 3),
##           (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
##           (troop_raise_skill, "$g_player_troop", skl_riding, 3),
##           (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
##           (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
##           (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
##           (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
##           (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
##           (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),
##
##        (troop_clear_inventory, "$g_player_troop"),
##        (troop_add_item, "$g_player_troop", "itm_leather_jerkin",0),
##        (troop_add_item, "$g_player_troop", "itm_leather_boots",0),
##        (troop_add_item, "$g_player_troop", "itm_practice_sword",0),
##        (troop_add_item, "$g_player_troop", "itm_quarter_staff",0),
##        (troop_equip_items, "$g_player_troop"),
##        (set_visitor,0, "trp_player"),
##        (set_visitor,32, "trp_tutorial_fighter_1"),
##        (set_visitor,33, "trp_tutorial_fighter_2"),
##        (set_visitor,34, "trp_tutorial_fighter_3"),
##        (set_visitor,35, "trp_tutorial_fighter_4"),
##        (set_visitor,40, "trp_tutorial_master_archer"),
##        (set_visitor,41, "trp_tutorial_archer_1"),
##        (set_visitor,42, "trp_tutorial_archer_1"),
##        (set_visitor,60, "trp_tutorial_master_horseman"),
##        (set_visitor,61, "trp_tutorial_rider_1"),
##        (set_visitor,62, "trp_tutorial_rider_1"),
##        (set_visitor,63, "trp_tutorial_rider_2"),
##        (set_visitor,64, "trp_tutorial_rider_2"),
##        (set_jump_mission, "mt_tutorial_training_ground"),
##        (jump_to_scene, "scn_tutorial_training_ground"),
##        (change_screen_mission),
##      ]),
##
##      ("tutorial_5",
##      [
##        (eq,1,0),
##      ],
##      "Tutorial #5: Commanding a band of soldiers. {s5}",
##      [
##        (modify_visitors_at_site, "scn_tutorial_5"),(reset_visitors,0),
##        (set_visitor,0, "trp_player"),
##        (set_visitor,1, "trp_vaegir_infantry"),
##        (set_visitor,2, "trp_vaegir_infantry"),
##        (set_visitor,3, "trp_vaegir_infantry"),
##        (set_visitor,4, "trp_vaegir_infantry"),
##        (set_jump_mission, "mt_tutorial_5"),
##        (jump_to_scene, "scn_tutorial_5"),
##        (change_screen_mission),
##      ]),
##
##      ("tutorial_edit_custom_battle_scenes",
##      [(eq,1,0),],
##      "(NO TRANSLATE) tutorial_edit_custom_battle_scenes",
##      [
##        (jump_to_menu, "mnu_custom_battle_scene"),
##      ]),

      ("continue",[], "Continue...",
      [
        (modify_visitors_at_site, "scn_tutorial_training_ground"),
        (reset_visitors, 0),
        (set_player_troop, "trp_player"),
        (assign, "$g_player_troop", "trp_player"),
        (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
        (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
        (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
        (troop_raise_skill, "$g_player_troop", skl_shield, 3),
        (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
        (troop_raise_skill, "$g_player_troop", skl_riding, 3),
        (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
        (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
        (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
        (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
        (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
        (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),

        (troop_clear_inventory, "$g_player_troop"),
        (troop_add_item, "$g_player_troop", "itm_leather_jerkin",0),
        (troop_add_item, "$g_player_troop", "itm_leather_boots",0),
        (troop_add_item, "$g_player_troop", "itm_practice_sword",0),
        (troop_add_item, "$g_player_troop", "itm_quarter_staff",0),
        (troop_equip_items, "$g_player_troop"),
        (set_visitor,0, "trp_player"),
        (set_visitor,32, "trp_tutorial_fighter_1"),
        (set_visitor,33, "trp_tutorial_fighter_2"),
        (set_visitor,34, "trp_tutorial_fighter_3"),
        (set_visitor,35, "trp_tutorial_fighter_4"),
        (set_visitor,40, "trp_tutorial_master_archer"),
        (set_visitor,41, "trp_tutorial_archer_1"),
        (set_visitor,42, "trp_tutorial_archer_1"),
        (set_visitor,60, "trp_tutorial_master_horseman"),
        (set_visitor,61, "trp_tutorial_rider_1"),
        (set_visitor,62, "trp_tutorial_rider_1"),
        (set_visitor,63, "trp_tutorial_rider_2"),
        (set_visitor,64, "trp_tutorial_rider_2"),
        (set_jump_mission, "mt_tutorial_training_ground"),
        (jump_to_scene, "scn_tutorial_training_ground"),
        (change_screen_mission),
        ]),

  # rafi scene chooser
      ("choose_scene",[], "Scene Chooser",
        [(jump_to_menu, "mnu_choose_scenes_0"),]
      ),
  # end rafi

      ("go_back_dot",
      [],
      "Go back.",
       [
         (change_screen_quit),
       ]),
    ]
  ),

  ("reports",0,
   # "Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
   "Mod Version: v{s22}^^Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (assign, reg5, ":renown"),
    (assign, reg6, "$player_honor"),
    (assign, reg7, ":party_size_limit"),
    (str_store_string, s22, "str_mod_version"), ### NEW 3.11/3.9.2 - 
    #(str_store_string, s22, "str_revision"), ### NEW 3.11/3.9.2 - 
    #(call_script, "script_get_player_party_morale_values"),
    #(party_set_morale, "p_main_party", reg0),
    (party_get_morale, reg8, "p_main_party"),
   ],
    [
    
    
    

    
      ("cheat_faction_orders",[(ge, "$cheat_mode",1)], "{!}Cheat: Faction orders.",
       [(jump_to_menu, "mnu_faction_orders"),
        ]
       ),
       
	   ################## NEW v2.1 -  RUBIK'S PERFECT TROOP TREE PRESENTATION 
	   ## CC
       ("action_view_troop_trees_1",[], "View troop trees.",
        [
         (start_presentation, "prsnt_faction_troop_trees_1"),
         ]
        ),
		
       ("action_view_troop_trees_2",[], "View troop trees (Cont.).",
        [
         (start_presentation, "prsnt_faction_troop_trees_2"),
         ]
        ),
       ## CC
	   ######################################################
       
       
      ("view_character_report",[], "View character report.",
       [(jump_to_menu, "mnu_character_report"),
        ]
       ),
      ("view_party_size_report",[], "View party size report.",
       [(jump_to_menu, "mnu_party_size_report"),
        ]
       ),

      ("view_npc_mission_report",[], "View companion mission report.",
       [(jump_to_menu, "mnu_companion_report"),
        ]
       ),

      ("view_weekly_budget_report",[], "View weekly budget report.",
       [
         (assign, "$g_apply_budget_report_to_gold", 0),
         (start_presentation, "prsnt_budget_report"),
        ]
       ),

      ("view_morale_report",[], "View party morale report.",
       [(jump_to_menu, "mnu_morale_report"),
        ]
       ),


#################################### NEW v2.1 -  Faction statistics
	   ## CC
       ("faction_statistics_1",
	   [
       (gt, "$g_current_factions_active", 0),
	   ], "View faction statistics (Part I).",
        [
         (assign, "$g_misc_current_statistics_menu", 1),
         (start_presentation, "prsnt_ee_faction_statistics"),
         ]
        ),
		
       ("faction_statistics_2",
	   [
       (gt, "$g_current_factions_active", 20),
	   ], "View faction statistics (Part II).",
        [
         (assign, "$g_misc_current_statistics_menu", 2),
         (start_presentation, "prsnt_ee_faction_statistics"),
         ]
        ),
		
       ("faction_statistics_3",
	   [
       (gt, "$g_current_factions_active", 43),
	   ], "View faction statistics (Part III).",
        [
         (assign, "$g_misc_current_statistics_menu", 3),
         (start_presentation, "prsnt_ee_faction_statistics"),
         ]
        ),
		
       # ("faction_statistics_4",
	   # [
       # (gt, "$g_current_factions_active", 55),
	   # ], "View faction statistics (Part IV).",
        # [
         # (assign, "$g_misc_current_statistics_menu", 4),
         # (start_presentation, "prsnt_ee_faction_statistics"),
         # ]
        # ),
       ## CC
########################################################################
       
       
	   
	   
#NPC companion changes begin
      ("lord_relations",[], "View list of known lords by relation.",
       [
        (jump_to_menu, "mnu_lord_relations"),
        ]
       ),

      ("courtship_relations",[], "View courtship relations.",
       [
        (jump_to_menu, "mnu_courtship_relations"),
        ]
       ),

      ("status_check",[(eq, "$cheat_mode",1)], "{!}NPC status check.",
       [
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (str_store_troop_name, 4, ":npc"),
            (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
            (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
            (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),
            (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),
            (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),
            (display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
        (try_end),
        ]
       ),

#NPC companion changes end

      ("view_faction_relations_report",[], "View faction relations report.",
       [(jump_to_menu, "mnu_faction_relations_report"),
        ]
       ),
      ("resume_travelling",[], "Resume travelling.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("custom_battle_scene",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "(NO_TRANS)",

    "none",
    [],
    [

      ("quick_battle_scene_1",[], "{!}quick_battle_scene_1",
       [
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, "scn_quick_battle_scene_1"),(change_screen_mission)
        ]
       ),
      ("quick_battle_scene_2",[], "{!}quick_battle_scene_2",
       [
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, "scn_quick_battle_scene_2"),(change_screen_mission)
        ]
       ),
      ("quick_battle_scene_3",[], "{!}quick_battle_scene_3",
       [
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, "scn_quick_battle_scene_3"),(change_screen_mission)
        ]
       ),
      ("quick_battle_scene_4",[], "{!}quick_battle_scene_4",
       [
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, "scn_quick_battle_scene_4"),(change_screen_mission)
        ]
       ),
      ("quick_battle_scene_5",[], "{!}quick_battle_scene_5",
       [
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, "scn_quick_battle_scene_5"),(change_screen_mission)
        ]
       ),

      ("go_back",[], "{!}Go back.",
       [(change_screen_quit),
        ]
       ),
      ]
  ),

 
  ("custom_battle_end",mnf_disable_all_keys,
    "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting.",
    "none",
    [(music_set_situation, 0),
     (assign, reg5, "$g_custom_battle_team2_death_count"),
     (assign, reg6, "$g_custom_battle_team1_death_count"),
     (get_player_agent_kill_count, ":kill_count"),
     (get_player_agent_kill_count, ":wound_count", 1),
     (store_add, reg7, ":kill_count", ":wound_count"),
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s1, "str_battle_won"),
     (else_try),
       (str_store_string, s1, "str_battle_lost"),
     (try_end),

     (try_begin),
       (ge, "$g_custom_battle_team2_death_count", 100),
       (unlock_achievement, ACHIEVEMENT_LOOK_AT_THE_BONES),
     (try_end),
     ],
    [
      ("continue",[], "Continue.",
       [(change_screen_quit),
        ]
       ),
    ]
  ),

  ("start_game_1", menu_text_color(0xFF000000),
    "Select your character's gender.",
    "none",
    [
      (assign, "$kaos_kings_kingdom", 0),
      (assign, "$kaos_kings_vassal", 0),
      (assign, "$kaos_kings_prince", 0),
      (assign, "$kaos_monarch_var", 0),
      (assign, "$kaos_heir", 0),
      (assign, "$start_as_vassal_gvar1", 0),
      (assign, "$teutonic_culture", 0),
      (assign, "$lithuania_culture", 0),
      (assign, "$mongol_culture", 0),
      (assign, "$denmark_culture", 0),
      (assign, "$poland_culture", 0),
      (assign, "$sweden_culture", 0),
      (assign, "$crusader_culture", 0),
      (assign, "$illkhanate_culture", 0),
      (assign, "$bandit_start", 0),
      (try_begin),
        (eq, "$cvw_start", 2),
        (assign, "$kaos_restore", 1),
      (else_try),
        (assign, "$kaos_restore", 0),
      (try_end),
      (str_clear, s10),
      (str_clear, s11),
      (str_clear, s12),
      (str_clear, s13),
      (str_clear, s14),
      (str_clear, s15),
      # (try_begin),
        # (eq, "$culture_pool_initialized", 0),
        # (call_script, "script_initialize_culture_pools"),
        # (assign, "$culture_pool_initialized", 1),
      # (try_end),
      # (try_begin),
        # (eq, "$culture_pool", 0),
        # (assign, "$culture_pool", 1),
        # (call_script, "script_rebalance_troops_by_culture"),
      # (try_end),
    ],
    [
      ("start_male",
        [], "Male.",
        [
          (troop_set_type, "trp_player", 0),
          (assign, "$character_gender", 0),
          (try_begin),
            (eq, "$quickstart", 0),
            (jump_to_menu, "mnu_start_game_new_2dot1"),
          (else_try),
            (jump_to_menu, "mnu_start_game_new_2dot1"),
          (try_end),
        ]
      ),

      ("start_female", ### Moved the female character start above "Quick Character" (NEW v3.9.3, by Khanor)
        [], "Female.",
        [
          (troop_set_type, "trp_player", 1),
          (assign, "$character_gender", 1),
          (try_begin),
            (eq, "$quickstart", 0),
            (jump_to_menu, "mnu_start_game_new_2dot1"),
          (else_try),
            (jump_to_menu, "mnu_start_game_new_2dot1"),
          (try_end),
        ]
      ),

      ### MF for testing start ### NEW v2.9-KOMKE
      ("start_mod",[(eq,1,1),],"Quick Character (for mod testing).",## when releasing new version set this to false so it is disabled
        [
          (troop_set_type,"trp_player",0),
          (assign,"$character_gender",tf_male),
          (troop_raise_attribute, "trp_player",ca_intelligence,-4), #so you dont need to wait time picking extra skills         
          (change_screen_return, 0),
        ]
      ),
      ### MF for testing end ###

      ("enable_quickstart",
      [
        (eq, "$quickstart", 0),
        (eq, 0, 1),
      ],
      "Enable_quickstart_(this_is_useful_for_debugging_only)",
      [
        (assign, "$quickstart", 1),
        (jump_to_menu, "mnu_start_game_new_2dot1"),
      ]
      ),

      ("disable_quickstart",
      [
        (gt, "$quickstart", 0),
      ],
      "Disable_quickstart_(this_is_useful_for_debugging_only)",
      [
        (assign, "$quickstart", 0),
        (jump_to_menu, "mnu_start_game_new_2dot1"),
      ]
      ),

      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_0"),
      ]
      ),
    ],
  ),

  
	  

################################### NEW v2.1 - choose wage system  
  ("start_game_new_2dot1", menu_text_color(0xFF000000),
    "Use 1257AD wage system, or the Native-friendly wages system? ^Note: 1257AD wage system is recommended for Windows players, and Native-friendly wage system for Mac/Linux. If you are a MAC/LINUX user make sure to choose the Native-friendly wage system, otherwise your troops will have buggy wages every once in a while, putting you in debt of billions.^(Note: Can be changed later in the EE Misc. Options under Camp)",
    "none",
    [],
    [
      ("suffix_yes_1",
      [],
      "1257AD_wage_system_(Windows).",
      [
        (assign, "$native_wages", 0),
        (jump_to_menu, "mnu_start_game_new_2dot1_2"),
      ]
      ),

      ("suffix_no_1",
      [],
      "Native_wage_system_(Mac_&_Linux).",
      [
        (assign, "$native_wages", 1),
        (jump_to_menu, "mnu_start_game_new_2dot1_2"),
      ]
      ),
	  
      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_0"),
      ]
      ),
    ],
  ),
######################################################################


################################### NEW v2.1 - turn those things on or off at the beggining	  
  ("start_game_new_2dot1_2", menu_text_color(0xFF000000),
    "Turn lord killing on?^If turned on lords have a chance to die in battle, get executed or assassinated by other lords or the player.^(Note: Can be changed later in the EE Misc. Options under Camp)",
    "none",
    [],
    [
      ("suffix_yes_2",
      [],
      "Yes.",
      [
        (jump_to_menu, "mnu_start_game_new_2dot1_3"),
      ]
      ),

      ("suffix_no_2",
      [],
      "No.",
      [
        (assign, "$g_lord_death_chance_battle", 0),
        (assign, "$g_lord_death_chance_battle_king", 0),
        (assign, "$g_lord_death_chance_assassination", 0), 
        (assign, "$g_lord_death_chance_assassination_king", 0),   
        (assign, "$g_lord_death_chance_execution_base", 0),
        (assign, "$g_lord_death_chance_execution_king_variation", 0),
        (assign, "$g_lord_death_chance_execution_relation_divider", 3),
        (jump_to_menu, "mnu_start_game_new_2dot1_3"),
      ]
      ),
	  
      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_new_2dot1"),
      ]
      ),
    ],
  ),
  
	  
  ("start_game_new_2dot1_3", menu_text_color(0xFF000000),
    "Turn lord creation on?^If turned on factions will get randomly generated lords based on their current fief count.^(Note: Can be changed later in the EE Misc. Options under Camp)",
    "none",
    [],
    [
      ("suffix_yes",
      [],
      "Yes.",
      [
        (jump_to_menu, "mnu_start_game_new_1dot9"),
      ]
      ),

      ("suffix_no",
      [],
      "No. Turn it off.",
      [
        (assign, "$g_lord_creation_rate", 0), #### turns it off
        (jump_to_menu, "mnu_start_game_new_1dot9"),
      ]
      ),
	  
      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_new_2dot1_2"),
      ]
      ),
    ],
  ),
################################### 
  
  
  
################################# NEW v1.9 - TOTAL WAR 
  ("start_game_new_1dot9", menu_text_color(0xFF000000),
    "Do you want to start with Total War mode on? If turned on it will cause all factions to start at war with all other neighbouring factions. Obviously not historically accurate. If it's off then vanilla faction relations are used.",
    "none",
    [
    ],
    [
      ("start_game_new_1dot9_yes",
      [],
      "YES! Turn it on.",
      [
        (set_show_messages, 0),
        (try_for_range, ":cur_kingdom", npc_kingdoms_begin, npc_kingdoms_end),  ######### NEW v2.8 - fixed player starting as adventurer and being at war with all faction when total war mode was on
          (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
            (try_for_range, ":cur_kingdom_2", npc_kingdoms_begin, npc_kingdoms_end),
              (neq, ":cur_kingdom", ":cur_kingdom_2"),
              (faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),
              (store_relation, ":cur_relation", ":cur_kingdom", ":cur_kingdom_2"),
              (call_script, "script_distance_between_factions", ":cur_kingdom", ":cur_kingdom_2"),
              (assign, ":fac_distance", reg0),
              
              (try_begin),
                (gt, ":cur_relation", -10), #NOT AT WAR
                # (this_or_next | eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
                (le, ":fac_distance", 30),
                
                (try_begin),
                  (eq, "$g_include_diplo_explanation", 0),
                  (assign, "$g_include_diplo_explanation", ":cur_kingdom"),
                  (str_store_string, s57, "str_s14"),
                (try_end),
               
                (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", 1),
             (try_end),
          (try_end),
        (try_end),
        (set_show_messages, 1),
        (try_begin),
          (eq, "$quickstart", 0),
          (jump_to_menu, "mnu_start_game_new_spawn_presets"),
        (else_try),
          (jump_to_menu, "mnu_start_game_new_spawn_presets"),
        (try_end),
      ]
      ),

      ("start_game_new_1dot9_no",
      [],
      "No. Start with it off.",
      [
        (try_begin),
          (eq, "$quickstart", 0),
          (jump_to_menu, "mnu_start_game_new_spawn_presets"),
        (else_try),
          (jump_to_menu, "mnu_start_game_new_spawn_presets"),
        (try_end),
      ]
      ),

      ("enable_quickstart",
      [
        (eq, "$quickstart", 0),
        (eq, 0, 1),
      ],
      "Enable_quickstart_(this_is_useful_for_debugging_only)",
      [
        (assign, "$quickstart", 1),
        (jump_to_menu, "mnu_start_game_new_spawn_presets"),
      ]
      ),

      ("disable_quickstart",
      [
        (gt, "$quickstart", 0),
      ],
      "Disable_quickstart_(this_is_useful_for_debugging_only)",
      [
        (assign, "$quickstart", 0),
        (jump_to_menu, "mnu_start_game_new_spawn_presets"),
      ]
      ),

      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_new_2dot1_3"),
      ]
      ),
    ],
  ),
##################################################################
  
  
################################# NEW v3.0 - SPAWN PRESETS
  ("start_game_new_spawn_presets", menu_text_color(0xFF000000),
    "What spawn preset do you wish to use? (Spawn presets affect the maximum amount of parties like bandits that can exist in the map at one time. Since warband only runs on a single core the only thing that matters for it cpu wise is clock speed. Below are the recommended speeds in GHz.)",
    "none",
    [
    ],
    [
      ("start_game_new_spawn_presets_1",
      [],
      "Very Light (50% less)(2.5GHz)",
      [
      (assign, "$g_party_faction_max_parties_foragers", 1),
      (assign, "$g_party_faction_max_parties_scouts", 1),
      (assign, "$g_party_faction_max_parties_patrols", 1),
      (assign, "$g_party_faction_max_parties_caravans", 1),
      (assign, "$g_party_faction_max_parties_prisoner_trains", 0),
      (assign, "$g_party_faction_max_parties_war_parties", 0),
      (assign, "$g_party_faction_max_parties_mercenary_companies", 0),
	  
      (assign, "$g_party_bandit_max_parties_looter", 25),
      (assign, "$g_party_bandit_max_parties_sea_raider", 15),
      (assign, "$g_party_bandit_max_parties_mountain_bandits", 20),
      (assign, "$g_party_bandit_max_parties_steppe_bandits", 15),
      (assign, "$g_party_bandit_max_parties_taiga_bandits", 15),
      (assign, "$g_party_bandit_max_parties_forest_bandits", 20),
      (assign, "$g_party_bandit_max_parties_desert_bandits", 15),
      (assign, "$g_party_bandit_max_parties_deserters", 30),
      (assign, "$g_party_bandit_max_parties_roving_knights", 5),
      (assign, "$g_party_mercenary_company_max", 5),
      (assign, "$g_party_rebellion_max", 2),
      (assign, "$g_party_rebellion_strong_max", 2),
      (assign, "$g_party_fugitive_serf_max", 10),
      (assign, "$g_party_mercenary_warband_max", 20),
	  
      (jump_to_menu, "mnu_start_game_new_3dot10"),
      ]
      ),
	  
      ("start_game_new_spawn_presets_2",
      [],
      "Light (25% less)(3.0GHz)",
      [
      (assign, "$g_party_faction_max_parties_foragers", 1),
      (assign, "$g_party_faction_max_parties_scouts", 2),
      (assign, "$g_party_faction_max_parties_patrols", 1),
      (assign, "$g_party_faction_max_parties_caravans", 1),
      (assign, "$g_party_faction_max_parties_prisoner_trains", 1),
      (assign, "$g_party_faction_max_parties_war_parties", 1),
      (assign, "$g_party_faction_max_parties_mercenary_companies", 1),
	  
      (assign, "$g_party_bandit_max_parties_looter", 38),
      (assign, "$g_party_bandit_max_parties_sea_raider", 22),
      (assign, "$g_party_bandit_max_parties_mountain_bandits", 30),
      (assign, "$g_party_bandit_max_parties_steppe_bandits", 22),
      (assign, "$g_party_bandit_max_parties_taiga_bandits", 22),
      (assign, "$g_party_bandit_max_parties_forest_bandits", 30),
      (assign, "$g_party_bandit_max_parties_desert_bandits", 22),
      (assign, "$g_party_bandit_max_parties_deserters", 45),
      (assign, "$g_party_bandit_max_parties_roving_knights", 7),
      (assign, "$g_party_mercenary_company_max", 7),
      (assign, "$g_party_rebellion_max", 3),
      (assign, "$g_party_rebellion_strong_max", 3),
      (assign, "$g_party_fugitive_serf_max", 15),
      (assign, "$g_party_mercenary_warband_max", 30),
	  
      (jump_to_menu, "mnu_start_game_new_3dot10"),
      ]
      ),

      ("start_game_new_spawn_presets_3",
      [],
      "Normal (3.5GHz)",
      [
      (jump_to_menu, "mnu_start_game_new_3dot10"),
      ]
      ),

      ("start_game_new_spawn_presets_4",
      [],
      "Heavy (25% more)(4.2GHz)",
      [
      (assign, "$g_party_faction_max_parties_foragers", 2),
      (assign, "$g_party_faction_max_parties_scouts", 4),
      (assign, "$g_party_faction_max_parties_patrols", 3),
      (assign, "$g_party_faction_max_parties_caravans", 3),
      (assign, "$g_party_faction_max_parties_prisoner_trains", 1),
      (assign, "$g_party_faction_max_parties_war_parties", 1),
      (assign, "$g_party_faction_max_parties_mercenary_companies", 1),
	  
      (assign, "$g_party_bandit_max_parties_looter", 62),
      (assign, "$g_party_bandit_max_parties_sea_raider", 38),
      (assign, "$g_party_bandit_max_parties_mountain_bandits", 50),
      (assign, "$g_party_bandit_max_parties_steppe_bandits", 38),
      (assign, "$g_party_bandit_max_parties_taiga_bandits", 38),
      (assign, "$g_party_bandit_max_parties_forest_bandits", 50),
      (assign, "$g_party_bandit_max_parties_desert_bandits", 38),
      (assign, "$g_party_bandit_max_parties_deserters", 75),
      (assign, "$g_party_bandit_max_parties_roving_knights", 13),
      (assign, "$g_party_mercenary_company_max", 13),
      (assign, "$g_party_rebellion_max", 6),
      (assign, "$g_party_rebellion_strong_max", 6),
      (assign, "$g_party_fugitive_serf_max", 25),
      (assign, "$g_party_mercenary_warband_max", 50),
	  
      (jump_to_menu, "mnu_start_game_new_3dot10"),
      ]
      ),

      ("start_game_new_spawn_presets_5",
      [],
      "Very Heavy (50% more)(5.0GHz)",
      [
      (assign, "$g_party_faction_max_parties_foragers", 4),
      (assign, "$g_party_faction_max_parties_scouts", 6),
      (assign, "$g_party_faction_max_parties_patrols", 4),
      (assign, "$g_party_faction_max_parties_caravans", 4),
      (assign, "$g_party_faction_max_parties_prisoner_trains", 2),
      (assign, "$g_party_faction_max_parties_war_parties", 2),
      (assign, "$g_party_faction_max_parties_mercenary_companies", 2),
	  
      (assign, "$g_party_bandit_max_parties_looter", 75),
      (assign, "$g_party_bandit_max_parties_sea_raider", 45),
      (assign, "$g_party_bandit_max_parties_mountain_bandits", 60),
      (assign, "$g_party_bandit_max_parties_steppe_bandits", 45),
      (assign, "$g_party_bandit_max_parties_taiga_bandits", 45),
      (assign, "$g_party_bandit_max_parties_forest_bandits", 60),
      (assign, "$g_party_bandit_max_parties_desert_bandits", 45),
      (assign, "$g_party_bandit_max_parties_deserters", 90),
      (assign, "$g_party_bandit_max_parties_roving_knights", 15),
      (assign, "$g_party_mercenary_company_max", 15),
      (assign, "$g_party_rebellion_max", 7),
      (assign, "$g_party_rebellion_strong_max", 7),
      (assign, "$g_party_fugitive_serf_max", 30),
      (assign, "$g_party_mercenary_warband_max", 60),
	  
      (jump_to_menu, "mnu_start_game_new_3dot10"),
      ]
      ),

      ("start_game_new_spawn_presets_20",
      [],
      "Go back.",
      [
      (jump_to_menu, "mnu_start_game_new_1dot9"),
      ]
      ),
    ],
  ),
##################################################################

############### NEW v3.10 - 
("start_game_new_3dot10", menu_text_color(0xFF000000),
"Choose the garrison size.",
"none",
[],
[

    ("select_opt1on_1",
    [],
    "Set it to default EE size (600 max for castles/800 for towns).",
    [
      (assign, "$g_party_garrison_max_size_castles", 600),
      (assign, "$g_party_garrison_max_size_towns", 800),
      (call_script, "script_ee_set_garrison_size", 30, 1),
      (jump_to_menu, "mnu_start_game_2"),
    ]
    ),

    ("select_opt1on_2",
    [],
    "Set it to 1257 default size (300 max for castles/500 for towns).",
    [
      (assign, "$g_party_garrison_max_size_castles", 300),
      (assign, "$g_party_garrison_max_size_towns", 500),
      (call_script, "script_ee_set_garrison_size", 15, 1),
      (jump_to_menu, "mnu_start_game_2"),
    ]
    ),

],
),
############### 

  
  # ("optional_1", menu_text_color(0xFF000000),
    # "Would you like to Enable or Disable decapitations? Note: Decapitations can be enabled or disabled at any time inside (Camp --> More mod options pages).",
    # "none",
    # [],
    # [
      # ("select_opt1on",
      # [],
      # "Enable_decapitations",
      # [
        # (assign, "$dynamic_decap", 1),
        # (jump_to_menu, "mnu_start_game_2"),
      # ]
      # ),

      # ("select_opt1off",
      # [],
      # "Disable_decapitations",
      # [
        # (assign, "$dynamic_decap", 0),
        # (jump_to_menu, "mnu_start_game_2"),
      # ]
      # ),
    # ],
  # ),
  
  
  
  ("start_game_2", menu_text_color(0xFF000000),
    "Select your future.",
    "none",
    [],
    [
      ("start_monarch",
      [
        (eq, "$character_gender", 0),
      ],
      "Start_as_a_Monarch.",
      [
        (str_clear, s10),
        (str_clear, s11),
        (str_clear, s12),
        (str_clear, s13),
        (str_clear, s14),
        (str_clear, s15),
        (assign, "$kaos_monarch_var", 1),
        (assign, "$g_start_faction", -1),
        (assign, "$background_type", cb_king),
	    (assign, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (start_presentation, "prsnt_faction_selection"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_monarch",
      [
        (eq, "$character_gender", 1),
      ],
      "Start_as_a_Queen.",
      [
        (str_clear, s10),
        (str_clear, s11),
        (str_clear, s12),
        (str_clear, s13),
        (str_clear, s14),
        (str_clear, s15),
        (assign, "$g_start_faction", -1),
        (assign, "$kaos_monarch_var", 1),
        (assign, "$background_type", cb_king),
	    (assign, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (start_presentation, "prsnt_faction_selection"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_heir",
      [
        (eq, "$character_gender", 0),
      ],
      "Start_as_a_Prince.",
      [
        (str_clear, s10),
        (str_clear, s11),
        (str_clear, s12),
        (str_clear, s13),
        (str_clear, s14),
        (str_clear, s15),
        (assign, "$g_start_faction", -1),
        (assign, "$kaos_heir", 1),
        (assign, "$background_type", cb_prince),
	    (assign, "$g_player_cur_role", role_prince),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (start_presentation, "prsnt_faction_selection"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_heir",
      [
        (eq, "$character_gender", 1),
      ],
      "Start_as_a_Princess.",
      [
        (str_clear, s10),
        (str_clear, s11),
        (str_clear, s12),
        (str_clear, s13),
        (str_clear, s14),
        (str_clear, s15),
        (assign, "$g_start_faction", -1),
        (assign, "$kaos_heir", 1),
        (assign, "$background_type", cb_prince),
        (assign, reg3, "$character_gender"),
	    (assign, "$g_player_cur_role", role_prince),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (start_presentation, "prsnt_faction_selection"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_vassal",
      [],
      "Start_as_a_sworn_Vassal.",
      [
        (str_clear, s10),
        (str_clear, s11),
        (str_clear, s12),
        (str_clear, s13),
        (str_clear, s14),
        (str_clear, s15),
        (assign, "$g_start_faction", -1),
        (assign, "$start_as_vassal_gvar1", 1),
        (assign, "$background_type", cb_vassal),
        (assign, reg3, "$character_gender"),
	    (assign, "$g_player_cur_role", role_vassal),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (start_presentation, "prsnt_faction_selection"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_adventurer",
      [],
      "Start_as_an_Adventurer.",
      [
        (assign, "$g_start_faction", -1),
        (assign, "$background_type", cb_adventurer),
	    (assign, "$g_player_cur_role", role_adventurer),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (jump_to_menu, "mnu_start_character_1"),
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),

      ("start_bandit",
      [],
      "Start_as_a_Bandit.",
      [
        (assign, "$g_start_faction", -1),
        (assign, "$bandit_start", 1),
        (assign, "$background_type", cb_bandit),
	    (assign, "$g_player_cur_role", role_bandit),  ####### NEW v3.0 - player role
        (try_begin),
          (eq, "$quickstart", 0),
          (jump_to_menu, "mnu_choose_skill"), ### Now jumps directly to the choose skill menu, like the Mercenary Captain start (NEW v3.9.3, by Khanor)
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),
	  
	  ################## NEW v3.0
      ("start_mercenary_captain",
      [],
      "Start_as_a_Mercenary_Captain.",
      [
        (assign, "$g_start_faction", -1),
        (assign, "$background_type", cb_mercenary_captain),
	    (assign, "$g_player_cur_role", role_mercenary_captain),  
        (try_begin),
          (eq, "$quickstart", 0),
          # (jump_to_menu, "mnu_start_character_1"),####### NEW v3.0-KOMKE replaced with below line
          (jump_to_menu, "mnu_choose_skill"),####### NEW v3.0-KOMKE otherwise choosing background overwrites background type
        (else_try),
          (jump_to_menu, "mnu_start_phase_2"),
        (try_end),
      ]
      ),
      ####################################
      ("go_back",
      [],
      "Go_back.",
      [
        (jump_to_menu, "mnu_start_game_1"),
      ]
      ),
    ],
  ),
  
  
  
  
  ("start_game_final_king", menu_text_color(0xFF000000),
    # "You grew tired of your liege, everything he did seemed to be in disagreement with your ways, you just didn't like him, infact you simply wanted his crown more than anything else, it was close to you, you waited and waited and now It was finally time to seize the crown for yourself a usurp with your brother while the Monarch is away. ^^ The moment couldn't have been better, for the old Monarch was busy with his trivialities and not around the country. ^^ While he was busy we took over the country and I declared myself the new Monarch, currently uncertainty runs the country as I worked with my brother to revoke his titles and imprison his loyal troops. ^^ I should get ready for I know that a civil war may soon occur, and that he still has loyal subjects, if a civil war occurs the longer it lasts the more likely he will get stronger, it would be wise to crush him while he is weak as soon as he shows up, I should also inform other factions of my title as they may try to take advantage of the situation.",
    "Your Father, the king, has died. It is your job as his heir to take the title and throne of your nation for yourself...",
    "none",
    [
      # (display_message, "@Uncertainty runs the nation and a Civil War may occur soon.", 0xEEE8AA),
    ],
    [
      ("continue",
      [],
      "All_hail_the_new_Monarch!",
      [
        # (try_begin),
          # (this_or_next|eq, "$kaos_kings_kingdom", 3),
          # (this_or_next|eq, "$kaos_kings_kingdom", 2),
          # (this_or_next|eq, "$kaos_kings_kingdom", 1),
          # (this_or_next|eq, "$kaos_kings_kingdom", 23),
          # (this_or_next|eq, "$kaos_kings_kingdom", 27),
          # (this_or_next|eq, "$kaos_kings_kingdom", 4),
          # (this_or_next|eq, "$kaos_kings_kingdom", 14),
          # (eq, "$kaos_kings_kingdom", 5),
          # (jump_to_menu, "mnu_start_game_culture_addon"),
        # (else_try),
          (jump_to_menu, "mnu_choose_skill"),
      ]
      ),
    ],
   ),
  
  
  
  
  ("start_character_1",mnf_disable_all_keys,
    "You were born years ago, in a land far away. Your father was...",
    "none",
    [
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    ],
    [
    ("start_noble",[], "An impoverished noble.",[
      (assign, "$background_type",cb_noble),
      (assign, reg3, "$character_gender"),
      (str_store_string, s10, "@You came into the world a {reg3?daughter:son} of declining nobility, owning only the house in which they lived. However, despite your family's hardships, they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("start_merchant",[], "A travelling merchant.",[
      (assign, "$background_type",cb_merchant),
      (assign, reg3, "$character_gender"),
        (str_store_string, s10, "@You were born the {reg3?daughter:son} of travelling merchants, always moving from place to place in search of a profit. Although your parents were wealthier than most and educated you as well as they could, you found little opportunity to make friends on the road, living mostly for the moments when you could sell something to somebody."),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("start_guard",[], "A veteran warrior.",[
      (assign, "$background_type",cb_guard),
      (assign, reg3, "$character_gender"),
        (str_store_string, s10, "@As a child, your family scrabbled out a meagre living from your father's wages as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("start_forester",[], "A hunter.",[
      (assign, "$background_type",cb_forester),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@{reg3?daughter:son}"),
        (str_store_string, s10, "@You were the {reg3?daughter:son} of a family who lived off the woods, doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows, even a spot of poaching whenever things got tight. Winter was never a good time for your family as the cold took animals and people alike, but you always lived to see another dawn, though your brothers and sisters might not be so fortunate."),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("start_nomad",[], "A steppe nomad.",[
      (assign, "$background_type",cb_nomad),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@{reg3?daughter:son}"),
        (str_store_string, s10, "@You were a child of the steppe, born to a tribe of wandering nomads who lived in great camps throughout the arid grasslands. Like the other tribesmen, your family revered horses above almost everything else, and they taught you how to ride almost before you learned how to walk. "),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("start_thief",[], "A thief.",[
      (assign, "$background_type",cb_thief),
      (assign, reg3, "$character_gender"),
        (str_store_string, s10, "@As the {reg3?daughter:son} of a thief, you had very little 'formal' education. Instead you were out on the street, begging until you learned how to cut purses, cutting purses until you learned how to pick locks, all the way through your childhood. Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
    (jump_to_menu, "mnu_start_character_2"),
    ]),
    ("go_back",[], "Go back.",
     [(jump_to_menu, "mnu_start_game_1"),
    ]),
    ]
  ),
  
  
  

  ("start_character_2",0,
    "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    "none",
    [],
    [
      ("page",[
          ], "A page at a nobleman's court.",[
      (assign, "$background_answer_2", cb2_page),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@As a {reg3?girl:boy} growing out of childhood, you were sent to live in the court of one of the nobles of the land. There, your first lessons were in humility, as you waited upon the lords and ladies of the household. But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
    (jump_to_menu, "mnu_start_character_3"),
    ]),
      ("apprentice",[
          ], "A craftsman's apprentice.",[
      (assign, "$background_answer_2", cb2_apprentice),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@As a {reg3?girl:boy} growing out of childhood, you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as you wished to stay."),
    (jump_to_menu, "mnu_start_character_3"),
    ]),
      ("stockboy",[
          ], "A shop assistant.",[
      (assign, "$background_answer_2",cb2_merchants_helper),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@As a {reg3?girl:boy} growing out of childhood, you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans. You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd got the better deal."),
    (jump_to_menu, "mnu_start_character_3"),
    ]),
      ("urchin",[
          ], "A street urchin.",[
      (assign, "$background_answer_2",cb2_urchin),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@As a {reg3?girl:boy} growing out of childhood, you took to the streets, doing whatever you must to survive. Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world, always one step ahead of the law and those who wished you ill."),
    (jump_to_menu, "mnu_start_character_3"),
    ]),
      ("nomad",[
          ], "A steppe child.",[
      (assign, "$background_answer_2",cb2_steppe_child),
      (assign, reg3, "$character_gender"),
      (str_store_string,s11, "@As a {reg3?girl:boy} growing out of childhood, you rode the great steppes on a horse of your own, learning the ways of the grass and the desert. Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country. Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
    (jump_to_menu, "mnu_start_character_3"),
    ]),
      ("go_back",[], "Go back.",
     [(jump_to_menu, "mnu_start_character_1"),
    ]),
    ]
  ),
  
  
  
 
  
  ("start_character_3",mnf_disable_all_keys,
    "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
    "none",
    [(assign, reg3, "$character_gender"),],
    [

      ("squire",[(eq, "$character_gender",tf_male)], "A squire.",[
        (assign, "$background_answer_3",cb3_squire),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. When you were named squire to a noble at court, you practiced long hours with weapons, learning how to deal out hard knocks and how to take them, too. You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals. But in addition to learning the chivalric ideal, you also learned about the less uplifting side -- old warriors' stories of ruthless power politics, of betrayals and usurpations, of men who used guile as well as valor to achieve their aims."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("lady",[(eq, "$character_gender",tf_female)], "A lady-in-waiting.",[
        (assign, "$background_answer_3",cb3_lady_in_waiting),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s13, "@{reg3?woman:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things, the wives and mistresses of noble men as well as maidens who had yet to find a husband. However, even here you found politics at work as the ladies schemed for prominence and fought each other bitterly to catch the eye of whatever unmarried man was in fashion at court. You soon learned ways of turning these situations and goings-on to your advantage. With it came the realisation that you yourself could wield great influence in the world, if only you applied yourself with a little bit of subtlety."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("troubadour",[], "A troubadour.",[
        (assign, "$background_answer_3",cb3_troubadour),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s13, "@{reg3?woman:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You set out on your own with nothing except the instrument slung over your back and your own voice. It was a poor existence, with many a hungry night when people failed to appreciate your play, but you managed to survive on your music alone. As the years went by you became adept at playing the drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("student",[], "A university student.",[
        (assign, "$background_answer_3",cb3_student),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. You found yourself as a student in the university of one of the great cities, where you studied theology, philosophy, and medicine. But not all your lessons were learned in the lecture halls. You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight. However, you certainly were able to observe how a broken jaw is set, or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("peddler",[], "A goods peddler.",[
        (assign, "$background_answer_3",cb3_peddler),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s13, "@{reg3?woman:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Heeding the call of the open road, you travelled from village to village buying and selling what you could. It was not a rich existence, but you became a master at haggling even the most miserly elders into giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("craftsman",[], "A smith.",[
        (assign, "$background_answer_3", cb3_craftsman),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s13, "@{reg3?woman:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You pursued a career as a smith, crafting items of function and beauty out of simple metal. As time wore on you became a master of your trade, and fine work started to fetch fine prices. With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("poacher",[], "A game poacher.",[
        (assign, "$background_answer_3", cb3_poacher),
      (str_store_string,s14, "@{reg3?daughter:man}"),
      (str_store_string,s13, "@{reg3?woman:man}"),
      (str_store_string,s12, "@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
    (jump_to_menu, "mnu_start_character_4"),
        ]),
      ("go_back",[], "Go back.",
       [(jump_to_menu, "mnu_start_character_2"),
        ]
       ),
    ]
  ),

  
  

  
  ("start_character_4",mnf_disable_all_keys,
    "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    #Finally, what made you decide to strike out on your own as an adventurer?",
    "none",
    [],
    [
      ("revenge",[], "Personal revenge.",[
        (assign, "$background_answer_4", cb4_revenge),
      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer. Still, it was not a difficult choice to leave, with the rage burning brightly in your heart. You want vengeance. You want justice. What was done to you cannot be undone, and these debts can only be paid in blood..."),
        (jump_to_menu, "mnu_choose_skill"),  ########## NEW v2.8 - player can only choose to start as vassal if he choose one of the noble options before (king, prince or vassal)
        # (jump_to_menu, "mnu_pick_nation"),
        ]),
      ("death",[], "The loss of a loved one.",[
        (assign, "$background_answer_4",cb4_loss),
      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer. All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so painful. Perhaps your new life will let you forget, or honour the name that you can no longer bear to speak..."),
        (jump_to_menu, "mnu_choose_skill"),  ##########
        # (jump_to_menu, "mnu_pick_nation"),
        ]),
      ("wanderlust",[], "Wanderlust.",[
        (assign, "$background_answer_4",cb4_wanderlust),
      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer. You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
        (jump_to_menu, "mnu_choose_skill"),  ##########
        # (jump_to_menu, "mnu_pick_nation"),
        ]),
##      ("fervor",[], "Religious fervor.",[
##        (assign, "$background_answer_4",4),
##      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
## Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
## There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
## seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
## glory of God by the time you're done..."),
##        (jump_to_menu, "mnu_choose_skill"),
##        ]),
      ("disown",[], "Being forced out of your home.",[
        (assign, "$background_answer_4",cb4_disown),
      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer. However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
        (jump_to_menu, "mnu_choose_skill"),   ##########
        # (jump_to_menu, "mnu_pick_nation"), 
        ]),
     ("greed",[], "Lust for money and power.",[
        (assign, "$background_answer_4",cb4_greed),
      (str_store_string,s13, "@Only you know exactly what caused you to give up your old life and become an adventurer. To everyone else, it's clear that you're now motivated solely by personal gain. You want to be rich, powerful, respected, feared. You want to be the one whom others hurry to obey. You want people to know your name, and tremble whenever it is spoken. You want everything, and you won't let anyone stop you from having it..."),
        (jump_to_menu, "mnu_choose_skill"),  ##########
        # (jump_to_menu, "mnu_pick_nation"),
        ]),
      ("go_back",[], "Go back.",
       [(jump_to_menu, "mnu_start_character_3"),
        ]
       ),
    ]
  ),


  
  
  ("choose_skill", 0,
    "{s13}",
    "none",
    [
      (assign, "$current_string_reg", 10),
      (assign, ":var0", 0),
      (try_begin),
        (eq, "$character_gender", 1),
        (str_store_string, s14, "str_woman"),
        (val_add, ":var0", 1),
      (else_try),
        (str_store_string, s14, "str_man"),
      (try_end),
      (try_begin),
        (this_or_next|eq, "$background_type", 8),
        (this_or_next|eq, "$background_type", 10),
        (this_or_next|eq, "$background_type", 9),
        (eq, "$background_type", 1),
        (str_store_string, s15, "str_noble"),
        (val_sub, ":var0", 1),
      (else_try),
        (str_store_string, s15, "str_common"),
      (try_end),
      (try_begin),
        (eq, ":var0", -1),
        (str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
      (else_try),
        (eq, ":var0", 0),
        (str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
      (else_try),
        (eq, ":var0", 1),
        (str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
      (try_end),
    ],
    [
      ("begin_adventuring",
      [],
      "I'm_satisfied_with_my_choices.",
      [
        
        (set_show_messages, 0),
        (try_begin),
          (eq, "$character_gender", 0),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
        (else_try),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
        (try_end),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (troop_raise_skill, "trp_player", "skl_riding", 1),
        
        #################################################
        ### --- King/Queen (faction leader) start --- ###
        #################################################
        (try_begin),
          (eq, "$background_type", cb_king),
          (troop_raise_attribute, "trp_player", ca_strength, 10),
          (troop_raise_attribute, "trp_player", ca_intelligence, 4),
          (troop_raise_attribute, "trp_player", ca_charisma, 6), ### Total of 20 attribute points extra. - Khanor
          (troop_raise_skill, "trp_player", "skl_ironflesh", 5),
          (troop_raise_skill, "trp_player", "skl_power_strike", 6),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 5),
          (troop_raise_skill, "trp_player", "skl_athletics", 3),
          (troop_raise_skill, "trp_player", "skl_riding", 7),
          (troop_raise_skill, "trp_player", "skl_shield", 4),
          (troop_raise_skill, "trp_player", "skl_tactics", 5),
          (troop_raise_skill, "trp_player", "skl_trainer", 3),
          (troop_raise_skill, "trp_player", "skl_looting", 3),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 5),
          (troop_raise_skill, "trp_player", "skl_persuasion", 6),
          (troop_raise_skill, "trp_player", "skl_prisoner_management", 4),
          (troop_raise_skill, "trp_player", "skl_leadership", 6),
          (troop_raise_skill, "trp_player", "skl_trade", 5),

          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 120),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 100),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 120),
          # (troop_set_slot, "trp_player", 7, 800), ### NEW 3.5 - this is now set in the init script
          (call_script, "script_change_player_honor", 50),
          (assign, ":player_gold", 0),
          (store_random_in_range, ":player_gold", 60000, 80000),
          (troop_add_gold, "trp_player", ":player_gold"),
          (party_add_xp, "p_main_party", 10000),

        ####################################################
        ### --- Prince/Princess (faction heir) start --- ###
        ####################################################
        (else_try),
          (eq, "$background_type", cb_prince),
          (troop_raise_attribute, "trp_player", ca_strength, 8),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 4), ### Total of 14 attribute points extra. - Khanor
          (troop_raise_skill, "trp_player", "skl_ironflesh", 4),
          (troop_raise_skill, "trp_player", "skl_power_strike", 5),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 4),
          (troop_raise_skill, "trp_player", "skl_athletics", 4),
          (troop_raise_skill, "trp_player", "skl_riding", 6),
          (troop_raise_skill, "trp_player", "skl_shield", 4),
          (troop_raise_skill, "trp_player", "skl_tactics", 4),
          (troop_raise_skill, "trp_player", "skl_trainer", 2),
          (troop_raise_skill, "trp_player", "skl_looting", 3),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 4),
          (troop_raise_skill, "trp_player", "skl_persuasion", 5),
          (troop_raise_skill, "trp_player", "skl_prisoner_management", 3),
          (troop_raise_skill, "trp_player", "skl_leadership", 5),
          (troop_raise_skill, "trp_player", "skl_trade", 4),

          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 100),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 80),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 100),
          # (troop_set_slot, "trp_player", 7, 500), ### NEW 3.5 - this is now set in the init script
          (call_script, "script_change_player_honor", 20),
          (assign, ":player_gold", 0),
          (store_random_in_range, ":player_gold", 35000, 50000),
          (troop_add_gold, "trp_player", ":player_gold"),
          (party_add_xp, "p_main_party", 6000),

        ##################################
        ### --- Sworn Vassal start --- ###
        ##################################
        (else_try),
          (eq, "$background_type", cb_vassal),
          (troop_raise_attribute, "trp_player", ca_strength, 8),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 4), ### Total of 14 attribute points extra. - Khanor
          (troop_raise_skill, "trp_player", "skl_ironflesh", 4),
          (troop_raise_skill, "trp_player", "skl_power_strike", 5),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 5),
          (troop_raise_skill, "trp_player", "skl_athletics", 5),
          (troop_raise_skill, "trp_player", "skl_riding", 5),
          (troop_raise_skill, "trp_player", "skl_shield", 4),
          (troop_raise_skill, "trp_player", "skl_tactics", 3),
          (troop_raise_skill, "trp_player", "skl_trainer", 3),
          (troop_raise_skill, "trp_player", "skl_looting", 4),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 3),
          (troop_raise_skill, "trp_player", "skl_persuasion", 4),
          (troop_raise_skill, "trp_player", "skl_prisoner_management", 3),
          (troop_raise_skill, "trp_player", "skl_leadership", 4),
          (troop_raise_skill, "trp_player", "skl_trade", 3),
          
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 80),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 60),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 80),
          # (troop_set_slot, "trp_player", 7, 400), ### NEW 3.5 - this is now set in the init script
          (call_script, "script_change_player_honor", 30),
          (assign, ":player_gold", 0),
          (store_random_in_range, ":player_gold", 25000, 40000),
          (troop_add_gold, "trp_player", ":player_gold"),
          (party_add_xp, "p_main_party", 4500),

        ###############################################################################
        ### --- Mercenary Captain start (NEW v3.0) (NEW v3.5 - moved this here) --- ###
        ###############################################################################
        (else_try),
          (eq, "$background_type", cb_mercenary_captain),
          (troop_raise_attribute, "trp_player", ca_strength, 6),
          (troop_raise_attribute, "trp_player", ca_intelligence, 3),
          (troop_raise_attribute, "trp_player", ca_charisma, 3), ### Total of 12 attribute points extra. - Khanor
          
          (troop_raise_skill, "trp_player", "skl_ironflesh", 4),
          (troop_raise_skill, "trp_player", "skl_power_strike", 3),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 3),
          (troop_raise_skill, "trp_player", "skl_athletics", 2),
          (troop_raise_skill, "trp_player", "skl_riding", 3),
          (troop_raise_skill, "trp_player", "skl_shield", 2),
          (troop_raise_skill, "trp_player", "skl_tactics", 2),
          (troop_raise_skill, "trp_player", "skl_trainer", 3),
          (troop_raise_skill, "trp_player", "skl_looting", 3),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 2),
          (troop_raise_skill, "trp_player", "skl_persuasion", 2),
          (troop_raise_skill, "trp_player", "skl_prisoner_management", 2),
          (troop_raise_skill, "trp_player", "skl_leadership", 3),
          (troop_raise_skill, "trp_player", "skl_trade", 2), ### Total of 36 skill points extra. - Khanor

          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 120),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 90),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 90),

          # (call_script, "script_give_source_troop_inventory_to_troop", "trp_player", "trp_bounty_9_mercenary_captain"),
          (call_script, "script_give_source_troop_inventory_to_troop", "trp_player", "trp_bounty_9_mercenary_captain", 4), ####### NEW v3.4 - fixed merc start not getting any equipment

          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_bread", 0),
          (troop_add_item, "trp_player", "itm_bread", 0),
          (troop_add_item, "trp_player", "itm_bread", 0),
          (troop_add_item, "trp_player", "itm_hunter", imod_heavy),

          (store_random_in_range, ":random", 100, 200),
          (troop_set_slot, "trp_player", slot_troop_renown, ":random"),  ####### NEW 3.5 - random
          (assign, ":random", 0),
          (store_random_in_range, ":random", 5000, 8000),
          (troop_add_gold, "trp_player", ":random"),

          (call_script, "script_ee_get_closest_town", "p_main_party"),
          (assign, ":town", reg0),
            (call_script, "script_fill_company", ":town", "p_main_party", slot_regional_mercs),
            (call_script, "script_fill_company", ":town", "p_main_party", slot_regional_mercs),
            (call_script, "script_fill_company", ":town", "p_main_party", slot_regional_mercs),
            (party_upgrade_with_xp, "p_main_party", 6000, 0),
            (party_upgrade_with_xp, "p_main_party", 6000, 0),
        
        ####################################################
        ### --- Bandit start (NEW v3.9.3, by Khanor) --- ###
        ####################################################
        (else_try),
          (eq, "$background_type", cb_bandit),
          (troop_raise_attribute, "trp_player", ca_strength, 2),
          (troop_raise_attribute, "trp_player", ca_intelligence, 4),
          (troop_raise_attribute, "trp_player", ca_charisma, 2), ### Total of 8 attribute points extra. - Khanor

          (troop_raise_skill, "trp_player", "skl_ironflesh", 3),
          (troop_raise_skill, "trp_player", "skl_power_strike", 2),
          (troop_raise_skill, "trp_player", "skl_power_throw", 1),
          (troop_raise_skill, "trp_player", "skl_power_draw", 1),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 2),
          (troop_raise_skill, "trp_player", "skl_athletics", 3),
          (troop_raise_skill, "trp_player", "skl_riding", 3),
          (troop_raise_skill, "trp_player", "skl_shield", 2),
          (troop_raise_skill, "trp_player", "skl_looting", 4),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 4),
          (troop_raise_skill, "trp_player", "skl_persuasion", 1),
          (troop_raise_skill, "trp_player", "skl_prisoner_management", 2),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (troop_raise_skill, "trp_player", "skl_trade", 3), ### Total of 32 skill points extra. - Khanor

          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 90),
          (troop_raise_proficiency, "trp_player", wpt_archery, 60),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 60),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 60),

          (store_random_in_range, ":starting_kit_randomizer", 0, 29), ### Used to give one of three bandit leader starting kits to the player. - Khanor
          (try_begin),
            (lt, "$starting_kit_randomizer", 10),
            (call_script, "script_give_source_troop_inventory_to_troop", "trp_player", "trp_bounty_3_bandit_leader", 4),
          (else_try),
            (lt, "$starting_kit_randomizer", 20),
            (call_script, "script_give_source_troop_inventory_to_troop", "trp_player", "trp_bounty_6_pirate", 4),
          (else_try),
            (call_script, "script_give_source_troop_inventory_to_troop", "trp_player", "trp_bounty_7_pirate_captain", 4),
          (try_end),

          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_bread", 0),
          (troop_add_item, "trp_player", "itm_bread", 0),
          (troop_add_item, "trp_player", "itm_hunter", imod_spirited),

          (call_script, "script_change_player_honor", -25),

          (store_random_in_range, ":random", 50, 120),
          (troop_set_slot, "trp_player", slot_troop_renown, ":random"),
          (assign, ":random", 0),
          (store_random_in_range, ":random", 9000, 12000),
          (troop_add_gold, "trp_player", ":random"),

          (party_add_members, "p_main_party", "trp_looter", 2),
          (party_add_members, "p_main_party", "trp_sea_raider", 4),
          (party_add_members, "p_main_party", "trp_sea_raider_veteran", 4),
          ### Remaining location specific bandits handed out after a starting town has been chosen, so the local area can be taken into account.

        ##############################
        ### --- Vanilla starts --- ###
        ##############################
        (else_try),
          (eq, "$background_type", 1),
          (eq, "$character_gender", 0),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 2),
          (troop_raise_skill, "trp_player", 27, 1),
          (troop_raise_skill, "trp_player", 35, 1),
          (troop_raise_skill, "trp_player", 24, 1),
          (troop_raise_skill, "trp_player", 15, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
          (troop_add_item, "trp_player", "itm_tab_shield_round_a", 5),
          (troop_set_slot, "trp_player", 7, 100),
          (call_script, "script_change_player_honor", 3),
          (troop_add_gold, "trp_player", 100),
        (else_try),
          (eq, "$background_type", 1),
          (eq, "$character_gender", 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 11, 1),
          (troop_raise_skill, "trp_player", 24, 2),
          (troop_raise_skill, "trp_player", 9, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
          (troop_set_slot, "trp_player", 7, 50),
          (troop_add_item, "trp_player", "itm_tab_shield_round_a", 5),
          (troop_add_gold, "trp_player", 100),
        (else_try),
          (eq, "$background_type", 2),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 24, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_skill, "trp_player", 0, 2),
          (troop_raise_skill, "trp_player", 12, 1),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
          (troop_add_gold, "trp_player", 250),
          (troop_set_slot, "trp_player", 7, 20),
        (else_try),
          (eq, "$background_type", 3),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
          (troop_raise_skill, "trp_player", "skl_power_strike", 1),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (troop_raise_skill, "trp_player", "skl_trainer", 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 15),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 20),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
          (troop_add_item, "trp_player", "itm_tab_shield_kite_c", 5),
          (troop_add_gold, "trp_player", 50),
          (troop_set_slot, "trp_player", 7, 10),
        (else_try),
          (eq, "$background_type", 4),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 2),
          (troop_raise_skill, "trp_player", "skl_power_draw", 1),
          (troop_raise_skill, "trp_player", "skl_tracking", 1),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
          (troop_raise_skill, "trp_player", "skl_spotting", 1),
          (troop_raise_skill, "trp_player", "skl_athletics", 1),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_archery, 30),
          (troop_add_gold, "trp_player", 30),
        (else_try),
          (eq, "$background_type", 5),
          (eq, "$character_gender", 0),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_power_draw", 1),
          (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
          (troop_raise_skill, "trp_player", "skl_riding", 2),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_archery, 30),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
          (troop_add_item, "trp_player", "itm_tab_shield_small_round_a", 5),
          (troop_add_gold, "trp_player", 15),
          (troop_set_slot, "trp_player", 7, 10),
        (else_try),
          (eq, "$background_type", 5),
          (eq, "$character_gender", 1),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
          (troop_raise_skill, "trp_player", "skl_first_aid", 1),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
          (troop_raise_skill, "trp_player", "skl_riding", 2),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 5),
          (troop_raise_proficiency, "trp_player", wpt_archery, 20),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
          (troop_add_item, "trp_player", "itm_tab_shield_small_round_a", 5),
          (troop_add_gold, "trp_player", 20),
        (else_try),
          (eq, "$background_type", 6),
          (troop_raise_attribute, "trp_player", ca_agility, 3),
          (troop_raise_skill, "trp_player", "skl_athletics", 2),
          (troop_raise_skill, "trp_player", "skl_power_throw", 1),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
          (troop_raise_skill, "trp_player", "skl_looting", 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 20),
          (troop_add_item, "trp_player", "itm_throwing_knives", 0),
          (troop_add_gold, "trp_player", 25),
        (else_try),
          (eq, "$background_type", 7),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 11, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_skill, "trp_player", 2, 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_add_item, "trp_player", "itm_coarse_tunic", 0),
          (troop_add_item, "trp_player", "itm_wrapping_boots", 0),
          (troop_add_item, "trp_player", "itm_club", 0),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
          (troop_add_item, "trp_player", "itm_sumpter_horse", 0),
          (troop_add_gold, "trp_player", 10),
          (troop_set_slot, "trp_player", 7, 10),
        (try_end),
        (try_begin),
          (eq, "$background_answer_2", 0),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_skill, "trp_player", "skl_power_strike", 1),
          (troop_raise_skill, "trp_player", "skl_persuasion", 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 5),
        (else_try),
          (eq, "$background_answer_2", 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_skill, "trp_player", "skl_engineer", 1),
          (troop_raise_skill, "trp_player", "skl_trade", 1),
        (else_try),
          (eq, "$background_answer_2", 2),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_spotting", 1),
          (troop_raise_skill, "trp_player", "skl_looting", 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
        (else_try),
          (eq, "$background_answer_2", 3),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
          (troop_raise_skill, "trp_player", "skl_power_throw", 1),
          (troop_raise_proficiency, "trp_player", wpt_archery, 15),
          (call_script, "script_change_troop_renown", "trp_player", 5),
        (else_try),
          (eq, "$background_answer_2", 4),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
          (troop_raise_skill, "trp_player", "skl_trade", 1),
        (else_try),
          (eq, "$background_answer_2", 5),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_skill, "trp_player", 25, 1),
          (troop_raise_skill, "trp_player", 24, 1),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 5),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 5),
          (call_script, "script_change_troop_renown", "trp_player", 15),
        (else_try),
          (eq, "$background_answer_2", 6),
          (troop_raise_attribute, "trp_player", ca_charisma, 3),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_skill, "trp_player", 27, 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),
          (call_script, "script_change_troop_renown", "trp_player", 20),
        (else_try),
          (eq, "$background_answer_2", 7),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 2),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_skill, "trp_player", 15, 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
          (call_script, "script_change_troop_renown", "trp_player", 15),
        (else_try),
          (eq, "$background_answer_2", 8),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 1, 1),
          (troop_raise_skill, "trp_player", 10, 1),
          (troop_raise_skill, "trp_player", 9, 1),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
          (call_script, "script_change_troop_renown", "trp_player", 5),
        (try_end),
        (try_begin),
          (eq, "$background_answer_3", 1),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_skill, "trp_player", 35, 1),
          (troop_raise_skill, "trp_player", 26, 1),
          (troop_add_gold, "trp_player", 10),
          (troop_add_item, "trp_player", "itm_scimitar", 0),
          (troop_add_item, "trp_player", "itm_tab_shield_round_b", 5),
          (troop_add_item, "trp_player", "itm_leather_jerkin", 22),
          (troop_add_item, "trp_player", "itm_leather_boots", 21),
          (troop_add_item, "trp_player", "itm_sword_type_xii", 2),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 31),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
          (troop_add_gold, "trp_player", 20),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 30),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 30),
        (else_try),
          (eq, "$background_answer_3", 2),
          (troop_raise_attribute, "trp_player", ca_agility, 2),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_shield", 1),
          (troop_raise_skill, "trp_player", "skl_tracking", 1),
          (troop_raise_skill, "trp_player", "skl_spotting", 1),
          (try_begin),
            (this_or_next|player_has_item, "itm_hide_boots"),
            (troop_has_item_equipped, "trp_player", "itm_hide_boots"),
            (troop_remove_item, "trp_player", "itm_hide_boots"),
          (try_end),
          (troop_add_item, "trp_player", "itm_norman_faceplate", 7),
          (troop_add_item, "trp_player", "itm_leather_jacket", 7),
          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_sword_khergit_1", 0),
          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_hunting_bow", 0),
          (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
          (troop_add_item, "trp_player", "itm_sumpter_horse", 18),
          (troop_add_gold, "trp_player", 20),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 40),
        (else_try),
          (eq, "$background_answer_3", 3),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_skill, "trp_player", "skl_power_draw", 1),
          (troop_raise_skill, "trp_player", "skl_tracking", 1),
          (troop_raise_skill, "trp_player", "skl_spotting", 1),
          (troop_raise_skill, "trp_player", "skl_athletics", 1),
          (troop_add_gold, "trp_player", 10),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
          (troop_raise_proficiency, "trp_player", wpt_archery, 35),
          (troop_add_item, "trp_player", "itm_raf_two_handed_axe_a", 4),
          (troop_add_item, "trp_player", "itm_rawhide_coat", 0),
          (troop_add_item, "trp_player", "itm_hunting_bow", 0),
          (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
          (troop_add_item, "trp_player", "itm_sumpter_horse", 18),
          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_dried_meat", 0),
          (troop_add_item, "trp_player", "itm_furs", 0),
          (troop_add_item, "trp_player", "itm_furs", 0),
        (else_try),
          (eq, "$background_answer_3", 4),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_engineer", 1),
          (troop_raise_skill, "trp_player", "skl_tactics", 1),
          (troop_raise_skill, "trp_player", "skl_trade", 1),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
          (troop_add_gold, "trp_player", 100),
          (troop_add_item, "trp_player", "itm_leather_boots", 22),
          (troop_add_item, "trp_player", "itm_coarse_tunic", 0),
          (troop_add_item, "trp_player", "itm_sword_type_xiii", 13),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_tools", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 0),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
          (eq, "$background_answer_3", 5),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_riding", 1),
          (troop_raise_skill, "trp_player", "skl_trade", 1),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
          (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
          (troop_add_item, "trp_player", "itm_leather_gloves", 0),
          (troop_add_gold, "trp_player", 90),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 15),
          (troop_add_item, "trp_player", "itm_leather_jacket", 0),
          (troop_add_item, "trp_player", "itm_leather_boots", 22),
          (troop_add_item, "trp_player", "itm_fur_hat", 0),
          (troop_add_item, "trp_player", "itm_staff", 0),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 0),
          (troop_add_item, "trp_player", "itm_sumpter_horse", 0),
          (troop_add_item, "trp_player", "itm_linen", 0),
          (troop_add_item, "trp_player", "itm_pottery", 0),
          (troop_add_item, "trp_player", "itm_wool", 0),
          (troop_add_item, "trp_player", "itm_wool", 0),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
          (eq, "$background_answer_3", 6),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 11, 1),
          (troop_raise_skill, "trp_player", 9, 1),
          (troop_raise_skill, "trp_player", 10, 2),
          (troop_add_item, "trp_player", "itm_leather_gloves", 22),
          # (troop_add_item, "trp_player", "itm_battlefield_cross", 18),
          (troop_add_item, "trp_player", "itm_1257_hood", 0),
          (troop_add_item, "trp_player", "itm_robe", 0),
          (troop_add_item, "trp_player", "itm_ankle_boots", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 0),
          (troop_add_gold, "trp_player", 15),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 25),
        (else_try),
          (eq, "$background_answer_3", 7),
          (troop_raise_attribute, "trp_player", ca_charisma, 2),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_persuasion", 1),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
          (troop_add_gold, "trp_player", 80),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 25),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),
          (troop_add_item, "trp_player", "itm_archer_a", 24),
          (troop_add_item, "trp_player", "itm_leather_boots", 22),
          (troop_add_item, "trp_player", "itm_sword_type_xii", 2),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 31),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
          (eq, "$background_answer_3", 8),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_skill, "trp_player", "skl_riding", 1),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_power_strike", 1),
          (troop_raise_skill, "trp_player", "skl_leadership", 1),
          (troop_add_gold, "trp_player", 20),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 30),
          (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 30),
          (troop_raise_proficiency, "trp_player", wpt_polearm, 30),
          (troop_raise_proficiency, "trp_player", wpt_archery, 10),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
          (troop_add_item, "trp_player", "itm_leather_jerkin", 22),
          (troop_add_item, "trp_player", "itm_leather_boots", 21),
          (troop_add_item, "trp_player", "itm_sword_type_xii", 2),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 31),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
          (eq, "$background_answer_3", 9),
          (eq, "$character_gender", 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", "skl_persuasion", 2),
          (troop_raise_skill, "trp_player", "skl_riding", 1),
          (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
          (troop_add_item, "trp_player", "itm_dagger", 0),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_courser", 35),
          (troop_add_item, "trp_player", "itm_arming_cap", 24),
          (troop_add_item, "trp_player", "itm_peasant_dress", 24),
          (troop_add_gold, "trp_player", 100),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 15),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
          (eq, "$background_answer_3", 10),
          (troop_raise_attribute, "trp_player", ca_intelligence, 2),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
          (troop_raise_skill, "trp_player", "skl_surgery", 1),
          (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
          (troop_raise_skill, "trp_player", "skl_persuasion", 1),
          (troop_add_gold, "trp_player", 80),
          (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
          (troop_raise_proficiency, "trp_player", wpt_crossbow, 20),
          (troop_add_item, "trp_player", "itm_linen_tunic", 24),
          (troop_add_item, "trp_player", "itm_woolen_hose", 0),
          (troop_add_item, "trp_player", "itm_sword_type_xii", 2),
          (troop_add_item, "trp_player", "itm_hunting_crossbow", 0),
          (troop_add_item, "trp_player", "itm_bolts", 0),
          (troop_add_item, "trp_player", "itm_saddle_horse", 31),
          (troop_add_item, "trp_player", "itm_smoked_fish", 0),
          (store_random_in_range, ":var0", "itm_book_tactics", "itm_spice"),
          (troop_add_item, "trp_player", ":var0", 0),
        (try_end),
        (try_begin),
          (eq, "$background_answer_4", 1),
          (troop_raise_attribute, "trp_player", ca_strength, 2),
          (troop_raise_skill, "trp_player", "skl_power_strike", 1),
        (else_try),
          (eq, "$background_answer_4", 2),
          (troop_raise_attribute, "trp_player", ca_charisma, 2),
          (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
        (else_try),
          (eq, "$background_answer_4", 3),
          (troop_raise_attribute, "trp_player", ca_agility, 2),
          (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
        (else_try),
          (eq, "$background_answer_4", 4),
          (troop_raise_attribute, "trp_player", ca_charisma, 1),
          (troop_raise_skill, "trp_player", 11, 2),
          (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
        (else_try),
          (eq, "$background_answer_4", 5),
          (troop_raise_attribute, "trp_player", ca_strength, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
        (else_try),
          (eq, "$background_answer_4", 6),
          (troop_raise_attribute, "trp_player", ca_agility, 1),
          (troop_raise_attribute, "trp_player", ca_intelligence, 1),
          (troop_raise_skill, "trp_player", "skl_looting", 1),
        (try_end),
		################################
        (try_begin),
		  ############# NEW v3.5
          (this_or_next|eq, "$background_type", cb_prince),
          (this_or_next|eq, "$background_type", cb_king),
          (this_or_next|eq, "$background_type", cb_vassal),
		  #############
          (eq, "$background_type", cb_noble),####### NEW v3.0-KOMKE
          (jump_to_menu, "mnu_auto_return"),
          (start_presentation, "prsnt_banner_selection"),
        (else_try),
          (change_screen_return, 0),
        (try_end),
        (troop_add_gold, "trp_player", 1000),
        (try_begin),
          (gt, "$g_start_faction", 0),
          (try_begin),
            (troop_add_gold, "trp_player", 5000),
            # (faction_get_slot, ":culture", "$g_start_faction", slot_faction_culture),
            # (faction_get_slot, ":var2", ":culture", slot_faction_tier_1_castle_troop),
            (try_begin),
              (gt, "$kaos_kings_kingdom", 0),
                (call_script, "script_equip_troop_king_start"),  ######### NEW v2.0
            (else_try),
			######### NEW v2.0
              (this_or_next|gt, "$kaos_kings_prince", 0),
              (eq, "$background_type", cb_vassal),
                (store_faction_of_troop, ":player_faction", "trp_player"),  
                (call_script, "script_equip_troop_royal_start", ":player_faction"),  
            #########
            (try_end),
			########################################
          (try_end),
        (try_end),
        (set_show_messages, 1),
      ]
      ),

      ("go_back_dot",
      [],
      "Go_back.",
      [
        (try_begin),
          (this_or_next|ge, "$kaos_kings_kingdom", 1),
          (eq, "$kaos_monarch_var", 1),
          (jump_to_menu, "mnu_start_game_1"),
        (else_try),
          (this_or_next|eq, "$kaos_heir", 1),
          (eq, "$start_as_vassal_gvar1", 1),
          (jump_to_menu, "mnu_start_game_1"),
        (else_try),
          (jump_to_menu, "mnu_start_character_4"),
        (try_end),
      ]
      ),
    ],
  ),
    
    
    
    

  ("past_life_explanation",mnf_disable_all_keys,
    "{s3}",
    "none",
    [
     (try_begin),
       (gt, "$current_string_reg",14),
       (assign, "$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3, "$current_string_reg"),
     (try_begin),
       (ge, "$current_string_reg",14),
       (str_store_string,s5, "@Back to the beginning..."),
     (else_try),
       (str_store_string,s5, "@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[], "{s5}",[
        (val_add, "$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue",[], "Continue...",
       [
        ]),
      ("go_back_dot",[], "Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
        ]),
    ]
  ),

   ("auto_return",0,
    "{!}This menu automatically returns to caller.",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),
  
  
  ("morale_report",0,
   "{s1}",
   "none",
   [
     (call_script, "script_get_player_party_morale_values"),

    ######### NEW v3.8
    (str_clear, s1),
    (str_clear, s2),
    (str_clear, s3),
    (str_clear, s4),
    (str_clear, s5),
    (str_clear, s6),
    (str_clear, s7),
    (str_clear, s8),
	###########################
    (assign, ":target_morale", reg0),
    (assign, reg1, "$g_player_party_morale_modifier_party_size"),
    (try_begin),
      (gt, reg1, 0),
      (str_store_string, s2, "@{!} -"),
    (else_try),
      (str_store_string, s2, "str_space"),
    (try_end),

    (assign, reg2, "$g_player_party_morale_modifier_leadership"),
    (try_begin),
      (gt, reg2, 0),
      (str_store_string, s3, "@{!} +"),
    (else_try),
      (str_store_string, s3, "str_space"),
    (try_end),
  
    ########### food_variety_s4 reg3 s5 s6
    ########### ^Food variety: {s4}{reg3}{s5}{s6}{s8}^
	############### https://media.discordapp.net/attachments/811305336690049056/884450393755623424/2021-09-06_08_49_38-Weird_words_2.png_-_Photos.png
	############ reg3 = +12
	############# s8 = bug
    (try_begin),
      (gt, "$g_player_party_morale_modifier_no_food", 0),
      (assign, reg7, "$g_player_party_morale_modifier_no_food"),
      (str_store_string, s5, "@^No food:  -{reg7}"),
    (else_try),
      (str_store_string, s5, "str_space"),
    (try_end),
    (assign, reg3, "$g_player_party_morale_modifier_food"),
    (try_begin),
      (gt, reg3, 0),
      (str_store_string, s4, "@{!} +"),
    (else_try),
      (str_store_string, s4, "str_space"),
    (try_end),

    (try_begin),
      (gt, "$g_player_party_morale_modifier_debt", 0),
      (assign, reg6, "$g_player_party_morale_modifier_debt"),
      (str_store_string, s6, "@^Wage debt:  -{reg6}"),
    (else_try),
      (str_store_string, s6, "str_space"),
    (try_end),

    (party_get_morale, reg5, "p_main_party"),
    (store_sub, reg4, reg5, ":target_morale"),
    (try_begin),
      (gt, reg4, 0),
      (str_store_string, s7, "@{!} +"),
    (else_try),
      (str_store_string, s7, "str_space"),
    (try_end),

    (assign, reg6, 50),

    (str_store_string, s1, "str_current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___"),

    # (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
      # (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
      # (val_div, ":faction_morale", 100),
      # (neq, ":faction_morale", 0),
      # (assign, reg6, ":faction_morale"),
      # (str_store_faction_name, s9, ":kingdom_no"),
      # (str_store_string, s1, "str_s1extra_morale_for_s9_troops__reg6_"),
    # (try_end),
    ],
    [
      ("continue",[], "Continue...",
      [
        (jump_to_menu, "mnu_reports"),
      ]),
      ]
  ),



  ("courtship_relations",0,
   "{s1}",
   "none",
   [(str_store_string, s1, "str_courtships_in_progress_"),
    (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_slot_eq, ":lady", slot_troop_met, 2),
        (call_script, "script_troop_get_relation_with_troop", "trp_player", ":lady"),
        (gt, reg0, 0),
        (assign, reg3, reg0),

        (str_store_troop_name, s2, ":lady"),

        (store_current_hours, ":hours_since_last_visit"),
        (troop_get_slot, ":last_visit_hour", ":lady", slot_troop_last_talk_time),
        (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
        (store_div, ":days_since_last_visit", ":hours_since_last_visit", 24),
        (assign, reg4, ":days_since_last_visit"),

        (str_store_string, s1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
    (try_end),

    (str_store_string, s1, "str_s1__poems_known"),
    (try_begin),
         (gt, "$allegoric_poem_recitations", 0),
         (str_store_string, s1, "str_s1_storming_the_castle_of_love_allegoric"),
    (try_end),
    (try_begin),
         (gt, "$tragic_poem_recitations", 0),
         (str_store_string, s1, "str_s1_kais_and_layali_tragic"),
    (try_end),
    (try_begin),
         (gt, "$comic_poem_recitations", 0),
         (str_store_string, s1, "str_s1_a_conversation_in_the_garden_comic"),
    (try_end),
    (try_begin),
         (gt, "$heroic_poem_recitations", 0),
         (str_store_string, s1, "str_s1_helgered_and_kara_epic"),
    (try_end),
    (try_begin),
         (gt, "$mystic_poem_recitations", 0),
         (str_store_string, s1, "str_s1_a_hearts_desire_mystic"),
    (try_end),

    ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("lord_relations",0,
   "{s1}",
   "none",
   [

    (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
	    (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ## he's alive/active
        (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
    (try_end),

    (str_clear, s1),
    (try_for_range, ":unused", active_npcs_begin, active_npcs_end),
        (assign, ":score_to_beat", -100),
        (assign, ":best_relation_remaining_npc", -1),
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
	        (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ## he's alive/active
            (troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
            (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_ge, ":active_npc", slot_troop_met, 1),

            (call_script, "script_troop_get_player_relation", ":active_npc"),
            (assign, ":relation_with_player", reg0),
            (ge, ":relation_with_player", ":score_to_beat"),

            (assign, ":score_to_beat", ":relation_with_player"),
            (assign, ":best_relation_remaining_npc", ":active_npc"),
        (try_end),
        (gt, ":best_relation_remaining_npc", -1),

        (str_store_troop_name_link, s4, ":best_relation_remaining_npc"),
        (assign, reg4, ":score_to_beat"),
        (str_store_string, s1, "@{!}{s1}^{s4}: {reg4}"),
        (troop_set_slot, ":best_relation_remaining_npc", slot_troop_temp_slot, 1),
    (try_end),


    ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),



  ("companion_report",0,
   "{s7}{s1}",
   "none",
   [
   (str_clear, s1),
   (str_store_string, s7, "str_no_companions_in_service"),

   (try_begin),
    (troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_spouse),
    (try_begin),
        (troop_get_type, ":is_female", "trp_player"),
        (eq, ":is_female", 1),
        (str_store_string, s8, "str_husband"),
    (else_try),
        (str_store_string, s8, "str_wife"),
    (try_end),

    (try_begin),
        (le, ":spouse_or_betrothed", 0),
        (troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_betrothed),
        (str_store_string, s8, "str_betrothed"),
    (try_end),
    (gt, ":spouse_or_betrothed", 0),

    (str_store_troop_name, s4, ":spouse_or_betrothed"),
    (troop_get_slot, ":cur_center", ":spouse_or_betrothed", slot_troop_cur_center),
    (try_begin),
        (is_between, ":cur_center", centers_begin, centers_end),
        (str_store_party_name, s5, ":cur_center"),
    (else_try),
        (troop_slot_eq, ":spouse_or_betrothed", slot_troop_occupation, slto_kingdom_hero),
        (str_store_string, s5, "str_leading_party"),
    (else_try),
        (str_store_string, s5, "str_whereabouts_unknown"),
    (try_end),
    (str_store_string, s3, "str_s4_s8_s5"),
    (str_store_string, s2, s1),
    (str_store_string, s1, "str_s2_s3"),

   (try_end),


   (try_begin),
    (ge, "$cheat_mode", 1),
    (ge, "$npc_to_rejoin_party", 0),
    (str_store_troop_name, s5, "$npc_to_rejoin_party"),
    (str_store_string, s1, "@{!}DEBUG -- {s1}^NPC in rejoin queue: {s5}^"),
   (try_end),


   (try_for_range, ":companion", companions_begin, companions_end),
        (str_clear, s2),
        (str_clear, s3),

        (try_begin),
            (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),
      # rafi
      (try_begin),
        (troop_slot_eq, ":companion", slot_troop_traveling, 1),
        (neg | troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
        (assign, ":messenger_party", -1),
        (assign, ":destination", -1),
        (assign, ":home", -1),
        (try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, raf_spt_messenger),
          (assign, ":messenger_party", ":cur_party"),
          (party_get_slot, ":destination", ":cur_party", slot_party_ai_object),
          (party_get_slot, ":home", ":cur_party", slot_party_home_center),
        (try_end),
        (try_begin),
          (gt, ":messenger_party", 0),
          (eq, ":destination", ":home"),
          (str_store_string, s8, "@is traveling to"),
          (str_store_party_name, s5, ":home"),
          (str_store_troop_name, s4, ":companion"),
          (display_message, "@{s4} {s8} to {s5}"),
        (else_try),
          (lt, ":messenger_party", 0), # no party found, arrived
          (troop_get_slot, ":center", ":companion", slot_troop_cur_center),
          (gt, ":center", 0),
          (party_slot_eq, ":center", slot_party_type, spt_town),
          (str_store_string, s8, "@Awaiting your arrival"),
          (str_store_party_name, s5, ":center"),
          (str_store_troop_name, s4, ":companion"),
          (display_message, "@{s4} - {s8} in {s5} tavern"),
        (else_try),
          (gt, ":messenger_party", 0),
          (str_store_string, s8, "@is awaiting your messenger in"),
          (str_store_party_name, s5, ":destination"),
          (str_store_troop_name, s4, ":companion"),
          (display_message, "@{s4} {s8} to {s5}"),
        (try_end),
        (str_store_string, s3, "str_s4_s8_s5"),
        (str_store_string, s2, s1),
        (str_store_string, s1, "str_s2_s3"),
      (try_end),
      # end rafi
            (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
            (str_store_troop_name, s4, ":companion"),
            (try_begin),
                (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
                (str_store_string, s8, "str_gathering_support"),
                (try_begin),
                    (eq, ":days_left", 1),
                    (str_store_string, s5, "str_expected_back_imminently"),
                (else_try),
                    (assign, reg3, ":days_left"),
                    (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
                (try_end),
            (else_try),
                (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
                (troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
                (str_store_party_name, s11, ":town_with_contacts"),

                (str_store_string, s8, "str_gathering_intelligence"),
                (try_begin),
                    (eq, ":days_left", 1),
                    (str_store_string, s5, "str_expected_back_imminently"),
                (else_try),
                    (assign, reg3, ":days_left"),
                    (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
                (try_end),
            (else_try),    #This covers most diplomatic missions
                (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
                # (neg|troop_slot_ge, ":companion", slot_troop_current_mission, 8), 
                (neg|troop_slot_ge, ":companion", slot_troop_current_mission, 19),  #### NEW v3.8

                (troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
                (str_store_faction_name, s9, ":faction"),
                (str_store_string, s8, "str_diplomatic_embassy_to_s9"),
                (try_begin),
                    (eq, ":days_left", 1),
                    (str_store_string, s5, "str_expected_back_imminently"),
                (else_try),
                    (assign, reg3, ":days_left"),
                    (str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
                (try_end),
            (else_try),
                (eq, ":companion", "$g_player_minister"),
                (str_store_string, s8, "str_serving_as_minister"),
                (try_begin),
                    (is_between, "$g_player_court", centers_begin, centers_end),
                    (str_store_party_name, s9, "$g_player_court"),
                    (str_store_string, s5, "str_in_your_court_at_s9"),
                (else_try),
                    (str_store_string, s5, "str_whereabouts_unknown"),
                (try_end),
            (else_try),
                (main_party_has_troop, ":companion"),
                (str_store_string, s8, "str_under_arms"),
                (str_store_string, s5, "str_in_your_party"),
            (else_try),
                (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                (str_store_string, s8, "str_attempting_to_rejoin_party"),
                (str_store_string, s5, "str_whereabouts_unknown"),
            (else_try),    #Companions who are in a center
                (troop_slot_ge, ":companion", slot_troop_cur_center, 1),


                (str_store_string, s8, "str_separated_from_party"),
                (str_store_string, s5, "str_whereabouts_unknown"),
            (else_try), #Excludes companions who have occupation = retirement
                (try_begin), #Native bug fixed
                  (check_quest_active, "qst_lend_companion"),
                  (quest_slot_eq, "qst_lend_companion", slot_quest_target_troop, ":companion"),
                  (str_store_string, s8, "@On loan, "), 
                (else_try),
                  (troop_set_slot, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                  (str_store_string, s8, "str_attempting_to_rejoin_party"),                  
                (try_end),
                
                (str_store_string, s5, "str_whereabouts_unknown"),
                (try_begin),
                    (ge, "$cheat_mode", 1),
                    (troop_get_slot, reg2, ":companion", slot_troop_current_mission),
                    (troop_get_slot, reg3, ":companion", slot_troop_days_on_mission),
                    (troop_get_slot, reg4, ":companion", slot_troop_prisoner_of_party),
                    (troop_get_slot, reg4, ":companion", slot_troop_playerparty_history),

                    (display_message, "@{!}DEBUG: {s4} current mission: {reg2}, days on mission: {reg3}, prisoner: {reg4}, pphistory: {reg5}"),
                (try_end),
            (try_end),

            (str_store_string, s3, "str_s4_s8_s5"),

            (str_store_string, s2, s1),
            (str_store_string, s1, "str_s2_s3"),

            (str_clear, s7), #"no companions in service"
        (else_try),
            (neg|troop_slot_eq, ":companion", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_ge, ":companion", slot_troop_prisoner_of_party, centers_begin),

            (str_store_troop_name, s4, ":companion"),
            (str_store_string, s8, "str_missing_after_battle"),
            (str_store_string, s5, "str_whereabouts_unknown"),


            (str_store_string, s3, "str_s4_s8_s5"),
            (str_store_string, s2, s1),
            (str_store_string, s1, "str_s2_s3"),
            (str_clear, s7), #"no companions in service"
        (try_end),
   (try_end),


    ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),





  ("faction_orders",0,
   "{!}{s9}",
   "none",
   [
    (str_clear, s9),
    (store_current_hours, ":cur_hours"),
    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (neq, ":faction_no", "fac_player_supporters_faction"),

        (faction_get_slot, ":old_faction_ai_state", ":faction_no", slot_faction_ai_state),

        (try_begin),
            (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
            (gt, ":faction_marshal", -1),
            (assign, ":faction_ai_decider", ":faction_marshal"),
        (else_try),
            (faction_get_slot, ":faction_ai_decider", ":faction_no", slot_faction_leader),
        (try_end),


        #(*1) these two lines moved to here from (*2)
        #####(display_debug_message, "@Line 6055"),
        (call_script, "script_npc_decision_checklist_faction_ai_alt", ":faction_ai_decider"),
        (assign, ":new_strategy", reg0),
        (str_store_string, s26, s14),

        #(3*) these three lines moved to here from (*4)
        (faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
        (faction_get_slot, ":faction_ai_object", ":faction_no", slot_faction_ai_object),
        (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),

        (faction_get_slot, ":faction_ai_offensive_max_followers", ":faction_no", slot_faction_ai_offensive_max_followers),
        (str_store_faction_name, s10, ":faction_no"),

       (try_begin),
            (faction_get_slot, ":faction_issue", ":faction_no", slot_faction_political_issue),

            (try_begin),
                (eq, ":faction_issue", 1),
                (str_store_string, s11, "@Appoint next marshal"),
            (else_try),
                (is_between, ":faction_issue", centers_begin, centers_end),
                (str_store_party_name, s12, ":faction_issue"),
                (str_store_string, s11, "@Award {s12} as fief"),
            (else_try),
                (eq, ":faction_issue", 0),
                (str_store_string, s11, "@None"),
            (else_try),
                (assign, reg3, ":faction_issue"),
                (str_store_string, s11, "@{!}Error ({reg3})"),
            (try_end),

            (store_current_hours, reg4),
            (faction_get_slot, ":faction_issue_put_on_agenda", ":faction_no", slot_faction_political_issue_time),
            (val_sub, reg4, ":faction_issue_put_on_agenda"),

            (str_store_string, s10, "@{!}{s10}^Faction political issue: {s11}"),
            (try_begin),
                (faction_slot_ge, ":faction_no", slot_faction_political_issue, 1),
                (str_store_string, s10, "@{!}{s10} (on agenda {reg4} hours)"),
            (try_end),
       (try_end),


       (assign, reg2, ":faction_ai_offensive_max_followers"),
       (try_begin),
         (eq, ":faction_ai_state", sfai_default),
         (str_store_string, s11, "@{!}Defending"),
       (else_try),
         (eq, ":faction_ai_state", sfai_gathering_army),
         (str_store_string, s11, "@{!}Gathering army"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Besieging {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_raiding_village),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Raiding {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemy_army),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "str_attacking_enemy_army_near_s11"),
       (else_try),
         (eq, ":faction_ai_state", sfai_feast),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "str_holding_feast_at_s11"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemies_around_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@{!}Attacking enemies around {s11}"),
       (else_try),
         (assign, reg4, ":faction_ai_state"),
         (str_store_string, s11, "str_sfai_reg4"),
       (try_end),

       (try_begin),
         (lt, ":faction_marshall", 0),
         (str_store_string, s12, "@No one"),
       (else_try),
         (str_store_troop_name, s12, ":faction_marshall"),
         (troop_get_slot, reg21, ":faction_marshall", slot_troop_controversy),
         (str_store_string, s12, "@{!}{s12} (controversy: {reg21})"),
       (try_end),

	   ############ NEW v2.1 - https://www.nexusmods.com/mbwarband/mods/3614
       (try_for_parties, ":screen_party"),
         #MOTO use substate to represent screening properly
         # (party_slot_eq, ":screen_party", slot_party_ai_state, spai_screening_army),
         (party_slot_eq, ":screen_party", slot_party_ai_state, spai_accompanying_army),
         (party_slot_eq, ":screen_party", slot_party_ai_substate, 1),
         #MOTO end use substate to represent screening properly
         (store_faction_of_party, ":screen_party_faction", ":screen_party"),
         (eq, ":screen_party_faction", ":faction_no"),
           (str_store_party_name, s38, ":screen_party"),
           (str_store_string, s12, "@{!}{s12}^Screening party: {s38}"),
       (try_end),
       ################################################
       #(*2) these two lines moved to up (look *1)
       #(call_script, "script_npc_decision_checklist_faction_ai", ":faction_no"),
       #(assign, ":new_strategy", reg0),

       #(try_begin),
       #  (this_or_next|eq, ":new_strategy", sfai_default),
       #  (eq, ":new_strategy", sfai_feast),
       #
       #  (store_current_hours, ":hours"),
       #  (faction_set_slot, ":faction_no", slot_faction_ai_last_rest_time, ":hours"),
       #(try_end),
      (try_begin),
         #new condition to rest, (a faction's new strategy should be feast or default) and (":hours_at_current_state" > 20)
         (this_or_next|eq, ":new_strategy", sfai_default),
         (eq, ":new_strategy", sfai_feast),

         (store_current_hours, ":hours_at_current_state"),
         (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
         (val_sub, ":hours_at_current_state", ":current_state_started"),
         (ge, ":hours_at_current_state", 18),

         (store_current_hours, ":hours"),
         (faction_set_slot, ":faction_no", slot_faction_ai_last_rest_time, ":hours"),
       (try_end),

        #Change of strategy
        (try_begin),
          (neq, ":new_strategy", ":old_faction_ai_state"),

          (store_current_hours, ":hours"),
          (faction_set_slot, ":faction_no", slot_faction_ai_current_state_started, ":hours"),
        (try_end),

       (call_script, "script_evaluate_realm_stability", ":faction_no"),
       (assign, ":disgruntled_lords", reg0),
       (assign, ":restless_lords", reg1),


       (faction_get_slot, ":last_feast_ended", ":faction_no", slot_faction_last_feast_start_time),
       (store_sub, ":hours_since_last_feast", ":cur_hours", ":last_feast_ended"),
       (val_sub, ":hours_since_last_feast", 72),

       (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
       (store_sub, ":hours_at_current_state", ":cur_hours", ":current_state_started"),

       (faction_get_slot, ":faction_ai_last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
       (store_sub, ":hours_since_last_offensive", ":cur_hours", ":faction_ai_last_offensive_time"),

       (faction_get_slot, ":faction_ai_last_rest", ":faction_no", slot_faction_ai_last_rest_time),
       (store_sub, ":hours_since_last_rest", ":cur_hours", ":faction_ai_last_rest"),

       (faction_get_slot, ":faction_ai_last_decisive_event", ":faction_no", slot_faction_ai_last_decisive_event),
       (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),

       (assign, reg3, ":hours_at_current_state"),
       (assign, reg4, ":hours_since_last_offensive"),
       (assign, reg5, ":hours_since_last_feast"),

       (assign, reg7, ":disgruntled_lords"),
       (assign, reg8, ":restless_lords"),
       (assign, reg9, ":hours_since_last_rest"),
       (assign, reg10, ":hours_since_last_decisive_event"),
       (str_store_string, s14, s26),

       (str_store_string, s9, "str_s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__"),

     (try_end),

     (try_begin),
       (neg|is_between, "$g_cheat_selected_faction", kingdoms_begin, kingdoms_end),
       (call_script, "script_get_next_active_kingdom", kingdoms_end),
       (assign, "$g_cheat_selected_faction", reg0),
     (try_end),
     (str_store_faction_name, s10, "$g_cheat_selected_faction"),
     (str_store_string, s9, "@Selected faction is: {s10}^^{s9}"),
    ],
    [
      ("faction_orders_next_faction", [], "{!}Select next faction.",
       [
         (call_script, "script_get_next_active_kingdom", "$g_cheat_selected_faction"),
         (assign, "$g_cheat_selected_faction", reg0),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),

      ("faction_orders_political_collapse", [], "{!}CHEAT - Cause all lords in faction to fall out with their liege.",
       [
       (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
	        (troop_slot_eq, ":lord", slot_troop_is_alive, 1),  ## he's alive/active
            (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
            (store_faction_of_troop, ":troop_faction", ":lord"),
            (eq, ":troop_faction", "$g_cheat_selected_faction"),
            (faction_get_slot, ":faction_liege", ":troop_faction", slot_faction_leader),
            (call_script, "script_troop_change_relation_with_troop", ":lord", ":faction_liege", -200),
       (try_end),

       ]
       ),

      ("faction_orders_defend", [], "{!}Force defend.",
       [
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_default),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_feast", [], "{!}Force feast.",
       [

         (assign, ":location_high_score", 0),
         (try_for_range, ":location", walled_centers_begin, walled_centers_end),
            (neg|party_slot_ge, ":location", slot_center_is_besieged_by, 1),
            (store_faction_of_party, ":location_faction", ":location"),
            (eq, ":location_faction", "$g_cheat_selected_faction"),
            (party_get_slot, ":location_lord", ":location", slot_town_lord),
            (troop_get_slot, ":location_score", ":location_lord", slot_troop_renown),
            (store_random_in_range, ":random", 0, 1000), #will probably be king or senior lord
            (val_add, ":location_score", ":random"),
            (gt, ":location_score", ":location_high_score"),
            (assign, ":location_high_score", ":location_score"),
            (assign, ":location_feast", ":location"),
         (try_end),

         (try_begin),
            (gt, ":location_feast", centers_begin),
            (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_feast),
            (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, ":location_feast"),
            (try_begin),
              (eq, "$g_player_eligible_feast_center_no", ":location_feast"),
              (assign, "$g_player_eligible_feast_center_no", -1),
            (try_end),

            (store_current_hours, ":hours"),
            (faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_feast_start_time, ":hours"),
         (try_end),

         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),


      ("faction_orders_gather", [], "{!}Force gather army.",
       [
         (store_current_hours, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_gathering_army),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_offensive_concluded, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_offensive_max_followers, 1),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_increase_time", [], "{!}Increase last offensive time by 24 hours.",
       [
         (faction_get_slot, ":faction_ai_last_offensive_time", "$g_cheat_selected_faction", slot_faction_last_offensive_concluded),
         (val_sub, ":faction_ai_last_offensive_time", 24),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_last_offensive_concluded, ":faction_ai_last_offensive_time"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink", [], "{!}Force rethink.",
       [
         (call_script, "script_init_ai_calculation"),
         (call_script, "script_decide_faction_ai", "$g_cheat_selected_faction"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink_all", [], "{!}Force rethink for all factions.",
       [
         (call_script, "script_recalculate_ais"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),

       ("enable_alt_ai",[(eq, "$g_use_alternative_ai", 2),], "{!}CHEAT! - enable alternative ai",
       [
       (assign, "$g_use_alternative_ai", 1),
       (jump_to_menu, "mnu_faction_orders"),
       ]
       ),

       ("disable_alt_ai",[(eq, "$g_use_alternative_ai", 2)], "{!}CHEAT! - disable alternative ai",
       [
       (assign, "$g_use_alternative_ai", 0),
       (jump_to_menu, "mnu_faction_orders"),
       ]
       ),

      ("faction_orders_init_econ", [], "{!}Initialize economic stats.",
       [
         (call_script, "script_initialize_economic_information"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),



      ("go_back_dot",[], "{!}Go back.",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("character_report",0,
   "{s9}",
   "none",
   [(try_begin),
      (gt, "$g_player_reading_book", 0),
      (player_has_item, "$g_player_reading_book"),
      (str_store_item_name, s8, "$g_player_reading_book"),
      (str_store_string, s9, "@You are currently reading {s8}."),
    (else_try),
      (assign, "$g_player_reading_book", 0),
      (str_store_string, s9, "@You are not reading any books."),
    (try_end),
    (assign, ":num_friends", 0),
    (assign, ":num_enemies", 0),
    (str_store_string, s6, "@none"),
    (str_store_string, s8, "@none"),
    (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	  (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ## he's alive/active
      (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
      (call_script, "script_troop_get_player_relation", ":troop_no"),
      (assign, ":player_relation", reg0),
      #(troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
      (try_begin),
        (gt, ":player_relation", 20),
        (try_begin),
          (eq, ":num_friends", 0),
          (str_store_troop_name, s8, ":troop_no"),
        (else_try),
          (eq, ":num_friends", 1),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{!}{s7}, {s8}"),
        (try_end),
        (val_add, ":num_friends", 1),
      (else_try),
        (lt, ":player_relation", -20),
        (try_begin),
          (eq, ":num_enemies", 0),
          (str_store_troop_name, s6, ":troop_no"),
        (else_try),
          (eq, ":num_enemies", 1),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5} and {s6}"),
        (else_try),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{!}{s5}, {s6}"),
        (try_end),
        (val_add, ":num_enemies", 1),
      (try_end),
    (try_end),

    #lord recruitment changes begin
    (str_clear, s12),
    (try_begin),
        (gt, "$player_right_to_rule", 0),
        (assign, reg12, "$player_right_to_rule"),
        (str_store_string, s12, "str__right_to_rule_reg12"),
    (try_end),

    (str_clear, s15),
    (try_begin),
        (this_or_next|gt, "$claim_arguments_made", 0),
        (this_or_next|gt, "$ruler_arguments_made", 0),
        (this_or_next|gt, "$victory_arguments_made", 0),
        (this_or_next|gt, "$lords_arguments_made", 0),
        (eq, 1, 0),

        (assign, reg3, "$claim_arguments_made"),
        (assign, reg4, "$ruler_arguments_made"),
        (assign, reg5, "$victory_arguments_made"),
        (assign, reg6, "$lords_arguments_made"),
        (assign, reg7, "$benefit_arguments_made"),

        (str_store_string, s15, "str_political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7"),
    (try_end),

    #lord recruitment changes begin

    (assign, reg3, "$player_honor"),
    (troop_get_slot, reg2, "trp_player", slot_troop_renown),

    (str_store_string, s9, "str_renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9"),


    (call_script, "script_get_number_of_hero_centers", "trp_player"),
    (assign, ":no_centers", reg0),
    (try_begin),
      (gt, ":no_centers", 0),
      (try_for_range, ":i_center", 0, ":no_centers"),
        (call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
        (assign, ":cur_center", reg0),
        (try_begin),
          (eq, ":i_center", 0),
          (str_store_party_name, s8, ":cur_center"),
        (else_try),
          (eq, ":i_center", 1),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{!}{s7}, {s8}"),
        (try_end),
      (try_end),
      (str_store_string, s9, "@Your estates are: {s8}.^{s9}"),
    (try_end),
    (try_begin),
	  ######### NEW v3.5
      (gt, "$players_kingdom", 0),
      (str_store_faction_name, s8, "$players_kingdom"),
      (neq, "$players_kingdom", fac_player_supporters_faction), 
      (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      (try_begin),
        (eq, "$freelancer_state", 1),        
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), 
          (str_store_troop_name, s8, "$enlisted_lord"),
          (str_store_faction_name, s10, "$players_kingdom"),
          (str_store_string, s9, "str_you_are_a_soldier_of_s8_s10_s9"),
      (else_try),
        (eq, "$player_cur_role", role_mercenary_captain),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), 
          (str_store_string, s9, "str_you_are_a_mercenary_captain_of_s8_s9"),
      (else_try),
        (eq, "$player_cur_role", role_vassal),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), 
          (str_store_string, s9, "str_you_are_a_lord_lady_of_s8_s9"),
      (else_try),
        (eq, "$player_cur_role", role_prince),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), 
          (str_store_string, s9, "str_you_are_prince_princess_of_s8_s9"),
      (else_try),
        # (eq, "$player_cur_role", role_king),
        (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          (str_store_string, s9, "str_you_are_king_queen_of_s8_s9"),
      (try_end),
    ###########################
    (else_try),
      (eq, "$players_kingdom", fac_player_supporters_faction),
      (try_begin),
        # (eq, "$player_cur_role", role_king),
        (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          (str_store_string, s9, "str_you_are_king_queen_of_s8_s9"),
      (else_try),
        (eq, "$player_cur_role", role_mercenary_captain),
          (str_store_string, s9, "str_you_are_a_mercenary_captain_s9"),
      (else_try),
        # (eq, "$player_cur_role", role_adventurer),
          (str_store_string, s9, "str_you_are_a_adventurer_s9"),
      (try_end),
	###########################
    (try_end),
    ],
    [

    #lord recruitment changes begin

    ("continue",[(eq, "$cheat_mode",1)], "{!}CHEAT! - increase Right to Rule",
       [
       (val_add, "$player_right_to_rule", 10),
       (jump_to_menu, "mnu_character_report"),
       ]
       ),


    ("continue",[(eq, "$cheat_mode",1),
        (str_store_troop_name, s14, "$g_talk_troop"),
    ], "{!}CHEAT! - increase your relation with {s14}",
       [
       (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 10),
       (jump_to_menu, "mnu_character_report"),
       ]
       ),


    ("continue",[(eq, "$cheat_mode",1)], "{!}CHEAT! - increase honor",
       [
       (val_add, "$player_honor", 10),
       (jump_to_menu, "mnu_character_report"),
       ]
       ),

    ("continue",[(eq, "$cheat_mode",1)], "{!}CHEAT! - increase renown",
       [
       (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
       (val_add, ":renown", 50),
       (troop_set_slot, "trp_player", slot_troop_renown, ":renown"),

       (jump_to_menu, "mnu_character_report"),
       ]
       ),

    ("continue",[(eq, "$cheat_mode",1)], "{!}CHEAT! - increase persuasion",
       [
       (troop_raise_skill, "trp_player", "skl_persuasion", 1),

       (jump_to_menu, "mnu_character_report"),
       ]
       ),



    ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),

    #lord recruitment changes end

       ]
  ),

  ("party_size_report",0,
   "{s1}",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),

	######### NEW v3.8
	(str_clear, s1),
	(str_clear, s2),
	(str_clear, s3),
	(str_clear, s4),
	(str_clear, s5),
	(str_clear, s6),
	(str_clear, s7),
	(str_clear, s8),
	##################
	
	############# NEW v2.0
    (assign, ":base_size", "$g_party_base_size"), 

    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
    (val_mul, ":leadership", "$g_party_size_leadership_bonus"),
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),

    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":renown", "$g_party_size_renown_bonus_divider"),
    
    (try_begin),
      (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
      (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
      (eq, "$g_player_cur_role", role_king),  ####### NEW v3.0 - player role
        (assign, ":king_bonus", "$g_party_size_king_bonus"),
    (try_end),

    (try_begin),
      (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
      (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
        (assign, ":marshall_bonus", "$g_party_size_marshall_bonus"),
    (try_end),
    
    (assign, ":castle_bonus", 0),
    (try_for_range, ":cur_center", castles_begin, castles_end),
      # (party_get_slot, ":party_leader", ":cur_center", slot_town_lord),
      (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
      (val_add, ":castle_bonus", "$g_party_size_castle_bonus"),
    (try_end),
    
    (try_begin),
      (gt, ":leadership", 0),
      (str_store_string, s2, "@{!} +"),
    (else_try),
      (str_store_string, s2, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":charisma", 0),
      (str_store_string, s3, "@{!} +"),
    (else_try),
      (str_store_string, s3, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":renown", 0),
      (str_store_string, s4, "@{!} +"),
    (else_try),
      (str_store_string, s4, "str_space"),
    (try_end),
    
    ##### NEW
    (try_begin),
      (gt, ":king_bonus", 0),
      (str_store_string, s5, "@{!} +"),
    (else_try),
      (str_store_string, s5, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":marshall_bonus", 0),
      (str_store_string, s6, "@{!} +"),
    (else_try),
      (str_store_string, s6, "str_space"),
    (try_end),
    (try_begin),
      (gt, ":castle_bonus", 0),
      (str_store_string, s7, "@{!} +"),
    (else_try),
      (str_store_string, s7, "str_space"),
    (try_end),
	########## NEW v2.0
    (try_begin),
      (gt, ":base_size", 0),
      (str_store_string, s8, "@{!} +"),
    (else_try),
      (str_store_string, s8, "str_space"),
    (try_end),
    
    (assign, reg7, ":party_size_limit"),
    (assign, reg1, ":leadership"),
    (assign, reg2, ":charisma"),
    (assign, reg3, ":renown"),
    
    (assign, reg4, ":king_bonus"),
    (assign, reg5, ":marshall_bonus"),
    (assign, reg6, ":castle_bonus"),
	
	######### NEW v2.0
    (assign, reg8, ":base_size"),
        
    (str_store_string, s1, "@Current party size limit is {reg7}.^Current party size modifiers are:^^Base size: {s8}{reg8}^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^King: {s5}{reg4}^Marshall: {s6}{reg5}^Castles: {s7}{reg6}^TOTAL:  {reg7}"),
    ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_relations_report",0,
   "{s1}",
   "none",
   [(str_clear, s2),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      # (neq, ":cur_kingdom", "fac_player_supporters_faction"),
      (neq, ":cur_kingdom", "$players_kingdom"),
      # (store_relation, ":cur_relation", "fac_player_supporters_faction", ":cur_kingdom"),
      (store_relation, ":cur_relation", "$players_kingdom", ":cur_kingdom"),  ######### NEW v3.3
      (try_begin),
        (ge, ":cur_relation", 90),
        (str_store_string, s3, "@Loyal"),
      (else_try),
        (ge, ":cur_relation", 80),
        (str_store_string, s3, "@Devoted"),
      (else_try),
        (ge, ":cur_relation", 70),
        (str_store_string, s3, "@Fond"),
      (else_try),
        (ge, ":cur_relation", 60),
        (str_store_string, s3, "@Gracious"),
      (else_try),
        (ge, ":cur_relation", 50),
        (str_store_string, s3, "@Friendly"),
      (else_try),
        (ge, ":cur_relation", 40),
        (str_store_string, s3, "@Supportive"),
      (else_try),
        (ge, ":cur_relation", 30),
        (str_store_string, s3, "@Favorable"),
      (else_try),
        (ge, ":cur_relation", 20),
        (str_store_string, s3, "@Cooperative"),
      (else_try),
        (ge, ":cur_relation", 10),
        (str_store_string, s3, "@Accepting"),
      (else_try),
        (ge, ":cur_relation", 0),
        (str_store_string, s3, "@Indifferent"),
      (else_try),
        (ge, ":cur_relation", -10),
        (str_store_string, s3, "@Suspicious"),
      (else_try),
        (ge, ":cur_relation", -20),
        (str_store_string, s3, "@Grumbling"),
      (else_try),
        (ge, ":cur_relation", -30),
        (str_store_string, s3, "@Hostile"),
      (else_try),
        (ge, ":cur_relation", -40),
        (str_store_string, s3, "@Resentful"),
      (else_try),
        (ge, ":cur_relation", -50),
        (str_store_string, s3, "@Angry"),
      (else_try),
        (ge, ":cur_relation", -60),
        (str_store_string, s3, "@Hateful"),
      (else_try),
        (ge, ":cur_relation", -70),
        (str_store_string, s3, "@Revengeful"),
      (else_try),
        (str_store_string, s3, "@Vengeful"),
      (try_end),
      (str_store_faction_name, s4, ":cur_kingdom"),
      (assign, reg1, ":cur_relation"),
      (str_store_string, s2, "@{!}{s2}^{s4}: {reg1} ({s3})"),
    (try_end),
    (str_store_string, s1, "@Your relation with the factions are:^{s2}"),



    ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("camp",mnf_scale_picture,
   "You set up camp. What do you want to do?",
   "none",
   [
     (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
     #(set_background_mesh, "mesh_pic_test_menu"),
    ],
    [
####### NEW v2.9-KOMKE START-    
     # ("camp_modding",[(eq, 1, 1), is_edit_mode_enabled],"Go to the modding menu.",## menu only available in edit mode when releasing new version set this to false so it is disabled
     ("camp_modding",[(ge, "$cheat_mode", 1)],"Go to the modding menu.",## menu only available in edit mode when releasing new version set this to false so it is disabled
       [
       # (assign, "$g_lord_creation_rate", 0), #### lord creation OFF
       # (assign, "$g_lord_death_chance_battle", 0),#### lord death OFF
       # (assign, "$g_lord_death_chance_battle_king", 0),
       # (assign, "$g_lord_death_chance_assassination", 0), 
       # (assign, "$g_lord_death_chance_assassination_king", 0),   
       # (assign, "$g_lord_death_chance_execution_base", 0),
       # (assign, "$g_lord_death_chance_execution_king_variation", 0),
       # (assign, "$g_lord_death_chance_execution_relation_divider", 3),
       (jump_to_menu, "mnu_camp_modding"),]
     ),       
####### NEW v2.9-KOMKE END-     
      # ("camp_action_1",[], "Walk around.",
       # [(set_jump_mission, "mt_ai_training"),
        # (call_script, "script_setup_random_scene"),
        # (change_screen_mission),
        # ]
       # ),
       
      ("camp_action_1",[], "Walk around the campsite.", #dckplmc
       [(set_jump_mission, "mt_camp"),
        (call_script, "script_setup_camp_scene"),
        (change_screen_mission),
        ]
       ),
       
       
       ("camp_disband_lances",[(eq, "$use_feudal_lance", 1),], "Disband lance forces.",
       [
         (assign, "$g_next_menu", "mnu_camp"),
         (jump_to_menu, "mnu_disband_lances"),
         
        ]
       ),
       
       # ("camp_reblance",[], "Troop rebalancing options",
       # [
        # (try_begin),
          # (eq, "$culture_pool", 0),
          # (call_script, "script_initialize_culture_pools"),
          # (assign, "$culture_pool", 1),
          
        # (try_end),
        # (call_script, "script_rebalance_troops_by_culture"),
        # (jump_to_menu, "mnu_mod_troop_rebalance"), 
         
        # ]
       # ),
       
        # ("camp_recruit_companions",[], "Companion test",
       # [
         
         # (jump_to_menu, "mnu_recruit_companions"),
         
        # ]
       # ),

#### export/import NPCs begin ####
      ("action_export_import",[], "Export/Import NPCs.",
        [
          (assign, "$g_player_troop", "trp_player"),
          (jump_to_menu, "mnu_export_import_npcs"),
        ]
      ),
#### export/import NPCs end ####

#### mod options ####
      ("action_mod_options",[], "1257AD Options.",
        [          
          (start_presentation, "prsnt_mod_options"),
        ]
      ),
#### mod options ####







### NEW mod options ####
      ("action_mod_options_2",[], "Enhanced Options.",
        [          
         (jump_to_menu, "mnu_enhanced_mod_options"),
        ]
      ),
#############################################




## NEW debug options ####
      ("action_mod_options_3",[
      (ge, "$cheat_mode", 1)
      ],
      "Debug Options.",
        [          
         (jump_to_menu, "mnu_debug_options"),
        ]
      ),
############################################









#### faction colours ####
      ("action_faction_colours",[], "Change faction colours.",
        [          
          (start_presentation, "prsnt_change_all_factions_color"),
        ]
      ),
#### faction colours ####

    # autoloot
    ("camp_manage_inventory",
      [
        (assign, ":num_companions", 0),
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
          (is_between, ":stack_troop", companions_begin, companions_end),
          (val_add, ":num_companions", 1),
        (try_end),
        (gt, ":num_companions", 0),
      ],
      "Manage your party's inventory.",
      [
        (troop_clear_inventory, "trp_temp_troop"),
        (assign, "$return_menu", "mnu_camp"),
        (assign, "$inventory_menu_offset", 0),
        ## CC
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":this_hero", "p_main_party", ":i_stack"),
          (is_between, ":this_hero", companions_begin, companions_end),
          (call_script, "script_transfer_inventory", ":this_hero", "trp_temp_troop", 0),
        (try_end),
        (troop_sort_inventory, "trp_temp_troop"),
        ## CC
        (jump_to_menu, "mnu_manage_loot_pool"),
      ]
    ),
    # autoloot
	
	
########## NEW v3.0 - player can customize troops is he has a fief
    ("ee_new_1",
      [
      (eq, "$g_player_know_culture_player", 1),
      (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
      (assign, ":num_fiefs", 0),
      (try_for_range, ":cur_center", centers_begin, centers_end),
        (party_get_slot, ":town_lord", ":cur_center", slot_town_lord),
        (eq, ":town_lord", "trp_player"),
          (val_add, ":num_fiefs", 1),
      (try_end),
      (gt, ":num_fiefs", 0),
      ],
      "Customize your kingdom's troops.",
      [
      (try_begin),
        (gt, "$cstm_troops_begin", 0),
          (assign, "$cstm_selected_troop", -1),
          (start_presentation, "prsnt_cstm_view_custom_troop_tree"),
      (else_try),
        (troop_set_name, cstm_troop_tree_prefix, "@Custom"),            
	    (assign, "$cstm_num_tiers", 5),
	    (assign, "$cstm_troops_begin", "trp_cstm_custom_troop_3_tiers_0_0_0"),
	    (assign, "$cstm_troops_end", "trp_cstm_custom_troop_3_tiers_1_0_0"),
	    (assign, "$cstm_presentation_troop", "trp_cstm_presentation_troop_0"),
        (start_presentation, "prsnt_cstm_view_custom_troop_tree"),
      (try_end),
      ]
    ),
##################################################

      ("camp_action",[], "Take an action.",
       [(jump_to_menu, "mnu_camp_action"),
        ]
       ),
      ("camp_wait_here",[], "Wait here for some time.",
       [
           (assign, "$g_camp_mode", 1),
           (assign, "$g_infinite_camping", 0),
           (assign, "$g_player_icon_state", pis_camping),
           #tom
           # (store_current_hours, ":hours"),
           # (assign, "$g_camp_start", ":hours"),
           #tom
           (rest_for_hours_interactive, 24 * 365, 5, 1), #rest while attackable
           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),
           (try_end),
           (change_screen_return),
        ]
       ),
      ("camp_cheat",
       [(ge, "$cheat_mode", 1)
        ], "CHEAT MENU!",
       [(jump_to_menu, "mnu_camp_cheat"),
        ],
       ),
      ("resume_travelling",[], "Resume travelling.",
       [
           (change_screen_return),
        ]
       ),
      ]
  ),
  
  ("mod_troop_rebalance",0,
   "This is an experimental feature to rebalances troop armour values to their appropriate tier. {s10}^^   What does it do? The troops are automatically re-equipped via scripts with a set range of body armours and helmets   appriopriate to their tier and culture.^^   Using this feature will make the gameplay more balanced, while still being historically correct. This   however will likely make the artistic values of the troop design obsolete.^^   To turn of this feature you will require to reload the game (it will not affect the save game in any way).   It's required you to do so, so the game engine could reload the troop items from the mod files. Turning on this feature   does not require you to reload the game.",
   "none",
   [
    (try_begin),
      (eq, "$culture_pool", 0),
      (str_store_string, s10, "@Currently this feature is turned off. "),
    (else_try),
      (str_store_string, s10, "@Currently this feature is turned on. "),
    (try_end),
   ],
    [
      ("turn_on",
      [
        (eq, "$culture_pool", 0),
      ], "Turn troop rebalancing on",
      [
        
        #building pool
        (try_begin),
          (eq, "$culture_pool_initialized", 0),
          (call_script, "script_initialize_culture_pools"),
          (assign, "$culture_pool_initialized", 1),
        (try_end),
        #equiping troops
        (assign, "$culture_pool", 1),
        (call_script, "script_rebalance_troops_by_culture"),
      ]
      ),
      ("turn_off",
      [
        (eq, "$culture_pool", 1),
      ], "Turn troop rebalancing off (You will need to reload the game for this to take effect)",
      [
        (assign, "$culture_pool", 0),
      ]
      ),


      ("back_to_camp_menu",[], "Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  ("camp_cheat",0,
   "Select a cheat:",
   "none",
   [
     ],
    [
      ("camp_cheat_find_item",[], "Find an item...",
       [
         (jump_to_menu, "mnu_cheat_find_item"),
       ]
       ),

      ("camp_cheat_find_item_weather",[], "Change weather..",
       [
         (jump_to_menu, "mnu_cheat_change_weather"),
       ]
       ),

      ("camp_cheat_1",[], "{!}Increase player renown.",
       [
         (str_store_string, s1, "@Player renown is increased by 100. "),
         (call_script, "script_change_troop_renown", "trp_player", 100),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),

      ("camp_cheat_2",[], "{!}Increase player honor.",
       [
         (assign, reg7, "$player_honor"),
         (val_add, reg7, 1),
         (display_message, "@Player honor is increased by 1 and it is now {reg7}."),
         (val_add, "$player_honor", 1),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),

      ("camp_cheat_3",[], "{!}Update political notes.",
       [
         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
	       (troop_slot_eq, ":hero", slot_troop_is_alive, 1),  ## he's alive/active
           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
           (call_script, "script_update_troop_political_notes", ":hero"),
         (try_end),

         (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
           (call_script, "script_update_faction_political_notes", ":kingdom"),
         (try_end),
        ]
       ),

      ("camp_cheat_4",[], "{!}Update troop notes.",
       [
         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
	       (troop_slot_eq, ":hero", slot_troop_is_alive, 1),  ## he's alive/active
           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
           (call_script, "script_update_troop_notes", ":hero"),
         (try_end),

         (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
           (call_script, "script_update_troop_notes", ":lady"),
           (call_script, "script_update_troop_political_notes", ":lady"),
           (call_script, "script_update_troop_location_notes", ":lady", 0),
         (try_end),
        ]
       ),

      ("camp_cheat_5",[], "{!}Scramble minstrels.",
       [
         (call_script, "script_update_tavern_minstrels"),
        ]
       ),

      ("camp_cheat_6",[], "{!}Infinite camp",
       [
         (assign, "$g_camp_mode", 1),
         (assign, "$g_infinite_camping", 1),
         (assign, "$g_player_icon_state", pis_camping),
         #(rest_for_hours_interactive, 10 * 24 * 365, 20), #10 year rest while not attackable with 20x speed
         (rest_for_hours_interactive, 10 * 24 * 365, 60), #tom
         (change_screen_return),
        ]
       ),

      ("cheat_faction_orders",[(ge, "$cheat_mode",1)],
      "{!}Cheat: Set Debug messages to All.",
       [(assign, "$cheat_mode",1),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
      (ge, "$cheat_mode", 1),
      (neq, "$cheat_mode",3)], "{!}Cheat: Set Debug messages to Econ Only.",
       [(assign, "$cheat_mode",3),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
      (ge, "$cheat_mode", 1),
      (neq, "$cheat_mode",4)], "{!}Cheat: Set Debug messages to Political Only.",
       [(assign, "$cheat_mode",4),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),


      ("back_to_camp_menu",[], "{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("cheat_find_item",0,
   "{!}Current item range: {reg5} to {reg6}",
   "none",
   [
     (assign, reg5, "$cheat_find_item_range_begin"),
     (store_add, reg6, "$cheat_find_item_range_begin", max_inventory_items),
     (val_min, reg6, "itm_items_end"),
     (val_sub, reg6, 1),
     ],
    [
      ("cheat_find_item_next_range",[], "{!}Move to next item range.",
       [
        (val_add, "$cheat_find_item_range_begin", max_inventory_items),
        (try_begin),
          (ge, "$cheat_find_item_range_begin", "itm_items_end"),
          (assign, "$cheat_find_item_range_begin", 0),
        (try_end),
        (jump_to_menu, "mnu_cheat_find_item"),
       ]
       ),
      #### NEW
      ("cheat_find_item_previous_range",[], "{!}Move to previous item range.",
       [
        (val_sub, "$cheat_find_item_range_begin", max_inventory_items),
        (try_begin),
          (ge, "$cheat_find_item_range_begin", "itm_items_end"),
          (assign, "$cheat_find_item_range_begin", 0),
        (try_end),
        (jump_to_menu, "mnu_cheat_find_item"),
       ]
       ),

       ("cheat_find_item_choose_this",[], "{!}Choose from this range.",
       [
        (troop_clear_inventory, "trp_find_item_cheat"),
        (store_add, ":max_item", "$cheat_find_item_range_begin", max_inventory_items),
        (val_min, ":max_item", "itm_items_end"),
        (store_sub, ":num_items_to_add", ":max_item", "$cheat_find_item_range_begin"),
        (try_for_range, ":i_slot", 0, ":num_items_to_add"),
          (store_add, ":item_id", "$cheat_find_item_range_begin", ":i_slot"),
          (troop_add_items, "trp_find_item_cheat", ":item_id", 1),
        (try_end),
        (change_screen_trade, "trp_find_item_cheat"),
       ]
       ),

      ("camp_action_4",[], "{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

   ("cheat_change_weather",0,
   "{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}",
   "none",
   [
     (get_global_cloud_amount, reg5),
     (get_global_haze_amount, reg6),
     ],
    [
      ("cheat_increase_cloud",[], "{!}Increase Cloud Amount.",
       [
        (get_global_cloud_amount, ":cur_cloud_amount"),
        (val_add, ":cur_cloud_amount", 5),
        (val_min, ":cur_cloud_amount", 100),
        (set_global_cloud_amount, ":cur_cloud_amount"),
       ]
       ),
      ("cheat_decrease_cloud",[], "{!}Decrease Cloud Amount.",
       [
        (get_global_cloud_amount, ":cur_cloud_amount"),
        (val_sub, ":cur_cloud_amount", 5),
        (val_max, ":cur_cloud_amount", 0),
        (set_global_cloud_amount, ":cur_cloud_amount"),
       ]
       ),
      ("cheat_increase_fog",[], "{!}Increase Fog Amount.",
       [
        (get_global_haze_amount, ":cur_fog_amount"),
        (val_add, ":cur_fog_amount", 5),
        (val_min, ":cur_fog_amount", 100),
        (set_global_haze_amount, ":cur_fog_amount"),
       ]
       ),
      ("cheat_decrease_fog",[], "{!}Decrease Fog Amount.",
       [
        (get_global_haze_amount, ":cur_fog_amount"),
        (val_sub, ":cur_fog_amount", 5),
        (val_max, ":cur_fog_amount", 0),
        (set_global_haze_amount, ":cur_fog_amount"),
       ]
       ),

      ("camp_action_4",[], "{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action",0,
   "Choose an action:",
   "none",
   [
     ],
    [


      ("camp_recruit_prisoners",
       [(troops_can_join, 1),
        (store_current_hours, ":cur_time"),
        (val_sub, ":cur_time", 24),
        (gt, ":cur_time", "$g_prisoner_recruit_last_time"),
        (try_begin),
          (gt, "$g_prisoner_recruit_last_time", 0),
          (assign, "$g_prisoner_recruit_troop_id", 0),
          (assign, "$g_prisoner_recruit_size", 0),
          (assign, "$g_prisoner_recruit_last_time", 0),
        (try_end),
        ], "Recruit some of your prisoners to your party.",
       [(jump_to_menu, "mnu_camp_recruit_prisoners"),
        ],
       ),

      ("action_read_book",[], "Select a book to read.",
       [(jump_to_menu, "mnu_camp_action_read_book"),
        ]
       ),
      ("action_rename_kingdom",
       [
         (eq, "$players_kingdom_name_set", 1),
         # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),  ######### NEW v3.3
         # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
         (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
         ], "Rename your kingdom.",
       [(start_presentation, "prsnt_name_kingdom"),
        ]
       ),

      ("action_modify_banner",[], "{!}Modify your banner.",
       [
           (start_presentation, "prsnt_banner_selection"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),
	   

################# NEW v2.1 - Wagon Trains
    ("camp_wagon",
	[
	(eq, "$wagon_active", 0),
	],"Form a wagon train (300 coins).",
    [
	 (store_troop_gold, ":gold_amount", "trp_player"),
     (try_begin),
       (ge, ":gold_amount", 300),
       (try_begin),
	     # (le, "$wagon_active", 0),
           (troop_remove_gold, "trp_player", 300),
	       (set_spawn_radius, 1),
           # (party_relocate_near_party, "p_wagon_train", "p_main_party", 1), 
           (spawn_around_party, "p_main_party", "pt_wagon_train_template"),  ###### NEW v3.9 - 
		   # (enable_party, "p_wagon_train"),
           (assign, "$wagon_active", reg0),
		   (party_add_members, "$wagon_active", "trp_wagon_master", 1),  ######## fixes crash
           (display_message, "@Wagon train formed nearby."),
	   (else_try),
         (display_message, "@You already have a wagon train!"),
       (try_end),
     (else_try),
       (lt, ":gold_amount", 300),
	     (display_message, "@You don't have enough money to form a wagon train!"),
     (try_end),
    ]),
#################

################# NEW v3.9 - Disband Wagon Trains
    ("camp_wagon_disband",
	[
	(gt, "$wagon_active", 0),
	],"Disband the wagon train.",
    [
    (try_begin),
      (remove_party, "$wagon_active"), 
      (assign, "$wagon_active", 0),
      (display_message, "@Wagon train disbanded."),
    (try_end),
    ]),
#################
	   
	   
      ("action_retire",[], "Retire from adventuring.",
       [(jump_to_menu, "mnu_retirement_verify"),
        ]
       ),
      ("camp_action_4",[], "Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_recruit_prisoners",0,
   "You offer your prisoners freedom if they agree to join you as soldiers. {s18}",
   "none",
   [(assign, ":num_regular_prisoner_slots", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":cur_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
      (neg|troop_is_hero, ":cur_troop_id"),
      (val_add, ":num_regular_prisoner_slots", 1),
    (try_end),
    (try_begin),
      (eq, ":num_regular_prisoner_slots", 0),
      (jump_to_menu, "mnu_camp_no_prisoners"),
    (else_try),
      (eq, "$g_prisoner_recruit_troop_id", 0),
      (store_current_hours, "$g_prisoner_recruit_last_time"),
      (store_random_in_range, ":rand", 0, 100),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (store_sub, ":reject_chance", 15, ":persuasion_level"),
      (val_mul, ":reject_chance", 4),
      (try_begin),
        (lt, ":rand", ":reject_chance"),
        (assign, "$g_prisoner_recruit_troop_id", -7),
      (else_try),
        (assign, ":num_regular_prisoner_slots", 0),
        (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_add, ":num_regular_prisoner_slots", 1),
        (try_end),
        (store_random_in_range, ":random_prisoner_slot", 0, ":num_regular_prisoner_slots"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_sub, ":random_prisoner_slot", 1),
          (lt, ":random_prisoner_slot", 0),
          (assign, ":num_stacks", 0),
          (assign, "$g_prisoner_recruit_troop_id", ":cur_troop_id"),
          (party_prisoner_stack_get_size, "$g_prisoner_recruit_size", "p_main_party", ":cur_stack"),
        (try_end),
      (try_end),

      (try_begin),
        (gt, "$g_prisoner_recruit_troop_id", 0),
        (party_get_free_companions_capacity, ":capacity", "p_main_party"),
        (val_min, "$g_prisoner_recruit_size", ":capacity"),
        (assign, reg1, "$g_prisoner_recruit_size"),
        (gt, "$g_prisoner_recruit_size", 0),
        (try_begin),
          (gt, "$g_prisoner_recruit_size", 1),
          (assign, reg2, 1),
        (else_try),
          (assign, reg2, 0),
        (try_end),
        (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (str_store_string, s18, "@{reg1} {s1} {reg2?accept:accepts} the offer."),
      (else_try),
        (str_store_string, s18, "@No one accepts the offer."),
      (try_end),
    (try_end),
    ],
    [
      ("camp_recruit_prisoners_accept",[(gt, "$g_prisoner_recruit_troop_id", 0)], "Take them.",
       [(remove_troops_from_prisoners, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (party_add_members, "p_main_party", "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (store_mul, ":morale_change", -3, "$g_prisoner_recruit_size"),
        (call_script, "script_change_player_party_morale", ":morale_change"),
        (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("camp_recruit_prisoners_reject",[(gt, "$g_prisoner_recruit_troop_id", 0)], "Reject them.",
       [(jump_to_menu, "mnu_camp"),
        (assign, "$g_prisoner_recruit_troop_id", 0),
        (assign, "$g_prisoner_recruit_size", 0),
        ]
       ),
      ("continue",[(le, "$g_prisoner_recruit_troop_id", 0)], "Go back.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_no_prisoners",0,
   "You have no prisoners to recruit from.",
   "none",
   [],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book",0,
   "Choose a book to read:",
   "none",
   [],
    [
      ("action_read_book_1",[(player_has_item, "itm_book_tactics"),
                             (item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_tactics"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_tactics"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_2",[(player_has_item, "itm_book_persuasion"),
                             (item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_persuasion"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_persuasion"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_3",[(player_has_item, "itm_book_leadership"),
                             (item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_leadership"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_leadership"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_4",[(player_has_item, "itm_book_intelligence"),
                             (item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_intelligence"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_intelligence"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_5",[(player_has_item, "itm_book_trade"),
                             (item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_trade"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_trade"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_6",[(player_has_item, "itm_book_weapon_mastery"),
                             (item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_weapon_mastery"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_weapon_mastery"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_7",[(player_has_item, "itm_book_engineering"),
                             (item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_engineering"),
                             ], "{s1}.",
       [(assign, "$temp", "itm_book_engineering"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("camp_action_4",[], "Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book_start",0,
   "{s1}",
   "none",
   [(assign, ":new_book", "$temp"),
    (str_store_item_name, s2, ":new_book"),
    (try_begin),
      (store_attribute_level, ":int", "trp_player", ca_intelligence),
      (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
      (le, ":int_req", ":int"),
      (str_store_string, s1, "@You start reading {s2}. After a few pages, you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time."),
      (assign, "$g_player_reading_book", ":new_book"),
    (else_try),
      (str_store_string, s1, "@You flip through the pages of {s2}, but you find the text confusing and difficult to follow. Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
    (try_end),],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),


  ("retirement_verify",0,
   "You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?",
   "none",
   [
     (store_current_day, reg0),
     (assign, reg1, "$g_player_luck"),
     ],
    [
      ("retire_yes",[], "Yes.",
       [
         (start_presentation, "prsnt_retirement"),
        ]
       ),
      ("retire_no",[], "No.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("end_game",0,
   "The decision is made, and you resolve to give up your adventurer's life and settle down. You sell off your weapons and armour, gather up all your money, and ride off into the sunset...",
   "none",
   [],
    [
      ("end_game_bye",[], "Farewell.",
       [
         (change_screen_quit),
        ]
       ),
      ]
  ),

  ("cattle_herd",mnf_scale_picture,
   "You encounter a herd of cattle.",
   "none",
   [(play_sound, "snd_cow_moo"),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("cattle_drive_away",[], "Drive the cattle onward.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
        (party_set_ai_object, "$g_encountered_party", "p_main_party"),
        (change_screen_return),
        ]
       ),
      ("cattle_stop",[], "Bring the herd to a stop.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
        (change_screen_return),
        ]
       ),
      ("cattle_kill",[(assign, ":continue", 1),
                      (try_begin),
                        (check_quest_active, "qst_move_cattle_herd"),
                        (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
                        (assign, ":continue", 0),
                      (try_end),
                      (eq, ":continue", 1)], "Slaughter some of the animals.",
       [(jump_to_menu, "mnu_cattle_herd_kill"),
        ]
       ),
      ("leave",[], "Leave.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill",0,
   "How many animals do you want to slaughter?",
   "none",
   [(party_get_num_companions, reg5, "$g_encountered_party")],
    [
      ("cattle_kill_1",[(ge, reg5, 1),], "One.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_2",[(ge, reg5, 2),], "Two.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_3",[(ge, reg5, 3),], "Three.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_4",[(ge, reg5, 4),], "Four.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_5",[(ge, reg5, 5),], "Five.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("go_back_dot",[], "Go back.",
       [(jump_to_menu, "mnu_cattle_herd"),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill_end",0,
   "{!}You shouldn't be reading this.",
   "none",
   [(change_screen_return)],
    [
      ]
  ),


  ("arena_duel_fight",0,
   "You and your opponent prepare to duel.",
   "none",
   [],
   [
     ("continue",[], "Continue...",
      [
        (assign, "$g_leave_encounter", 0),

        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (party_get_slot, ":duel_scene", "$g_encountered_party", slot_town_arena),
        (else_try),
          (eq, "$g_start_arena_fight_at_nearest_town", 1),
          (assign, ":closest_town", -1),
          (assign, ":minimum_dist", 10000),
          (try_for_range, ":cur_town", towns_begin, towns_end),
            (store_distance_to_party_from_party, ":dist", ":cur_town", "$g_encountered_party"),
            (lt, ":dist", ":minimum_dist"),
            (assign, ":minimum_dist", ":dist"),
            (assign, ":closest_town", ":cur_town"),
          (try_end),
          (try_begin),
            (ge, ":closest_town", 0),
            (party_get_slot, ":duel_scene", ":closest_town", slot_town_arena),
          (try_end),
          (assign, "$g_start_arena_fight_at_nearest_town", 0),
        (else_try),
          (party_get_current_terrain, ":terrain", "p_main_party"),
          (eq, ":terrain", 4),
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_3"),
        (else_try),
          (eq, ":terrain", 5),
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_4"),
        (else_try),
          (assign, ":duel_scene", "scn_training_ground_ranged_melee_1"),
        (try_end),

        (modify_visitors_at_site, ":duel_scene"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 1, "$g_duel_troop"),
        (set_jump_mission, "mt_duel_with_lord"),
        (jump_to_scene, ":duel_scene"),
        (jump_to_menu, "mnu_arena_duel_conclusion"),
        (change_screen_mission),
      ]),
    ]
  ),


  ("arena_duel_conclusion",0,
   "{!}{s11}",
   "none",
   [

    (try_begin),
        (eq, "$g_leave_encounter", 1),
        (change_screen_return),
    (try_end),


    (str_store_troop_name, s10, "$g_duel_troop"),
    (try_begin),
        (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_failed, "qst_duel_for_lady"),
        (str_store_string, s11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_succeeded, "qst_duel_for_lady"),
        (str_store_string, s11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_failed, "qst_duel_courtship_rival"),
        (str_store_string, s11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_succeeded, "qst_duel_courtship_rival"),
        (str_store_string, s11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_succeeded, "qst_duel_avenge_insult"),
        (str_store_string, s11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_failed, "qst_duel_avenge_insult"),
        (str_store_string, s11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_succeeded, "qst_denounce_lord"),
        (str_store_string, s11, "str_s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel"),
    (else_try),
        (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_duel_troop"),
        (check_quest_failed, "qst_denounce_lord"),
        (str_store_string, s11, "str_you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel"),
    (else_try),
        (str_store_troop_name, s10, "$g_duel_troop"),
    (try_end),
   ],
   [
     ("continue",[], "Continue...",
      [
        (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
        (modify_visitors_at_site, ":meeting_scene"),
        (reset_visitors),
        (set_visitor,0, "trp_player"),
        (set_visitor,17, "$g_duel_troop"),
        (set_jump_mission, "mt_conversation_encounter"),
        (jump_to_scene, ":meeting_scene"),
        (assign, "$talk_context", tc_after_duel),
        (change_screen_map_conversation, "$g_duel_troop"),
        ]),
      ]
  ),

   ("simple_encounter",mnf_enable_hot_keys|mnf_scale_picture,
    "{s2} You have {reg10} troops fit for battle against their {reg11}.",
    "none",
    [
      (assign, "$g_enemy_party", "$g_encountered_party"),
      (assign, "$g_ally_party", -1),
      (call_script, "script_encounter_calculate_fit"),
      (try_begin),
        (eq, "$new_encounter", 1),
        (assign, "$new_encounter", 0),
        (assign, "$g_encounter_is_in_village", 0),
        (assign, "$g_encounter_type", 0),
        (try_begin),
          (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),
          (party_get_slot, ":village_no", "$g_enemy_party", slot_party_ai_object),

          (store_distance_to_party_from_party, ":dist", ":village_no", "$g_enemy_party"),

          (try_begin),
            (lt, ":dist", raid_distance),
            (assign, "$g_encounter_is_in_village", ":village_no"),
            (assign, "$g_encounter_type", enctype_fighting_against_village_raid),
          (try_end),
          
        (try_end),
        
        (try_begin),          
          (eq, "$g_player_sallies", "$g_encountered_party"),
          (assign, "$g_encounter_type", enctype_player_sally),
        (try_end),
        
        (try_begin),
          (gt, "$g_player_raiding_village", 0),
          (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
          (assign, "$g_encounter_type", enctype_catched_during_village_raid),
          (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
          (str_store_string, s1, "@Villagers"),
          (display_message, "str_s1_joined_battle_enemy", 0xFF5050),
        (else_try),
          (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
          (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
          (str_store_string, s1, "@Villagers"),
          (display_message, "str_s1_joined_battle_friend", 0x50FF50),
          # Let village party join battle at your side
        (else_try),
          (eq, "$g_encounter_type", enctype_player_sally),
          (party_quick_attach_to_current_battle, "$g_player_sally_town", 0), #attach as friend
          (str_store_string, s1, "@The garrison"),
          (display_message, "str_s1_joined_battle_friend", 0x50FF50),
          # Let village party join battle at your side
        (try_end),

        (try_begin),
          # (neq, "$g_battle_preparation_phase", 1),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
          (call_script, "script_encounter_init_variables"),
        (try_end),
        
        (assign, "$encountered_party_hostile", 0),
        (assign, "$encountered_party_friendly", 0),
        (try_begin),
          (gt, "$g_encountered_party_relation", 0),
          (assign, "$encountered_party_friendly", 1),
        (try_end),
        (try_begin),
          (lt, "$g_encountered_party_relation", 0),
          (assign, "$encountered_party_hostile", 1),
          (try_begin),
            # (this_or_next | eq, "$g_battle_preparation_phase", 3),
            (encountered_party_is_attacker),
            (assign, "$cant_leave_encounter", 1),
          (try_end),
        (try_end),
        (assign, "$talk_context", tc_party_encounter),
        (call_script, "script_setup_party_meeting", "$g_encountered_party"),        
      (else_try), #second or more turn
        (try_begin),
          # We can leave battle only after some troops have been killed.
          (eq, "$cant_leave_encounter", 1),
          (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
          (assign, ":org_total_party_counts", reg0),
          (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
          (val_add, ":org_total_party_counts", reg0),

          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":cur_total_party_counts", reg0),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (val_add, ":cur_total_party_counts", reg0),

          (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
          (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
          (assign, "$cant_leave_encounter", 0),
        (try_end),
        (eq, "$g_leave_encounter",1),
        (change_screen_return),
      (try_end),

        #setup s2
      (try_begin),
        (party_is_active, "$g_encountered_party"),
        (str_store_party_name, s1, "$g_encountered_party"),
        (try_begin),
          (eq, "$g_encounter_type", 0),
          (str_store_string, s2, "@You have encountered {s1}."),
        (else_try),
          (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
          (str_store_party_name, s3, "$g_encounter_is_in_village"),
          (str_store_string, s2, "@You have engaged {s1} while they were raiding {s3}."),
        (else_try),
          (eq, "$g_encounter_type", enctype_catched_during_village_raid),
          (str_store_party_name, s3, "$g_encounter_is_in_village"),
          (str_store_string, s2, "@You were caught by {s1} while your forces were raiding {s3}."),
        (else_try),
          (eq, "$g_encounter_type", enctype_player_sally),
          (str_store_party_name, s3, "$g_player_sally_town"),
          (str_store_string, s2, "@You rally your forces and sally against {s1} to defend {s3}."),
        (try_end),
      (try_end),
      (try_begin),
        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, ":num_enemy_regulars_remaining", reg0),
        (assign, ":enemy_finished", 0),
        (try_begin),
          (eq, "$g_battle_result", 1), #battle won
          (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
          (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

          (assign, ":enemy_finished",1),
        (else_try),
          (eq, "$g_engaged_enemy", 1),

          (this_or_next|le, ":num_enemy_regulars_remaining", 0),
          (le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),  #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

          (ge, "$g_friend_fit_for_battle",1),
          (assign, ":enemy_finished",1),
        (try_end),

        (this_or_next|eq, ":enemy_finished",1),
        (eq, "$g_enemy_surrenders",1),
        (assign, "$g_next_menu", -1),
        (jump_to_menu, "mnu_total_victory"),
      (else_try),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":num_our_regulars_remaining", reg0),
        (assign, ":friends_finished",0),
        (try_begin),
          (eq, "$g_battle_result", -1),

          #(eq, ":num_our_regulars_remaining", 0), #battle lost
          (le, ":num_our_regulars_remaining",  "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

          (assign,  ":friends_finished", 1),
        (else_try),
          (eq, "$g_engaged_enemy", 1),
          (ge, "$g_enemy_fit_for_battle",1),
          (le, "$g_friend_fit_for_battle",0),
          (assign,  ":friends_finished",1),
        (try_end),

        (this_or_next|eq,  ":friends_finished",1),
        (eq, "$g_player_surrenders",1),
        (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
        (jump_to_menu, "mnu_total_defeat"),
      (try_end),


      (try_begin),
        (eq, "$g_encountered_party_template", "pt_looters"),
        #(set_background_mesh, "mesh_pic_bandits"),
        (set_background_mesh, "mesh_pic_encounter_looters_new"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
        #(set_background_mesh, "mesh_pic_mountain_bandits"),
        (set_background_mesh, "mesh_pic_encounter_mountain_bandits_new"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
        (set_background_mesh, "mesh_pic_steppe_bandits"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_robber_knights"),
        (set_background_mesh, "mesh_pic_roving_knights"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_desert_bandits"),
        (set_background_mesh, "mesh_pic_desert_bandits"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
        (set_background_mesh, "mesh_pic_tundra_bandits"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_sea_raiders"),
        (set_background_mesh, "mesh_pic_sea_raiders"),
      (else_try),
        (eq, "$g_encountered_party_template", "pt_forest_bandits"),
        (set_background_mesh, "mesh_pic_forest_bandits"),
      (else_try),
          (eq, "$g_encountered_party_template", "pt_deserters"),
          (set_background_mesh, "mesh_pic_deserters"),
        (else_try),
          # (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
          # (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
          # (ge, ":leader_troop", 1),
          # (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
          # (faction_get_slot, ":culture", ":leader_troop_faction",slot_faction_culture),
          ##tom new
          (store_faction_of_party, ":faction", "$g_encountered_party"),
          (is_between, ":faction", kingdoms_begin, kingdoms_end),
          (faction_get_slot, ":culture", ":faction",slot_faction_culture),
          
          #(set_background_mesh, "mesh_pic_horizontol"),
          (try_begin),
            (eq, ":culture", fac_culture_iberian),
            (set_background_mesh, "mesh_pic_encounter_iberians"),
          (else_try),
            (eq, ":culture", fac_culture_italian),
            (set_background_mesh, "mesh_pic_encounter_leuro"),
          (else_try),
            (eq, ":culture", fac_culture_rus),
            (set_background_mesh, "mesh_pic_encounter_rus"),
          (else_try),
            (eq, ":culture", fac_culture_teutonic),
            (set_background_mesh, "mesh_pic_encounter_teutonic"),
          (else_try),
            (eq, ":culture", fac_culture_mongol),
            (set_background_mesh, "mesh_pic_encounter_mongol"),
          (else_try),
            (eq, ":culture", fac_culture_baltic),
            (set_background_mesh, "mesh_pic_encounter_balt"),
          (else_try),
            (eq, ":culture", fac_culture_nordic),
            (set_background_mesh, "mesh_pic_encounter_scand"),
          (else_try),
            (eq, ":culture", fac_culture_welsh),
            (set_background_mesh, "mesh_pic_encounter_welsh"),
          (else_try),
            (eq, ":culture", fac_culture_gaelic),
            (set_background_mesh, "mesh_pic_encounter_irish"),
          (else_try),
            (eq, ":culture", fac_culture_scotish),
            (set_background_mesh, "mesh_pic_encounter_scot"),
          (else_try),
            (eq, ":culture", fac_culture_mamluke),
            (set_background_mesh, "mesh_pic_encounter_mamluk"),
          (else_try),
            (eq, ":culture", fac_culture_andalus),
            (set_background_mesh, "mesh_pic_encounter_andalus"),
          (else_try),
            (eq, ":culture", fac_culture_byzantium),
            (set_background_mesh, "mesh_pic_encounter_byz"),
          (else_try),    
            (eq, ":culture", fac_culture_serbian),
            (set_background_mesh, "mesh_pic_encounter_serbs"),
          (else_try),    
            (eq, ":culture", fac_culture_balkan),
            (set_background_mesh, "mesh_pic_encounter_bulgars"),
          (else_try),    
            (eq, ":culture", fac_culture_marinid),
            (set_background_mesh, "mesh_pic_encounter_marrinid"),
          (else_try),
            #(eq, ":culture", fac_culture_western),
            (set_background_mesh, "mesh_pic_encounter_weuro"),
          (try_end),
        (try_end),
    ],
    [

      ("encounter_attack",
      [
          (eq, "$encountered_party_friendly", 0),
          (neg|troop_is_wounded, "trp_player"),
          # (neq, "$g_battle_preparation_phase", 2),
          # rafi
          (assign, ":water", 0),
          (try_begin),
            (call_script, "script_cf_is_party_on_water", "p_main_party"),
            (assign, ":water", 1),
          (try_end),
          (eq, ":water", 0),
          # rafi
          ],
      "Charge the enemy.",
      [        
        (assign, "$g_battle_result", 0),
        (assign, "$g_engaged_enemy", 1),

        (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
        (try_begin),
          (eq, ":encountered_party_template", "pt_village_farmers"),
          (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
        (try_end),

        (call_script, "script_calculate_renown_value"),
        (call_script, "script_calculate_battle_advantage"),
        (set_battle_advantage, reg0),
        (set_party_battle_mode),
        (try_begin),
          (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
          (assign, "$g_village_raid_evil", 0),
          (set_jump_mission, "mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
        (else_try),
          (eq, "$g_encounter_type", enctype_catched_during_village_raid),
          (assign, "$g_village_raid_evil", 0),
          (set_jump_mission, "mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
        (else_try),
          (eq, "$g_encounter_type", enctype_player_sally),
          (set_jump_mission, "mt_castle_attack_walls_defenders_sally_player"),
          (try_begin),
            (party_slot_eq, "$g_player_sally_town", slot_party_type, spt_town),
            (party_get_slot, ":scene_to_use", "$g_player_sally_town", slot_town_walls),
          (else_try),
            (party_get_slot, ":scene_to_use", "$g_player_sally_town", slot_castle_exterior),
          (try_end),
          (assign, "$g_player_sally_town", -1),
          (assign, "$g_player_sallies", -1),
          (jump_to_scene, ":scene_to_use"),
        (else_try),
          (set_jump_mission, "mt_lead_charge"),
          (call_script, "script_setup_random_scene"),
        (try_end),
        (assign, "$g_next_menu", "mnu_simple_encounter"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
      ]),
      # rafi
      ("encounter_attack",
      [
          (eq, "$encountered_party_friendly", 0),
          (neg|troop_is_wounded, "trp_player"),
          # (neq, "$g_battle_preparation_phase", 2),
          (call_script, "script_cf_is_party_on_water", "p_main_party"),
          ],
      "Close in and board the enemy.",
      [
        (assign, "$g_battle_result", 0),
        (assign, "$g_engaged_enemy", 1),

        (call_script, "script_calculate_renown_value"),
        (call_script, "script_calculate_battle_advantage"),
        (set_battle_advantage, reg0),
        (set_party_battle_mode),
        (set_jump_mission, "mt_ship_battle"),
        (assign, "$g_next_menu", "mnu_simple_encounter"),
        (jump_to_menu, "mnu_battle_debrief"),

        (store_faction_of_party, ":ai_party_faction", "$g_encountered_party"),
        (call_script, "script_raf_aor_faction_to_region", ":ai_party_faction"),
        (assign, ":ai_region", reg0),
        (call_script, "script_raf_aor_faction_to_region", "$players_kingdom"),
        (assign, ":player_region", reg0),

        (assign, ":scene_to_use", "scn_scene_sea"),
        (try_begin),
          (this_or_next | eq, ":ai_region", region_andalusian),
          (this_or_next | eq, ":ai_region", region_mamluk),
          (this_or_next | eq, ":ai_region", region_anatolian),
          (eq, ":ai_region", region_north_african),
          (eq, ":player_region", region_nordic),
          (assign, ":scene_to_use", "scn_scene_sea_player_nord_vs_eastern"),
        (else_try),
          (this_or_next | eq, ":player_region", region_andalusian),
          (this_or_next | eq, ":player_region", region_mamluk),
          (this_or_next | eq, ":player_region", region_anatolian),
          (eq, ":player_region", region_north_african),
          (eq, ":ai_region", region_nordic),
          (assign, ":scene_to_use", "scn_scene_sea_player_eastern_vs_nordic"),
        (else_try),
          (eq, ":ai_region", region_nordic),
          (this_or_next | eq, ":player_region", region_latin),
          (this_or_next | eq, ":player_region", region_unknown),
          (this_or_next | eq, ":player_region", region_eastern),
          (this_or_next | eq, ":player_region", region_balkan),
          (this_or_next | eq, ":player_region", region_baltic),
          (this_or_next | eq, ":player_region", region_european),
          (this_or_next | eq, ":player_region", region_teutonic),
          (this_or_next | eq, ":player_region", region_gaelic),
          (this_or_next | eq, ":player_region", region_scot), #TOM
          (eq, ":player_region", region_crusaders),
          (assign, ":scene_to_use", "scn_scene_sea_player_generic_vs_nordic"),
        (else_try),
          (eq, ":player_region", region_nordic),
          (this_or_next | eq, ":ai_region", region_latin),
          (this_or_next | eq, ":ai_region", region_unknown),
          (this_or_next | eq, ":ai_region", region_eastern),
          (this_or_next | eq, ":ai_region", region_baltic),
          (this_or_next | eq, ":ai_region", region_european),
          (this_or_next | eq, ":ai_region", region_teutonic),
          (this_or_next | eq, ":ai_region", region_gaelic),
          (this_or_next | eq, ":ai_region", region_scot), #TOM
          (eq, ":ai_region", region_crusaders),
          (assign, ":scene_to_use", "scn_scene_sea_player_nord_vs_generic"),
        (else_try),
          (this_or_next | eq, ":ai_region", region_andalusian),
          (this_or_next | eq, ":ai_region", region_mamluk),
          (this_or_next | eq, ":ai_region", region_anatolian),
          (eq, ":ai_region", region_north_african),
          (this_or_next | eq, ":player_region", region_latin),
          (this_or_next | eq, ":player_region", region_unknown),
          (this_or_next | eq, ":player_region", region_eastern),
          (this_or_next | eq, ":player_region", region_baltic),
          (this_or_next | eq, ":player_region", region_european),
          (this_or_next | eq, ":player_region", region_teutonic),
          (this_or_next | eq, ":player_region", region_gaelic),
          (this_or_next | eq, ":player_region", region_scot), #TOM
          (eq, ":player_region", region_crusaders),
          (assign, ":scene_to_use", "scn_scene_sea_player_generic_vs_eastern"),
        (else_try),
          (this_or_next | eq, ":player_region", region_andalusian),
          (this_or_next | eq, ":player_region", region_mamluk),
          (this_or_next | eq, ":player_region", region_anatolian),
          (eq, ":player_region", region_north_african),
          (this_or_next | eq, ":ai_region", region_latin),
          (this_or_next | eq, ":ai_region", region_unknown),
          (this_or_next | eq, ":ai_region", region_eastern),
          (this_or_next | eq, ":ai_region", region_baltic),
          (this_or_next | eq, ":ai_region", region_european),
          (this_or_next | eq, ":ai_region", region_teutonic),
          (this_or_next | eq, ":ai_region", region_gaelic),
          (this_or_next | eq, ":ai_region", region_scot), #TOM
          (eq, ":ai_region", region_crusaders),
          (assign, ":scene_to_use", "scn_scene_sea_player_eastern_vs_generic"),
        (else_try),
          (assign, ":scene_to_use", "scn_scene_sea"),
        (try_end),

        (jump_to_scene, ":scene_to_use"),
        (change_screen_mission),
      ]),
      # end rafi

      ("encounter_order_attack",
      [
        # (neq, "$g_battle_preparation_phase", 2),
        (eq, "$encountered_party_friendly", 0),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg0, 4),
      ],
      "Order your troops to attack without you.",
      [
        (jump_to_menu, "mnu_order_attack_begin"),
        #(simulate_battle,3),
      ]),

      ("encounter_leave",[
          (eq, "$cant_leave_encounter", 0),
          ], "Leave.",[
###NPC companion changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
              (try_end),
###NPC companion changes end
#Troop commentary changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
#                  (encountered_party_is_attacker),
                  (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id,   ":stack_troop", "p_encountered_party_backup", ":stack_no"),
                    (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
                    (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
                    (store_troop_faction, ":victorious_faction", ":stack_troop"),
#                    (store_relation, ":relation_with_stack_troop", ":victorious_faction", "fac_player_faction"),
#                    (lt, ":relation_with_stack_troop", 0),
                    (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
                  (try_end),
              (try_end),
#Troop commentary changes end
              (leave_encounter),(change_screen_return)]),
      ("encounter_retreat",[
         # (neq, "$g_battle_preparation_phase", 2),
         (eq, "$cant_leave_encounter", 1),
         (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
         (assign, ":max_skill", reg0),
         (val_add, ":max_skill", 4),

         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
         (assign, ":enemy_party_strength", reg0),
         (val_div, ":enemy_party_strength", 2),

         (val_div, ":enemy_party_strength", ":max_skill"),
         (val_max, ":enemy_party_strength", 1),

         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (assign, ":player_count", reg0),
         (ge, ":player_count", ":enemy_party_strength"),
         ], "Pull back, leaving some soldiers behind to cover your retreat.",[(jump_to_menu, "mnu_encounter_retreat_confirm"),]),

      ("encounter_surrender",[
         (eq, "$cant_leave_encounter", 1),
          ], "Surrender.",[(assign, "$g_player_surrenders",1)]),
    ]
  ),
   ("encounter_retreat_confirm",0,
    "As the party member with the highest tactics skill, ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives, but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     (val_add, ":max_skill", 4),

     (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
     (assign, ":enemy_party_strength", reg0),
     (val_div, ":enemy_party_strength", 2),

     (store_div, reg4, ":enemy_party_strength", ":max_skill"),
     (val_max, reg4, 1),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     ],
    [
      ("leave_behind",[], "Go on. The sacrifice of these men will save the rest.",
      [
        (assign, ":num_casualties", reg4),
        (try_for_range, ":unused", 0, ":num_casualties"),
          (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
          (assign, ":lost_troop", reg0),
          (store_random_in_range, ":random_no", 0, 100),
          (ge, ":random_no", 30),
          (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
        (try_end),
        (call_script, "script_change_player_party_morale", -20),
        (jump_to_menu, "mnu_encounter_retreat"),
      ]),
      ("dont_leave_behind",[], "No. We leave no one behind.",[(jump_to_menu, "mnu_simple_encounter"),]),
    ]
  ),
   ("encounter_retreat",0,
    "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
    "none",
    [
     ],
    [
      ("continue",[], "Continue...",
      [
        ###Troop commentary changes begin
        (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
        (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id,   ":stack_troop", "p_encountered_party_backup", ":stack_no"),
          (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
          (store_troop_faction, ":victorious_faction", ":stack_troop"),
          (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
        (try_end),
        ###Troop commentary changes end
        (party_ignore_player, "$g_encountered_party", 1),
        (leave_encounter),
        (change_screen_return)
      ]),
    ]
  ),
   ("order_attack_begin",0,
    "Your troops prepare to attack the enemy.",
    "none",
    [],
    [
      ("order_attack_begin",[], "Order the attack to begin.",
      [
        (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
        (try_begin),
          (eq, ":encountered_party_template", "pt_village_farmers"),
          (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
        (try_end),

        (assign, "$g_engaged_enemy", 1),
        (jump_to_menu, "mnu_order_attack_2"),
      ]),
      ("call_back",[], "Call them back.",[(jump_to_menu, "mnu_simple_encounter")]),
    ]
  ),
  
  
  
  (
      "order_attack_2",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
      "none",
      [
      (set_background_mesh, "mesh_pic_charge"),

      (call_script, "script_party_calculate_strength", "p_main_party", 1), #exclude player
      (assign, ":player_party_strength", reg0),

      (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
      (assign, ":enemy_party_strength", reg0),

      (party_collect_attachments_to_party, "p_main_party", "p_collective_ally"),
      (call_script, "script_party_calculate_strength", "p_collective_ally", 1), #exclude player
      (assign, ":total_player_and_followers_strength", reg0),

      (try_begin),
        (le, ":total_player_and_followers_strength", ":enemy_party_strength"),
        (assign, ":minimum_power", ":total_player_and_followers_strength"),
      (else_try),
        (assign, ":minimum_power", ":enemy_party_strength"),
      (try_end),

      (try_begin),
        (le, ":minimum_power", 5),
        (assign, ":division_constant", 1),
      (else_try),
        (le, ":minimum_power", 10),
        (assign, ":division_constant", 2),
      (else_try),
        (le, ":minimum_power", 25),
        (assign, ":division_constant", 3),
      (else_try),
        (le, ":minimum_power", 500),
        (assign, ":division_constant", 40),
      (else_try),
        (le, ":minimum_power", 1000),
        (assign, ":division_constant", 50),
      (else_try),
        (le, ":minimum_power", 2000),
        (assign, ":division_constant", 60),
      (else_try),
        (le, ":minimum_power", 4000),
        (assign, ":division_constant", 70),
      (else_try),
        (le, ":minimum_power", 8000),
        (assign, ":division_constant", 80),
      (else_try),
        (le, ":minimum_power", 16000),
        (assign, ":division_constant", 90),
      (else_try),
        (le, ":minimum_power", 32000),
        (assign, ":division_constant", 100),
      (else_try),
        (le, ":minimum_power", 64000),
        (assign, ":division_constant", 110),
      (else_try),
        (le, ":minimum_power", 128000),
        (assign, ":division_constant", 120),
      (else_try),
        (le, ":minimum_power", 256000),
        (assign, ":division_constant", 130),
      (else_try),
        (le, ":minimum_power", 512000),
        (assign, ":division_constant", 140),
      (else_try),
        (le, ":minimum_power", 1024000),
        (assign, ":division_constant", 150),
      (else_try),
        (assign, ":division_constant", 160),
      (try_end),

      (val_div, ":player_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":player_party_strength", 1), #1.126
      (val_div, ":enemy_party_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":enemy_party_strength", 1), #1.126
      (val_div, ":total_player_and_followers_strength", ":division_constant"), #1.126, ":division_constant" was 5 before
      (val_max, ":total_player_and_followers_strength", 1), #1.126

      (store_mul, "$g_strength_contribution_of_player", ":player_party_strength", 100),
      (val_div, "$g_strength_contribution_of_player", ":total_player_and_followers_strength"),

         (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
         (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
         (str_store_string_reg, s8, s0),

      (try_begin),
        (ge, "$g_ally_party", 0),
        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (str_store_string_reg, s8, s0),
      (try_end),

      (inflict_casualties_to_party_group, "$g_encountered_party", ":total_player_and_followers_strength", "p_temp_casualties"),
											
      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

         (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
         (str_store_string_reg, s9, s0),

         (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),
         (assign, "$no_soldiers_left", 0),
         (try_begin),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":num_our_regulars_remaining", reg0),
        (store_add, ":num_routed_us_plus_one", "$num_routed_us", 1),
        (le, ":num_our_regulars_remaining", ":num_routed_us_plus_one"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            (assign, "$no_soldiers_left", 1),
            (str_store_string, s4, "str_order_attack_failure"),
         (else_try),
        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, ":num_enemy_regulars_remaining", reg0),
        (this_or_next|le, ":num_enemy_regulars_remaining", 0),
        (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            (assign, ":continue", 0),
            (party_get_num_companion_stacks, ":party_num_stacks", "p_collective_enemy"),
            (try_begin),
               (eq, ":party_num_stacks", 0),
               (assign, ":continue", 1),
            (else_try),
               (party_stack_get_troop_id, ":party_leader", "p_collective_enemy", 0),
               (try_begin),
                  (neg|troop_is_hero, ":party_leader"),
                  (assign, ":continue", 1),
               (else_try),
                  (troop_is_wounded, ":party_leader"),
                  (assign, ":continue", 1),
               (try_end),
            (try_end),
            (eq, ":continue", 1),
            (assign, "$g_battle_result", 1),
            (assign, "$no_soldiers_left", 1),
            (str_store_string, s4, "str_order_attack_success"),
         (else_try),
            (str_store_string, s4, "str_order_attack_continue"),
         (try_end),
      ],
    [
      ("order_attack_continue",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to continue the attack.",[
          (jump_to_menu,"mnu_order_attack_2"),
          ]),
      ("order_retreat",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
      ("continue",[(eq, "$no_soldiers_left", 1)],"Continue...",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
    ]
  ),

   ("battle_debrief",mnf_scale_picture|mnf_disable_all_keys,
    "{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}^^Kill count:{s12}",
    "none",
    [
    #TOM
    #### battlesize?
    #### battlesize?
    #### shaders    
    # (set_fixed_point_multiplier, 100),
    # (set_shader_param_float, "@vFresnelMultiplier", shader_float_default),
    #### shaders
    #copy backup to main party
    (try_begin),
      (eq, "$auxilary_player_active", 1),

      ###new method, adjust the main party, by the manualy counted one
      ##adjust the party to pre battle
      (party_get_num_companion_stacks, ":stack_num", "p_temp_casualties_3"),
      (try_for_range, ":stack_no", 0, ":stack_num"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties_3", ":stack_no"),
        (neq, ":stack_troop", "trp_player"), #player does not count
        (neg|troop_is_hero, ":stack_troop"), #heroes either
        (party_count_members_of_type, ":main_troop_count", "p_main_party", ":stack_troop"), #get number of troops from main
        (party_count_members_of_type, ":sub_troop_count", "p_temp_casualties_3", ":stack_troop"), #get number of troops from sub
        (try_begin), 
          (gt, ":sub_troop_count", ":main_troop_count"), #sub party has more members
          (store_sub, ":amount", ":sub_troop_count", ":main_troop_count"), #calculate number of troops to adjust
          (party_add_members, "p_main_party", ":stack_troop", ":amount"), #adjust number of troops in the main party
        (else_try),
          (lt, ":sub_troop_count", ":main_troop_count"), #sub party has less members
          (store_sub, ":amount", ":main_troop_count", ":sub_troop_count"), #calculate number of troops to adjust
          (party_remove_members, "p_main_party", ":stack_troop", ":amount"), #adjust number of troops in the main party
        (try_end),
        #wound the members, only if there are less wounded in the main party
        (party_stack_get_num_wounded, ":num_wounded_sub", "p_temp_casualties_3", ":stack_no"),
        (party_stack_get_num_wounded, ":num_wounded_main", "p_main_party", ":stack_no"),
        (try_begin),
          (gt, ":num_wounded_sub", ":num_wounded_main"), #sub has more wounded
          (store_sub, ":amount", ":num_wounded_sub", ":num_wounded_main"), #calculate number of troops to wound
          (party_wound_members, "p_main_party", ":stack_troop", ":amount"),
        (try_end),
      (try_end),
      
      ##adjust the party based on the casualties sustained on the battlefield
      (party_get_num_companion_stacks, ":num_stacks", "p_player_casualties"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_player_casualties", ":stack_no"),
        (neq, ":stack_troop", "trp_player"), #player does not count
        (neg|troop_is_hero, ":stack_troop"), #heroes either
        (party_stack_get_size, ":stack_size", "p_player_casualties", ":stack_no"),
        (party_stack_get_num_wounded, ":num_wounded", "p_player_casualties", ":stack_no"),
        (val_sub, ":stack_size", ":num_wounded"),
        (party_remove_members, "p_main_party", ":stack_troop", ":stack_size"), 
        (party_wound_members, "p_main_party", ":stack_troop", ":num_wounded"),
      (try_end),
      
      (party_clear, "p_temp_casualties_3"),
      (assign, "$auxilary_player_active", 0),
    (try_end),
    
    #TOM
    # (assign, "$g_battle_preparation_phase", 0),
    # (assign, "$g_battle_preparation", -1),
    
     (try_begin),
       (eq, "$g_battle_result", 1),
       (call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),

       (try_begin),
         (ge, "$g_encountered_party", 0),
         (party_is_active, "$g_encountered_party"),
         (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),
         (eq, ":encountered_party_template", "pt_kingdom_caravan_party"),

         (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
         (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
         (val_add, ":number_of_caravan_raids", 1),
         (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 1, ":number_of_caravan_raids"),

         (try_begin),
           (ge, ":number_of_village_raids", 3),
           (ge, ":number_of_caravan_raids", 3),
           (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
         (try_end),
       (try_end),

       (try_begin),
         (party_get_current_terrain, ":cur_terrain", "p_main_party"),
         (eq, ":cur_terrain", rt_snow),
         (get_achievement_stat, ":number_of_victories_at_snowy_lands", ACHIEVEMENT_BEST_SERVED_COLD, 0),
         (val_add, ":number_of_victories_at_snowy_lands", 1),
         (set_achievement_stat, ACHIEVEMENT_BEST_SERVED_COLD, 0, ":number_of_victories_at_snowy_lands"),

         (try_begin),
           (eq, ":number_of_victories_at_snowy_lands", 10),
           (unlock_achievement, ACHIEVEMENT_BEST_SERVED_COLD),
         (try_end),
       (try_end),

       (try_begin),
         (ge, "$g_enemy_party", 0),
         (party_is_active, "$g_enemy_party"),
         (party_stack_get_troop_id, ":stack_troop", "$g_enemy_party", 0),
         (eq, ":stack_troop", "trp_mountain_bandit"),

         (get_achievement_stat, ":number_of_victories_aganist_mountain_bandits", ACHIEVEMENT_MOUNTAIN_BLADE, 0),
         (val_add, ":number_of_victories_aganist_mountain_bandits", 1),
         (set_achievement_stat, ACHIEVEMENT_MOUNTAIN_BLADE, 0, ":number_of_victories_aganist_mountain_bandits"),

         (try_begin),
           (eq, ":number_of_victories_aganist_mountain_bandits", 10),
           (unlock_achievement, ACHIEVEMENT_MOUNTAIN_BLADE),
         (try_end),
     (try_end),

       (try_begin),
         (is_between, "$g_ally_party", walled_centers_begin, walled_centers_end),
         (unlock_achievement, ACHIEVEMENT_NONE_SHALL_PASS),
       (try_end),

       (try_begin),
         (eq, "$g_joined_battle_to_help", 1),
         (unlock_achievement, ACHIEVEMENT_GOOD_SAMARITAN),
       (try_end),
     (try_end),

     (assign, "$g_joined_battle_to_help", 0),
       (call_script, "script_count_casualties_and_adjust_morale"),#new
     (call_script, "script_encounter_calculate_fit"),

     (call_script, "script_party_count_fit_regulars", "p_main_party"),
     (assign, "$playerparty_postbattle_regulars", reg0),

     (try_begin),
       (eq, "$g_battle_result", 1),
       (eq, "$g_enemy_fit_for_battle", 0),
       (str_store_string, s11, "@You were victorious!"),
#       (play_track, "track_bogus"), #clear current track.
#       (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", -1),
       (ge, "$g_enemy_fit_for_battle",1),
       (this_or_next|le, "$g_friend_fit_for_battle",0),
       (le, "$playerparty_postbattle_regulars", 0),
       (str_store_string, s11, "@Battle was lost. Your forces were utterly crushed."),
       (set_background_mesh, "mesh_pic_defeat"),
     (else_try),
       (eq, "$g_battle_result", -1),
       (str_store_string, s11, "@Your companions carry you away from the fighting."),
       (troop_get_type, ":is_female", "trp_player"),
       (try_begin),
         (eq, ":is_female", 1),
         (set_background_mesh, "mesh_pic_wounded_fem"),
       (else_try),
         (set_background_mesh, "mesh_pic_wounded"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 1),
       (str_store_string, s11, "@You have defeated the enemy."),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 0),
       (str_store_string, s11, "@You have retreated from the fight."),
     (try_end),
#NPC companion changes begin
##check for excessive casualties, more forgiving if battle result is good
     (try_begin),
        (gt, "$playerparty_prebattle_regulars", 9),
        (store_add, ":divisor", 3, "$g_battle_result"),
        (store_div, ":half_of_prebattle_regulars", "$playerparty_prebattle_regulars", ":divisor"),
        (lt, "$playerparty_postbattle_regulars", ":half_of_prebattle_regulars"),
        (call_script, "script_objectionable_action", tmt_egalitarian, "str_excessive_casualties"),
     (try_end),
#NPC companion changes end

     (call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
     (str_store_string_reg, s8, s0),
     (call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
     (str_store_string_reg, s9, s0),
     
     (call_script, "script_print_kill_count_to_s0"),
     (str_store_string_reg, s12, s0),
     
     (str_clear, s10),
     (try_begin),
       (eq, "$any_allies_at_the_last_battle", 1),
       (call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
       (str_store_string, s10, "@^^Ally Casualties:{s0}"),
     (try_end),
     (try_begin),
       (assign,reg20, "$killcount"),
       (assign, "$killcount",0),
     (try_end),
     ],
    [
      ("continue",[], "Continue...",[(jump_to_menu, "$g_next_menu"),]),
    ]
  ),



  (
    "total_victory", 0,
    "You shouldn't be reading this... {s9}",
    "none",
    [
        # We exploit the menu condition system below.
        # The conditions should make sure that always another screen or menu is called.
      
      (assign, ":break", 0),
      (try_begin),
        (eq, "$routed_party_added", 0), #new
        (assign, "$routed_party_added", 1),
         #add new party to map (routed_warriors)
        (call_script, "script_add_routed_party"),
      (try_end),


      (try_begin),
        (check_quest_active, "qst_track_down_bandits"),
        (neg|check_quest_succeeded, "qst_track_down_bandits"),
        (neg|check_quest_failed, "qst_track_down_bandits"),

        (quest_get_slot, ":quest_party", "qst_track_down_bandits", slot_quest_target_party),
        (party_is_active, ":quest_party"),
        (party_get_attached_to, ":quest_party_attached"),
        (this_or_next|eq, ":quest_party", "$g_enemy_party"),
          (eq, ":quest_party_attached", "$g_enemy_party"),
        (call_script, "script_succeed_quest", "qst_track_down_bandits"),
      (try_end),


		(try_begin),
			(gt, "$g_private_battle_with_troop", 0),
			(troop_slot_eq, "$g_private_battle_with_troop", slot_troop_leaded_party, "$g_encountered_party"),
			(assign, "$g_private_battle_with_troop", 0),
			(assign, "$g_disable_condescending_comments", 1),
		(try_end),

		#new - begin
        (party_get_num_companion_stacks, ":num_stacks", "p_collective_enemy"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":i_stack"),
          (is_between, ":stack_troop", lords_begin, lords_end),
          (troop_is_wounded, ":stack_troop"),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", 1),
        (try_end),
        #new - end

        (try_begin),
          # Talk to ally leader
          (eq, "$thanked_by_ally_leader", 0),
          (assign, "$thanked_by_ally_leader", 1),

          (gt, "$g_ally_party", 0),

          #(store_add, ":total_str_without_player", "$g_starting_strength_ally_party", "$g_starting_strength_enemy_party"),

          (store_add, ":total_str_without_player", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
          (val_sub, ":total_str_without_player", "$g_starting_strength_main_party"),

          (store_sub, ":ally_strength_without_player", "$g_starting_strength_friends", "$g_starting_strength_main_party"),

          (store_mul, ":ally_advantage", ":ally_strength_without_player", 100),
          (val_add, ":total_str_without_player", 1),
          (val_div, ":ally_advantage", ":total_str_without_player"),
          #Ally advantage=50  means battle was evenly matched

          (store_sub, ":enemy_advantage", 100, ":ally_advantage"),

          (store_mul, ":faction_reln_boost", ":enemy_advantage", "$g_starting_strength_enemy_party"),
          (val_div, ":faction_reln_boost", 3000),
          (val_min, ":faction_reln_boost", 4),

          (store_mul, "$g_relation_boost", ":enemy_advantage", ":enemy_advantage"),
          (val_div, "$g_relation_boost", 700),
          (val_clamp, "$g_relation_boost", 0, 20),

          (party_get_num_companion_stacks, ":num_ally_stacks", "$g_ally_party"),
          (gt, ":num_ally_stacks", 0),
          (store_faction_of_party, ":ally_faction","$g_ally_party"),
          (call_script, "script_change_player_relation_with_faction", ":ally_faction", ":faction_reln_boost"),
          (party_stack_get_troop_id, ":ally_leader", "$g_ally_party"),
          (party_stack_get_troop_dna, ":ally_leader_dna", "$g_ally_party", 0),
          (try_begin),
            (troop_is_hero, ":ally_leader"),
            (troop_get_slot, ":hero_relation", ":ally_leader", slot_troop_player_relation),
            (assign, ":rel_boost", "$g_relation_boost"),
            (try_begin),
              (lt, ":hero_relation", -5),
              (val_div, ":rel_boost", 3),
            (try_end),
            (call_script,"script_change_player_relation_with_troop", ":ally_leader", ":rel_boost"),
          (try_end),
          
          ############## NEW v2.1 - freelancer lord recognition of battle kills
          (try_begin),
            (eq, "$freelancer_state", 1),
              (get_player_agent_no, ":player"),
              (agent_get_kill_count, ":player_kill_count", ":player"),
              (agent_get_kill_count, ":player_wounded_count", ":player", 1),
              (store_add, ":total_player_inflicted_casualties", ":player_kill_count", ":player_wounded_count"),
              (ge, ":total_player_inflicted_casualties", 5),    
                (assign, "$g_total_player_inflicted_casualties", ":total_player_inflicted_casualties"),
                (assign, "$g_talk_troop", "$enlisted_lord"),
                (assign, "$talk_context", tc_freelancer_talk),
                (call_script, "script_setup_troop_meeting", "$enlisted_lord", -1),
          (else_try),
            (assign, "$talk_context", tc_ally_thanks),
            (call_script, "script_setup_troop_meeting", ":ally_leader", ":ally_leader_dna"),
          (try_end),
          ##############
					
        (else_try),
          # Talk to enemy leaders
		  # (neq, "$freelancer_state", 1), #+freelancer chief #prevents player in party from talking to enemy leaders
          (assign, ":break", 0),

          (party_get_num_companion_stacks, ":num_stacks", "p_total_enemy_casualties"), #p_encountered changed to total_enemy_casualties
          (try_for_range, ":stack_no", "$last_defeated_hero", ":num_stacks"), #May 31 bug note -- this now returns some heroes in victorious party as well as in the other party
            (eq, ":break", 0),
            (party_stack_get_troop_id, ":stack_troop", "p_total_enemy_casualties", ":stack_no"),
            (party_stack_get_troop_dna, ":stack_troop_dna", "p_total_enemy_casualties", ":stack_no"),

            (troop_is_hero, ":stack_troop"),

            (store_troop_faction, ":defeated_faction", ":stack_troop"),
            #steve post 0912 changes begin - removed, this is duplicated elsewhere in game menus
            #(call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":stack_troop", ":defeated_faction"),
            (try_begin),
   			  # (store_relation, ":relation", ":defeated_faction", "fac_player_faction"),
   			  (store_relation, ":relation", ":defeated_faction", "$players_kingdom"),  ########## NEW v3.8
			  (ge, ":relation", 0),
			  (str_store_troop_name, s4, ":stack_troop"),

			  (try_begin),
				(eq, "$cheat_mode", 1),
				(display_message, "@{!}{s4} skipped in p_total_enemy_casualties capture queue because is friendly"),
			  (try_end),
			(else_try),
              (try_begin),
                (party_stack_get_troop_id, ":party_leader", "$g_encountered_party", 0),
                (is_between, ":party_leader", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":party_leader", slot_troop_occupation, slto_kingdom_hero),
                (store_sub, ":kingdom_hero_id", ":party_leader", active_npcs_begin),
                (get_achievement_stat, ":was_he_defeated_player_before", ACHIEVEMENT_BARON_GOT_BACK, ":kingdom_hero_id"),
                (eq, ":was_he_defeated_player_before", 1),
                (unlock_achievement, ACHIEVEMENT_BARON_GOT_BACK),
              (try_end),
              (store_add, "$last_defeated_hero", ":stack_no", 1),  
			  ############### NEW v3.3 - lords can be killed in battle with player
			  (call_script, "script_rand", 0, 100),
              (assign, ":chance", reg0), 
		      ######## NEW v3.8 - fixes dead lords causing script errors
			  # (assign, ":current_slot", 20), 
              # (try_for_range, ":cur_slot", 20, 80),
		        # (troop_set_slot, "trp_temp_troop", ":cur_slot", -1), 
              # (try_end),
              ###########
              (try_begin), ### King
                (faction_slot_eq, ":defeated_faction", slot_faction_leader, ":stack_troop"), 
                (lt, ":chance", "$g_lord_death_chance_battle_king"), 
                  (str_store_troop_name, s1, ":stack_troop"),
                  (str_store_faction_name, s3, ":defeated_faction"),
                  # (str_store_string, s17, "@"),
                  (display_log_message, "@{!}{s1} of {s3} has died from wounds!"), ############### NEW v3.12 - 
                  (jump_to_menu, "mnu_enemy_died_from_wounds"),
                  ############### NEW v3.12 - 
                  (assign, ":party_leader", -1),
                  (try_begin),
                      (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                        (assign, ":party_leader", "trp_player"),
                  (else_try),
                      (party_stack_get_troop_id, ":party_leader", "p_collective_ally", 0),
                          (try_begin),
                              (gt, ":party_leader", -1),
                          (else_try),
                              (assign, ":party_leader", "trp_player"),
                          (try_end),
                  (try_end),
                  ############### 
                  (call_script, "script_kill_lord_battle", ":party_leader", ":stack_troop"),   
                  ########### NEW v3.7 - fixes lords parties not disappearing from the map
                  # (call_script, "script_remove_dead_lord_from_game", ":stack_troop"),   
				  ######## NEW v3.8
			      # (troop_set_slot, "trp_temp_troop", ":current_slot", ":stack_troop"), 
			      # (val_add, ":current_slot", 1), 
                  # (troop_get_slot, ":party", ":stack_troop", slot_troop_leaded_party),
		          # (gt, ":party", 0), 
                     # (remove_party, ":party"),
                  ###########
                  (assign, ":break", 1),
              (else_try),
                (neg|faction_slot_eq, ":defeated_faction", slot_faction_leader, ":stack_troop"), 
                (lt, ":chance", "$g_lord_death_chance_battle"), 
                  (str_store_troop_name, s1, ":stack_troop"),
                  (str_store_faction_name, s3, ":defeated_faction"),
                  (str_store_string, s17, "@{s1} of {s3} has died from wounds!"),
                  (display_log_message, "@{!}{s17}"),
                  (jump_to_menu, "mnu_enemy_died_from_wounds"),
                  ############### NEW v3.12 - 
                  (assign, ":party_leader", -1),
                  (try_begin),
                      (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                        (assign, ":party_leader", "trp_player"),
                  (else_try),
                      (party_stack_get_troop_id, ":party_leader", "p_collective_ally", 0),
                          (try_begin),
                              (gt, ":party_leader", -1),
                          (else_try),
                              (assign, ":party_leader", "trp_player"),
                          (try_end),
                  (try_end),
                  ############### 
                  (call_script, "script_kill_lord_battle", ":party_leader", ":stack_troop"),  
                  ########### NEW v3.7 - fixes lords parties not disappearing from the map
                  # (call_script, "script_remove_dead_lord_from_game", ":stack_troop"),   
				  ######## NEW v3.8
			      # (troop_set_slot, "trp_temp_troop", ":current_slot", ":stack_troop"), 
			      # (val_add, ":current_slot", 1),  
                  # (troop_get_slot, ":party", ":stack_troop", slot_troop_leaded_party),
		          # (gt, ":party", 0), 
                    # (remove_party, ":party"),
                  ###########
                  (assign, ":break", 1),
              (else_try),
                (call_script, "script_remove_troop_from_prison", ":stack_troop"),
                (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
                (call_script, "script_cf_check_hero_can_escape_from_player", ":stack_troop"),
                (str_store_troop_name, s1, ":stack_troop"),
                (str_store_faction_name, s3, ":defeated_faction"),
                (str_store_string, s17, "@{s1} of {s3} managed to escape."),
                (display_log_message, "@{!}{s17}"),
                (jump_to_menu, "mnu_enemy_slipped_away"),
                (assign, ":break", 1),
			  (else_try),
                (store_add, "$last_defeated_hero", ":stack_no", 1),
                (call_script, "script_remove_troop_from_prison", ":stack_troop"),
                (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
                (assign, "$talk_context", tc_hero_defeated),
                (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
                (assign, ":break", 1),
			  (try_end),
			    #############################################
            (try_end),
          (try_end),
          (eq, ":break", 1),
        (else_try),
          # Talk to freed heroes
		  (neq, "$freelancer_state", 1), #+freelancer chief #prevents player in party from talking to freed heroes after battle
          (assign, ":break", 0),
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_collective_enemy"),
          (try_for_range, ":stack_no", "$last_freed_hero", ":num_prisoner_stacks"),
            (eq, ":break", 0),
            (party_prisoner_stack_get_troop_id, ":stack_troop", "p_collective_enemy", ":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (party_prisoner_stack_get_troop_dna, ":stack_troop_dna", "p_collective_enemy", ":stack_no"),
            (store_add, "$last_freed_hero", ":stack_no", 1),
            (assign, "$talk_context", tc_hero_freed),
            (call_script, "script_setup_troop_meeting", ":stack_troop", ":stack_troop_dna"),
            (assign, ":break", 1),
          (try_end),
          (eq, ":break", 1),
        (else_try),
          (eq, "$capture_screen_shown", 0),
          (assign, "$capture_screen_shown", 1),
          (party_clear, "p_temp_party"),
          (assign, "$g_move_heroes", 0),
          #(call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_collective_enemy"),
          #p_total_enemy_casualties deki yarali askerler p_temp_party'e prisoner olarak eklenecek.
          (call_script, "script_party_add_wounded_members_as_prisoners", "p_temp_party", "p_total_enemy_casualties"),
          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),
          (try_begin),
            (call_script, "script_party_calculate_strength", "p_collective_friends_backup",0),
            (assign,":total_initial_strength", reg(0)),
            (gt, ":total_initial_strength", 0),
            #(gt, "$g_ally_party", 0),
            (call_script, "script_party_calculate_strength", "p_main_party_backup",0),
            (assign,":player_party_initial_strength", reg(0)),
            # move ally_party_initial_strength/(player_party_initial_strength + ally_party_initial_strength) prisoners to ally party.
            # First we collect the share of prisoners of the ally party and distribute those among the allies.
            (store_sub, ":ally_party_initial_strength", ":total_initial_strength", ":player_party_initial_strength"),
            #(call_script, "script_party_calculate_strength", "p_ally_party_backup"),
            #(assign,":ally_party_initial_strength", reg(0)),
            #(store_add, ":total_initial_strength", ":player_party_initial_strength", ":ally_party_initial_strength"),
            (store_mul, ":ally_share", ":ally_party_initial_strength", 1000),
            (val_div, ":ally_share", ":total_initial_strength"),
            (assign, "$pin_number", ":ally_share"), #we send this as a parameter to the script.
            (party_clear, "p_temp_party_2"),							
            (call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),
            #TODO: This doesn't handle prisoners if our allies joined battle after us.
            (try_begin),
              (gt, "$g_ally_party", 0),
              (distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
            (try_end),
            #next if there's anything left, we'll open up the party exchange screen and offer them to the player.
          (try_end),
          (party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
          (party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),
          (store_add, ":total_capture_size", ":num_rescued_prisoners", ":num_captured_enemies"),
		  # (neq, "$freelancer_state", 1), #+freelancer - makes it so player can not have prisoners while in commanders party
          (gt, ":total_capture_size", 0),
          (change_screen_exchange_with_party, "p_temp_party"),   
        (else_try),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
          # (try_begin),
            # (gt, "$g_ally_party", 0),
            # (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
          # (else_try),
            # (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
            # (gt, ":num_quick_attachments", 0),
            # (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
            # (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
          # (try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
          ## CC
          # Autoloot: Instead of just displaying the loot screen, we display a loot management menu instead
          (assign, ":num_companions", 0),
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (val_add, ":num_companions", 1),
          (try_end),
          (try_begin),
            (gt, ":num_companions", 0),            
            (assign, "$return_menu", "mnu_total_victory"),
            (jump_to_menu, "mnu_manage_loot_pool"),
          (else_try),
            (change_screen_loot, "trp_temp_troop"),
          (try_end),
          #end Autoloot
          ## CC
        (else_try),
          #finished all
          (try_begin),
            (le, "$g_ally_party", 0),
            (end_current_battle),
          (try_end),
          (call_script, "script_party_give_xp_and_gold", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (try_begin),
            (eq, "$g_enemy_party", 0),
            (display_message,"str_error_string"),
          (try_end),

		  (try_begin),
		    (party_is_active, "$g_ally_party"),
			(call_script, "script_battle_political_consequences", "$g_enemy_party", "$g_ally_party"),
		  (else_try),
			(call_script, "script_battle_political_consequences", "$g_enemy_party", "p_main_party"),
		  (try_end),

          (call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
          (call_script, "script_clear_party_group", "$g_enemy_party"),
          (try_begin),
            (eq, "$g_next_menu", -1),

            #NPC companion changes begin
            (call_script, "script_post_battle_personality_clash_check"),
            #NPC companion changes end

            #Post 0907 changes begin
            (party_stack_get_troop_id, ":enemy_leader", "p_encountered_party_backup",0),
            (try_begin),
              (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
              (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
              (store_troop_faction, ":enemy_leader_faction", ":enemy_leader"),

              (try_begin),
                (eq, "$g_ally_party", 0),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Victory comment. Player was alone"),
                (try_end),
              (else_try),
                (ge, "$g_strength_contribution_of_player", 40),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Ordinary victory comment. The player provided at least 40 percent forces."),
                (try_end),
              (else_try),
                (gt, "$g_starting_strength_enemy_party", 1000),
                (call_script, "script_get_closest_center", "p_main_party"),
                (assign, ":battle_of_where", reg0),
                (call_script, "script_add_log_entry", logent_player_participated_in_major_battle, "trp_player",  ":battle_of_where", -1, ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@{!}Player participation comment. The enemy had at least 1k starting strength."),
                (try_end),
              (else_try),
                (eq, "$cheat_mode", 1),
                (display_message, "@{!}No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
              (try_end),
            (try_end),
            #Post 0907 changes end
            (val_add, "$g_total_victories", 1),
            # (assign, "$g_battle_preparation_phase", 0),
            # (assign, "$g_battle_preparation", -1),            
            (leave_encounter),
            (change_screen_return),
          (else_try),
            (neq, "$freelancer_state", 1),   #+freelancer prevents player's actions from having political consequences when in party
            (try_begin), #my kingdom
              #(change_screen_return),
              (eq, "$g_next_menu", "mnu_castle_taken"),
			  ####### NEW v3.8 - player learns a culture after capturing a fief
              (call_script, "script_ee_player_learn_new_culture", "$g_encountered_party"),
              ##############
              (call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
              (store_current_hours, ":hours"),
			  (faction_set_slot, "$players_kingdom", slot_faction_ai_last_decisive_event, ":hours"),
			  ############## NEW v3.9.1 - 
              (try_begin),
                (eq, "$g_auto_change_captured_fief_culture", 1),
                  (faction_get_slot, ":player_culture", "$players_kingdom", slot_faction_culture),
                  (party_set_slot, "$g_encountered_party", slot_center_culture, ":player_culture"),
              (try_end),
############################
			  ######################## NEW v3.8
              (try_begin), #player took a walled center while he is a vassal of npc kingdom.
                (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
                # rafi - rename Nicae to Roman Empire
                (try_begin),                
                  (eq, "$g_encountered_party", "p_town_26_1"),
                    ########## FIX 
                    (faction_get_slot, ":player_culture", "$players_kingdom", slot_faction_culture),
                    (eq, ":player_culture", "fac_culture_byzantium"),  ######### NEW v2.4
					##########
                      (faction_set_name, "$players_kingdom", "@Roman Empire"),
                      (display_message, "@The Roman Empire has been restored!", 0xff0000),
                      (party_set_slot, "p_town_26_1", slot_spec_mercs2, merc_varangians),
                      (party_set_slot, "p_town_26_1", slot_spec_mercs2_party_template, "pt_company_varangian_1"),
                      (party_set_slot, "p_town_26_1", slot_spec_mercs2_number, 1),
                      ####### NEW
                      (party_set_slot, "p_town_26_1", slot_center_has_quarters_varangian, 1),
                (try_end),
                # rafi																 
                (jump_to_menu, "$g_next_menu"), ###### NEW v3.8
				################################################
              (else_try), #player took a walled center while he is a vassal of rebels.
                (eq, "$players_kingdom", "fac_player_supporters_faction"),
                (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
                (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
                (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
                (change_screen_return),
                (start_map_conversation, ":faction_leader", -1),
              (else_try), #player took a walled center for player's kingdom
                (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				######## NEW v3.3 
                # (neq, "$g_player_cur_role", role_vassal), 
                # (neq, "$g_player_cur_role", role_mercenary_captain), 
                # (neq, "$g_player_cur_role", role_prince), 
				########################
                (assign, "$g_center_taken_by_player_faction", "$g_encountered_party"),
                (assign, "$talk_context", tc_give_center_to_fief),
                (change_screen_return),

                (assign, ":best_troop", "trp_euro_horse_4"),
                (assign, ":maximum_troop_score", 0),

                (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
                (try_for_range, ":stack_no", 0, ":num_stacks"),
                  (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
                  (neq, ":stack_troop", "trp_player"),

                  (party_stack_get_size, ":stack_size", "p_main_party", ":stack_no"),
                  (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack_no"),
                  (troop_get_slot, ":num_routed", "p_main_party", slot_troop_player_routed_agents),

                  (assign, ":continue", 0),

                  (try_begin),
                    (neg|troop_is_hero, ":stack_troop"),
                    (store_add, ":agents_which_cannot_speak", ":num_wounded", ":num_routed"),
                    (gt, ":stack_size", ":agents_which_cannot_speak"),
                    (assign, ":continue", 1),
                  (else_try),
                    (troop_is_hero, ":stack_troop"),
                    (neg|troop_is_wounded, ":stack_troop"),
                    (assign, ":continue", 1),
                  (try_end),

                  (eq, ":continue", 1),

                  (try_begin),
                    (troop_is_hero, ":stack_troop"),
                    (troop_get_slot, ":troop_renown", ":stack_troop", slot_troop_renown),
                    (store_mul, ":troop_score", ":troop_renown", 100),
                    (val_add, ":troop_score", 1000),
                  (else_try),
                    (store_character_level, ":troop_level", ":stack_troop"),
                    (assign, ":troop_score", ":troop_level"),
                  (try_end),

                  (try_begin),
                    (gt, ":troop_score", ":maximum_troop_score"),
                    (assign, ":maximum_troop_score", ":troop_score"),
                    (assign, ":best_troop", ":stack_troop"),
                    (party_stack_get_troop_dna, ":best_troop_dna", "p_main_party", ":stack_no"),
                  (try_end),
                (try_end),

                (start_map_conversation, ":best_troop", ":best_troop_dna"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
		
		######## NEW v3.8 - fixes dead lords causing script errors
        # (val_add, ":current_slot", 1),
        # (try_for_range, ":cur_slot", 20, ":current_slot"),
		  # (troop_get_slot, ":dead_lord", "trp_temp_troop", ":cur_slot"), 
		  # (gt, ":dead_lord", 0), 
		    # (troop_set_slot, "trp_temp_troop", ":cur_slot", -1), 
            # (troop_get_slot, ":party", ":dead_lord", slot_troop_leaded_party),
		    # (gt, ":party", 0), 
              # (remove_party, ":party"),
        # (try_end),
        ###########
      ],

    [
      ("continue",[],"Continue...",[]),
        ]
  ),

   ("enemy_slipped_away",0,
    "{s17}",
    "none",
    [],
    [
      ("continue",[], "Continue...",[(jump_to_menu, "mnu_total_victory")]),
    ]
  ),
  
###################### NEW v3.3
   ("enemy_died_from_wounds",0,
    "{s17}",
    "none",
    [],
    [
      ("continue",[], "Continue...",[(jump_to_menu, "mnu_total_victory")]),
    ]
  ),
######################

   ("total_defeat",0,
    "{!}You shouldn't be reading this...",
    "none",
    [

      (play_track, "track_captured", 1),
       # Free prisoners
      (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_main_party"),
      (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
        (troop_is_hero, ":stack_troop"),
        (call_script, "script_remove_troop_from_prison", ":stack_troop"),
      (try_end),

          (try_begin),
            (party_is_active, "$g_ally_party"),
        (call_script, "script_battle_political_consequences", "$g_ally_party", "$g_enemy_party"),
      (else_try),
        (call_script, "script_battle_political_consequences", "p_main_party", "$g_enemy_party"),
          (try_end),

      (call_script, "script_loot_player_items", "$g_enemy_party"),

      (assign, "$g_move_heroes", 0),
      (party_clear, "p_temp_party"),
#################################### NEW v2.1 - TROOPS LOST (CAPTURED) (Player)
      # (store_faction_of_party, ":faction", "p_main_party"),
      # (faction_get_slot, ":cur_slot_value", ":faction", slot_faction_troops_lost_captured),
      # (faction_get_slot, ":cur_slot_value2", ":faction", slot_faction_troops_lost_wounded),
      # (store_party_size, ":amount", "p_main_party"),
      # (val_add, ":cur_slot_value", ":amount"),
      # (val_add, ":cur_slot_value2", ":amount"),
      # (faction_set_slot, ":faction", slot_faction_troops_lost_captured, ":cur_slot_value"),
      # (faction_set_slot, ":faction", slot_faction_troops_lost_wounded, ":cur_slot_value2"),
########################################################################
      (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
      (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
      (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),

      (assign, "$g_prison_heroes", 1),
      (call_script, "script_party_remove_all_companions", "p_main_party"),
      (assign, "$g_prison_heroes", 0),
      (assign, "$g_move_heroes", 1),
      (call_script, "script_party_remove_all_prisoners", "p_main_party"),

      (val_add, "$g_total_defeats", 1),

      (try_begin),
        (neq, "$g_player_surrenders", 1),
        (store_random_in_range, ":random_no", 0, 100),
        (ge, ":random_no", "$g_player_luck"),
        (jump_to_menu, "mnu_permanent_damage"),
      (else_try),
        (try_begin),
          (eq, "$g_next_menu", -1),
          # (assign, "$g_battle_preparation_phase", 0),
          # (assign, "$g_battle_preparation", -1),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "$g_next_menu"),
        (try_end),
      (try_end),
      (try_begin),
        (gt, "$g_ally_party", 0),
        (call_script, "script_party_wound_all_members", "$g_ally_party"),
#################################### NEW v2.1 - TROOPS LOST (CAPTURED) (Allies)
        # (store_faction_of_party, ":ally_faction", "$g_ally_party"),
        # (faction_get_slot, ":cur_slot_value", ":ally_faction", slot_faction_troops_lost_captured),
        # (faction_get_slot, ":cur_slot_value2", ":ally_faction", slot_faction_troops_lost_wounded),
        # (store_party_size, ":amount", "$g_ally_party"),
        # (val_add, ":cur_slot_value", ":amount"),
        # (val_add, ":cur_slot_value2", ":amount"),
        # (faction_set_slot, ":ally_faction", slot_faction_troops_lost_captured, ":cur_slot_value"),
        # (faction_set_slot, ":ally_faction", slot_faction_troops_lost_wounded, ":cur_slot_value2"),
########################################################################
      (try_end),

#Troop commentary changes begin
      (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id,   ":stack_troop", "p_encountered_party_backup", ":stack_no"),
        (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
        (store_troop_faction, ":victorious_faction", ":stack_troop"),
        (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
      (try_end),
#Troop commentary changes end

      ],
    []
  ),

   ("permanent_damage",mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, ":end_cond", 1),
      (try_for_range, ":unused", 0, ":end_cond"),
        (store_random_in_range, ":random_attribute", 0, 4),
        (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
        (try_begin),
          (gt, ":attr_level", 3),
          (neq, ":random_attribute", ca_charisma),
          (try_begin),
            (eq, ":random_attribute", ca_strength),
            (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
          (else_try),
            (eq, ":random_attribute", ca_agility),
            (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility."),
##          (else_try),
            ###(eq, ":random_attribute", ca_charisma),
            ###(str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
          (else_try),
            ###(eq, ":random_attribute", ca_intelligence),
            (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
          (try_end),
        (else_try),
          (lt, ":end_cond", 200),
          (val_add, ":end_cond", 1),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":end_cond", 200),
        (try_begin),
          (eq, "$g_next_menu", -1),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "$g_next_menu"),
        (try_end),
      (else_try),
        (troop_raise_attribute, "trp_player", ":random_attribute", -1),
      (try_end),
      ],
    [
      ("s0",
       [
         (store_random_in_range, ":random_no", 0, 4),
         (try_begin),
           (eq, ":random_no", 0),
           (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
         (else_try),
           (eq, ":random_no", 1),
           (str_store_string, s0, "@Retirement is starting to sound better and better."),
         (else_try),
           (eq, ":random_no", 2),
           (str_store_string, s0, "@No matter! I will persevere!"),
         (else_try),
           (eq, ":random_no", 3),
           (troop_get_type, ":is_female", "trp_player"),
           (try_begin),
             (eq, ":is_female", 1),
             (str_store_string, s0, "@What did I do to deserve this?"),
           (else_try),
             (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
           (try_end),
         (try_end),
         ],
       "{s0}",
       [
         (try_begin),
           (eq, "$g_next_menu", -1),
           (leave_encounter),
           (change_screen_return),
         (else_try),
           (jump_to_menu, "$g_next_menu"),
         (try_end),
         ]),
      ]
  ),

   ("pre_join",0,
    "You come across a battle between {s2} and {s1}. You decide to...",
    "none",
    [
        (str_store_party_name, 1, "$g_encountered_party"),
        (str_store_party_name, 2, "$g_encountered_party_2"),
      ],
    [
      ("pre_join_help_attackers",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          # (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_relation, ":attacker_relation", ":attacker_faction", "$players_kingdom"), ######### NEW v3.3
          # (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          # (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (assign, reg10, ":attacker_relation"),
          (str_store_string, s4, "@[Relation: {reg10}]"),
          # (ge, ":attacker_relation", 0), #tom was 0
          # (lt, ":defender_relation", 0), #tom was 0
          ],
          "Move in to help the {s2}. {s4}",[
          # "Move in to help the {s2}." ,[
              (select_enemy,0),
              (assign, "$g_enemy_party", "$g_encountered_party"),
              (assign, "$g_ally_party", "$g_encountered_party_2"),
              (jump_to_menu, "mnu_join_battle")]),
      ("pre_join_help_defenders",[
          # (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          # (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          # (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (store_relation, ":defender_relation", ":defender_faction", "$players_kingdom"), ######### NEW v3.3
          (assign, reg11, ":defender_relation"),
          (str_store_string, s5, "@[Relation: {reg11}]"),
          # (ge, ":defender_relation", 0), #tom was 0
          # (lt, ":attacker_relation", 0), #tom was 0
          ],
          "Rush to the aid of the {s1}. {s5}",[
          # "Rush to the aid of the {s1}." ,[
              (select_enemy,1),
              (assign, "$g_enemy_party", "$g_encountered_party_2"),
              (assign, "$g_ally_party", "$g_encountered_party"),
              (jump_to_menu, "mnu_join_battle")]),
      ("pre_join_leave",[], "Don't get involved.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

   ("join_battle",0,
    "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
    "none",
    [
        (str_store_party_name, 1, "$g_enemy_party"),
        (str_store_party_name, 2, "$g_ally_party"),

        (call_script, "script_encounter_calculate_fit"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished",0),
          (try_begin),
            (eq, "$g_battle_result", 1),

            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (le, "$g_enemy_fit_for_battle",0),
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),

          (this_or_next|eq, ":enemy_finished",1),
          (eq, "$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":num_ally_regulars_remaining", reg0),
          (assign, ":battle_lost", 0),
          (try_begin),
            (eq, "$g_battle_result", -1),

            #(eq, ":num_ally_regulars_remaining", 0), #battle lost
            (le, ":num_ally_regulars_remaining",  "$num_routed_allies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":battle_lost",1),
          (try_end),

          (this_or_next|eq, ":battle_lost",1),
          (eq, "$g_player_surrenders",1),
          (leave_encounter),
          (change_screen_return),
        (try_end),
      ],
    [
      ("join_attack",
      [
           (neg|troop_is_wounded, "trp_player"),
           # rafi
           (assign, ":water", 0),
           (try_begin),
             (call_script, "script_cf_is_party_on_water", "p_main_party"),
             (assign, ":water", 1),
           (try_end),
           (eq, ":water", 0),
           # rafi
          ],
      "Charge the enemy.",
      [
        (assign, "$g_joined_battle_to_help", 1),
          (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
          (assign, "$g_battle_result", 0),
          (call_script, "script_calculate_renown_value"),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (set_jump_mission, "mt_lead_charge"),
          (call_script, "script_setup_random_scene"),
          (assign, "$g_next_menu", "mnu_join_battle"),
          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),

  # rafi sea
  ("join_attack",
  [
      (neg|troop_is_wounded, "trp_player"),
      (call_script, "script_cf_is_party_on_water", "p_main_party"),
      ],
  "Board the enemy.",
  [
    (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
    (assign, "$g_battle_result", 0),
    (call_script, "script_calculate_renown_value"),
    (call_script, "script_calculate_battle_advantage"),
    (set_battle_advantage, reg0),
    (set_party_battle_mode),
    (set_jump_mission, "mt_ship_battle"),
    (call_script, "script_setup_random_scene"),
    (assign, "$g_next_menu", "mnu_join_battle"),
    (jump_to_menu, "mnu_battle_debrief"),
    (jump_to_scene, "scn_scene_sea"),
    (change_screen_mission),
    ]),

  ("join_order_attack",
  [
      (neq, "$freelancer_state", 1),    #+freelancer chief
      (call_script, "script_party_count_members_with_full_health", "p_main_party"),
      (ge, reg0, 3),
      ],
  "Order your troops to attack with your allies while you stay back.",
  [
        (assign, "$g_joined_battle_to_help", 1),
    (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                                                                     (jump_to_menu, "mnu_join_order_attack"),
                                                        ]),

  ("join_leave",[], "Leave.",
  [
    # (neq, "$freelancer_state", 1),    #+freelancer
    (try_begin),
       (neg|troop_is_wounded, "trp_player"),
       (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
       (party_stack_get_troop_id, ":enemy_leader", "$g_enemy_party",0),
   (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
       (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
    (try_end),

      (leave_encounter),(change_screen_return)]),
      
  ]),
  
   ("join_order_attack",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
      (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
      (assign, ":player_party_strength", reg0),
      (val_div, ":player_party_strength", 5),
      (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
      (assign, ":friend_party_strength", reg0),
      (val_div, ":friend_party_strength", 5),

      (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
      (assign, ":enemy_party_strength", reg0),
      (val_div, ":enemy_party_strength", 5),

      (try_begin),
        (eq, ":friend_party_strength", 0),
        (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
      (else_try),
        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
      (try_end),

      (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
      (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties_player"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties_player", 0),
      (str_store_string_reg, s8, s0),

      (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties_attacker"),

      #ozan begin
      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties_attacker"),
      (try_for_range, ":stack_no", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties_attacker", ":stack_no"),
        (try_begin),
          (party_stack_get_size, ":stack_size", "p_temp_casualties_attacker", ":stack_no"),
          (gt, ":stack_size", 0),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties_attacker", ":stack_no"),
          (gt, ":stack_wounded_size", 0),
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
        (try_end),
      (try_end),
      #ozan end

      (call_script, "script_print_casualties_to_s0", "p_temp_casualties_attacker", 0),
      (str_store_string_reg, s10, s0),

      (call_script, "script_collect_friendly_parties"),
      #(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

      (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties_defender"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties_defender", 0),
      (str_store_string_reg, s9, s0),
      (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

       #(assign, "$cant_leave_encounter", 0),
       (assign, "$no_soldiers_left", 0),
       (try_begin),
         (call_script, "script_party_count_members_with_full_health", "p_main_party"),
         (assign, ":num_our_regulars_remaining", reg0),

         #(le, ":num_our_regulars_remaining", 0),
         (le, ":num_our_regulars_remaining", "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

         (assign, "$no_soldiers_left", 1),
         (str_store_string, s4, "str_join_order_attack_failure"),
       (else_try),
         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
         (assign, ":num_enemy_regulars_remaining", reg0),

         (this_or_next|le, ":num_enemy_regulars_remaining", 0),
         (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

         (assign, "$g_battle_result", 1),
         (assign, "$no_soldiers_left", 1),
         (str_store_string, s4, "str_join_order_attack_success"),
       (else_try),
         (str_store_string, s4, "str_join_order_attack_continue"),
       (try_end),
    ],
    [
      ("continue",[], "Continue...",
      [
        (jump_to_menu, "mnu_join_battle"),
      ]),
    ]
  ),


# Towns
   ("zendar",mnf_auto_enter,
    "You enter the town of Zendar.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item, "itm_tools",70),(set_price_rate_for_item, "itm_salt",140)],
    [
      ("zendar_enter",[], "_",[(set_jump_mission, "mt_town_default"),(jump_to_scene, "scn_zendar_center"),(change_screen_mission)], "Door to the town center."),
      ("zendar_tavern",[], "_",[(set_jump_mission, "mt_town_default"),
                                                   (jump_to_scene, "scn_the_happy_boar"),
                                                   (change_screen_mission)], "Door to the tavern."),
      ("zendar_merchant",[], "_",[(set_jump_mission, "mt_town_default"),
                                                   (jump_to_scene, "scn_zendar_merchant"),
                                                   (change_screen_mission)], "Door to the merchant."),
      ("zendar_arena",[], "_",[(set_jump_mission, "mt_town_default"),
                                                   (jump_to_scene, "scn_zendar_arena"),
                                                   (change_screen_mission)], "Door to the arena."),
#      ("zendar_leave",[], "Leave town.",[[leave_encounter],[change_screen_return]]),
      ("town_1_leave",[], "_",[(leave_encounter),(change_screen_return)]),
    ]
  ),
   ("salt_mine",mnf_auto_enter,
    "You enter the salt mine.",
    "none",
    [(reset_price_rates,0),(set_price_rate_for_item, "itm_salt",55)],
    [
      ("enter",[], "Enter.",[(set_jump_mission, "mt_town_center"),(jump_to_scene, "scn_salt_mine"),(change_screen_mission)]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
   ("four_ways_inn",mnf_auto_enter,
    "You arrive at the Four Ways Inn.",
    "none",
    [],
    [

#      ("enter",[], "Enter.",[[set_jump_mission, "mt_town_default"],[jump_to_scene, "scn_conversation_scene"],[change_screen_mission]]),
      ("enter",[], "Enter.",[(set_jump_mission, "mt_ai_training"),(jump_to_scene, "scn_four_ways_inn"),(change_screen_mission)]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
   ("test_scene",0,
    "You enter the test scene.",
    "none",
    [],
    [

      ("enter",[], "Enter 1.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_1"],[change_screen_mission]]),
      ("enter",[], "Enter 2.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_2"],[change_screen_mission]]),
      ("enter",[], "Enter 3.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_3"],[change_screen_mission]]),
      ("enter",[], "Enter 4.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_4"],[change_screen_mission]]),
      ("enter",[], "Enter 5.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_5"],[change_screen_mission]]),
      ("enter",[], "Enter 6.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_6"],[change_screen_mission]]),
      ("enter",[], "Enter 7.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_test2"],[change_screen_mission]]),
      ("enter",[], "Enter 8.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_test3"],[change_screen_mission]]),
      ("enter",[], "Enter 9.",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_multi_scene_13"],[change_screen_mission]]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
   ("battlefields",0,
    "{!}Select a field...",
    "none",
    [],
    [

      ("enter_f1",[], "{!}Field 1",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_field_1"],[change_screen_mission]]),
      ("enter_f2",[], "{!}Field 2",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_field_2"],[change_screen_mission]]),
      ("enter_f3",[], "{!}Field 3",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_field_3"],[change_screen_mission]]),
      ("enter_f4",[], "{!}Field 4",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_field_4"],[change_screen_mission]]),
      ("enter_f5",[], "{!}Field 5",[[set_jump_mission, "mt_ai_training"],[jump_to_scene, "scn_field_5"],[change_screen_mission]]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
   ("dhorak_keep",0,
#    "Dhorak Keep, the stronghold of the bandits stands overlooking the barren wilderness.",
    "You enter the Dhorak Keep",
    "none",
    [],
    [
      ("enter",[], "Enter.",[(set_jump_mission, "mt_town_center"),(jump_to_scene, "scn_dhorak_keep"),(change_screen_mission)]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

##  (
##    "center_under_attack_while_resting",0,
##    "{s1} has been besieged by {s2}, and the enemy seems to be preparing for an assault!\
## What will you do?",
##    "none",
##    [
##        (party_get_battle_opponent, ":besieger_party", "$auto_enter_town"),
##        (str_store_party_name, s1, "$auto_enter_town"),
##        (str_store_party_name, s2, ":besieger_party"),
##    ],
##    [
##      ("defend_against_siege", [], "Help the defenders of {s1}!",
##       [
##           (assign, "$g_last_player_do_nothing_against_siege_next_check", 0),
##           (rest_for_hours, 0, 0, 0),
##           (change_screen_return),
##           (start_encounter, "$auto_enter_town"),
##           ]),
##      ("do_not_defend_against_siege",[], "Find a secure place and wait there.",
##       [
##           (change_screen_return),
##           ]),
##    ]
##  ),

   ("join_siege_outside",mnf_scale_picture,
    "{s1} has come under siege by {s2}.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
    ],
    [
      ("approach_besiegers",[(store_faction_of_party, ":faction_no", "$g_encountered_party_2"),
                             # (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (store_relation, ":relation", ":faction_no", "$players_kingdom"), ######## NEW v3.3
                             (ge, ":relation", -5),
							 ######## NEW v2.1 - allow joining siege regardless of relation
                             # (store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             # (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             # (lt, ":relation", 0),
                             ], "Approach the siege camp.",[
          (jump_to_menu, "mnu_besiegers_camp_with_allies"),
                                ]),
      ("pass_through_siege",[(store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             # (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (store_relation, ":relation", ":faction_no", "$players_kingdom"), ######## NEW v3.3
                             (ge, ":relation", -5),
                             ], "Pass through the siege lines and enter {s1}.",
       [
            (jump_to_menu, "mnu_cut_siege_without_fight"),
          ]),
      ("leave",[], "Leave.",[(leave_encounter),
                            (change_screen_return)]),
    ]
  ),
   ("cut_siege_without_fight",0,
    "The besiegers let you approach the gates without challenge.",
    "none",
    [],
    [
      ("continue",[], "Continue...",[(try_begin),
                                   (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                                   (eq, "$g_encountered_party_faction", "$players_kingdom"),
                                   (jump_to_menu, "mnu_town"),
                                 (else_try),
                                   (jump_to_menu, "mnu_castle_outside"),
                                 (try_end)]),
      ]
  ),
   ("besiegers_camp_with_allies",0,
    "{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers, where you and your men are welcomed.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", "$g_encountered_party_2"),
        (select_enemy, 0),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
##          (assign, "$g_next_menu", -1),#"mnu_castle_taken_by_friends"),
##          (jump_to_menu, "mnu_total_victory"),
          (call_script, "script_party_wound_all_members", "$g_enemy_party"),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":ally_num_soldiers", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":ally_num_soldiers", 0), #battle lost (sdsd = TODO : also compare this with routed allies too like in other parts)
          (leave_encounter),
          (change_screen_return),
        (try_end),
        ],
    [
      ("talk_to_siege_commander",[], " Request a meeting with the commander.",[
                                (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
                                (modify_visitors_at_site, ":meeting_scene"),(reset_visitors),
                                (set_visitor, 0, "trp_player"),
                                (party_stack_get_troop_id, ":siege_leader_id", "$g_encountered_party_2",0),
                                (party_stack_get_troop_dna, ":siege_leader_dna", "$g_encountered_party_2",0),
                                (set_visitor, 17, ":siege_leader_id", ":siege_leader_dna"),
                                (set_jump_mission, "mt_conversation_encounter"),
                                (jump_to_scene, ":meeting_scene"),
                                (assign, "$talk_context", tc_siege_commander),
                                (change_screen_map_conversation, ":siege_leader_id")]),
      ("join_siege_with_allies",[(neg|troop_is_wounded, "trp_player")], "Join the next assault.",
       [
           (assign, "$g_joined_battle_to_help", 1),
           (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
		   ################## NEW v2.7 - negative relations with opposite faction 
		   (store_faction_of_party, ":faction_no1", "$g_encountered_party"),
           (store_relation, ":relation", "$players_kingdom", ":faction_no1"),
           (val_sub, ":relation", 10),
           (call_script, "script_set_player_relation_with_faction", ":faction_no1", ":relation"),
		   
		   (store_faction_of_party, ":faction_no2", "$g_encountered_party_2"),
           (store_relation, ":relation", "$players_kingdom", ":faction_no2"),
           (val_add, ":relation", 8),
           (call_script, "script_set_player_relation_with_faction", ":faction_no2", ":relation"),
		   ##################
           (try_begin),
             (check_quest_active, "qst_join_siege_with_army"),
             (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
             (add_xp_as_reward, 250),
             (call_script, "script_end_quest", "qst_join_siege_with_army"),
             #Reactivating follow army quest
             (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
             (str_store_troop_name_link, s9, ":faction_marshall"),
             (setup_quest_text, "qst_follow_army"),
             (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
             (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
             (assign, "$g_player_follow_army_warnings", 0),
           (try_end),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
           (try_end),
           (call_script, "script_calculate_battle_advantage"),
           (val_mul, reg0, 2),
           (val_div, reg0, 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
             (set_jump_mission, "mt_castle_attack_walls_belfry"),
           (else_try),
             (set_jump_mission, "mt_castle_attack_walls_ladder"),
           (try_end),
           (jump_to_scene, ":battle_scene"),
           (assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
           (assign, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
          ]),
      ("join_siege_stay_back", [
                                # (neq, "$freelancer_state", 1),    #+freelancer chief
                                (call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                (ge, reg0, 3),
                                ],
       "Order your soldiers to join the next assault without you.",
       [
         (assign, "$g_joined_battle_to_help", 1),
         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
         (try_begin),
           (check_quest_active, "qst_join_siege_with_army"),
           (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
           (add_xp_as_reward, 100),
           (call_script, "script_end_quest", "qst_join_siege_with_army"),
           #Reactivating follow army quest
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s9, ":faction_marshall"),
           (setup_quest_text, "qst_follow_army"),
           (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
           (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
           (assign, "$g_player_follow_army_warnings", 0),
         (try_end),
         (jump_to_menu, "mnu_castle_attack_walls_with_allies_simulate")]),
      ("leave",[], "Leave.",[(leave_encounter),(change_screen_return)]),

    ]
  ),

   ("castle_outside",mnf_scale_picture,
    "You are outside {s2}.{s11} {s3} {s4}",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, s2, "$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        (assign, "$all_doors_locked",1),
        (assign, "$current_town", "$g_encountered_party"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$entry_to_town_forbidden",0),
          (assign, "$sneaked_into_town",0),
          (assign, "$town_entered", 0),
#          (assign, "$waiting_for_arena_fight_result", 0),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_player_besiege_town", 0),
            (neq, "$g_player_besiege_town", "$g_encountered_party"),
            (party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign, "$g_player_besiege_town",-1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (assign, "$entry_to_town_forbidden",1),
          (try_end),

          ##diplomacy begin
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
            (assign, "$encountered_party_hostile", 1),
            (assign, "$entry_to_town_forbidden",1),
          (try_end),
          ##diplomacy end

          (assign, "$cant_sneak_into_town",0),
          (try_begin),
            (eq, "$current_town", "$last_sneak_attempt_town"),
            (store_current_hours,reg(2)),
            (val_sub,reg(2), "$last_sneak_attempt_time"),
            (lt,reg(2),12),
            (assign, "$cant_sneak_into_town",1),
          (try_end),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (str_clear,s4),
        (try_begin),
          (eq, "$entry_to_town_forbidden",1),
          (try_begin),
            (eq, "$cant_sneak_into_town",1),
            (str_store_string,s4, "str_sneaking_to_town_impossible"),
          (else_try),
            (str_store_string,s4, "str_entrance_to_town_forbidden"),
          (try_end),
        (try_end),

        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8, ":center_lord"),
          (str_store_string,s7, "@{s8} of {s9}"),
        (try_end),

        (try_begin), # same mnu_town
          (party_slot_eq, "$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11, "@ Your own banner flies over the castle gate."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11, "@ You see the banner of {s7} over the castle gate."),
          (else_try),
            (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string,s11, "str__this_castle_is_temporarily_under_royal_control"),
          (else_try),
            (str_store_string,s11, "str__this_castle_does_not_seem_to_be_under_anyones_control"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11, "@ Your own banner flies over the town gates."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11, "@ You see the banner of {s7} over the town gates."),
          (else_try),
            (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string,s11, "str__this_town_is_temporarily_under_royal_control"),
          (else_try),
            (str_store_string,s11, "str__the_townspeople_seem_to_have_declared_their_independence"),
          (try_end),
        (try_end),

        (party_get_num_companions, reg(7), "p_collective_enemy"),
        (assign, "$castle_undefended",0),
        (str_clear, s3),
        (try_begin),
          (eq,reg(7),0),
          (assign, "$castle_undefended",1),
#          (party_set_faction, "$g_encountered_party", "fac_neutral"),
#          (party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),
          (str_store_string, s3, "str_castle_is_abondened"),
        (else_try),
        ##diplomacy begin
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
          (str_store_string, s3, "str_dplmc_place_is_occupied_by_insurgents"),
        (else_try),
        ##diplomacy end
          # (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
          (eq, "$g_encountered_party_faction", "$players_kingdom"), ####### NEW v3.3
          (str_store_string, s3, "str_place_is_occupied_by_player"),
        (else_try),
          (lt, "$g_encountered_party_relation", 0),
          (str_store_string, s3, "str_place_is_occupied_by_enemy"),
        (else_try),
#          (str_store_string, s3, "str_place_is_occupied_by_friendly"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_town_outside",1),
          (assign, "$g_leave_town_outside",0),
          (assign, "$g_permitted_to_center", 0),
          (change_screen_return),
        (else_try),
          (check_quest_active, "qst_escort_lady"),
          (quest_slot_eq, "qst_escort_lady", slot_quest_target_center, "$g_encountered_party"),
          (quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
          (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          (modify_visitors_at_site, ":meeting_scene"),
          (reset_visitors),
          (set_visitor, 0, "trp_player"),
          (set_visitor, 17, ":quest_object_troop"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, ":quest_object_troop"),
        (else_try),
          (check_quest_active, "qst_kidnapped_girl"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
          (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          (modify_visitors_at_site, ":meeting_scene"),
          (reset_visitors),
          (set_visitor, 0, "trp_player"),
          (set_visitor, 17, "trp_kidnapped_girl"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, "trp_kidnapped_girl"),
##        (else_try),
##          (gt, "$lord_requested_to_talk_to", 0),
##          (store_current_hours, ":cur_hours"),
##          (neq, ":cur_hours", "$quest_given_time"),
##          (modify_visitors_at_site, "scn_conversation_scene"),
##          (reset_visitors),
##          (assign, ":cur_lord", "$lord_requested_to_talk_to"),
##          (assign, "$lord_requested_to_talk_to", 0),
##          (set_visitor, 0, "trp_player"),
##          (set_visitor, 17, ":cur_lord"),
##          (set_jump_mission, "mt_conversation_encounter"),
##          (jump_to_scene, "scn_conversation_scene"),
##          (assign, "$talk_context", tc_castle_gate_lord),
##          (change_screen_map_conversation, ":cur_lord"),
        (else_try),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (jump_to_menu, "mnu_town"),
        ##diplomacy begin
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
          (try_begin),
            (eq, "$g_player_besiege_town", "$g_encountered_party"),
            (jump_to_menu, "mnu_castle_besiege"),
          (try_end),
        ##diplomacy end
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
          (this_or_next|party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
          (faction_slot_eq, "$g_encountered_party_faction", slot_faction_leader, "trp_player"),
          (jump_to_menu, "mnu_enter_your_own_castle"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type,spt_castle),
          (ge, "$g_encountered_party_relation", 0),
          (this_or_next|eq, "$castle_undefended", 1),
          (this_or_next|eq, "$g_permitted_to_center", 1),
          (eq, "$g_encountered_party_faction", "$players_kingdom"),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type,spt_town),
          (ge, "$g_encountered_party_relation", 0),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (eq, "$g_player_besiege_town", "$g_encountered_party"),
          (jump_to_menu, "mnu_castle_besiege"),
        (try_end),

          ##diplomacy begin
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
            (set_background_mesh, "mesh_pic_townriot"),
          (else_try),
          ##diplomacy end
        (call_script, "script_set_town_picture"),
              ##diplomacy begin
          (try_end),
          ##diplomacy end
        ],
    [
#        ("talk_to_castle_commander",[
#            (party_get_num_companions, ":no_companions", "$g_encountered_party"),
#            (ge, ":no_companions", 1),
#            (eq, "$ruler_meeting_denied",0), #this variable is removed
#            ],
#         "Request a meeting with the lord of the castle.",[
#             (modify_visitors_at_site, "scn_conversation_scene"),(reset_visitors),
#             (set_visitor, 0, "trp_player"),
#             (party_stack_get_troop_id, reg(6), "$g_encountered_party",0),
#             (party_stack_get_troop_dna,reg(7), "$g_encountered_party",0),
#             (set_visitor, 17,reg(6),reg(7)),
#             (set_jump_mission, "mt_conversation_encounter"),
#             (jump_to_scene, "scn_conversation_scene"),
#             (assign, "$talk_context", tc_castle_commander),
#             (change_screen_map_conversation, reg(6))
#             ]),
      ("approach_gates",[(this_or_next|eq, "$entry_to_town_forbidden",1),
                          (party_slot_eq, "$g_encountered_party", slot_party_type,spt_castle)],
       "Approach the gates and hail the guard.",[
                                                  (jump_to_menu, "mnu_castle_guard"),
##                                                   (modify_visitors_at_site, "scn_conversation_scene"),(reset_visitors),
##                                                   (set_visitor,0, "trp_player"),
##                                                   (store_faction_of_party, ":cur_faction", "$g_encountered_party"),
##                                                   (faction_get_slot, ":cur_guard", ":cur_faction", slot_faction_guard_troop),
##                                                   (set_visitor,17, ":cur_guard"),
##                                                   (set_jump_mission, "mt_conversation_encounter"),
##                                                   (jump_to_scene, "scn_conversation_scene"),
##                                                   (assign, "$talk_context", tc_castle_gate),
##                                                   (change_screen_map_conversation, ":cur_guard")
                                                   ]),

      ("town_sneak",
        [
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_party_type,spt_town),
            (str_store_string, s7, "str_town"),
          (else_try),
            (str_store_string, s7, "str_castle"),
          (try_end),

          (eq, "$entry_to_town_forbidden", 1),
          (eq, "$cant_sneak_into_town", 0)
        ],
       "Disguise yourself and try to sneak into the {s7}",
       [
         (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
         (party_get_num_companions, ":num_men", "p_main_party"),
         (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
         (val_add, ":num_men", ":num_prisoners"),
         (val_mul, ":num_men", 2),
         (val_div, ":num_men", 3),
         (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
         ################# NEW v2.1 - persuasion decreases chances of being caught
         (store_skill_level, ":persuasion_subtraction", "skl_persuasion", "trp_player"),
         (val_mul, ":persuasion_subtraction", 5), ########## less 5% chance per level
         (val_sub, ":get_caught_chance", ":persuasion_subtraction"),
         #################
         (store_random_in_range, ":random_chance", 0, 100),
         (try_begin),
           (this_or_next|ge, ":random_chance", ":get_caught_chance"),
           (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
           (assign, "$g_last_defeated_bandits_town", 0),
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu, "mnu_sneak_into_town_suceeded"),
           (assign, "$g_mt_mode", tcm_disguised),
         (else_try),
           (jump_to_menu, "mnu_sneak_into_town_caught"),
         (try_end)
         ]),
      ##diplomacy begin
      ("dplmc_riot_start_siege",
       [
           (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle", "p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Besiege the {reg6?town:castle} to counter the insurgency.",
       [
         (assign, "$g_player_besiege_town", "$g_encountered_party"),
         (jump_to_menu, "mnu_castle_besiege"),
         ]),
       ("dplmc_riot_negotiate",
       [
           (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle", "p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Begin negotiations.",
       [
          (jump_to_menu, "mnu_dplmc_riot_negotiate"),
        ]),

     ##diplomacy end
      ("castle_start_siege",
       [
          # (neq, "$g_encountered_party", "p_town_21_1"), # rafi
           ##diplomacy begin
           (neg|party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, "trp_peasant_woman"),
           ##diplomacy end
           (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
           # (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
           (store_relation, ":reln", "$g_encountered_party_faction", "$players_kingdom"),  ####### NEW v3.3
           (lt, ":reln", 0),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle", "p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Besiege the {reg6?town:castle}.",
       [
         #(neq, "$g_encountered_party", "p_town_21_1"), # rafi
         (assign, "$g_player_besiege_town", "$g_encountered_party"),
         # (store_relation, ":relation", "fac_player_supporters_faction", "$g_encountered_party_faction"),
         (store_relation, ":relation", "$players_kingdom", "$g_encountered_party_faction"),
         (val_min, ":relation", -40),
         (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
         (call_script, "script_update_all_notes"),
         (jump_to_menu, "mnu_castle_besiege"),
         ]),

      ("cheat_castle_start_siege",
       [
         (eq, "$cheat_mode", 1),
         # (neq, "$g_encountered_party", "p_town_21_1"), # rafi
         (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
         # (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
         (store_relation, ":reln", "$g_encountered_party_faction", "$players_kingdom"),
         (ge, ":reln", 0),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],
       "{!}CHEAT: Besiege the {reg6?town:castle}...",
       [
           (assign, "$g_player_besiege_town", "$g_encountered_party"),
           (jump_to_menu, "mnu_castle_besiege"),
           ]),

      ("castle_cheat_interior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Interior.",[(set_jump_mission, "mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
                                                       (jump_to_scene, ":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_exterior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Exterior.",[
#                                                       (set_jump_mission, "mt_town_default"),
                                                       (set_jump_mission, "mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_castle_exterior),
                                                       (jump_to_scene, ":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq, "$current_town",slot_party_type, spt_town),], "{!}CHEAT! Town Walls.",
       [
         (party_get_slot, ":scene", "$current_town", slot_town_walls),
         (set_jump_mission, "mt_ai_training"),
         (jump_to_scene, ":scene"),
         (change_screen_mission)]),
         
      ("castle_leave",[], "Leave.",[(change_screen_return,0)]),

    ]
  ),
    ("castle_guard",mnf_scale_picture,
    "You approach the gate. The men on the walls watch you closely.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("request_shelter",[(party_slot_eq, "$g_encountered_party",slot_party_type, spt_castle),
                          (ge, "$g_encountered_party_relation", 0)],
       "Request entry to the castle.",
       [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (lt, ":castle_lord", 0),
          (jump_to_menu, "mnu_castle_entry_granted"),
        (else_try),
          (call_script, "script_troop_get_player_relation", ":castle_lord"),
          (assign, ":castle_lord_relation", reg0),
          #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
          (try_begin),
            (gt, ":castle_lord_relation", -15),
            (jump_to_menu, "mnu_castle_entry_granted"),
          (else_try),
            (jump_to_menu, "mnu_castle_entry_denied"),
          (try_end),
        (try_end),
       ]),
      ("request_meeting_commander",[],
       "Request a meeting with someone.",
       [
          (jump_to_menu, "mnu_castle_meeting"),
       ]),
      ("guard_leave",[],
       "Leave.",
       [(change_screen_return,0)]),
    ]
  ),
   ("castle_entry_granted",mnf_scale_picture,
    "After a brief wait, the guards open the gates for you and allow your party inside.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_town")]),
    ]
  ),
   ("castle_entry_denied",mnf_scale_picture,
    "The lord of this castle has forbidden you from coming inside these walls, and the guard sergeant informs you that his men will fire if you attempt to come any closer.",
    "none",
    [
        (call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_castle_guard")]),
    ]
  ),
   ("castle_meeting",mnf_scale_picture,
    "With whom do you want to meet?",
    "none",
    [
        (assign, "$num_castle_meeting_troops", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ## he's alive/active
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_get_troop_attached_party", ":troop_no"),
          (eq, "$g_encountered_party", reg0),
          (troop_set_slot, "trp_temp_array_a", "$num_castle_meeting_troops", ":troop_no"),
          (val_add, "$num_castle_meeting_troops", 1),
        (try_end),
        (call_script, "script_set_town_picture"),
    ],
    [
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 0),(troop_get_slot, ":troop_no", "trp_temp_array_a", 0),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 0),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 1),(troop_get_slot, ":troop_no", "trp_temp_array_a", 1),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 1),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 2),(troop_get_slot, ":troop_no", "trp_temp_array_a", 2),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 2),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 3),(troop_get_slot, ":troop_no", "trp_temp_array_a", 3),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 3),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 4),(troop_get_slot, ":troop_no", "trp_temp_array_a", 4),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 4),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 5),(troop_get_slot, ":troop_no", "trp_temp_array_a", 5),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 5),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 6),(troop_get_slot, ":troop_no", "trp_temp_array_a", 6),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 6),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 7),(troop_get_slot, ":troop_no", "trp_temp_array_a", 7),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 7),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 8),(troop_get_slot, ":troop_no", "trp_temp_array_a", 8),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 8),(jump_to_menu, "mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 9),(troop_get_slot, ":troop_no", "trp_temp_array_a", 9),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 9),(jump_to_menu, "mnu_castle_meeting_selected")]),

      ("forget_it",[],
       "Forget it.",
       [(jump_to_menu, "mnu_castle_guard")]),
    ]
  ),
   ("castle_meeting_selected",0,
    "Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
    "none",
    [(str_store_troop_name, s6, "$castle_meeting_selected_troop")],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_castle_outside"),
        (modify_visitors_at_site, "scn_conversation_scene"),(reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 17, "$castle_meeting_selected_troop"),
        (set_jump_mission, "mt_conversation_encounter"),
        (jump_to_scene, "scn_conversation_scene"),
        (assign, "$talk_context", tc_castle_gate),
        (change_screen_map_conversation, "$castle_meeting_selected_troop"),
        ]),
    ]
  ),


    ("castle_besiege",mnf_scale_picture,
    "You are laying siege to {s1}. {s2} {s3}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, "$g_siege_force_wait", 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
          (party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
          (store_current_hours, ":cur_hours"),
          (party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":cur_hours"),
          (assign, "$g_siege_method", 0),
          (assign, "$g_siege_sallied_out_once", 0),
        (try_end),

        (party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
        (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
        (assign, ":food_consumption", reg0),
        (assign, reg7, ":food_consumption"),
        (assign, reg8, ":town_food_store"),
        (store_div, reg3, ":town_food_store", ":food_consumption"),

        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (assign, reg6, 1),
        (else_try),
          (assign, reg6, 0),
        (try_end),

        (try_begin),
          (gt, reg3, 0),
          (str_store_string, s2, "@The {reg6?town's:castle's} food stores should last for {reg3} more days."),
        (else_try),
          (str_store_string, s2, "@The {reg6?town's:castle's} food stores have run out and the defenders are starving."),
        (try_end),

        (str_store_string, s3, "str_empty_string"),
        (try_begin),
          (ge, "$g_siege_method", 1),
          (store_current_hours, ":cur_hours"),
          (try_begin),
            (lt, ":cur_hours",  "$g_siege_method_finish_hours"),
            (store_sub, reg9, "$g_siege_method_finish_hours", ":cur_hours"),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@You're preparing to attack the walls, the work should finish in {reg9} hours."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@Your forces are building a siege tower. They estimate another {reg9} hours to complete the build."),
            (try_end),
          (else_try),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@You are ready to attack the walls at any time."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@The siege tower is built and ready to make an assault."),
            (try_end),
            ########## NEW v2.1 - music addition
            (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
            ####################################
          (try_end),
        (try_end),

        #Check if enemy leaves the castle to us...
        (try_begin),
          (eq, "$g_castle_left_to_player",1), #we come here after dialog. Empty the castle and send parties away.
          (assign, "$g_castle_left_to_player",0),
          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
          (party_set_faction, "$g_encountered_party", "fac_neutral"), #temporarily erase faction so that it is not the closest town
          (party_get_num_attached_parties, ":num_attached_parties_to_castle", "$g_encountered_party"),
          (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
            (party_get_attached_party_with_rank, ":attached_party", "$g_encountered_party", ":iap"),
            (party_detach, ":attached_party"),
            (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
            (eq, ":attached_party_type", spt_kingdom_hero_party),
            (store_faction_of_party, ":attached_party_faction", ":attached_party"),
            (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
            (try_begin),
              (gt, reg0, 0),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
            (else_try),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, "$g_encountered_party"),
            (try_end),
          (try_end),
          (call_script, "script_party_remove_all_companions", "$g_encountered_party"),
          (change_screen_return),
          (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"), #recalculate so that
          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
          (party_set_faction, "$g_encountered_party", ":castle_faction"),
        (try_end),

        #Check for victory or defeat....
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, 1, "$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),

        (assign, reg11, "$g_enemy_fit_for_battle"),
        (assign, reg10, "$g_friend_fit_for_battle"),


        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),

          (assign, "$g_next_menu", "mnu_castle_taken"),          
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":main_party_fit_regulars", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":main_party_fit_regulars", 0), #all lost (sdsd = TODO : )
          (assign, "$g_next_menu", "mnu_captivity_start_castle_defeat"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),
    ],
    [
      ("siege_request_meeting",[(eq, "$cant_talk_to_enemy", 0)], "Call for a meeting with the castle commander.", [
          (assign, "$cant_talk_to_enemy", 1),
          (assign, "$g_enemy_surrenders",0),
          (assign, "$g_castle_left_to_player",0),
          (assign, "$talk_context", tc_castle_commander),
          (party_get_num_attached_parties, ":num_attached_parties_to_castle", "$g_encountered_party"),
          (try_begin),
            (gt, ":num_attached_parties_to_castle", 0),
            (party_get_attached_party_with_rank, ":leader_attached_party", "$g_encountered_party", 0),
            (call_script, "script_setup_party_meeting", ":leader_attached_party"),
          (else_try),
            (call_script, "script_setup_party_meeting", "$g_encountered_party"),
          (try_end),
           ]),

      ("wait_24_hours",[], "Wait until tomorrow.", [
          (assign, "$auto_besiege_town", "$g_encountered_party"),
          (assign, "$g_siege_force_wait", 1),
          (store_time_of_day, ":cur_time_of_day"),
          (val_add, ":cur_time_of_day", 1),
          (assign, ":time_to_wait", 31),
          (val_sub, ":time_to_wait", ":cur_time_of_day"),
          (val_mod, ":time_to_wait",24),
          (val_add, ":time_to_wait", 1),
          #(rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
          # rafi
          (rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
          # end

          (assign, "$cant_talk_to_enemy", 0),
          (change_screen_return),
          ]),


      ("castle_lead_attack",
       [
         (neg|troop_is_wounded, "trp_player"),
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
         ],
       "Lead your soldiers in an assault.",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
           (try_end),

           (call_script, "script_calculate_renown_value"),
           (call_script, "script_calculate_battle_advantage"),
           (assign, ":battle_advantage", reg0),
           (val_mul, ":battle_advantage", 2),
           (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, ":battle_advantage"),
           (set_party_battle_mode),
           (assign, "$g_siege_battle_state", 1),
           (assign, ":siege_sally", 0),
           (try_begin),
             (le, ":battle_advantage", -4), #we are outnumbered, defenders sally out
             (eq, "$g_siege_sallied_out_once", 0),
             (set_jump_mission, "mt_castle_attack_walls_defenders_sally"),
             (assign, "$g_siege_battle_state", 0),
             (assign, ":siege_sally", 1),
           (else_try),
             (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
             (set_jump_mission, "mt_castle_attack_walls_belfry"),
           (else_try),
             (set_jump_mission, "mt_castle_attack_walls_ladder"),
           (try_end),
           (assign, "$cant_talk_to_enemy", 0),
           (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (assign, "$g_siege_method", 0), #reset siege timer
           (jump_to_scene, ":battle_scene"),
           (try_begin),
             (eq, ":siege_sally", 1),
             (jump_to_menu, "mnu_siege_attack_meets_sally"),
           (else_try),
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
           (try_end),
       ]),
      ("attack_stay_back",
       [
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours",  "$g_siege_method_finish_hours"),
         ],
       "Order your soldiers to attack while you stay back...", [(assign, "$cant_talk_to_enemy", 0),(jump_to_menu, "mnu_castle_attack_walls_simulate")]),

      ("build_ladders",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 0),(eq, "$g_siege_method", 0)],
       "Prepare ladders to attack the walls.", [(jump_to_menu, "mnu_construct_ladders")]),

      ("build_siege_tower",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),(eq, "$g_siege_method", 0)],
       "Build a siege tower.", [(jump_to_menu, "mnu_construct_siege_tower")]),

      ("cheat_castle_lead_attack",[(eq, "$cheat_mode", 1),
                                   (eq, "$g_siege_method", 0)],
       "{!}CHEAT: Instant build equipments.",
       [
         (assign, "$g_siege_method", 1),
         (assign, "$g_siege_method_finish_hours", 0),
         (jump_to_menu, "mnu_castle_besiege"),
       ]),


      ("cheat_conquer_castle",[(eq, "$cheat_mode", 1),
                                   ],
       "{!}CHEAT: Instant conquer castle.",
       [
        (assign, "$g_next_menu", "mnu_castle_taken"),
        (jump_to_menu, "mnu_total_victory"),
       ]),


      ("lift_siege",[], "Abandon the siege.",
       [
         (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
         (assign, "$g_player_besiege_town", -1),
         (change_screen_return)]),
    ]
  ),

   ("siege_attack_meets_sally",mnf_scale_picture,
    "The defenders sally out to meet your assault.",
    "none",
    [
        (set_background_mesh, "mesh_pic_sally_out"),
    ],
    [
      ("continue",[],
       "Continue...",
       [
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
       ]),
    ]
  ),

   ("siege_attack_meets_sally_player",mnf_scale_picture,
    "Your forces sally out to delay the besiegers.",
    "none",
    [
        (set_background_mesh, "mesh_pic_sally_out"),
    ],
    [
      ("continue",[],
       "Continue...",
       [
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
       ]),
    ]
  ),

    ("castle_besiege_inner_battle",mnf_scale_picture,
    "{s1}",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, ":result", "$g_battle_result"),#will be reset at script_encounter_calculate_fit
        (call_script, "script_encounter_calculate_fit"),

# TODO: To use for the future:
            (str_store_string, s1, "@As a last defensive effort, you retreat to the main hall of the keep. You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
            (str_store_string, s1, "@You've been driven away from the walls. Now the attackers are pouring into the streets. IF you can defeat them, you can perhaps turn the tide and save the day."),
        (try_begin),
          (this_or_next|neq, ":result", 1),
          (this_or_next|le, "$g_friend_fit_for_battle", 0),
          (le, "$g_enemy_fit_for_battle", 0),
          (jump_to_menu, "$g_siege_final_menu"),
        (else_try),
          (call_script, "script_encounter_calculate_fit"),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@You've breached the town walls, but the stubborn defenders continue to resist you in the streets! You'll have to deal with them before you can attack the keep at the heart of the town."),
          (else_try),
            (eq, "$g_siege_battle_state", 2),
            (eq, ":result", 1),
            (str_store_string, s1, "@The town centre is yours, but the remaining defenders have retreated to the castle. It must fall before you can complete your victory."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (try_end),
    ],
    [
      ("continue",[],
       "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
             (try_begin),
               (eq, "$g_siege_battle_state", 1),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
               (set_jump_mission, "mt_besiege_inner_battle_town_center"),
             (else_try),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
               (set_jump_mission, "mt_besiege_inner_battle_castle"),
             (try_end),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
             (set_jump_mission, "mt_besiege_inner_battle_castle"),
           (try_end),
##           (call_script, "script_calculate_battle_advantage"),
##           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (jump_to_scene, ":battle_scene"),
           (val_add, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
       ]),
    ]
  ),


   ("construct_ladders",0,
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take {reg4} hours to build enough scaling ladders for the assault.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 14, ":max_skill"),
     # (val_mul, reg4, 2),
     # rafi - (val_div, reg4, 3),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("build_ladders_cont",[],
       "Do it.", [
           (assign, "$g_siege_method", 1),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 14, reg0),
           # (val_mul, ":hours_takes", 2),
           # rafi - (val_div, ":hours_takes", 3),
           (store_add, "$g_siege_method_finish_hours", ":cur_hours", ":hours_takes"),
           (assign, "$auto_besiege_town", "$current_town"),
           #(rest_for_hours_interactive, 96, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           # rafi
           (rest_for_hours_interactive, 96, 3, 1),
           # end
           (change_screen_return),
           ]),
      ("go_back",[],
       "Go back.", [(jump_to_menu, "mnu_castle_besiege")]),
        ],
  ),


   ("construct_siege_tower",0,
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 15, ":max_skill"),
     # (val_mul, reg4, 6),
     (val_mul, reg4, 2),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("build_siege_tower_cont",[],
       "Start building.", [
           (assign, "$g_siege_method", 2),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 15, reg0),
           #(val_mul, ":hours_takes", 6),
           (val_mul, ":hours_takes", 2), # rafi decrease this
           (store_add, "$g_siege_method_finish_hours", ":cur_hours", ":hours_takes"),
           (assign, "$auto_besiege_town", "$current_town"),
           #(rest_for_hours_interactive, 240, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           # rafi
           (rest_for_hours_interactive, 240, 3, 1),
           # end
           (change_screen_return),
           ]),
      ("go_back",[],
       "Go back.", [(jump_to_menu, "mnu_castle_besiege")]),
        ],
  ),

#
# mnu_castle_attack_walls_simulate
   (
    "castle_attack_walls_simulate",mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}",
   "none",
   [
      (try_begin),
          (set_background_mesh, "mesh_pic_siege_attack"),
      (try_end),

        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),

        (call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties_player"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties_player", 0),
      (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties_attacker"),
      (call_script, "script_print_casualties_to_s0", "p_temp_casualties_attacker", 0),
      (str_store_string_reg, s9, s0),

      (assign, "$no_soldiers_left", 0),
      (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_us)
         (assign, "$no_soldiers_left", 1),
         (str_store_string, s4, "str_attack_walls_failure"),
      (else_try),
          (call_script, "script_party_count_members_with_full_health", "$g_encountered_party"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_enemies)
         (assign, "$no_soldiers_left", 1),
         (assign, "$g_battle_result", 1),
         (str_store_string, s4, "str_attack_walls_success"),
      (else_try),
         (str_store_string, s4, "str_attack_walls_continue"),
      (try_end),
   ],
   [
##      ("lead_next_wave",[(eq, "$no_soldiers_left", 0)], "Lead the next wave of attack personally.", [
##           (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
##           (set_party_battle_mode),
##           (set_jump_mission, "mt_castle_attack_walls"),
##           (jump_to_scene, ":battle_scene"),
##           (jump_to_menu, "mnu_castle_outside"),
##           (change_screen_mission),
##       ]),
##      ("continue_attacking",[(eq, "$no_soldiers_left", 0)], "Order your soldiers to keep attacking...", [
##                                    (jump_to_menu, "mnu_castle_attack_walls_3"),
##                                    ]),
##      ("call_soldiers_back",[(eq, "$no_soldiers_left", 0)], "Call your soldiers back.",[(jump_to_menu, "mnu_castle_outside")]),
   ("continue",[], "Continue...",[(jump_to_menu, "mnu_castle_besiege")]),
    ]
  ),
  
  
  
    ("castle_attack_walls_with_allies_simulate",mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (try_begin),
          (set_background_mesh, "mesh_pic_siege_attack"),
        (try_end),

        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),
        (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
        (assign, ":friend_party_strength", reg0),
        (val_div, ":friend_party_strength", 10),

        (val_max, ":friend_party_strength", 1),

        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

##        (assign, reg0, ":player_party_strength"),
##        (assign, reg1, ":friend_party_strength"),
##        (assign, reg2, ":enemy_party_strength"),
##        (assign, reg3, "$g_enemy_party"),
##        (assign, reg4, "$g_ally_party"),
##        (display_message, "@{!}player_str={reg0} friend_str={reg1} enemy_str={reg2}"),
##        (display_message, "@{!}enemy_party={reg3} ally_party={reg4}"),

        (try_begin),
          (eq, ":friend_party_strength", 0),
          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
        (else_try),
          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (try_end),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties_player"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_player", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties_attacker"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_attacker", 0),
        (str_store_string_reg, s10, s0),

        (call_script, "script_collect_friendly_parties"),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties_defender"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_defender", 0),
        (str_store_string_reg, s9, s0),

        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_us)
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (le, reg0, 0), #(sdsd = TODO : compare with num_routed_enemies)
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
     ],
    [
      ("continue",[], "Continue...",[(jump_to_menu, "mnu_besiegers_camp_with_allies")]),
    ]
  ),

   ("castle_taken_by_friends",0,
    "Nothing to see here.",
    "none",
    [
        (party_clear, "$g_encountered_party"),
        (party_stack_get_troop_id, ":leader", "$g_encountered_party_2", 0),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":leader"),
        (store_troop_faction, ":faction_no", ":leader"),
        #Reduce prosperity of the center by 5
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        (try_begin),
            #(assign, ":damage", 20),
            (assign, ":damage", 60), # rafi
            (is_between, "$g_encountered_party", towns_begin, towns_end),
            #(assign, ":damage", 40), 
            (assign, ":damage", 120), #rafi
        (try_end),
        (try_begin),
            (neq, ":faction_no", "$g_encountered_party_faction"),
            (call_script, "script_faction_inflict_war_damage_on_faction", ":faction_no", "$g_encountered_party_faction", ":damage"),
        (try_end),

        (call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_no"),
        (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
##        (call_script, "script_change_troop_renown", "trp_player", 1),
        (change_screen_return),
    ],
    [
    ],
  ),


   ("castle_taken",mnf_disable_all_keys,
    "{s3} has fallen to your troops, and you now have full control of the {reg2?town:castle}.\
{reg1? You may station troops here to defend it against enemies who may try to recapture it. Also, you should select now whether you will hold the {reg2?town:castle} yourself or give it to a faithful vassal...:}",# Only visible when castle is taken without being a vassal of a kingdom.
    "none",
    [
        (party_clear, "$g_encountered_party"),

        (try_begin),
          # (eq, "$players_kingdom", "fac_player_supporters_faction"),
          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),  ######## NEW v3.3
          (party_get_slot, ":new_owner", "$g_encountered_party", slot_town_lord),
          (neq, ":new_owner", "trp_player"),
         
          (try_for_range, ":unused", 0, 4), 
            (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
          (try_end),
        (try_end),

        (call_script, "script_lift_siege", "$g_encountered_party", 0),
        (assign, "$g_player_besiege_town", -1),

        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        #Reduce prosperity of the center by 5
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        # (call_script, "script_change_troop_renown", "trp_player", 5),
        (call_script, "script_change_troop_renown", "trp_player", 30), ##### NEW v2.7
		############## NEW v3.10
        (try_begin),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),  
		    (faction_get_slot, ":faction_liege", "$players_kingdom", slot_faction_leader),
		    (call_script, "script_troop_change_relation_with_troop", ":faction_liege", "trp_player", 5), 
        (try_end),
############################

        #(assign, ":damage", 20),
        (assign, ":damage", 60), # rafi
        (try_begin),
            (is_between, "$g_encountered_party", towns_begin, towns_end),
            #(assign, ":damage", 40),
            (assign, ":damage", 120), # rafi
        (try_end),
        (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", "$g_encountered_party_faction", ":damage"),

        #removed, is it duplicate (useless)? See 20 lines above.
        #(call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),

        (try_begin),
          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          # (neq, "$players_kingdom", "fac_player_supporters_faction"),####### NEW v3.0-KOMKE uncommented to make it as in native Warband
          # (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), ########## NEW v3.8
		  # (eq, "$player_has_homage", 1),
          (this_or_next|eq, "$g_player_cur_role", role_vassal),  
          (eq, "$g_player_cur_role", role_prince),  
          # (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),  ###### NEW v2.9 - fixes option appearing for player to send word to himself####### NEW v3.0-KOMKE commented out
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
          (jump_to_menu, "mnu_castle_taken_2"),
        (else_try),
####### NEW v3.0-KOMKE START-commented out code was giving center to $players_kingdom and should be fac_player_supporters_faction
          # (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
          # (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
          # (str_store_party_name, s3, "$g_encountered_party"),
          # (assign, reg1, 0),
          # (try_begin),
          #   (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          #   (assign, reg1, 1),
          # (try_end),
          # #(party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),
          # (call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),          
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),      ####### NEW v3.3     
          # (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"), ####### NEW v3.3
          (str_store_party_name, s3, "$g_encountered_party"),
          (assign, reg1, 0),
          (try_begin),
            # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"), ######## NEW v3.8
            (assign, reg1, 1),
          (try_end),          
		  ####### NEW v3.8 - moved this here
		  ####### NEW v3.0 - player role
          (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),  
            (neq, "$g_player_cur_role", role_king),  
              (assign, "$g_player_cur_role", role_king),  
          (try_end),
		  ############## 
		  ############################
		  #(party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),		  
####### NEW v3.0-KOMKE END-           
        (try_end),
        (assign, reg2, 0),
        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (assign, reg2, 1),
        (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
         (assign, "$auto_enter_town", "$g_encountered_party"),
         (change_screen_return),
        ]),
    ],
  ),
   ("castle_taken_2",mnf_disable_all_keys,
    "{s3} has fallen to your troops, and you now have full control of the castle. It is time to send word to {s9} about your victory. {s5}",
    "none",
    [
        (str_store_party_name, s3, "$g_encountered_party"),
        (str_clear, s5),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        (str_store_troop_name, s9, ":faction_leader"),
        (try_begin),
          (eq, "$player_has_homage", 0),
          (assign, reg8, 0),
          (try_begin),
            (party_slot_eq, "$g_encountered_party", spt_town),
            (assign, reg8, 1),
          (try_end),
          (str_store_string, s5, "@However, since you are not a sworn {man/follower} of {s9}, there is no chance he would recognize you as the {lord/lady} of this {reg8?town:castle}."),
        (try_end),
    ],
    [
        ("castle_taken_claim",[(eq, "$player_has_homage", 1)],
        "Request that {s3} be awarded to you.",
        [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$g_castle_requested_by_player", "$current_town"),
        (assign, "$g_castle_requested_for_troop", "trp_player"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
        ]),

        ("castle_taken_claim_2",[
        (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
        (is_between, ":spouse", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
        (store_faction_of_troop, ":spouse_faction", ":spouse"),
        (eq, ":spouse_faction", "$players_kingdom"),
        ],
        "Request that {s3} be awarded to your {wife/husband}.",
        [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$g_castle_requested_by_player", "$current_town"),
        (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
        (assign, "$g_castle_requested_for_troop", ":spouse"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
        ]),



      ("castle_taken_no_claim",[], "Ask no rewards.",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
#        (jump_to_menu, "mnu_town"),
        ]),
    ],
  ),

("requested_castle_granted_to_player",mnf_scale_picture,
    "You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage..",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        (str_store_troop_name, s3, ":faction_leader"),
        (str_store_party_name, s2, "$g_center_to_give_to_player"),
        (try_begin),
            (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
            (assign, reg3, 1),
            (try_for_range, ":cur_village", villages_begin, villages_end),
                (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
                (str_store_party_name, s4, ":cur_village"),
            (try_end),
        (else_try),
            (assign, reg3, 0),
        (try_end),
        (troop_get_type, reg4, ":faction_leader"),

   ],
    [
        ("continue",[], "Continue.",
            [
            (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
            (jump_to_menu, "mnu_give_center_to_player_2"),
            ],
        ),
    ]
),



("requested_castle_granted_to_player_husband", mnf_scale_picture,
    "You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to your husband, {s7}.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
        (str_store_troop_name, s3, ":faction_leader"),
        (str_store_party_name, s2, "$g_center_to_give_to_player"),
        (try_begin),
            (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
            (assign, reg3, 1),
            (try_for_range, ":cur_village", villages_begin, villages_end),
                (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
                (str_store_party_name, s4, ":cur_village"),
            (try_end),
        (else_try),
            (assign, reg3, 0),
        (try_end),
        (troop_get_type, reg4, ":faction_leader"),

        (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
        (str_store_troop_name, s11, ":spouse"),
        (str_store_string, s7, "str_to_your_husband_s11"),
    ],
    [
        ("continue",[], "Continue.",
            [
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", ":spouse", 0),
            ],
        ),
    ]
),







("requested_castle_granted_to_another",mnf_scale_picture,
    "You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give you ownership of the castle, but that is a favour which I fear I cannot grant, as you already hold significant estates in my realm. Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.' ",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
     (str_store_troop_name, s5, ":new_owner"),
     # (assign, reg6, 900),
	 ############## NEW v3.9.1 - (base 500 + (5 * renown)) + (liege relations * 20) 
     (assign, reg6, 500),  ### default
     (try_begin),
	   (troop_slot_ge, "trp_player", slot_troop_renown, 1),
	     (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		 # 1000 * 5 = 5000 + 500 = 5500
	     (store_mul, ":value", ":player_renown", 5),
	     (val_add, reg6, ":value"),
     (try_end),
     (try_begin),
       (call_script, "script_troop_get_player_relation", ":faction_leader"),
       (assign, ":relation", reg0),
	   (gt, ":relation", 0),
	     (store_mul, ":value2", ":relation", 20),
	     (val_add, reg6, ":value2"),
     (else_try), ###### negative relation
	   (lt, ":relation", 0),
	     (val_mul, ":relation", -1), ###### turns into positive
	     (store_mul, ":value2", ":relation", 20),
	     (val_sub, reg6, ":value2"),
     (try_end),
############################

     (assign, "$g_castle_requested_by_player", -1),
     (assign, "$g_castle_requested_for_troop", -1),

    ],
    [
      ("accept_decision",[], "Accept the decision.",
       [
	 ############## NEW v3.10
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (assign, reg6, 500),  ### default
     (try_begin),
	   (troop_slot_ge, "trp_player", slot_troop_renown, 1),
	     (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		 # 1000 * 5 = 5000 + 500 = 5500
	     (store_mul, ":value", ":player_renown", 5),
	     (val_add, reg6, ":value"),
     (try_end),
     (try_begin),
       (call_script, "script_troop_get_player_relation", ":faction_leader"),
       (assign, ":relation", reg0),
	   (gt, ":relation", 0),
	     (store_mul, ":value2", ":relation", 20),
	     (val_add, reg6, ":value2"),
     (else_try), ###### negative relation
	   (lt, ":relation", 0),
	     (val_mul, ":relation", -1), ###### turns into positive
	     (store_mul, ":value2", ":relation", 20),
	     (val_sub, reg6, ":value2"),
     (try_end),
############################

       (call_script, "script_troop_add_gold", "trp_player", reg6),
       (change_screen_return),
       ]),

       ("leave_faction",[], "You have been wronged! Renounce your oath to your liege! ",
       [
         (jump_to_menu, "mnu_leave_faction"),
         # (call_script, "script_troop_add_gold", "trp_player", reg6),
        ]),
     ],
  ),


("requested_castle_granted_to_another_female",mnf_scale_picture,
    "You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give ownership of the castle to your husband, but that is a favour which I fear I cannot grant, as he already holds significant estates in my realm. Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.' ",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
     (str_store_troop_name, s5, ":new_owner"),
     # (assign, reg6, 900),
	 ############## NEW v3.9.1 - (base 500 + (5 * renown)) + (liege relations * 20) 
     (assign, reg6, 500),  ### default
     (try_begin),
	   (troop_slot_ge, "trp_player", slot_troop_renown, 1),
	     (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		 # 1000 * 5 = 5000 + 500 = 5500
	     (store_mul, ":value", ":player_renown", 5),
	     (val_add, reg6, ":value"),
     (try_end),
     (try_begin),
       (call_script, "script_troop_get_player_relation", ":faction_leader"),
       (assign, ":relation", reg0),
	   (gt, ":relation", 0),
	     (store_mul, ":value2", ":relation", 20),
	     (val_add, reg6, ":value2"),
     (else_try), ###### negative relation
	   (lt, ":relation", 0),
	     (val_mul, ":relation", -1), ###### turns into positive
	     (store_mul, ":value2", ":relation", 20),
	     (val_sub, reg6, ":value2"),
     (try_end),
############################

     (assign, "$g_castle_requested_by_player", -1),
     (assign, "$g_castle_requested_for_troop", -1),
    ],

    [
        ("accept_decision",[], "Accept the decision.",
        [
        
	 ############## NEW v3.10
     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
     (assign, reg6, 500),  ### default
     (try_begin),
	   (troop_slot_ge, "trp_player", slot_troop_renown, 1),
	     (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
		 # 1000 * 5 = 5000 + 500 = 5500
	     (store_mul, ":value", ":player_renown", 5),
	     (val_add, reg6, ":value"),
     (try_end),
     (try_begin),
       (call_script, "script_troop_get_player_relation", ":faction_leader"),
       (assign, ":relation", reg0),
	   (gt, ":relation", 0),
	     (store_mul, ":value2", ":relation", 20),
	     (val_add, reg6, ":value2"),
     (else_try), ###### negative relation
	   (lt, ":relation", 0),
	     (val_mul, ":relation", -1), ###### turns into positive
	     (store_mul, ":value2", ":relation", 20),
	     (val_sub, reg6, ":value2"),
     (try_end),
############################
        (call_script, "script_troop_add_gold", "trp_player", reg6),
        (change_screen_return),
        ]),
    ],
),




   ("leave_faction",0,
    "Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings. However, if you return them of your own free will, he may let the betrayal go without a fight.",
    "none",
    [
    ],
    [
      ("leave_faction_give_back", [], "Renounce your oath and give up your holdings.",
       [
#Troop commentary changes begin
#        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
#Troop commentary changes end
        (call_script, "script_player_leave_faction", 1), #1 means give back fiefs
        (change_screen_return),
        ]),
      ("leave_faction_hold", [
          (str_store_party_name, s2, "$g_center_to_give_to_player"),
          ], "Renounce your oath and rule your lands, including {s2}, in your own name.",
       [
        (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0), #this should activate the player faction (it does not)
        (call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
        (call_script, "script_activate_player_faction", "trp_player"), #Activating player faction should now work
        (change_screen_return),
        ]),
      ("leave_faction_cancel", [], "Remain loyal and accept the decision.",
       [
        (change_screen_return),
        ]),
    ],
  ),

   ("give_center_to_player",mnf_scale_picture,
    "Your lord offers to extend your fiefs! {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service, adding it to your holdings. What is your answer?",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (store_faction_of_party, ":center_faction", "$g_center_to_give_to_player"),
     (faction_get_slot, ":faction_leader", ":center_faction", slot_faction_leader),
     (str_store_troop_name, s1, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
    ],
    [
      ("give_center_to_player_accept",[], "Accept the offer.",
       [(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
      ("give_center_to_player_reject",[], "Reject. You have no interest in holding {s2}.",
       [(party_set_slot, "$g_center_to_give_to_player", slot_town_lord, stl_rejected_by_player),
        (change_screen_return),
        ]),
    ],
  ),

   ("give_center_to_player_2",0,
    "With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound village {s4}:}. {reg3?They:It} will make a fine part of your fiefdom. You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace, and manage the lands as you see fit. However, you are also expected to defend your fief and your people from harm, as well as maintaining the rule of law and order.",
    "none",
    [
      (str_store_party_name, s2, "$g_center_to_give_to_player"),
      (assign, reg3, 0),
      (try_begin),
        (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
          (str_store_party_name, s4, ":cur_village"),
          (assign, reg3, 1),
        (try_end),
      (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
    ],
  ),


   ("oath_fulfilled",0,
    "You had a contract with {s1} to serve him for a certain duration. Your contract has now expired. What will you do?",
    "none",
    [
      (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
      (str_store_troop_name, s1, ":faction_leader"),
     ],
    [
      ("renew_oath",[(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
                     (str_store_troop_name, s1, ":faction_leader")], "Renew your contract with {s1} for another month.",
       [
         (store_current_day, ":cur_day"),
         (store_add, "$mercenary_service_next_renew_day", ":cur_day", 14),####### NEW v2.9-KOMKE changed from 30 to 14 like in dialogs
         (change_screen_return),
         ]),
      ("dont_renew_oath",[], "Become free of your bond.",
       [
         (call_script, "script_player_leave_faction", 1), #1 means give back fiefs
         (assign, "$g_player_cur_role", role_adventurer),  ####### NEW v3.0 - player role
         (change_screen_return),
         ]),
    ]
  ),


##  (
##    "castle_garrison_stationed",0,
###    "The rest of the castle garrison recognizes that their situation is hopeless and surrenders. {s1} is at your mercy now. What do you want to do with this castle?",
##    "_",
##    "none",
##    [
##        (jump_to_menu, "mnu_town"),
##    ],
##    [],
##  ),

##  (
##    "castle_choose_captain",0,
##    "You will need to assign one of your companions as the castellan. Who will it be?",
##    "none",
##    [
##        (try_for_range, ":slot_no", 0, 20),
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (assign, ":num_captains", 0),
##        (party_clear, "p_temp_party"),
##        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
##        (try_for_range, ":i_s", 1, ":num_stacks"),
##          (party_stack_get_troop_id, ":companion", "p_main_party", ":i_s"),
##          (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
##          (troop_set_slot, "trp_temp_troop", ":num_captains", ":companion"),
##        (try_end),
##    ],
##    [
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 0),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 0),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 1),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 1),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 2),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 2),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 3),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 3),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 4),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 4),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 5),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 5),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 6),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 6),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 7),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 7),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 8),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 8),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 9),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 9),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 10),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 10),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 11),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 11),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 12),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 12),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 13),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 13),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 14),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 14),(jump_to_menu, "mnu_castle_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 15),(gt, ":captain",0),(str_store_troop_name, s5, ":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 15),(jump_to_menu, "mnu_castle_captain_chosen")]),
##
##      ("cancel",[],
##         "Cancel...",
##         [(jump_to_menu, "mnu_town")]),
##    ],
##  ),
##  (
##    "castle_captain_chosen",0,
##    "h this castle?",
##    "none",
##    [
##        (party_add_leader, "$g_encountered_party",  "$selected_castellan"),
##        (party_remove_members, "p_main_party", "$selected_castellan",1),
##        (party_set_slot, "$g_encountered_party", slot_town_lord, "trp_player"),
##        (party_set_faction, "$g_encountered_party", "fac_player_supporters_faction"),
##        (try_for_range, ":slot_no", 0, 20), #clear temp troop slots just in case
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (jump_to_menu, "mnu_town"),
##        (change_screen_exchange_members,0),
##    ],
##    [],
##  ),

##  (
##    "under_siege_attacked_continue",0,
##    "Nothing to see here.",
##    "none",
##    [
##        (assign, "$g_enemy_party", "$g_encountered_party_2"),
##        (assign, "$g_ally_party", "$g_encountered_party"),
##        (party_set_next_battle_simulation_time, "$g_encountered_party", 0),
##        (call_script, "script_encounter_calculate_fit"),
##        (try_begin),
##          (call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
##          (assign, ":num_enemy_regulars_remaining", reg(0)),
##          (assign, ":enemy_finished",0),
##          (try_begin),
            ###(eq, "$g_battle_result", 1),
            ###(eq, ":num_enemy_regulars_remaining", 0), #battle won
            ###(assign, ":enemy_finished",1),
##          (else_try),
            ###(eq, "$g_engaged_enemy", 1),
            ###(le, "$g_enemy_fit_for_battle",0),
            ###(ge, "$g_friend_fit_for_battle",1),
            ###(assign, ":enemy_finished",1),
##          (try_end),
##          (this_or_next|eq, ":enemy_finished",1),
##          (eq, "$g_enemy_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", -1),
##          (jump_to_menu, "mnu_total_victory"),
##        (else_try),
##          (assign, ":battle_lost", 0),
##          (try_begin),
            ###(eq, "$g_battle_result", -1),
            ###(assign, ":battle_lost",1),
##          (try_end),
##          (this_or_next|eq, ":battle_lost",1),
##          (eq, "$g_player_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
##          (jump_to_menu, "mnu_total_defeat"),
##        (else_try),
##    # Ordinary victory.
##          (try_begin),
##          #check whether enemy retreats
            ###(eq, "$g_battle_result", 1),
            ###(store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
            ###(lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
            ###(party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
##
            ###(try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
##              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
##              (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
##              (gt, ":party_no", 0),
##              (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
##              (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
##              (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            ###(try_end),
            ###(display_message, "@{!}TODO: Enemy retreated. The assault has ended, siege continues."),
            ###(change_screen_return),
##          (try_end),
####          (assign, "$g_center_under_siege_battle", 0),
##        (try_end),
##        ],
##    [
##    ]
##  ),


   ("siege_started_defender",0,
    "{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to...",
    "none",
    [
        (select_enemy,1),
        (assign, "$g_enemy_party", "$g_encountered_party_2"),
        (assign, "$g_ally_party", "$g_encountered_party"),
        (str_store_party_name, 1, "$g_enemy_party"),
        (str_store_party_name, 2, "$g_ally_party"),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$g_siege_first_encounter", 1),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_siege_first_encounter", 0),
          (try_begin),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (assign, ":num_enemy_regulars_remaining", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
            (assign, ":num_ally_regulars_remaining", reg0),
            (assign, ":enemy_finished", 0),
            (try_begin),
              (eq, "$g_battle_result", 1),
              (eq, ":num_enemy_regulars_remaining", 0), #battle won (sdsd = TODO : compare with num_routed_us)
              (assign, ":enemy_finished",1),
            (else_try),
              (eq, "$g_engaged_enemy", 1),
              (le, "$g_enemy_fit_for_battle",0),
              (ge, "$g_friend_fit_for_battle",1),
              (assign, ":enemy_finished",1),
            (try_end),
            (this_or_next|eq, ":enemy_finished",1),
            (eq, "$g_enemy_surrenders",1),
            (assign, "$g_next_menu", -1),
            (jump_to_menu, "mnu_total_victory"),
          (else_try),
            (assign, ":battle_lost", 0),
            (try_begin),
              (this_or_next|eq, "$g_battle_result", -1),
              (troop_is_wounded,  "trp_player"),
              (eq, ":num_ally_regulars_remaining", 0), #(sdsd = TODO : compare with num_routed_allies)
              (assign, ":battle_lost",1),
            (try_end),
            (this_or_next|eq, ":battle_lost",1),
            (eq, "$g_player_surrenders",1),
            (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
            (jump_to_menu, "mnu_total_defeat"),
          (else_try),
            # Ordinary victory/defeat.
            (assign, ":attackers_retreat", 0),
            (try_begin),
            #check whether enemy retreats
              (eq, "$g_battle_result", 1),
              ###(store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
              ###(lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (eq, "$g_battle_result", 0),
              (store_div, ":min_enemy_str", "$g_enemy_fit_for_battle", 3),
              (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (store_random_in_range, ":random_no", 0, 100),
              (store_mul, ":num_ally_regulars_remaining_multiplied", ":num_ally_regulars_remaining", 13),
              (val_div, ":num_ally_regulars_remaining_multiplied", 10),
              (ge, ":num_ally_regulars_remaining_multiplied", ":num_enemy_regulars_remaining"),
              (lt, ":random_no", 10),
              (neq, "$new_encounter", 1),
              (assign, ":attackers_retreat", 1),
            (try_end),
            (try_begin),
              (eq, ":attackers_retreat", 1),
              (party_get_slot, ":siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
              (val_add, ":siege_hardness", 100),
              (party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":siege_hardness"),
              (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),

              (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ## he's alive/active
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
                (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (gt, ":party_no", 0),
                (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
                (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
                (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, "$g_encountered_party"),
              (try_end),
              (display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues.", 0x93C47D),
              (assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
              (leave_encounter),
              (change_screen_return),
              (assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
            (try_end),
          (try_end),
        (try_end),
        (assign, "$g_siege_first_encounter", 0),
        (assign, "$new_encounter", 0),
        ],
    [
     ##diplomacy begin
      ("dplmc_negotiate_with_besieger",
      [
        # (neq, "$freelancer_state", 1),    #+freelancer chief
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (party_slot_ge, "$current_town", slot_center_is_besieged_by, 1),
      ]
       , "Negotiate with the besieger.",
       [
        (jump_to_menu, "mnu_dplmc_negotiate_besieger"),
        ]),
     ##diplomacy end
      ("siege_defender_join_battle",
       [
         (neg|troop_is_wounded, "trp_player"),
         ],
          "Join the battle.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (assign, "$g_battle_result", 0),
		      ################## NEW v2.7 - negative relations with opposite faction 
		      (store_faction_of_party, ":faction_no1", "$g_encountered_party"),
              (store_relation, ":relation", "$players_kingdom", ":faction_no1"),
              (val_add, ":relation", 8),
              (call_script, "script_set_player_relation_with_faction", ":faction_no1", ":relation"),
		      
		      (store_faction_of_party, ":faction_no2", "$g_encountered_party_2"),
              (store_relation, ":relation", "$players_kingdom", ":faction_no2"),
              (val_sub, ":relation", 10),
              (call_script, "script_set_player_relation_with_faction", ":faction_no2", ":relation"),
		      ##################
              (try_begin),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
              (else_try),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
              (try_end),
              (call_script, "script_calculate_battle_advantage"),
              (val_mul, reg0, 2),
              (val_div, reg0, 3), #scale down the advantage a bit.
              (set_battle_advantage, reg0),
              (set_party_battle_mode),
              (try_begin),
                (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
                (set_jump_mission, "mt_castle_attack_walls_belfry"),
              (else_try),
                (set_jump_mission, "mt_castle_attack_walls_ladder"),
              (try_end),
              (jump_to_scene, ":battle_scene"),
              (assign, "$g_next_menu", "mnu_siege_started_defender"),
              (jump_to_menu, "mnu_battle_debrief"),
              (change_screen_mission)]),
      ("siege_defender_troops_join_battle",[
                                            # (neq, "$freelancer_state", 1),    #+freelancer chief
                                            (call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                            (this_or_next|troop_is_wounded,  "trp_player"),
                                            (ge, reg0, 3)],
          "Order your men to join the battle without you.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (select_enemy,1),
              (assign, "$g_enemy_party", "$g_encountered_party_2"),
              (assign, "$g_ally_party", "$g_encountered_party"),
              (assign, "$g_siege_join", 1),
              (jump_to_menu, "mnu_siege_join_defense")]),
              
    ]
  ),

   ("siege_join_defense",mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (try_begin),
          (eq, "$g_siege_join", 1),
          (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
          (assign, ":player_party_strength", reg0),
          (val_div, ":player_party_strength", 5),
        (else_try),
          (assign, ":player_party_strength", 0),
        (try_end),

        (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
        (assign, ":ally_party_strength", reg0),
        (val_div, ":ally_party_strength", 5),
        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 10),

        (store_add, ":friend_party_strength", ":player_party_strength", ":ally_party_strength"),
        (try_begin),
          (eq, ":friend_party_strength", 0),
          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
        (else_try),
          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (try_end),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties_player"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_player", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties_attacker"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_attacker", 0),
        (str_store_string_reg, s9, s0),
        (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties_defender"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties_defender", 0),
        (str_store_string_reg, s10, s0),
        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0),
          (str_store_string, s4, "str_siege_defender_order_attack_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (le, reg0, 0),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_siege_defender_order_attack_success"),
        (else_try),
          (str_store_string, s4, "str_siege_defender_order_attack_continue"),
        (try_end),
    ],
    [
      ("continue",[], "Continue...",[
          (jump_to_menu, "mnu_siege_started_defender"),
          ]),
    ]
  ),

   ("enter_your_own_castle",0,
    "{s10}",
    "none",
    [
      (try_begin),
        (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        # (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader), ######## NEW v3.3
        (eq, ":faction_leader", "trp_player"),
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {king/queen}."),
      (else_try),
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {lord/lady}."),
      (try_end),

      (str_store_party_name, s2, "$current_town"),
    ],
    [
      ("continue",[], "Continue...",
       [ (jump_to_menu, "mnu_town"),
        ]),
    ],
  ),

   ("village",mnf_enable_hot_keys,
    "{s10} {s12}^{s11}^{s6}{s7}",
    "none",
    [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        (try_begin),
          (gt, "$auto_enter_menu_in_center", 0),
          (jump_to_menu, "$auto_enter_menu_in_center"),
          (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        (try_begin),
          (neq, "$g_player_raiding_village",  "$current_town"),
          (assign, "$g_player_raiding_village", 0),
        (else_try),
          (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),

        (try_begin),#Fix for collecting taxes
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8, ":center_lord"),
          (str_store_string,s7, "@{s8} of {s9}"),
        (try_end),

        (str_clear, s10),
        (str_clear, s12),

        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s60, s2),

          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg4, ":prosperity",),
            (display_message, "@{!}Prosperity: {reg4}"),
          (try_end),

          #(val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
          (val_min, ":str_id", 9),
          (val_add, ":str_id", "str_village_prosperity_0"),
          (str_store_string, s10, ":str_id"),


          (store_div, ":str_id", ":prosperity", 20),
          (val_min, ":str_id", 4),
      # rafi
      (store_faction_of_party, ":cur_faction", "$current_town"),
      (call_script, "script_raf_aor_faction_to_region", ":cur_faction"),
      # end rafi
          (try_begin),
        (this_or_next | eq, reg0, region_andalusian),
        (this_or_next | eq, reg0, region_north_african),
        (eq, reg0, region_mamluk),
        (val_add, ":str_id", "str_oasis_village_alt_prosperity_0"),
          (else_try),
            (val_add, ":str_id", "str_village_alt_prosperity_0"),
          (try_end),

          (str_store_string, s12, ":str_id"),
        (try_end),

        (str_clear, s11),
        (try_begin),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (else_try),
          (eq, ":center_lord", "trp_player"),
          (str_store_string,s11, "@ This village and the surrounding lands belong to you."),
        (else_try),
          (ge, ":center_lord", 0),
          (str_store_string,s11, "@ You remember that this village and the surrounding lands belong to {s7}."),
        (else_try),
          (str_store_string,s11, "@ These lands belong to no one."),
        (try_end),

        (str_clear, s7),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s7, "@{!} {s3} ({reg9})."), ### The number inside the parentheses relates to the text string, and it also looks tidier with the period outside the parentheses. - Khanor
        (try_end),
        (str_clear, s6),
        (try_begin),
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
          (store_character_level, ":player_level", "trp_player"),
          (store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":player_level", 10),
          (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 12),
          (val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 10),
          (store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", 25, 30),
          (assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_string, s6, "@ The village is infested by {reg8} {s35}."),

          (assign, "$g_enemy_party", -1), #new, no known enemy party while saving village from bandits dfdf
          (assign, "$g_ally_party", -1), #new, no known enemy party while saving village from bandits dfdf

          (try_begin),
            (eq, ":bandit_troop", "trp_forest_bandit"),
            (set_background_mesh, "mesh_pic_forest_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_steppe_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_taiga_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_mountain_bandit"),
            (set_background_mesh, "mesh_pic_mountain_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_sea_raider"),
            (set_background_mesh, "mesh_pic_sea_raiders"),
          (else_try),
           ##diplmacy begin
            (eq, ":bandit_troop", "trp_peasant_woman"),
            (str_store_string, s6, "@ The peasants hired mercenaries and are rebelling against you."),
            (set_background_mesh, "mesh_pic_villageriot"),
          (else_try),
           ##diplomacy end
            (set_background_mesh, "mesh_pic_bandits"),
          (try_end),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s6, "@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses."),
          (try_begin),
            (neq, "$g_player_raid_complete", 1),
            (play_track, "track_empty_village", 1),
          (try_end),
          (set_background_mesh, "mesh_pic_looted_village"),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
          (str_store_string, s6, "@ The village is being raided."),
        (else_try),
        ##TOM OLD SCENE THINGs
          # (party_get_current_terrain, ":cur_terrain", "$current_town"),
          # (try_begin),
            # (this_or_next|eq, ":cur_terrain", rt_steppe),
            # (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
            # (this_or_next|eq, ":cur_terrain", rt_desert),
            # (             eq, ":cur_terrain", rt_desert_forest),
            # (set_background_mesh, "mesh_pic_village_s"),
          # (else_try),
            # (this_or_next|eq, ":cur_terrain", rt_snow),
            # (             eq, ":cur_terrain", rt_snow_forest),
            # (set_background_mesh, "mesh_pic_village_w"),
          # (else_try),
            # (set_background_mesh, "mesh_pic_village_p"),
          # (try_end),
          #NEW!
          (call_script, "script_set_town_picture"),
          #(call_script, "script_get_settlement_mesh", "$current_town"),
          #(set_background_mesh, reg0),
        (try_end),

        (try_begin),
          (eq, "$g_player_raid_complete", 1),
          (assign, "$g_player_raid_complete", 0),
          (jump_to_menu, "mnu_village_loot_complete"),
        (else_try),
          (party_get_slot, ":raider_party", "$current_town", slot_village_raided_by),
          (gt, ":raider_party", 0),
        # Process here...
        (try_end),

        (try_begin),
          (eq, "$g_leave_town",1),
          (assign, "$g_leave_town",0),
          (change_screen_return),
        (try_end),

        (try_begin),
          (store_time_of_day, ":cur_hour"),
          (ge, ":cur_hour", 5),
          (lt, ":cur_hour", 21),
          (assign, "$town_nighttime", 0),
        (else_try),
          (assign, "$town_nighttime", 1),
        (try_end),
    ],
    [
    ## CC
      ("auto_sell",
        [
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        ],
       "Sell items automatically.",
       [
          (assign, "$g_next_menu", "mnu_village"),
          (jump_to_menu, "mnu_trade_auto_sell_begin"),
        ]),

      ("auto_buy_food",
        [
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        ],
       "Buy food automatically.",
       [
          (assign, "$g_next_menu", "mnu_village"),
          (jump_to_menu, "mnu_trade_auto_buy_food_begin"),
        ]),
      ("Meet_with_village_elder",
       [
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        ],
         "Meet with the elder.",
         [
           (try_begin),
              (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
              (call_script, "script_start_town_conversation", slot_town_elder, 11),
           (try_end),
          ]),      ("village_manage",
      [
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player")
        ]
       , "Manage this village.",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_center_manage"),
        ]),
      ("recruit_volunteers",
      [
        (call_script, "script_cf_village_recruit_volunteers_cond"),
        #tom
        (assign, ":continue", 0),
        (try_begin),
          (eq, "$use_feudal_lance", 1),
          (assign, ":continue", 1),
          (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
          (eq, ":town_lord", "trp_player"),
          (assign, ":continue", 0),
        (try_end),
        (eq, ":continue", 0),
        #tom
       ]
       , "Recruit Volunteers.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (eq, "$use_feudal_lance", 0), #tom
           (jump_to_menu, "mnu_recruit_volunteers"),
           #tom
         (else_try),
           (eq, "$use_feudal_lance", 1),
           (jump_to_menu, "mnu_lance_recruitment"),
           #tom
         (try_end),
        ]),
        #retinue ###VILLLAGE
    ("call_retinue",
      [
        (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),        
        (this_or_next|eq, ":town_lord", "trp_player"),
        (ge, "$cheat_mode", 1),
        ], "Invite local nobles to a hunt.",
       [
          #(call_script, "script_enter_court", "$current_town"),
          (set_jump_mission, "mt_visit_town_castle"),
          (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
          #(party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
          (call_script, "script_get_party_campsite", "$current_town"),
          (assign, ":castle_scene", reg0),
          (modify_visitors_at_site, ":castle_scene"),
          (reset_visitors),
          
          ###guards
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_get_slot, ":guard_troop", ":center_faction", slot_faction_guard_troop),
          (try_begin),
            (le, ":guard_troop", 0),
            (assign, ":guard_troop", "trp_euro_spearman_3"),
          (try_end),
          (set_visitor, 6, ":guard_troop"),
          (set_visitor, 7, ":guard_troop"),
          
          (assign, ":cur_pos", 16),
          
          (assign, reg5, 0),
          (party_get_slot, ":local_culture", "$current_town", slot_center_culture),
          #(party_get_slot, ":culture", "$current_town",slot_center_culture),
          (faction_get_slot, ":fac_troop", ":local_culture",slot_faction_tier_1_castle_troop),
          
          (assign, ":start_troop", -1),
          (assign, ":end_troop", -1),
          (try_begin),  #monogol
            (this_or_next|eq, ":center_faction", "fac_kingdom_3"),
            (this_or_next|eq, ":center_faction", "fac_kingdom_27"),
            (eq, ":local_culture", "fac_culture_mongol"),
            (faction_get_slot, ":fac_troop", "fac_culture_mongol",slot_faction_tier_1_castle_troop),
            (assign, reg5, "$retinue_noble_mongol"),
            (val_add, "$retinue_noble_mongol", 1),
            (assign, ":start_troop", "trp_npc13"),
            (assign, ":end_troop", "trp_npc16"), #trp_npc30
            #(val_add, ":end_troop", 1),
          (else_try),  #baltic
            (eq, ":local_culture", "fac_culture_baltic"),
            (neq, ":center_faction", "fac_kingdom_1"), #not crusader kngihts
            (assign, reg5, "$retinue_noble_balt"),
            (val_add, "$retinue_noble_balt", 1),
            (assign, ":start_troop", "trp_npc1"),
            (assign, ":end_troop", "trp_npc4"), #trp_npc7
          (else_try), #orthodox
            (this_or_next|eq, ":local_culture", "fac_culture_rus"),
            (this_or_next|eq, ":local_culture", "fac_culture_serbian"),
            (this_or_next|eq, ":local_culture", "fac_culture_balkan"),
            (eq, ":local_culture", "fac_culture_byzantium"),
            (assign, reg5, "$retinue_noble_orthodox"),
            (val_add, "$retinue_noble_orthodox", 1),
            (assign, ":start_troop", "trp_npc7"),
            (assign, ":end_troop", "trp_npc10"), #trp_npc19
          (else_try), #muslim
            (this_or_next|eq, ":local_culture", "fac_culture_marinid"),
            (this_or_next|eq, ":local_culture", "fac_culture_mamluke"),
            (this_or_next|eq, ":local_culture", "fac_culture_andalus"),
            (eq, ":local_culture", "fac_culture_anatolian"),
            (assign, reg5, "$retinue_noble_muslim"),
            (val_add, "$retinue_noble_muslim", 1),
            (assign, ":start_troop", "trp_npc10"),
            (assign, ":end_troop", "trp_npc13"), #trp_npc25
          (else_try), #western - anything else
            (assign, reg5, "$retinue_noble_west"),
            (val_add, "$retinue_noble_west", 1),
            (assign, ":start_troop", "trp_npc4"),
            (assign, ":end_troop", "trp_npc7"), #trp_npc13
            (eq, ":center_faction", "fac_kingdom_1"), #not crusader kngihts
            (faction_get_slot, ":fac_troop", "fac_culture_teutonic",slot_faction_tier_1_castle_troop),
          (try_end),
          
          #(party_get_slot, ":culture", slot_center_culture
         
          (try_for_range, ":troop", ":start_troop", ":end_troop"),
            (neg | troop_slot_eq, ":troop", slot_troop_traveling, 1), # rafi
            (troop_slot_eq, ":troop", slot_troop_days_on_mission, 0),
            (troop_slot_eq, ":troop", slot_troop_occupation, slto_inactive),
            (neg|troop_slot_ge, ":troop", slot_troop_prisoner_of_party, 0),
            (neq, ":troop", "$g_player_minister"),
            (neq, ":troop", "$g_player_chamberlain"),
            (neq, ":troop", "$g_player_constable"),
            (set_visitor, ":cur_pos", ":troop"),
            (val_add, ":cur_pos", 1),
            #ADD CHECK HERE
            (eq, reg5, 0), #culture equip first time
            (call_script, "script_equip_companion", ":troop", ":fac_troop"),
          (try_end),
               # (this_or_next|eq, "$talk_context", tc_tavern_talk),
        # (eq, "$talk_context", tc_court_talk),
          (assign, "$talk_context", tc_court_talk),
          (jump_to_scene, ":castle_scene"),
          (change_screen_mission),
        ]),
        #retinue end
        #retinue end
################################################################
      ("village_center",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),]
       , "Go to the Village center.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site, ":village_scene"),
           (reset_visitors),
           (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
           (set_visitor, 11, ":village_elder_troop"),

           (call_script, "script_init_town_walkers"),

           (try_begin),
             (check_quest_active, "qst_hunt_down_fugitive"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
             (neg|check_quest_failed, "qst_hunt_down_fugitive"),
             (set_visitor, 45, "trp_fugitive"),
           (try_end),

           
#################################### BRYTENWALDA TAVERN BOUNTY
        (try_begin),
          (check_quest_active, "qst_bounty_1"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_1"),
             (neg|check_quest_failed, "qst_bounty_1"),
          (try_begin),
            (eq, "$g_random_fugitive_1", 1),
            (assign, "$bounty_target_1", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_1", 2),
            (assign, "$bounty_target_1", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_1", 3),
            (assign, "$bounty_target_1", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_1", 4),
            (assign, "$bounty_target_1", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_1", 5),
            (assign, "$bounty_target_1", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_1", 6),
            (assign, "$bounty_target_1", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_1", 7),
            (assign, "$bounty_target_1", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_1", 8),
            (assign, "$bounty_target_1", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_1", 9),
            (assign, "$bounty_target_1", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_1", 10),
            (assign, "$bounty_target_1", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_1"),
       (try_end),

        (try_begin),
          (check_quest_active, "qst_bounty_2"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_2"),
             (neg|check_quest_failed, "qst_bounty_2"),
          (try_begin),
            (eq, "$g_random_fugitive_2", 1),
            (assign, "$bounty_target_2", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_2", 2),
            (assign, "$bounty_target_2", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_2", 3),
            (assign, "$bounty_target_2", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_2", 4),
            (assign, "$bounty_target_2", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_2", 5),
            (assign, "$bounty_target_2", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_2", 6),
            (assign, "$bounty_target_2", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_2", 7),
            (assign, "$bounty_target_2", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_2", 8),
            (assign, "$bounty_target_2", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_2", 9),
            (assign, "$bounty_target_2", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_2", 10),
            (assign, "$bounty_target_2", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_2"),
       (try_end),
          
          
        (try_begin),
          (check_quest_active, "qst_bounty_3"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_3"),
             (neg|check_quest_failed, "qst_bounty_3"),
         
          (try_begin),
            (eq, "$g_random_fugitive_3", 1),
            (assign, "$bounty_target_3", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_3", 2),
            (assign, "$bounty_target_3", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_3", 3),
            (assign, "$bounty_target_3", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_3", 4),
            (assign, "$bounty_target_3", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_3", 5),
            (assign, "$bounty_target_3", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_3", 6),
            (assign, "$bounty_target_3", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_3", 7),
            (assign, "$bounty_target_3", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_3", 8),
            (assign, "$bounty_target_3", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_3", 9),
            (assign, "$bounty_target_3", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_3", 10),
            (assign, "$bounty_target_3", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_3"),
       (try_end),
          
          
        (try_begin),
          (check_quest_active, "qst_bounty_4"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_4"),
             (neg|check_quest_failed, "qst_bounty_4"),
          (try_begin),
            (eq, "$g_random_fugitive_4", 1),
            (assign, "$bounty_target_4", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_4", 2),
            (assign, "$bounty_target_4", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_4", 3),
            (assign, "$bounty_target_4", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_4", 4),
            (assign, "$bounty_target_4", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_4", 5),
            (assign, "$bounty_target_4", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_4", 6),
            (assign, "$bounty_target_4", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_4", 7),
            (assign, "$bounty_target_4", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_4", 8),
            (assign, "$bounty_target_4", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_4", 9),
            (assign, "$bounty_target_4", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_4", 10),
            (assign, "$bounty_target_4", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_4"),
       (try_end),
          
          
        (try_begin),
          (check_quest_active, "qst_bounty_5"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_5"),
             (neg|check_quest_failed, "qst_bounty_5"),
          (try_begin),
            (eq, "$g_random_fugitive_5", 1),
            (assign, "$bounty_target_5", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_5", 2),
            (assign, "$bounty_target_5", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_5", 3),
            (assign, "$bounty_target_5", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_5", 4),
            (assign, "$bounty_target_5", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_5", 5),
            (assign, "$bounty_target_5", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_5", 6),
            (assign, "$bounty_target_5", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_5", 7),
            (assign, "$bounty_target_5", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_5", 8),
            (assign, "$bounty_target_5", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_5", 9),
            (assign, "$bounty_target_5", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_5", 10),
            (assign, "$bounty_target_5", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_5"),
       (try_end),
          
          
        (try_begin),
          (check_quest_active, "qst_bounty_6"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_6"),
             (neg|check_quest_failed, "qst_bounty_6"),
          (try_begin),
            (eq, "$g_random_fugitive_6", 1),
            (assign, "$bounty_target_6", "trp_bounty_1_knight"),
          (else_try),
            (eq, "$g_random_fugitive_6", 2),
            (assign, "$bounty_target_6", "trp_bounty_2_bandit"),
          (else_try),
            (eq, "$g_random_fugitive_6", 3),
            (assign, "$bounty_target_6", "trp_bounty_3_bandit_leader"),
          (else_try),
            (eq, "$g_random_fugitive_6", 4),
            (assign, "$bounty_target_6", "trp_bounty_4_deserter"),
          (else_try),
            (eq, "$g_random_fugitive_6", 5),
            (assign, "$bounty_target_6", "trp_fugitive"),
          (else_try),
            (eq, "$g_random_fugitive_6", 6),
            (assign, "$bounty_target_6", "trp_bounty_5_arena_fighter"),
          (else_try),
            (eq, "$g_random_fugitive_6", 7),
            (assign, "$bounty_target_6", "trp_bounty_6_pirate"),
          (else_try),
            (eq, "$g_random_fugitive_6", 8),
            (assign, "$bounty_target_6", "trp_bounty_7_pirate_captain"),
          (else_try),
            (eq, "$g_random_fugitive_6", 9),
            (assign, "$bounty_target_6", "trp_bounty_8_mercenary"),
          (else_try),
            (eq, "$g_random_fugitive_6", 10),
            (assign, "$bounty_target_6", "trp_bounty_9_mercenary_captain"),
          (try_end),
          (set_visitor, 45, "$bounty_target_6"),
       (try_end),
          
######################################################################### 



           (set_jump_mission, "mt_village_center"),
           (jump_to_scene, ":village_scene"),
           (change_screen_mission),
         (try_end),
        ], "Door to the village center."),
      ("village_buy_food",[(party_slot_eq, "$current_town", slot_village_state, 0),
                           (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                           ], "Buy supplies from the peasants.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
           (change_screen_trade, ":merchant_troop"),
         (try_end),
         ]),

      ("village_attack_bandits",[
        (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        ##diplomacy begin
        (neg|party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ##diplmacy end
        ],
       "Attack the bandits.",

       [(party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
        (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),

        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
        (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission, "mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_village_infest_bandits_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
        ]),

      ("village_wait",
       [(party_slot_eq, "$current_town", slot_center_has_manor, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        ],
         "Wait here for some time.",
         [
           (assign, "$auto_enter_town", "$current_town"),
           (assign, "$g_last_rest_center", "$current_town"),

           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),
           (try_end),

           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
           (change_screen_return),
          ]),

       ##diplomacy begin
      ("dplmc_village_counter_insurgency",[
        (party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ],
       "Counter the insurgency.",
       [
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1), #check
          (set_jump_mission, "mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_dplmc_village_riot_result"),

          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
        ]),

      ("dplmc_village_negotiate",[
        (party_slot_eq, "$current_town", slot_village_infested_by_bandits, "trp_peasant_woman"),
        ],
       "Begin negotiations.",
       [
          (jump_to_menu, "mnu_dplmc_riot_negotiate"),
        ]),
        ##diplomacy end
        
        #tom
      ("village_spawn_manor",[
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_slot_eq, "$current_town",slot_town_lord, "trp_player"),
          #rev3 it should be an empty field
          (party_get_slot, ":manor", "$current_town", village_slot_manor),
          # (party_get_template_id, ":manor_template", ":manor"),
          # (eq, ":manor_template", "pt_empty"),
          # (assign, "$current_manor_id", ":manor"),
          (le, ":manor", 0),
        ],
       "Invest into regional manor.",
       [
          (assign, "$g_next_menu", "mnu_village"),
          (jump_to_menu, "mnu_center_spawn_manor"),
        ]),
        #tom

      ("collect_taxes_qst",[(party_slot_eq, "$current_town", slot_village_state, 0),
                            (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                            (check_quest_active, "qst_collect_taxes"),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),

      ("train_peasants_against_bandits_qst",
       [
         (party_slot_eq, "$current_town", slot_village_state, 0),
         (check_quest_active, "qst_train_peasants_against_bandits"),
         (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
         (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town"),
         ], "Train the peasants.",
       [(jump_to_menu, "mnu_train_peasants_against_bandits"),]),

      ("village_hostile_action",[(party_slot_eq, "$current_town", slot_village_state, 0),
                                 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                                 (neq, "$players_kingdom", "$g_encountered_party_faction"),
                                 ], "Take a hostile action.",
       [(jump_to_menu, "mnu_village_hostile_action"),
           ]),

      ("village_reports",[(eq, "$cheat_mode", 1),], "{!}CHEAT! Show reports.",
       [(jump_to_menu, "mnu_center_reports"),
           ]),

######################### NEW v1.8
      ("change_culture_village",
      [
          (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          
          # (faction_get_slot, ":cur_faction_culture", "$players_kingdom"),
          (this_or_next|eq, "$g_player_know_culture_finnish", 1),
          (this_or_next|eq, "$g_player_know_culture_mazovian", 1),
          (this_or_next|eq, "$g_player_know_culture_serbian", 1),
          (this_or_next|eq, "$g_player_know_culture_welsh", 1),
          (this_or_next|eq, "$g_player_know_culture_teutonic", 1),
          (this_or_next|eq, "$g_player_know_culture_balkan", 1),
          (this_or_next|eq, "$g_player_know_culture_rus", 1),
          (this_or_next|eq, "$g_player_know_culture_nordic", 1),
          (this_or_next|eq, "$g_player_know_culture_baltic", 1),
          (this_or_next|eq, "$g_player_know_culture_marinid", 1),
          (this_or_next|eq, "$g_player_know_culture_mamluke", 1),
          (this_or_next|eq, "$g_player_know_culture_byzantium", 1),
          (this_or_next|eq, "$g_player_know_culture_iberian", 1),
          (this_or_next|eq, "$g_player_know_culture_italian", 1),
          (this_or_next|eq, "$g_player_know_culture_andalus", 1),
          (this_or_next|eq, "$g_player_know_culture_gaelic", 1),
          (this_or_next|eq, "$g_player_know_culture_anatolian_christian", 1),
          (this_or_next|eq, "$g_player_know_culture_anatolian", 1),
          (this_or_next|eq, "$g_player_know_culture_western", 1),
          (this_or_next|eq, "$g_player_know_culture_mongol", 1),
          (this_or_next|eq, "$g_player_know_culture_templar", 1),
          (this_or_next|eq, "$g_player_know_culture_hospitaller", 1),
          (eq, "$g_player_know_culture_player", 1),    
       ]
       , "Change this village's culture.",
       [
         (jump_to_menu, "mnu_change_culture"),
         
        ]),
###########################################################################

      ("village_leave",[], "Leave...",[(change_screen_return,0)]),

    ],
  ),

   ("village_hostile_action",0,
    "What action do you have in mind?",
    "none",
    [],
    [
      ("village_take_food",[
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
          (assign, ":town_stores_not_empty", 0),
          (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
            (ge, ":slot_item", 0),
            (assign, ":town_stores_not_empty", 1),
          (try_end),
          (eq, ":town_stores_not_empty", 1),
          ], "Force the peasants to give you supplies.",
       [
           (jump_to_menu, "mnu_village_take_food_confirm")
        ]),
      ("village_steal_cattle",
       [
          (party_slot_eq, "$current_town", slot_village_state, 0),
          (party_slot_eq, "$current_town", slot_village_player_can_not_steal_cattle, 0),
          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
          (gt, ":num_cattle", 0),
          ], "Steal cattle.",
       [
           (jump_to_menu, "mnu_village_steal_cattle_confirm")
        ]),
        
      # ("village_tavern",
                     # [(party_slot_eq, "$current_town", slot_village_state, 0),
                       # (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                       # (party_slot_eq, "$current_town",slot_center_has_tavern,1 ),
                       # ],
       # "To the tavern. To get drunk as a cow!",
       # [
            # (display_message, "@ALE!"),
           # ]),
           
        ("village_loot",[(party_slot_eq, "$current_town", slot_village_state, 0),
                       (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                       (store_faction_of_party, ":center_faction", "$current_town"),
                       # (store_relation, ":reln", "fac_player_supporters_faction", ":center_faction"),
                       (store_relation, ":reln", "$players_kingdom", ":center_faction"),  ####### NEW v3.3
                       (lt, ":reln", 0),
                       ],
       "Loot and burn this village.",
       [
#           (party_clear, "$current_town"),
#           (party_add_template, "$current_town", "pt_villagers_in_raid"),
           (jump_to_menu, "mnu_village_start_attack"),
           ]),   
         
      ("forget_it",[],
      "Forget it.",[(jump_to_menu, "mnu_village")]),
    ],
  ),

   ("recruit_volunteers",0,
    "{s18}",
    "none",
    [(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
     (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
     (val_min, ":volunteer_amount", ":free_capacity"),
     (store_troop_gold, ":gold", "trp_player"),
     (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
     (val_min, ":volunteer_amount", ":gold_capacity"),
     (assign, reg5, ":volunteer_amount"),

      # rafi hospitallers/templars/teutonic
      (store_faction_of_party, ":faction", "$current_town"),

      (try_begin),
        (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),

        (try_begin),
          (eq, "$players_kingdom", "fac_kingdom_1"),
          (eq, ":faction", "fac_kingdom_6"),
          (try_begin),
          #TOM
            # (party_slot_eq, "$current_town", slot_party_type, spt_village),
            # (assign, ":volunteer_troop", "trp_teu_village_recruit"),
          # (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (assign, ":volunteer_troop", "trp_teu_horse_1"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (assign, ":volunteer_troop", "trp_teu_town_1"),
          (try_end),
          #TOM
        # (else_try),
          # (eq, "$players_kingdom", "fac_kingdom_23"),
          # (store_random_in_range, ":random", 0, 3),
          # (try_begin),
            # (eq, ":random", 0),
            # (try_begin),
              # (party_slot_eq, "$current_town", slot_party_type, spt_village),
              # (assign, ":volunteer_troop", "trp_iberian_village_recruit"),
            # (else_try),
              # (party_slot_eq, "$current_town", slot_party_type, spt_castle),
              # (assign, ":volunteer_troop", "trp_crusader_turkopole"),
            # (else_try),
              # (party_slot_eq, "$current_town", slot_party_type, spt_town),
              # (assign, ":volunteer_troop", "trp_iberian_town_recruit"),
            # (try_end),
          # (else_try),
            # (eq, ":random", 1),
            # (try_begin),
              # (party_slot_eq, "$current_town", slot_party_type, spt_village),
              # (assign, ":volunteer_troop", "trp_iberian_village_recruit"),
            # (else_try),
              # (party_slot_eq, "$current_town", slot_party_type, spt_castle),
              # (assign, ":volunteer_troop", "trp_crusader_turkopole"),
            # (else_try),
              # (party_slot_eq, "$current_town", slot_party_type, spt_town),
              # (assign, ":volunteer_troop", "trp_iberian_town_recruit"),
            # (try_end),
         # (try_end),
        (try_end),
        (party_set_slot, "$current_town", slot_center_volunteer_troop_type, ":volunteer_troop"),
      (try_end),
      # end rafi

     (try_begin),
       (eq, ":volunteer_amount", 0),
       (str_store_string, s18, "@No one here seems to be willing to join your party."),
     (else_try),
       (assign, ":divisor", recruitment_cost_village),
       (try_begin),
        (party_slot_eq, "$current_town", slot_party_type, spt_castle),
        (assign, ":divisor", recruitment_cost_castle),
       (else_try),
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
        (assign, ":divisor", recruitment_cost_town),
       (try_end),

       (store_mul, reg6, ":volunteer_amount", ":divisor"),#10 denars per man
       (store_mul, reg7, 1, ":divisor"),#10 denars per man
       (str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),
       (try_begin),
         (eq, reg5, 1),
         (str_store_string, s18, "@One {s3} volunteers to follow you."),
       (else_try),
         (str_store_string, s18, "@{reg5} {s3} volunteer to follow you."),
       (try_end),
       (set_background_mesh, "mesh_pic_recruits"),
     (try_end),
    ],
    [
      ("continue",[(eq, reg5, 0)],
       "Continue...",
        [
          (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
          (try_begin),
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (jump_to_menu, "mnu_village"),
          (try_end)
      ]),
      ("recruit_them",[(gt, reg5, 0)],
       "Recruit all of them ({reg6} denars).",
        [
          (call_script, "script_village_recruit_volunteers_recruit", -1),
          (try_begin),
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (jump_to_menu, "mnu_village"),
          (try_end)

      ]),
      ("recruit_one_of_them",[(gt, reg5, 0)],
       "Recruit one of them ({reg7} denars).",
        [
          (call_script, "script_village_recruit_volunteers_recruit", 1),
          (try_begin),
            (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
            (gt, ":volunteer_amount", 0),
            (jump_to_menu, "mnu_recruit_volunteers"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (jump_to_menu, "mnu_village"),
          (try_end)

      ]),

      ("forget_it",[(gt, reg5, 0)],
      "Forget it.",
        [
          (try_begin),
            (party_slot_eq, "$current_town", slot_party_type, spt_town),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (jump_to_menu, "mnu_village"),
          (try_end)
      ]),
    ],
  ),

   ("village_hunt_down_fugitive_defeated",0,
    "A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark. Time passes. When you open your eyes again you find yourself battered and bloody, but luckily none of the wounds appear to be lethal.",
    "none",
    [],
    [
      ("continue",[], "Continue...",[(jump_to_menu, "mnu_village"),]),
    ],
  ),

   ("village_infest_bandits_result",mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_village_infestation_removed"),
     (else_try),
       (str_store_string, s9, "@Try as you might, you could not defeat the bandits. Infuriated, they raze the village to the ground to punish the peasants, and then leave the burning wasteland behind to find greener pastures to plunder."),
       (set_background_mesh, "mesh_pic_looted_village"),
     (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [(party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (call_script, "script_village_set_state",  "$current_town", svs_looted),
        (party_set_slot, "$current_town", slot_village_raid_progress, 0),
        (party_set_slot, "$current_town", slot_village_recover_progress, 0),
        (try_begin),
          (check_quest_active, "qst_eliminate_bandits_infesting_village"),
          (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
          (call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
          (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
        (else_try),
          (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
          (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -4),
          (call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
          (call_script, "script_end_quest", "qst_deal_with_bandits_at_lords_village"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (try_end),
        (jump_to_menu, "mnu_village"),]),
    ],
  ),


   ("village_infestation_removed",mnf_disable_all_keys,
    "In a battle worthy of song, you and your men drive the bandits out of the village, making it safe once more. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find.",
    "none",
    [(party_get_slot, ":bandit_troop", "$g_encountered_party", slot_village_infested_by_bandits),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (party_clear, "p_temp_party"),
     (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
     (assign, "$g_strength_contribution_of_player", 50),
     (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
     (try_begin),
       (check_quest_active, "qst_eliminate_bandits_infesting_village"),
       (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
       #Add quest reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
     (else_try),
       (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
       (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
     (else_try),
     #Add normal reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
     (try_end),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 70),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
    ],
    [
      ("village_bandits_defeated_accept",[], "Take it as your just due.",[(jump_to_menu, "mnu_village"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),

      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",
      [    (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
        (call_script, "script_change_player_honor", 1),
        (jump_to_menu, "mnu_village")]),
    ],
  ),

   ("center_manage",0,
    "{s19}^{reg6?^^You are currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
    "none",
    [(assign, ":num_improvements", 0),
     (str_clear, s18),
     (try_begin),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (val_add, ":end", 1), ######### NEW v3.8
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),

     (try_for_range, ":improvement_no", ":begin", ":end"),
       (try_begin),
         (eq, ":improvement_no", ":end"), ######### NEW v3.8
           (assign, ":improvement_no", slot_center_has_stables),
       (try_end),
       (party_slot_ge, "$g_encountered_party", ":improvement_no", 1),
       (party_get_slot, ":improvement_level", "$g_encountered_party", ":improvement_no"), ######## NEW v3.8
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no", ":improvement_level"), ######## NEW v3.8
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{!}{s0}"),
       (else_try),
         (str_store_string, s18, "@{!}{s18}, {s0}"),
       (try_end),
     (try_end),

     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements: {s18}."),
     (try_end),

     (assign, reg6, 0),
     (try_begin),
       (party_get_slot, ":cur_improvement", "$g_encountered_party", slot_center_current_improvement),
       (party_get_slot, ":cur_improvement_level", "$g_encountered_party", slot_center_current_improvement_level),
       (gt, ":cur_improvement", 0),
       (call_script, "script_get_improvement_details", ":cur_improvement", ":cur_improvement_level"),
       (str_store_string, s7, s0),
       (assign, reg6, 1),
       (store_current_hours, ":cur_hours"),
       (party_get_slot, ":finish_time", "$g_encountered_party", slot_center_improvement_end_hour),
       (val_sub, ":finish_time", ":cur_hours"),
       (store_div, reg8, ":finish_time", 24),
       (val_max, reg8, 1),
       (store_sub, reg9, reg8, 1),
     (try_end),
	 (assign, "$g_improvement_type_level", 0),  ########## NEW v3.8
    ],
    [
      ("center_build_manor",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0),
                                  ],
       "Build a manor house.",[(assign, "$g_improvement_type", slot_center_has_manor),
                         (jump_to_menu, "mnu_center_improve"),]),
                         
      ("center_build_fish_pond",[(eq, reg6, 0),
                                 (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                 (party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0),
                                  ],
       "Build a mill.",[(assign, "$g_improvement_type", slot_center_has_fish_pond),
                             (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_watch_tower",[(eq, reg6, 0),
                                   (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                   (party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0),
                                  ],
       "Build a watch tower.",[(assign, "$g_improvement_type", slot_center_has_watch_tower),
                               (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_school",[(eq, reg6, 0),
                              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                              (party_slot_eq, "$g_encountered_party", slot_center_has_school, 0),
                                  ],
       "Build a school.",[(assign, "$g_improvement_type", slot_center_has_school),
                          (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_messenger_post",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0),
                                       ],
       "Build a messenger post.",[(assign, "$g_improvement_type", slot_center_has_messenger_post),
                                  (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_prisoner_tower",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0),
                                       ],
       "Build a prisoner tower.",[(assign, "$g_improvement_type", slot_center_has_prisoner_tower),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
                                  
                                  
      # rafi
      ("center_build_fortifications_1",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (neg | party_slot_eq, "$g_encountered_party", slot_center_has_fortifications_1, 1),
                                      (neg | party_slot_eq, "$g_encountered_party", slot_center_has_fortifications_2, 1),
                                      (eq, "$g_encountered_party", "p_castle_player"),
                                      (display_message, "@fort castle_player"),
                                       ],
       "Improve the fortifications.",[(assign, "$g_improvement_type", slot_center_has_fortifications_1),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
                                  
                                  
      ("center_build_fortifications_2",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_fortifications_1, 1),
                                      (neg | party_slot_eq, "$g_encountered_party", slot_center_has_fortifications_2, 1),
                                      (eq, "$g_encountered_party", "p_castle_player"),
                                       ],
       "Improve the fortifications.",[(assign, "$g_improvement_type", slot_center_has_fortifications_2),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
	################## NEW v3.8
      ("center_build_stables",[
	  (eq, reg6, 0),
      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
      (party_get_slot, ":level", "$g_encountered_party", slot_center_has_stables),
	  (ge, ":level", 0),
	  (lt, ":level", 4),
      ],
       "Improve the stables.",[
	   (assign, "$g_improvement_type", slot_center_has_stables),
       (party_get_slot, ":level", "$g_encountered_party", slot_center_has_stables),
	   (val_add, ":level", 1),
	   (assign, "$g_improvement_type_level", ":level"),
       (jump_to_menu, "mnu_center_improve"),]),
	################## 
      # rafi
      
#################################################### NEW IMPROVEMENTS

       # ("center_build_improvements_welfare",[
       # (eq, reg6, 0),
       # ],
       # "Build fief welfare improvements.",[(jump_to_menu, "mnu_improvement_welfare_select"),]),
      
      
      
       # ("center_build_improvements_economic",[
       # (eq, reg6, 0),
       # ],
       # "Build economic improvements.",[(jump_to_menu, "mnu_improvement_economic_select"),]),
      
      
      
       # ("center_build_improvements_military",[
       # (eq, reg6, 0),
       # ],
       # "Build military improvements.",[(jump_to_menu, "mnu_improvement_military_select"),]),
      
####################################################
     
      
      ("go_back_dot",[], "Go back.",[(jump_to_menu, "$g_next_menu")]),
    ],
  ),

   ("center_improve",0,
    "{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you {reg5} denars and will take {reg6} days.",
    "none",
    [      
	 ######## NEW v3.8
     (try_begin),
       (eq, "$g_improvement_type_level", 0), 
         (assign, "$g_improvement_type_level", 1), 
     (try_end),
	 ########################
     # (store_encountered_party, "$g_encountered_party"),
     (call_script, "script_get_improvement_details", "$g_improvement_type", "$g_improvement_type_level"),
     # (assign, "$g_improvement_type_level", 0), ######## NEW v3.8
     (assign, ":improvement_cost", reg0),
     (assign, ":improvement_time", reg1),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     
     #######(assign, ":improvement_cost_original", ":improvement_cost"),
     #######(assign, ":improvement_cost_original2", ":improvement_cost"),
     #######(assign, ":improvement_cost_original3", ":improvement_cost"),

     #######(assign, ":improvement_time_original", ":improvement_time"),
     #######(assign, ":improvement_time_original2", ":improvement_time"),
     #######(assign, ":improvement_time_original3", ":improvement_time"),

     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_cost", ":multiplier"),
     (val_div, ":improvement_cost", 20),
     
     ######### need to further add more stuff to reflect new buildings effects
     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_time", ":multiplier"),
     (val_div, ":improvement_time", 20),

     
#################### NEW STUFF

#################### MASON'S GUILD
#################### TIME
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_masons_guild, 1),
          # (val_div, ":improvement_time_original", 100),
          # (val_mul, ":improvement_time_original", tier_1_masons_guild_cost_time_reduction),
          # (val_sub, ":improvement_time", ":improvement_time_original"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_master_masons_guild, 1),
          # (val_div, ":improvement_time_original", 100),
          # (val_mul, ":improvement_time_original", tier_2_master_masons_guild_cost_time_reduction),
          # (val_sub, ":improvement_time", ":improvement_time_original"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_3_masons_guild_hq, 1),
          # (val_div, ":improvement_time_original", 100),
          # (val_mul, ":improvement_time_original", tier_3_masons_guild_hq_cost_time_reduction),
          # (val_sub, ":improvement_time", ":improvement_time_original"),
     # (try_end),     
     
     
################### COST
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_masons_guild, 1),
          # (val_div, ":improvement_cost_original", 100),
          # (val_mul, ":improvement_cost_original", tier_1_masons_guild_cost_time_reduction),
          # (val_sub, ":improvement_cost", ":improvement_cost_original"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_master_masons_guild, 1),
          # (val_div, ":improvement_cost_original", 100),
          # (val_mul, ":improvement_cost_original", tier_2_master_masons_guild_cost_time_reduction),
          # (val_sub, ":improvement_cost", ":improvement_cost_original"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_3_masons_guild_hq, 1),
          # (val_div, ":improvement_cost_original", 100),
          # (val_mul, ":improvement_cost_original", tier_3_masons_guild_hq_cost_time_reduction),
          # (val_sub, ":improvement_cost", ":improvement_cost_original"),
     # (try_end),     
     
     
################### TOWN ADMINISTRATION BUILDINGS
################### TIME
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_town_hall, 1),
          # (val_div, ":improvement_time_original2", 100),
          # (val_mul, ":improvement_time_original2", tier_1_town_hall_reduce_time_costs),
          # (val_sub, ":improvement_time", ":improvement_time_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_city_hall, 1),
          # (val_div, ":improvement_time_original2", 100),
          # (val_mul, ":improvement_time_original2", tier_2_city_hall_reduce_time_costs),
          # (val_sub, ":improvement_time", ":improvement_time_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_3_governors_palace, 1),
          # (val_div, ":improvement_time_original2", 100),
          # (val_mul, ":improvement_time_original2", tier_3_governors_palace_reduce_time_costs),
          # (val_sub, ":improvement_time", ":improvement_time_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_4_royal_palace, 1),
          # (val_div, ":improvement_time_original2", 100),
          # (val_mul, ":improvement_time_original2", tier_4_royal_palace_reduce_time_costs),
          # (val_sub, ":improvement_time", ":improvement_time_original2"),
     # (try_end),     
     
     
################### COST
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_town_hall, 1),
          # (val_div, ":improvement_cost_original2", 100),
          # (val_mul, ":improvement_cost_original2", tier_1_town_hall_reduce_time_costs),
          # (val_sub, ":improvement_cost", ":improvement_cost_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_city_hall, 1),
          # (val_div, ":improvement_cost_original2", 100),
          # (val_mul, ":improvement_cost_original2", tier_2_city_hall_reduce_time_costs),
          # (val_sub, ":improvement_cost", ":improvement_cost_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_3_governors_palace, 1),
          # (val_div, ":improvement_cost_original2", 100),
          # (val_mul, ":improvement_cost_original2", tier_3_governors_palace_reduce_time_costs),
          # (val_sub, ":improvement_cost", ":improvement_cost_original2"),
          
      # (else_try),
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_4_royal_palace, 1),
          # (val_div, ":improvement_cost_original2", 100),
          # (val_mul, ":improvement_cost_original2", tier_4_royal_palace_reduce_time_costs),
          # (val_sub, ":improvement_cost", ":improvement_cost_original2"),
     # (try_end),     
     
     
################### VILLAGE COUNCIL
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_village_council_hall, 1),
          # (val_div, ":improvement_time_original3", 100),
          # (val_mul, ":improvement_time_original3", tier_1_village_council_hall_reduction_costs_time),
          # (val_sub, ":improvement_time", ":improvement_time_original3"),
     # (try_end),     
     
     # (try_begin),  
        # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_village_council_hall, 1),
          # (val_div, ":improvement_cost_original3", 100),
          # (val_mul, ":improvement_cost_original3", tier_1_village_council_hall_reduction_costs_time),
          # (val_sub, ":improvement_cost", ":improvement_cost_original3"),
     # (try_end),     
     
##############################################################




     (try_begin),
      (this_or_next | eq, "$g_improvement_type", slot_center_has_fortifications_1),
      (this_or_next | eq, "$g_improvement_type", slot_center_has_fortifications_2),
      (eq, "$g_improvement_type", slot_party_temp_slot_1),
      (val_div, ":improvement_time", 5),     
    (try_end),

     (assign, reg5, ":improvement_cost"),
     (assign, reg6, ":improvement_time"),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ##diplomacy begin
      ("dplmc_improve_cont",
      [
        (gt, "$g_player_chamberlain", 0),
        (store_troop_gold, ":cur_gold", "trp_household_possessions"),
        (ge, ":cur_gold", reg5)
      ], "Go on. (Pay from treasury)",
        [
          (call_script, "script_dplmc_withdraw_from_treasury", reg5),
          (party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
          (party_set_slot, "$g_encountered_party", slot_center_current_improvement_level, "$g_improvement_type_level"),  ###### NEW v3.8
          (store_current_hours, ":cur_hours"),
          (store_mul, ":hours_takes", reg6, 24),
          (val_add, ":hours_takes", ":cur_hours"),
          (party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":hours_takes"),
          (jump_to_menu, "mnu_center_manage"),
         ]
      ),
      ##diplomacy end
      ("improve_cont",[(store_troop_gold, ":cur_gold", "trp_player"),
                       (ge, ":cur_gold", reg5)],
       "Go on.", [(troop_remove_gold, "trp_player", reg5),
                  (party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
                  (party_set_slot, "$g_encountered_party", slot_center_current_improvement_level, "$g_improvement_type_level"),  ###### NEW v3.8
                  (store_current_hours, ":cur_hours"),
                  (store_mul, ":hours_takes", reg6, 24),
                  (val_add, ":hours_takes", ":cur_hours"),
                  (party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":hours_takes"),
                  (jump_to_menu, "mnu_center_manage"),
                  ]),
      ("forget_it",[(store_troop_gold, ":cur_gold", "trp_player"),
                     ##diplomacy begin
                    (store_troop_gold, ":cur_treasury", "trp_household_possessions"),
                    (this_or_next|ge, ":cur_treasury", reg5),
                    ##diplomacy end
                    (ge, ":cur_gold", reg5)],
       "Forget it.", [(jump_to_menu, "mnu_center_manage")]),
      ("improve_not_enough_gold",[(store_troop_gold, ":cur_gold", "trp_player"),
                                  ##diplomacy begin
                                  (store_troop_gold, ":cur_treasury", "trp_household_possessions"),
                                  (this_or_next|lt, ":cur_treasury", reg5),
                                  ##diplomacy end
                                  (lt, ":cur_gold", reg5)],
       "I don't have enough money for that.", [(jump_to_menu, "mnu_center_manage"),]),
    ],
  ),

   ("town_bandits_failed",mnf_disable_all_keys,
    "{s4} {s5}",
    "none",
    [
#      (call_script, "script_loot_player_items", 0),
      (store_troop_gold, ":total_gold", "trp_player"),
      (store_div, ":gold_loss", ":total_gold", 100),
      (store_random_in_range, ":random_loss", 40, 100),
      (val_add, ":gold_loss", ":random_loss"),
      (val_min, ":gold_loss", ":total_gold"),
      (troop_remove_gold, "trp_player", ":gold_loss"),
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (party_get_num_companions, ":num_companions", "p_main_party"),
      (str_store_string, s4, "@The assasins beat you down and leave you for dead. ."),
      (str_store_string, s4, "@You have fallen. The bandits quickly search your body for every coin they can find, then vanish into the night. They have left you alive, if only barely."),
      (try_begin),
        (gt, ":num_companions", 2),
        (str_store_string, s5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
      (else_try),
        (str_store_string, s5, "@Luckily some passing townspeople find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
      (try_end),
    ],
    [
      ("continue",[], "Continue...",[(change_screen_return)]),
    ],
  ),

   ("town_bandits_succeeded",mnf_disable_all_keys,
    "The bandits fall before you as wheat to a scythe! Soon you stand alone in the streets while most of your attackers lie unconscious, dead or dying. Searching the bodies, you find a purse which must have belonged to a previous victim of these brutes. Or perhaps, it was given to them by someone who wanted to arrange a suitable ending to your life.",
    "none",
    [
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),
      (try_begin),
        (check_quest_active, "qst_deal_with_night_bandits"),
        (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
        (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, "$g_encountered_party"),
        (call_script, "script_succeed_quest", "qst_deal_with_night_bandits"),
      (try_end),
      (store_mul, ":xp_reward", "$num_center_bandits", 117),
      (add_xp_to_troop, ":xp_reward", "trp_player"),
      (store_mul, ":gold_reward", "$num_center_bandits", 50),
      (call_script, "script_troop_add_gold", "trp_player", ":gold_reward"),
    ],
    [
      ("continue",[], "Continue...",[(change_screen_return)]),
    ],
  ),


    ("village_steal_cattle_confirm",0,
    "As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle.",
    "none",
    [
      (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
      (assign, reg2, reg0),
      (assign, ":max_skill_owner", reg1),
      (try_begin),
        (eq, ":max_skill_owner", "trp_player"),
        (assign, reg3, 1),
      (else_try),
        (assign, reg3, 0),
        (str_store_troop_name, s1, ":max_skill_owner"),
      (try_end),
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, reg4, reg0),
      ],
    [
      ("village_steal_cattle_confirm",[], "Go on.",
       [
         #(rest_for_hours_interactive, 3, 5, 1), #rest while attackable
         # rafi
         (rest_for_hours_interactive, 3, 3, 1), #rest while attackable
         # end
         (assign, "$auto_menu", "mnu_village_steal_cattle"),
         (change_screen_return),
       ]),
      ("forget_it",[], "Forget it.",[(change_screen_return)]),
    ],
  ),

   ("village_steal_cattle",mnf_disable_all_keys,
    "{s1}",
    "none",
    [
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, ":max_value", reg0),
      (val_add, ":max_value", 1),
      (store_random_in_range, ":random_value", 0, ":max_value"),
      (party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),
      (party_get_slot, ":lord", "$current_town", slot_town_lord),
      (try_begin),
        (le, ":random_value", 0),
        (call_script, "script_change_player_relation_with_center", "$current_town", -3),
        (str_store_string, s1, "@You fail to steal any cattle."),
      (else_try),
        (assign, reg17, ":random_value"),
        (store_sub, reg12, ":random_value", 1),
        (try_begin),
          (gt, ":lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":lord", -3),
          (call_script, "script_add_log_entry", logent_player_stole_cattles_from_village, "trp_player",  "$current_town", ":lord", "$g_encountered_party_faction"),
        (try_end),
        (call_script, "script_change_player_relation_with_center", "$current_town", -5),
        (str_store_string, s1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),

        (try_begin),
          (eq, ":random_value", 3),
          (unlock_achievement, ACHIEVEMENT_GOT_MILK),
        (try_end),

        (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
        (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
        (val_sub, ":num_cattle", ":random_value"),
        (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
      (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
         (change_screen_return),
         ]),
    ],
  ),


    ("village_take_food_confirm",0,
    "It will be difficult to force and threaten the peasants into giving their precious supplies. You think you will need at least one hour.",
    #TODO: mention looting skill?
    "none",
    [],
    [
      ("village_take_food_confirm",[], "Go ahead.",
       [
         (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
         (change_screen_return),
         ]),
      ("forget_it",[], "Forget it.",[(jump_to_menu, "mnu_village_hostile_action")]),
    ],
  ),

   ("village_take_food",0,
    "The villagers grudgingly bring out what they have for you.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health", "p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health", "$current_town"),
       (assign, ":villagers_party_size", reg0),
       (try_begin),
         (lt, ":player_party_size", 6),
         (ge, ":villagers_party_size", 40),
         (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
         (jump_to_menu, "mnu_village_start_attack"),
       (try_end),
    ],
    [
      ("take_supplies",[], "Take the supplies.",
       [
         (try_begin),
           (party_slot_ge, "$current_town", slot_center_player_relation, -55),
           (try_begin),
             (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (call_script, "script_change_player_relation_with_center", "$current_town", -1),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -3),
           (try_end),
         (try_end),
         (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
         (try_begin),
           (gt,  ":village_lord", 1),
          (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
          (try_end),
         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
         (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
         (val_mul, ":player_party_looting", 3),
         (store_sub, ":random_chance", 70, ":player_party_looting"), #Increases the chance of looting by 3% per skill level
         (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", ":random_chance"),
           (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
         (try_end),

###NPC companion changes begin
         (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),
#NPC companion changes end
#Troop commentary changes begin
          (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", -1, -1),
          (store_faction_of_party, ":village_faction",  "$current_town"),
          (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", ":village_faction", 5),
#Troop commentary changes end

         (jump_to_menu, "mnu_village"),
         (troop_sort_inventory, ":merchant_troop"),
         (change_screen_loot, ":merchant_troop"),
         ]),
      ("let_them_keep_it",[], "Let them keep it.",[(jump_to_menu, "mnu_village")]),
    ],
  ),


   ("village_start_attack",mnf_disable_all_keys|mnf_scale_picture,
    "Some of the angry villagers grab their tools and prepare to resist you. It looks like you'll have a fight on your hands if you continue.",
    "none",
    [
       (set_background_mesh, "mesh_pic_villageriot"),
       (call_script, "script_party_count_members_with_full_health", "p_main_party"),
       (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health", "$current_town"),
       (assign, ":villagers_party_size", reg0),

       (try_begin),
         (gt, ":player_party_size", 25),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (this_or_next|eq, ":villagers_party_size", 0),
         (eq, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_battle_result", 1),
           (store_random_in_range, ":enmity", -30, -15),
           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
           (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
           (gt, ":town_lord", 0),
           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
         (try_end),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (eq, "$g_battle_result", -1),
         (jump_to_menu, "mnu_village_loot_defeat"),
       (try_end),
    ],
    [
      ("village_raid_attack",[], "Charge them.",[
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (try_begin),
            (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
            (gt, ":town_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
          (try_end),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1),
          (set_jump_mission, "mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_village_start_attack"),

          (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
###NPC companion changes begin
          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end

          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),
      ("village_raid_leave",[], "Leave this village alone.",[(change_screen_return)]),
    ],
  ),

   ("village_loot_no_resist",0,
    "The villagers here are few and frightened, and they quickly scatter and run before you. The village is at your mercy.",
    "none",
    [],
    [
      ("village_loot",[], "Plunder the village, then raze it.",
       [
          (call_script, "script_village_set_state", "$current_town", svs_being_raided),
          (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
          (assign, "$g_player_raiding_village", "$current_town"),

          (try_begin),
            (store_faction_of_party, ":village_faction", "$current_town"),
            (store_relation, ":relation", "$players_kingdom", ":village_faction"),
            (ge, ":relation", 0),
            (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
          (try_end),

          #(rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
          # rafi
          (rest_for_hours_interactive, 3, 3, 1),
          # end
          (change_screen_return),
           ]),
		   
      # ("village_loot_kill",[
       # (call_script, "script_party_count_members_with_full_health", "$current_town"),
       # (assign, ":villagers_party_size", reg0),
       # (gt, ":villagers_party_size", 0),
	  # ], "Plunder the village, kill the remaining villagers, then raze it.",
       # [
          # (call_script, "script_village_set_state", "$current_town", svs_being_raided),
          # (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
          # (assign, "$g_player_raiding_village", "$current_town"),

          # (try_begin),
            # (store_faction_of_party, ":village_faction", "$current_town"),
            # (store_relation, ":relation", "$players_kingdom", ":village_faction"),
            # (ge, ":relation", 0),
            # (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
          # (try_end),
		  
          # (jump_to_menu, "mnu_village_start_attack_2"),
          # (rest_for_hours_interactive, 3, 3, 1),
          # (change_screen_return),
           # ]),
      ("village_raid_leave",[], "Leave this village alone.",[(change_screen_return)]),
    ],
  ),
  
  
  
######################## NEW v2.1 - 
   ("village_start_attack_2",mnf_disable_all_keys|mnf_scale_picture,
    "Some of the angry villagers grab their tools and prepare to resist you. It looks like you'll have a fight on your hands if you continue.",
    "none",
    [
       (set_background_mesh, "mesh_pic_villageriot"),
       # (call_script, "script_party_count_members_with_full_health", "p_main_party"),
       # (assign, ":player_party_size", reg0),
       (call_script, "script_party_count_members_with_full_health", "$current_town"),
       (assign, ":villagers_party_size", reg0),

       (try_begin),
         (this_or_next|eq, ":villagers_party_size", 0),
         (eq, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_battle_result", 1),
           (store_random_in_range, ":enmity", -40, -25),
           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
           (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
           (gt, ":town_lord", 0),
           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
         (try_end),
         (jump_to_menu, "mnu_village_loot_no_resist"),
       (else_try),
         (eq, "$g_battle_result", -1),
         (jump_to_menu, "mnu_village_loot_defeat"),
       (try_end),
    ],
    [
      ("village_raid_attack_2",[], "Charge them.",[
          (store_random_in_range, ":enmity", -15, -10),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (try_begin),
            (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
            (gt, ":town_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
            (call_script, "script_change_player_honor", -3),  ### NEW v2.1
          (try_end),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_village_raid_evil", 1),
          (set_jump_mission, "mt_village_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_village_start_attack"),

          (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
###NPC companion changes begin
          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end

          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),
      ("village_raid_leave_2",[], "Leave this village alone.",[(change_screen_return)]),
    ],
  ),
#####################################################################
  
  
   ("village_loot_complete",mnf_disable_all_keys,
    "On your orders your troops sack the village, pillaging everything of any value, and then put the buildings to the torch. From the coins and valuables that are found, you get your share of {reg1} denars.",
    "none",
    [
        (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
        (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
        (val_add, ":number_of_village_raids", 1),
        (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 0, ":number_of_village_raids"),

        (try_begin),
          (ge, ":number_of_village_raids", 3),
          (ge, ":number_of_caravan_raids", 3),
          (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
        (try_end),

        (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
        (try_begin),
          (gt,  ":village_lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
        (try_end),
        (store_random_in_range, ":enmity", -35, -25),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),

        (store_faction_of_party, ":village_faction", "$current_town"),
        # (store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
        (store_relation, ":relation", ":village_faction", "$players_kingdom"),  ######## NEW v3.3
        (try_begin),
          (lt, ":relation", 0),
          (call_script, "script_change_player_relation_with_faction", ":village_faction", -3),
        (try_end),

        (assign, ":money_gained", 50),
        (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
        (store_mul, ":prosperity_of_village_mul_5", ":prosperity", 5),
        (val_add, ":money_gained", ":prosperity_of_village_mul_5"),
        (call_script, "script_troop_add_gold", "trp_player", ":money_gained"),

        (assign, ":morale_increase", 3),
        (store_div, ":money_gained_div_100", ":money_gained", 100),
        (val_add, ":morale_increase", ":money_gained_div_100"),
        (call_script, "script_change_player_party_morale", ":morale_increase"),


        (faction_get_slot, ":faction_morale", ":village_faction",  slot_faction_morale_of_player_troops),
        (store_mul, ":morale_increase_mul_2", ":morale_increase", 200),
        (val_sub, ":faction_morale", ":morale_increase_mul_2"),
        # rafi (faction_set_slot, ":village_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),



#NPC companion changes begin
        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end
        (assign, reg1, ":money_gained"),
      ],
    [
      ("continue",[], "Continue...",
       [
          (jump_to_menu, "mnu_close"),
          (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
          (assign, ":max_cattle", reg0),
          (val_mul, ":max_cattle", 3),
          (val_div, ":max_cattle", 2),
          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
          (val_min, ":max_cattle", ":num_cattle"),
          (val_add, ":max_cattle", 1),
          (store_random_in_range, ":random_value", 0, ":max_cattle"),
          (try_begin),
            (gt, ":random_value", 0),
            (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
            (val_sub, ":num_cattle", ":random_value"),
            (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
          (try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (reset_item_probabilities,100),
          (troop_add_merchandise, "trp_temp_troop",itp_type_goods,45),
          (troop_sort_inventory, "trp_temp_troop"),
          (change_screen_loot, "trp_temp_troop"),
        ]),
    ],
  ),
   ("village_loot_defeat",mnf_scale_picture,
    "Fighting with courage and determination, the villagers manage to hold together and drive off your forces.",
    "none",
    [
        (set_background_mesh, "mesh_pic_villageriot"),
    ],
    [
      ("continue",[], "Continue...",[(change_screen_return)]),
    ],
  ),

   ("village_loot_continue",0,
    "Do you wish to continue looting this village?",
    "none",
    [],
    [
      ("disembark_yes",[], "Yes.",[ (rest_for_hours_interactive, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
                              (change_screen_return),
                              ]),
      ("disembark_no",[], "No.",[(call_script, "script_village_set_state", "$current_town", 0),
                            (party_set_slot, "$current_town", slot_village_raided_by, -1),
                            (assign, "$g_player_raiding_village", 0),
                            (change_screen_return)]),
    ],
  ),


   ("close",0,
    "Nothing.",
    "none",
    [
        (change_screen_return),
      ],
    [],
  ),

  ("town",mnf_enable_hot_keys|mnf_scale_picture,
    "{s10} {s14}^{s11}{s12}{s13}",
    "none",
    [
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
        (store_encountered_party, "$current_town"),
      ## CC
        (try_begin),
          (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
          (ge, ":center_lord", 0),
          (set_fixed_point_multiplier, 100),
          (position_set_x, pos0, 70),
          (position_set_y, pos0, 5),
          (position_set_z, pos0, 75),
          (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":center_lord", pos0),
        (try_end),
      ## CC
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        # (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (store_relation, ":faction_relation", ":encountered_faction", "$players_kingdom"),  ######### NEW v3.3
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", -5),
		  ########## NEW v2.1 - player can help defend against anyone
          # (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          # (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          # (this_or_next | party_slot_eq, "$current_town", slot_town_lord, "trp_player"), # rafi for crusades
          # (lt, ":besieger_party_relation", -5),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),

        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (store_sub, ":encountered_town_no", "$g_encountered_party", towns_begin),
          (set_achievement_stat, ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no", 1),

          (assign, ":there_are_villages_not_visited", 0),
          (try_for_range, ":cur_town", towns_begin, towns_end),
            (store_sub, ":encountered_town_no", ":cur_town", towns_begin),
            (get_achievement_stat, ":town_is_visited", ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no"),
            (eq, ":town_is_visited", 0),
            (assign, ":there_are_villages_not_visited", 1),
          (try_end),

          (try_begin),
            (eq, ":there_are_villages_not_visited", 0),
            (unlock_achievement, ACHIEVEMENT_MIGRATING_COCONUTS),
          (try_end),
        (try_end),

        #Quest menus

        (assign, "$qst_collect_taxes_currently_collecting", 0),

        (try_begin),
          (gt, "$quest_auto_menu", 0),
          (jump_to_menu, "$quest_auto_menu"),
          (assign, "$quest_auto_menu", 0),
        (try_end),

        (try_begin),
          (eq, "$g_town_assess_trade_goods_after_rest", 1),
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu, "mnu_town_trade_assessment"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign, "$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq, "$g_leave_town",1),
          (assign, "$g_leave_town",0),
          (assign, "$g_permitted_to_center",0),
          (leave_encounter),
          (change_screen_return),
        (try_end),

        (str_store_party_name, s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name, s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8, ":center_lord"),
          (str_store_string,s7, "@{s8} of {s9}"),
        (try_end),

        (try_begin),
          (party_slot_eq, "$current_town",slot_party_type, spt_town),

          (str_store_string, s60, s2),

          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
          (try_begin),
            (ge, "$cheat_mode", 1),
            (assign, reg4, ":prosperity",),
            (display_message, "@{!}DEBUG -- Prosperity: {reg4}"),
          (try_end),

          #    (val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
          (val_min, ":str_id", 9),
          (val_add, ":str_id", "str_town_prosperity_0"),
          (str_store_string, s10, ":str_id"),

          (store_div, ":str_id", ":prosperity", 20),
          (val_min, ":str_id", 4),
          (val_add, ":str_id", "str_town_alt_prosperity_0"),

          (str_store_string, s14, ":str_id"),


        (else_try),
          (str_clear, s14),
          (str_store_string,s10, "@You are at {s2}."),
        (try_end),

        (try_begin),
          (party_slot_eq, "$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11, "@ Your own banner flies over the castle gate."),
          (else_try),
            (gt, ":center_lord", -1),
            (troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11, "str__you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate"),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11, "@ You see the banner of {s7} over the castle gate."),
          (else_try),
            ###(str_store_string,s11, "@ This castle seems to belong to no one."),
            (str_store_string,s11, "@ This castle has no garrison."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11, "@ Your own banner flies over the town gates."),
          (else_try),
            (gt, ":center_lord", -1),
            (troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11, "str__the_banner_of_your_wifehusband_s7_flies_over_the_town_gates"),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11, "@ You see the banner of {s7} over the town gates."),
          (else_try),
            ###(str_store_string,s11, "@ The townsfolk here have declared their independence."),
            (str_store_string,s11, "@ This town has no garrison."),
          (try_end),
        (try_end),

        (str_clear, s12),
        (try_begin),
          (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s12, "@{!} {s3} ({reg9})."), ### The number inside the parentheses relates to the text string, and it also looks tidier with the period outside the parentheses. - Khanor
        (try_end),

        (str_clear, s13),
        (try_begin),
          (gt, "$entry_to_town_forbidden",0),
          (str_store_string, s13, "@ You have successfully sneaked in."),
        (else_try),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),

          (str_store_string, s13, "str__the_lord_is_currently_holding_a_feast_in_his_hall"),
        (try_end),

        #forbidden to enter?
        (try_begin),
          (store_time_of_day,reg(12)),
          (ge,reg(12),5),
          (lt,reg(12),21),
          (assign, "$town_nighttime",0),
        (else_try),
          (assign, "$town_nighttime",1),
          (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (str_store_string, s13, "str_town_nighttime"),
        (try_end),

        (try_begin),
          (party_slot_ge, "$current_town", slot_town_has_tournament, 1),
          (neg|is_currently_night),
          (party_set_slot, "$current_town", slot_town_has_tournament, 1),
          (str_store_string, s13, "@{s13} A tournament will be held here soon."),
        (try_end),

        (assign, "$castle_undefended",0),
        (party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq, ":castle_garrison_size",0),
          (assign, "$castle_undefended",1),
        (try_end),

        ##TOM - new
        (call_script, "script_set_town_picture"),
        ],
    [
########################################
      ("castle_castle",
      [
        (party_slot_eq, "$current_town",slot_party_type, spt_castle),

        (eq, "$sneaked_into_town", 0),

        (str_clear, s1),
        (try_begin),
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
          (str_store_string, s1, "str__join_the_feast"),
        (try_end),
        ], "Go to the Lord's hall{s1}.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
		     (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
			 (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
			 (neq, "$g_player_eligible_feast_center_no", "$current_town"),

			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),

			 (neg|check_quest_active, "qst_wed_betrothed"),
			 (neg|check_quest_active, "qst_wed_betrothed_female"),

			 (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut

			 (jump_to_menu, "mnu_cannot_enter_court"),
		   (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),
########################################
      ("join_tournament", 
      [
        (neg|is_currently_night),
        (party_slot_ge, "$current_town", slot_town_has_tournament, 1),
        # (eq, "$freelancer_state", 0),
      ]
       , "Join the tournament.",
       [
           #(call_script, "script_fill_tournament_participants_troop", "$current_town", 1), #tom - this now happens in _town_tournament_start_new
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           #(jump_to_menu, "mnu_town_tournament"),
           (jump_to_menu, "mnu_town_tournament_start_new"),
        ]),
########################################
      ("town_castle",[
          (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (eq, "$entry_to_town_forbidden",0),
          (str_clear, s1),
          (try_begin),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
            (str_store_string, s1, "str__join_the_feast"),
          (try_end),

          ], "Go to the castle{s1}.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
		     (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
				(neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
			 (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
			 (neq, "$g_player_eligible_feast_center_no", "$current_town"),

			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),

			 (neg|check_quest_active, "qst_wed_betrothed"),
			 (neg|check_quest_active, "qst_wed_betrothed_female"),

			 (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut

             (jump_to_menu, "mnu_cannot_enter_court"),
			(else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),
########################################
      ("town_center",
      [
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (this_or_next|eq, "$entry_to_town_forbidden",0),
        (eq, "$sneaked_into_town",1)
      ],
      "Take a walk around the streets.",
       [
         #If the player is fighting his or her way out
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),
           (assign, "$g_mt_mode", tcm_escape),
           (store_faction_of_party, ":town_faction", "$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           #ideally we could alarm troops at locations
           (try_begin),
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #there are 6 guards at day time (no fire ext)
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 2),
               (set_visitors, 26, ":tier_2_troop", 2),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 1),
             (else_try),  #only 4 guards because of night
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 1),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 1),
             (try_end),
           (else_try),
             #if guards have gone to some other important happening at nearby villages, then spawn only 1 guard. (example : fire)
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #only 2 guard because there is a fire at one owned village
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 0),
             (else_try), #only 1 guard because both night and there is a fire at one owned village
               (set_visitors, 25, ":tier_2_troop", 0),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 0),
             (try_end),
           (try_end),
           
           (set_jump_mission, "mt_town_center"),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset
         (else_try),
           (call_script, "script_cf_enter_center_location_bandit_check"),
           #All other circumstances...
         (else_try),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           (assign, "$g_mt_mode", tcm_default),
           (store_faction_of_party, ":town_faction", "$current_town"),

           (try_begin),  
             # (neq, ":town_faction", "fac_player_supporters_faction"), ######### NEW v3.3 - fixed troops not changing when the player took control of a fief
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
             (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (try_end),
             (try_begin), #think about this, should castle guard have to go nearby fire too? If he do not go, killing 2 armored guard is too hard for player. For now he goes too.
               #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
               (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
               (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

               (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
               (set_visitor, 23, ":troop_castle_guard"),
             (try_end),
           (set_visitor, 24, ":troop_prison_guard"),

           (try_begin),
             (gt, ":tier_2_troop", 0),
             (assign,reg0, ":tier_3_troop"),
             (assign,reg1, ":tier_3_troop"),
             (assign,reg2, ":tier_2_troop"),
             (assign,reg3, ":tier_2_troop"),
           (else_try),
             (assign,reg0, "trp_euro_spearman_3"),
             (assign,reg1, "trp_euro_spearman_3"),
             (assign,reg2, "trp_euro_archer_2"),
             (assign,reg3, "trp_euro_spearman_2"),
           (try_end),
           (shuffle_range,0,4),

           (try_begin),
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (set_visitor,25,reg0),
             (set_visitor,26,reg1),
             (set_visitor,27,reg2),
             (set_visitor,28,reg3),
           (try_end),

           (party_get_slot, ":spawned_troop", "$current_town", slot_town_armorer),
           (set_visitor, 9, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_weaponsmith),
           (set_visitor, 10, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_elder),
           (set_visitor, 11, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_horse_merchant),
           (set_visitor, 12, ":spawned_troop"),
           (call_script, "script_init_town_walkers"),
           (set_jump_mission, "mt_town_center"),
           (assign, ":override_state", af_override_horse),
           (try_begin),
             (eq, "$sneaked_into_town", 1), #setup disguise
             (assign, ":override_state", af_override_all),
           (try_end),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
             (eq, "$town_nighttime", 0),
             (set_jump_entry, 1),
           (try_end),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
         (try_end),
         (call_script, "script_ee_set_town_troop_names"),
      ], "Door to the town center."),    
	  
################### NEW v3.5 - tranports player to prison entrance
	  # ("town_center_prison",
      # [
        # (eq, 0, 1), 
        # (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_castle),
        # (party_slot_eq, "$current_town", slot_party_type, spt_town),
        # (this_or_next|eq, "$entry_to_town_forbidden", 0),
        # (eq, "$sneaked_into_town", 1)
      # ],
      # "Go to the prison.",
       # [
         ###########If the player is fighting his or her way out
         # (try_begin),
           # (eq, "$talk_context", tc_prison_break),
           # (assign, "$talk_context", tc_escape),
           # (assign, "$g_mt_mode", tcm_escape),
           # (store_faction_of_party, ":town_faction", "$current_town"),
           # (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
           # (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           # (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
           # (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           # (modify_visitors_at_site, ":town_scene"),
           # (reset_visitors),
           ###########ideally we could alarm troops at locations
           # (try_begin),
             ###########if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             # (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             # (store_current_hours, ":cur_time"),
             # (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             # (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             # (store_time_of_day, ":cur_day_hour"),
             # (try_begin), #there are 6 guards at day time (no fire ext)
               # (ge, ":cur_day_hour", 6),
               # (lt, ":cur_day_hour", 22),
               # (set_visitors, 25, ":tier_2_troop", 2),
               # (set_visitors, 26, ":tier_2_troop", 2),
               # (set_visitors, 27, ":tier_3_troop", 1),
               # (set_visitors, 28, ":tier_4_troop", 1),
             # (else_try),  #only 4 guards because of night
               # (set_visitors, 25, ":tier_2_troop", 1),
               # (set_visitors, 26, ":tier_2_troop", 1),
               # (set_visitors, 27, ":tier_3_troop", 1),
               # (set_visitors, 28, ":tier_4_troop", 1),
             # (try_end),
           # (else_try),
             ###########if guards have gone to some other important happening at nearby villages, then spawn only 1 guard. (example : fire)
             # (store_time_of_day, ":cur_day_hour"),
             # (try_begin), #only 2 guard because there is a fire at one owned village
               # (ge, ":cur_day_hour", 6),
               # (lt, ":cur_day_hour", 22),
               # (set_visitors, 25, ":tier_2_troop", 1),
               # (set_visitors, 26, ":tier_2_troop", 0),
               # (set_visitors, 27, ":tier_3_troop", 1),
               # (set_visitors, 28, ":tier_4_troop", 0),
             # (else_try), #only 1 guard because both night and there is a fire at one owned village
               # (set_visitors, 25, ":tier_2_troop", 0),
               # (set_visitors, 26, ":tier_2_troop", 0),
               # (set_visitors, 27, ":tier_3_troop", 1),
               # (set_visitors, 28, ":tier_4_troop", 0),
             # (try_end),
           # (try_end),
           
           # (set_jump_mission, "mt_town_center"),
           # (jump_to_scene, ":town_scene"),
           # (change_screen_mission),
            ############If you're already at escape, then talk context will reset
         # (else_try),
           # (call_script, "script_cf_enter_center_location_bandit_check"),
           ############All other circumstances...
         # (else_try),
           # (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           # (modify_visitors_at_site, ":town_scene"),
           # (reset_visitors),
           # (assign, "$g_mt_mode", tcm_default),
           # (store_faction_of_party, ":town_faction", "$current_town"),

           # (try_begin),  
             ######## (neq, ":town_faction", "fac_player_supporters_faction"), ######### NEW v3.3 - fixed troops not changing when the player took control of a fief
             # (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             # (faction_get_slot, ":troop_castle_guard", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
             # (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
             # (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           # (try_end),
             # (try_begin), #think about this, should castle guard have to go nearby fire too? If he do not go, killing 2 armored guard is too hard for player. For now he goes too.
               ########if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
               # (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
               # (store_current_hours, ":cur_time"),
             # (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

               # (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
               # (set_visitor, 23, ":troop_castle_guard"),
             # (try_end),
           # (set_visitor, 24, ":troop_prison_guard"),

           # (try_begin),
             # (gt, ":tier_2_troop", 0),
             # (assign,reg0, ":tier_3_troop"),
             # (assign,reg1, ":tier_3_troop"),
             # (assign,reg2, ":tier_2_troop"),
             # (assign,reg3, ":tier_2_troop"),
           # (else_try),
             # (assign,reg0, "trp_euro_spearman_3"),
             # (assign,reg1, "trp_euro_spearman_3"),
             # (assign,reg2, "trp_euro_archer_2"),
             # (assign,reg3, "trp_euro_spearman_2"),
           # (try_end),
           # (shuffle_range,0,4),

           # (try_begin),
             #########if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             # (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             # (store_current_hours, ":cur_time"),
             # (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             # (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             # (set_visitor,25,reg0),
             # (set_visitor,26,reg1),
             # (set_visitor,27,reg2),
             # (set_visitor,28,reg3),
           # (try_end),

           # (party_get_slot, ":spawned_troop", "$current_town", slot_town_armorer),
           # (set_visitor, 9, ":spawned_troop"),
           # (party_get_slot, ":spawned_troop", "$current_town", slot_town_weaponsmith),
           # (set_visitor, 10, ":spawned_troop"),
           # (party_get_slot, ":spawned_troop", "$current_town", slot_town_elder),
           # (set_visitor, 11, ":spawned_troop"),
           # (party_get_slot, ":spawned_troop", "$current_town", slot_town_horse_merchant),
           # (set_visitor, 12, ":spawned_troop"),
           # (call_script, "script_init_town_walkers"),
           # (set_jump_mission, "mt_town_center"),
           # (assign, ":override_state", af_override_horse),
           # (try_begin),
             # (eq, "$sneaked_into_town", 1), #setup disguise
             # (assign, ":override_state", af_override_all),
           # (try_end),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
           # (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
           # (try_begin),
             # (eq, "$town_entered", 0),
             # (assign, "$town_entered", 1),
             # (eq, "$town_nighttime", 0),
             # (set_jump_entry, 24),  ########## NEW v3.5 - to the prison
           # (try_end),
           # (jump_to_scene, ":town_scene"),
           # (change_screen_mission),
         # (try_end),
         # (call_script, "script_ee_set_town_troop_names"),
      # ], "Door to the prison."),
######################################
######################################
      ("town_tavern",[
          (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (this_or_next|eq, "$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1),
#          (party_get_slot, ":scene", "$current_town", slot_town_tavern),
#          (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ]
       , "Visit the tavern.",
       [      
           (try_begin),
             (eq, "$all_doors_locked",1),
             (display_message, "str_door_locked",0xFFFFAAAA),
           (else_try),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_tavern),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),

             (assign, "$talk_context", tc_tavern_talk),
             (call_script, "script_initialize_tavern_variables"),

             (store_random_in_range, ":randomize_attacker_placement", 0, 4),
             # (party_get_slot, ":town_scene", "$current_town", slot_town_center),
             (assign, "$g_mt_mode", tcm_default),
             # (store_faction_of_party, ":town_faction", "$current_town"),

             (assign, "$g_init_fight", 0),
             (modify_visitors_at_site, ":cur_scene"),
             (reset_visitors),
             
             (call_script, "script_init_town_walkers"),
             
             # rafi
             (party_get_slot, ":tavernkeeper", "$current_town", slot_town_tavernkeeper),
             (set_visitor, 9, ":tavernkeeper"),
             # end rafi
             (assign, ":cur_entry", 17),
             
             #whores - tom
             (try_begin),
               (set_visitor, ":cur_entry", "trp_whore"),
               (val_add, ":cur_entry", 1),
             (try_end),
             #whores end

             #this is just a cheat right now
             #(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
             (try_begin),
                (eq, "$cheat_mode", 1),
                (troop_get_slot, ":drunk_location", "trp_belligerent_drunk", slot_troop_cur_center),
                (try_begin),
                    (eq, "$cheat_mode", 0),
                (else_try),
                    (is_between, ":drunk_location", centers_begin, centers_end),
                    (str_store_party_name, s4, ":drunk_location"),
                    (display_message, "str_belligerent_drunk_in_s4"),
                (else_try),
                    (display_message, "str_belligerent_drunk_not_found"),
                (try_end),

                (troop_get_slot, ":promoter_location", "trp_fight_promoter", slot_troop_cur_center),
                (try_begin),
                    (eq, "$cheat_mode", 0),
                (else_try),
                    (is_between, ":promoter_location", centers_begin, centers_end),
                    (str_store_party_name, s4, ":promoter_location"),
                    (display_message, "str_roughlooking_character_in_s4"),
                (else_try),
                    (display_message, "str_roughlooking_character_not_found"),
                (try_end),

             (try_end),

             #this determines whether or not a lord who dislikes you will commission an assassin
             (try_begin),
                (store_current_hours, ":hours"),
                (store_sub, ":hours_since_last_attempt", ":hours", "$g_last_assassination_attempt_time"),
############################## NEW v3.11 - 
                (store_random_in_range, ":random_time", 120, 216),  #### 5 to 9 days
                (gt, ":hours_since_last_attempt", ":random_time"),
                (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
                    (troop_slot_eq, ":lord", slot_troop_is_alive, 1),  ## he's alive/active
                    (try_begin),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
                        (assign, ":negative_relation", -20),
                    (else_try),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_martial),
                        (assign, ":negative_relation", -60),
                    (else_try),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_quarrelsome),
                        (assign, ":negative_relation", -40),
                    (else_try),
                        (this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_cunning),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
                        (assign, ":negative_relation", -30),
                    (else_try),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_upstanding),
                        (assign, ":negative_relation", -75),
                    (else_try),
                        (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
                        (assign, ":negative_relation", -90),
                    (try_end),
                    (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
                    (party_is_active, ":led_party"),
                    # (party_get_attached_to, ":led_party_attached", ":led_party"),
                    # (eq, ":led_party_attached", "$g_encountered_party"),
                    (call_script, "script_troop_get_relation_with_troop", "trp_player", ":lord"),
                    (le, reg0, ":negative_relation"),
                    (assign, "$g_last_assassination_attempt_time", ":hours"),
#                    (assign, "$g_last_assassination_attempt_location", "$g_encountered_party"),
#                    (assign, "$g_last_assassination_attempt_perpetrator", ":lord"),

                    (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
                (try_end),
############################################# 
             (try_end),

             (try_begin),
                 (eq, ":randomize_attacker_placement", 0),
                 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
                 (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
                (eq, 1, 0),
                (troop_slot_eq, "trp_fight_promoter", slot_troop_cur_center, "$current_town"),
                (set_visitor, ":cur_entry", "trp_fight_promoter"),
                (val_add, ":cur_entry", 1),
             (try_end),
       #(call_script, "script_update_mercenary_units_of_towns"),
             (call_script, "script_get_available_mercenary_troop_and_amount_of_center", "$current_town"),
       #(party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
       #(party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
       (assign, ":mercenary_troop", reg0),
       (assign, ":mercenary_amount", reg1),
       (str_store_troop_name, s10, ":mercenary_troop"),
       (assign, reg25, ":mercenary_amount"),
       (try_begin),
               (gt, ":mercenary_troop", 0),
               (gt, ":mercenary_amount", 0),
               (set_visitor, ":cur_entry", ":mercenary_troop"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
                 (eq, ":randomize_attacker_placement", 1),
                 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
                 (val_add, ":cur_entry", 1),
             (try_end),

             #TOM
             # (try_for_range, ":companion_candidate", companions_begin, companions_end),
               # (troop_slot_eq, ":companion_candidate", slot_troop_occupation, 0),
               # (troop_slot_eq, ":companion_candidate", slot_troop_cur_center, "$current_town"),
               # (neg|troop_slot_ge, ":companion_candidate", slot_troop_prisoner_of_party, centers_begin),

               # (set_visitor, ":cur_entry", ":companion_candidate"),
               # (val_add, ":cur_entry", 1),
             # (try_end),
             
             (try_for_range, ":merchant", traders_begin, traders_end),
               (troop_slot_eq, ":merchant", slot_troop_cur_center, "$current_town"),
               (set_visitor, ":cur_entry", ":merchant"),
               (val_add, ":cur_entry", 1),
             (try_end),
             #TOM

             (try_begin),
                 (eq, ":randomize_attacker_placement", 2),
                 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
                 (val_add, ":cur_entry", 1),
             (try_end),

       (try_begin), #this doubles the incidence of ransom brokers and (below) minstrels
         (party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
         (gt, ":ransom_broker", 0),
         (assign, reg20, ":cur_entry"),
         (display_message, "@ransom broker present entry point: {reg20}."),

         (assign, reg0, ":ransom_broker"),
         (assign, reg1, "$current_town"),

         (set_visitor, ":cur_entry", ":ransom_broker"),
         (val_add, ":cur_entry", 1),
             (else_try),
               (is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
               (store_add, ":alternative_town", "$current_town", 9),

               (try_begin),
                (ge, ":alternative_town", towns_end),
                (val_sub, ":alternative_town", 22),
               (try_end),
               (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s3, "$current_town"),
                (str_store_party_name, s4, ":alternative_town"),
                (display_message, "@{!}DEBUG - Current town is {s3}, but also checking {s4}"),
               (try_end),

               (party_get_slot, ":ransom_broker", ":alternative_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),

               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
               (gt, ":tavern_traveler", 0),
               (set_visitor, ":cur_entry", ":tavern_traveler"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
               (gt, ":tavern_minstrel", 0),

               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
             (else_try),
               (store_add, ":alternative_town", "$current_town", 9),
               (try_begin),
                (ge, ":alternative_town", towns_end),
                (val_sub, ":alternative_town", 22),
               (try_end),
               (party_get_slot, ":tavern_minstrel", ":alternative_town", slot_center_tavern_minstrel),
               (gt, ":tavern_minstrel", 0),

               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
               (gt, ":tavern_bookseller", 0),
               (set_visitor, ":cur_entry", ":tavern_bookseller"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
                 (eq, ":randomize_attacker_placement", 3),
                 (call_script, "script_setup_tavern_attacker", ":cur_entry"),
                 (val_add, ":cur_entry", 1),
             (try_end),

             (try_begin),
               (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
               (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
               (assign, ":end_cond", villages_end),
               (try_for_range, ":cur_village", villages_begin, ":end_cond"),
                 (party_slot_eq, ":cur_village", slot_village_bound_center, "$current_town"),
                 (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
                 (neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
                 (set_visitor, ":cur_entry", "trp_farmer_from_bandit_village"),
                 (val_add, ":cur_entry", 1),
                 (assign, ":end_cond", 0),
               (try_end),
             (try_end),
############################ NEW v2.1 - tavern townspeople 
            #dedal begin
            (party_get_slot, ":center_faction", "$current_town", slot_center_original_faction), #dckplmc - tavern patrons same culture as town
            (faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture),
            (faction_get_slot, ":walker_troop_id", ":center_culture", slot_faction_town_walker_male_troop),
            (try_for_range, ":entry",32,41),
                        (store_random_in_range, ":rand",0,2), #dckplmc - randomly male or female
                        (store_add, ":town_walker", ":rand", ":walker_troop_id"),
                        (store_random_in_range, ":dna",0,1000),
                        (mission_tpl_entry_clear_override_items, "mt_town_default", ":entry"),
                        # (store_random_in_range, ":r",0,10),
                        # (try_begin),
                            # (gt, ":r",2),
                            # (mission_tpl_entry_add_override_item, "mt_town_default", ":entry", "itm_dedal_kufel"),
                        # (try_end),
                        (set_visitor, ":entry", ":town_walker", ":dna"),
                        
                        (troop_set_slot, "trp_temp_array_c", ":entry", ":dna"),
                        
            (try_end),
            #dedal end
######################################################################
             (change_screen_mission),
           (try_end),
        ], "Door to the tavern."),
########################################
      ("town_merchant",
       [(party_slot_eq, "$current_town",slot_party_type, spt_town),
           (eq, 1, 0),
           (eq, "$town_nighttime",0),
           (this_or_next|eq, "$entry_to_town_forbidden",0),
           (eq, "$sneaked_into_town",1),
#           (party_get_slot, ":scene", "$current_town", slot_town_store),
#           (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Speak with the merchant.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked",1),
             (eq, "$town_nighttime",1),
             (display_message, "str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),

             (party_get_slot, ":cur_scene", "$current_town", slot_town_store),
             # rafi
             (modify_visitors_at_site, ":cur_scene"),
             (reset_visitors),
             (party_get_slot, ":merchant", "$current_town", slot_town_merchant),
             (set_visitor, 9, ":merchant"),
             # end rafi

             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ], "Door to the shop."),
########################################
      ("town_arena",
       [(party_slot_eq, "$current_town",slot_party_type, spt_town),
        (eq, "$sneaked_into_town", 0),
#           (party_get_slot, ":scene", "$current_town", slot_town_arena),
#           (scene_slot_eq,  ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Enter the arena.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked",1),
             (eq, "$town_nighttime",1),
             (display_message, "str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$g_mt_mode", abm_visit),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_arena_melee_fight"),
             (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
             (modify_visitors_at_site, ":arena_scene"),
             (reset_visitors),
             (try_for_range, ":cur_agent", 0, 39),
                (set_visitor, ":cur_agent", "trp_regular_fighter"),
             (try_end),
             (try_for_range, ":cur_agent", 32, 39),
                (set_visitor, ":cur_agent", "trp_veteran_fighter"),
             (try_end),
             (try_for_range, ":cur_agent", 32, 39),
                (set_visitor, ":cur_agent", "trp_veteran_fighter"),
             (try_end),
             (try_for_range, ":cur_agent", 32, 39),
                (set_visitor, ":cur_agent", "trp_veteran_fighter"),
             (try_end),
             (try_for_range, ":cur_agent", 32, 39),
                (set_visitor, ":cur_agent", "trp_champion_fighter"),
             (try_end),
             # rafi
             (party_get_slot, ":arena_master", "$current_town", slot_town_arena_master),
             (set_visitor, 52, ":arena_master"),
             # end rafi

             (set_visitor, 43, "trp_veteran_fighter"),
             (set_visitor, 44, "trp_regular_fighter"),
             (set_jump_entry, 50),
             (jump_to_scene, ":arena_scene"),
             (scene_set_slot, ":arena_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ], "Door to the arena."),
########################################
      ("town_dungeon",
       [
	   ######## NEW v3.1 - player can enter the prison from the town menu
	   (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
	   (this_or_next|party_slot_eq, "$current_town",slot_party_type, spt_town),
	   (party_slot_eq, "$current_town",slot_party_type, spt_castle),
	   ################
	   ],  
       "Enter the prison.",
       [
           (try_begin),
            (eq, "$talk_context", tc_prison_break),
            (gt, "$g_main_attacker_agent", 0),

               (neg|agent_is_alive, "$g_main_attacker_agent"),

            (agent_get_troop_id, ":agent_type", "$g_main_attacker_agent"),
            (try_begin),
              # (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
              (eq, "$g_encountered_party_faction", "$players_kingdom"),
              (party_get_slot, ":prison_guard_faction", "$current_town", slot_center_original_faction),
            (else_try),
              (assign, ":prison_guard_faction", "$g_encountered_party_faction"),
            (try_end),
            (faction_slot_eq, ":prison_guard_faction", slot_faction_prison_guard_troop, ":agent_type"),

            (call_script, "script_deduct_casualties_from_garrison"),
            (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),

           (else_try),
             (eq, "$all_doors_locked",1),
             (display_message, "str_door_locked",0xFFFFAAAA),
           (else_try),
             (this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (eq, "$g_encountered_party_faction", "$players_kingdom"),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
           (else_try),
             (display_message, "str_door_locked",0xFFFFAAAA),
           (try_end),
        ], "Door to the dungeon."),
########################################
      ("castle_inspect",
      [
         (party_slot_eq, "$current_town",slot_party_type, spt_castle),
      ],
       "Take a walk around the courtyard.",
       [
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),

           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site, ":cur_castle_exterior"),
           (reset_visitors),

           (assign, ":guard_no", 40),

           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
             (this_or_next|eq, ":guard_no", 40),
             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             #nearby fire condition end

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size", "$g_encountered_party", ":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna, ":troop_dna", "$g_encountered_party", ":troop_iterator"),
			 (gt, ":cur_troop_id", 0),  ###### NEW v3.9 - 
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
             (val_add, ":guard_no", 1),
           (try_end),
           #(set_jump_entry, 1),
           (set_visitor, 7, "$g_player_troop"),

           (set_jump_mission, "mt_castle_visit"),
           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset
         (else_try),
           (assign, "$talk_context", tc_town_talk),

           (assign, "$g_mt_mode", tcm_default),

           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site, ":cur_castle_exterior"),
           (reset_visitors),

           (try_begin),
             # (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
             (neq, "$g_encountered_party_faction", "$players_kingdom"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
           (else_try),
             (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
             (faction_get_slot, ":troop_prison_guard", ":town_original_faction", slot_faction_prison_guard_troop),
           (try_end),
             (set_visitor, 24, ":troop_prison_guard"),

           (assign, ":guard_no", 40),

           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
             (neg|is_between, ":cur_time", ":fire_finish_time", ":last_nearby_fire_time"),

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size", "$g_encountered_party", ":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded", "$g_encountered_party", ":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna, ":troop_dna", "$g_encountered_party", ":troop_iterator"),
			 (gt, ":cur_troop_id", 0),  ###### NEW v3.9 - 
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),

             (val_add, ":guard_no", 1),
           (try_end),

           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
           (try_end),
           (set_jump_entry, 1),

           (assign, ":override_state", af_override_horse),
           (try_begin),
             (eq, "$sneaked_into_town", 1), #setup disguise
             (assign, ":override_state", af_override_all),
           (try_end),
           (set_jump_mission, "mt_castle_visit"),

           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 0, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 1, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 2, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 3, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 4, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 5, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 6, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 7, ":override_state"),

           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
         (try_end),
        ], "To the castle courtyard."),
########################################
    # rafi player sally out
      ("castle_player_sally_out",
        [
          (neg | party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
          (neg|troop_is_wounded, "trp_player"),
          (party_get_slot, ":besieger", "$g_encountered_party", slot_center_is_besieged_by),
          (party_is_active, ":besieger"),
          (store_distance_to_party_from_party, ":distance", ":besieger", "$g_encountered_party"),
          (le, ":distance", 7),
          (party_get_battle_opponent, ":opponent", "$g_encountered_party"),
          (lt, ":opponent", 0),
          (party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
          (str_store_troop_name, s11, ":enemy_party_leader"),
          (store_faction_of_troop, ":besieger_faction", ":enemy_party_leader"),
          (store_relation, ":relation", "$players_kingdom", ":besieger_faction"),
          (str_store_party_name, s12, "$current_town"),
          (lt, ":relation", 0),
        ],
        "{s12} is under siege.  Sally out to delay the attackers.",
        [
          (assign, "$auto_enter_town", 0),          
          (party_get_slot, ":besieger", "$g_encountered_party", slot_center_is_besieged_by),
          #(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0), #tom

          (assign, "$g_player_sally_town", "$g_encountered_party"),
          (assign, "$g_player_sallies", ":besieger"),
          (display_message, "@Sally!"),          
          (leave_encounter),
          (change_screen_return),          
        ]),
########################################
    # end rafi
     ("town_enterprise",
      [
        (party_slot_eq, "$current_town",slot_party_type, spt_town),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
        (gt, ":item_produced", 1),
        (eq, "$entry_to_town_forbidden",0),
        (call_script, "script_get_enterprise_name", ":item_produced"),
        (str_store_string, s3, reg0),
      ],
      "Visit your {s3}.",
      [
        (store_sub, ":town_order", "$current_town", towns_begin),
        (store_add, ":master_craftsman", "trp_town_1_master_craftsman", ":town_order"),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
        (assign, ":enterprise_scene", "scn_enterprise_mill"),
        (try_begin),
            (eq, ":item_produced", "itm_bread"),
            (assign, ":enterprise_scene", "scn_enterprise_mill"),
        (else_try),
            (eq, ":item_produced", "itm_ale"),
            (assign, ":enterprise_scene", "scn_enterprise_brewery"),
        (else_try),
            (eq, ":item_produced", "itm_oil"),
            (assign, ":enterprise_scene", "scn_enterprise_oil_press"),
        (else_try),
            (eq, ":item_produced", "itm_wine"),
            (assign, ":enterprise_scene", "scn_enterprise_winery"),
        (else_try),
            (eq, ":item_produced", "itm_leatherwork"),
            (assign, ":enterprise_scene", "scn_enterprise_tannery"),
        (else_try),
            (eq, ":item_produced", "itm_wool_cloth"),
            (assign, ":enterprise_scene", "scn_enterprise_wool_weavery"),
        (else_try),
            (eq, ":item_produced", "itm_linen"),
            (assign, ":enterprise_scene", "scn_enterprise_linen_weavery"),
        (else_try),
            (eq, ":item_produced", "itm_velvet"),
            (assign, ":enterprise_scene", "scn_enterprise_dyeworks"),
        (else_try),
            (eq, ":item_produced", "itm_tools"),
            (assign, ":enterprise_scene", "scn_enterprise_smithy"),
        (try_end),
        (modify_visitors_at_site, ":enterprise_scene"),
        (reset_visitors),
        (set_visitor,0, "trp_player"),
        (set_visitor,17, ":master_craftsman"),
        (set_jump_mission, "mt_town_default"),
        (jump_to_scene, ":enterprise_scene"),
        (change_screen_mission),
      ], "Door to your enterprise."),
########################################
    ## CC
      ("meet_with_guild_master",
       [
           (party_slot_eq, "$current_town",slot_party_type, spt_town)
        ],
         "Meet with the guild master.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (call_script, "script_start_town_conversation", slot_town_elder, 11),
           (try_end),
          ]),
########################################
    ## CC
      ("trade_with_merchants",
       [
           (party_slot_eq, "$current_town",slot_party_type, spt_town)
        ],
         "Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu, "mnu_town_trade"),
           (try_end),
          ]),
############### NEW v3.5
    ## CC
       ("ee_recruits_garrison_options_1",
        [
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
         (assign, ":ok", 0),
		 (store_faction_of_party, ":castle_faction", "$current_town"),
		 (try_begin),
           (eq, ":castle_faction", "$players_kingdom"),
             (assign, ":ok", 1),
		 (else_try),
           (store_relation, ":relation", ":castle_faction", "$players_kingdom"),
           (gt, ":relation", -5),
             (assign, ":ok", 1),
		 (try_end),
         (eq, ":ok", 1),
        ],
         "Recruit and garrison options.",
         [
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       ]),
########################################
      ("walled_center_manage",
      [
####### NEW v3.0-KOMKE below line commented out because it was blocking access to garrison while center is under siege
        # (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (assign, reg0, 1),
        (try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (assign, reg0, 0),
        (try_end),
       ],
       "Manage this {reg0?town:castle}.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_ee_center_manage"),
       ]),
########################################
      ("castle_wait",
       [
        #(party_slot_eq, "$current_town",slot_party_type, spt_castle),
           (this_or_next|ge, "$g_encountered_party_relation", 0),
           (eq, "$castle_undefended",1),
           (assign, ":can_rest", 1),
           (str_clear, s1),
           (try_begin),
             (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
             (neg|party_slot_eq, "$current_town", slot_town_lord, ":player_spouse"),
          (party_slot_ge, "$current_town", slot_town_lord, "trp_player"), #can rest for free in castles and towns with unassigned lords
          (store_faction_of_party, ":current_town_faction", "$current_town"),
          # (neq, ":current_town_faction", "fac_player_supporters_faction"),
          (neq, ":current_town_faction", "$players_kingdom"),  ########### NEW v3.3
             (party_get_num_companions, ":num_men", "p_main_party"),
             (store_div, reg1, ":num_men", 4),
             (val_add, reg1, 1),
             (str_store_string, s1, "@ ({reg1} denars per night)"),
             (store_troop_gold, ":gold", "trp_player"),
             (lt, ":gold", reg1),
             (assign, ":can_rest", 0),
           (try_end),
           (eq, ":can_rest", 1),
        ],
         "Wait here for some time{s1}.",
         [
           (assign, "$auto_enter_town", "$current_town"),
           (assign, "$g_town_visit_after_rest", 1),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),

        (try_begin),
          (party_is_active, "p_main_party"),
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (try_begin),
            (eq, ":cur_terrain", rt_desert),
            (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
          (try_end),
        (try_end),

           #(rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
           # (rest_for_hours_interactive, 24 * 7, 3, 0), #rafi slow this down
           (rest_for_hours_interactive, 24 * 30, 3, 0), #rafi slow this down
           (change_screen_return),
          ]),
########################################

########################################
      ("collect_taxes_qst",
      [
        (check_quest_active, "qst_collect_taxes"),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
      ],
      "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
      [
        (jump_to_menu, "mnu_collect_taxes"),
      ]),
########################################
      ("debug_town_cheat_menus",
      [
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT! Go to menus.",
      [
        (jump_to_menu, "mnu_town_cheat_menus"),
      ]),
########################################
      ("fief_misc_options_menus",
      [
      ],
      "Misc. Options.",
      [
        (jump_to_menu, "mnu_fief_misc_options"),
      ]),
########################################
     ("town_leave",[], "Leave...",
      [
        (assign, "$g_permitted_to_center",0),
        # (change_screen_return,0),
        (change_screen_return),
      ], "Leave Area."),
########################################
    ]
  ),
################################################################################


   ("cannot_enter_court",0,
    # "There is a feast in progress in the lord's hall, but you are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while the feast is in progress...",####### NEW v3.1-KOMKE
    "You are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while a feast is in progress...",####### NEW v3.1-KOMKE
    "none",
    [],
    [
    ("continue", [], "Continue",
       [
        (jump_to_menu, "mnu_town"),
        ]),
    ]),


   ("lady_visit",0,
    "Whom do you wish to visit?",
    "none",
    [],
    [

    ("visit_lady_1", [
    (gt, "$love_interest_in_town", 0),
    (str_store_troop_name, s12, "$love_interest_in_town"),
    ],
      "Visit {s12}",
       [
        (assign, "$love_interest_in_town", "$love_interest_in_town"),
        (jump_to_menu, "mnu_garden"),
        ]),



    ("visit_lady_2", [
    (gt, "$love_interest_in_town_2", 0),
    (str_store_troop_name, s12, "$love_interest_in_town_2"),
    ],
      "Visit {s12}",
       [
        (assign, "$love_interest_in_town", "$love_interest_in_town_2"),
        (jump_to_menu, "mnu_garden"),
        ]),

    ("visit_lady_3", [
    (gt, "$love_interest_in_town_3", 0),
    (str_store_troop_name, s12, "$love_interest_in_town_3"),
    ],
      "Visit {s12}",
       [
        (assign, "$love_interest_in_town", "$love_interest_in_town_3"),
        (jump_to_menu, "mnu_garden")], "Door to the garden."),


    ("visit_lady_4", [(gt, "$love_interest_in_town_4", 0),(str_store_troop_name, s12, "$love_interest_in_town_4"),],
    "Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_4"),(jump_to_menu, "mnu_garden"),]),

    ("visit_lady_5", [(gt, "$love_interest_in_town_5", 0),(str_store_troop_name, s12, "$love_interest_in_town_5"),],
    "Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_5"),(jump_to_menu, "mnu_garden"),]),

    ("visit_lady_6",[(gt, "$love_interest_in_town_6", 0),(str_store_troop_name, s12, "$love_interest_in_town_6"),],
    "Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_6"),(jump_to_menu, "mnu_garden"),]),

    ("visit_lady_7",[(gt, "$love_interest_in_town_7", 0),(str_store_troop_name, s12, "$love_interest_in_town_7"),],
    "Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_7"),(jump_to_menu, "mnu_garden"),]),

    ("visit_lady_8",[(gt, "$love_interest_in_town_8", 0),(str_store_troop_name, s12, "$love_interest_in_town_8"),],
    "Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_8"),(jump_to_menu, "mnu_garden"),]),


    ("leave",[], "Leave",[(jump_to_menu, "mnu_town")]),

    ]
    ),


   ("town_tournament_lost",0,
    "You have been eliminated from the tournament.{s8}",
    "none",
    [
    (str_clear, s8),
    (try_begin),
        (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
            (neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
        (gt, "$g_player_tournament_placement", 4),
        (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
        (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
        (str_store_string, s8, "str__however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle"),
    (try_end),

        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
    ]
  ),

   ("town_tournament_won",mnf_disable_all_keys,
    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name. In addition to honour, fame and glory, you earn a prize of {reg9} denars. {s8}",
    "none",
    [
        (str_store_party_name, s3, "$current_town"),
        (call_script, "script_change_troop_renown", "trp_player", 20),
        (call_script, "script_change_player_relation_with_center", "$current_town", 1),
        (assign, reg9, 5000), #tom was 200
        (add_xp_to_troop, 2500, "trp_player"),
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),
        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
          (gt, "$g_tournament_bet_win_amount", 0),
          (assign, reg8, ":total_win"),
          (str_store_string, s8, "@Moreover, you earn {reg8} denars from the clever bets you placed on yourself..."),
        (try_end),
        (try_begin),
####### NEW v3.1-KOMKE START-
            # (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
            #     (neg|troop_slot_ge, "trp_player", slot_troop_renown, 70),
            # (neg|troop_slot_ge, "trp_player", slot_troop_renown, 145),
            # 
            # (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
            # (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
            # (str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
            (neq, "$players_kingdom", "$g_encountered_party_faction"),
            (assign, "$g_player_eligible_feast_center_no", "$current_town"),
            (str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
####### NEW v3.1-KOMKE END- 
        (try_end),
        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),
        (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
        (call_script, "script_play_victorious_sound"),

        (unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

   ("town_tournament_won_by_another",mnf_disable_all_keys,
    "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
    "none",
    [
      ##tom
      # (call_script, "script_get_num_tournament_participants"),
        # (store_sub, ":needed_to_remove_randomly", reg0, 1),
      # (try_begin),
        # (troop_slot_eq, "trp_tournament_participants", 0, 0), #delete player from the participants
        # (troop_set_slot, "trp_tournament_participants", 0, -1),
        # (val_sub, ":needed_to_remove_randomly", 1),
      # (try_end),
        # (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        # (call_script, "script_sort_tournament_participant_troops"),
        # (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        # (str_store_troop_name, s1, ":winner_troop"),
        # (try_begin),
          # (troop_is_hero, ":winner_troop"),
          # (call_script, "script_change_troop_renown", ":winner_troop", 20),
        # (try_end),
        
        (troop_get_slot, ":wins", "trp_temp_array_c",1),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants",1),
        (try_for_range, reg0, 2, 8),
          (troop_get_slot, ":victories", "trp_temp_array_c",reg0),
          (gt, ":victories", ":wins"),
          (troop_get_slot, ":wins", "trp_temp_array_c",reg0),
          (troop_get_slot, ":winner_troop", "trp_tournament_participants",reg0),
        (try_end),
        (str_store_troop_name, s1, ":winner_troop"),
        ##tom
        (troop_get_type, reg3, ":winner_troop"),
        
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

   ("town_tournament",mnf_disable_all_keys,
    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("tournament_view_participants", [], "View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")], "Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]),
      ("tournament_join_next_fight", [], "Fight in the next round.",
       [
           (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
           (modify_visitors_at_site, ":arena_scene"),
           (reset_visitors),
           #Assuming that there are enough participants for the teams
           (assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
           (try_begin),
             (gt, "$g_player_tournament_placement", 4),
             (assign, "$g_player_eligible_feast_center_no", "$current_town"),
           (try_end),
           (val_add, "$g_tournament_cur_tier", 1),

           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),


           (try_for_range, ":slot_no", 0, 4),#shuffle teams
             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),

           (assign, ":cur_slot", 0),
           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),

             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
             (try_end),
             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),

             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
               (store_mul, ":cur_entry_point", ":cur_team", 8),
               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
               (val_add, ":cur_entry_point", ":entry_offset"),
               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
               (set_visitor, ":cur_entry_point", ":troop_no"),
               (val_add, ":cur_slot", 1),
             (try_end),
           (try_end),

           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),

           (assign, "$g_mt_mode", abm_tournament),

           (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
           (assign, ":town_index_within_faction", 0),
           (assign, ":end_cond", towns_end),
           (try_for_range, ":cur_town", towns_begin, ":end_cond"),
             (try_begin),
               (eq, ":cur_town", "$current_town"),
               (assign, ":end_cond", 0), #break
             (else_try),
               (party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
               (val_add, ":town_index_within_faction", 1),
             (try_end),
           (try_end),
           (store_faction_of_party, ":town_faction", "$current_town"),
           (call_script, "script_raf_aor_faction_to_region", ":town_faction"),
           (try_begin),
             (this_or_next | eq, reg0, region_eastern),
             (this_or_next | eq, reg0, region_balkan),
             (eq, reg0, region_baltic),
             (set_jump_mission, "mt_arena_tournament_fight_foot"),
           (else_try),
             (set_jump_mission, "mt_arena_tournament_fight"),
           (try_end),

           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),
      ("leave_tournament",[], "Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),
    ]
  ),

   ("tournament_withdraw_verify",0,
    "Are you sure you want to withdraw from the tournament?",
    "none",
    [],
    [
      ("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
       [
       (jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
      ("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
       [
       #(jump_to_menu, "mnu_town_tournament"),
       (jump_to_menu, "mnu_town_tournament_new"), #tom
        ]),
    ]
  ),

   ("tournament_bet",0,
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} denars on yourself, and if you win, you will earn {reg2} denars.:} How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [

      ("bet_500_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 500)
                          ],
       "500 denars.",
       [
         (assign, "$temp", 500),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),

      ("bet_250_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 250)
                          ],
       "250 denars.",
       [
         (assign, "$temp", 250),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),

      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 100)
                          ],
       "100 denars.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],
       "50 denars.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 20)
                         ],
       "20 denars.",
       [
         (assign, "$temp", 20),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 10)
                         ],
       "10 denars.",
       [
         (assign, "$temp", 10),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 5)
                        ],
       "5 denars.",
       [
         (assign, "$temp", 5),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("go_back_dot", [], "Go back.",
       [
         #(jump_to_menu, "mnu_town_tournament"),
         (jump_to_menu, "mnu_town_tournament_new"), #tom
        ]),
    ]
  ),

   ("tournament_bet_confirm",0,
    "If you bet {reg1} denars, you will earn {reg2} denars if you win the tournament. Is that all right?",
    "none",
    [
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":win_amount", reg0),
      (val_mul, ":win_amount", "$temp"),
      (val_div, ":win_amount", 100),
      (assign, reg1, "$temp"),
      (assign, reg2, ":win_amount"),
      ],
    [
      ("tournament_bet_accept", [],
       "Go ahead.",
       [
         (call_script, "script_tournament_place_bet", "$temp"),
         #(jump_to_menu, "mnu_town_tournament"),
         (jump_to_menu, "mnu_town_tournament_new"), #tom
         ]),
      ("tournament_bet_cancel", [],
       "Forget it.",
       [
         (jump_to_menu, "mnu_tournament_bet"),
         ]),
    ]
  ),

   ("tournament_participants",0,
    "You ask one of the criers for the names of the tournament participants. They are:^{s11}",
    "none",
    [
        (str_clear, s11),
        (call_script, "script_sort_tournament_participant_troops"),
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_for_range, ":cur_slot", 0, ":num_participants"),
          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
          (str_store_troop_name, s12, ":troop_no"),
          (str_store_string, s11, "@{!}{s11}^{s12}"),
        (try_end),
        ],
    [
      ("go_back_dot", [], "Go back.",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  ###TOM
    ("town_tournament_start_new",0,
####### NEW v3.0-KOMKE START-
    # "Select which type of tournament do you wish to participate in. You can only participate in one of them.",
    "You need 125 renown to fight in tournaments. Only companions can join your team!",####### NEW v3.1-KOMKE
    "none",
    [
        #(set_background_mesh, "mesh_pic_tournament_euro"),
        (assign, "$current_opponent", 0),
    ],
    [
      ("join_one_on_one", [
	  ######### NEW v3.1 - one on one enable but new mission template to use only two handed swords
      (troop_get_slot, ":plyr_renown", "trp_player", slot_troop_renown),
      (ge, ":plyr_renown", 125),
	  ], "Join one on one tournament.",
      [
        (party_set_slot, "$current_town", slot_town_has_tournament, 0),
        (assign, "$tournament_type", 0),
        (call_script, "script_init_tournament_participents", "$current_town"),
        (jump_to_menu, "mnu_town_tournament_new"),
      ]),
      
      ("join_team_on_team", 
      [
        # (try_begin),
          # (store_party_size, ":party_size", "p_main_party"),
          # (lt, ":party_size", 5),
          # (eq, "$freelancer_state", 0),
          # (display_message, "@You do not have five men in your party to form a team!", 0xEA9999),
        # (try_end),
        (troop_get_slot, ":plyr_renown", "trp_player", slot_troop_renown),
        (ge, ":plyr_renown", 125),####### NEW v3.1-KOMKE 200->125 so player can access tournament and enter castle (200 required) if he wins
####### NEW v3.0-KOMKE END- 
      ], "Join team on team tournament.",
      [  
        
        (party_set_slot, "$current_town", slot_town_has_tournament, 0),
        (assign, "$tournament_type", 1),
        (call_script, "script_init_tournament_participents", "$current_town"),
        (jump_to_menu, "mnu_town_tournament_new"),
        #(party_clear, "p_temp_tournament_team1"),
        #(change_screen_exchange_members, 1, "p_temp_tournament_team1"),
      ]),
    
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town"),
       ]
      ),
    ]
  ), 
  
("town_tournament_new",0,
    "{s2}^Current rankings:^ {s1}",
    "none",
    [
      #team-on-team combat, copy back the party
      # (try_begin),
        # (eq, "$current_opponent",0), #the v. begining only
        # (eq, "$tournament_type",1), #team battle!
        ###add the party back to the main
        # (call_script, "script_party_add_party", "p_main_party", "p_temp_tournament_team1"),
        ###add it to the storage
        # (troop_set_slot, "trp_temp_array_b",0, "trp_player"),
        # (try_for_range, reg0, 1, 5),
          # (call_script, "script_get_and_remove_member", "p_temp_tournament_team1"),
          # (try_begin),
            # (gt, reg1, 0),
            # (troop_set_slot, "trp_temp_array_b",reg0,reg1),
          # (else_try),
            # (troop_set_slot, "trp_temp_array_b",reg0,-1),
          # (try_end),
        # (try_end),
      # (try_end),
      
      (set_background_mesh, "mesh_pic_tournament_euro"),
      
      (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
      ##display participents
      (str_clear, s1),
      (try_for_range, reg0, 0, 8),
        (troop_get_slot, ":victories", "trp_temp_array_c",reg0),
        (assign, reg1, ":victories"),
        (store_sub, reg2, "$current_opponent", ":victories"), #lost
        (troop_get_slot, ":participent", "trp_tournament_participants",reg0),
        (str_store_troop_name, s0, ":participent"),
        (try_begin),  #one-on-one
          (eq, "$tournament_type", 0),
          (str_store_string, s1, "@{s1} {s0} wins:{reg1}, losses: {reg2}^"),
        (else_try),  #team-on-team
          (str_store_string, s0, "@{s0}'s team"),
          (str_store_string, s1, "@{s1} {s0}, wins:{reg1}, losses: {reg2}^"),
        (try_end),
      (try_end),
      
      #display next opponent
      (str_store_string, s2, "@The tournament has ended!"),
      (try_begin),
        (lt, "$current_opponent", 7),
        (store_add, ":opponent", "$current_opponent", 1),
        (troop_get_slot, ":participent", "trp_tournament_participants", ":opponent"),
        (str_store_troop_name, s0, ":participent"),
        (str_store_string, s2, "@Your next opponent: {s0}"),
                (try_begin),
          (set_fixed_point_multiplier, 100),
          (position_set_x, pos0, 70),
          (position_set_y, pos0, 5),
          (position_set_z, pos0, 75),
          (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":participent", pos0),
        (try_end),
      (try_end),
      
      (troop_get_slot, ":p_wins", "trp_temp_array_c",0),
      (assign, "$g_player_tournament_placement", ":p_wins"), #tier is based on victories now
    ],
    [
      ("end_tournament", 
      [
        (ge, "$current_opponent", 7),
      ], "The tournament has ended, let's get drunk!",
      [ 
        (troop_get_slot, ":p_wins", "trp_temp_array_c",0),
        (try_for_range, reg0, 1, 8),
          (troop_get_slot, ":victories", "trp_temp_array_c",reg0),
          (gt, ":victories", ":p_wins"),
          (assign, ":p_wins", -1),
        (try_end),
      
        (try_begin), #player lost, you suck
          (eq, ":p_wins", -1),
          (jump_to_menu, "mnu_town_tournament_won_by_another"),
        (else_try), #player won
          (assign, "$g_player_eligible_feast_center_no", "$current_town"), #so player can enter fest
          (jump_to_menu, "mnu_town_tournament_won"),
        (try_end),
      ]),
    
      ("bash_heads", 
      [
        (lt, "$current_opponent", 7),
      ], "Let's go bash some skulls!",
      [  
        
        (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
        (modify_visitors_at_site, ":arena_scene"),
        (reset_visitors),
        
        (val_add, "$current_opponent", 1),
        (call_script, "script_simulate_next_battle", "$current_opponent"), #simulate opponent battles
        (try_begin), #one-on-one
          (eq, "$tournament_type", 0),
          (troop_get_slot, ":opponent", "trp_tournament_participants", "$current_opponent"),
          (set_visitor, 0, "trp_player"),
          (set_visitor, 8, ":opponent"),
        (else_try), #team-on-team
          (eq, "$tournament_type", 1),
          #player
          (set_visitor, 0, "trp_player"),
          (try_for_range, reg0, 1, 5),
            (troop_get_slot, ":opponent", "trp_temp_array_b", reg0),
            (ge, ":opponent", 1),
            (set_visitor, reg0, ":opponent"),
          (try_end),
          #oponnent team
          (store_mul, ":op", "$current_opponent", 5),
          (store_add, ":top", ":op", 5),
          (assign, ":visitor", 8),
          (try_for_range, reg0, ":op", ":top"),
            (troop_get_slot, ":opponent", "trp_temp_array_b", reg0),
            (set_visitor, ":visitor", ":opponent"),
            (val_add, ":visitor", 1),
          (try_end),
        (try_end),
        
        (assign, "$g_mt_mode", abm_tournament),
        (store_faction_of_party, ":fac", "$current_town"),
        (faction_get_slot, ":culture", ":fac",slot_faction_culture),
        (try_begin), 
		############ NEW v3.8 - removed this 
          # (eq, "$tournament_type", 0),
            # (set_jump_mission, "mt_arena_tournament_fight_1vs1"),
        # (else_try),#foot fighting
		########################
          (this_or_next|eq, ":culture", "fac_culture_finnish"),
          (this_or_next|eq, ":culture", "fac_culture_rus"),
          (this_or_next|eq, ":culture", "fac_culture_baltic"),
          (eq, ":culture", "fac_culture_gaelic"),
          (set_jump_mission, "mt_arena_tournament_fight_foot"),
        (else_try),
          (set_jump_mission, "mt_arena_tournament_fight"),
        (try_end),
        (jump_to_scene, ":arena_scene"),
        (change_screen_mission),
      ]),
      
      ("participents", 
      [
        (eq, "$tournament_type", 1), #no need for single troops?
      ], "View the combatants.",
      [
        (jump_to_menu, "mnu_town_tournament_participents"),
      ]),
      
      ("bet", 
      [
        (lt, "$current_opponent", 7),
        (neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier"),
      ], "Place a bet on yourself.",
      [
        (jump_to_menu, "mnu_tournament_bet"),
      ]),
    
      ("leave", [], "No more - I quit!",
       [
        (lt, "$current_opponent", 7),
        (jump_to_menu, "mnu_tournament_withdraw_verify"),
       ]
      ),
    ]
  ), 
  
   ("town_tournament_participents",0,
    "{s0}",
    "none",
    [
        (str_clear, s0),
        (try_for_range, reg0, 0, 8),
          (troop_get_slot, ":participent", "trp_tournament_participants",reg0),
          (str_store_troop_name, s1, ":participent"),
          (store_mul, ":op", 5, reg0),
          (store_add, ":top", ":op", 5),
          (str_clear, s2),
          (try_for_range, reg1, ":op", ":top"),
            (troop_get_slot, ":opponent", "trp_temp_array_b", reg1),
####### NEW v3.0-KOMKE BEGIN-if not enough companions to fill team replace name with empty place
            (try_begin),
              (neq, ":opponent",-1),
                (str_store_troop_name, s3, ":opponent"),
                (str_store_string, s2, "@{s2} {s3};"),
            (else_try),
              (str_store_string, s3, "@Empty place"),
              (str_store_string, s2, "@{s2} {s3};"),
            (try_end),
####### NEW v3.0-KOMKE END-
          (try_end),
          (str_store_string, s0, "@{s0}{s1} team, consisting of: {s2}^"),
        (try_end),
    ],
    [
      ("go_back_dot", [], "I see.",
       [
         (jump_to_menu, "mnu_town_tournament_new"),
       ]
      ),
    ]
  ), 
  ###TOM
  
  
   ("collect_taxes",mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} that collecting taxes from here will take {reg4} days...",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (assign, ":tax_quest_expected_revenue", 3000),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_town),
       (assign, ":tax_quest_expected_revenue", 6000),
     (try_end),

     (try_begin),
       (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
       (store_add, ":max_skill_plus_thirty", ":max_skill", 30),
       (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (store_div, "$qst_collect_taxes_total_hours", 24* 7 * 30, ":max_skill_plus_thirty"),
       (else_try),
         #Village
         (store_div, "$qst_collect_taxes_total_hours", 24 * 3 * 30, ":max_skill_plus_thirty"),
       (try_end),

       (call_script, "script_party_count_fit_for_battle", "p_main_party"),
       (val_add, reg0, 20),
       (val_mul, "$qst_collect_taxes_total_hours", 20),
       (val_div, "$qst_collect_taxes_total_hours", reg0),


       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, "$qst_collect_taxes_total_hours"),
       (store_div, ":menu_begin_time", "$qst_collect_taxes_total_hours", 20),#between %5-%25
       (store_div, ":menu_end_time", "$qst_collect_taxes_total_hours", 4),
       (assign, ":unrest_begin_time", ":menu_end_time"),#between %25-%75
       (store_mul, ":unrest_end_time", "$qst_collect_taxes_total_hours", 3),
       (val_div, ":unrest_end_time", 4),

       (val_mul, ":tax_quest_expected_revenue", 2),
       (store_div, "$qst_collect_taxes_hourly_income", ":tax_quest_expected_revenue", "$qst_collect_taxes_total_hours"),

       (store_random_in_range, "$qst_collect_taxes_menu_counter", ":menu_begin_time", ":menu_end_time"),
       (store_random_in_range, "$qst_collect_taxes_unrest_counter", ":unrest_begin_time", ":unrest_end_time"),
       (assign, "$qst_collect_taxes_halve_taxes", 0),
     (try_end),
     (quest_get_slot, ":target_hours", "qst_collect_taxes", slot_quest_target_amount),
     (store_div, ":target_days", ":target_hours", 24),
     (val_mul, ":target_days", 24),
     (try_begin),
       (lt, ":target_days", ":target_hours"),
       (val_add, ":target_days", 24),
     (try_end),
     (val_div, ":target_days", 24),
     (assign, reg4, ":target_days"),
     ],
    [
      ("start_collecting", [], "Start collecting.",
       [(assign, "$qst_collect_taxes_currently_collecting", 1),
        (try_begin),
          (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 1),
        (try_end),
        (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
        (assign, "$auto_enter_town", "$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("collect_later", [], "Put it off until later.",
       [(try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
        ]),
    ]
  ),

   ("collect_taxes_complete",mnf_disable_all_keys,
    "You've collected {reg3} denars in taxes from {s3}. {s19} will be expecting you to take the money to him.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s19, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (try_begin),
       (eq, "$qst_collect_taxes_halve_taxes", 0),
       (call_script, "script_change_player_relation_with_center", "$current_town", -2),
     (try_end),
     (call_script, "script_succeed_quest", "qst_collect_taxes"),
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_return),
        ]),
    ]
  ),

   ("collect_taxes_rebels_killed",0,
    "Your quick action and strong arm have successfully put down the revolt. Surely, anyone with a mind to rebel against you will think better of it after this.",
    "none",
    [
    ],
    [
      ("continue", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

   ("collect_taxes_failed",mnf_disable_all_keys,
    "You could collect only {reg3} denars as tax from {s3} before the revolt broke out. {s1} won't be happy, but some silver will placate him better than nothing at all...",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s1, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (call_script, "script_fail_quest", "qst_collect_taxes"),
     (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
     (rest_for_hours, 0, 0, 0), #stop resting
     ],
    [
      ("continue", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

   ("collect_taxes_revolt_warning",0,
    "The people of {s3} are outraged at your demands and decry it as nothing more than extortion. They're getting very restless, and they may react badly if you keep pressing them.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("continue_collecting_taxes", [], "Ignore them and continue.",
       [(change_screen_return),]),
      ("halve_taxes", [(quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                       (str_store_troop_name, s1, ":quest_giver_troop"),],
       "Agree to reduce your collection by half. ({s1} may be upset)",
       [(assign, "$qst_collect_taxes_halve_taxes", 1),
        (change_screen_return),
        ]),
    ]
  ),

   ("collect_taxes_revolt",0,
    "You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?peasants:townsmen} is marching nearer, shouting about the exorbitant taxes and waving torches and weapons. It looks like they aim to fight you!",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (assign, reg9, 0),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_village),
       (assign, reg9, 1),
     (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(set_jump_mission, "mt_back_alley_revolt"),
        (quest_get_slot, ":target_center", "qst_collect_taxes", slot_quest_target_center),
        (try_begin),
          (party_slot_eq, ":target_center", slot_party_type, spt_town),
          (party_get_slot, ":town_alley", ":target_center", slot_town_alley),
        (else_try),
          (party_get_slot, ":town_alley", ":target_center", slot_castle_exterior),
        (try_end),
        (modify_visitors_at_site, ":town_alley"),
        (reset_visitors),
        (assign, ":num_rebels", 6),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 5),
        (val_add, ":num_rebels", ":level"),
        (set_visitors, 1, "trp_tax_rebel", ":num_rebels"),
        (jump_to_scene, ":town_alley"),
        (change_screen_mission),
        ]),
    ]
  ),

# They must learn field discipline and the steadiness to follow orders in combat before they can be thought to use arms.",
   ("train_peasants_against_bandits",0,
    "As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (store_sub, ":needed_hours", 20, ":max_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (store_sub, reg4, ":needed_hours", "$qst_train_peasants_against_bandits_num_hours_trained"),
     ],
    [
      ("make_preparation", [], "Train them.",
       [
         (assign, "$qst_train_peasants_against_bandits_currently_training", 1),
         (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (change_screen_return),
         ]),
      ("train_later", [], "Put it off until later.",
       [
         (jump_to_menu, "mnu_village"),
        ]),
    ]
  ),

   ("train_peasants_against_bandits_ready",0,
    "You put the peasants through the basics of soldiering, discipline and obedience. You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice.",
    "none",
    [
      (store_character_level, ":level", "trp_player"),
      (val_div, ":level", 10),
      (val_add, ":level", 1),
      (quest_get_slot, ":quest_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
      (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
      (val_sub, ":quest_target_amount", ":quest_current_state"),
      (assign, ":max_random", ":level"),
      (val_min, ":max_random", ":quest_target_amount"),
      (val_add, ":max_random", 1),
      (store_random_in_range, ":random_number", 1, ":max_random"),
      (assign, "$g_train_peasants_against_bandits_num_peasants", ":random_number"),
      (assign, reg0, ":random_number"),
      (store_sub, reg1, ":random_number", 1),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", ":random_number"),
     ],
    [
      ("peasant_start_practice", [], "Start the practice fight.",
       [
         (set_jump_mission, "mt_village_training"),
         (quest_get_slot, ":target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
         (party_get_slot, ":village_scene", ":target_center", slot_castle_exterior),
         (modify_visitors_at_site, ":village_scene"),
         (reset_visitors),
         (set_visitor, 0, "trp_player"),
         (set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
         (set_jump_entry, 11),
         (jump_to_scene, ":village_scene"),
         (jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
         (music_set_situation, 0),
         (change_screen_mission),
         ]),
      ]
    ),

   ("train_peasants_against_bandits_training_result",mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
      (try_begin),
        (eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
        (str_store_string, s0, "@You were beaten. The peasants are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
      (else_try),
        (str_store_string, s0, "@After beating your last opponent, you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
        (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
        (val_add, ":quest_current_state", "$g_train_peasants_against_bandits_num_peasants"),
        (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":quest_current_state"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [
         (try_begin),
           (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
           (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":quest_current_state"),
           (jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
         (else_try),
           (change_screen_map),
         (try_end),
         ]),
      ]
    ),

   ("train_peasants_against_bandits_attack",0,
    "As you get ready to continue the training, a sentry from the village runs up to you, shouting alarums. The bandits have been spotted on the horizon, riding hard for {s3}. The elder begs that you organize your newly-trained militia and face them.",
    "none",
    [
    (str_store_party_name, s3, "$current_town"),
     ],
    [
      ("peasants_against_bandits_attack_resist", [], "Prepare for a fight!",
       [
        (store_random_in_range, ":random_no", 0, 3),
        (try_begin),
          (eq, ":random_no", 0),
          (assign, ":bandit_troop", "trp_bandit"),
        (else_try),
          (eq, ":random_no", 1),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
        (else_try),
          (assign, ":bandit_troop", "trp_forest_bandit"),
        (try_end),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 2),
        (store_add, ":min_bandits", ":level", 16),
        (store_add, ":max_bandits", ":min_bandits", 6),
        (store_random_in_range, ":random_no", ":min_bandits", ":max_bandits"),
        (set_visitors, 0, ":bandit_troop", ":random_no"),
        (assign, ":num_villagers", ":max_bandits"),
        (set_visitors, 2, "trp_trainee_peasant", ":num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission, "mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
    ),

   ("train_peasants_against_bandits_attack_result",mnf_scale_picture|mnf_disable_all_keys,
    "{s9}",
    "none",
    [
      (try_begin),
        (eq, "$g_battle_result", 1),
        (str_store_string, s9, "@The bandits are broken! Those few who remain alive and conscious run off with their tails between their legs, terrified of the peasants and their new champion."),
    (call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
        (jump_to_menu, "mnu_train_peasants_against_bandits_success"),
      (else_try),
        (call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
        (str_store_string, s9, "@Try as you might, you could not defeat the bandits. Infuriated, they raze the village to the ground to punish the peasants, and then leave the burning wasteland behind to find greener pastures to plunder."),
        (set_background_mesh, "mesh_pic_looted_village"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(try_begin),
          (call_script, "script_village_set_state",  "$current_town", svs_looted),
          (party_set_slot, "$current_town", slot_village_raid_progress, 0),
          (party_set_slot, "$current_town", slot_village_recover_progress, 0),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
          (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
        (try_end),
        (change_screen_map),
     ]),
      ]
    ),

    ("train_peasants_against_bandits_success",mnf_disable_all_keys,
    "The bandits are broken! Those few who remain run off with their tails between their legs, terrified of the peasants and their new champion. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find to show their gratitude.",
    "none",
    [(party_clear, "p_temp_party"),
     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
     (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
    ],
    [
      ("village_bandits_defeated_accept",[], "Take it as your just due.",[(jump_to_menu, "mnu_auto_return_to_map"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[
      (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
      (call_script, "script_change_player_honor", 1),
      (change_screen_map)]),
    ],
  ),


   ("disembark",0,
    "Do you wish to disembark?",
    "none",
    [],
    [
      ("disembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_normal),
        (party_set_flags, "p_main_party", pf_is_ship, 0),
        (party_get_position, pos1, "p_main_party"),
        (party_set_position, "p_main_party", pos0),
        (try_begin),
          (le, "$g_main_ship_party", 0),
          (set_spawn_radius, 0),
          (spawn_around_party, "p_main_party", "pt_none"),
          (assign, "$g_main_ship_party", reg0),
          (party_set_flags, "$g_main_ship_party", pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship, 1),
          (str_store_troop_name, s1, "trp_player"),
          (party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
          (party_set_icon, "$g_main_ship_party", "icon_ship"),
          (party_set_slot, "$g_main_ship_party", slot_party_type, spt_ship),
        (try_end),
        (enable_party, "$g_main_ship_party"),
        (party_set_position, "$g_main_ship_party", pos0),
        (party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),
      ("disembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

   ("ship_reembark",0,
    "Do you wish to embark?",
    "none",
    [],
    [
      ("reembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", "$g_encountered_party"),
        (disable_party, "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("reembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

   ("center_reports",0,
    "Town Name: {s1}^Rent Income: {reg1} denars^Tariff Income: {reg2} denars^Food Stock: for {reg3} days",
    "none",
    [(party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
     (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
     (assign, ":food_consumption", reg0),
     (try_begin),
       (gt, ":food_consumption", 0),
       (store_div, reg3, ":town_food_store", ":food_consumption"),
     (else_try),
       (assign, reg3, 9999),
     (try_end),
     (str_store_party_name, s1, "$g_encountered_party"),
     (party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
     (party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs),
     ],
    [
      ("to_price_and_productions", [], "Show prices and productions.",
       [(jump_to_menu, "mnu_price_and_production"),
        ]),

      ("go_back_dot",[], "Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),

   ("price_and_production",0,
    "Productions are:^(Note: base/modified by raw materials/modified by materials plus prosperity)^{s1}^^Price factors are:^{s2}",
    "none",
    [

     (assign, ":calradian_average_urban_hardship", 0),
     (assign, ":calradian_average_rural_hardship", 0),

     (try_for_range, ":center", towns_begin, towns_end),
        (call_script, "script_center_get_goods_availability", ":center"),
        (val_add, ":calradian_average_urban_hardship", reg0),
     (try_end),

     (try_for_range, ":center", villages_begin, villages_end),
        (call_script, "script_center_get_goods_availability", ":center"),
        (val_add, ":calradian_average_rural_hardship", reg0),
     (try_end),

     (val_div, ":calradian_average_rural_hardship", 110),
     (val_div, ":calradian_average_urban_hardship", 22),



     (call_script, "script_center_get_goods_availability", "$g_encountered_party"),

     (assign, reg1, ":calradian_average_urban_hardship"),
     (assign, reg2, ":calradian_average_rural_hardship"),

     (try_begin),
        (ge, "$cheat_mode", 1),
        (str_store_string, s1, "str___hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__"),
        (display_message, "@{!}DEBUG - {s1}"),
     (try_end),


     (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
       (neq, ":cur_good", "itm_pork"), #tied to price of grain
       (neq, ":cur_good", "itm_chicken"), #tied to price of grain
       (neq, ":cur_good", "itm_butter"), #tied to price of cheese
       (neq, ":cur_good", "itm_cattle_meat"),
       (neq, ":cur_good", "itm_cabbages"), #possibly include later

       (call_script, "script_center_get_production", "$g_encountered_party", ":cur_good"),
       (assign, ":production", reg0),
       (assign, ":base_production", reg2),
       (assign, ":base_production_modded_by_raw_materials", reg1),

       (call_script, "script_center_get_consumption", "$g_encountered_party", ":cur_good"),
       (assign, ":consumer_consumption", reg2),
       (assign, ":raw_material_consumption", reg1),
       (assign, ":consumption", reg0),

       (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
       (party_get_slot, ":price", "$g_encountered_party", ":cur_good_price_slot"),


       (assign, ":total_centers", 0),
       (assign, ":calradian_average_price", 0),
       (assign, ":calradian_average_production", 0),
       (assign, ":calradian_average_consumption", 0),


       (try_for_range, ":center", centers_begin, centers_end),
        (neg|is_between, ":center", castles_begin, castles_end),
        (val_add, ":total_centers", 1),
        (call_script, "script_center_get_production", ":center", ":cur_good"),
        (assign, ":center_production", reg2),
        (call_script, "script_center_get_consumption", ":center", ":cur_good"),
        (store_add, ":center_consumption", reg1, reg2),

        (party_get_slot, ":center_price", ":center", ":cur_good_price_slot"),
        (val_add, ":calradian_average_price", ":center_price"),
        (val_add, ":calradian_average_production", ":center_production"),
        (val_add, ":calradian_average_consumption", ":center_consumption"),
       (try_end),

       (assign, ":calradian_total_production", ":calradian_average_production"),
       (assign, ":calradian_total_consumption", ":calradian_average_consumption"),

       (val_div, ":calradian_average_price", ":total_centers"),
       (val_div, ":calradian_average_production", ":total_centers"),
       (val_div, ":calradian_average_consumption", ":total_centers"),


       (str_store_item_name, s3, ":cur_good"),

       (assign, reg1, ":base_production"),
       (assign, reg2, ":base_production_modded_by_raw_materials"),
       (assign, reg3, ":production"),
       (assign, reg4, ":price"),

       (assign, reg5, ":calradian_average_production"),
       (assign, reg6, ":calradian_average_price"),

       (assign, reg7, ":consumer_consumption"),
       (assign, reg8, ":raw_material_consumption"),
       (assign, reg9, ":consumption"),

       (assign, reg10, ":calradian_average_consumption"),

       (item_get_slot, ":production_slot", ":cur_good", slot_item_production_slot),
       (party_get_slot, ":production_number", "$g_encountered_party", ":production_slot"),
       (assign, reg11, ":production_number"),
       (assign, reg12, ":calradian_total_production"),
       (assign, reg13, ":calradian_total_consumption"),

       (item_get_slot, ":production_string", ":cur_good", slot_item_production_string),
       (str_store_string, s4, ":production_string"),

       (str_store_string, s1, "str___s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_"),



     (try_end),


     ],
    [
      ("go_back_dot",[], "Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),

   ("town_trade",0,
    "You head towards the marketplace.",
    "none",
    [],

    [
      ## CC
      ("auto_sell",[],
       "Sell items automatically.",
       [
          (assign, "$g_next_menu", "mnu_town"),
          (jump_to_menu, "mnu_trade_auto_sell_begin"),
        ]),
      ## CC
      ("assess_prices",[
         (store_faction_of_party, ":current_town_faction", "$current_town"),
         # (store_relation, ":reln", ":current_town_faction", "fac_player_supporters_faction"),
         (store_relation, ":reln", ":current_town_faction", "$players_kingdom"),  ######## NEW v3.3
         (ge, ":reln", 0),
         ],
       "Assess the local prices.",
       [
           (jump_to_menu, "mnu_town_trade_assessment_begin"),
        ]),
      ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_town_weaponsmith, 1)],
       "Trade with the arms merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_weaponsmith),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_town_armorer, 1)],
       "Trade with the armor merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_armorer),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_town_horse_merchant, 1)],
       "Trade with the horse merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_horse_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_town_merchant, 1)],
       "Trade with the goods merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ## CC
      ("auto_buy_food",[],
       "Buy food automatically.",
       [
          (assign, "$g_next_menu", "mnu_town"),
          (jump_to_menu, "mnu_trade_auto_buy_food_begin"),
        ]),
      ## CC
      ("back_to_town_menu",[], "Head back.",
       [
           (jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

## CC
   ("trade_auto_sell_begin",0,
    "Items in the inventory of companions which selected as the type for sell and their prices below {reg1} denars will be sold to {reg2?all merchants:the elder} in current {reg2?town:village} automatically. Specifically foods, trade goods and books will never be sold.\
^^You can change some settings here freely. ",
    "none",
    [
    (assign, reg1, "$g_auto_sell_price_limit"),
    (try_begin),
      (is_between, "$current_town", towns_begin, towns_end),
      (assign, reg2, 1),
    (else_try),
      (assign, reg2, 0),
    (try_end),
    ],

    [
      ("continue",[], "Continue...",
       [
      (try_begin),
        (is_between, "$current_town", towns_begin, towns_end),
        (party_get_slot, ":town_weaponsmith", "$current_town", slot_town_weaponsmith),
        (party_get_slot, ":town_armorer", "$current_town", slot_town_armorer),
        (party_get_slot, ":town_horse_merchant", "$current_town", slot_town_horse_merchant),
        (party_get_slot, ":town_merchant", "$current_town", slot_town_merchant),
      (else_try),
        (is_between, "$current_town", villages_begin, villages_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
      (try_end),

      (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
      (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
        (is_between, ":stack_troop", companions_begin, companions_end),
        (store_free_inventory_capacity, ":begin_space", ":stack_troop"),
        (store_troop_gold, ":begin_gold", ":stack_troop"),
        (try_begin),
          (is_between, "$current_town", towns_begin, towns_end),
          (call_script, "script_auto_sell", ":stack_troop", ":town_weaponsmith"),
          (call_script, "script_auto_sell", ":stack_troop", ":town_armorer"),
          (call_script, "script_auto_sell", ":stack_troop", ":town_horse_merchant"),
          (call_script, "script_auto_sell", ":stack_troop", ":town_merchant"),
        (else_try),
          (is_between, "$current_town", villages_begin, villages_end),
          (call_script, "script_auto_sell", ":stack_troop", ":merchant_troop"),
        (try_end),
        (store_free_inventory_capacity, ":end_space", ":stack_troop"),
        (store_troop_gold, ":end_gold", ":stack_troop"),
        (neq, ":end_gold", ":begin_gold"),
        (store_sub, ":gained_gold", ":end_gold", ":begin_gold"),
        (set_show_messages, 0),
        (troop_remove_gold, ":stack_troop", ":gained_gold"),
        (troop_add_gold, "trp_player", ":gained_gold"),
        (set_show_messages, 1),
        (store_sub, reg1, ":end_space", ":begin_space"),
        (assign, reg2, ":gained_gold"),
        (store_sub, reg3, reg1, 1),
        (store_sub, reg4, reg2, 1),
        (str_store_troop_name, s1, ":stack_troop"),
        (display_message, "@{s1} have sold {reg1} {reg3?items:item} and you gained {reg2} {reg4?denars:denar}."),
      (try_end),
      (jump_to_menu, "$g_next_menu"),
        ]),
    ("change_settings",[], "Change settings.",[(start_presentation, "prsnt_auto_sell_options"),]),
    ("go_back",[], "Go back.",[(jump_to_menu, "$g_next_menu")]),
  ]
  ),

   ("trade_auto_buy_food_begin",0,
    "You will buy any food which you don't have for one portion automatically. Do you want to continue?",
    "none", [],
  [
    ("continue",[], "Continue...",
    [
      # rafi
      (assign, ":max_amount", 0),
      # end

      (try_begin),
        (is_between, "$current_town", towns_begin, towns_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
      (else_try),
        (is_between, "$current_town", villages_begin, villages_end),
        (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
      (try_end),

      (store_troop_gold, ":begin_gold", "trp_player"),
      (store_free_inventory_capacity, ":begin_space", "trp_player"),
      (set_show_messages, 0),
      (troop_get_inventory_capacity, ":inv_cap", ":merchant_troop"),
      (try_for_range, ":i_slot", 10, ":inv_cap"),
        (troop_get_inventory_slot, ":item", ":merchant_troop", ":i_slot"),
        (gt, ":item", -1),
        (is_between, ":item", food_begin, food_end),
        (troop_inventory_slot_get_item_amount, ":amount", ":merchant_troop", ":i_slot"),
        (troop_inventory_slot_get_item_max_amount, ":max_amount", ":merchant_troop", ":i_slot"),
        (eq, ":amount", ":max_amount"),
        (neg|player_has_item, ":item"),
        (store_free_inventory_capacity, ":free_inv_cap", "trp_player"),
        (gt, ":free_inv_cap", 0),

        (call_script, "script_game_get_item_buy_price_factor", ":item"),
        (assign, ":buy_price_factor", reg0),
        (store_item_value, ":score", ":item"),
        (val_mul, ":score", ":buy_price_factor"),
        (val_div, ":score", 100),
        (val_max, ":score",1),
        (store_troop_gold, ":player_gold", "trp_player"),
        (ge, ":player_gold", ":score"),

        (troop_add_item, "trp_player", ":item"),
        (troop_set_inventory_slot, ":merchant_troop", ":i_slot", -1),
        (troop_remove_gold, "trp_player", ":score"),
        (troop_add_gold, ":merchant_troop", ":score"),
      (try_end),
      (set_show_messages, 1),
      (store_troop_gold, ":end_gold", "trp_player"),
      (store_free_inventory_capacity, ":end_space", "trp_player"),
      (try_begin),
        (neq, ":end_gold", ":begin_gold"),
        (store_sub, reg1, ":begin_gold", ":end_gold"),
        (store_sub, reg2, ":begin_space", ":end_space"),
        (store_sub, reg3, reg1, 1),
        (store_sub, reg4, reg2, 1),
        (display_message, "@You have bought {reg2} {reg4?kinds:kind} of food and lost {reg1} {reg3?denars:denar}."),
      (try_end),

      (jump_to_menu, "$g_next_menu"),
      ]),
    ("go_back",[], "Go back.",[(jump_to_menu, "$g_next_menu")]),
    ]
  ),
## CC

  (
   "town_trade_assessment_begin",0,
   #"You overhear the following details about the roads out of town :^(experimental feature -- this may go into dialogs)^{s42}^You also overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
   "You overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
    "none",
    [
    (str_clear, s42),
##    (call_script, "script_merchant_road_info_to_s42", "$g_encountered_party"),

    ],

    [
      ("continue",[], "Continue...",
       [
           (assign, "$auto_enter_town", "$current_town"),
           (assign, "$g_town_assess_trade_goods_after_rest", 1),
           (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
           (val_div, reg0, 2),
           (store_sub, ":num_hours", 6, reg0),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),
           (rest_for_hours, ":num_hours", 5, 0), #rest while not attackable
           (change_screen_return),
        ]),
      ("go_back_dot",[], "Go back.",
       [
           (jump_to_menu, "mnu_town_trade"),
       ]),
    ]
  ),

   ("town_trade_assessment",mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),

     (assign, ":num_best_results", 0),
     (assign, ":best_result_1_item", -1),
     (assign, ":best_result_1_town", -1),
     (assign, ":best_result_1_profit", 0),
     (assign, ":best_result_2_item", -1),
     (assign, ":best_result_2_town", -1),
     (assign, ":best_result_2_profit", 0),
     (assign, ":best_result_3_item", -1),
     (assign, ":best_result_3_town", -1),
     (assign, ":best_result_3_profit", 0),

     (store_sub, ":num_towns", towns_end, towns_begin),
     (store_sub, ":num_goods", trade_goods_end, trade_goods_begin),
     (store_mul, ":max_iteration", ":num_towns", ":num_goods"),
     (val_mul, ":max_iteration", ":max_skill"),
     (val_div, ":max_iteration", 20),

     (assign, ":org_encountered_party", "$g_encountered_party"),

     (try_for_range, ":unused", 0, ":max_iteration"),
       (store_random_in_range, ":random_trade_good", trade_goods_begin, trade_goods_end),
       (store_random_in_range, ":random_town", towns_begin, towns_end),
       (assign, ":already_best", 0),
       (try_begin),
         (eq, ":random_trade_good", ":best_result_1_item"),
         (eq, ":random_town", ":best_result_1_town"),
         (val_add, ":already_best", 1),
       (else_try),
         (eq, ":random_trade_good", ":best_result_2_item"),
         (eq, ":random_town", ":best_result_2_town"),
         (val_add, ":already_best", 1),
       (else_try),
         (eq, ":random_trade_good", ":best_result_3_item"),
         (eq, ":random_town", ":best_result_3_town"),
         (val_add, ":already_best", 1),
       (try_end),
       (eq, ":already_best", 0),
       (store_item_value, ":random_trade_good_price", ":random_trade_good"),
       (assign, "$g_encountered_party", ":org_encountered_party"),
       (call_script, "script_game_get_item_buy_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_buy_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_buy_price", 100),
       (val_max, ":random_trade_good_buy_price", 1),
       (assign, "$g_encountered_party", ":random_town"),
       (call_script, "script_game_get_item_sell_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_sell_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_sell_price", 100),
       (val_max, ":random_trade_good_sell_price", 1),
       (store_sub, ":difference", ":random_trade_good_sell_price", ":random_trade_good_buy_price"),
       (try_begin),
         (gt, ":difference", ":best_result_1_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":best_result_1_item"),
         (assign, ":best_result_2_town", ":best_result_1_town"),
         (assign, ":best_result_2_profit", ":best_result_1_profit"),
         (assign, ":best_result_1_item", ":random_trade_good"),
         (assign, ":best_result_1_town", ":random_town"),
         (assign, ":best_result_1_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_2_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":random_trade_good"),
         (assign, ":best_result_2_town", ":random_town"),
         (assign, ":best_result_2_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_3_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":random_trade_good"),
         (assign, ":best_result_3_town", ":random_town"),
         (assign, ":best_result_3_profit", ":difference"),
       (try_end),
     (try_end),

     (assign, "$g_encountered_party", ":org_encountered_party"),

     (str_clear, s3),

     (assign, reg2, ":max_skill"),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (try_begin),
       (le, ":num_best_results", 0),
       (str_store_string, s2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
     (else_try),
       (try_begin),
         (ge, ":best_result_3_item", 0),
         (assign, reg6, ":best_result_3_profit"),
         (str_store_item_name, s4, ":best_result_3_item"),
         (str_store_party_name, s5, ":best_result_3_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_2_item", 0),
         (assign, reg6, ":best_result_2_profit"),
         (str_store_item_name, s4, ":best_result_2_item"),
         (str_store_party_name, s5, ":best_result_2_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_1_item", 0),
         (assign, reg6, ":best_result_1_profit"),
         (str_store_item_name, s4, ":best_result_1_item"),
         (str_store_party_name, s5, ":best_result_1_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (str_store_string, s2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
     (try_end),
     ],
    [
      ("continue",[], "Continue...",
       [
           (jump_to_menu, "mnu_town_trade"),
        ]),
    ]
  ),




   ("sneak_into_town_suceeded",0,
    "Disguised in the garments of a poor pilgrim, you fool the guards and make your way into the town.",
    "none",
    [],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (jump_to_menu, "mnu_town"),
        ]),
    ]
  ),
   ("sneak_into_town_caught",0,
    "As you try to sneak in, one of the guards recognizes you and raises the alarm! You must flee back through the gates before all the guards in the town come down on you!",
    "none",
    [
       (assign, "$auto_menu", "mnu_captivity_start_castle_surrender"),
    ],
    [
      ("sneak_caught_fight",[], "Try to fight your way out!",
       [
           (assign, "$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town", slot_town_center), # slot_town_gate),
           (modify_visitors_at_site, ":sneak_scene"),
           (reset_visitors),

           (try_begin),
             (this_or_next|eq, "$talk_context", tc_escape),
             (eq, "$talk_context", tc_prison_break),
             (set_jump_entry, 7),
           (else_try),
             (party_slot_eq, "$current_town", slot_party_type, spt_town),
             #(set_visitor,0, "trp_player"),
             (set_jump_entry, 0),
           (else_try),
             #(set_visitor,1, "trp_player"),
             (set_jump_entry, 1),
           (try_end),

           #(store_faction_of_party, ":town_faction", "$current_town"),
           #(faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           #(faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           #(try_begin),
           #  (gt, ":tier_2_troop", 0),
           #  (gt, ":tier_3_troop", 0),
           #  (assign,reg0, ":tier_3_troop"),
           #  (assign,reg1, ":tier_3_troop"),
           #  (assign,reg2, ":tier_2_troop"),
           #  (assign,reg3, ":tier_2_troop"),
           #(else_try),
           #  (assign,reg0, "trp_swadian_skirmisher"),
           #  (assign,reg1, "trp_swadian_crossbowman"),
           #  (assign,reg2, "trp_swadian_infantry"),
           #  (assign,reg3, "trp_swadian_crossbowman"),
           #(try_end),
           #(assign,reg4,-1),
           #(shuffle_range,0,5),
           #(set_visitor,2,reg0),
           #(set_visitor,3,reg1),
           #(set_visitor,4,reg2),
           #(set_visitor,5,reg3),

           (set_jump_mission, "mt_sneak_caught_fight"),
           (set_passage_menu, "mnu_town"),
           (jump_to_scene, ":sneak_scene"),
           (change_screen_mission),
        ]),
      ("sneak_caught_surrender",[], "Surrender.",
       [
           (jump_to_menu, "mnu_captivity_start_castle_surrender"),
        ]),
    ]
  ),
   ("sneak_into_town_caught_dispersed_guards",0,
    "You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets.",
    "none",
    [],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

   ("sneak_into_town_caught_ran_away",0,
    "You make your way back through the gates and quickly retreat to the safety of the countryside.{s11}",
    "none",
    [

    (str_clear, s11),
    (assign, ":at_least_one_escaper_caught", 0),

    (assign, ":end_cond", kingdom_ladies_end),
    (try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
      (troop_slot_eq, ":prisoner", slot_troop_is_alive, 1),  ## he's alive/active
      (try_begin),
        (troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_escaped),
        (assign, "$talk_context", tc_hero_freed),
        (assign, reg14, ":prisoner"),
        (call_script, "script_setup_troop_meeting", ":prisoner", -1),
        (troop_set_slot, ":prisoner", slot_troop_mission_participation, -1),

        (troop_get_slot, ":prison_center", ":prisoner", slot_troop_prisoner_of_party),
        (party_remove_prisoners, ":prison_center", ":prisoner", 1),
        (troop_set_slot, ":prisoner", slot_troop_prisoner_of_party, -1),

        (assign, ":end_cond", -1),
      (else_try),
        (troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_caught),
        (str_store_troop_name, s12, ":prisoner"),
        (try_begin),
            (eq, ":at_least_one_escaper_caught", 0),
            (str_store_string, s11, "str_s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind"),
        (else_try),
            (str_store_string, s11, "str_s11_also_s12_was_wounded_and_had_to_be_left_behind"),
        (try_end),
        (assign, ":at_least_one_escaper_caught", 1),
      (try_end),

      (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new
    (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$auto_menu",-1),
           (store_encountered_party, "$last_sneak_attempt_town"),
           (store_current_hours, "$last_sneak_attempt_time"),
           (change_screen_return),
        ]),
    ]
  ),


   ("enemy_offer_ransom_for_prisoner",0,
    "{s2} offers you a sum of {reg12} denars in silver if you are willing to sell him {s1}.",
    "none",
    [(call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
     (assign, reg12, reg0),
     (str_store_troop_name, s1, "$g_ransom_offer_troop"),
     (store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
     (str_store_faction_name, s2, ":faction_no"),
     ],
    [
      ("ransom_accept",[], "Accept the offer.",
       [(troop_add_gold, "trp_player", reg12),
        (party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),        
        (call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),        
        #(try_begin),
            #(troop_get_type, ":is_female", "trp_player"),
            #(eq, ":is_female", 1),                        

            #(get_achievement_stat, ":number_of_lords_sold", ACHIEVEMENT_MEN_HANDLER, 0),
            #(val_add, ":number_of_lords_sold", 1),
            #(set_achievement_stat, ACHIEVEMENT_MEN_HANDLER, 0, ":number_of_lords_sold"),            

            #(eq, ":number_of_lords_sold", 3),
            #(unlock_achievement, ACHIEVEMENT_MEN_HANDLER),
        #(try_end),

        (change_screen_return),
        ]),
      ("ransom_reject",[], "Reject the offer.",
       [
        (call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
        (call_script, "script_change_player_honor", -1),
        (assign, "$g_ransom_offer_rejected", 1),
        (change_screen_return),
        ]),
    ]
  ),


   ("training_ground",0,
    "You approach a training field where you can practice your martial skills. What kind of training do you want to do?",
    "none",
    [
      (store_add, "$g_training_ground_melee_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
      (val_sub, "$g_training_ground_melee_training_scene", training_grounds_begin),
      (try_begin),
        (ge, "$g_training_ground_training_count", 3),
        (assign, "$g_training_ground_training_count", 0),
        (rest_for_hours, 1, 5, 1), #rest while attackable
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
      (try_end),
      ],
    [
      ("camp_trainer",
       [], "Speak with the trainer.",
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
         (music_set_situation, 0),
         ]),
      ("camp_train_melee",
       [
         (neg|troop_is_wounded, "trp_player"),
         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
         (gt, reg0, 1),
         ], "Sparring practice.",
       [
         (assign, "$g_mt_mode", ctm_melee),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_archery",[], "Ranged weapon practice.",
       [
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_mounted",[], "Horseback practice.",
       [
         (assign, "$g_mt_mode", ctm_mounted),
         (jump_to_menu, "mnu_training_ground_selection_details_mounted"),
         (music_set_situation, 0),
         ]),

      ("go_to_track",[(eq, "$cheat_mode", 1)], "{!}Cheat: Go to track.",
       [
         (set_jump_mission, "mt_ai_training"),
         (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
         (val_sub, ":scene_no", training_grounds_begin),
         (jump_to_scene, ":scene_no"),
         (change_screen_mission),
        ]
       ),
      ("go_to_range",[(eq, "$cheat_mode", 1)], "{!}Cheat: Go to range.",
       [
         (set_jump_mission, "mt_ai_training"),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
        ]
       ),
      ("leave",[], "Leave.",
       [(change_screen_return),
        ]),
    ]
  ),

  ("training_ground_selection_details_melee_1",0,
   "How many opponents will you go against?",
   "none",
   [
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (troop_get_slot, "$temp", "trp_stack_selection_amounts", 1), #number of men fit
     (assign, "$temp_2", 1),
     ],
    [
      ("camp_train_melee_num_men_1",[(ge, "$temp", 1)], "One.",
       [
         (assign, "$temp", 1),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_2",[(ge, "$temp", 2)], "Two.",
       [
         (assign, "$temp", 2),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_3",[(ge, "$temp", 3)], "Three.",
       [
         (assign, "$temp", 3),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("camp_train_melee_num_men_4",[(ge, "$temp", 4)], "Four.",
       [
         (assign, "$temp", 4),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("go_back_dot",[], "Cancel.",
       [
         (jump_to_menu, "mnu_training_ground"),
        ]),
      ]
  ),

  ("training_ground_selection_details_melee_2",0,
   "Choose your opponent #{reg1}:",
   "none",
   [
     (assign, reg1, "$temp_2"),
     (troop_get_slot, "$temp_3", "trp_stack_selection_amounts", 0), #number of slots
     ],
    [
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 1),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 1),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 2),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 2),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 3),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 3),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 4),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 4),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 5),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 5),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 6),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 6),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 7),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 7),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 8),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 8),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 9),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 9),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 10),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 10),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 11),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 11),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 12),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 12),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 13),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 13),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 14),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 14),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 15),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 15),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 16),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 16),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 17),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 17),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 18),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 18),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 19),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 19),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 20),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 20),]),
      ("training_ground_selection_details_melee_random", [], "Choose randomly.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", -1),]),
      ("go_back_dot",[], "Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_mounted",0,
   "What kind of weapon do you want to train with?",
   "none",
   [],
    [
      ("camp_train_mounted_details_1",[], "One handed weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_one_handed_wpn, 0),
         ]),
      ("camp_train_mounted_details_2",[], "Polearm.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_polearm, 0),
         ]),
      ("camp_train_mounted_details_3",[], "Bow.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_bow, 0),
         ]),
      ("camp_train_mounted_details_4",[], "Thrown weapon.",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_thrown, 0),
         ]),
      ("go_back_dot",[], "Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_1",0,
   "What kind of ranged weapon do you want to train with?",
   "none",
   [],
    [
      ("camp_train_ranged_weapon_bow",[], "Bow and arrows.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_bow),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_crossbow",[], "Crossbow.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_crossbow),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_ranged_weapon_thrown",[], "Throwing Knives.",
       [
         (assign, "$g_mt_mode", ctm_ranged),
         (assign, "$temp", itp_type_thrown),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("go_back_dot",[], "Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_2",0,
   "What range do you want to practice at?",
   "none",
   [],
    [
      ("camp_train_ranged_details_1",[], "10 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 10),
         ]),
      ("camp_train_ranged_details_2",[], "20 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 20),
         ]),
      ("camp_train_ranged_details_3",[], "30 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 30),
         ]),
      ("camp_train_ranged_details_4",[], "40 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 40),
         ]),
      ("camp_train_ranged_details_5",[(eq, "$g_mt_mode", ctm_ranged),], "50 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 50),
         ]),
      ("camp_train_ranged_details_6",[(eq, "$g_mt_mode", ctm_ranged),], "60 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 60),
         ]),
      ("camp_train_ranged_details_7",[(eq, "$g_mt_mode", ctm_ranged),], "70 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 70),
         ]),
      ("go_back_dot",[], "Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_description",0,
   "{s0}",
   "none",
   [],
    [
      ("continue", [], "Continue...",
       [
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
        ]
       ),
      ]
  ),

  ("training_ground_training_result",mnf_disable_all_keys,
   "{s7}{s2}",
   "none",
   [
     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (str_clear, s2),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
     (try_begin),
       (gt, "$g_training_ground_training_success_ratio", 0),
       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
       (try_begin),
         (eq, "$g_training_ground_training_success_ratio", 100),
         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (val_div, ":xp_ratio_to_add", 2),
       (try_end),
       (val_div, ":xp_ratio_to_add", 10), # value over 1000
       (try_begin),
         (gt, ":num_fit", 8),
         (val_mul, ":xp_ratio_to_add", 3),
         (assign, ":divisor", ":num_fit"),
         (convert_to_fixed_point, ":divisor"),
         (store_sqrt, ":divisor", ":divisor"),
         (convert_to_fixed_point, ":xp_ratio_to_add"),
         (val_div, ":xp_ratio_to_add", ":divisor"),
       (try_end),
##       (assign, reg0, ":xp_ratio_to_add"),
##       (display_message, "@xp earn ratio: {reg0}/1000"),
       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (store_add, ":end_cond", ":num_slots", 2),
       (try_for_range, ":i_slot", 2, ":end_cond"),
         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
         (assign, ":end_cond_2", ":num_stacks"),
         (try_for_range, ":stack_no", 0, ":end_cond_2"),
           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
           (eq, ":stack_troop", ":troop_id"),
           (assign, ":end_cond_2", 0), #break
           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
           (assign, reg1, ":amount"),
           (str_store_string, s2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
         (try_end),
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
         (val_div, ":special_xp_ratio_to_add", 2),
         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
           (assign, ":end_cond_2", ":num_stacks"),
           (try_for_range, ":stack_no", 0, ":end_cond_2"),
             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
             (eq, ":stack_troop", ":troop_id"),
             (assign, ":end_cond_2", 0), #break
             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
             (str_store_troop_name, s1, ":troop_id"),
             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
           (try_end),
         (try_end),
       (try_end),
       (try_begin),
         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
       (try_end),
     (try_end),
     (try_begin),
       (eq, "$g_training_ground_training_success_ratio", 0),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 25),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 50),
       (str_store_string, s7, "@The training didn't go very well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 75),
       (str_store_string, s7, "@The training went quite well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 99),
       (str_store_string, s7, "@The training went very well."),
     (else_try),
       (str_store_string, s7, "@The training went perfectly."),
     (try_end),

     ],
    [
      ("continue",[], "Continue...",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
   ),

  ("marshall_selection_candidate_ask",0,
   "{s15} will soon select a new marshall for {s23}. Some of the lords have suggested your name as a likely candidate.",
   "none",
   [
     (try_begin),
       (eq, "$g_presentation_marshall_selection_ended", 1),
       (change_screen_return),
     (try_end),
     (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
     (str_store_troop_name, s15, ":king"),
     (str_store_faction_name, s23, "$players_kingdom"),
     ],
    [
      ("marshall_candidate_accept", [], "Let {s15} learn that you are willing to serve as marshall.",
       [
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ("marshall_candidate_reject", [], "Tell everyone that you are too busy these days.",
       [
         (try_begin),
           (eq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (else_try),
           (assign, "$g_presentation_marshall_selection_max_renown_1", "$g_presentation_marshall_selection_max_renown_2"),
           (assign, "$g_presentation_marshall_selection_max_renown_1_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (try_end),
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ]
  ),




##    [
##      ("renew_oath",[], "Renew your oath to {s1} for another month.",[
##          (store_current_day, ":cur_day"),
##          (store_add, "$g_oath_end_day", ":cur_day", 30),
##          (change_screen_return)]),
##      ("dont_renew_oath",[], "Become free of your bond.",[
##          (assign, "$players_kingdom",0),
##          (assign, "$g_player_permitted_castles", 0),
##          (change_screen_return)]),
##    ]
##  ),


#####################################################################
## Captivity...
#####################################################################
#####################################################################
#####################################################################
#####################################################################
   ("captivity_avoid_wilderness",0,
    "Suddenly all the world goes black around you. Many hours later you regain your conciousness and find yourself at the spot you fell. Your enemies must have taken you up for dead and left you there. However, it seems that none of your wound were lethal, and altough you feel awful, you find out that can still walk. You get up and try to look for any other survivors from your party.",
    "none",
    [
      ],
    []
  ),

   ("captivity_start_wilderness",0,
    "Stub",
    "none",
    [
          (assign, "$g_player_is_captive", 1),
          (try_begin),
            (eq, "$g_player_surrenders",1),
            (jump_to_menu, "mnu_captivity_start_wilderness_surrender"),
          (else_try),
            (jump_to_menu, "mnu_captivity_start_wilderness_defeat"),
          (try_end),
      ],
    []
  ),

   ("captivity_start_wilderness_surrender",0,
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign, "$auto_menu",-1), #We need this since we may come here by something other than auto_menu
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
      ],
    []
  ),
   ("captivity_start_wilderness_defeat",0,
    "Your enemies take you prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign, "$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),

       (try_begin),
         (party_stack_get_troop_id, ":party_leader", "$g_encountered_party", 0),
         (is_between, ":party_leader", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":party_leader", slot_troop_occupation, slto_kingdom_hero),
         (store_sub, ":kingdom_hero_id", ":party_leader", active_npcs_begin),
         (set_achievement_stat, ACHIEVEMENT_BARON_GOT_BACK, ":kingdom_hero_id", 1),
       (try_end),

       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
    ],
    []
  ),
   ("captivity_start_castle_surrender",0,
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign, "$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
      ],
    []
  ),
   ("captivity_start_castle_defeat",0,
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign, "$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
      ],
    []
  ),
   ("captivity_start_under_siege_defeat",0,
    "Your enemies take you prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign, "$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
    ],
    []
  ),

   ("captivity_wilderness_taken_prisoner",mnf_scale_picture,
    "Your enemies take you prisoner.",
    "none",
    [
        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
     ],
    [
      ("continue",[], "Continue...",
       [
         # (try_for_range, ":npc", companions_begin, companions_end),
           # (main_party_has_troop, ":npc"),
           # (store_random_in_range, ":rand", 0, 100),
           # (lt, ":rand", 30),
           # (remove_member_from_party, ":npc", "p_main_party"),
           # (troop_set_slot, ":npc", slot_troop_occupation, 0),
           # (troop_set_slot, ":npc", slot_troop_playerparty_history, pp_history_scattered),
           # (assign, "$last_lost_companion", ":npc"),
           # (store_faction_of_party, ":victorious_faction", "$g_encountered_party"),
           # (troop_set_slot, ":npc", slot_troop_playerparty_history_string, ":victorious_faction"),
           # (troop_set_health, ":npc", 100),
           # (store_random_in_range, ":rand_town", towns_begin, towns_end),
           # (troop_set_slot, ":npc", slot_troop_cur_center, ":rand_town"),
           # (assign, ":nearest_town_dist", 1000),
           # (try_for_range, ":town_no", towns_begin, towns_end),
             # (store_faction_of_party, ":town_fac", ":town_no"),
             # (store_relation, ":reln", ":town_fac", "fac_player_faction"),
             # (ge, ":reln", 0),
             # (store_distance_to_party_from_party, ":dist", ":town_no", "p_main_party"),
             # (lt, ":dist", ":nearest_town_dist"),
             # (assign, ":nearest_town_dist", ":dist"),
             # (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
           # (try_end),
         # (try_end),

         (set_camera_follow_party, "$capturer_party"),
         (assign, "$g_player_is_captive", 1),
         # (store_random_in_range, ":random_hours", 18, 30),
         (store_random_in_range, ":random_hours", 12, 72),   ###### NEW v3.9.1 - 
         (call_script, "script_event_player_captured_as_prisoner"),
         (call_script, "script_stay_captive_for_hours", ":random_hours"),
         (assign, "$auto_menu", "mnu_captivity_wilderness_check"),
         (change_screen_return),
         ]),
      ]
  ),
   ("captivity_wilderness_check",0,
    "stub",
    "none",
    [(jump_to_menu, "mnu_captivity_end_wilderness_escape")],
    []
  ),
   ("captivity_end_wilderness_escape", mnf_scale_picture,
    "After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
    "none",
    [
        (play_cue_track, "track_escape"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_escape_1_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_escape_1"),
        (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 8, 12),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
   ("captivity_castle_taken_prisoner",0,
    "You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you must while away the miserable days of your captivity.",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign, "$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return)
        ]),
    ]
  ),
   ("captivity_rescue_lord_taken_prisoner",0,
    "You remain in disguise for as long as possible before revealing yourself. The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
   ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign, "$auto_menu", "mnu_captivity_castle_check"),
           (change_screen_return),
        ]),
    ]
  ),
   ("captivity_castle_check",0,
    "stub",
    "none",
    [
        (store_random_in_range, reg(7), 0, 10),
        (try_begin),
          (party_is_active, "$capturer_party"),
          (store_faction_of_party, ":capturer_faction", "$capturer_party"),
          (is_between, ":capturer_faction", kingdoms_begin, kingdoms_end),
          (store_relation, ":relation_w_player_faction", ":capturer_faction", "fac_player_faction"),
          (ge, ":relation_w_player_faction", 0),
          (jump_to_menu, "mnu_captivity_end_exchanged_with_prisoner"),
        (else_try),
          (lt, reg(7), 4),

          (store_character_level, ":player_level", "trp_player"),
############################ NEW v3.0 - added roles
          ####### if player is king, triple ransom
          (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
            (eq, "$g_player_cur_role", role_king),
              (store_mul, "$player_ransom_amount", ":player_level", 300),
              (val_add, "$player_ransom_amount", 300),
          ####### if prince, double
          (else_try), 
            (eq, "$g_player_cur_role", role_prince),
            (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
              (store_mul, "$player_ransom_amount", ":player_level", 200),
              (val_add, "$player_ransom_amount", 200),
          ####### if lord, 50% more
          (else_try), 
            (eq, "$g_player_cur_role", role_vassal),
            (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
              (store_mul, "$player_ransom_amount", ":player_level", 150),
              (val_add, "$player_ransom_amount", 150),
          (else_try),
            (this_or_next|eq, "$g_player_cur_role", role_adventurer),
            (this_or_next|eq, "$g_player_cur_role", role_bandit),
            (eq, "$g_player_cur_role", role_mercenary_captain),
            (store_mul, "$player_ransom_amount", ":player_level", 100),
            (val_add, "$player_ransom_amount", 100),
          (try_end),
############################
          # (store_troop_gold, reg3, "trp_player"),
          # (store_div, ":player_gold_div_20", reg3, 20),
          # (val_add, "$player_ransom_amount", ":player_gold_div_20"),




          (gt, reg3, "$player_ransom_amount"),
          (jump_to_menu, "mnu_captivity_end_propose_ransom"),
        (else_try),
          (lt, reg7, 7),

          (jump_to_menu, "mnu_captivity_end_exchanged_with_prisoner"),
        (else_try),
          (jump_to_menu, "mnu_captivity_castle_remain"),
        (try_end),
    ],
    []
  ),
   ("captivity_end_exchanged_with_prisoner",0,
    "After days of imprisonment, you are finally set free when your captors exchange you with another prisoner.",
    "none",
    [
      (play_cue_track, "track_escape"),
      ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 8, 12),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
   ("captivity_end_propose_ransom",0,
    "You spend long hours in the sunless dank of the dungeon, more than you can count. Suddenly one of your captors enters your cell with an offer; he proposes to free you in return for {reg5} denars of your hidden wealth. You decide to...",
    "none",
    [



      (assign, reg5, "$player_ransom_amount"),
    ],
    [
      ("captivity_end_ransom_accept",
      [
        (store_troop_gold, ":player_gold", "trp_player"),
        (ge, ":player_gold", "$player_ransom_amount")
      ], "Accept the offer.",
      [
        (play_cue_track, "track_escape"),
        (assign, "$g_player_is_captive", 0),
        (troop_remove_gold, "trp_player", "$player_ransom_amount"),
        (try_begin),
          (party_is_active, "$capturer_party"),
          (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
        (try_end),
        (call_script, "script_set_parties_around_player_ignore_player", 8, 12),
        (assign, "$g_player_icon_state", pis_normal),
        (set_camera_follow_party, "p_main_party"),
        (rest_for_hours, 0, 0, 0), #stop resting
        (change_screen_return),
      ]),
      ("captivity_end_ransom_deny",
      [
      ], "Refuse him, wait for something better.",
      [
        (assign, "$g_player_is_captive", 1),
        (store_random_in_range, reg(8), 16, 22),
        (call_script, "script_stay_captive_for_hours", reg8),
        (assign, "$auto_menu", "mnu_captivity_castle_check"),
        (change_screen_return),
      ]),
    ]
  ),
   ("captivity_castle_remain",mnf_scale_picture|mnf_disable_all_keys,
    "More days pass in the darkness of your cell. You get through them as best you can, enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
        (store_random_in_range, ":random_hours", 16, 22),
        (call_script, "script_stay_captive_for_hours", ":random_hours"),
        (assign, "$auto_menu", "mnu_captivity_castle_check"),

    ],
    [
      ("continue",[], "Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (change_screen_return),
        ]),
    ]
  ),

   ("kingdom_army_quest_report_to_army",mnf_scale_picture,
    "{s8} sends word that he wishes you to join {reg4?her:his} new military campaign. You need to bring at least {reg13} troops to the army, and are instructed to raise more men with all due haste if you do not have enough.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
        (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
        (call_script, "script_get_information_about_troops_position", ":quest_target_troop", 0),
        (str_clear, s9),
        (try_begin),
          (eq, reg0, 1), #troop is found and text is correct
          (str_store_string, s9, s1),
        (try_end),
        (str_store_troop_name, s8, ":quest_target_troop"),
        (assign, reg13, ":quest_target_amount"),
        (troop_get_type, reg4, ":quest_target_troop"),
      ],
    [
      ("continue",[], "Continue...",
       [
           (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
           (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
           (str_store_troop_name_link, s13, ":quest_target_troop"),
           (assign, reg13, ":quest_target_amount"),
           (setup_quest_text, "qst_report_to_army"),
           (str_store_string, s2, "@{s13} asked you to report to him with at least {reg13} troops."),
           (call_script, "script_start_quest", "qst_report_to_army", ":quest_target_troop"),
           (call_script, "script_report_quest_troop_positions", "qst_report_to_army", ":quest_target_troop", 3),
           (change_screen_return),
        ]),
     ]
  ),

   ("kingdom_army_quest_messenger",mnf_scale_picture,
    "{s8} sends word that he wishes to speak with you about a task he needs performed. He requests you to come and see him as soon as possible.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("kingdom_army_quest_join_siege_order",mnf_scale_picture,
    "{s8} sends word that you are to join the siege of {s9} in preparation for a full assault. Your troops are to take {s9} at all costs.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
        (str_store_troop_name, s8, ":faction_marshall"),
        (str_store_party_name, s9, ":quest_target_center"),
      ],
    [
      ("continue",[], "Continue...",
       [
           (call_script, "script_end_quest", "qst_follow_army"),
           (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
           (str_store_troop_name_link, s13, ":faction_marshall"),
           (str_store_party_name_link, s14, ":quest_target_center"),
           (setup_quest_text, "qst_join_siege_with_army"),
           (str_store_string, s2, "@{s13} ordered you to join the assault against {s14}."),
           (call_script, "script_start_quest", "qst_join_siege_with_army", ":faction_marshall"),
           (change_screen_return),
        ]),
     ]
  ),

   ("kingdom_army_follow_failed",mnf_scale_picture,
    "You have failed to follow {s8}. The marshal assumes that you were otherwise engaged, but would have appreciated your support.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
        (call_script, "script_abort_quest", "qst_follow_army", 1),
#        (call_script, "script_change_player_relation_with_troop", ":faction_marshall", -3),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("invite_player_to_faction_without_center",mnf_scale_picture,
    "You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, although he offers you no lands or titles. He will surely be offended if you do not take the offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
      ],
    [
      ("faction_accept",[], "Accept!",
       [(str_store_troop_name,s1, "$g_invite_faction_lord"),
        (setup_quest_text, "qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 0),

        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[], "Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),


   ("invite_player_to_faction",mnf_scale_picture,
    "You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, offering you the fief of {s2} for your loyal service. He will surely be offended if you do not take the offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
        (str_store_party_name, s2, "$g_invite_offered_center"),
      ],
    [
      ("faction_accept",[], "Accept!",
       [(str_store_troop_name,s1, "$g_invite_faction_lord"),
        (setup_quest_text, "qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[], "Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),

   ("invite_player_to_faction_accepted",0,
    "In order to become a vassal, you must swear an oath of homage to {s3}. You shall have to find him and give him your oath in person. {s5}",
    "none",
    [
        (call_script, "script_get_information_about_troops_position", "$g_invite_faction_lord", 0),
        (str_store_troop_name, s3, "$g_invite_faction_lord"),
        (str_store_string, s5, "@{!}{s1}"),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("question_peace_offer",0,
    "You Receive a Peace Offer^^The {s1} offers you a peace agreement. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("peace_offer_accept",[], "Accept",
       [
         # (call_script, "script_diplomacy_start_peace_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (call_script, "script_diplomacy_start_peace_between_kingdoms", "$players_kingdom", "$g_notification_menu_var1", 1), ######### NEW v3.3
         (change_screen_return),
        ]),
        ##diplomacy begin
      ("dplmc_peace_offer_terms",[], "Dictate the peace terms",
       [
         (jump_to_menu, "mnu_dplmc_dictate_terms"),
        ]),
        ##diplomacy end
      ("peace_offer_reject",[], "Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
         (change_screen_return),
        ]),
     ]
  ),

   ("notification_truce_expired",0,
    "Truce Has Expired^^The truce between {s1} and {s2} has expired.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),

   ("notification_feast_quest_expired",0,
    "{s10}",
    "none",
    [
    (str_store_string, s10, "str_feast_quest_expired"),
    ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),

   ("notification_sortie_possible",0,
    "Enemy Sighted: Enemies have been sighted outside the walls of {s4}, and {s5} and others are preparing for a sortie. You may join them if you wish.",
    "none",
    [
    (str_store_party_name, s4, "$g_notification_menu_var1"),
    (party_stack_get_troop_id, ":leader", "$g_notification_menu_var2", 0),
    (str_store_troop_name, s5, ":leader"),
      ],
    [
      ("continue",[], "Continue",
       [
       #stop auto-clock

       (change_screen_return),
        ]),
     ]
  ),




   ("notification_casus_belli_expired",0,
    "Kingdom Fails to Respond^^The {s1} has not responded to the {s2}'s provocations, and {s3} suffers a loss of face among {reg4?her:his} more bellicose subjects...^",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (faction_get_slot, ":faction_leader", "$g_notification_menu_var1", slot_faction_leader),
      (str_store_troop_name, s3, ":faction_leader"),
      (troop_get_type, reg4, ":faction_leader"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue",
       [
       (call_script, "script_faction_follows_controversial_policy", "$g_notification_menu_var1", logent_policy_ruler_ignores_provocation),
       (change_screen_return),
        ]),
     ]
  ),

   ("notification_lord_defects",0,
    "Defection: {s4} has abandoned the {s5} and joined the {s7}, taking {reg4?her:his} his fiefs with him",
    "none",
    [
      (assign, ":defecting_lord", "$g_notification_menu_var1"),
      (assign, ":old_faction", "$g_notification_menu_var2"),
      (str_store_troop_name, s4, ":defecting_lord"),
      (str_store_faction_name, s5, ":old_faction"),
      (store_faction_of_troop, ":new_faction", ":defecting_lord"),
      (str_store_faction_name, s7, ":new_faction"),
      (troop_get_type, reg4, ":defecting_lord"),

    ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
    ),


   ("notification_treason_indictment",0,
    "Treason Indictment^^{s9}",
    "none",
    [
      (assign, ":indicted_lord", "$g_notification_menu_var1"),
      (assign, ":former_faction", "$g_notification_menu_var2"),
      (faction_get_slot, ":former_faction_leader", ":former_faction", slot_faction_leader),

      #Set up string
      (try_begin),
            (eq, ":indicted_lord", "trp_player"),
            (str_store_troop_name, s7, ":former_faction_leader"),
            (str_store_string, s9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
      (else_try),
            (str_store_troop_name, s4, ":indicted_lord"),
            (str_store_faction_name, s5, ":former_faction"),
            (str_store_troop_name, s6, ":former_faction_leader"),

            (troop_get_type, reg4, ":indicted_lord"),
            (store_faction_of_troop, ":new_faction", ":indicted_lord"),
            (try_begin),
                (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
                (str_store_faction_name, s10, ":new_faction"),
                (str_store_string, s11, "str_with_the_s10"),
            (else_try),
                (str_store_string, s11, "str_outside_calradia"),
            (try_end),
            (str_store_string, s9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
        (try_end),


    ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
    ),



   ("notification_border_incident",0,
    "Border incident^^Word reaches you that {s9}. Though you don't know whether or not the rumors are true, you do know one thing -- this seemingly minor incident has raised passions among the {s4}, making it easier for them to go to war against the {s3}, if they want it...",
    "none",
    [
      (assign, ":acting_village", "$g_notification_menu_var1"),
      (assign, ":target_village", "$g_notification_menu_var2"),
      (store_faction_of_party, ":acting_faction", ":acting_village"),

      (try_begin),
            (eq, ":target_village", -1),
            (party_get_slot, ":target_faction", ":acting_village", slot_center_original_faction),
            (try_begin),
                (this_or_next|eq, ":target_faction", ":acting_faction"),
                                      (neg|faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
                (party_get_slot, ":target_faction", ":acting_village", slot_center_ex_faction),
            (try_end),

            (str_store_party_name, s1, ":acting_village"),
            (str_store_faction_name, s3, ":acting_faction"),
            (str_store_faction_name, s4, ":target_faction"),
            (faction_get_slot, ":target_leader", ":target_faction", slot_faction_leader),
            (str_store_troop_name, s5, ":target_leader"),

            (str_store_string, s9, "str_local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection"),
            (display_log_message, "@There has been an alleged border incident: {s9}"),

            (call_script, "script_add_log_entry", logent_border_incident_subjects_mistreated, ":acting_village", -1, -1, ":acting_faction"),


      (else_try),
            (store_faction_of_party, ":target_faction", ":target_village"),

            (str_store_party_name, s1, ":acting_village"),
            (str_store_party_name, s2, ":target_village"),

            (store_random_in_range, ":random", 0, 3),
            (try_begin),
                (eq, ":random", 0),

                (str_store_string, s9, "str_villagers_from_s1_stole_some_cattle_from_s2"),
                (display_log_message, "@There has been an alleged border incident: {s9}"),

                (call_script, "script_add_log_entry", logent_border_incident_cattle_stolen, ":acting_village", ":target_village", -1, ":acting_faction"),

            (else_try),
                (eq, ":random", 1),

                (str_store_string, s9, "str_villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys"),
                (display_log_message, "@There has been an alleged border incident: {s9}"),

                (call_script, "script_add_log_entry", logent_border_incident_bride_abducted, ":acting_village", ":target_village", -1, ":acting_faction"),
            (else_try),
                (eq, ":random", 2),

                (str_store_string, s9, "str_villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream"),
                (display_log_message, "@There has been an alleged border incident: {s9}"),

                (call_script, "script_add_log_entry", logent_border_incident_villagers_killed, ":acting_village", ":target_village", -1, ":acting_faction"),
            (try_end),

      (try_end),

      (str_store_faction_name, s3, ":acting_faction"),
      (str_store_faction_name, s4, ":target_faction"),

      (store_add, ":slot_provocation_days", ":acting_faction", slot_faction_provocation_days_with_factions_begin),
      (val_sub, ":slot_provocation_days", kingdoms_begin),
      (faction_set_slot, ":target_faction", ":slot_provocation_days", 30),

      ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),




   ("notification_player_faction_active",0,####### NEW v3.1-KOMKE removed reference to changing minister
    # "You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Europe will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^At any rate, your first step should be to appoint a chief minister from among your companions, to handle affairs of state. Different companions have different capabilities.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister.  Don't forget to change your kingdom's religion through your minister.",
    "You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Europe will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^You may also change the location of your court when you own more than one castle, and you may change your kingdom's culture and religion through your minister.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),

      (unlock_achievement, ACHIEVEMENT_CALRADIAN_TEA_PARTY),
      (play_track, "track_coronation"),

      (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
        (lt, "$g_player_court", walled_centers_begin),
        (store_faction_of_party, ":walled_center_faction", ":walled_center"),
        (eq, ":walled_center_faction", "fac_player_supporters_faction"),
        (assign, "$g_player_court", ":walled_center"),

####### NEW v3.1-KOMKE START- commented out this was setting player culture to no specified probably because the slot was not right
##KOMKE now player culture is set to western at script activate_player_faction (see NEW v3.1-KOMKE)
    #rafi
    # (party_get_slot, ":old_faction", "$g_player_court", slot_center_original_faction),
    # (assign, "$g_player_culture", ":old_faction"),
    # end rafi
####### NEW v3.1-KOMKE END-

        (try_begin),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
        (try_end),

        (str_store_party_name, s12, "$g_player_court"),
      (try_end),
	  
      ######### NEW v2.6 - Fixes some error messages when player builds his kingdom from scratch
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),####### NEW v3.0-KOMKE uncommented
      # (faction_set_slot, "fac_player_supporters_faction", slot_faction_marshall, -1),  ####### NEW v3.0-KOMKE commented out
	  #########
      ],
    [
####### NEW v3.1-KOMKE START-disabled
      # ("appoint_spouse",[
      # (troop_slot_ge, "trp_player", slot_troop_spouse, 1),
      # (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
      # (neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_hero),
      # (str_store_troop_name, s10, ":player_spouse"),
      # ], "Appoint your wife, {s10}...",
      #  [
      #  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
      #  (assign, "$g_player_minister", ":player_spouse"),
      #  (jump_to_menu, "mnu_minister_confirm"),
      #  ]),
      # 
      # ("appoint_npc1",[
      # (main_party_has_troop, "trp_npc1"),
      # (str_store_troop_name, s10, "trp_npc1"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc1"),
      #  (jump_to_menu, "mnu_minister_confirm"),
      #  ]),
      # 
      # ("appoint_npc2",[
      # (main_party_has_troop, "trp_npc2"),
      # (str_store_troop_name, s10, "trp_npc2"),], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc2"),
      #  (jump_to_menu, "mnu_minister_confirm"),]),
      # 
      # ("appoint_npc3",[
      # (main_party_has_troop, "trp_npc3"),
      # (str_store_troop_name, s10, "trp_npc3"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc3"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc4",[
      # (main_party_has_troop, "trp_npc4"),
      # (str_store_troop_name, s10, "trp_npc4"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc4"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc5",[
      # (main_party_has_troop, "trp_npc5"),
      # (str_store_troop_name, s10, "trp_npc5"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc5"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc6",[
      # (main_party_has_troop, "trp_npc6"),
      # (str_store_troop_name, s10, "trp_npc6"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc6"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc7",[
      # (main_party_has_troop, "trp_npc7"),
      # (str_store_troop_name, s10, "trp_npc7"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc7"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc8",[
      # (main_party_has_troop, "trp_npc8"),
      # (str_store_troop_name, s10, "trp_npc8"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc8"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc9",[
      # (main_party_has_troop, "trp_npc9"),
      # (str_store_troop_name, s10, "trp_npc9"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc9"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc10",[ #was npc9
      # (main_party_has_troop, "trp_npc10"),
      # (str_store_troop_name, s10, "trp_npc10"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc10"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc11",[
      # (main_party_has_troop, "trp_npc11"),
      # (str_store_troop_name, s10, "trp_npc11"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc11"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc12",[
      # (main_party_has_troop, "trp_npc12"),
      # (str_store_troop_name, s10, "trp_npc12"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc12"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc13",[
      # (main_party_has_troop, "trp_npc13"),
      # (str_store_troop_name, s10, "trp_npc13"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc13"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc14",[
      # (main_party_has_troop, "trp_npc14"),
      # (str_store_troop_name, s10, "trp_npc14"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc14"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc15",[
      # (main_party_has_troop, "trp_npc15"),
      # (str_store_troop_name, s10, "trp_npc15"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc15"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc16",[
      # (main_party_has_troop, "trp_npc16"),
      # (str_store_troop_name, s10, "trp_npc16"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc16"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc17",[
      # (main_party_has_troop, "trp_npc17"),
      # (str_store_troop_name, s10, "trp_npc17"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc17"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc18",[
      # (main_party_has_troop, "trp_npc18"),
      # (str_store_troop_name, s10, "trp_npc18"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc18"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc20",[
      # (main_party_has_troop, "trp_npc20"),
      # (str_store_troop_name, s10, "trp_npc20"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc20"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc21",[
      # (main_party_has_troop, "trp_npc21"),
      # (str_store_troop_name, s10, "trp_npc21"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc21"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc22",[
      # (main_party_has_troop, "trp_npc22"),
      # (str_store_troop_name, s10, "trp_npc22"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc22"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc23",[
      # (main_party_has_troop, "trp_npc23"),
      # (str_store_troop_name, s10, "trp_npc23"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc23"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc24",[
      # (main_party_has_troop, "trp_npc24"),
      # (str_store_troop_name, s10, "trp_npc24"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc24"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc25",[
      # (main_party_has_troop, "trp_npc25"),
      # (str_store_troop_name, s10, "trp_npc25"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc25"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
      # 
      # ("appoint_npc26",[
      # (main_party_has_troop, "trp_npc26"),
      # (str_store_troop_name, s10, "trp_npc26"),
      # ], "Appoint {s10}",
      #  [
      #  (assign, "$g_player_minister", "trp_npc26"),
      #  (jump_to_menu, "mnu_minister_confirm"), ]),
####### NEW v3.1-KOMKE END- 

      # ("appoint_npc27",[
      # (main_party_has_troop, "trp_npc27"),
      # (str_store_troop_name, s10, "trp_npc27"),
      # ], "Appoint {s10}",
       # [
       # (assign, "$g_player_minister", "trp_npc27"),
       # (jump_to_menu, "mnu_minister_confirm"), ]),

      # ("appoint_npc28",[
      # (main_party_has_troop, "trp_npc28"),
      # (str_store_troop_name, s10, "trp_npc28"),
      # ], "Appoint {s10}",
       # [
       # (assign, "$g_player_minister", "trp_npc28"),
       # (jump_to_menu, "mnu_minister_confirm"), ]),

      # ("appoint_npc29",[
      # (main_party_has_troop, "trp_npc29"),
      # (str_store_troop_name, s10, "trp_npc29"),
      # ], "Appoint {s10}",
       # [
       # (assign, "$g_player_minister", "trp_npc29"),
       # (jump_to_menu, "mnu_minister_confirm"), ]),

      # ("appoint_npc30",[
      # (main_party_has_troop, "trp_npc30"),
      # (str_store_troop_name, s10, "trp_npc30"),
      # ], "Appoint {s10}",
       # [
       # (assign, "$g_player_minister", "trp_npc30"),
       # (jump_to_menu, "mnu_minister_confirm"), ]),

      # ("appoint_npc31",[
      # (main_party_has_troop, "trp_npc31"),
      # (str_store_troop_name, s10, "trp_npc31"),
      # ], "Appoint {s10}",
       # [
       # (assign, "$g_player_minister", "trp_npc31"),
       # (jump_to_menu, "mnu_minister_confirm"), ]),

      ("appoint_default",[], "Appoint a prominent citizen from the area...",
       [
       (assign, "$g_player_minister", "trp_temporary_minister"),
       (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
       (jump_to_menu, "mnu_minister_confirm"),
        ]),
     ]
  ),

   ("minister_confirm",0,
    "{s9}can be found at your court in {s12}. You should consult periodically, to avoid the accumulation of unresolved issues that may sap your authority...",
    "none",
    [
      (try_begin),
        (eq, "$players_kingdom_name_set", 1),
        (change_screen_return),
      (try_end),

    (try_begin),
        (eq, "$g_player_minister", "trp_temporary_minister"),
        (str_store_string, s9, "str_your_new_minister_"),
    (else_try),
        (str_store_troop_name, s10, "$g_player_minister"),
        (str_store_string, s9, "str_s10_is_your_new_minister_and_"),
    (try_end),

    (try_begin),
        (main_party_has_troop, "$g_player_minister"),
        (remove_member_from_party, "$g_player_minister", "p_main_party"),
    (try_end),
    ],
    [
      ("continue",[], "Continue...",
       [
         (start_presentation, "prsnt_name_kingdom"),
        ]),
     ]
  ),



  (
  "notification_court_lost",0,
  "{s12}",
  "none",
  [
    (try_begin),
        (is_between, "$g_player_court", centers_begin, centers_end),
        (str_store_party_name, s10, "$g_player_court"),
        (str_store_party_name, s11, "$g_player_court"),
    (else_try),
        (str_store_string, s10, "str_your_previous_court_some_time_ago"),
        (str_store_string, s11, "str_your_previous_court_some_time_ago"),
    (try_end),


    (assign, "$g_player_court", -1),
    (str_store_string, s14, "str_after_to_the_fall_of_s11_your_court_has_nowhere_to_go"),
    (try_begin),
        # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
        (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_inactive),  ######## NEW v3.3
        (str_store_string, s14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
    (try_end),

    (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
      (eq, "$g_player_court", -1),
      ##diplomacy begin
      (neg|party_slot_eq, ":walled_center", slot_village_infested_by_bandits, "trp_peasant_woman"),
      ##diplomacy end
        (store_faction_of_party, ":walled_center_faction", ":walled_center"),
        # (eq, ":walled_center_faction", "fac_player_supporters_faction"),
        (eq, ":walled_center_faction", "$players_kingdom"),  ####### NEW v3.3
        (neg|party_slot_ge, ":walled_center", slot_town_lord, active_npcs_begin),

        (assign, "$g_player_court", ":walled_center"),
        (try_begin),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
            (str_store_party_name, s11, "$g_player_court"),
        (try_end),

        (str_store_string, s14, "str_due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12"),
    (try_end),

    (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
        (eq, "$g_player_court", -1),

        (store_faction_of_party, ":walled_center_faction", ":walled_center"),
        # (eq, ":walled_center_faction", "fac_player_supporters_faction"),
        (eq, ":walled_center_faction", "$players_kingdom"),  ######## NEW v3.3

        (assign, "$g_player_court", ":walled_center"),

        (try_begin),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
        (try_end),

        (party_get_slot, ":town_lord", ":walled_center", slot_town_lord),
        (str_store_party_name, s11, "$g_player_court"),
        (str_store_troop_name, s9, ":town_lord"),
        (str_store_string, s14, "str_after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_"),
    (try_end),

    (try_begin),
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
        (str_store_string, s14, "str_as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court"),
    (try_end),
    (str_store_string, s12, s14),
  ],
  [
      ("continue",[], "Continue...",[
      (change_screen_return),
      ]),
     ],
  ),



   ("notification_player_faction_deactive",0,
    "Your kingdom no longer holds any land.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      # (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$players_kingdom", pos0), ####### NEW v3.3
      ],
    [
      ("continue",[], "Continue...",
       [

       (try_begin),


       (try_end),
       (assign, "$g_player_minister", -1),
       (change_screen_return),
        ]),
     ]
  ),






   ("notification_player_wedding_day",mnf_scale_picture,
    "{s8} wishes to inform you that preparations for your wedding at {s10} have been complete, and that your presence is expected imminently .",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (str_store_troop_name, s8, "$g_notification_menu_var1"),
        (str_store_party_name, s10, "$g_notification_menu_var2"),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("notification_player_kingdom_holds_feast",mnf_scale_picture,
    "{s11}",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),

        (str_store_troop_name, s8, "$g_notification_menu_var1"),
        (store_faction_of_troop, ":host_faction", "$g_notification_menu_var1"),
        (str_store_faction_name, s9, ":host_faction"),

#        (str_store_faction_name, s9, "$players_kingdom"),
        (str_store_party_name, s10, "$g_notification_menu_var2"),

        (str_clear, s12),
        (try_begin),
            (check_quest_active, "qst_wed_betrothed"),
            (quest_get_slot, ":giver_troop", "qst_wed_betrothed", slot_quest_giver_troop),
            (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
            (eq, ":giver_troop_faction", "$players_kingdom"),
            (str_store_string, s12, "str_feast_wedding_opportunity"),
        (try_end),



        (str_store_string, s11, "str_s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly"),
        (try_begin),
            (eq, "$g_notification_menu_var1", 0),
            (str_store_string, s11, "str_the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast"),
        (try_end),
        (str_store_string, s11, "@{!}{s11}{s12}"),

        (try_begin),
            (ge, "$cheat_mode", 1),
            (store_current_hours, ":hours_since_last_feast"),
            (faction_get_slot, ":last_feast_start_time", "$players_kingdom", slot_faction_last_feast_start_time),
            (val_sub, ":hours_since_last_feast", ":last_feast_start_time"),
            (assign, reg4, ":hours_since_last_feast"),
            (display_message, "@{!}DEBUG -- Hours since last feast started: {reg4}"),
        (try_end),

      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("notification_center_under_siege",0,
    "{s1} has been besieged by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_village_raided",0,
    "Enemies have laid waste to {reg0?your:a} Fief^^{s1} has been raided by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),

      ### Check if raided village actually belongs to the player, and fill in appropriate words in the string (NEW v3.9.3, by Khanor) ###
      (party_get_slot, ":fief_lord", "$g_notification_menu_var1", slot_town_lord),
      (try_begin),
        (eq, ":fief_lord", "trp_player"),
        (assign, reg0, 1),
      (else_try),
        (assign, reg0, 0),
      (try_end),
      ### Player check end ###

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_village_raid_started",0,
    "Your {reg0?:faction's }Village is under attack!^^{s2} of {s3} is laying waste to {s1}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      
      ### Check if currently raided village actually belongs to the player, else fill in "faction's" in the string (NEW v3.9.3, by Khanor) ###
      (party_get_slot, ":fief_lord", "$g_notification_menu_var1", slot_town_lord),
      (try_begin),
        (eq, ":fief_lord", "trp_player"),
        (assign, reg0, 1),
      (else_try),
        (assign, reg0, 0),
      (try_end),
      ### Player check end ###
      
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_one_faction_left",0,
    "Europe Conquered by One Kingdom^^{s1} has defeated all rivals and stands as the sole kingdom.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      (try_begin),
        (faction_slot_eq, "$g_notification_menu_var1", slot_faction_leader, "trp_player"),
        (unlock_achievement, ACHIEVEMENT_THE_GOLDEN_THRONE),
      (else_try),
        (unlock_achievement, ACHIEVEMENT_MANIFEST_DESTINY),
      (try_end),

      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_oath_renounced_faction_defeated",0,
    "Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_center_lost",0,
    "An Estate was Lost^^You have lost {s1} to {s2}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("notification_troop_left_players_faction",0,
    "Betrayal!^^{s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$players_kingdom"),
      (str_store_faction_name, s3, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_troop_joined_players_faction",0,
    "Good news!^^ {s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (str_store_faction_name, s3, "$players_kingdom"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_war_declared",0,
    "Declaration of War^^{s1} has declared war against {s2}!",
    "none",
    [

#      (try_begin),
#        (eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
#        (assign, "$g_include_diplo_explanation", 0),
#        (str_store_string, s57, "$g_notification_menu_var1"),
#      (else_try),
#        (str_clear, s57),
#      (try_end),


    #to do the reason, have war_damage = 0 yield pre-war reasons
      (try_begin),
#        (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var2"),
#        (str_store_string, s2, "@you"),
#      (else_try),
#        (eq, "$g_notification_menu_var2", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var1"),
#        (str_store_string, s2, "@you"),
#      (else_try),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (try_end),


      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("notification_peace_declared",0,
    "Peace Agreement^^{s1} and {s2} have made peace!^{s57}",
    "none",
    [

      (try_begin),
        (eq, 1, 0), #Alas, this does not seem to work
        (eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
        (assign, "$g_include_diplo_explanation", 0),
      (else_try),
        (str_clear, s57),
      (try_end),

      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("notification_faction_defeated",0,
    "Faction Eliminated^^{s1} is no more!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[], "Continue...",
       [
         (try_begin),
           (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
           (troop_slot_eq, "$supported_pretender", slot_troop_original_faction, "$g_notification_menu_var1"),

           #All rebels switch to kingdom
           (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
             (troop_slot_eq, ":cur_troop", slot_troop_is_alive, 1),  ## he's alive/active
             (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (troop_set_faction, ":cur_troop", "$g_notification_menu_var1"),
             (call_script, "script_troop_set_title_according_to_faction", ":cur_troop", "$g_notification_menu_var1"),
             (try_begin),
               (this_or_next|eq, "$g_notification_menu_var1", "$players_kingdom"),
               (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
               (call_script, "script_check_concilio_calradi_achievement"),
             (try_end),
           (else_try), #all loyal lords gain a small bonus with the player
             (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "$g_notification_menu_var1"),
             (call_script, "script_troop_change_relation_with_troop", ":cur_troop", "trp_player", 5),
           (try_end),

           (try_for_parties, ":cur_party"),
             (store_faction_of_party, ":cur_faction", ":cur_party"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (party_set_faction, ":cur_party", "$g_notification_menu_var1"),
           (try_end),

           (assign, "$players_kingdom", "$g_notification_menu_var1"),
           (try_begin),
            (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
            (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_faction, ":spouse", "$g_notification_menu_var1"),
           (try_end),


           (call_script, "script_add_notification_menu", "mnu_notification_rebels_switched_to_faction", "$g_notification_menu_var1", "$supported_pretender"),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_state, sfs_active),
           (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),

           (faction_get_slot, ":old_leader", "$g_notification_menu_var1", slot_faction_leader),
           (troop_set_slot, ":old_leader", slot_troop_change_to_faction, "fac_commoners"),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_leader, "$supported_pretender"),
           (troop_set_faction, "$supported_pretender", "$g_notification_menu_var1"),

           (faction_get_slot, ":old_marshall", "$g_notification_menu_var1", slot_faction_marshall),
           (try_begin),
             (ge, ":old_marshall", 0),
             (troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
             (party_is_active, ":old_marshall_party"),
             (party_set_marshall, ":old_marshall_party", 0),
           (try_end),

           (faction_set_slot, "$g_notification_menu_var1", slot_faction_marshall, "trp_player"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_state, sfai_default),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_object, -1),
           (troop_set_slot, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
           (troop_set_slot, "$supported_pretender", slot_troop_renown, 1000),

           (party_remove_members, "p_main_party", "$supported_pretender", 1),
           (call_script, "script_set_player_relation_with_faction", "$g_notification_menu_var1", 0),
           (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
             (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
             (neq, ":cur_kingdom", "$g_notification_menu_var1"),
             (store_relation, ":reln", ":cur_kingdom", "fac_player_supporters_faction"),
             (set_relation, ":cur_kingdom", "$g_notification_menu_var1", ":reln"),
                             #####(display_debug_message, "@Line 19320"),
             (call_script, "script_recalculate_ais_for_faction", ":cur_kingdom"), ###### NEW v3.8
           (try_end),
           (assign, "$supported_pretender", 0),
           (assign, "$supported_pretender_old_faction", 0),
           # (assign, "$g_recalculate_ais", 1),
           (call_script, "script_update_all_notes"),
         (try_end),
         (change_screen_return),
        ]),
     ]
  ),


   ("notification_rebels_switched_to_faction",0,
    "Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
    "none",
    [
      (str_store_faction_name, s11, "$g_notification_menu_var1"),
      (str_store_troop_name, s12, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue",[], "Continue...",
       [
         (assign, "$talk_context", tc_rebel_thanks),
         (start_map_conversation, "$g_notification_menu_var2", -1),
         (change_screen_return),
        ]),
     ]
  ),


   ("notification_player_should_consult",0,
    "Your minister send words that there are problems brewing in the realm which, if left untreated, could sap your authority. You should consult with him at your earliest convenience",
    "none",
    [
      ],
    [
      ("continue",[], "Continue...",
       [
        (setup_quest_text, "qst_consult_with_minister"),

        (str_store_troop_name, s11, "$g_player_minister"),
        (str_store_party_name, s12, "$g_player_court"),

        (str_store_string, s2, "str_consult_with_s11_at_your_court_in_s12"),
        (call_script, "script_start_quest", "qst_consult_with_minister", -1),


        (quest_set_slot, "qst_consult_with_minister", slot_quest_expiration_days, 30),
        (quest_set_slot, "qst_consult_with_minister", slot_quest_giver_troop, "$g_player_minister"),


        (change_screen_return),
        ]),
     ]
  ),







   ("notification_player_feast_in_progress",0,
    "Feast in Preparation^^Your wife has started preparations for a feast in your hall in {s11}",
    "none",
    [
    (str_store_party_name, s11, "$g_notification_menu_var1"),
    ],
    [
      ("continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


   ("notification_lady_requests_visit",0, #add this once around seven days after the last visit, or three weeks, or three months
    "An elderly woman approaches your party and passes one of your men a letter, sealed in plain wax. It is addressed to you. When you break the seal, you see it is from {s15}. It reads, 'I so enjoyed your last visit. {s14} I am currently in {s10}.{s12}'",
    "none",
    [

      (assign, ":lady_no", "$g_notification_menu_var1"),
      (assign, ":center_no", "$g_notification_menu_var2"),

      (str_store_troop_name, s15, ":lady_no"),
      (str_store_party_name, s10, ":center_no"),

      (store_current_hours, ":hours_since_last_visit"),
      (troop_get_slot, ":last_visit_hours", ":lady_no", slot_troop_last_talk_time),
      (val_sub, ":hours_since_last_visit", ":last_visit_hours"),

      (call_script, "script_get_kingdom_lady_social_determinants", ":lady_no"),
      (assign, ":lady_guardian", reg0),

      (str_store_troop_name, s16, ":lady_guardian"),
      (call_script, "script_troop_get_family_relation_to_troop", ":lady_guardian", ":lady_no"),

      (str_clear, s14),
      (try_begin),
        (lt, ":hours_since_last_visit", 336),
        (try_begin),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_otherworldly),
            (str_store_string, s14, "str_as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years"),
        (else_try),
            (str_store_string, s14, "str_although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again"),
        (try_end),
      (else_try),
        (ge, ":hours_since_last_visit", 336),
        (try_begin),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_ambitious),
            (str_store_string, s14, "str_although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_"),
        (else_try),
            (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_moralist),
            (str_store_string, s14, "str_i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_"),
        (else_try),
            (str_store_string, s14, "str_it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again"),
        (try_end),
      (try_end),


      (str_clear, s12),
      (str_clear, s18),
      (try_begin),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 0),
        (str_store_string, s12, "str__you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me"),
        (str_store_string, s18, "str__you_should_first_ask_her_s11_s16s_permission"),
      (else_try),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, -1),
        (str_store_string, s12, "str__alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected"),
      (else_try),
        (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
        (str_store_string, s12, "str__as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival"),
      (try_end),

      ],
    [

      ("continue",[], "Tell the woman to inform her mistress that you will come shortly.",
       [

         (assign, ":lady_to_visit", "$g_notification_menu_var1"),
        (str_store_troop_name_link, s3, ":lady_to_visit"),
        (str_store_party_name_link, s4, "$g_notification_menu_var2"),

        (str_store_string, s2, "str_visit_s3_who_was_last_at_s4s18"),
        (call_script, "script_start_quest", "qst_visit_lady", ":lady_to_visit"),
        (quest_set_slot, "qst_visit_lady", slot_quest_giver_troop, ":lady_to_visit"), #don't know why this is necessary

        (try_begin),
            (eq, "$cheat_mode", 1),
            (quest_get_slot, ":giver_troop", "qst_visit_lady", slot_quest_giver_troop),
            (str_store_troop_name, s2, ":giver_troop"),
            (display_message, "str_giver_troop_=_s2"),
        (try_end),

        (quest_set_slot, "qst_visit_lady", slot_quest_expiration_days, 30),
        (change_screen_return),
        ]),

      ("continue",[], "Tell the woman to inform her mistress that you are indisposed.",
       [
        (troop_set_slot, "$g_notification_menu_var1", slot_lady_no_messages, 1),
        (change_screen_return),
        ]),
     ]
  ),



  ( #pre lady visit
    "garden",0,
    "{s12}",
    "none",
    [

    (call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
    (assign, ":guardian_lord", reg0),
    (str_store_troop_name, s11, "$love_interest_in_town"),

    (try_begin),
      (call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", ":guardian_lord", "trp_player"),
      (lt, reg0, 0),
      (troop_set_slot, ":guardian_lord", slot_lord_granted_courtship_permission, -1),
    (try_end),

    (assign, "$nurse_assists_entry", 0),
    (try_begin),
        (troop_slot_eq, ":guardian_lord", slot_lord_granted_courtship_permission, 1),
        (str_store_string, s12, "str_the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink"),
    (else_try), #the circumstances under which the lady arranges for a surreptitious entry
        (call_script, "script_troop_get_relation_with_troop", "trp_player", "$love_interest_in_town"),
        (gt, reg0, 0),

        (assign, ":player_completed_quest", 0),
        (try_begin),
            (check_quest_active, "qst_visit_lady"),
            (quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, "$love_interest_in_town"),
            (assign, ":player_completed_quest", 1),
        (else_try),
            (check_quest_active, "qst_formal_marriage_proposal"),
            (quest_slot_eq, "qst_formal_marriage_proposal", slot_quest_giver_troop, "$love_interest_in_town"),
            (this_or_next|check_quest_succeeded, "qst_formal_marriage_proposal"),
                (check_quest_failed, "qst_formal_marriage_proposal"),
            (assign, ":player_completed_quest", 1),
        (else_try),
            (check_quest_active, "qst_duel_courtship_rival"),
            (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_giver_troop, "$love_interest_in_town"),
            (this_or_next|check_quest_succeeded, "qst_duel_courtship_rival"),
                (check_quest_failed, "qst_duel_courtship_rival"),
            (assign, ":player_completed_quest", 1),
        (try_end),

        (try_begin),
            (store_current_hours, ":hours_since_last_visit"),
            (troop_get_slot, ":last_visit_time", "$love_interest_in_town", slot_troop_last_talk_time),
            (val_sub, ":hours_since_last_visit", ":last_visit_time"),
            (this_or_next|ge, ":hours_since_last_visit", 96), #at least four days
                (eq, ":player_completed_quest", 1),

            (try_begin),
                (is_between, "$g_encountered_party", towns_begin, towns_end),
                (str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
                (assign, "$nurse_assists_entry", 1),
            (else_try),
                (str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete"),
                (assign, "$nurse_assists_entry", 2),
            (try_end),
        (else_try),
            (str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous"),
        (try_end),
    (else_try),
        (str_store_string, s12, "str_the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter"),
    (try_end),

    ],
    [

    ("enter",
    [
    (call_script, "script_get_kingdom_lady_social_determinants", "$love_interest_in_town"),
    (troop_slot_eq, reg0, slot_lord_granted_courtship_permission, 1)
    ], "Enter",
    [
    (jump_to_menu, "mnu_town"),
    (call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
    ]
    ),

    ("nurse",
    [
    (eq, "$nurse_assists_entry", 1),
    ], "Go with the nurse",
    [
    (jump_to_menu, "mnu_town"),
    (call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
    ]
    ),


    ("nurse",
    [
    (eq, "$nurse_assists_entry", 2),
    ], "Wait by the spring",
    [
    (jump_to_menu, "mnu_town"),
    (call_script, "script_setup_meet_lady", "$love_interest_in_town", "$g_encountered_party"),
    ]
    ),

    ("leave",
    [],
    "Leave",
    [(jump_to_menu, "mnu_town")]),

    ]


  ),


     ("kill_local_merchant_begin",0,
    "You spot your victim and follow him, observing as he turns a corner into a dark alley. This will surely be your best opportunity to attack him.",
    "none",
    [
    ],
    [
      ("continue",[], "Continue...",
       [(set_jump_mission, "mt_back_alley_kill_local_merchant"),
        (party_get_slot, ":town_alley", "$qst_kill_local_merchant_center", slot_town_alley),
        (modify_visitors_at_site, ":town_alley"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 1, "trp_local_merchant"),
        (jump_to_menu, "mnu_town"),
        (jump_to_scene, ":town_alley"),
        (change_screen_mission),
        ]),
     ]
  ),


     ("debug_alert_from_s65",0,
    "DEBUG ALERT: {s65}",
    "none",
    [
    ],
    [
      ("continue",[], "Continue...",
       [
        (assign, "$debug_message_in_queue", 0),
        (change_screen_return),
        ]),
     ]
  ),

   ("auto_return_to_map",0,
    "stub",
    "none",
    [(change_screen_map)],
    []
  ),

     ("bandit_lair",0,
    "{s3}",
    "none",
    [
      (try_begin),
        (eq, "$loot_screen_shown", 1),

        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),

        (assign, "$g_leave_encounter", 0),
        (change_screen_return),

      (else_try),
        (party_stack_get_troop_id, ":bandit_type", "$g_encountered_party", 0),
        (str_store_troop_name_plural, s4, ":bandit_type"),
        (str_store_string, s5, "str_bandit_approach_defile"),

        (try_begin),
          (eq, ":bandit_type", "trp_desert_bandit"),
          (str_store_string, s5, "str_bandit_approach_defile"),
        (else_try),
          (eq, ":bandit_type", "trp_mountain_bandit"),
          (str_store_string, s5, "str_bandit_approach_cliffs"),
        (else_try),
          (eq, ":bandit_type", "trp_forest_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
        (else_try),
          (eq, ":bandit_type", "trp_taiga_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
        (else_try),
          (eq, ":bandit_type", "trp_steppe_bandit"),
          (str_store_string, s5, "str_bandit_approach_thickets"),
        (else_try),
          (eq, ":bandit_type", "trp_sea_raider"),
          (str_store_string, s5, "str_bandit_approach_cove"),
        (else_try),
          (eq, ":bandit_type", "trp_raider"),
          (str_store_string, s5, "str_bandit_approach_cove"),
        (try_end),

        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_preattack"),
        (else_try),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (eq, ":template", "pt_looter_lair"),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_lost_startup_hideout_attack"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_failure"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_success"),
        (try_end),
      (try_end),
    ],
    [
      ("continue_1",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
      ],
      "Attack the hideout...",

      [
        (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 1),
        (party_get_template_id, ":template", "$g_encountered_party"),
        (assign, "$g_enemy_party", "$g_encountered_party"),


        (try_begin),
          (eq, ":template", "pt_sea_raider_lair"),
          (assign, ":bandit_troop", "trp_sea_raider"),
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (else_try),
          (eq, ":template", "pt_forest_bandit_lair"),
          (assign, ":bandit_troop", "trp_forest_bandit"),
          (assign, ":scene_to_use", "scn_lair_forest_bandits"),
        (else_try),
        (eq, ":template", "pt_desert_bandit_lair"),
          (assign, ":bandit_troop", "trp_desert_bandit"),
          (assign, ":scene_to_use", "scn_lair_desert_bandits"),
        (else_try),
          (eq, ":template", "pt_mountain_bandit_lair"),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
          (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
        (else_try),
          (eq, ":template", "pt_taiga_bandit_lair"),
          (assign, ":bandit_troop", "trp_taiga_bandit"),
          (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
        (else_try),
          (eq, ":template", "pt_steppe_bandit_lair"),
          (assign, ":bandit_troop", "trp_steppe_bandit"),
          (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
        (else_try),
          (eq, ":template", "pt_robber_knight_lair"),
          (assign, ":bandit_troop", "trp_raider"),
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (else_try),
          (eq, ":template", "pt_looter_lair"),
          (assign, ":bandit_troop", "trp_looter"),

          (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),

          (try_begin),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_5"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_6"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_7"),
            (eq, ":starting_town_faction", "fac_kingdom_1"), #player selected swadian city as starting town.
            (assign, ":scene_to_use", "scn_lair_forest_bandits"),
          (else_try),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_8"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_15"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_29"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_30"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_33"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_34"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_35"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_36"),
            (eq, ":starting_town_faction", "fac_kingdom_2"), #player selected Vaegir city as starting town.
            (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
          (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_3"), #player selected Khergit city as starting town.
            (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
          (else_try),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_11"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_14"),
            (eq, ":starting_town_faction", "fac_kingdom_4"), #player selected Nord city as starting town.
            (assign, ":scene_to_use", "scn_lair_sea_raiders"),
          (else_try),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_9"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_37"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_10"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_12"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_13"),
            (eq, ":starting_town_faction", "fac_kingdom_5"), #player selected Rhodok city as starting town.
            (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
          (else_try),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_16"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_17"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_18"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_19"),
          (this_or_next | eq, ":starting_town_faction", "fac_papacy"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_22"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_23"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_24"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_25"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_26"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_27"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_28"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_31"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_32"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_38"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_39"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_40"),
          (this_or_next | eq, ":starting_town_faction", "fac_kingdom_41"),
            (eq, ":starting_town_faction", "fac_kingdom_20"), #player selected Sarranid city as starting town.
            (assign, ":scene_to_use", "scn_lair_desert_bandits"),
          (try_end),
        (try_end),



        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),

        (store_character_level, ":player_level", "trp_player"),
        (store_add, ":number_of_bandits_will_be_spawned_at_each_period", 5, ":player_level"),
        (val_div, ":number_of_bandits_will_be_spawned_at_each_period", 3),

        (try_for_range, ":unused", 0, ":number_of_bandits_will_be_spawned_at_each_period"),
          (store_random_in_range, ":random_entry_point", 2, 11),
          (set_visitor, ":random_entry_point", ":bandit_troop", 1),
        (try_end),

        (party_clear, "p_temp_casualties"),
        (party_clear, "p_temp_casualties_player"),
        (party_clear, "p_temp_casualties_attacker"),
        (party_clear, "p_temp_casualties_defender"),

        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission, "mt_bandit_lair"),

        (jump_to_scene, ":scene_to_use"),
        (change_screen_mission),
      ]),

      ("leave_no_attack",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0),
      ],
      "Leave...",
      [
        (change_screen_return),
      ]),

      ("leave_victory",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2),
      ],
      "Continue...",
      [
        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),

        (party_get_template_id, ":template", "$g_encountered_party"),
        (try_begin),
          (neq, ":template", "pt_looter_lair"),
          (check_quest_active, "qst_destroy_bandit_lair"),
          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
          (call_script, "script_succeed_quest", "qst_destroy_bandit_lair"),
        (try_end),

        (assign, "$g_leave_encounter", 0),
        (change_screen_return),

        (try_begin),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
          # (try_begin),
            # (gt, "$g_ally_party", 0),
            # (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
          # (else_try),
            # (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
            # (gt, ":num_quick_attachments", 0),
            # (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
            # (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
          # (try_end),
          (troop_clear_inventory, "trp_temp_troop"),

          (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties_attacker"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties_attacker", ":stack_no"),
            (try_begin),
              (party_stack_get_size, ":stack_size", "p_temp_casualties_attacker", ":stack_no"),
              (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties_attacker", ":stack_no"),
              (gt, ":stack_size", 0),
              (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
              (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties_attacker", ":stack_no"),
              (gt, ":stack_wounded_size", 0),
              (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
            (try_end),
          (try_end),

          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
          ## CC
          # Autoloot: Instead of just displaying the loot screen, we display a loot management menu instead
          (assign, ":num_companions", 0),
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (val_add, ":num_companions", 1),
          (try_end),
          (try_begin),
            (gt, ":num_companions", 0),
            (assign, "$return_menu", "mnu_bandit_lair"),
            (jump_to_menu, "mnu_manage_loot_pool"),
          (else_try),
            (change_screen_loot, "trp_temp_troop"),
          (try_end),
          #end Autoloot
          ## CC
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (eq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),
      ]),

      ("leave_defeat",
      [
        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1),
      ],
      "Continue...",
      [
        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),

        (try_begin),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (check_quest_active, "qst_destroy_bandit_lair"),
          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
          (call_script, "script_fail_quest", "qst_destroy_bandit_lair"),
        (try_end),

        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),
          (neq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),

        (assign, "$g_leave_encounter", 0),

        (try_begin),
            (party_is_active, "$g_encountered_party"),
            (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 0),
        (try_end),

        (change_screen_return),
        ]),

     ]
  ),


   ("notification_player_faction_political_issue_resolved",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on {s12}.",
    "none",
    [
    (assign, ":faction_issue_resolved", "$g_notification_menu_var1"),
    (assign, ":faction_decision", "$g_notification_menu_var2"),
    (faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
    (str_store_troop_name, s10, ":leader"),
    (try_begin),
        (eq, ":faction_issue_resolved", 1),
        (str_store_string, s11, "str_the_marshalship"),
    (else_try),
        (str_store_party_name, s11, ":faction_issue_resolved"),
    (try_end),
    (str_store_troop_name, s12, ":faction_decision"),

    ],
    [
       ("continue",
       [], "Continue...",
       [
        (change_screen_return),
        ]),


    ]
  ),

   ("notification_player_faction_political_issue_resolved_for_player",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on you. You may decline the honor, but it will probably mean that you will not receive other awards for a little while.{s12}",
    "none",
    [
    (faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
    (str_store_troop_name, s10, ":leader"),
    (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
    (try_begin),
        (eq, ":issue", 1),
        (str_clear, s11),   ############### NEW v3.11 - 
        (str_store_string, s11, "str_the_marshalship"),
        (str_store_string, s12, "@^^Note that so long as you remain marshal, the lords of the realm will be expecting you to lead them on campaign. So, if you are awaiting a feast, either for a wedding or for other purposes, you may wish to resign the marshalship by speaking to your liege."),
    (else_try),
        (str_clear, s11),   ############### NEW v3.11 - 
        (str_clear, s12),
        (str_store_party_name, s11, ":issue"),
    (try_end),
    ],
    [
       ("accept",
       [], "Accept the honor",
       [
        (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),

        (try_begin),
            (eq, ":issue", 1),
            (call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),
            (call_script, "script_appoint_faction_marshall", "$players_kingdom", "trp_player"),
            (unlock_achievement, ACHIEVEMENT_AUTONOMOUS_COLLECTIVE),
        (else_try),
            (call_script, "script_give_center_to_lord", ":issue", "trp_player", 0), #Zero means don't add garrison
        (try_end),

        (faction_set_slot, "$players_kingdom", slot_faction_political_issue, 0),
        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ## he's alive/active
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "$players_kingdom"),
            (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
        (try_end),
        (change_screen_return),
        ]),

       ("decline",
       [], "Decline the honor",
       [
        (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
        (try_begin),
            (is_between, ":issue", centers_begin, centers_end),
            (assign, "$g_dont_give_fief_to_player_days", 14),
        (else_try),
            (assign, "$g_dont_give_marshalship_to_player_days", 14),
        (try_end),

        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ## he's alive/active
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            (eq, ":active_npc_faction", "$players_kingdom"),
            (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
        (try_end),
        (change_screen_return),
        ]),
    ]
  ),

  ("start_phase_2_5",mnf_disable_all_keys,
    "{!}{s16}",
    "none",
    [
      (str_store_party_name, s1, "$g_starting_town"),
      (str_store_string, s16, "@You came by caravan through the heartland of Europe. Green shoots of wheat, barley and oats are beginning to push through the dark soil of the rolling hills, and on the lower slopes of the snowcapped mountains, herds of cattle and sheep are grazing on the spring grass. Occasionally, too, you catch sight of one of the great warhorses that are the pride of the European nobility. The land here is rich -- but also troubled, as the occasional burnt-out farm bears witness. You keep a wide berth of the forests, where desperate men have taken refuge, and it is some relief when you crest a ridge and catch sight of the great city of {s1}, its rooftops made golden by the last rays of the setting sun."),
      #(str_store_string, s16, "$g_journey_string"),
    ],
    [
      ("continue",[], "Continue...",
       [
         (jump_to_menu, "mnu_start_phase_3"),
       ]),
    ]
  ),


  ("start_phase_3",mnf_disable_all_keys,
    #"{s16}^^You are exhausted by the time you find the inn in {s1}, and fall asleep quickly. However, you awake before dawn and are eager to explore your surroundings. You venture out onto the streets, which are still deserted. All of a sudden, you hear a sound that stands the hairs of your neck on end -- the rasp of a blade sliding from its scabbard...",
    "{s16}^^You are exhausted by the time you find the inn in {s1}, you get drunk and fall asleep under the table. However, you awake before dawn and are eager to explore your surroundings. You venture out onto the streets, which are still deserted. You continue out of the town to begin your adventure.",
    "none",
    [
      (assign, ":continue", 1),
      (try_begin),
        (eq, "$current_startup_quest_phase", 1),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
        (else_try),
          (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
        (try_end),
        (jump_to_menu, "mnu_start_phase_4"),
        (assign, ":continue", 0),
      (else_try),
        (eq, "$current_startup_quest_phase", 3),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
        (else_try),
          (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
        (try_end),
        (jump_to_menu, "mnu_start_phase_4"),
        (assign, ":continue", 0),
      (try_end),

      (str_store_party_name, s1, "$g_starting_town"),
      (str_clear, s16),
      (eq, ":continue", 1),
    ],
    [
      ("continue",[], "Continue...",
       [
         (assign, "$g_starting_town", -1),
         #(assign, "$g_starting_town", "$current_town"),
         (call_script, "script_player_arrived"),
         (party_set_morale, "p_main_party", 100),
         (set_encountered_party, "$current_town"),
         #tom
         (party_get_position, pos2, "$current_town"),
         (map_get_land_position_around_position, pos1, pos2, 1),
         (party_set_position, "p_main_party",pos1),

         ### Check local area by means of local town culture, add appropriate bandits for the bandit start (NEW v3.9.3, by Khanor) ###
         (try_begin),
          (eq, "$background_type", cb_bandit),

          (call_script, "script_ee_get_closest_town", "p_main_party"),
          (assign, ":nearest_town", reg0),
          (party_get_slot, ":local_culture", ":nearest_town", slot_center_culture), ### Get culture.
          (try_begin),
            (this_or_next|eq, ":local_culture", "fac_culture_nordic"),
            (this_or_next|eq, ":local_culture", "fac_culture_finnish"),
            (this_or_next|eq, ":local_culture", "fac_culture_baltic"),
            (eq, ":local_culture", "fac_culture_rus"),
            (party_add_members, "p_main_party", "trp_taiga_bandit", 10),
          (else_try),
            (eq, ":local_culture", "fac_culture_mongol"),
            (party_add_members, "p_main_party", "trp_steppe_bandit", 10),
          (else_try),
            (this_or_next|eq, ":local_culture", "fac_culture_balkan"),
            (this_or_next|eq, ":local_culture", "fac_culture_anatolian_christian"),
            (eq, ":local_culture", "fac_culture_anatolian"),
            (party_add_members, "p_main_party", "trp_mountain_bandit", 10),
          (else_try),
            (this_or_next|eq, ":local_culture", "fac_culture_marinid"),
            (this_or_next|eq, ":local_culture", "fac_culture_mamluke"),
            (eq, ":local_culture", "fac_culture_jerusalem"),
            (party_add_members, "p_main_party", "trp_desert_bandit", 10),
          (else_try),
            (party_add_members, "p_main_party", "trp_forest_bandit", 10),
          (try_end),
        (try_end),
        ###############################################################################################################################

         # (set_show_messages, 0),
         # (succeed_quest, "qst_save_relative_of_merchant"),
         # (succeed_quest, "qst_save_town_from_bandits"),
         # (succeed_quest, "qst_collect_men"),
         # (assign, "$g_do_one_more_meeting_with_merchant", 2),
         # (assign, "$dialog_with_merchant_ended", 0),
         # (set_show_messages, 1),
         (change_screen_map),
         #(call_script, "script_prepare_alley_to_fight"),
         #tom
       ]),
    ]
  ),

  ("start_phase_4",mnf_disable_all_keys,
    "{s11}",
    "none",
    [
      (assign, ":continue", 1),
      (try_begin),
        (eq, "$current_startup_quest_phase", 2),
        (change_screen_return),
        (assign, ":continue", 0),
      (else_try),
        (eq, "$current_startup_quest_phase", 3),
        (str_store_string, s11, "str_merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern"),
      (else_try),
        (eq, "$current_startup_quest_phase", 4),
        (try_begin),
          (eq, "$g_killed_first_bandit", 1),
          (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits"),
        (else_try),
          (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded"),
        (try_end),
      (try_end),

      (eq, ":continue", 1),
    ],
    [
      ("continue",
      [
        (this_or_next|eq, "$current_startup_quest_phase", 1),
        (eq, "$current_startup_quest_phase", 4),
      ],
      "Continue...",
      [
        (assign, "$town_entered", 1),

        ################nord interiors
        # (try_begin),
          # (eq, "$current_town", "p_town_5_1"), # krakow
          # (assign, ":town_merchant", "trp_merchant_kingdom_5"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_14_1"), # stockholm
          # (assign, ":town_merchant", "trp_merchant_kingdom_14"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_11_2"), # trondheim
          # (assign, ":town_merchant", "trp_merchant_kingdom_11"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_12_1"), # edinburgh
          # (assign, ":town_merchant", "trp_merchant_kingdom_12"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_4_1"), # copenhagen
          # (assign, ":town_merchant", "trp_merchant_kingdom_4"),
          # (assign, ":town_room_scene", "scn_town_1_room"),

        ########### rhodok interiors
        # (else_try),
          # (eq, "$current_town", "p_town_10_1"), # paris
          # (assign, ":town_merchant", "trp_merchant_kingdom_10"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_13_2"), # cork
          # (assign, ":town_merchant", "trp_merchant_kingdom_13"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_9_1"), # London
          # (assign, ":town_merchant", "trp_merchant_kingdom_9"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_2_1"), # Vilnius
          # (assign, ":town_merchant", "trp_merchant_kingdom_2"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_1_1"), # marienburg
          # (assign, ":town_merchant", "trp_merchant_kingdom_1"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_6_1"), # brandenburg
          # (assign, ":town_merchant", "trp_merchant_kingdom_6"),
          # (assign, ":town_room_scene", "scn_town_1_room"),

        # (else_try),
          # (eq, "$current_town", "p_town_8_1"), # novgorod
          # (assign, ":town_merchant", "trp_merchant_kingdom_8"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_7_1"), # esztergom
          # (assign, ":town_merchant", "trp_merchant_kingdom_7"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (eq, "$current_town", "p_town_3_1"), # sarai
          # (assign, ":town_merchant", "trp_merchant_kingdom_3"),
          # (assign, ":town_room_scene", "scn_town_1_room"),
        # (else_try),
          # (store_faction_of_party, ":fac", "$current_town"),
          # (try_begin),
            # (eq, ":fac", "fac_kingdom_1"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_1"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (this_or_next| eq, ":fac", "fac_kingdom_33"),
            # (this_or_next| eq, ":fac", "fac_kingdom_34"),
            # (this_or_next| eq, ":fac", "fac_kingdom_35"),
            # (this_or_next| eq, ":fac", "fac_kingdom_36"),
            # (eq, ":fac", "fac_kingdom_2"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_2"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_3"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_3"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_4"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_4"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_5"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_5"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (this_or_next|eq, ":fac", "fac_kingdom_42"),
            # (eq, ":fac", "fac_kingdom_6"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_6"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_7"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_7"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (this_or_next | eq, ":fac", "fac_kingdom_15"),
            # (eq, ":fac", "fac_kingdom_8"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_8"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_9"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_9"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_10"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_10"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_11"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_11"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_12"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_12"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_13"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_13"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_14"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_14"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_15"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_15"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_16"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_16"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_17"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_17"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_18"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_18"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_19"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_19"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_20"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_20"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_papacy"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_21"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_22"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_22"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_23"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_23"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (this_or_next|eq, ":fac", "fac_kingdom_24"),
            # (this_or_next|eq, ":fac", "fac_kingdom_38"),
            # (this_or_next|eq, ":fac", "fac_kingdom_39"),
            # (this_or_next|eq, ":fac", "fac_kingdom_40"),
            # (eq, ":fac", "fac_kingdom_41"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_24"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_25"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_25"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_26"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_26"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_27"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_27"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_28"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_28"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_29"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_29"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_30"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_30"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_31"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_31"),
            # (assign, ":town_room_scene", "scn_town_1_room"),
          # (else_try),
            # (eq, ":fac", "fac_kingdom_32"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_32"),
            # (assign, ":town_room_scene", "scn_town_1_room"),    
          # (else_try),
            # (eq, ":fac", "fac_kingdom_37"),
            # (assign, ":town_merchant", "trp_merchant_kingdom_37"),
            # (assign, ":town_room_scene", "scn_town_1_room"),        
          # (else_try),
            # (display_message, "@unknown faction in module_game_menus start_phase_4!"),
          # (try_end),
       ############ # (else_try),
       ############   # (eq, "$current_town", "p_town_19"),
       ############   # (assign, ":town_merchant", "trp_sarranid_merchant"),
       ############   # (assign, ":town_room_scene", "scn_town_1_room"),
        # (try_end),

        # (modify_visitors_at_site, ":town_room_scene"),
        # (reset_visitors),
        # (set_visitor, 0, "trp_player"),
        # (set_visitor, 9, ":town_merchant"),

        # (assign, "$talk_context", tc_merchants_house),

        # (assign, "$dialog_with_merchant_ended", 0),

        # (set_jump_mission, "mt_meeting_merchant"),

        # (jump_to_scene, ":town_room_scene"),
        # (change_screen_mission),
      ]),

      ("continue",
      [
        (eq, "$current_startup_quest_phase", 3),
      ],
      "Continue...",
      [
        # (call_script, "script_prepare_town_to_fight"),
      ]),
    ]
  ),


  ("lost_tavern_duel",mnf_disable_all_keys,
    "{s11}",
    "none",
    [
    (try_begin),
        (agent_get_troop_id, ":type", "$g_main_attacker_agent"),
        (eq, ":type", "trp_belligerent_drunk"),
        (str_store_string, s11, "str_lost_tavern_duel_ordinary"),
    (else_try),
        (agent_get_troop_id, ":type", "$g_main_attacker_agent"),
        (eq, ":type", "trp_hired_assassin"),
        (str_store_string, s11, "str_lost_tavern_duel_assassin"),
    (try_end),
    (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
    ],
    [
      ("continue",[], "Continue...",
       [
         (jump_to_menu, "mnu_town"),
       ]),
    ]
  ),


  ("establish_court",mnf_disable_all_keys,
    "To establish {s4} as your court will require a small refurbishment. In particular, you will need a set of tools and a bolt of velvet. it may also take a short while for some of your followers to relocate here. Do you wish to proceed?",
    "none",
    [
    (str_store_party_name, s4, "$g_encountered_party"),
    ],

    [
      ("establish",[
      (player_has_item, "itm_tools"),
      (player_has_item, "itm_velvet"),
      ], "Establish {s4} as your court",
       [
        (assign, "$g_player_court", "$current_town"),
        (troop_remove_item, "trp_player", "itm_tools"),
        (troop_remove_item, "trp_player", "itm_velvet"),
        # rafi
        # (party_get_slot, ":old_faction", "$g_player_court", slot_center_original_faction),
        # (assign, "$g_player_culture", ":old_faction"),
        # end rafi
        (jump_to_menu, "mnu_town"),
       ]),


      ("continue",[], "Hold off...",
       [
         (jump_to_menu, "mnu_town"),
       ]),
    ]
  ),

  ("notification_relieved_as_marshal", mnf_disable_all_keys,
    "{s4} wishes to inform you that your services as marshal are no longer required. In honor of valiant efforts on behalf of the realm over the last {reg4} days, however, {reg8?she:he} offers you a purse of {reg5} denars.",
    "none",
    [
    (assign, reg4, "$g_player_days_as_marshal"),



    (store_div, ":renown_gain", "$g_player_days_as_marshal",4),
    (val_min, ":renown_gain", 20),
    (store_mul, ":denar_gain", "$g_player_days_as_marshal", 50),
    (val_max, ":denar_gain", 200),
    (val_min, ":denar_gain", 4000),
    (troop_add_gold, "trp_player", ":denar_gain"),
    (call_script, "script_change_troop_renown", "trp_player", ":renown_gain"),
    (assign, "$g_player_days_as_marshal", 0),
    (assign, "$g_dont_give_marshalship_to_player_days", 15),
    (assign, reg5, ":denar_gain"),

    (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
    (str_store_troop_name, s4, ":faction_leader"),
    (troop_get_type, reg8, ":faction_leader"),

    ],

     [
      ("continue",[], "Continue",
       [
         (change_screen_return),
       ]),
    ]
  ),

#### export/import NPCs begin ####
  ("export_import_npcs", mnf_enable_hot_keys,
   "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
   "none",
    [
      (assign, reg0, "$g_player_troop"),
      (str_store_troop_name, s0, "$g_player_troop"),
    ],
    [
      ("export_import_back",[], "Go back.",
        [
          (assign, "$g_player_troop", "trp_player"),
          (set_player_troop, "$g_player_troop"),
          #SW - modified to clear the s0 string
          (str_clear, s0),
          (jump_to_menu, "mnu_camp"),
        ]
      ),
    ]+[("export_import_npc"+str(x+1),
        [
          (store_add, ":dest_npc", "trp_npc1", x),
          (str_store_troop_name, s0, ":dest_npc"),
        ], "{s0}",
        [
          (store_add, ":dest_npc", "trp_npc1", x),
          (assign, "$g_player_troop", ":dest_npc"),
          (set_player_troop, "$g_player_troop"),
        ]) for x in range(0, 8)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_export_import_npcs_2")]),
    ]
  ),

  ("export_import_npcs_2", mnf_enable_hot_keys,
    "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
    "none",
     [
       (assign, reg0, "$g_player_troop"),
       (str_store_troop_name, s0, "$g_player_troop"),
     ],
    [
      ("export_import_prev",[], "Previous page", [(jump_to_menu, "mnu_export_import_npcs")]),
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (str_store_troop_name, s0, ":dest_npc"),
      ], "{s0}",
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (assign, "$g_player_troop", ":dest_npc"),
        (set_player_troop, "$g_player_troop"),
        ]) for x in range(8, 16)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_export_import_npcs_3")]),
    ]
  ),

  ("export_import_npcs_3", mnf_enable_hot_keys,
    "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
    "none",
     [
       (assign, reg0, "$g_player_troop"),
       (str_store_troop_name, s0, "$g_player_troop"),
     ],
    [
      ("export_import_prev",[], "Previous page", [(jump_to_menu, "mnu_export_import_npcs_2")]),
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (str_store_troop_name, s0, ":dest_npc"),
      ], "{s0}",
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (assign, "$g_player_troop", ":dest_npc"),
        (set_player_troop, "$g_player_troop"),
        ]) for x in range(16, 24)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_export_import_npcs_4")]),
    ]
  ),

  ("export_import_npcs_4", mnf_enable_hot_keys,
    "Please choose an NPC, then press key C to view and export/import this character.^^You choose {reg0?{s0}:none}.",
    "none",
     [
       (assign, reg0, "$g_player_troop"),
       (str_store_troop_name, s0, "$g_player_troop"),
     ],
    [
      ("export_import_prev",[], "Previous page", [(jump_to_menu, "mnu_export_import_npcs_3")]),
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (str_store_troop_name, s0, ":dest_npc"),
      ], "{s0}",
      [
        (store_add, ":dest_npc", "trp_npc1", x),
        (assign, "$g_player_troop", ":dest_npc"),
        (set_player_troop, "$g_player_troop"),
        ]) for x in range(24, 29)
      
    ]
  ),

#### export/import NPCs end ####

# ---- pick nation ---- #
    ("pick_nation",
        0,
        "Whom will you serve?",
        "none",
        [],
        [
            ("serve_noone",
                [],
                "No-one",
                [
          (assign, "$g_start_faction", -1),
                    (jump_to_menu, "mnu_choose_skill"),
                ]
            ),

            ("serve_pick",
                [],
                "or select",
                [
          (assign, "$g_start_faction", -1),
          (start_presentation, "prsnt_faction_selection"),
                ]
            ),

      ("go_back",[], "Go back.",
       [(jump_to_menu, "mnu_start_character_4"),
        ]
       ),
        ]
    ),
# ---- pick nation ---- #

  ##diplomacy begin
   ("dplmc_notification_alliance_declared",0,
    "Alliance Agreement^^{s1} and {s2} have formed an alliance!^{s57}",
    "none",
    [

      (str_clear, s57),

      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_defensive_declared",0,
    "Defensive Pact^^{s1} and {s2} have agreed to a defensive pact!^{s57}",
    "none",
    [

      (str_clear, s57),

      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_trade_declared",0,
    "Trade Agreement^^{s1} and {s2} have signed a trade agreement!^{s57}",
    "none",
    [

      (str_clear, s57),

      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_nonaggression_declared",0,
    "Non-aggression Treaty^^{s1} and {s2} have concluded a non-aggression treaty!^{s57}",
    "none",
    [
      (str_clear, s57),

      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("dplmc_question_alliance_offer",0,
    "You Receive an Alliance Offer^^The {s1} wants to form an alliance with you. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_alliance_offer_accept",[], "Accept",
       [
         # (call_script, "script_dplmc_start_alliance_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (call_script, "script_dplmc_start_alliance_between_kingdoms", "$players_kingdom", "$g_notification_menu_var1", 1), ######### NEW v3.3
         (change_screen_return),
        ]),
      ("dplmc_alliance_offer_reject",[], "Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_question_defensive_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a defensive pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_defensive_offer_accept",[], "Accept",
       [
         # (call_script, "script_dplmc_start_defensive_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (call_script, "script_dplmc_start_defensive_between_kingdoms", "$players_kingdom", "$g_notification_menu_var1", 1),  ####### NEW v3.3
         (change_screen_return),
        ]),
      ("dplmc_defensive_offer_reject",[], "Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_question_trade_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a trade pact. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_trade_offer_accept",[], "Accept",
       [
         # (call_script, "script_dplmc_start_trade_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (call_script, "script_dplmc_start_trade_between_kingdoms", "$players_kingdom", "$g_notification_menu_var1", 1), ######## NEW v3.3
         (change_screen_return),
        ]),
      ("dplmc_trade_offer_reject",[], "Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_question_nonaggression_offer",0,
    "You Receive a Pact Offer^^The {s1} offers you a non-aggression treaty. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_nonaggression_offer_accept",[], "Accept",
       [
         # (call_script, "script_dplmc_start_nonaggression_between_kingdoms", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (call_script, "script_dplmc_start_nonaggression_between_kingdoms", "$players_kingdom", "$g_notification_menu_var1", 1), ###### NEW v3.3
         (change_screen_return),
        ]),
      ("dplmc_nonaggression_offer_reject",[], "Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -2),
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_alliance_expired",0,
    "Alliance Has Expired^^The alliance between {s1} and {s2} has expired and was degraded to a defensive pact.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_defensive_expired",0,
    "Defensive Pact Has Expired^^The defensive pact between {s1} and {s2} has expired and was degraded to a trade agreement.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),


   ("dplmc_notification_trade_expired",0,
    "Trade Agreement Has Expired^^The trade agreement between {s1} and {s2} has expired and was degraded to a non-aggression treaty.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),

      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("dplmc_continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),

  ("dplmc_dictate_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Dictate your peace terms.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
      ("dplmc_demand_4000",[(gt, "$g_player_chamberlain", 0),], "Demand 4000 denars",
      [
        # (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "$players_kingdom", -1),
        (assign, ":goodwill", reg0),
        (store_random_in_range, ":random", 0, 4),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -3),
        (try_begin),
          (le, ":random", ":goodwill"),
          (call_script, "script_dplmc_pay_into_treasury", 4000),
          # (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "$players_kingdom", 1),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "mnu_dplmc_deny_terms"),
        (try_end),
      ]),
      ("dplmc_demand_8000",[(gt, "$g_player_chamberlain", 0),], "Demand 8000 denars",
       [
         # (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
         (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "$players_kingdom", -1),
         (assign, ":goodwill", reg0),
         (val_mul, ":goodwill", 2),
                 (store_random_in_range, ":random", 0, 10),

         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
                 (try_begin),
                   (le, ":random", ":goodwill"),
           (call_script, "script_dplmc_pay_into_treasury", 8000),
           # (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
           (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "$players_kingdom", 1),
           (change_screen_return),
         (else_try),
             (jump_to_menu, "mnu_dplmc_deny_terms"),
         (try_end),
       ]),
      ("dplmc_demand_castle",[
        (assign, ":distance", 100),
        (assign, "$demanded_castle", -1),
        (try_for_range, ":castle", castles_begin, castles_end),
          (store_faction_of_party, ":castle_faction", ":castle"),
          (eq, ":castle_faction", "$g_notification_menu_var1"),
          (try_for_range, ":center", centers_begin, centers_end),
            (store_faction_of_party, ":center_faction", ":center"),
            # (eq, ":center_faction", "fac_player_supporters_faction"),
            (eq, ":center_faction", "$players_kingdom"),
            (store_distance_to_party_from_party, ":tmp_distance", ":center", ":castle"),

            (lt, ":tmp_distance", ":distance"),
            (assign, ":distance", ":tmp_distance"),
            (assign, "$demanded_castle", ":castle"),
            (str_store_party_name, s2, ":castle"),
          (end_try),
        (end_try),
        (is_between, "$demanded_castle", castles_begin,castles_end),
      ], "Demand {s2}.",
       [
        # (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "fac_player_supporters_faction", -1),
        (call_script, "script_npc_decision_checklist_peace_or_war", "$g_notification_menu_var1", "$players_kingdom", -1),
        (assign, ":goodwill", reg0),
        (val_mul, ":goodwill", 2),
        (store_random_in_range, ":random", 0, 12),

        (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -6),
        (try_begin),
          (le, ":random", ":goodwill"),
          # (call_script, "script_give_center_to_faction", "$demanded_castle", "fac_player_supporters_faction"),
          (call_script, "script_give_center_to_faction", "$demanded_castle", "$players_kingdom"),
          # (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "fac_player_supporters_faction", 1),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_notification_menu_var1", "$players_kingdom", 1),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "mnu_dplmc_deny_terms"),
        (try_end),        ]
       ),
      ("dplmc_go_back",[], "Go back.",
       [
         (jump_to_menu, "mnu_question_peace_offer"),
       ]),
    ]
  ),

  ("dplmc_deny_terms",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "The {s1} refuses your terms and is breaking off of negotiations.",
    "none",
    [(set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),],
    [
      ("dplmc_continue",[], "Continue",
       [
       (change_screen_return),
       ]),
    ]
  ),

   ("dplmc_village_riot_result",mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_dplmc_village_riot_removed"),
     (else_try),
       (set_background_mesh, "mesh_pic_villageriot"),
       (str_store_string, s9, "@Try as you might, you could not defeat the rebelling village."),
     (try_end),
    ],
    [
      ("dplmc_continue",[], "Continue...",
       [(call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (jump_to_menu, "mnu_village"),]),
    ],
  ),

   ("dplmc_village_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the village. But there is not much left you can control.",
    "none",
    [
     (set_background_mesh, "mesh_pic_looted_village"),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (call_script, "script_village_set_state",  "$current_town", svs_looted),
    ],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (jump_to_menu, "mnu_village"),
       ]),
    ],
  ),

   ("dplmc_town_riot_removed",mnf_disable_all_keys,
    "In bloody battle you and your men slaughter the rebels and regain control over the town.",
    "none",
    [],
    [
      ("dplmc_continue",[], "Continue...",
       [
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (assign, "$new_encounter", 1),
        (try_begin),
          (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
          (troop_get_slot, ":cur_banner", ":town_lord", slot_troop_banner_scene_prop),
          (gt, ":cur_banner", 0),
          (val_sub, ":cur_banner", banner_scene_props_begin),
          (val_add, ":cur_banner", banner_map_icons_begin),
          (party_set_banner_icon, "$g_encountered_party", ":cur_banner"),
        (try_end),
        (jump_to_menu, "mnu_castle_outside"),
       ]),
    ],
  ),

   ("dplmc_riot_negotiate",mnf_disable_all_keys,
    "You approach the angry crowd and begin negotiations. The leader of the riot demands {reg0} denars. He agrees to lay down arms if you are willing to pay.",
    "none",
    [
      (party_get_slot, ":center_relation", "$g_encountered_party", slot_center_player_relation),
      (val_min, ":center_relation", 0),
      (try_begin),
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
        (val_sub, ":center_relation", 75),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (val_sub, ":center_relation", 50),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),

      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (val_add, ":center_relation", ":persuasion_level"),
      (val_mul, ":center_relation", ":center_relation"),
      (assign, reg0, ":center_relation"),
    ],
    [
      ("dplmc_pay_riot_treasury",
      [
        (gt, "$g_player_chamberlain", 0),
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", reg0),
      ], "Induce your chamberlain to pay the money from the treasury.",
       [
        (call_script, "script_dplmc_withdraw_from_treasury", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),

       ]),
       ("dplmc_pay_riot_cash",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg0),
      ], "Pay cash.",
       [
        (troop_remove_gold, "trp_player", reg0),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),

       ]),

      ("dplmc_back",[], "Back...",
       [
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
       ]),
    ],
  ),

   ("dplmc_notification_riot",0,
    "The peasants of {s1} launched a riot against you! In a surprise attack, men loyal to you have been slain. The remainder joined the angry crowd.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (try_begin),
        (party_slot_eq, "$g_notification_menu_var1", slot_party_type, spt_town),
        (set_background_mesh, "mesh_pic_townriot"),
      (else_try),
        (set_background_mesh, "mesh_pic_villageriot"),
      (try_end),
      ],
    [
      ("dplmc_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_appoint_chamberlain",0,
    "As a lord of a fief you can now appoint a chamberlain who resides at you court for a weekly salary of 15 denars. He will handle all financial affairs like collecting and determining taxes, paying wages and managing your estate. In addition he supervises money transfers between kingdoms giving you more diplomatic options.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[], "Appoint a prominent nobleman from the area.",
       [
        (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
        (troop_equip_items, "$g_player_chamberlain"),
        (jump_to_menu, "mnu_dplmc_chamberlain_confirm"),
        ]),
      ("dplmc_continue",[], "Proceed without chamberlain.",
       [
         (assign, "$g_player_chamberlain", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_chamberlain_confirm",0,
    "Your chamberlain can be found at your court. You should consult him if you want to give him any financial advice or you need greater amounts of money. You should always make sure that there is enough money in the treasury to pay for political affairs.",
    "none",
    [],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_notification_appoint_constable",0,
    "As a lord of a fief you can now appoint a constable who resides at you court for a weekly salary of 15 denars. He will recruit new troops and provide information about your army.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[], "Appoint a prominent nobleman from the area.",
       [
        (assign, "$g_player_constable", "trp_dplmc_constable"),
        (assign, "$g_constable_training_center", -1),
        (troop_equip_items, "$g_player_constable"),
        (jump_to_menu, "mnu_dplmc_constable_confirm"),
        ]),
      ("dplmc_continue",[], "Proceed without constable.",
       [
         (assign, "$g_player_constable", -1), #denied
         (assign, "$g_constable_training_center", -1),
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_constable_confirm",0,
    "Your constable can be found at your court. You should consult him if you want to recruit new troops or get detailed informatiom about your standing  army.",
    "none",
    [],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),



   ("dplmc_notification_appoint_chancellor",0,
    "As a lord of a fief you can now appoint a chancellor who resides at you court for a weekly salary of 20 denars. He will be the keeper of your seal and conduct the correspondence between you and other important persons.",
    "none",
    [],
    [

      ("dplmc_appoint_default",[], "Appoint a prominent nobleman from the area.",
       [
        (assign, "$g_player_chancellor", "trp_dplmc_chancellor"),
        (troop_equip_items, "$g_player_chancellor"),
        (jump_to_menu, "mnu_dplmc_chancellor_confirm"),
        ]),
      ("dplmc_continue",[], "Proceed without chancellor.",
       [
         (assign, "$g_player_chancellor", -1), #denied
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_chancellor_confirm",0,
    "Your chancellor can be found at your court. You should consult him if you want to send messages or gifts.",
    "none",
    [],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),


   ("dplmc_deserters",0,
    "Some of your men don't believe that you will pay their wages and desert. Overall you lose: {s11} men.",
    "none",
    [
      (set_background_mesh, "mesh_pic_deserters"),
      (store_random_in_range, ":random", 1,  "$g_notification_menu_var1"),
      (call_script, "script_dplmc_player_troops_leave", ":random"),
      (str_store_string, s11, "@{reg0}"),
    ],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

   ("dplmc_negotiate_besieger",0,
    "You appear with a white flag at the top of the wall. After a while a negotiator of {s11} approaches you. He demands {s6} and all associated villages as well as {reg0} denars for safe conduct.",
    "none",
    [
      (party_get_slot, ":besieger", "$current_town", slot_center_is_besieged_by),
      (party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
      (str_store_troop_name, s11, ":enemy_party_leader"),
      (store_faction_of_troop, ":besieger_faction", ":enemy_party_leader"),

      (assign, ":besieger_size", 0),
      (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":lord", slot_troop_is_alive, 1),  ## he's alive/active
        (store_faction_of_troop, ":lord_faction", ":lord"),
        (eq, ":lord_faction", ":besieger_faction"),
        (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
        (party_is_active, ":led_party"),

        (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
        (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

        (party_is_active, ":besieger"),
        (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
        (lt, ":distance_to_marshal", 25),
        (party_get_num_companions, ":party_size", ":led_party"),
        (val_add, ":besieger_size", ":party_size"),
      (try_end),

      (assign, ":garrison_size", 0),
      (party_get_num_companion_stacks, ":num_stacks", "$current_town"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_size, ":stack_size", "$current_town", ":i_stack"),
        (val_add, ":garrison_size", ":stack_size"),
      (try_end),
      (val_sub, ":besieger_size", ":garrison_size"),

      (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
      (val_mul, ":player_persuasion_skill", 10),
      (store_sub, "$diplomacy_var", ":besieger_size", ":player_persuasion_skill"),
      (val_mul, "$diplomacy_var", 4),
      (val_max, "$diplomacy_var",500),
      (val_div, "$diplomacy_var", 100),
      (val_mul, "$diplomacy_var", 100),
      (assign, reg0, "$diplomacy_var"),

      (str_store_party_name, s6, "$current_town"),

    ],
      [
      ("dplmc_comply_treasury",
      [
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", "$diplomacy_var"),
      ], "Comply and induce your chamberlain to pay the money form the treasury.",
      [
        (call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_comply",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", "$diplomacy_var"),
      ], "Comply and pay the money cash.",
      [
        (troop_remove_gold, "trp_player", "$diplomacy_var"),
        (call_script, "script_dplmc_player_center_surrender", "$current_town"),
        (change_screen_return),
      ]),

      ("dplmc_break_off",[], "Break off negotiations.",
       [
          (jump_to_menu, "mnu_town"),
        ]),
     ]
  ),


   ("dplmc_messenger",0,
    "Sire, I found {s10} and delivered your message. His answer was {s11}.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (str_store_troop_name, s10, "$g_notification_menu_var1"),
        (try_begin),
          (eq, "$g_notification_menu_var2", 1),
          (str_store_string, s11, "@positive"),
        (else_try),
          (str_store_string, s11, "@negative"),
        (try_end),
    ],
    [
      ("dplmc_continue",[], "Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),
  ##diplomacy end

########################################################
# Autoloot Game Menus Begin
########################################################

##########################################################
# Inventory allocation / Loot allocation Game Menu  -  by Fisheye
# Parameters:
# $return_menu : return to this menu after managing loot. 0 if this menu is called via random encounter
  ("manage_loot_pool",
    0,
    "{s10}",
    "none",
    [
      (assign, "$pool_troop", "trp_temp_troop"),
      (assign, reg20, -5), ### Start at -5 to account for equipped gear on the "pool_troop" (NEW v3.9.3, by Khanor) ###
      (troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
        (try_for_range, ":i_slot", 0, ":inv_cap"),
          (troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
          (ge, ":item_id", 0),
          (val_add, reg20, 1),
        (try_end),
        ### reg20 now contains number of items in loot pool.
        (try_begin),
          (le, reg20, 0),
          (str_store_string, 10, "str_item_pool_no_items"),
          (str_store_string, 20, "str_item_pool_leave"),
        (else_try),
          (eq, reg20, 1),
          (str_store_string, 10, "str_item_pool_one_item"),
          (str_store_string, 20, "str_item_pool_abandon"),
          (str_store_string, 30, "str_item_pool_leave_without_items"),
        (else_try),
          (str_store_string, 10, "str_item_pool_many_items"),
          (str_store_string, 20, "str_item_pool_abandon"),
          (str_store_string, 30, "str_item_pool_leave_without_items"),
        (try_end),
    ],
    [
      ("auto_loot",
        [
          (eq, "$inventory_menu_offset", 0),
          (store_free_inventory_capacity, ":space", "$pool_troop"),
          (ge, ":space", 10)
        ],
        "Let your heroes select gear from the item pool.", [(jump_to_menu, "mnu_auto_loot")]
      ),
      ("auto_loot_no",
        [
          (eq, "$inventory_menu_offset", 0),
          (store_free_inventory_capacity, ":space", "$pool_troop"),
          (lt, ":space", 10),
          (disable_menu_option)
        ],
        "Insufficient item pool space for auto-upgrade.", []
      ),
      ("loot", [],
        "Access the item pool.", [(change_screen_loot, "$pool_troop")]
      ),
      ## CC
      ("auto_loot_upgrade_management", [],
        "Upgrade management of the companions' equipment.",
        [
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (assign, "$temp", ":stack_troop"),
            (assign, ":num_stacks", 0),
          (try_end),
          # (start_presentation, "prsnt_autoloot_upgrade_management"),
          (start_presentation, "prsnt_dplmc_autoloot_upgrade_management"), ######### NEW v3.5
        ]
      ),
      ("auto_loot_leave_with_nothing",
        [
          (gt, reg20, 0),
          (assign, reg1, "$g_price_threshold_for_picking"),
          (gt, reg1, 0),
        ],
        "Pick the items which price higher than {reg1} denars and continue.",
        [
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (call_script, "script_transfer_special_inventory", "$pool_troop", ":stack_troop"), #special items
          (try_end),
          # (call_script, "script_sort_food", "trp_player"),  ### NEW v3.5
          (jump_to_menu, "$return_menu"),
        ]
      ),
      ("auto_loot_leave", [],
        "{s20}",
        [
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (call_script, "script_transfer_inventory", "$pool_troop", ":stack_troop", 1), #include book
          (try_end),
          # (call_script, "script_sort_food", "trp_player"),  ### NEW v3.5
          (jump_to_menu, "$return_menu"),
        ]
      ),
      ### Option to leave without any items as a convenience when the remaining items aren't even worth picking up (NEW v3.9.3, by Khanor) ###
      ("auto_loot_leave_without_items", [],
        "{s30}",
        [
          (display_message, "@You decide to leave and let any remaining items lie."),
          (jump_to_menu, "$return_menu"),
        ]
      ),
################################################################
##### Custom Commander(CC)
################################################################
    ]
  ),

  ("auto_loot", 0,
    "Your heroes will automatically grab items from the item pool based on their pre-selected upgrade options. Heroes listed first in the party order will have first pick. Any equipment no longer needed will be placed back into the item pool. Are you sure you wish to do this?",
    "none", [],
    [
      ("No", [],
        "No, I've changed my mind.",
        [(jump_to_menu, "mnu_manage_loot_pool")]
      ),
      ("Yes", [],
        "Yes, perform the upgrading.",
        [
          (call_script, "script_auto_loot_all"),
          (jump_to_menu, "mnu_manage_loot_pool"),
        ]
      ),
    ]
  ),
########################################################
# Autoloot Game Menus end
########################################################

   ("pagan_stronghold",0,
    "You enter a deep forest and spot a fortified settlement, it belongs to the {s21}.",
    "none",
    [
      (str_store_faction_name, s21, "$g_encountered_party_faction"),
      (troop_get_type, ":is_female", "trp_player"),
      (try_begin),
        (eq, ":is_female", 1),
        (set_background_mesh, "mesh_pic_siege_sighted_fem"),
      (else_try),
        (set_background_mesh, "mesh_pic_siege_sighted"),
      (try_end),
    ],
    [
      ("pagan_stronghold_attack",
      [
        (store_relation, ":rel", "$g_encountered_party_faction", "fac_player_supporters_faction"),
        (assign, reg0, ":rel"),
        (display_message, "@relation: {reg0}"),
        (lt, ":rel", 0),
        (set_background_mesh, "mesh_pic_siege_attack"),
      ],
      "Attack...",
      [
        (call_script, "script_calculate_renown_value"),
        (call_script, "script_calculate_battle_advantage"),
        (assign, ":battle_advantage", reg0),
        (val_mul, ":battle_advantage", 2),
        (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
        (set_battle_advantage, ":battle_advantage"),
        (set_jump_mission, "mt_pagan_stronghold_attack"),
        (assign, "$g_next_menu", "mnu_castle_taken"),
        (set_party_battle_mode),
        (assign, ":battle_scene", "scn_pagan_stronghold_1"),
        (assign, "$g_next_menu", "mnu_simple_encounter"),
        (jump_to_scene, ":battle_scene"),
        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
      ]),

      ("pagan_stronghold_leave",
      [],
      "Leave.",
      [
        (change_screen_return),
      ]),
    ]
  ),
  
 ("manor_center",0,
    "{s9} {s21}. {s22} {s23}",
    "none",
    [
      (try_begin),
        (store_time_of_day, ":cur_hour"),
        (ge, ":cur_hour", 5),
        (lt, ":cur_hour", 21),
        (assign, "$town_nighttime", 0),
      (else_try),
        (assign, "$town_nighttime", 1),
      (try_end),
    
      (str_store_faction_name, s21, "$g_encountered_party_faction"),
      # (troop_get_type, ":is_female", "trp_player"),
      (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
      (str_store_string, s9, "@You come across a small settlement. It belongs to "),
      (try_begin),
        (this_or_next|party_slot_eq, ":bound_center", slot_village_state, svs_looted),
        (party_slot_eq, "$g_encountered_party", slot_village_state, svs_looted),
        (party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_notbuild),
        (set_background_mesh, "mesh_pic_looted_village"),
        (str_store_string, s9, "@You come across a small abandoned settlement. It belonged to "),
      (else_try),
        (set_background_mesh, "mesh_pic_manor"),
      (try_end),
            
      (str_clear, s22),
      (assign, ":continue", 0),
      (try_begin),
        (party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_notbuild),
        (this_or_next|party_slot_eq, ":bound_center", slot_village_state, svs_looted),
        (party_slot_eq, "$g_encountered_party", slot_village_state, svs_looted),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 0),
      (try_begin),
        # (party_slot_eq, "$g_encountered_party", manor_slot_unique, manor_building_inprogress), 
        # (str_store_string, s22, "@A new manor is being built and peasants are being relocated to live near it."),    
      # (else_try),#bandits
        (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 1),
        (str_store_string, s22, "@Troublesome bandits are abusing the peasants."),
      (else_try), #mercenary company
        (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 2),
        (str_store_string, s22, "@A Company of mercenaries are causing problems. People talk, that they are well armed!"),
      (else_try), #more to do
        (str_store_string, s22, "@Troublesome bandits are abusing the peasants."),
        (str_clear, s22),
      (try_end),      
      
      (str_clear, s23),
      (try_begin),
        (party_get_slot, ":population", "$g_encountered_party", manor_slot_population),
        (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
        (assign, reg0, ":population"),
        (assign, reg1, ":prosperity"),
        (str_store_string, s23, "@Current population: {reg0}, current prosperity: {reg1}"),
      (try_end),
    ],
    [    
      ("manor_debug",
      [
        (eq, 0, 1),
        # (party_get_slot, ":village", "$g_encountered_party", slot_village_bound_center), 
        # (party_get_slot, ":village_lord", ":village", slot_town_lord),
        # (eq, ":village_lord", "trp_player"),
        # (neg|party_slot_eq, ":village", slot_village_state, svs_looted),
      ],
      "DEBUG this manor.",
      [
        #(change_screen_return),
        (jump_to_menu, "mnu_manor_build"),
      ]),
    
      ("manor_center_bandits",
      [
        (party_slot_ge, "$g_encountered_party", slot_village_infested_by_bandits, 1),
        (neg|party_slot_eq, "$g_encountered_party", slot_village_state, svs_looted),
        (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
        (neg|party_slot_eq, ":bound_center", slot_village_state, svs_looted),
        #(neg|party_slot_eq, "$g_encountered_party", manor_slot_unique, manor_building_inprogress), 
        
      ],
      "Smash the Bastards.",
      [
        (party_clear_particle_systems, "$g_encountered_party"),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (store_faction_of_party, ":manor_faction", "$g_encountered_party"),
        (party_clear, ":scene_to_use"),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (try_begin), #mercenaries
          (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 2),
          (store_random_in_range, ":random", 3, 7),
          (call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
          (assign, ":random_troop", reg0),
          (set_visitors, 0, ":random_troop", ":random"),
          (party_add_members, "$g_encountered_party", ":random_troop", ":random"),
          
          (store_random_in_range, ":random", 3, 7),
          (call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
          (assign, ":random_troop", reg0),
          (set_visitors, 0, ":random_troop", ":random"),
          (party_add_members, "$g_encountered_party", ":random_troop", ":random"),
          
          (store_random_in_range, ":random", 3, 7),
          (call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
          (assign, ":random_troop", reg0),
          (set_visitors, 0, ":random_troop", ":random"),
          (party_add_members, "$g_encountered_party", ":random_troop", ":random"),
          
          (store_random_in_range, ":random", 3, 7),
          (call_script, "script_get_mercenary_troop_for_manor", ":manor_faction"),
          (assign, ":random_troop", reg0),
          (set_visitors, 0, ":random_troop", ":random"),
          (party_add_members, "$g_encountered_party", ":random_troop", ":random"),
        (else_try), #bandits and else(for now)
          #(party_slot_ge, "$g_encountered_party", slot_village_infested_by_bandits, 1),
          (store_random_in_range, ":random_troop", "trp_mountain_bandit", "trp_taiga_bandit"),
          (store_random_in_range, ":random", 10, 31),
          (set_visitors, 0, ":random_troop", ":random"),
          (party_add_members, "$g_encountered_party", ":random_troop", ":random"),
        (try_end),
        #(set_visitors, 2, "trp_farmer", 5),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission, "mt_manor_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_manor_infest_bandits_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
      ]),
    
      ("manor_walk",
      [
        #(neq, "$g_encountered_party_template", "pt_empty"), #no point in walking in an empty field?
        (neg|party_slot_eq, "$g_encountered_party", slot_village_state, svs_looted),
        (party_slot_eq, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
        (this_or_next|party_slot_eq, "$g_encountered_party", manor_slot_walls, manor_building_operational),
        (neg|party_slot_eq, ":bound_center", slot_village_state, svs_looted),
        #(neg|party_slot_eq, "$g_encountered_party", manor_slot_unique, manor_building_inprogress), 
      ],
      "Walk around the center.",
      [
        (party_get_slot, ":village_scene", "$g_encountered_party", slot_castle_exterior),
        (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
        (assign, "$current_town", ":bound_center"),        
        (call_script, "script_manor_refresh_inventories", "$g_encountered_party"),
        
        #(assign, ":village_scene", "scn_manor_fortified_euro_plains"), #TOM DEBUG
        (modify_visitors_at_site, ":village_scene"),
        (reset_visitors),
        
        #(party_get_template_id, ":manor_template", "$g_encountered_party"),
        (try_begin), #unique manor.
          (call_script, "script_init_manor_agents", "$g_encountered_party"),
          (set_jump_mission, "mt_manor_center"),
        (try_end),

        
        (jump_to_scene, ":village_scene"),
        (change_screen_mission),
      ]),
      
      ("manor_improve",
      [
        #(eq, 0, 1),
        (neg|party_slot_eq, "$g_encountered_party", manor_slot_unique, manor_building_operational), 
        (neg|party_slot_eq, "$g_encountered_party", manor_slot_unique, manor_building_inprogress), 
        (this_or_next|eq, "$g_encountered_party_template", "pt_salt"),
        (eq, "$g_encountered_party_template", "pt_iron"),
        (party_get_slot, ":village", "$g_encountered_party", slot_village_bound_center), 
        (party_get_slot, ":village_lord", ":village", slot_town_lord),
        (eq, ":village_lord", "trp_player"),
        (neg|party_slot_eq, ":village", slot_village_state, svs_looted),
      ],
      "Improve this settlement.",
      [
        (jump_to_menu, "mnu_manor_improve_menu"), 
        #(change_screen_return),
      ]),
############# NEW v3.8
      ("manor_wait",
       [
	    (party_slot_ge, "$g_encountered_party", manor_slot_houses, 1),
        (party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
        ],
         "Wait here for some time.",
         [
           (assign, "$auto_enter_town", "$g_encountered_party"),
           (assign, "$g_last_rest_center", "$g_encountered_party"),

           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),
           (try_end),

           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
           (change_screen_return),
          ]),
####################
      ("manor_leave",
      [],
      "Leave.",
      [
        (change_screen_return),
      ]),
    ]
  ),
  
   ("manor_build",0,
    "MANOR DEBUG",
    "none",
    [
        
    ],
    [
      
   ("manor_improve_next",
    [],
    "Next Page",
    [
      (try_begin),
        (eq, "$tom_page", 0),
        (assign, "$tom_page", 1),
      (else_try),
        (assign, "$tom_page", 0),
      (try_end),
    ]),      
    
    ("manor_improve_leave",
      [],
      "Reset Buildings.",
      [
         (party_set_slot, "$g_encountered_party",manor_slot_houses,0),
         (party_set_slot, "$g_encountered_party",manor_slot_grainfarm,0),
         (party_set_slot, "$g_encountered_party",manor_slot_livestock,0),
         (party_set_slot, "$g_encountered_party",manor_slot_fruitfarm,0),
         (party_set_slot, "$g_encountered_party",manor_slot_fisher,0),
         (party_set_slot, "$g_encountered_party",manor_slot_marketplace,0),
         (party_set_slot, "$g_encountered_party",manor_slot_tavern,0),
         (party_set_slot, "$g_encountered_party",manor_slot_whorehouse,0),
         (party_set_slot, "$g_encountered_party",manor_slot_Monastery,0),
         (party_set_slot, "$g_encountered_party",manor_slot_well,0),
         (party_set_slot, "$g_encountered_party",manor_slot_bakery,0),
         (party_set_slot, "$g_encountered_party",manor_slot_winery,0),
         (party_set_slot, "$g_encountered_party",manor_slot_brewery,0),
         (party_set_slot, "$g_encountered_party",manor_slot_potter,0),
         (party_set_slot, "$g_encountered_party",manor_slot_blacksmith,0),
         (party_set_slot, "$g_encountered_party",manor_slot_butcher,0),
         (party_set_slot, "$g_encountered_party",manor_slot_oilmaker,0),
         (party_set_slot, "$g_encountered_party",manor_slot_linenworkshop,0),
         (party_set_slot, "$g_encountered_party",manor_slot_woolworkshop,0),
         (party_set_slot, "$g_encountered_party",manor_slot_tannery,0),
         (party_set_slot, "$g_encountered_party",manor_slot_prison,0),
         (party_set_slot, "$g_encountered_party",manor_slot_armorsmith,0),
         (party_set_slot, "$g_encountered_party",manor_slot_weaponsmith,0),
         (party_set_slot, "$g_encountered_party",manor_slot_fletcher,0),
         (party_set_slot, "$g_encountered_party",manor_slot_walls,0),
         (party_set_slot, "$g_encountered_party",manor_slot_breeder,0),
         
      ]),
      
    ("manor_improve_leave",
      [],
      "Go Back.",
      [
        (jump_to_menu, "mnu_manor_center"), 
        
        (change_screen_return),
      ]),
    
      
      ("manor_improve_house",
        [
          (eq, "$tom_page", 0),
          (this_or_next|party_slot_eq, "$g_encountered_party", manor_slot_houses, 0), #tier1->2
          (party_slot_eq, "$g_encountered_party", manor_slot_houses, 1), #tier2->3
        ],
        "Improve houses",
        [
          (party_get_slot, ":houses", "$g_encountered_party",manor_slot_houses),
          (val_add, ":houses", 1),
          (party_set_slot, "$g_encountered_party",manor_slot_houses, ":houses"),
        ]),
      
      ("manor_improve_farm",
        [
          (eq, "$tom_page", 0),
          (party_slot_eq, "$g_encountered_party", manor_slot_grainfarm, 0),
        ],
        "Build grain farm",
        [
          (party_get_slot, ":houses", "$g_encountered_party",manor_slot_grainfarm),
          (val_add, ":houses", 1),
          (party_set_slot, "$g_encountered_party",manor_slot_grainfarm, ":houses"),
        ]),
      
      ("manor_improve_livestock",
        [
          (eq, "$tom_page", 0),
          (party_slot_eq, "$g_encountered_party", manor_slot_livestock, 0),
        ],
        "Build animal farm",
        [
          (party_get_slot, ":houses", "$g_encountered_party",manor_slot_livestock),
          (val_add, ":houses", 1),
          (party_set_slot, "$g_encountered_party",manor_slot_livestock, ":houses"),
        ]),
    
      ("manor_improve_fruitfarm",
        [
          (eq, "$tom_page", 0),
          (party_slot_eq, "$g_encountered_party", manor_slot_fruitfarm, 0),
        ],
        "Build fruit farm",
        [
          (party_get_slot, ":houses", "$g_encountered_party",manor_slot_fruitfarm),
          (val_add, ":houses", 1),
          (party_set_slot, "$g_encountered_party",manor_slot_fruitfarm, ":houses"),
        ]),
      
      ("manor_improve_fisher",
        [
          (eq, "$tom_page", 0),
          (party_slot_eq, "$g_encountered_party", manor_slot_fisher, 0),
        ],
        "Build fishers",
        [
          (party_get_slot, ":houses", "$g_encountered_party",manor_slot_fisher),
          (val_add, ":houses", 1),
          (party_set_slot, "$g_encountered_party",manor_slot_fisher, ":houses"),
        ]),
        
      #tier2
      ("manor_improve_marketplace",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_marketplace, 0),
      ],
      "Build Marketplace",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_marketplace),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_marketplace, ":houses"),
      ]),
      
     ("manor_improve_tavern",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_tavern, 0),
      ],
      "Build tavern",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_tavern),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_tavern, ":houses"),
      ]),
    
    ("manor_improve_whorehouse",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_whorehouse, 0),
      ],
      "Build Harlot houses",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_whorehouse),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_whorehouse, ":houses"),
      ]),
    
    ("manor_improve_temple",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_Monastery, 0),
      ],
      "Build Monastery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_Monastery),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_Monastery, ":houses"),
      ]),
    
    ("manor_improve_well",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_well, 0),
      ],
      "Dig wells",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_well),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_well, ":houses"),
      ]),
    
    ("manor_improve_bakery",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_bakery, 0),
      ],
      "Build bakery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_bakery),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_bakery, ":houses"),
      ]),
      
    ("manor_improve_winery",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_winery, 0),
      ],
      "Build Winery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_winery),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_winery, ":houses"),
      ]),  
    
    ("manor_improve_brewery",
      [
        (eq, "$tom_page", 0),
        (party_slot_eq, "$g_encountered_party", manor_slot_brewery, 0),
      ],
      "Build Brewery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_brewery),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_brewery, ":houses"),
      ]),
      
    ("manor_improve_potter",
      [
        (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_potter, 0),
      ],
      "Build Pottery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_potter),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_potter, ":houses"),
      ]),

    ("manor_improve_blacksmith",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_blacksmith, 0),
      ],
      "Build Blacksmith",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_blacksmith),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_blacksmith, ":houses"),
      ]),
      
    ("manor_improve_butcher",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_butcher, 0),
      ],
      "Build Butchery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_butcher),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_butcher, ":houses"),
      ]),
      

      
    ("manor_improve_oilmaker",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_oilmaker, 0),
      ],
      "Build Oil Maker",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_oilmaker),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_oilmaker, ":houses"),
      ]),
      
    ("manor_improve_linenworkshop",
      [
        (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_linenworkshop, 0),
      ],
      "Build Linen Workshop",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_linenworkshop),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_linenworkshop, ":houses"),
      ]),
      
    ("manor_improve_woolworkshop",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_woolworkshop, 0),
      ],
      "Build Wool Workshop",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_woolworkshop),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_woolworkshop, ":houses"),
      ]),
      
    ("manor_improve_tannery",
      [
        (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_tannery, 0),
      ],
      "Build Tannery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_tannery),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_tannery, ":houses"),
      ]),  
     
    #tier4     
    ("manor_improve_prison",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_prison, 0),
      ],
      "Build Prison",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_prison),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_prison, ":houses"),
      ]),
    
    ("manor_improve_armorsmith",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_armorsmith, 0),
      ],
      "Build Armorsmithy",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_armorsmith),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_armorsmith, ":houses"),
      ]),
     
    ("manor_improve_weaponsmith",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_weaponsmith, 0),
      ],
      "Build Weaponsmithy",
      [
         (eq, "$tom_page", 1),
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_weaponsmith),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_weaponsmith, ":houses"),
      ]),

    ("manor_improve_fletcher",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_fletcher, 0),
      ],
      "Build Fletchery",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_fletcher),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_fletcher, ":houses"),
      ]),
      
    ("manor_improve_breeder",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_breeder, 0),
      ],
      "Build Stables",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_breeder),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_breeder, ":houses"),
      ]),
      
    ("manor_improve_walls",
      [
         (eq, "$tom_page", 1),
        (party_slot_eq, "$g_encountered_party", manor_slot_walls, 0),
      ],
      "Build Walls",
      [
        (party_get_slot, ":houses", "$g_encountered_party",manor_slot_walls),
        (val_add, ":houses", 1),
        (party_set_slot, "$g_encountered_party",manor_slot_walls, ":houses"),
      ]),
    ]),

  
  
   ("manor_improve_menu",0,
    "Do you wish to upgrade your {s0} to a {s1}. This would increase their production. It would cost you {reg0}",
    "none",
    [
        (try_begin),
          (eq, "$g_encountered_party_template", "pt_salt"),
          (str_store_string, s0, "@Salt Trader"),
          (str_store_string, s1, "@Salt Mine"),
          (store_add, reg0, manor_salt_cost, manor_salt_cost),
        (else_try),  
          (eq, "$g_encountered_party_template", "pt_iron"),
          (str_store_string, s0, "@Iron Trader"),
          (str_store_string, s1, "@Iron Mine"),
          (store_add, reg0, manor_iron_cost, manor_iron_cost),
        (else_try),
          (jump_to_menu, "mnu_manor_center"), 
        (try_end), 
    ],
    [
      ("manor_improve_menu_accept",
      [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg0),
      ],
      "Yes.",
      [
        (troop_remove_gold, "trp_player", reg0),
        (party_get_slot, ":village_id", "$g_encountered_party",slot_village_bound_center),
        (assign, ":newly_spawned_manor", 0),
        (try_begin),
          (eq, "$g_encountered_party_template", "pt_salt"),
          # (party_get_slot, ":good", ":village_id",slot_center_salt_pans),
          # (val_add, ":good", 2),
          # (party_set_slot, ":village_id",slot_center_salt_pans, ":good"),
          (call_script, "script_spawn_manor_party", "pt_salt_mine", ":village_id"),
          (assign, ":newly_spawned_manor", reg0),
        (else_try),
          #rev2
          # (party_get_slot, ":good", ":village_id",slot_center_iron_deposits),
          # (val_add, ":good", 2),
          # (party_set_slot, ":village_id",slot_center_iron_deposits, ":good"),
          (call_script, "script_spawn_manor_party", "pt_iron_mine", ":village_id"),
          (assign, ":newly_spawned_manor", reg0),
        (try_end),
        
        (party_get_position, pos0, "$g_encountered_party"),
        (party_set_position, ":newly_spawned_manor", pos0),
        (remove_party, "$g_encountered_party"),
        (assign, "$g_encountered_party", ":newly_spawned_manor"), #rev2
        (call_script, "script_update_manor_array"),
        (change_screen_return),
      ]),
      
      ("manor_improve_menu_refuse",
      [],
      "No.",
      [
        (jump_to_menu, "mnu_manor_center"), 
      ]),
    ]
    ),
    
    ("center_spawn_manor",0,
    "Do you wish to purchase a manor house nearby? It costs {reg10} denars.",
    #"What kind of settlement do you wish to invest to?",
    "none",
    [
        (assign, reg10, manor_cost),
    ],
    [
       ("center_spawn_manor_farm",
       [
        # (neg|is_between, "$current_town", castles_begin, castles_end),
        # (assign, ":valid_for_build", 0),
        # (troop_get_slot, ":manor_amount", "trp_manor_array",0),
        # (try_for_range, ":slot", 1, ":manor_amount"),
         # (troop_get_slot, ":manor", "trp_manor_array", ":slot"),
         # (party_slot_eq, ":manor", slot_village_bound_center, "$current_town"),
         # (party_get_template_id, ":manor_template", ":manor"),
         # (eq, ":manor_template", "pt_farm"),
         # (assign, ":valid_for_build", 1),
         # (assign, ":manor_amount", 0),
        # (try_end),      
        # (eq, ":valid_for_build", 0),    
        
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", manor_cost),
        (assign, reg0, manor_cost),
      ],
      "Yes!",
      [                
        (call_script, "script_spawn_manor_party", "pt_manor", "$current_town"),
        (call_script, "script_update_manor_array"),
        (troop_remove_gold, "trp_player",manor_cost),
        (display_message, "@You purchased a manor nearby!", 0x00FF00),
        (jump_to_menu, "$g_next_menu"), 
      ]),      
      
      ("center_spawn_manor_leave",
      [],
      "No.",
      [
        #(change_screen_return),
        (jump_to_menu, "$g_next_menu"), 
      ]),
    ]
  ),  
  
  
    ("manor_infest_bandits_result",mnf_scale_picture,
    "{s9}",
    "none",
    [
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s9, "@You slaughter the bandits like they were nothing! The peasants cheer your name and are planning on holding a feast in the near future to honor you!"),
     (else_try),
       (str_store_string, s9, "@Trying as you might, you could not defeat the bandits. They had their fun with the settlement peasants and went off, to celebrate elsewhere."),
       (set_background_mesh, "mesh_pic_looted_village"),
     (try_end),
    ],
    [
      ("manor_infest_victory",
      [
        (eq, "$g_battle_result", 1),
      ], "Huzzah! Now for the looting...",
      [
        (display_message, "@Relationship with the regional center improves!", 0x00FF00),
        (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
        # (call_script, "script_change_player_relation_with_center", ":bound_center", 1),
        (call_script, "script_change_player_relation_with_center", ":bound_center", 3),  ###### NEW v3.9.1 - 
        
        #(assign, "$g_next_menu", "mnu_manor_center"),

        #fake the looting script
        (troop_clear_inventory, "trp_temp_troop"),
        (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "$g_encountered_party", ":i_stack"),
          (party_stack_get_size, ":stack_size", "$g_encountered_party", ":i_stack"),
          (try_for_range, ":unused", 0, ":stack_size"),
            (troop_loot_troop, "trp_temp_troop", ":stack_troop", 70),
          (try_end),
        (try_end),
        
        (party_clear, "$g_encountered_party"),
        (party_set_slot, "$g_encountered_party",slot_village_infested_by_bandits, 0),
        #(jump_to_menu, "mnu_manor_center"),
        #(change_screen_loot, "trp_temp_troop"),
        ## CC - tom
          # Autoloot: Instead of just displaying the loot screen, we display a loot management menu instead
          (assign, ":num_companions", 0),
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop", "p_main_party", ":stack_no"),
            (is_between, ":stack_troop", companions_begin, companions_end),
            (val_add, ":num_companions", 1),
          (try_end),
          (try_begin),
            (gt, ":num_companions", 0),            
            (assign, "$return_menu", "mnu_manor_center"),
            (jump_to_menu, "mnu_manage_loot_pool"),
          (else_try),
            (jump_to_menu, "mnu_manor_center"),
            (change_screen_loot, "trp_temp_troop"),
          (try_end),
          #end Autoloot
          ## CC
      ]),
       
      ("manor_infest_defeat",
      [
        (neq, "$g_battle_result", 1),
      ], "Well, at least I'm still alive...",
      [
       (display_message, "@Relationship with the regional center deteriorates", 0xff0000),
       (party_get_slot, ":bound_center", "$g_encountered_party",slot_village_bound_center),
       (call_script, "script_change_player_relation_with_center", ":bound_center", -1),
       (party_set_slot, "$g_encountered_party",slot_village_infested_by_bandits, 0),
       (party_set_slot, "$g_encountered_party", slot_village_state, svs_looted),
       (party_clear, "$g_encountered_party"),
       (change_screen_return),
      ]) 
    ],
  ),
  
   ("harlot_services",mnf_scale_picture,
    "{s9}",
    "none",
    [
      (str_store_string, s9, "@You walk with the harlot to a private room to have some fun. The experience was very enjoyable and made you forget all about your troubles."),
    ],
    [
      ("harlot_services_continue",
      [
        (str_store_string, s0, "@And my Johnson became really itchy too..."),
      ], "{s0}",
      [
       
      ]) 
    ],
  ),



  
  ######################################################
  

]  #################################### END OF GAME MENUS BRACKET

import header_scenes
from template_tools import *
from module_scenes import scenes


sorted_scenes = sorted(scenes)
for i in xrange(len(sorted_scenes)):
  current_scene = list(sorted_scenes[i])
  current_scene[1] = get_flags_from_bitmap(header_scenes, "sf_", current_scene[1])
  sorted_scenes[i] = tuple(current_scene)

choose_scene_template = Game_Menu_Template(
  id="choose_scenes_",
  text="Choose a scene: (Page {current_page} of {num_pages})",
  optn_id="choose_scene_",
  optn_text="{list_item[0]}{list_item[1]}",
  optn_consq = [
    (jump_to_scene, "scn_{list_item[0]}"),
    (change_screen_mission)
  ]
)

game_menus += choose_scene_template.generate_menus(sorted_scenes)


# modmerger_start version=201 type=2
try:
    component_name = "game_menus"
    var_set = { "game_menus" : game_menus }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
