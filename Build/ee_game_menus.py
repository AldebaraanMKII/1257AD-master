from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *


game_menus = [
  
####### NEW v3.0-KOMKE START-Removed some spaces, changed string registers to avoid the s67 and up
   ("lance_recruitment",0,
   "{s40}^{s41}^{s42}^{s43}^{s44}^{s45}^{s46}^{s47}^{s48}^{s49}^{s50}^{s51}^{s52}^{s53}^{s54}^{s55}^{s56}^{s57}^{s58}^{s59}^{s60}^{s61}",
   "none",
   [
     (str_clear, s40),
     (str_clear, s41),
     (str_clear, s42),
     (str_clear, s43),
     (str_clear, s44),
     (str_clear, s45),
     (str_clear, s46),
     (str_clear, s47),
     (str_clear, s48),
     (str_clear, s49),
     (str_clear, s50),
     (str_clear, s51),
     (str_clear, s52),
     (str_clear, s53),
     (str_clear, s54),
     (str_clear, s55),
     (str_clear, s56),
     (str_clear, s57),
     (str_clear, s58),
     (str_clear, s59),
     (str_clear, s60),
     (str_clear, s61),
     
     (str_store_string, s40, "@There are no lances available for recruitment."),
     (str_store_string, s41, "@There is no local mercenary company available for hire."),
     
     (party_get_slot, reg20, "$current_town", slot_feudal_lances),
     (party_get_slot, reg21, "$current_town", slot_regional_mercs_number),
     (party_get_slot, reg22, "$current_town", slot_spec_mercs1_number),
     (party_get_slot, reg23, "$current_town", slot_spec_mercs2_number),
     # (party_get_slot, reg40, "$current_town", slot_regional_mercs2_number),
     # (party_get_slot, reg41, "$current_town", slot_regional_mercs3_number),

    ### Lance de-pluralization check (NEW v3.9.3, by Khanor) ###
    (try_begin),
      (eq, reg20, 1),
      (assign, reg0, 1),
    (else_try),
      (assign, reg0, 0),
    (try_end),
    ### Lance de-pluralization check end ###
    (try_begin),
      (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
      (this_or_next|eq, "$cheat_mode", 1),
      (eq, ":town_lord", "trp_player"),
      (str_store_string, s40, "@You currently have {reg20} lance{reg0?:s} available for recruitment."),
      (party_get_slot, reg24, "$current_town", slot_number_nobles),
      (party_get_slot, reg25, "$current_town", slot_number_commoner),
      (this_or_next|gt, reg24, 0),
      (gt, reg25, 0),
      (str_store_string, s40, "@You currently have {reg20} lance{reg0?:s} available for recruitment. Among them are {reg24} nobles and {reg25} commoners that have experience on the field of battle."),
    (try_end),
     
    (try_begin),
      (is_between, "$current_town", towns_begin, towns_end),
      (gt, reg21, 0),
      # (is_between,  "$current_town", towns_begin, towns_end),
      #  (party_get_slot, reg24, "$current_town", slot_number_nobles),
      #  (party_get_slot, reg25, "$current_town", slot_number_commoner),
      (str_store_string, s41, "@A local mercenary company is available for hire."),
    (try_end),
     
     (try_begin),
       (is_between, "$current_town", centers_begin, centers_end),
       (try_begin),
         (party_slot_ge, "$current_town", slot_center_has_quarters_genoese, 1),
         (str_store_string, s42, "@Genoese crossbowman are stationed here."),
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
         (str_store_string, s43, "@Turkopole mercenaries have an outpost here."),
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_camp_georgian, 1),
         (str_store_string, s44, "@Georgian mercenaries have a camp here."), 
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_camp_cuman, 1),
         (str_store_string, s45, "@Cuman mercenaries have a camp here."), 
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_quarters_brabantine, 1),
         (str_store_string, s46, "@Brabantine mercenaries are stationed here."), 
         
       (else_try),
         (party_slot_eq, "$current_town", slot_spec_mercs1, merc_sicily_muslims),
         (str_store_string, s47, "@Sicilian muslim mercenaries often pass-by here."),
         
       (else_try),
         (party_slot_eq, "$current_town", slot_spec_mercs1, generic_maghreb),
         (str_store_string, s48, "@Maghreb mercenaries often pass-by here."),        
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_camp_kwarezmian, 1),
         (str_store_string, s49, "@Kwarezmian mercenaries have a camp here."),    
         
       (else_try),
         (party_slot_eq, "$current_town", slot_spec_mercs1, merc_mordovian),
         (str_store_string, s50, "@Mordovian mercenaries often pass-by here."),    
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_camp_kipchak, 1),
         (str_store_string, s51, "@Kipchak mercenaries have a camp here."),    
         
       (else_try),
         (party_slot_ge, "$current_town", slot_center_has_outpost_finnish, 1),
         (str_store_string, s52, "@Finnish mercenaries have an outpost here."),    
       (try_end),
     (try_end),
     
     (try_begin),
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
         (try_begin),
           (party_slot_ge, "$current_town", slot_center_has_quarters_varangian, 1),
           (str_store_string, s53, "@The Varangians are stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_teutonic, 1),
           (str_store_string, s54, "@The Teutonic Order is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_hospitaller, 1),
           (str_store_string, s55, "@The Hospitalier Order is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_templar, 1),
           (str_store_string, s56, "@The Templar Order is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
           (str_store_string, s57, "@The Order of Saint Lazarus is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_santiago, 1),
           (str_store_string, s58, "@The Order of Santiago is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_calatrava, 1),
           (str_store_string, s59, "@The Order of Calatrava is stationed here."),
           
         (else_try),
           (party_slot_ge, "$current_town", slot_center_has_chapter_saint_thomas, 1),
           (str_store_string, s60, "@The Order of Saint Thomas is stationed here."),    
         (try_end),
     (try_end),
####### NEW v3.0-KOMKE END- 
    
     (set_background_mesh, "mesh_pic_recruits"),
      # (try_for_range, ":faction_at_war", kingdoms_begin, kingdoms_end),
       # (store_relation, ":relation", ":faction_no", ":faction_at_war"),
       # (lt, ":relation", 0),
       # (assign, reg9, 0),
     # (try_end),
   ],  
   [
#############################################   
     ("recruit_lance",
     [
       (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
       (this_or_next|eq, ":town_lord", "trp_player"),
       (eq, "$cheat_mode", 1),
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 10),
       (party_get_slot, ":manpower", "$current_town", slot_feudal_lances),
       (gt, ":manpower", 0), #more then one
       #(assign, reg10, ":manpower"),
       (store_faction_of_party, ":faction", "$current_town"),
       (call_script, "script_check_if_faction_is_at_war", ":faction"),
       (assign, reg5, 0),
       (str_clear, s1),
       (try_begin),
         (eq, reg0, 0), #faction is at war
         (assign, reg5, 500), #cost for one lance
         (str_store_string, s1, "@Cost: {reg5}"),
       (try_end),
       
       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg5),
     ], "Recruit one lance. {s1}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_feudal_lances),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_feudal_lances, ":manpower"),
       (call_script, "script_fill_lance", "$current_town", "p_main_party"),
       (call_script, "script_balance_lance_storage"),
       #(assign, ":spawned_party", reg0),
       #(call_script, "script_party_add_party", "p_main_party", ":spawned_party"),
       #(remove_party, ":spawned_party"),
       
       (try_begin),
         (gt, reg5, 0),
         (troop_remove_gold, "trp_player", reg5),
       (try_end),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
#############################################
     ("recruit_all_lances",
     [
       (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
       (eq, ":town_lord", "trp_player"),
       
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 20),
       (party_get_slot, ":manpower", "$current_town", slot_feudal_lances),
       (gt, ":manpower", 1), #more then 2
       (set_background_mesh, "mesh_pic_recruits"),
       #(assign, reg10, ":manpower"), #more then 2
       (store_faction_of_party, ":faction", "$current_town"),
       (call_script, "script_check_if_faction_is_at_war", ":faction"),
       (assign, reg6, 0),
       (str_clear, s2),
       (try_begin),
         (eq, reg0, 0), #faction is at war
         (assign, reg6, 500), #cost for one lance
         (val_mul, reg6, ":manpower"),
         (str_store_string, s2, "@Cost: {reg6}"),
       (try_end),
       
       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg6),
     ], "Recruit all of the lances. {s2}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_feudal_lances),
       (assign, ":cycle_cap", ":manpower"),
       (try_for_range, ":spin_da_shit", 0, ":cycle_cap"),
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 10),
         (call_script, "script_fill_lance", "$current_town", "p_main_party"),
         (call_script, "script_balance_lance_storage"),
         #(assign, ":spawned_party", reg0),
         #(call_script, "script_party_add_party", "p_main_party", ":spawned_party"),
         #(remove_party, ":spawned_party"),
         (val_sub, ":manpower", 1),
       (try_end),
       (party_set_slot, "$current_town", slot_feudal_lances, ":manpower"),
       
       (try_begin),
         (gt, reg6, 0),
         (troop_remove_gold, "trp_player", reg6),
       (try_end),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    
    
    ###############################
    ### --- MERCS - GENERIC --- ###
    ###############################
    ("recruit_company",
      [
        (is_between,  "$current_town", towns_begin, towns_end),
        (party_slot_ge, "$current_town", slot_regional_mercs_number, 1),
        (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
        (ge, ":free_capacity", 20), ### NEW v3.8
        # (party_get_slot, ":manpower", "$current_town", slot_regional_mercs_number),
        # (gt, ":manpower", 0), ### More than zero.
        # (store_faction_of_party, ":faction", "$current_town"),
        (call_script, "script_get_number_of_hero_centers", "trp_player"),
        # (assign, ":owned_centers", reg0),
        (assign, reg7, merc_cost),
        (str_clear, s1),
        (try_begin),
          (gt, reg0, 0), ### Is a lord
          (assign, reg7, merc_cost * 3), ### Cost for one company.
          
        (try_end),
        (store_party_size, ":party_size", "p_main_party"),
        (store_div, ":price_increase", ":party_size", 20),
        (val_add, ":price_increase", 1),
        (assign, reg0, ":price_increase"),
        # (display_message, "@price increase: {reg0}"),
        
        (try_begin),
          (eq, 0, 1), ### Lets disable this for now
          (gt, ":price_increase", 1),
          (val_mul, reg7, ":price_increase"),
        (try_end),

        (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
          (eq, "$background_type", cb_mercenary_captain),
          (ge, reg7, 5),

          (val_mul, reg7, 4),
          (val_div, reg7, 5),
        (try_end),

        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg7),
        (str_store_string, s3, "@Cost: {reg7}"),
      ], "Hire a local mercenary company. {s3}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_regional_mercs_number),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_regional_mercs_number, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg7, 0),
          (troop_remove_gold, "trp_player", reg7),
        (try_end),
        
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company", "$current_town", "p_main_party", slot_regional_mercs),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ################################
    ### --- NEW MERC OPTIONS --- ###
    ################################
    ("recruit_company_special_genoese",
      [
        (is_between,  "$current_town", towns_begin, towns_end),
        (party_slot_ge, "$current_town", slot_center_has_quarters_genoese, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_genoese),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),

              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s4, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
          (str_store_string, s20, "@Genoese Crossbowmen (Normal)"),
          # (assign, "$current_mercs", "pt_company_genoese_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 2),
          (str_store_string, s20, "@Genoese Crossbowmen (Large)"),
          # (assign, "$current_mercs", "pt_company_genoese_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 3),
          (str_store_string, s20, "@Genoese Crossbowmen (Very Large)"),
          # (assign, "$current_mercs", "pt_company_genoese_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s20}. {s4}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_genoese),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_genoese, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
          (assign, "$current_mercs", "pt_company_genoese_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 2),
          (assign, "$current_mercs", "pt_company_genoese_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 3),
          (assign, "$current_mercs", "pt_company_genoese_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_finnish",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_outpost_finnish, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_finnish),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s5, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 1),
          (str_store_string, s21, "@Finnish mercenaries (Normal)"),
          # (assign, "$current_mercs", "pt_company_finnish_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 2),
          (str_store_string, s21, "@Finnish mercenaries (Large)"),
          # (assign, "$current_mercs", "pt_company_finnish_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 3),
          (str_store_string, s21, "@Finnish mercenaries (Very Large)"),
          # (assign, "$current_mercs", "pt_company_finnish_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s21}. {s5}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_finnish),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_finnish, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 1),
          (assign, "$current_mercs", "pt_company_finnish_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 2),
          (assign, "$current_mercs", "pt_company_finnish_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_finnish, 3),
          (assign, "$current_mercs", "pt_company_finnish_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_turcopole",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
        ### NEW v3.5 - Only recruitable with Christian owners
        (store_faction_of_party, ":faction", "$current_town"),  
        (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
        (faction_slot_eq, ":faction", slot_faction_religion, religion_orthodox),  
        ######################################
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_turkopole),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s6, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
          (str_store_string, s22, "@Turcopoles (Normal)"),
          # (assign, "$current_mercs", "pt_company_turkopoles_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 2),
          (str_store_string, s22, "@Turcopoles (Large)"),
          # (assign, "$current_mercs", "pt_company_turkopoles_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 3),
          (str_store_string, s22, "@Turcopoles (Very Large)"),
          # (assign, "$current_mercs", "pt_company_turkopoles_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s22}. {s6}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_turkopole),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_turkopole, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
          (assign, "$current_mercs", "pt_company_turkopoles_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 2),
          (assign, "$current_mercs", "pt_company_turkopoles_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 3),
          (assign, "$current_mercs", "pt_company_turkopoles_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_georgians",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_camp_georgian, 1),
        ### NEW v3.5 - Only recruitable with Christian owners
        (store_faction_of_party, ":faction", "$current_town"),  
        (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
        (faction_slot_eq, ":faction", slot_faction_religion, religion_orthodox),  
        ######################################
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_georgian),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s6, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
          (str_store_string, s23, "@Georgians (Normal)"),
          # (assign, "$current_mercs", "pt_company_georgian_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 2),
          (str_store_string, s23, "@Georgians (Large)"),
          # (assign, "$current_mercs", "pt_company_georgian_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 3),
          (str_store_string, s23, "@Georgians (Very Large)"),
          # (assign, "$current_mercs", "pt_company_georgian_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s23}. {s6}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_georgian),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_georgian, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
          (assign, "$current_mercs", "pt_company_georgian_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 2),
          (assign, "$current_mercs", "pt_company_georgian_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 3),
          (assign, "$current_mercs", "pt_company_georgian_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_brabantine",
      [
        (is_between, "$current_town", towns_begin, towns_end),
        (party_slot_ge, "$current_town", slot_center_has_quarters_brabantine, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_brabantine),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), #lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s7, "@Cost: {reg8}"),
              ##################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
          (str_store_string, s24, "@Brabantine mercenaries (Normal)"),
          # (assign, "$current_mercs", "pt_company_brabantine_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 2),
          (str_store_string, s24, "@Brabantine mercenaries (Large)"),
          # (assign, "$current_mercs", "pt_company_brabantine_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 3),
          (str_store_string, s24, "@Brabantine mercenaries (Very Large)"),
          # (assign, "$current_mercs", "pt_company_brabantine_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ########################################
        (try_end),
      ], "Hire a company of {s24}. {s7}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_brabantine),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_brabantine, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
          (assign, "$current_mercs", "pt_company_brabantine_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 2),
          (assign, "$current_mercs", "pt_company_brabantine_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 3),
          (assign, "$current_mercs", "pt_company_brabantine_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_sicilian_muslims", ### Sicilian Mercenaries are back! (NEW v3.9.3a, by Khanor) ###
      [
        (is_between, "$current_town", towns_begin, towns_end),
        (this_or_next|party_slot_eq, "$current_town", slot_spec_mercs1, merc_sicily_muslims),
        (this_or_next|eq, "$current_town", "p_town_24_1"),
        (eq, "$current_town", "p_town_24_2"),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_sicily_muslims),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s7, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (ge, ":manpower", 1),
          (str_store_string, s25, "@Sicilian mercenaries (Normal)"),
          
        ######################################
        (try_end),
      ], "Hire a company of {s25}. {s7}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_sicily_muslims),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_sicily_muslims, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),

        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_spec_mercs1, merc_sicily_muslims),
          (assign, "$current_mercs", "pt_company_sicily"),
        (try_end),
        
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_welsh_kern",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_outpost_welsh_kern, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_welsh_kern),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
          (str_store_string, s26, "@Welsh mercenaries (Normal)"),
          # (assign, "$current_mercs", "pt_company_welsh_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 2),
          (str_store_string, s26, "@Welsh mercenaries (Large)"),
          # (assign, "$current_mercs", "pt_company_welsh_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 3),
          (str_store_string, s26, "@Welsh mercenaries (Very Large)"),
          # (assign, "$current_mercs", "pt_company_welsh_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s26}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_welsh_kern),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_welsh_kern, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
          (assign, "$current_mercs", "pt_company_welsh_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 2),
          (assign, "$current_mercs", "pt_company_welsh_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 3),
          (assign, "$current_mercs", "pt_company_welsh_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_gaelic",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_outpost_gaelic, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_gaelic),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 1),
          (str_store_string, s27, "@Gaelic mercenaries (Normal)"),
          # (assign, "$current_mercs", "pt_generic_gaelic_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 2),
          (str_store_string, s27, "@Gaelic mercenaries (Large)"),
          # (assign, "$current_mercs", "pt_generic_gaelic_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 3),
          (str_store_string, s27, "@Gaelic mercenaries (Very Large)"),
          # (assign, "$current_mercs", "pt_generic_gaelic_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s27}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_gaelic),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_gaelic, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 1),
          (assign, "$current_mercs", "pt_generic_gaelic_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 2),
          (assign, "$current_mercs", "pt_generic_gaelic_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_outpost_gaelic, 3),
          (assign, "$current_mercs", "pt_generic_gaelic_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_cuman",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_camp_cuman, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_cuman),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              #(display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this.
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
          (str_store_string, s28, "@Cumans (Normal)"),
          # (assign, "$current_mercs", "pt_company_cuman_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 2),
          (str_store_string, s28, "@Cumans (Large)"),
          # (assign, "$current_mercs", "pt_company_cuman_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 3),
          (str_store_string, s28, "@Cumans (Very Large)"),
          # (assign, "$current_mercs", "pt_company_cuman_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s28}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_cuman),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_cuman, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
          (assign, "$current_mercs", "pt_company_cuman_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 2),
          (assign, "$current_mercs", "pt_company_cuman_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 3),
          (assign, "$current_mercs", "pt_company_cuman_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_kipchak",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_camp_kipchak, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_kipchak),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
          (str_store_string, s29, "@Kipchaks (Normal)"),
          # (assign, "$current_mercs", "pt_company_kipchak_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 2),
          (str_store_string, s29, "@Kipchaks (Large)"),
          # (assign, "$current_mercs", "pt_company_kipchak_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 3),
          (str_store_string, s29, "@Kipchaks (Very Large)"),
          # (assign, "$current_mercs", "pt_company_kipchak_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s29}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_kipchak),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_kipchak, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
          (assign, "$current_mercs", "pt_company_kipchak_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 2),
          (assign, "$current_mercs", "pt_company_kipchak_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 3),
          (assign, "$current_mercs", "pt_company_kipchak_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_mordovians", ### Mordovian Mercenaries are back! (NEW v3.9.3a, by Khanor) ###
      [
        (is_between, "$current_town", towns_begin, towns_end),
        (party_slot_eq, "$current_town", slot_spec_mercs1, merc_mordovian),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mordovians),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s7, "@Cost: {reg8}"),
              ################################
        (try_begin),
          (ge, ":manpower", 1),
          (str_store_string, s30, "@Mordovians (Normal)"),
          
        ######################################
        (try_end),
      ], "Hire a company of {s30}. {s7}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mordovians),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_mordovians, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),

        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_spec_mercs1, merc_mordovian),
          (assign, "$current_mercs", "pt_company_mordovian"),
        (try_end),
        
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),

    

    ("recruit_company_special_mongol",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_camp_mongol, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mongol),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
          (str_store_string, s31, "@Mongols (Normal)"),
          # (assign, "$current_mercs", "pt_company_mongol_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 2),
          (str_store_string, s31, "@Mongols (Large)"),
          # (assign, "$current_mercs", "pt_company_mongol_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 3),
          (str_store_string, s31, "@Mongols (Very Large)"),
          # (assign, "$current_mercs", "pt_company_mongol_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s31}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mongol),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_mongol, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
          (assign, "$current_mercs", "pt_company_mongol_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 2),
          (assign, "$current_mercs", "pt_company_mongol_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 3),
          (assign, "$current_mercs", "pt_company_mongol_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),



    ("recruit_company_special_kwarezmian",
      [
        (is_between,  "$current_town", centers_begin, centers_end),
        (party_slot_ge, "$current_town", slot_center_has_camp_kwarezmian, 1),
          (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
          (ge, ":free_capacity", 20), ### NEW v3.8
            (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_kwarezmian),
            (gt, ":manpower", 0), ### More than zero.
              # (store_faction_of_party, ":faction", "$current_town"),
              (call_script, "script_get_number_of_hero_centers", "trp_player"),
              # (assign, ":owned_centers", reg0),
              (assign, reg8, merc_cost),
              (str_clear, s1),
              (try_begin),
                (gt, reg0, 0), ### Is a lord
                (assign, reg8, merc_cost * 3), ### Cost for one company.
              (try_end),
              (store_party_size, ":party_size", "p_main_party"),
              (store_div, ":price_increase", ":party_size", 20),
              (val_add, ":price_increase", 1),
              (assign, reg0, ":price_increase"),
              # (display_message, "@price increase: {reg0}"),
              
              (try_begin),
                (eq, 0, 1), ### Lets disable this
                (gt, ":price_increase", 1),
                (val_mul, reg8, ":price_increase"),
              (try_end),

              (try_begin), ### Players with the Mercenary Captain background now have a permanent 20% discount on the final value of mercenary companies! (NEW v3.9.3a, by Khanor) ###
                (eq, "$background_type", cb_mercenary_captain),
                (ge, reg8, 5),

                (val_mul, reg8, 4),
                (val_div, reg8, 5),
              (try_end),
              
              (store_troop_gold, ":gold", "trp_player"),
              (ge, ":gold", reg8),
              (str_store_string, s8, "@Cost: {reg8}"),
        ######################################
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
          (str_store_string, s32, "@Kwarezmians (Normal)"),
          # (assign, "$current_mercs", "pt_company_kwarezmian_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 2),
          (str_store_string, s32, "@Kwarezmians (Large)"),
          # (assign, "$current_mercs", "pt_company_kwarezmian_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 3),
          (str_store_string, s32, "@Kwarezmians (Very Large)"),
          # (assign, "$current_mercs", "pt_company_kwarezmian_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
          
        ######################################
        (try_end),
      ], "Hire a company of {s32}. {s8}",
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_kwarezmian),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs_number_kwarezmian, ":manpower"),
        # (call_script, "script_fill_lance", "$current_town", "p_main_party"),
        
        (try_begin),
          (gt, reg8, 0),
          (troop_remove_gold, "trp_player", reg8),
        (try_end),
        
        ### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
          (assign, "$current_mercs", "pt_company_kwarezmian_1"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 2),
          (assign, "$current_mercs", "pt_company_kwarezmian_2"),
        (else_try),
          (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 3),
          (assign, "$current_mercs", "pt_company_kwarezmian_3"),
        (try_end),
        ### NEW v3.0-KOMKE END- 
        # (party_set_slot, "$current_town", slot_regional_mercs, generic_euro), ### TEMP!!
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
            (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),
    


     ("recruit_crusaders_teutonic",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_teutonic, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_teutonic),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s33, "@The Teutonic Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_teutonic_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 2),
         (str_store_string, s33, "@The Teutonic Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_teutonic_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 3),
         (str_store_string, s33, "@The Teutonic Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_teutonic_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 4),
         (str_store_string, s33, "@The Teutonic Knights (Very Large)"),
         # (assign, "$current_mercs", "pt_company_teutonic_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
         
############################################
       (try_end),
     ], "Call upon {s33}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_teutonic),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_teutonic, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (assign, "$current_mercs", "pt_company_teutonic_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 2),
         (assign, "$current_mercs", "pt_company_teutonic_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 3),
         (assign, "$current_mercs", "pt_company_teutonic_3"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 4),
         (assign, "$current_mercs", "pt_company_teutonic_4"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_templar",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_templar, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_templar),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s34, "@The Templar Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_templar_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 2),
         (str_store_string, s34, "@The Templar Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_templar_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 3),
         (str_store_string, s34, "@The Templar Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_templar_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 4),
         (str_store_string, s34, "@The Templar Knights (Very Large)"),
         # (assign, "$current_mercs", "pt_company_templar_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
         
############################################
       (try_end),
     ], "Call upon {s34}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_templar),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_templar, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (assign, "$current_mercs", "pt_company_templar_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 2),
         (assign, "$current_mercs", "pt_company_templar_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 3),
         (assign, "$current_mercs", "pt_company_templar_3"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 4),
         (assign, "$current_mercs", "pt_company_templar_4"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_hospitaller",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_hospitaller, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_hospitaller),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s35, "@The Hospitaller Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_hospitaller_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 2),
         (str_store_string, s35, "@The Hospitaller Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_hospitaller_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 3),
         (str_store_string, s35, "@The Hospitaller Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_hospitaller_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 4),
         (str_store_string, s35, "@The Hospitaller Knights (Very Large)"),
         # (assign, "$current_mercs", "pt_company_hospitaller_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
         
############################################
       (try_end),
     ], "Call upon {s35}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_hospitaller),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_hospitaller, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (assign, "$current_mercs", "pt_company_hospitaller_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 2),
         (assign, "$current_mercs", "pt_company_hospitaller_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 3),
         (assign, "$current_mercs", "pt_company_hospitaller_3"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 4),
         (assign, "$current_mercs", "pt_company_hospitaller_4"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_saint_lazarus",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_saint_lazarus),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
         (str_store_string, s36, "@The Saint Lazarus Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 2),
         (str_store_string, s36, "@The Saint Lazarus Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 3),
         (str_store_string, s36, "@The Saint Lazarus Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s36}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_saint_lazarus),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_saint_lazarus, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
         (assign, "$current_mercs", "pt_company_saint_lazarus_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 2),
         (assign, "$current_mercs", "pt_company_saint_lazarus_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 3),
         (assign, "$current_mercs", "pt_company_saint_lazarus_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_santiago",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_santiago, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_santiago),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
         (str_store_string, s37, "@The Santiago Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_santiago_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 2),
         (str_store_string, s37, "@The Santiago Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_santiago_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 3),
         (str_store_string, s37, "@The Santiago Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_santiago_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s37}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_santiago),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_santiago, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
         (assign, "$current_mercs", "pt_company_santiago_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 2),
         (assign, "$current_mercs", "pt_company_santiago_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 3),
         (assign, "$current_mercs", "pt_company_santiago_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_calatrava",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_calatrava, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_calatrava),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
         (str_store_string, s38, "@The Calatrava Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_calatrava_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 2),
         (str_store_string, s38, "@The Calatrava Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_calatrava_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 3),
         (str_store_string, s38, "@The Calatrava Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_calatrava_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s38}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_calatrava),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_calatrava, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
         (assign, "$current_mercs", "pt_company_calatrava_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 2),
         (assign, "$current_mercs", "pt_company_calatrava_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 3),
         (assign, "$current_mercs", "pt_company_calatrava_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusaders_saint_thomas",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_saint_thomas, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_saint_thomas),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
         (str_store_string, s39, "@The Saint Thomas Knights (Small)"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 2),
         (str_store_string, s39, "@The Saint Thomas Knights (Medium)"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 3),
         (str_store_string, s39, "@The Saint Thomas Knights (Large)"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s39}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_saint_thomas),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_saint_thomas, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
         (assign, "$current_mercs", "pt_company_saint_thomas_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 2),
         (assign, "$current_mercs", "pt_company_saint_thomas_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 3),
         (assign, "$current_mercs", "pt_company_saint_thomas_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_spec2_varangians",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_quarters_varangian, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_orthodox),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_varangian),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
         (str_store_string, s40, "@The Varangians (Normal)"),
         # (assign, "$current_mercs", "pt_company_varangian_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 2),
         (str_store_string, s40, "@The Varangians (Large)"),
         # (assign, "$current_mercs", "pt_company_varangian_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
          
############################################
       (try_end),
     ], "Call upon {s40}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_varangian),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_varangian, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
         (assign, "$current_mercs", "pt_company_varangian_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 2),
         (assign, "$current_mercs", "pt_company_varangian_2"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_spec2_cataphract",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_quarters_cataphract, 1),
	   ###### NEW v3.5 - only recruitable with christian owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_orthodox),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_cataphract),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 1),
         (str_store_string, s41, "@The Cataphracts (Small)"),
         # (assign, "$current_mercs", "pt_company_cataphract_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 2),
         (str_store_string, s41, "@The Cataphracts (Medium)"),
         # (assign, "$current_mercs", "pt_company_cataphract_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 3),
         (str_store_string, s41, "@The Cataphracts (Large)"),
         # (assign, "$current_mercs", "pt_company_cataphract_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s41}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_cataphract),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_cataphract, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 1),
         (assign, "$current_mercs", "pt_company_cataphract_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 2),
         (assign, "$current_mercs", "pt_company_cataphract_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_cataphract, 3),
         (assign, "$current_mercs", "pt_company_cataphract_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_spec2_mamluk",
     [
       (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
       (party_slot_ge, "$current_town", slot_center_has_quarters_mamluk, 1),
	   ###### NEW v3.5 - only recruitable with muslim owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_muslim),  
	   ########################
         (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
         (ge, ":free_capacity", 20), ####### NEW v3.8
           (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mamluk),
           (gt, ":manpower", 0), #more then one
             #(store_faction_of_party, ":faction", "$current_town"),
           (assign, reg9, 4000), #cost for one company
           #(try_end),
           # (store_party_size, ":party_size", "p_main_party"),
           # (store_div, ":price_increase", ":party_size", 20),
           
           (store_troop_gold, ":gold", "trp_player"),
           (ge, ":gold", reg9),
           (str_store_string, s9, "@Cost: {reg9}"),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
         (str_store_string, s42, "@The Mamluks (Small)"),
         # (assign, "$current_mercs", "pt_company_mamlukes_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 2),
         (str_store_string, s42, "@The Mamluks (Medium)"),
         # (assign, "$current_mercs", "pt_company_mamlukes_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 3),
         (str_store_string, s42, "@The Mamluks (Large)"),
         # (assign, "$current_mercs", "pt_company_mamlukes_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
############################################
       (try_end),
     ], "Call upon {s42}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_mamluk),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_mamluk, ":manpower"),
       #(call_script, "script_fill_lance", "$current_town", "p_main_party"),
       
       (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
         (assign, "$current_mercs", "pt_company_mamlukes_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 2),
         (assign, "$current_mercs", "pt_company_mamlukes_2"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 3),
         (assign, "$current_mercs", "pt_company_mamlukes_3"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       ##(party_set_slot, "$current_town", slot_regional_mercs, generic_euro), #######TEMP!!
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    ###MERCS END
     
     

################ NEW CRUSADER AUXILIARY TROOPS (SPEARMEN AND CROSSBOWMEN)
     ("recruit_crusader_aux_teutonic",
     [
       (is_between,  "$current_town", towns_begin, towns_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_teutonic, 1),
	   ###### NEW v3.5 - only recruitable with catholic owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       # (faction_slot_eq, ":faction", slot_faction_religion, religion_muslim),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 20), ####### NEW v3.8
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_teutonic_aux),
       (gt, ":manpower", 0), #more then one
       (store_faction_of_party, ":faction", "$current_town"),
       #(eq, ":faction", "fac_kingdom_23"),
       (eq, ":faction", "$players_kingdom"), #same faction ##

       #(call_script, "script_get_number_of_hero_centers", "trp_player"),
       #(assign, ":owned_centers", reg0),
       #(assign, reg9, 3000),
       (str_clear, s1),
       #(try_begin),
         #(gt, reg0, 0), #is a lord
         (assign, reg9, 4000), #cost for one company
       #(try_end),
       # (store_party_size, ":party_size", "p_main_party"),
       # (store_div, ":price_increase", ":party_size", 20),
       
       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg9),
       (str_store_string, s9, "@Cost: {reg9}"),
       
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s43, "@The Teutonic Knights Auxiliaries (Normal)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_teutonic_aux_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block

      (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 2),
         (str_store_string, s43, "@The Teutonic Knights Auxiliaries (Large)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_teutonic_aux_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (try_end),
       
     ], "Call upon {s43}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_teutonic_aux),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_teutonic_aux, ":manpower"),
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (assign, "$current_mercs", "pt_company_teutonic_aux_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 2),
         (assign, "$current_mercs", "pt_company_teutonic_aux_2"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       
       
        (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusader_aux_templar",
     [
       (is_between,  "$current_town", towns_begin, towns_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_templar, 1),
	   ###### NEW v3.5 - only recruitable with catholic owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       # (faction_slot_eq, ":faction", slot_faction_religion, religion_muslim),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 20), ####### NEW v3.8
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_templar_aux),
       (gt, ":manpower", 0), #more then one
       (store_faction_of_party, ":faction", "$current_town"),
       #(eq, ":faction", "fac_kingdom_23"),
       (eq, ":faction", "$players_kingdom"), #same faction ##

       #(call_script, "script_get_number_of_hero_centers", "trp_player"),
       #(assign, ":owned_centers", reg0),
       #(assign, reg9, 3000),
       (str_clear, s1),
       #(try_begin),
         #(gt, reg0, 0), #is a lord
         (assign, reg9, 4000), #cost for one company
       #(try_end),
       # (store_party_size, ":party_size", "p_main_party"),
       # (store_div, ":price_increase", ":party_size", 20),
       
       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg9),
       (str_store_string, s9, "@Cost: {reg9}"),
       
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s44, "@The Knights Templar Auxiliaries (Normal)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_templar_aux_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 2),
         (str_store_string, s44, "@The Knights Templar Auxiliaries (Large)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_templar_aux_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (try_end),
       
     ], "Call upon {s44}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_templar_aux),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_templar_aux, ":manpower"),
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (assign, "$current_mercs", "pt_company_templar_aux_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 2),
         (assign, "$current_mercs", "pt_company_templar_aux_2"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       
       
        (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    


     ("recruit_crusader_aux_hospitaller",
     [
       (is_between,  "$current_town", towns_begin, towns_end),
       (party_slot_ge, "$current_town", slot_center_has_chapter_hospitaller, 1),
	   ###### NEW v3.5 - only recruitable with catholic owners
       (store_faction_of_party, ":faction", "$current_town"),  
       # (this_or_next|faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
       # (faction_slot_eq, ":faction", slot_faction_religion, religion_muslim),  
       (faction_slot_eq, ":faction", slot_faction_religion, religion_catholic),  
	   ########################
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 20), ####### NEW v3.8
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_hospitaller_aux),
       (gt, ":manpower", 0), #more then one
       (store_faction_of_party, ":faction", "$current_town"),
       #(eq, ":faction", "fac_kingdom_23"),
       (eq, ":faction", "$players_kingdom"), #same faction ##

       #(call_script, "script_get_number_of_hero_centers", "trp_player"),
       #(assign, ":owned_centers", reg0),
       #(assign, reg9, 3000),
       (str_clear, s1),
       #(try_begin),
         #(gt, reg0, 0), #is a lord
         (assign, reg9, 4000), #cost for one company
       #(try_end),
       # (store_party_size, ":party_size", "p_main_party"),
       # (store_div, ":price_increase", ":party_size", 20),
       
       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg9),
       (str_store_string, s9, "@Cost: {reg9}"),
       
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s45, "@The Knights Hospitaller Auxiliaries (Normal)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_hospitaller_aux_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
         
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 2),
         (str_store_string, s45, "@The Knights Hospitaller Auxiliaries (Large)"),####### NEW v3.0-KOMKE
         # (assign, "$current_mercs", "pt_company_hospitaller_aux_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (try_end),
       
     ], "Call upon {s45}. {s9}",
     [
       (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_hospitaller_aux),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$current_town", slot_spec_mercs_number_hospitaller_aux, ":manpower"),
####### NEW v3.0-KOMKE START-mercs assigned in consequences block
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (assign, "$current_mercs", "pt_company_hospitaller_aux_1"),
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 2),
         (assign, "$current_mercs", "pt_company_hospitaller_aux_2"),
       (try_end),
####### NEW v3.0-KOMKE END- 
       (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
       
       
       
        (try_begin),
         (gt, reg9, 0),
         (troop_remove_gold, "trp_player", reg9),
       (try_end),
       
       
       (try_begin),
         (gt, ":manpower", 0),
         (jump_to_menu, "mnu_lance_recruitment"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
     
     
############################################################
    
############################################################


    #################################################################################
    #### This adds recruitable knights from jousting lists/tournament grounds --- ###
    #################################################################################
    ("recruit_knights_tournament",
      [
        (is_between,  "$current_town", walled_centers_begin, walled_centers_end),
        (store_faction_of_party, ":cur_fief_faction", "$current_town"),
        ############ only factions with knights can have this
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_western"),
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_teutonic"),
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_nordic"),
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_iberian"),
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_gaelic"),
        (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_welsh"),
        (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_italian"),
        # (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_player"),
        
        (this_or_next|party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
        (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
        
        (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
        (ge, ":free_capacity", 20), ####### NEW v3.8
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs_number_tournament_knights),
        (gt, ":manpower", 0), #more then one
        (store_faction_of_party, ":faction", "$current_town"),
        #(eq, ":faction", "fac_kingdom_23"),
        (eq, ":faction", "$players_kingdom"), #same faction ##

        #(call_script, "script_get_number_of_hero_centers", "trp_player"),
        #(assign, ":owned_centers", reg0),
        #(assign, reg9, 3000),
        (str_clear, s1),
        #(try_begin),
          #(gt, reg0, 0), #is a lord
          (assign, reg9, 3000), #cost for one company
        #(try_end),
        # (store_party_size, ":party_size", "p_main_party"),
        # (store_div, ":price_increase", ":party_size", 20),
        
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", reg9),
        (str_store_string, s5, "@Cost: {reg9}"),
  #######################################
  ####### NEW v3.0-KOMKE START-
        (str_clear, s46),####### NEW v3.0-KOMKE otherwise the register was overwritten
        (str_clear, s47),
        (str_clear, s48),####### NEW v3.0-KOMKE there are 6 knight options
        (str_clear, s49),
        (str_clear, s50),
        (str_clear, s51),
        (try_begin),
          (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_western"),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_teutonic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s46, "@Euro Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_euro_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_western"),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_teutonic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s46, "@Euro Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_euro_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block

          
  #######################################
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_nordic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s47, "@Scandinavian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_scandinavian_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_nordic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s47, "@Scandinavian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_scandinavian_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
          
  #######################################
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_iberian"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s48, "@Iberian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_iberian_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
        
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_iberian"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s48, "@Iberian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_iberian_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
          
  #######################################
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_gaelic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s49, "@Gaelic Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_gaelic_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
        
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_gaelic"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s49, "@Gaelic Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_gaelic_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
          
  #######################################
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_welsh"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s50, "@Welsh Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_welsh_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
        
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_welsh"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s50, "@Welsh Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_welsh_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
          
          
  #######################################
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_italian"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (str_store_string, s51, "@Italian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_italian_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
        
        (else_try),
          (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_italian"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (str_store_string, s51, "@Italian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_italian_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block

          
  ###################################### CTT TROOPS
        # (else_try),
          # (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_player"),
          # (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          # (str_store_string, s51, "@Italian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_italian_1"),
        
        # (else_try),
          # (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, "fac_culture_player"),
          # (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          # (str_store_string, s51, "@Italian Knights"),
          # (assign, "$current_mercs", "pt_company_knights_tournament_italian_2"),
    (try_end),  
      # ], "Recruit {s51}. {s5}",
      ], "Recruit the following knights {s46}-{s47}-{s48}-{s40}-{s50}-{s51}. Cost = {s5}",
  ####### NEW v3.0-KOMKE END-
      [
        (party_get_slot, ":manpower", "$current_town", slot_spec_mercs2_number),
        (val_sub, ":manpower", 1),
        (party_set_slot, "$current_town", slot_spec_mercs2_number, ":manpower"),
  ####### NEW v3.0-KOMKE START-mercs assigned in consequences block
        (try_begin),
          (eq, s46, "@Euro Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_euro_1"),
        (else_try),
          (eq, s46, "@Euro Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_euro_2"),
        (else_try),
          (eq, s47, "@Scandinavian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_scandinavian_1"),
        (else_try),
          (eq, s47, "@Scandinavian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_scandinavian_2"),
        (else_try),
          (eq, s48, "@Iberian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_iberian_1"),
        (else_try),
          (eq, s48, "@Iberian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_iberian_2"),
        (else_try),
          (eq, s49, "@Gaelic Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_gaelic_1"),
        (else_try),
          (eq, s49, "@Gaelic Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_gaelic_2"),
        (else_try),
          (eq, s50, "@Welsh Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_welsh_1"),
        (else_try),
          (eq, s50, "@Welsh Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_welsh_2"),
        (else_try),
          (eq, s51, "@Italian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_1_jousting_lists, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_italian_1"),
        (else_try),
          (eq, s51, "@Italian Knights"),
          (party_slot_eq, "$current_town", slot_center_has_tier_2_tournament_grounds, 1),
          (assign, "$current_mercs", "pt_company_knights_tournament_italian_2"),
        (try_end),
  ####### NEW v3.0-KOMKE END- 
        (call_script, "script_fill_company_new", "$current_town", "p_main_party", "$current_mercs"),
        
        
        
        (try_begin),
          (gt, reg9, 0),
          (troop_remove_gold, "trp_player", reg9),
        (try_end),
        
        
        (try_begin),
          (gt, ":manpower", 0),
          (jump_to_menu, "mnu_lance_recruitment"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_ee_recruits_garrison_options"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
      ]
    ),
############################################################



     
     ("camp_disband_lances",[
     (eq, "$use_feudal_lance", 1),
     (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
     ], "Disband lance forces.",
       [
         (assign, "$g_next_menu", "mnu_lance_recruitment"),
         (jump_to_menu, "mnu_disband_lances"),
         
        ]
       ),
     
     ("go_back",
     [
       
     ], "Go back.",
     [
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
         # (jump_to_menu, "mnu_town"),
         (jump_to_menu, "mnu_ee_recruits_garrison_options"), ######## NEW v3.5
       # (else_try),
         # (party_slot_eq, "$current_town", slot_party_type, spt_castle),
         # (jump_to_menu, "mnu_town"),
       (else_try),
         (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
   ]
  ),   
  
   ##
   ("lance_prison",0,
   "Garrison management for {s0}^ Currently garrison is controlled and maintained {s1}",
   "none",
   [
    (str_store_party_name, s0, "$current_town"),
    (try_begin),
      (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
      (str_store_string, s1, "@by the townsmen"),
    (else_try),
      (str_store_string, s1, "@by the the lord"),
    (try_end),
    (assign, "$g_move_heroes", 1),
    (try_begin),
      (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
      (call_script, "script_party_prisoners_add_party_prisoners", "$current_town", "p_temp_party"),
      (call_script, "script_party_remove_all_prisoners", "p_temp_party"),
      (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),    
      (party_clear, "p_temp_party"),
    (try_end),

    (set_background_mesh, "mesh_pic_siege_sighted_fem"),
   ],
   
   [
     ("trade_prisoners",
     [
       (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
     ], "Trade prisoners.",
     [
       (call_script, "script_party_prisoners_add_party_prisoners", "p_temp_party", "$current_town"), 
       (call_script, "script_party_remove_all_prisoners", "$current_town"),
       (assign, "$g_next_menu", "mnu_lance_prison"),
       (change_screen_exchange_members, 1, "p_temp_party"),
     ]),
     
     ("adjust_garrison",
     [
       (party_slot_eq, "$current_town", slot_garrison_control, lord_controled),
     ], "Inspect the garrison.",
     [
       (change_screen_exchange_members,1),
     ]),

     ("garrison_control_player",
     [
       (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
     # ], "Take control of the garrison (Warning: this will disband current garrison).",
     ], "Take control of the garrison (Warning: This will disband current garrison if option in EE menu is checked.)",
     [
       (party_set_slot, "$current_town", slot_garrison_control, lord_controled),      
       (try_begin),
         (eq, "$g_misc_garrison_dont_disband_troops_when_taking_control", 0),
           (call_script, "script_party_remove_all_companions", "$current_town"),
       (try_end),
	   ##### NEW v2.9 - disabled
       # (try_begin),
         # (neg|is_between, "$current_town", castles_begin, castles_end),
         # (call_script, "script_change_player_relation_with_center", "$current_town", -10),
         # (display_message, "@The commoners are angry you take away their rights!", 0xff0000),
         # (play_sound, "snd_quest_failed"),
       # (try_end),
	   ###################
       
     ]),
     
     ("garrison_control_ai",
     [
       (party_slot_eq, "$current_town", slot_garrison_control, lord_controled),
     ], "Give control of the garrison to the local settlement. (Warning: This will disband current garrison.)",
     [
       (party_set_slot, "$current_town", slot_garrison_control, town_controled),
       #remove the rest
       (eq, "$g_misc_garrison_dont_disband_troops_when_taking_control", 0),  ##### NEW v2.9
         (call_script, "script_party_remove_all_companions", "$current_town"), 
         (call_script, "script_cf_reinforce_party", "$current_town"),
         (call_script, "script_cf_reinforce_party", "$current_town"),
         (call_script, "script_cf_reinforce_party", "$current_town"),
         (play_sound, "snd_quest_succeeded"),
     ]),

     ("garrison_control_hire_local_merc",
     [
        (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
        (party_slot_ge, "$current_town", slot_regional_mercs, 1),
        (party_slot_ge, "$current_town", slot_regional_mercs_number, 1),
        (assign, reg5, 3000),
     ], "Hire local mercenaries to the town garrison, cost: {reg5}",
     [
        (try_begin),
          (store_troop_gold, ":gold", "trp_player"),
          (lt, ":gold", reg5),
          (display_message, "@You do not have enough gold!", 0xff0000),    
        ######## NEW v3.0		  
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_town),
          (store_party_size_wo_prisoners, ":party_size", "$current_town"),
          (ge, ":party_size", "$g_party_garrison_max_size_towns"),
          (display_message, "@Town garrison if full and can not hire additional men!", 0xff0000),
        (else_try),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (store_party_size_wo_prisoners, ":party_size", "$current_town"),
          (ge, ":party_size", "$g_party_garrison_max_size_castles"),
          (display_message, "@Castle garrison if full and can not hire additional men!", 0xff0000),
        ################
        (else_try),
          (troop_remove_gold, "trp_player", reg5),
          
          (party_get_slot, ":mercs_number", "$current_town", slot_regional_mercs_number),
          # (party_get_slot, ":company_template", "$current_town", slot_regional_party_template),####### NEW v3.0-KOMKE not used
        
          (val_sub, ":mercs_number", 1),
          (party_set_slot, "$current_town", slot_regional_mercs_number, ":mercs_number"),
          (call_script, "script_fill_company", "$current_town", "$current_town", slot_regional_mercs),
        (try_end),
     ]),
     
     ("garrison_control_hire_merc_1",
     [
        (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
        (party_slot_ge, "$current_town", slot_spec_mercs1, 1),
        (party_slot_ge, "$current_town", slot_spec_mercs1_number, 1),
        (assign, reg6, 3000),
      ### NEW v3.0-KOMKE START- ###
        (str_clear, s52), ### NEW v3.0-KOMKE otherwise the register was overwritten
        (str_clear, s53),
        (str_clear, s54), ### NEW v3.0-KOMKE there are 11 mercenary options
        (str_clear, s55),
        (str_clear, s56),
        (str_clear, s57),
        (str_clear, s58),
        (str_clear, s59),
        (str_clear, s60),
        (str_clear, s61),
        (str_clear, s62),
      ######################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
         (str_store_string, s52, "@Genoese crossbowmen"),
         # (assign, "$current_mercs", "pt_company_genoese_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
         (str_store_string, s52, "@Genoese crossbowmen"),
         # (assign, "$current_mercs", "pt_company_genoese_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
         (str_store_string, s52, "@Genoese crossbowmen"),
         # (assign, "$current_mercs", "pt_company_genoese_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
         (str_store_string, s53, "@Turkopoles"),
         # (assign, "$current_mercs", "pt_company_turkopoles_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
         (str_store_string, s53, "@Turkopoles"),
         # (assign, "$current_mercs", "pt_company_turkopoles_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
         (str_store_string, s53, "@Turkopoles"),
         # (assign, "$current_mercs", "pt_company_turkopoles_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
         (str_store_string, s54, "@Georgians"),
         # (assign, "$current_mercs", "pt_company_georgian_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
         (str_store_string, s54, "@Georgians"),
         # (assign, "$current_mercs", "pt_company_georgian_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
         (str_store_string, s54, "@Georgians"),
         # (assign, "$current_mercs", "pt_company_georgian_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
         (str_store_string, s55, "@Cumans"),
         # (assign, "$current_mercs", "pt_company_cuman_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
         (str_store_string, s55, "@Cumans"),
         # (assign, "$current_mercs", "pt_company_cuman_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
         (str_store_string, s55, "@Cumans"),
         # (assign, "$current_mercs", "pt_company_cuman_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
         (str_store_string, s56, "@Brabantines"),
         # (assign, "$current_mercs", "pt_company_brabantine_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
         (str_store_string, s56, "@Brabantines"),
         # (assign, "$current_mercs", "pt_company_brabantine_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
         (str_store_string, s56, "@Brabantines"),
         # (assign, "$current_mercs", "pt_company_brabantine_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_spec_mercs1, merc_sicily_muslims),
         (str_store_string, s57, "@Sicilian Muslims"),
         # (assign, "$current_mercs", "pt_company_templar_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
         (str_store_string, s58, "@Welsh archers"),
         # (assign, "$current_mercs", "pt_company_welsh_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
         (str_store_string, s58, "@Welsh archers"),
         # (assign, "$current_mercs", "pt_company_welsh_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
         (str_store_string, s58, "@Welsh archers"),
         # (assign, "$current_mercs", "pt_company_welsh_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
         (str_store_string, s59, "@Kipchaks"),
         # (assign, "$current_mercs", "pt_company_kipchak_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
         (str_store_string, s59, "@Kipchaks"),
         # (assign, "$current_mercs", "pt_company_kipchak_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
         (str_store_string, s59, "@Kipchaks"),
         # (assign, "$current_mercs", "pt_company_kipchak_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_spec_mercs1, merc_mordovian),
         (str_store_string, s60, "@Mordovians"),
         # (assign, "$current_mercs", "pt_company_mordovian"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
         (str_store_string, s61, "@Kwarezmians"),
         # (assign, "$current_mercs", "pt_company_kwarezmian_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
         (str_store_string, s61, "@Kwarezmians"),
         # (assign, "$current_mercs", "pt_company_kwarezmian_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
         (str_store_string, s61, "@Kwarezmians"),
         # (assign, "$current_mercs", "pt_company_kwarezmian_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
         (str_store_string, s62, "@Mongols"),
         # (assign, "$current_mercs", "pt_company_mongol_1"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
         (str_store_string, s62, "@Mongols"),
         # (assign, "$current_mercs", "pt_company_mongol_2"), ### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
         (str_store_string, s62, "@Mongols"),
         # (assign, "$current_mercs", "pt_company_mongol_3"), ### NEW v3.0-KOMKE mercs assigned in consequences block
      ######################################
    (try_end),
     # ], "Hire {s20} mercenaries to the town garrison, cost: {reg6}",
     ], "Hire to the town garrison the following mercenaries: {s52}-{s53}-{s54}-{s55}-{s56}-{s57}-{s58}-{s59}-{s60}-{s61}-{s62}, cost: {reg6}",
     [
        (try_begin),
          (store_troop_gold, ":gold", "trp_player"),
          (lt, ":gold", reg6),
          (display_message, "@You do not have enough gold!", 0xff0000),
        (else_try),
          (store_party_size_wo_prisoners, ":party_size", "$current_town"),
          (ge, ":party_size", "$g_party_garrison_max_size_towns"),
          (display_message, "@Town garrison is full and can not hire additional men!", 0xff0000),
        (else_try),
          (troop_remove_gold, "trp_player", reg6),
          (party_get_slot, ":mercs_number", "$current_town", slot_spec_mercs1_number),
          # (party_get_slot, ":company_template", "$current_town", slot_regional_party_template),####### NEW v3.0-KOMKE not used
          (val_sub, ":mercs_number", 1),
          (party_set_slot, "$current_town", slot_spec_mercs1_number, ":mercs_number"),
           (try_begin),
             # (eq, s52, "@Genoese crossbowmen"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
             (assign, "$current_mercs", "pt_company_genoese_1"),
           (else_try),
             # (eq, s52, "@Genoese crossbowmen"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
             (assign, "$current_mercs", "pt_company_genoese_2"),
           (else_try),
             # (eq, s52, "@Genoese crossbowmen"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_genoese, 1),
             (assign, "$current_mercs", "pt_company_genoese_3"),
           (else_try),
             # (eq, s53, "@Turkopoles"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
             (assign, "$current_mercs", "pt_company_turkopoles_1"),
           (else_try),
             # (eq, s53, "@Turkopoles"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
             (assign, "$current_mercs", "pt_company_turkopoles_2"),
           (else_try),
             # (eq, s53, "@Turkopoles"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_crusader_turcopole, 1),
             (assign, "$current_mercs", "pt_company_turkopoles_3"),
           (else_try),
             # (eq, s54, "@Georgians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
             (assign, "$current_mercs", "pt_company_georgian_1"),
           (else_try),
             # (eq, s54, "@Georgians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
             (assign, "$current_mercs", "pt_company_georgian_2"),
           (else_try),
             # (eq, s54, "@Georgians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_georgian, 1),
             (assign, "$current_mercs", "pt_company_georgian_3"),
           (else_try),
             # (eq, s55, "@Cumans"),
             (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
             (assign, "$current_mercs", "pt_company_cuman_1"),
           (else_try),
             # (eq, s55, "@Cumans"),
             (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
             (assign, "$current_mercs", "pt_company_cuman_2"),
           (else_try),
             # (eq, s55, "@Cumans"),
             (party_slot_eq, "$current_town", slot_center_has_camp_cuman, 1),
             (assign, "$current_mercs", "pt_company_cuman_3"),
           (else_try),
             # (eq, s56, "@Brabantines"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
             (assign, "$current_mercs", "pt_company_brabantine_1"),
           (else_try),
             # (eq, s56, "@Brabantines"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
             (assign, "$current_mercs", "pt_company_brabantine_2"),
           (else_try),
             # (eq, s56, "@Brabantines"),
             (party_slot_eq, "$current_town", slot_center_has_quarters_brabantine, 1),
             (assign, "$current_mercs", "pt_company_brabantine_3"),
           (else_try),
             # (eq, s57, "@Sicily Muslims"),
             (party_slot_eq, "$current_town", slot_spec_mercs1, merc_sicily_muslims),
             (assign, "$current_mercs", "pt_company_sicily"),
           (else_try),
             # (eq, s58, "@Welsh archers"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
             (assign, "$current_mercs", "pt_company_welsh_1"),
           (else_try),
             # (eq, s58, "@Welsh archers"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
             (assign, "$current_mercs", "pt_company_welsh_2"),
           (else_try),
             # (eq, s58, "@Welsh archers"),
             (party_slot_eq, "$current_town", slot_center_has_outpost_welsh_kern, 1),
             (assign, "$current_mercs", "pt_company_welsh_3"),
           (else_try),
             # (eq, s59, "@Kipchaks"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
             (assign, "$current_mercs", "pt_company_kipchak_1"),
           (else_try),
             # (eq, s59, "@Kipchaks"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
             (assign, "$current_mercs", "pt_company_kipchak_2"),
           (else_try),
             # (eq, s59, "@Kipchaks"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kipchak, 1),
             (assign, "$current_mercs", "pt_company_kipchak_3"),
           (else_try),
             # (eq, s60, "@Mordovians"),
             (party_slot_eq, "$current_town", slot_spec_mercs1, merc_mordovian),
             (assign, "$current_mercs", "pt_company_mordovian"),
           (else_try),
             # (eq, s61, "@Kwarezmians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
             (assign, "$current_mercs", "pt_company_kwarezmian_1"),
           (else_try),
             # (eq, s61, "@Kwarezmians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
             (assign, "$current_mercs", "pt_company_kwarezmian_2"),
           (else_try),
             # (eq, s61, "@Kwarezmians"),
             (party_slot_eq, "$current_town", slot_center_has_camp_kwarezmian, 1),
             (assign, "$current_mercs", "pt_company_kwarezmian_3"),
           (else_try),
             # (eq, s62, "@Mongols"),
             (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
             (assign, "$current_mercs", "pt_company_mongol_1"),
           (else_try),
             # (eq, s62, "@Mongols"),
             (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
             (assign, "$current_mercs", "pt_company_mongol_2"),
           (else_try),
             # (eq, s62, "@Mongols"),
             (party_slot_eq, "$current_town", slot_center_has_camp_mongol, 1),
             (assign, "$current_mercs", "pt_company_mongol_3"),
           (try_end),
####### NEW v3.0-KOMKE END- 
        (call_script, "script_fill_company_new", "$current_town", "$current_town", "$current_mercs"),
    (try_end),
     ]),
     
     ("garrison_control_hire_merc_2",
     [
####### NEW v3.0-KOMKE BEGIN- 
        (party_slot_eq, "$current_town", slot_garrison_control, town_controled),
        (party_slot_ge, "$current_town", slot_spec_mercs2, 1),
        (party_slot_ge, "$current_town", slot_spec_mercs2_number, 1),
        (assign, reg7, 4000),
        (str_clear, s11),## otherwise the register was overwritten
        (str_clear, s12),
        (str_clear, s13),## there are 9 mercenary options
        (str_clear, s14),
        (str_clear, s15),
        (str_clear, s16),
        (str_clear, s17),
        (str_clear, s18),
        (str_clear, s19),
############################################
       (try_begin),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s11, "@The Knights Templar"),
         # (assign, "$current_mercs", "pt_company_templar_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s11, "@The Knights Templar"),
         # (assign, "$current_mercs", "pt_company_templar_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s11, "@The Knights Templar"),
         # (assign, "$current_mercs", "pt_company_templar_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
         (str_store_string, s11, "@The Knights Templar"),
         # (assign, "$current_mercs", "pt_company_templar_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s12, "@The Knights Hospitalier"),
         # (assign, "$current_mercs", "pt_company_hospitaller_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s12, "@The Knights Hospitalier"),
         # (assign, "$current_mercs", "pt_company_hospitaller_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s12, "@The Knights Hospitalier"),
         # (assign, "$current_mercs", "pt_company_hospitaller_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
         (str_store_string, s12, "@The Knights Hospitalier"),
         # (assign, "$current_mercs", "pt_company_hospitaller_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
         (str_store_string, s13, "@The Knights of Saint Lazarus"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
         (str_store_string, s13, "@The Knights of Saint Lazarus"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
         (str_store_string, s13, "@The Knights of Saint Lazarus"),
         # (assign, "$current_mercs", "pt_company_saint_lazarus_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
         (str_store_string, s14, "@The Knights of Santiago"),
         # (assign, "$current_mercs", "pt_company_santiago_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
         (str_store_string, s14, "@The Knights of Santiago"),
         # (assign, "$current_mercs", "pt_company_santiago_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
         (str_store_string, s14, "@The Knights of Santiago"),
         # (assign, "$current_mercs", "pt_company_santiago_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
         (str_store_string, s15, "@The Knights of Calatrava"),
         # (assign, "$current_mercs", "pt_company_calatrava_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
         (str_store_string, s15, "@The Knights of Calatrava"),
         # (assign, "$current_mercs", "pt_company_calatrava_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
         (str_store_string, s15, "@The Knights of Calatrava"),
         # (assign, "$current_mercs", "pt_company_calatrava_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
         (str_store_string, s16, "@The Knights of Saint Thomas of Acre"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
         (str_store_string, s16, "@The Knights of Saint Thomas of Acre"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
         (str_store_string, s16, "@The Knights of Saint Thomas of Acre"),
         # (assign, "$current_mercs", "pt_company_saint_thomas_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s17, "@The Teutonic Knights"),
         # (assign, "$current_mercs", "pt_company_teutonic_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s17, "@The Teutonic Knights"),
         # (assign, "$current_mercs", "pt_company_teutonic_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s17, "@The Teutonic Knights"),
         # (assign, "$current_mercs", "pt_company_teutonic_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
         (str_store_string, s17, "@The Teutonic Knights"),
         # (assign, "$current_mercs", "pt_company_teutonic_4"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
         (str_store_string, s18, "@The Varangians"),
         # (assign, "$current_mercs", "pt_company_varangian_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
         (str_store_string, s18, "@The Varangians"),
         # (assign, "$current_mercs", "pt_company_varangian_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
############################################
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
         (str_store_string, s19, "@The Mamlukes"),
         # (assign, "$current_mercs", "pt_company_mamlukes_1"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
         (str_store_string, s19, "@The Mamlukes"),
         # (assign, "$current_mercs", "pt_company_mamlukes_2"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (else_try),
         (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
         (str_store_string, s19, "@The Mamlukes"),
         # (assign, "$current_mercs", "pt_company_mamlukes_3"),####### NEW v3.0-KOMKE mercs assigned in consequences block
       (try_end),
############################################
     # ], "Hire {s21} to the town garrison, cost: {reg7}",
     ], "Hire to the town garrison the following special mercenaries: {s11}-{s12}-{s13}-{s14}-{s15}-{s16}-{s17}-{s18}-{s19} cost: {reg7}",
     [
    (try_begin),
        (store_troop_gold, ":gold", "trp_player"),
        (lt, ":gold", reg7),
          (display_message, "@You do not have enough gold!", 0xff0000),
    (else_try),
        (store_party_size_wo_prisoners, ":party_size", "$current_town"),
        (ge, ":party_size", "$g_party_garrison_max_size_towns"),
          (display_message, "@Town garrison is full and can not hire additional men!", 0xff0000),
    (else_try),
        (troop_remove_gold, "trp_player", reg7),
        (party_get_slot, ":mercs_number", "$current_town", slot_spec_mercs2_number),
          # (party_get_slot, ":company_template", "$current_town", slot_regional_party_template),####### NEW v3.0-KOMKE not used
        (val_sub, ":mercs_number", 1),
        (party_set_slot, "$current_town", slot_spec_mercs2_number, ":mercs_number"),
        (try_begin),
            # (eq, s11, "@The Knights Templar"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
            (assign, "$current_mercs", "pt_company_templar_1"),
        (else_try),
            # (eq, s11, "@The Knights Templar"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
            (assign, "$current_mercs", "pt_company_templar_2"),
        (else_try),
            # (eq, s11, "@The Knights Templar"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
            (assign, "$current_mercs", "pt_company_templar_3"),
        (else_try),
            # (eq, s11, "@The Knights Templar"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_templar, 1),
            (assign, "$current_mercs", "pt_company_templar_4"),
        (else_try),
            # (eq, s12, "@The Knights Hospitalier"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
            (assign, "$current_mercs", "pt_company_hospitaller_1"),
        (else_try),
            # (eq, s12, "@The Knights Hospitalier"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
            (assign, "$current_mercs", "pt_company_hospitaller_2"),
        (else_try),
            # (eq, s12, "@The Knights Hospitalier"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
            (assign, "$current_mercs", "pt_company_hospitaller_3"),
        (else_try),
            # (eq, s12, "@The Knights Hospitalier"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_hospitaller, 1),
            (assign, "$current_mercs", "pt_company_hospitaller_4"),
        (else_try),
            # (eq, s13, "@The Knights of Saint Lazarus"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
            (assign, "$current_mercs", "pt_company_saint_lazarus_1"),
        (else_try),
            # (eq, s13, "@The Knights of Saint Lazarus"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
            (assign, "$current_mercs", "pt_company_saint_lazarus_2"),
        (else_try),
            # (eq, s13, "@The Knights of Saint Lazarus"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_lazarus, 1),
            (assign, "$current_mercs", "pt_company_saint_lazarus_3"),
        (else_try),
            # (eq, s14, "@The Knights of Santiago"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
            (assign, "$current_mercs", "pt_company_santiago_1"),
        (else_try),
            # (eq, s14, "@The Knights of Santiago"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
            (assign, "$current_mercs", "pt_company_santiago_2"),
        (else_try),
            # (eq, s14, "@The Knights of Santiago"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_santiago, 1),
            (assign, "$current_mercs", "pt_company_santiago_3"),
        (else_try),
            # (eq, s15, "@The Knights of Calatrava"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
            (assign, "$current_mercs", "pt_company_calatrava_1"),
        (else_try),
            # (eq, s15, "@The Knights of Calatrava"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
            (assign, "$current_mercs", "pt_company_calatrava_2"),
        (else_try),
            # (eq, s15, "@The Knights of Calatrava"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_calatrava, 1),
            (assign, "$current_mercs", "pt_company_calatrava_3"),
        (else_try),
            # (eq, s16, "@The Knights of Saint Thomas of Acre"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
            (assign, "$current_mercs", "pt_company_saint_thomas_1"),
        (else_try),
            # (eq, s16, "@The Knights of Saint Thomas of Acre"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
            (assign, "$current_mercs", "pt_company_saint_thomas_2"),
        (else_try),
            # (eq, s16, "@The Knights of Saint Thomas of Acre"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_saint_thomas, 1),
            (assign, "$current_mercs", "pt_company_saint_thomas_3"),
        (else_try),
            # (eq, s17, "@The Teutonic Knights"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
            (assign, "$current_mercs", "pt_company_teutonic_1"),
        (else_try),
            # (eq, s17, "@The Teutonic Knights"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
            (assign, "$current_mercs", "pt_company_teutonic_2"),
        (else_try),
            # (eq, s17, "@The Teutonic Knights"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
            (assign, "$current_mercs", "pt_company_teutonic_3"),
        (else_try),
            # (eq, s17, "@The Teutonic Knights"),
            (party_slot_eq, "$current_town", slot_center_has_chapter_teutonic, 1),
            (assign, "$current_mercs", "pt_company_teutonic_4"),
        (else_try),
            # (eq, s18, "@The Varangians"),
            (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
            (assign, "$current_mercs", "pt_company_varangian_1"),
        (else_try),
            # (eq, s18, "@The Varangians"),
            (party_slot_eq, "$current_town", slot_center_has_quarters_varangian, 1),
            (assign, "$current_mercs", "pt_company_varangian_2"),
        (else_try),
            # (eq, s19, "@The Mamlukes"),
            (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
            (assign, "$current_mercs", "pt_company_mamlukes_1"),
        (else_try),
            # (eq, s19, "@The Mamlukes"),
            (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
            (assign, "$current_mercs", "pt_company_mamlukes_2"),
        (else_try),
            # (eq, s19, "@The Mamlukes"),
            (party_slot_eq, "$current_town", slot_center_has_quarters_mamluk, 1),
            (assign, "$current_mercs", "pt_company_mamlukes_3"),
        (try_end),
        (call_script, "script_fill_company_new", "$current_town", "$current_town", "$current_mercs"),
    (try_end),
     ]),
####### NEW v3.0-KOMKE END- 
     
     ("go_back",
     [
       
     ], "Go back.",
     [
       # (jump_to_menu, "mnu_town"),
       # (jump_to_menu, "mnu_ee_center_manage"),  #### NEW v2.4
       (jump_to_menu, "mnu_ee_recruits_garrison_options"),  #### NEW v3.5
     ]),
   ]
  ),
  
  #######
 ("mongol_camp",0,
   "You come across a Mongolian Camp. {s10}",
   "none",
   [
    (str_clear, s10),
    (party_get_slot, ":town", "$g_encountered_party", slot_mongol_town),
    (party_get_slot, ":town_lord", ":town", slot_town_lord),
    (call_script, "script_troop_get_player_relation", ":town_lord"),

    (store_faction_of_party, ":faction_town", ":town"),
    (store_faction_of_party, ":faction_camp", "$g_encountered_party"),
    (try_begin),
      (eq, ":faction_town", ":faction_camp"),
      (str_store_troop_name,s0, ":town_lord"),
      (call_script, "script_troop_get_player_relation", ":town_lord"),
      (try_begin),
        (eq, "trp_player", ":town_lord"),
        (str_store_string, s10, "@You are the protector of this camp."),
      (else_try),
        (gt, reg0, 0),
        (str_store_string, s10, "@The camp is protected by {s0}. Because you have a positive relationship with him, he would not mind if you recruited some of the Mongols for your army."),
      (else_try),
        (str_store_string, s10, "@The camp is protected by {s0}. Because you have a bad relationship with him, he does not allow you to recruit the Mongols for your army."),
      (try_end),
    (try_end),
   ],
   
   [
      ("camp_walk",
      [
        (party_slot_eq, "$g_encountered_party",slot_mongol_camp_status, status_stationed),
        (store_faction_of_party, ":faction", "$g_encountered_party"),
        # (store_relation, ":player_relation", ":faction", "fac_player_supporters_faction"),
        (store_relation, ":player_relation", ":faction", "$players_kingdom"),
        (ge, ":player_relation", 0),
      ],
      "Walk around the campsite.",
      [
        (party_get_slot, ":village_scene", "$g_encountered_party", slot_castle_exterior),
        
        (party_get_current_terrain, ":terrain_type", "$g_encountered_party"), #default is steppe
        (try_begin),
          (this_or_next|eq, ":terrain_type", rt_snow),
          (eq, ":terrain_type", rt_snow_forest),
          (assign, ":village_scene", "scn_village_mongol_snow"),
        (else_try),
          (this_or_next|eq, ":terrain_type", rt_desert),
          (eq, ":terrain_type", rt_desert_forest),
          (assign, ":village_scene", "scn_village_mongol_desert"),
        (else_try),
          (this_or_next|eq, ":terrain_type", rt_plain),
          (eq, ":terrain_type", rt_forest),        
          (assign, ":village_scene", "scn_village_mongol_plains"),          
        (try_end),

        (modify_visitors_at_site, ":village_scene"),
        (reset_visitors),
        (set_visitor, 11, "trp_tatar_heavy_lancer"), #temp for now
        (assign, "$current_town", "$g_encountered_party"), #for walkers
        (party_set_slot, "$g_encountered_party", slot_center_walker_0_troop, "trp_khergit_walker_1"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_1_troop, "trp_khergit_walker_2"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_2_troop, "trp_khergit_walker_1"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_3_troop, "trp_khergit_walker_2"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_4_troop, "trp_khergit_walker_1"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_5_troop, "trp_khergit_walker_2"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_6_troop, "trp_khergit_walker_1"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_7_troop, "trp_khergit_walker_2"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_8_troop, "trp_khergit_walker_1"),
        (party_set_slot, "$g_encountered_party", slot_center_walker_9_troop, "trp_khergit_walker_2"),
        
        (call_script, "script_init_town_walkers"),
        (set_jump_mission, "mt_village_center"),
        
        (assign, "$talk_context", tc_mongol_camp),
        
        (jump_to_scene, ":village_scene"),
        (change_screen_mission),
      ]),
      
      ("camp_recruit",
      [
       (party_get_slot, ":town", "$g_encountered_party", slot_mongol_town),
       (party_get_slot, ":town_lord", ":town", slot_town_lord),
       (call_script, "script_troop_get_player_relation", ":town_lord"),
       (this_or_next|gt, reg0, 0),
       #(this_or_next|eq, "$g_encountered_party_faction", "$players_kingdom"),
       (this_or_next|eq, ":town_lord", "trp_player"),
       (eq, "$cheat_mode", 1),
       (store_faction_of_party, ":faction", "$g_encountered_party"),
       # (store_relation, ":player_relation", ":faction", "fac_player_supporters_faction"),
       (store_relation, ":player_relation", ":faction", "$players_kingdom"),
       (ge, ":player_relation", 0),
       
       (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
       (ge, ":free_capacity", 10),
       (party_get_slot, ":manpower", "$g_encountered_party", slot_feudal_lances),
       (gt, ":manpower", 0), #more then one,
       (assign, reg1, ":manpower"),
       #(store_faction_of_party, ":faction", "$g_encountered_party"),  
       
       (assign, reg5, 2000), #cost for one lance
       (try_begin),
         (eq, ":town_lord", "trp_player"),
         (assign, reg5, 500),
       (try_end),
       (str_store_string, s1, "@Cost: {reg5}"),

       (store_troop_gold, ":gold", "trp_player"),
       (ge, ":gold", reg5),
      ],
      "Recruit some Tribesman {s1}. (Available: {reg1})",
      [
       (party_get_slot, ":manpower", "$g_encountered_party", slot_feudal_lances),
       (val_sub, ":manpower", 1),
       (party_set_slot, "$g_encountered_party", slot_feudal_lances, ":manpower"),
       (call_script, "script_fill_lance", "$g_encountered_party", "p_main_party"),
       
       (try_begin),
         (gt, reg5, 0),
         (troop_remove_gold, "trp_player", reg5),
       (try_end),
       
       (jump_to_menu, "mnu_mongol_camp"),
      ]),
     
      ("camp_attack",
      [
        
      ],
      "Burn it! Burn them all! Attack the camp!",
      [
        (party_get_slot, ":town", "$g_encountered_party", slot_mongol_town),
        (party_get_slot, ":town_lord", ":town", slot_town_lord),
        (store_faction_of_party, ":faction", "$g_encountered_party"),
		######### NEW v3.1 - i don't know why this was disabled
        (call_script, "script_change_player_relation_with_faction", ":faction", -5),
        (call_script, "script_change_player_relation_with_troop", ":town_lord", -2),
        ##################
        (jump_to_menu, "mnu_simple_encounter"),
       #(change_screen_mission),
      ]),

     
      ("manor_leave",
      [],
      "Leave.",
      [
        (change_screen_return),
      ]),
   ]
  ),
  
 ("inspect_property",0,
   "'House!",
   "none",
   [
        #(set_player_troop, "trp_player"),
   ],
   [
    ##build new things in the settlement
      ("build",
      [
    
      ],
      "Build",
      [
        (start_presentation, "prsnt_economy_build"),
      ]),
   
      ("visit_house",
      [
        (eq, 0,1),
        
      ],
      "Go to your house",
      [        
        (modify_visitors_at_site, "scn_town_house_euro"),
        (reset_visitors),
        (mission_tpl_entry_set_override_flags, "mt_home_visit", 0, af_override_horse),
        
        (set_visitor, 0, "trp_player"), #no need?
        (assign, ":cur_entry", 3),
        (set_visitor, ":cur_entry", "trp_maid_1"),
        (set_jump_mission, "mt_home_visit"),
        (jump_to_scene, "scn_town_house_euro"),
        (change_screen_mission),
      ]),
   
      ("buy_house",
      [
        (eq, 0,1),
      ],
      "Buy a house in this town, cost: {reg1}",
      [        

      ]),
      
      ("recruit_maid",
      [
         (eq, 0,1),
      ],
      "Recruit a housemaid for the ",
      [        
        #(troop_raise_attribute, "trp_test", ca_strength, 12),
        #(set_player_troop, "trp_test"),
        (change_screen_view_character),
      ]),
      
     
      ("leave",
      [
        
      ],
      "Nevermind.",
      [
        (change_screen_return),
      ]),
   ]
  ),
  
  #######
 ("disband_lances",0,
   "Do you realy want to disband your feudal forces? (This will only affect forces that were recruited in lances.)",
   "none",
   [

   ],
   
   [
      ("disband",
      [
         
      ],
      "Yes! The peasants emit strong foul odour... Reward the nobles, however!",
      [
        (call_script, "script_balance_lance_storage"),
        #1st loop - find troops from this fief, that is in the player party.
        (try_for_range, ":fief", centers_begin, centers_end),
          #(party_slot_eq, ":fief", slot_town_lord, "trp_player"), #find the own by the player fief
          (try_for_range, ":index", 0, "$lance_troop_serving"),
            (troop_get_slot, ":place" , "trp_lances_places", ":index"), #it's the troops fief
            (troop_get_slot, ":troop", "trp_lances_troops", ":index"), #get the troop
            (eq, ":fief", ":place"),
            (main_party_has_troop, ":troop"), #party has the troop
            (troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", ":troop"), #set troop
            (troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":place"), #set places
            (troop_set_slot, "trp_lances_troops", ":index", 0), #remove current from array
            (troop_set_slot, "trp_lances_places", ":index", 0), #remove current from array
            (val_add, "$lance_troop_reserve", 1), #increase troops
            
            # (str_store_troop_name, s0, ":troop"),
            # (display_message, "@troop: {s0}"),
            
            (party_remove_members, "p_main_party", ":troop", 1), #remove from party
            (party_get_slot, ":troop_amount" , ":place", slot_number_troops_pending),
            (val_add, ":troop_amount", 1), #increase troops for the fief - to count how many lances to add
            (party_set_slot, ":place", slot_number_troops_pending, ":troop_amount"),
          (try_end),
        (try_end),
        (call_script, "script_balance_lance_storage"),
        
        #2st loop - we have a bunch of freeloaders who might have been upgraded - lets find them in the party
        (try_for_range, ":index", 0, "$lance_troop_serving"),
          (troop_get_slot, ":place" , "trp_lances_places", ":index"), #it's the troops fief
          (troop_get_slot, ":troop", "trp_lances_troops", ":index"), #get the troop
          #(party_get_slot, ":culture", ":place", slot_center_culture), #get culture
          (party_get_num_companion_stacks, ":num_stacks", "p_main_party"), #get troop stacks
          (try_for_range, ":i_stack", 0, ":num_stacks"), #check for evey troop, until found
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (is_between, ":stack_troop", regulars_begin, regulars_end),
            (assign, reg10, -1),
            (call_script, "script_troop_tree_search", ":stack_troop", ":troop"), #get stack_troops @ciaciacia
            (ge, reg10, ":stack_troop"),
            (assign, ":num_stacks", -1), #break;
          (try_end),
          (ge, reg10, 0), #found?
          (troop_set_slot, "trp_lances_troops", ":index", 0), #clear troop
          (troop_set_slot, "trp_lances_places", ":index", 0), #clear place
          (troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", reg10), #set troop
          (troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":place"), #set place
          (party_remove_members, "p_main_party",reg10, 1), #if found remove from the party
          (party_get_slot, ":troop_amount" , ":place", slot_number_troops_pending),
          (val_add, ":troop_amount", 1), #increase troops for the fief - to count how many lances to add
          (party_set_slot, ":place", slot_number_troops_pending, ":troop_amount"),
          (val_add, "$lance_troop_reserve", 1), #increase troops
        (try_end),
        (call_script, "script_balance_lance_storage"),
        
        #3rd - if some left, it means they are not recruited via lance - so put them to random fief. Some might be dead
        (call_script, "script_party_copy", "p_temp_casualties_player", "p_main_party"), #copy to backup. So we can remove members from main party
        (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties_player"), 
        (try_for_range, ":i_stack", 0, ":num_stacks"), #check for evey troop, until found
          (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties_player", ":i_stack"),
          (is_between, ":stack_troop", regulars_begin, regulars_end),
          (party_stack_get_size, ":stack_size", "p_temp_casualties_player", ":i_stack"),
          (try_for_range, reg2, 0, ":stack_size"), #remove from main party and add to the array the troop
            (try_for_range, ":place", centers_begin, centers_end),
              (party_slot_eq, ":place", slot_town_lord, "trp_player"), #find the own by the player fief
              (troop_set_slot, "trp_lances_troops_reserve", "$lance_troop_reserve", ":stack_troop"), #set troop
              (troop_set_slot, "trp_lances_places_reserve", "$lance_troop_reserve", ":place"), #set place
              (val_add, "$lance_troop_reserve", 1), #increase troops
              (party_remove_members, "p_main_party", ":stack_troop", 1),
              (party_get_slot, ":troop_amount" , ":place", slot_number_troops_pending),
              (val_add, ":troop_amount", 1), #increase troops for the fief - to count how many lances to add
              (party_set_slot, ":place", slot_number_troops_pending, ":troop_amount"),
            (try_end),
          (try_end),
        (try_end),
        (call_script, "script_balance_lance_storage"),
        (call_script, "script_count_nobles_commoners_for_center"),
        (assign, "$lance_troop_serving", 0),
        #(jump_to_menu, "mnu_camp"),
        (jump_to_menu, "$g_next_menu"),
      ]),
      
      ("leave",
      [
        
      ],
      "No. I'd rather burn a village or two instead!",
      [
        #(change_screen_return),
        (jump_to_menu, "$g_next_menu"),
      ]),
   ]
  ),
  
 ("recruit_companions",0,
   "what? Companion maker mk1.0",
   "none",
   [
        (set_player_troop, "trp_player"),
   ],
   
   [
      ("recruit_noble",
      [
         #todo, set the noble level skill thing
      ],
      "Recruit a local noble to your party",
      [        

      ]),
      
      ("recruit_priest",
      [
         
      ],
      "Recruit a holy man to your party",
      [        
        #(troop_raise_attribute, "trp_test", ca_strength, 12),
        #(set_player_troop, "trp_test"),
        (change_screen_view_character),
      ]),
      
      ("recruit_trainer",
      [
         
      ],
      "Recruit an experienced troop trainer",
      [        

      ]),
      
      ("recruit_trader",
      [
         
      ],
      "Recruit a fat local merchant",
      [        

      ]),
      
      ("recruit_pathfinder",
      [
         
      ],
      "Recruit an experienced pathfinder",
      [        

      ]),
     
      ("manor_leave",
      [
        
      ],
      "Nevermind.",
      [
        (change_screen_return),
      ]),
   ]
  ),
  
########################################################
# Autoloot Game Menus end
########################################################




######################################### restoration begin
#rubik Source code of Restoration
 # restoration begin
   ("notification_kingdom_restoration",0,
    "Restoration^^{s11} of {s13} gets a fief from {s12}, {s13} is restored! All lords of {s13} include {s14} will come back to {s13} later.",
    "none",
    [
      (troop_get_slot, ":original_faction", "$g_notification_menu_var1", slot_troop_original_faction),
      (faction_get_slot, ":original_king", ":original_faction", slot_faction_leader),
      (str_store_troop_name, s11, "$g_notification_menu_var1"),
      (str_store_faction_name, s12, "$g_notification_menu_var2"),
      (str_store_faction_name, s13, ":original_faction"),
      (str_store_troop_name, s14, ":original_king"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, ":original_faction", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", ":original_faction", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", ":original_faction", pos0),
      (try_end),
      ],
    [
      ("continue",[], "Continue...",
        [
          (troop_get_slot, ":original_faction", "$g_notification_menu_var1", slot_troop_original_faction),
          ## start peace
          (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (neq, ":cur_kingdom", ":original_faction"),
            (neq, ":cur_kingdom", "$g_notification_menu_var2"),
            (call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":original_faction", 0),
          (try_end),
          ## start war
          (call_script, "script_diplomacy_start_war_between_kingdoms", "$g_notification_menu_var2", ":original_faction", 1),
          (call_script, "script_update_all_notes"),
          (change_screen_return),
        ]),
     ]
  ),
#rubik Source code of Restoration
############################################ restoration end









  ("enhanced_mod_options",mnf_scale_picture,
   "Here you can change the various options pertaining to the Enhanced Edition.",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
     #(set_background_mesh, "mesh_pic_test_menu"),
   ],     
    [      
       ("enhanced_mod_options_1",[], "Party Options.",
       [
          (start_presentation, "prsnt_enhanced_mod_options_party"),
        ]
       ),
             
       ("enhanced_mod_options_2",[], "Kingdom Party Options.",
       [
          (start_presentation, "prsnt_enhanced_mod_options_party_kingdom"),
        ]
       ),
             
       ("enhanced_mod_options_3",[], "Non-Kingdom Party Options.",
       [
          (start_presentation, "prsnt_enhanced_mod_options_party_non_kingdom"),
        ]
       ),

             
       ("enhanced_mod_options_4",[], "Merchant Options.",
       [
          (start_presentation, "prsnt_enhanced_mod_options_merchants"),
        ]
       ),
            
             
       # ("enhanced_mod_options_5",[], "Quest Options",
       # [
          # (start_presentation, "prsnt_enhanced_mod_options_quests"),
        # ]
       # ),

            
       ("enhanced_mod_options_6",[], "Misc. Options.",
       [
          (start_presentation, "prsnt_enhanced_mod_options_misc"),
        ]
       ),

        ############## NEW v3.8 - 
        ("enhanced_mod_options_7",[], "Misc. Options #2.",
        [
           (start_presentation, "prsnt_enhanced_mod_options_misc_2"),
         ]
        ),
		############################
       
      # ("enhanced_mod_options_7",[], "Fix CTT troops.",
       # [
           # (jump_to_menu, "mnu_ctt_fix"),
        # ]
       # ),
       
      ("enhanced_mod_options_8",[], "Sorting options.",
        [
          (jump_to_menu, "mnu_ee_sort"),
        ]
      ),

      ### Troop update button, bringing older saves up to the current version's troop attributes, skills and proficiencies (NEW v3.9.2, by Khanor) ###
      ### Remember to add newly tweaked troops here if wanting players to update them!
      ("enhanced_mod_options_9",[], "Update troops to the current mod version.",
        [
          (try_for_range, ":cur_updating_troop", "trp_merc_mamluke_range", "trp_merc_mamluke_syrian"), ### Mamluke Archer
            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 160),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 60),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 160),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 60),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_merc_gaelic_spearman", "trp_merc_gaelic_axeman"), ### Gaelic Mercenary Spearman
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 12),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 9),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 12),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 9),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 210),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 210),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_merc_gaelic_axeman", "trp_merc_veteran_gaelic_spearman"), ### Gaelic Mercenary Axeman
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 12),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 9),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 12),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 9),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 210),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 210),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_merc_veteran_gaelic_spearman", "trp_merc_veteran_gaelic_axeman"), ### Veteran Gaelic Mercenary Spearman
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 15),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 12),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 15),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 12),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 6),
            
            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 160),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 280),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 50),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 160),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 280),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 50),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_merc_veteran_gaelic_axeman", "trp_merc_elite_gaelic_spearman"), ### Veteran Gaelic Mercenary Axeman
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 15),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 12),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 15),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 12),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 6),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 280),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 50),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 280),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 50),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_ee_constable_armory", "trp_ramun_the_slave_trader"), ### Armory (accessed via Constable)
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 18),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 20),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 21),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 21),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 18),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 20),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 21),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 21),

            # (call_script, "script_ee_raise_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),

            # (call_script, "script_ee_lower_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 40),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 40),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 40),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 40),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 40),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 40),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 40),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 40),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 40),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 40),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 40),
          (try_end),
          
          (try_for_range, ":cur_updating_troop", "trp_follower_woman", "trp_hunter_woman"), ### Camp Follower
            (troop_set_class, ":cur_updating_troop", grc_archers), ### Set to "Archers"-class.

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (lt, ":cur_level", 12), ### Add enough exp for level 12.
                (add_xp_to_troop, 600, ":cur_updating_troop"), ### Add exp repeatedly until desired level.
            (try_end),

            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 10),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 8),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 7),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 7),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 10),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 8),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 7),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 7),
            
            # (call_script, "script_ee_raise_actor_skill", skl_ironflesh, ":cur_updating_troop", 0),
            # (call_script, "script_ee_raise_actor_skill", skl_power_strike, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_power_draw, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_power_throw, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_weapon_master, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_athletics, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_shield, ":cur_updating_troop", 0),
            # (call_script, "script_ee_raise_actor_skill", skl_riding, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_pathfinding, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_wound_treatment, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_first_aid, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_surgery, ":cur_updating_troop", 0),
            # (call_script, "script_ee_raise_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),
            
            # (call_script, "script_ee_lower_actor_skill", skl_ironflesh, ":cur_updating_troop", 0),
            # (call_script, "script_ee_lower_actor_skill", skl_power_strike, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_power_draw, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_power_throw, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_weapon_master, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_athletics, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_shield, ":cur_updating_troop", 0),
            # (call_script, "script_ee_lower_actor_skill", skl_riding, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_pathfinding, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_wound_treatment, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_first_aid, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_surgery, ":cur_updating_troop", 0),
            # (call_script, "script_ee_lower_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 80),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 120),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 120),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 120),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 80),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 120),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 120),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 120),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_hunter_woman", "trp_sword_sister"), ### Camp Huntress, Camp Defender
            (troop_set_class, ":cur_updating_troop", grc_archers), ### Set to "Archers"-class.

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (lt, ":cur_level", 19), ### Add enough exp for level 19.
                (add_xp_to_troop, 600, ":cur_updating_troop"), ### Add exp repeatedly until desired level.
            (try_end),

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (gt, ":cur_level", 40), ### Remove enough exp for level 40.
                (add_xp_to_troop, -600000, ":cur_updating_troop"), ### Remove exp repeatedly until desired level.
            (try_end),

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (gt, ":cur_level", 30), ### Remove enough exp for level 30.
                (add_xp_to_troop, -60000, ":cur_updating_troop"), ### Remove exp repeatedly until desired level.
            (try_end),

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (gt, ":cur_level", 20), ### Remove enough exp for level 20.
                (add_xp_to_troop, -6000, ":cur_updating_troop"), ### Remove exp repeatedly until desired level.
            (try_end),

            (try_begin),
              (store_character_level, ":cur_level", ":cur_updating_troop"),
              (gt, ":cur_level", 19), ### Remove enough exp for level 19.
                (add_xp_to_troop, -600, ":cur_updating_troop"), ### Remove exp repeatedly until desired level.
            (try_end),
            
            (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_updating_troop", 14),
            (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_updating_troop", 11),
            (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_updating_troop", 8),
            (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_updating_troop", 6),

            (call_script, "script_ee_lower_actor_attribute", ca_strength, ":cur_updating_troop", 14),
            (call_script, "script_ee_lower_actor_attribute", ca_agility, ":cur_updating_troop", 11),
            (call_script, "script_ee_lower_actor_attribute", ca_intelligence, ":cur_updating_troop", 8),
            (call_script, "script_ee_lower_actor_attribute", ca_charisma, ":cur_updating_troop", 6),
            
            # (call_script, "script_ee_raise_actor_skill", skl_ironflesh, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_power_strike, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_power_draw, ":cur_updating_troop", 3),
            # (call_script, "script_ee_raise_actor_skill", skl_power_throw, ":cur_updating_troop", 0),
            # (call_script, "script_ee_raise_actor_skill", skl_weapon_master, ":cur_updating_troop", 5),
            # (call_script, "script_ee_raise_actor_skill", skl_athletics, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_shield, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_riding, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_pathfinding, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_wound_treatment, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_first_aid, ":cur_updating_troop", 2),
            # (call_script, "script_ee_raise_actor_skill", skl_surgery, ":cur_updating_troop", 1),
            # (call_script, "script_ee_raise_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),
            
            # (call_script, "script_ee_lower_actor_skill", skl_ironflesh, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_power_strike, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_power_draw, ":cur_updating_troop", 3),
            # (call_script, "script_ee_lower_actor_skill", skl_power_throw, ":cur_updating_troop", 0),
            # (call_script, "script_ee_lower_actor_skill", skl_weapon_master, ":cur_updating_troop", 5),
            # (call_script, "script_ee_lower_actor_skill", skl_athletics, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_shield, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_riding, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_pathfinding, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_wound_treatment, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_first_aid, ":cur_updating_troop", 2),
            # (call_script, "script_ee_lower_actor_skill", skl_surgery, ":cur_updating_troop", 1),
            # (call_script, "script_ee_lower_actor_skill", skl_inventory_management, ":cur_updating_troop", 10),

            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 200),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 60),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 100),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 200),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 60),
          (try_end),

          (try_for_range, ":cur_updating_troop", "trp_sea_raider_captain", "trp_steppe_bandit"), ### Sea Raider Captain
            (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 300),
            (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_updating_troop", 200),
            (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_updating_troop", 200),
            (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 200),
            (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_updating_troop", 180),

            (call_script, "script_ee_lower_actor_proficiency", wpt_one_handed_weapon, ":cur_updating_troop", 300),
            (call_script, "script_ee_lower_actor_proficiency", wpt_two_handed_weapon, ":cur_updating_troop", 60),
            (call_script, "script_ee_lower_actor_proficiency", wpt_polearm, ":cur_updating_troop", 200),
            (call_script, "script_ee_lower_actor_proficiency", wpt_archery, ":cur_updating_troop", 200),
            (call_script, "script_ee_lower_actor_proficiency", wpt_crossbow, ":cur_updating_troop", 200),
            (call_script, "script_ee_lower_actor_proficiency", wpt_throwing, ":cur_updating_troop", 180),
          (try_end),

          (display_message, "@Troop attributes, skills and proficiencies updated for the current mod version."),

          (jump_to_menu, "mnu_camp"),
        ]
      ),

      ### Unique charcter inventory update button, bringing older saves character inventories in line if item updates cluttered things up (NEW v3.9.2, by Khanor) ###
      ### Remember to add newly tweaked troops here if wanting players to update them!
      # ("enhanced_mod_options_10",[], "Reload inventories of Lords, Ladies and Tournament Competitors. (Excluding player spouse.)",
      #   [
      #     (try_for_range, ":cur_updating_character", "trp_kingdom_1_lord", "trp_knight_1_1"), ### All Faction Leaders.
      #       (call_script, "script_ee_reload_character_starting_equipment_excluding_player_spouse", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_knight_1_1", "trp_enhanced_rnd_lord_1"), ### All starting Lords (not custom).
      #       (call_script, "script_ee_reload_character_starting_equipment_excluding_player_spouse", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_knight_1_1_wife", "trp_heroes_end"), ### All starting Ladies.
      #       (call_script, "script_ee_reload_character_starting_equipment_excluding_player_spouse", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_ramun_the_slave_trader", "trp_kingdom_heroes_including_player_begin"), ### Other non-companion unique characters.
      #       (call_script, "script_ee_reload_character_starting_equipment_excluding_player_spouse", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (display_message, "@Reloaded inventories of all Lords, Ladies and Tournament Competitors. (Excluding player spouse.)"),

      #     (jump_to_menu, "mnu_camp"),
      #   ]
      # ),

      ### Unique charcter inventory update button, bringing older saves character inventories in line if item updates cluttered things up (NEW v3.9.2, by Khanor) ###
      ### Remember to add newly tweaked troops here if wanting players to update them!
      # ("enhanced_mod_options_11",[], "Reload inventories of Lords, Ladies and Tournament Competitors. (Including player spouse.)",
      #   [
      #     (try_for_range, ":cur_updating_character", "trp_kingdom_1_lord", "trp_knight_1_1"), ### All Faction Leaders.
      #       (call_script, "script_ee_reload_character_starting_equipment", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_knight_1_1", "trp_enhanced_rnd_lord_1"), ### All starting Lords (not custom).
      #       (call_script, "script_ee_reload_character_starting_equipment", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_knight_1_1_wife", "trp_heroes_end"), ### All starting Ladies.
      #       (call_script, "script_ee_reload_character_starting_equipment", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (try_for_range, ":cur_updating_character", "trp_ramun_the_slave_trader", "trp_kingdom_heroes_including_player_begin"), ### Other non-companion unique characters.
      #       (call_script, "script_ee_reload_character_starting_equipment", ":cur_updating_character", ":cur_updating_character"), ### Get your own starting inventory, remove it, and replace with your starting inventory.
      #     (try_end),

      #     (display_message, "@Reloaded inventories of all Lords, Ladies and Tournament Competitors. (Including player spouse.)"),

      #     (jump_to_menu, "mnu_camp"),
      #   ]
      # ),
       
      ("enhanced_mod_options_12",[], "Go back.",
        [
          (jump_to_menu, "mnu_camp"),
        ]
      ),
       
    ]
  ),


  ("debug_options",mnf_scale_picture,
   "Debug options",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
     #(set_background_mesh, "mesh_pic_test_menu"),
   ],     
    [      
       ("debug_options_1",[], "Reset Tavern troops.",
       [
        (try_for_range, ":town_no", towns_begin, towns_end),
          (store_sub, ":offset", ":town_no", towns_begin),
          
          (store_add, ":cur_object_no", "p_town_merc_1", ":offset"),
          (party_set_slot, ":town_no", slot_town_mercs, ":cur_object_no"),
          
          (call_script, "script_add_tavern_troops"),
          (str_store_party_name, s7, ":town_no"),
          (str_store_party_name, s8, ":cur_object_no"),
          (display_message, "@{s8} assigned to {s7}"),
        (try_end)         
        ]
       ),    
       
       ("debug_options_2",[], "Give me equipment!",
        [
         (troop_raise_skill, "trp_player", "skl_inventory_management", 10),
         
         (troop_add_item, "trp_player", "itm_maciejowski_crown", 29),
         (troop_add_item, "trp_player", "itm_maciejowski_crown", 29),
         (troop_add_item, "trp_player", "itm_maciejowski_crown", 29),
         
         (troop_add_item, "trp_player", "itm_short_bow", 17),
         (troop_add_item, "trp_player", "itm_short_bow", 17),
         (troop_add_item, "trp_player", "itm_short_bow"),
         (troop_add_item, "trp_player", "itm_bodkin_arrows", 42),
         (troop_add_item, "trp_player", "itm_bodkin_arrows", 42),
         (troop_add_item, "trp_player", "itm_bodkin_arrows", 42),
         (troop_add_item, "trp_player", "itm_bodkin_arrows", 42),
         
         (troop_add_item, "trp_player", "itm_heraldic_lance", 13),
         (troop_add_item, "trp_player", "itm_heraldic_lance", 13),
         (troop_add_item, "trp_player", "itm_heraldic_lance", 13),
         (troop_add_item, "trp_player", "itm_heraldic_lance", 13),
         (troop_add_item, "trp_player", "itm_heraldic_lance", 13),
         
         (troop_add_item, "trp_player", "itm_surcoat_over_mail", 29),
         (troop_add_item, "trp_player", "itm_surcoat_over_mail", 29),
         (troop_add_item, "trp_player", "itm_mail_with_surcoat", 29),
         (troop_add_item, "trp_player", "itm_mail_with_surcoat", 29),
         
         (troop_add_item, "trp_player", "itm_coat_of_plates_red", 29),
         (troop_add_item, "trp_player", "itm_coat_of_plates_red", 29),
         (troop_add_item, "trp_player", "itm_coat_of_plates", 29),
         (troop_add_item, "trp_player", "itm_coat_of_plates", 29),
         (troop_add_item, "trp_player", "itm_hirdman_a", 29),
         (troop_add_item, "trp_player", "itm_hirdman_a", 29),
         
         (troop_add_item, "trp_player", "itm_hunting_crossbow", 17),
         (troop_add_item, "trp_player", "itm_hunting_crossbow", 17),
         (troop_add_item, "trp_player", "itm_hunting_crossbow", 17),
         (troop_add_item, "trp_player", "itm_hunting_crossbow", 17),
         (troop_add_item, "trp_player", "itm_crossbow", 17),
         (troop_add_item, "trp_player", "itm_crossbow", 17),
         (troop_add_item, "trp_player", "itm_heavy_crossbow", 17),
         
         (troop_add_item, "trp_player", "itm_steel_bolts", 42),
         (troop_add_item, "trp_player", "itm_steel_bolts", 42),
         (troop_add_item, "trp_player", "itm_steel_bolts", 42),
         (troop_add_item, "trp_player", "itm_steel_bolts", 42),
         (troop_add_item, "trp_player", "itm_steel_bolts", 42),
         
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         (troop_add_item, "trp_player", "itm_lamellar_gauntlets", 29),
         
         (troop_add_item, "trp_player", "itm_osp_great_helm_a", 29),
         (troop_add_item, "trp_player", "itm_osp_great_helm_a", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_03", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_04", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_04", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_04", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_05", 29),
         (troop_add_item, "trp_player", "itm_rnd_helm_06", 29),
         
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         (troop_add_item, "trp_player", "itm_mail_boots_long", 29),
         
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         (troop_add_item, "trp_player", "itm_sword_type_xiiia", 13),
         
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
         (troop_add_item, "trp_player", "itm_tab_shield_heater_cav_b", 27),
        ]
       ),

       ("debug_options_3",[], "Turn Total War mode 1.",
       [
             (set_show_messages, 0),
             (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
               (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
                 (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
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
        ]
       ),
       
       
       ("debug_options_4",[], "Make lords build stuff.",
       [
          (call_script, "script_lord_random_build_script"),
        ]
       ),
                     
       ("debug_options_5",[], "Reset Tavern Bounty quests.",
       [
          (assign, "$g_bounty_activo", 0),
        ]
       ),
              
                     
       ("debug_options_6",[], "Track simple triggers.",
       [
         (jump_to_menu, "mnu_debug_simple_trigger_tracker"),
        ]
       ),              
                     
       ("debug_options_7",[], "Create a new lord for a faction.",
       [
         (jump_to_menu, "mnu_choose_faction_to_spawn_lord_1"),
       ]
       ),
       
       ("debug_options_8",[], "Jump to a scene.",
       [
         (jump_to_menu, "mnu_debug_jump_to_scene"),
       ]
       ),
       
       ("debug_options_9",[], "Start a civil war in a random faction.",
       [
        (assign, ":number_of_lords", 0),
        (assign, ":upper_bound", 500),
        (assign, ":upper_bound_2", active_npcs_end),
        (try_for_range, ":unused", 0, ":upper_bound"),
          (store_random_in_range, ":faction", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
          (assign, ":faction_to_use", ":faction"),
          (assign, ":upper_bound", -1), ## breaks loop
        (try_end),
       
        (faction_get_slot, ":lord_count", ":faction_to_use", slot_faction_lord_count),  
        (faction_get_slot, ":faction_to_use_king", ":faction_to_use", slot_faction_leader),
        (try_for_range, ":cur_faction_lord", active_npcs_begin, ":upper_bound_2"),
          (troop_slot_eq, ":cur_faction_lord", slot_troop_is_alive, 1),
          (troop_slot_eq, ":cur_faction_lord", slot_troop_occupation, slto_kingdom_hero),
          (neq, ":cur_faction_lord", ":faction_to_use_king"), ### not the king
            (store_faction_of_troop, ":cur_lord_faction", ":cur_faction_lord"),
            (eq, ":cur_lord_faction", ":faction_to_use"),
              (call_script, "script_troop_change_relation_with_troop", ":faction_to_use_king", ":cur_faction_lord", -100),
              (str_store_troop_name_link, s1, ":cur_faction_lord"),
              (display_message, "@{s1} lowered relations with king"),
              (val_add, ":number_of_lords", 1),
              (try_begin),
                (assign, ":number_of_lords_temp", ":number_of_lords"),   
                (val_mul, ":number_of_lords_temp", 100),   
                (store_div, ":cur_angry_lords_percentage", ":number_of_lords_temp", ":lord_count"),   #### e.g. 10 total lords with 4 angry lords = 4*100 = 400 / 10 = 40% which meets the requirements 
                (ge, ":cur_angry_lords_percentage", 40),  #### needs 40% angry lords
                  (assign, ":upper_bound_2", -1), ## breaks loop
              (try_end),
        (try_end),
   
        (try_begin),
          (display_message, "@script_check_faction_civil_war_requirements called!"),
          (call_script, "script_check_faction_civil_war_requirements", ":faction_to_use"),
          (eq, reg0, 1),
            (display_message, "@script_initiate_civil_war called!"),
            (call_script, "script_initiate_civil_war", ":faction_to_use", reg1),
        (try_end),
       ]
       ),
              
       
       ("debug_options_10",[], "Create a custom battle.",
       [
           (start_presentation, "prsnt_ee_custom_battle_designer"),
        ]
       ),
       
       ("debug_options_11",[], "Kill the current king of player faction by assassination.",
       [
         (faction_get_slot, ":king", "$players_kingdom", slot_faction_leader),
         (call_script, "script_kill_lord_assassination", ":king", 0, "trp_player"),
        ]
       ),
       
       
       ("debug_options_12",[], "Create a new lord for Player Faction.",
       [
         # (call_script, "script_create_new_lord_for_faction", "fac_player_supporters_faction"),
         (call_script, "script_create_new_lord_for_faction", "$players_kingdom"),
       ]
       ),
       
       
       ("debug_options_13",[], "Build a castle for player near London.",
       [
         (party_set_slot, "p_town_9_1", slot_center_current_improvement, slot_center_has_fortifications_1),
         (call_script, "script_process_1257ad_center_upgrades", "p_town_9_1"),
       ]
       ),
       
	   ######### NEW v3.0
       ("debug_options_14",[], "Display pretender locations.",
       [
       (try_for_range, ":cur_troop", pretenders_begin, pretenders_end),
         (troop_get_slot, ":cur_center", ":cur_troop", slot_troop_cur_center),
         (str_store_troop_name, s15, ":cur_troop"),  
         (str_store_party_name_link, s11, ":cur_center"),  
         (display_message, "@{s15} is currently at {s11}."),		 
       (try_end),
       ]
       ),
	   #########
	   
	   ######### NEW v3.0
       ("debug_options_15",[], "More options.",
       [
       (jump_to_menu, "mnu_debug_options_new_1"),
       ]
       ),
	   #########
	   
	   
       ("debug_options_99",[], "Go back.",
       [
           (jump_to_menu, "mnu_camp"),
        ]
       ),
       
       
       
    ]
  ),


########################### SIMPLE TRIGGER TRACKER
  ("debug_simple_trigger_tracker",mnf_scale_picture,
   "Simple trigger tracking. If you don't know what this is don't use it.",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
   ],     
    [      
       ("debug_simple_trigger_tracker_start",[], "Start Tracking",
       [
         (assign, "$g_simple_trigger_fire_count_1", 0),
         (assign, "$g_simple_trigger_fire_count_2", 0),
         (assign, "$g_simple_trigger_fire_count_3", 0),
         (assign, "$g_simple_trigger_fire_count_4", 0),
         (assign, "$g_simple_trigger_fire_count_5", 0),
         (assign, "$g_simple_trigger_fire_count_6", 0),
         (assign, "$g_simple_trigger_fire_count_7", 0),
         (assign, "$g_simple_trigger_fire_count_8", 0),
         (assign, "$g_simple_trigger_fire_count_9", 0),
         (assign, "$g_simple_trigger_fire_count_10", 0),
         (assign, "$g_simple_trigger_fire_count_11", 0),
         (assign, "$g_simple_trigger_fire_count_12", 0),
         (assign, "$g_simple_trigger_fire_count_13", 0),
         (assign, "$g_simple_trigger_fire_count_14", 0),
         (assign, "$g_simple_trigger_fire_count_15", 0),
         (assign, "$g_simple_trigger_fire_count_16", 0),
         (assign, "$g_simple_trigger_fire_count_17", 0),
         (assign, "$g_simple_trigger_fire_count_18", 0),
         (assign, "$g_simple_trigger_fire_count_19", 0),
         (assign, "$g_simple_trigger_fire_count_20", 0),
         (assign, "$g_simple_trigger_fire_count_21", 0),
         (assign, "$g_simple_trigger_fire_count_22", 0),
         (assign, "$g_simple_trigger_fire_count_23", 0),
         (assign, "$g_simple_trigger_fire_count_24", 0),
         (assign, "$g_simple_trigger_fire_count_25", 0),
         (assign, "$g_simple_trigger_fire_count_26", 0),
         (assign, "$g_simple_trigger_fire_count_27", 0),
         (assign, "$g_simple_trigger_fire_count_28", 0),
         (assign, "$g_simple_trigger_fire_count_29", 0),
         (assign, "$g_simple_trigger_fire_count_30", 0),
         (assign, "$g_simple_trigger_fire_count_31", 0),
         (assign, "$g_simple_trigger_fire_count_32", 0),
         (assign, "$g_simple_trigger_fire_count_33", 0),
         (assign, "$g_simple_trigger_fire_count_34", 0),
         (assign, "$g_simple_trigger_fire_count_35", 0),
         (assign, "$g_simple_trigger_fire_count_36", 0),
         (assign, "$g_simple_trigger_fire_count_37", 0),
         (assign, "$g_simple_trigger_fire_count_38", 0),
         (assign, "$g_simple_trigger_fire_count_39", 0),
         (assign, "$g_simple_trigger_fire_count_40", 0),
         (assign, "$g_simple_trigger_fire_count_41", 0),
         (display_message, "@Done."),
         
       ]
       ),    
            
       ("debug_simple_trigger_tracker_2",[], "Print results to log",
       [
         (assign, reg18, "$g_simple_trigger_fire_count_1"),
         (display_message, "@Trigger 1 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_2"),
         (display_message, "@Trigger 2 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_3"),
         (display_message, "@Trigger 3 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_4"),
         (display_message, "@Trigger 4 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_5"),
         (display_message, "@Trigger 5 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_6"),
         (display_message, "@Trigger 6 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_7"),
         (display_message, "@Trigger 7 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_8"),
         (display_message, "@Trigger 8 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_9"),
         (display_message, "@Trigger 9 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_10"),
         (display_message, "@Trigger 10 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_11"),
         (display_message, "@Trigger 11 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_12"),
         (display_message, "@Trigger 12 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_13"),
         (display_message, "@Trigger 13 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_14"),
         (display_message, "@Trigger 14 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_15"),
         (display_message, "@Trigger 15 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_16"),
         (display_message, "@Trigger 16 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_17"),
         (display_message, "@Trigger 17 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_18"),
         (display_message, "@Trigger 18 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_19"),
         (display_message, "@Trigger 19 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_20"),
         (display_message, "@Trigger 20 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_21"),
         (display_message, "@Trigger 21 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_22"),
         (display_message, "@Trigger 22 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_23"),
         (display_message, "@Trigger 23 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_24"),
         (display_message, "@Trigger 24 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_25"),
         (display_message, "@Trigger 25 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_26"),
         (display_message, "@Trigger 26 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_27"),
         (display_message, "@Trigger 27 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_28"),
         (display_message, "@Trigger 28 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_29"),
         (display_message, "@Trigger 29 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_30"),
         (display_message, "@Trigger 30 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_31"),
         (display_message, "@Trigger 31 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_32"),
         (display_message, "@Trigger 32 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_33"),
         (display_message, "@Trigger 33 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_34"),
         (display_message, "@Trigger 34 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_35"),
         (display_message, "@Trigger 35 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_36"),
         (display_message, "@Trigger 36 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_37"),
         (display_message, "@Trigger 37 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_38"),
         (display_message, "@Trigger 38 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_39"),
         (display_message, "@Trigger 39 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_40"),
         (display_message, "@Trigger 40 fire count since start: {reg18}."),
         
         (assign, reg18, "$g_simple_trigger_fire_count_41"),
         (display_message, "@Trigger 41 fire count since start: {reg18}."),
       ]
       ),    
       
       
       ("debug_simple_trigger_tracker_4",[], "Go back.",
       [
           (jump_to_menu, "mnu_camp"),
        ]
       ),
       
       
       
    ]
  ),

######################################################

  
  


########################### CTT BUG FIX
  ("ctt_fix",mnf_scale_picture,
   "Select the amount of branches.",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
   ],     
    [      
       ("ctt_fix_options_1",[], "1 Branch",
       [
         (assign, "$cstm_num_tiers", 1),
         (call_script, "script_initialize_faction_troop_types_player"),
         (display_message, "@CTT reinforcements set to work with 1 branch."),
       ]
       ),    
       
       ("ctt_fix_options_2",[], "2 Branches",
       [
         (assign, "$cstm_num_tiers", 2),
         (call_script, "script_initialize_faction_troop_types_player"),
         (display_message, "@CTT reinforcements set to work with 2 branches."),
       ]
       ),    
       
       ("ctt_fix_options_3",[], "3 Branches",
       [
         (assign, "$cstm_num_tiers", 3),
         (call_script, "script_initialize_faction_troop_types_player"),
         (display_message, "@CTT reinforcements set to work with 3 branches."),
       ]
       ),    
                   
       ("ctt_fix_options_8",[], "Go back.",
       [
           (jump_to_menu, "mnu_enhanced_mod_options"),
        ]
       ),
    ]
  ),
######################################################

  

########################### NEW v2.1 - jump to scene
  ("debug_jump_to_scene", mnf_enable_hot_keys,
   "Choose a scene to jump to.",
   "none",
    [
    ],
    [
    ]+[("go_to_scene"+str(x+1),
        [
          (store_add, ":dest_scene", "scn_camp_scene_desert", x),
          (str_store_string, s0, ":dest_scene"),
        ], "{s0}",
        [
          (store_add, ":dest_scene", "scn_camp_scene_desert", x),
          (modify_visitors_at_site, ":dest_scene"),
          (reset_visitors),
          (assign, "$g_mt_mode", tcm_default),
          (jump_to_scene, ":dest_scene"),
          (change_screen_mission),
        ]) for x in range(0, 8)]+[
      
      ("debug_jump_to_scene_back",[], "Go back.",
        [(jump_to_menu, "mnu_debug_options"),]),
    ]
),
######################################################

  
  
  
  
  
  
  
########################### NEW IMPROVEMENTS






########################### ECONOMIC IMPROVEMENTS
("improvement_economic_select",mnf_scale_picture,
   "Select which improvement you wish to build here.",
   "none",
    [],
    [


######################## DOCK BUILDINGS
       ("center_build_mechants_warf",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      #################### ONLY TOWNS CLOSE TO THE SEA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_16_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_20_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_5_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_29_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),

                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_docks, 0),
                                       ],
       "Build a Merchant's Warf.",[(assign, "$g_improvement_type", slot_center_tier_docks),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_warehouse",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      #################### ONLY TOWNS CLOSE TO THE SEA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_16_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_20_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_5_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_29_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),

                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_docks, 1),
                                       ],
       "Build a Warehouse.",[(assign, "$g_improvement_type", slot_center_tier_docks),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_docklands",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      #################### ONLY TOWNS CLOSE TO THE SEA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_16_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_20_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_17_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_11_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_5_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_24_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_29_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_26_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_1_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_4_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_22_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),

                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_docks, 2),
                                       ],
       "Build Docklands.",[(assign, "$g_improvement_type", slot_center_tier_docks),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
################################################



######################## MERCHANT'S GUILD BUILDINGS
       ("center_build_merchants_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_merchants_guild, 1),
                                       ],
       "Build a Merchant's Guild Quarters.",[(assign, "$g_improvement_type", slot_center_tier_merchants_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_master_merchants_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_merchants_guild, 2),
                                       ],
       "Build a Master Merchant's Guild Quarters.",[(assign, "$g_improvement_type", slot_center_tier_merchants_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_hq_merchants_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_merchants_guild, 3),
                                       ],
       "Build a Merchant's Guild HQ.",[(assign, "$g_improvement_type", slot_center_tier_merchants_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                            
################################################

          
          



######################## MASON'S GUILD BUILDINGS
       ("center_build_masons_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_masons_guild, 0),
                                       ],
       "Build a Mason's Guild Quarters.",[(assign, "$g_improvement_type", slot_center_has_tier_masons_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_master_masons_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_masons_guild, 1),
                                       ],
       "Build a Master Mason's Guild Quarters.",[(assign, "$g_improvement_type", slot_center_has_tier_masons_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_hq_masons_guild",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_masons_guild, 2),
                                       ],
       "Build a Mason's Guild HQ.",[(assign, "$g_improvement_type", slot_center_has_tier_masons_guild),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                            
################################################


          

######################## MARKET BUILDINGS
       ("center_build_fairground",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_market, 0),
                                       ],
       "Build a Fairground.",[(assign, "$g_improvement_type", slot_center_has_tier_market),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_great_market",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_market, 1),
                                       ],
       "Build a Great Market.",[(assign, "$g_improvement_type", slot_center_has_tier_market),
                                  (jump_to_menu, "mnu_center_improve"),]),


                                  
       ("center_build_merchants_quarter",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_market, 2),
                                       ],
       "Build a Merchant's Quarters.",[(assign, "$g_improvement_type", slot_center_has_tier_market),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
                            
################################################

          
          
######################## MINES
       ("center_build_mine",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_mines, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_mining_network, 0),
                                       ],
       "Build a mine.",[(assign, "$g_improvement_type", slot_center_has_tier_1_mines),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_mining_network",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_mines, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_mining_network, 0),
                                       ],
       "Build a Mining Network.",[(assign, "$g_improvement_type", slot_center_has_tier_2_mining_network),
                                  (jump_to_menu, "mnu_center_improve"),]),

                            
################################################
          
          
          
          
######################## FARMS
       ("center_build_land_clearance",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_farm, 0),
                                       ],
       "Develop Land Clearance.",[(assign, "$g_improvement_type", slot_center_has_tier_farm),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_communal_farming",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_farm, 1),
                                       ],
       "Develop Communal Farming.",[(assign, "$g_improvement_type", slot_center_has_tier_farm),
                                  (jump_to_menu, "mnu_center_improve"),]),


                                  
       ("center_build_crop_rotation",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_farm, 2),
                                       ],
       "Develop Crop Rotation.",[(assign, "$g_improvement_type", slot_center_has_tier_farm),
                                  (jump_to_menu, "mnu_center_improve"),]),



                                  
       ("center_build_irrigation",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_farm, 3),
                                       ],
       "Develop Irrigation.",[(assign, "$g_improvement_type", slot_center_has_tier_farm),
                                  (jump_to_menu, "mnu_center_improve"),]),

################################################

          
          
          
      ("center_build_economic_exit",[(eq, reg6, 0)], "Go back.",
       [
           (jump_to_menu, "mnu_center_manage"),
        ]
       ),
      
    ],
),
######################################################




########################### WELFARE IMPROVEMENTS
("improvement_welfare_select",mnf_scale_picture,
   "Select which improvement you wish to build here.",
   "none",
    [],
    [


######################## ADMINISTRATION BUILDINGS
       ("center_build_town_hall",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_town_hall, 0),
                                       ],
       "Build a Town Hall.",[(assign, "$g_improvement_type", slot_center_tier_town_hall),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_city_hall",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_town_hall, 1),
                                       ],
       "Build a City Hall.",[(assign, "$g_improvement_type", slot_center_tier_town_hall),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_governors_palace",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_town_hall, 0),
                                       ],
       "Build a Governors Palace.",[(assign, "$g_improvement_type", slot_center_tier_town_hall),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_royal_palace",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_town_hall, 0),
                                       ],
       "Build a Royal Palace.",[(assign, "$g_improvement_type", slot_center_tier_town_hall),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                                                    
       ("center_build_village_council_hall",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_town_hall, 1),
                                       ],
       "Build a Village Council Hall.",[(assign, "$g_improvement_type", slot_center_tier_town_hall),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
                                  
################################################



          


######################## RELIGIOUS BUILDINGS

######################## TIER 1
       ("center_build_small_church",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_religious_building, 0),
                                      
                                       ],
                                      
       "Build a small Church.",[(assign, "$g_improvement_type", slot_center_tier_religious_building),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
################################################
                                  
                                  


######################## HEALTH BUILDINGS
       ("center_build_small_hospital",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_balt),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_mongol),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_heretic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_nordic),
                                      
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 0),

                                       ],
       "Build a small Hospital.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),

                            
                                  
       ("center_build_hospital",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_balt),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_mongol),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_heretic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_nordic),
                                      
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 1),

                                       ],
       "Build a Hospital.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),

                            
                                  
       ("center_build_college_of_surgeons",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_balt),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_mongol),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_heretic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_nordic),
                                      
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 2),
                                       ],
       "Build a College of Surgeons.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),


                                  
                                  
                                  
       ("center_build_small_bimaristan",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 3),

                                       ],
       "Build a small Bimaristan.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                                  
       ("center_build_bimaristan",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 4),

                                       ],
       "Build a Bimaristan.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),

                              
                                  
       ("center_build_great_bimaristan",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_hospital, 5),

                                       ],
       "Build a great Bimaristan.",[(assign, "$g_improvement_type", slot_center_tier_hospital),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
################################################


                                  
                                  

######################## SQUALOR REDUCTION BUILDINGS
       ("center_build_sewers",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_sewers, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_improved_sewers, 0),

                                       ],
       "Build Sewers.",[(assign, "$g_improvement_type", slot_center_has_tier_1_sewers),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_improved_sewers",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_sewers, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_improved_sewers, 0),

                                       ],
       "Build improved_Sewers.",[(assign, "$g_improvement_type", slot_center_has_tier_2_improved_sewers),
                                  (jump_to_menu, "mnu_center_improve"),]),

                            
################################################


                                  

                                  
                                  

######################## ROADS
       ("center_build_dirt_roads",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_dirt_roads, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_paved_roads, 0),

                                       ],
       "Build Dirt Roads.",[(assign, "$g_improvement_type", slot_center_has_tier_1_dirt_roads),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
       ("center_build_paved_roads",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_dirt_roads, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_paved_roads, 0),

                                       ],
       "Build Paved Roads.",[(assign, "$g_improvement_type", slot_center_has_tier_2_paved_roads),
                                  (jump_to_menu, "mnu_center_improve"),]),

                            
################################################


                                  

                                  
                                  

######################## PLEASURE 
       ("center_build_brothel",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      # (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      # (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      # (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_balt),
                                      # (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_mongol),
                                      # (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_heretic),
                                      # (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_nordic),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_brothel, 0),

                                       ],
       "Build a Brothel.",[(assign, "$g_improvement_type", slot_center_tier_brothel),
                                  (jump_to_menu, "mnu_center_improve"),]),

                                  
                    
       ("center_build_coaching_house",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_balt),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_mongol),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_heretic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_pagan_nordic),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_brothel, 1),

                                       ],
       "Build a Coaching House.",[(assign, "$g_improvement_type", slot_center_tier_brothel),
                                  (jump_to_menu, "mnu_center_improve"),]),
                              
                    
       ("center_build_wayfarers_rest",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_brothel, 2),

                                       ],
       "Build a Wayfarer's Rest.",[(assign, "$g_improvement_type", slot_center_tier_brothel),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
                                  
                    
       ("center_build_pleasure_palace",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_brothel, 3),

                                       ],
       "Build a Pleasure Palace.",[(assign, "$g_improvement_type", slot_center_tier_brothel),
                                  (jump_to_menu, "mnu_center_improve"),]),

                    
                            
################################################

                                  
                                  

######################## EDUCATION 
       ("center_build_improved_schools",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_school, 0),

                                       ],
       "Build a Improved School.",[(assign, "$g_improvement_type", slot_center_tier_school),
                                  (jump_to_menu, "mnu_center_improve"),]),

                
                
       ("center_build_university",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_school, 1),

                                       ],
       "Build a University.",[(assign, "$g_improvement_type", slot_center_tier_school),
                                  (jump_to_menu, "mnu_center_improve"),]),

                
                            
################################################



                                  
                                  

######################## HOUSING - TOWN
       ("center_build_housing_1",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 0),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                
       ("center_build_housing_2",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 1),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_3",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 2),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_4",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 3),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_5",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 4),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_6",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 5),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_7",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 6),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                
       ("center_build_housing_8",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_housing, 7),

                                       ],
       "Improve Housing.",[(assign, "$g_improvement_type", slot_center_tier_housing),
                                  (jump_to_menu, "mnu_center_improve"),]),

                

                            
################################################


                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
################################################



          
          
      ("center_build_welfare_exit",[(eq, reg6, 0)], "Go back.",
       [
           (jump_to_menu, "mnu_center_manage"),
        ]
       ),

    ],
),
######################################################




########################### MILITARY IMPROVEMENTS
("improvement_military_select",mnf_scale_picture,
   "Select which improvement you wish to build here",
   "none",
    [],
    [
################################################ KNIGHT CHAPTERS
       ("center_build_knight_order_chapter",[
       (eq, reg6, 0),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
       (party_slot_ge, "$g_encountered_party", slot_center_tier_religious_building, 3),
       
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_teutonic, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_templar, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_hospitaller, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_saint_lazarus, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_santiago, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_calatrava, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_saint_thomas, 0),
       (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
       (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
       
       ],
       "Build a chapter for a knight order.",[(jump_to_menu, "mnu_knight_chapter_select"),]),
################################################





######################## MERCENARY QUARTERS
      ("center_build_mercenary_quarters",[
       (eq, reg6, 0),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
       (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_varangian, 0),
       ],
       "Build mercenary quarters.",[(jump_to_menu, "mnu_merc_quarter_select"),]
       ),
       
################################################

      
      
      
      
################################################ NOMAD MERC CAMP
       ("center_build_camp_merc",[
       (eq, reg6, 0),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       
       (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
       # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
       # (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
       
       ],
       "Build a camp for mercenaries.",[(jump_to_menu, "mnu_merc_camp_select"),]),
       
################################################

      
      
      
######################## MERC OUTPOSTS
       ("center_build_outpost_merc",[
       (eq, reg6, 0),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
       (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
       ],
       "Build a mercenary outpost.",[(jump_to_menu, "mnu_merc_outpost_select"),]),
       
################################################

      
      
      
######################## OTHER IMPROVEMENTS 
           
        
######################## GARRISON IMPROVEMENTS
       ("center_build_garrison_quarters",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_garrison_quarters, 0),
                                       ],
       "Build a Garrison Quarters.",[(assign, "$g_improvement_type", slot_center_tier_garrison_quarters),
                                  (jump_to_menu, "mnu_center_improve"),]),
                 
      
       ("center_build_drill_square",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_garrison_quarters, 1),
                                       ],
       "Build a Drill Square.",[(assign, "$g_improvement_type", slot_center_tier_garrison_quarters),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
                 
      
       ("center_build_barracks",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_garrison_quarters, 2),
                                       ],
       "Build a Barracks.",[(assign, "$g_improvement_type", slot_center_tier_garrison_quarters),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
                 
       ("center_build_armoury",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_garrison_quarters, 3),
                                       ],
       "Build a Armoury.",[(assign, "$g_improvement_type", slot_center_tier_garrison_quarters),
                                  (jump_to_menu, "mnu_center_improve"),]),
################################################





######################## MERCENARY QUARTERS
       ("center_build_mercenary_quarters",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_mercenary_quarters, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_mercenary_hq, 0),
                                       ],
       "Build a Mercenary Quarters.",[(assign, "$g_improvement_type", slot_center_has_tier_1_mercenary_quarters),
                                  (jump_to_menu, "mnu_center_improve"),]),
                 
      
       ("center_build_mercenary_hq",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_mercenary_quarters, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_mercenary_hq, 0),
                                       ],
       "Build a Mercenary HQ.",[(assign, "$g_improvement_type", slot_center_has_tier_2_mercenary_hq),
                                  (jump_to_menu, "mnu_center_improve"),]),


################################################




######################## SIEGE WORKS
       ("center_build_siege_works",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_siege_works, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_great_siege_works, 0),
                                       ],
       "Build a Siege Works.",[(assign, "$g_improvement_type", slot_center_has_tier_1_siege_works),
                                  (jump_to_menu, "mnu_center_improve"),]),
                 
      
       ("center_build_great_siege_works",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_siege_works, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_great_siege_works, 0),
                                       ],
       "Build a Great Siege Works.",[(assign, "$g_improvement_type", slot_center_has_tier_2_great_siege_works),
                                  (jump_to_menu, "mnu_center_improve"),]),


################################################
      
      


      
######################## TRAINING IMPROVEMENTS
       ("center_build_training_grounds",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_training_grounds, 0),
                                       ],
       "Build Training Grounds.",[(assign, "$g_improvement_type", slot_center_tier_training_grounds),
                                  (jump_to_menu, "mnu_center_improve"),]),
                 
      
       ("center_build_training_facilities",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_tier_training_grounds, 1),
                                       ],
       "Build Training Facilities.",[(assign, "$g_improvement_type", slot_center_tier_training_grounds),
                                  (jump_to_menu, "mnu_center_improve"),]),


################################################

      
      
      
      
      
######################## TRAINING IMPROVEMENTS
       ("center_build_jousting_lists",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (store_faction_of_party, ":cur_fief_faction", "$g_encountered_party"),
                                      
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_western),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_teutonic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_nordic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_iberian),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_gaelic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_welsh),
                                      (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_italian),
       
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_jousting_lists, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_tournament_grounds, 0),
                                       ],
       "Build Jousting Lists.",[(assign, "$g_improvement_type", slot_center_has_tier_1_jousting_lists),
                                  (jump_to_menu, "mnu_center_improve"),]),
                 
      
       ("center_build_tournament_grounds",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (store_faction_of_party, ":cur_fief_faction", "$g_encountered_party"),
                                      
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_western),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_teutonic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_nordic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_iberian),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_gaelic),
                                      (this_or_next|faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_welsh),
                                      (faction_slot_eq, ":cur_fief_faction", slot_faction_culture, fac_culture_italian),
                                      
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_jousting_lists, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_tier_2_tournament_grounds, 0),
                                       ],
       "Build Tournament Grounds.",[(assign, "$g_improvement_type", slot_center_has_tier_2_tournament_grounds),
                                  (jump_to_menu, "mnu_center_improve"),]),


################################################
      
      
      
      
####################### VILLAGE GUARDS
       # ("center_build_village_guards",[(eq, reg6, 0),
                                      # (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                      
                                      # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_1_village_guards, 0),
                                       # ],
       # "Hire Village Guards to defend the fief.",[(assign, "$g_improvement_type", slot_center_has_tier_1_village_guards),
                                  # (jump_to_menu, "mnu_center_improve"),]),
                 

###############################################
      
      
      
      
      ("center_build_military_exit",[(eq, reg6, 0)], "Go back.",
       [
           (jump_to_menu, "mnu_center_manage"),
        ]
       ),
      
      
    ],
),





########################### KNIGHT CHAPTERS
("knight_chapter_select",mnf_scale_picture,
   "Select which chapter you wish to build here",
   "none",
    [],
    [
    ############### TIER 1
       ("center_build_chapter_minor_teutonic",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_chapter_teutonic, 0),
                                      # (party_slot_eq, "$g_encountered_party", slot_center_has_tier_5_huge_cathedral, 1),
                                       ],
       "Build a minor Teutonic chapter.",[(assign, "$g_improvement_type", slot_center_has_chapter_teutonic),
                                  (jump_to_menu, "mnu_center_improve"),]),
      

      
      ("center_build_chapter_exit",[], "Go back.",
       [
           (jump_to_menu, "mnu_improvement_military_select"),
        ]
       ),
      
      
      
    ],
  ),
######################################################






########################### MERC CAMPS
("merc_camp_select",mnf_scale_picture,
   "Select which camp you wish to build here",
   "none",
    [],
    [
############### CUMAN
       ("center_build_camp_minor_cuman",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      ########### HUNGARY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_9"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_14"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_15"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_16"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_7_17"),

                                      ########### BULGARIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_30_7"),
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_11"),
                                      (eq, "$g_encountered_party", "p_village_15_12"),

                                       ],
       "Build a minor Cuman camp.",[(assign, "$g_improvement_type", slot_center_has_camp_cuman),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_large_cuman",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      ########### HUNGARY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_9"),

                                      ########### BULGARIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_3"),
                                      
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (eq, "$g_encountered_party", "p_castle_15_6"),
                                       ],
       "Build a large Cuman camp.",[(assign, "$g_improvement_type", slot_center_has_camp_cuman),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_major_cuman",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_cuman, 0),
                                      ########### HUNGARY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_7_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_7_9"),

                                      ########### BULGARIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_30_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_30_3"),
                                      
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (eq, "$g_encountered_party", "p_castle_15_6"),
                                       ],
       "Build a major Cuman camp.",[(assign, "$g_improvement_type", slot_center_has_camp_cuman),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
      
############### KIPCHAK
       ("center_build_camp_minor_kipchak",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_14"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_15"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_16"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_8"),
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_15_11"),
                                      (eq, "$g_encountered_party", "p_village_15_12"),
                                      
                                       ],
       "Build a minor Kipchak camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kipchak),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_large_kipchak",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (eq, "$g_encountered_party", "p_castle_15_6"),
                                       ],
       "Build a large Kipchak camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kipchak),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_major_kipchak",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kipchak, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      
                                      ########### HALYCH-VOLHYNIA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_15_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_15_5"),
                                      (eq, "$g_encountered_party", "p_castle_15_6"),
                                       ],
       "Build a major Kipchak camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kipchak),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
      
     
      
############### MONGOL
       ("center_build_camp_minor_mongol",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_14"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_15"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_3_16"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_8_8"),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_8"),
                                      (eq, "$g_encountered_party", "p_village_27_9"),
                                       ],
       "Build a minor Mongol camp.",[(assign, "$g_improvement_type", slot_center_has_camp_mongol),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_large_mongol",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                       ],
       "Build a large Mongol camp.",[(assign, "$g_improvement_type", slot_center_has_camp_mongol),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_major_mongol",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_mongol, 0),
                                      ########### GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_3_8"),
                                      
                                      ########### NOVGOROD
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_8_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_8_4"),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (eq, "$g_encountered_party", "p_castle_27_6"),
                                       ],
       "Build a major Mongol camp.",[(assign, "$g_improvement_type", slot_center_has_camp_mongol),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
      
      
############### GEORGIAN
       ("center_build_camp_minor_georgian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_8"),
                                      (eq, "$g_encountered_party", "p_village_27_9"),
                                      
                                      ############ GOLDEN HORDE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a minor Georgian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_georgian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_large_georgian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      ############ GOLDEN HORDE
                                      (eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a large Georgian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_georgian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_major_georgian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_georgian, 0),
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      ############ GOLDEN HORDE
                                      (eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a major Georgian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_georgian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      

############### KWAREZMIAN
       ("center_build_camp_minor_kwarezmian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      
                                      ############ GOLDEN HORDE
                                      (eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a minor Kwarezmian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kwarezmian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_large_kwarezmian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      
                                      ############ GOLDEN HORDE
                                      (eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a large Kwarezmian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kwarezmian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_camp_major_kwarezmian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_camp_kwarezmian, 0),
                                      
                                      ############ GOLDEN HORDE
                                      (eq, "$g_encountered_party", "p_town_3_1"),
                                       ],
       "Build a major Kwarezmian camp.",[(assign, "$g_improvement_type", slot_center_has_camp_kwarezmian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      ("center_build_camp_exit",[], "Go back.",
       [
           (jump_to_menu, "mnu_improvement_military_select"),
        ]
      ),
      
    ],
  ),
######################################################





########################### MERC OUTPOSTS
("merc_outpost_select",mnf_scale_picture,
   "Select which outpost you wish to build here",
   "none",
    [],
    [
    
      
############### CRUSADER TURCOPOLE
       ("center_build_outpost_minor_crusader_turcopole",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      
                                      ######## only Christians can recruit
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_27_9"),
                                      
                                      ########### CRUSADER STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_23_14"),
                                      
                                      ########### MAMLUK SULTANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_5"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_7"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_14"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_15"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_16"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_25_17"),
                                      
                                      ########### HAFSID DYNASTY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_28_9"),
                                      (eq, "$g_encountered_party", "p_village_28_10"),
                             
                                       ],
       "Build a minor Turcopole outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_crusader_turcopole),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_large_crusader_turcopole",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      
                                      ######## only Christians can recruit
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      ########### CRUSADER STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_3"),
                                      
                                      ########### MAMLUK SULTANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_5"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_7"),
                                      
                                      ########### HAFSID DYNASTY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_5"),
                                      (eq, "$g_encountered_party", "p_castle_28_6"),
                             
                                       ],
       "Build a large Turcopole outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_crusader_turcopole),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_major_crusader_turcopole",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_crusader_turcopole, 0),
                                      
                                      ######## only Christians can recruit
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|faction_slot_eq, ":fief_faction", slot_faction_religion, religion_catholic),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_orthodox),
                                      
                                      
                                      ########### IL-KHANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_27_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_27_6"),
                                      
                                      ########### CRUSADER STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_23_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_23_3"),
                                      
                                      ########### MAMLUK SULTANATE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_25_5"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_25_7"),
                                      
                                      ########### HAFSID DYNASTY
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_28_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_28_5"),
                                      (eq, "$g_encountered_party", "p_castle_28_6"),
                             
                                       ],
       "Build a major Turcopole outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_crusader_turcopole),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
          
      
      
############### FINNISH
       ("center_build_outpost_minor_finnish",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      
                                      ########### SWEDEN
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_14_11"),
                                      (eq, "$g_encountered_party", "p_village_14_12"),
                                       ],
       "Build a minor Finnish outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_finnish),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_large_finnish",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      
                                      ########### SWEDEN
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_5"),
                                      (eq, "$g_encountered_party", "p_castle_14_6"),
                                       ],
       "Build a large Finnish outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_finnish),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_major_finnish",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_finnish, 0),
                                      
                                      ########### SWEDEN
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_14_3"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_14_5"),
                                      (eq, "$g_encountered_party", "p_castle_14_6"),
                                       ],
       "Build a major Finnish outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_finnish),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
      
          
      
############### WELSH & KERN
       ("center_build_outpost_minor_welsh_kern",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      
                                      ########### WELSH
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_37_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_37_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_37_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_37_3"),
                                      
                                      
                                      ########### ENGLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_9"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_8"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_9"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_10"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_11"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_12"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_13"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_14"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_15"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_16"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_17"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_18"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_9_19"),
                                      (eq, "$g_encountered_party", "p_village_9_20"),
                                      
                                       ],
       "Build a minor Welsh outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_welsh_kern),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_large_welsh_kern",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      
                                      ########### WELSH
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_37_1"),
                                      
                                      
                                      ########### ENGLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_8"),
                                      (eq, "$g_encountered_party", "p_castle_9_9"),
                                       ],
       "Build a large Welsh outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_welsh_kern),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_major_welsh_kern",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_welsh_kern, 0),
                                      
                                      ########### WELSH
                                      (this_or_next|eq, "$g_encountered_party", "p_town_37_1"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_37_1"),
                                      
                                      
                                      ########### ENGLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_9_6"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_9_8"),
                                      (eq, "$g_encountered_party", "p_castle_9_9"),
                                       ],
       "Build a major Welsh outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_welsh_kern),
                                  (jump_to_menu, "mnu_center_improve"),]),
            
          
      
############### GAELIC
       ("center_build_outpost_minor_gaelic",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), #### yeah they can station here
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      
                                      ########### IRELAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_7"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_13_8"),
                                      
                                      
                                      ########### SCOTLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_4"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_5"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_6"),
                                      (this_or_next|eq, "$g_encountered_party", "p_village_12_7"),
                                      (eq, "$g_encountered_party", "p_village_12_8"),
                                       ],
       "Build a minor Gaelic outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_gaelic),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_large_gaelic",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      
                                      ########### IRELAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_4"),
                                      
                                      
                                      ########### SCOTLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_3"),
                                      (eq, "$g_encountered_party", "p_castle_12_4"),
                                       ],
       "Build a large Gaelic outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_gaelic),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
       ("center_build_outpost_major_gaelic",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_village), 
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_outpost_gaelic, 0),
                                      
                                      ########### IRELAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_13_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_13_4"),
                                      
                                      
                                      ########### SCOTLAND
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_12_2"),
                                      
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_castle_12_3"),
                                      (eq, "$g_encountered_party", "p_castle_12_4"),
                                       ],
       "Build a major Gaelic outpost.",[(assign, "$g_improvement_type", slot_center_has_outpost_gaelic),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                 
                                 
       ("center_build_outpost_exit",[], "Go back.",
       [
           (jump_to_menu, "mnu_improvement_military_select"),
        ]
       ),
       
      
      
    ],
  ),
######################################################









########################### MERC QUARTERS
("merc_quarter_select",mnf_scale_picture,
   "Select which buildings you wish to build here",
   "none",
    [],
    [


################################################ MAMLUK
       ("center_build_quarters_minor_mamluk",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                       ],
       "Build a minor Mamluk quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_mamluk),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
            
      
       ("center_build_quarters_major_mamluk",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                       ],
       "Build a major Mamluk quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_mamluk),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
              
      
       ("center_build_quarters_hq_mamluk",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_mamluk, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (faction_slot_eq, ":fief_faction", slot_faction_religion, religion_muslim),
                                       ],
       "Build a Mamluk HQ.",[(assign, "$g_improvement_type", slot_center_has_quarters_mamluk),
                                  (jump_to_menu, "mnu_center_improve"),]),
################################################



                    
      
################################################ BYZANTINES
       ("center_build_quarters_major_varangian",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_varangian, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_varangian, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|eq, ":fief_faction", "fac_kingdom_22"), #### only Byzantines
                                      (eq, "$kaos_kings_kingdom", 22), #### only Byzantines
                                      
                                       ],
       "Build a major Varangian quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_varangian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
        
      
       ("center_build_quarters_hq_varangian",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_varangian, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_varangian, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|eq, ":fief_faction", "fac_kingdom_22"), #### only Byzantines
                                      (eq, "$kaos_kings_kingdom", 22), #### only Byzantines
                                      
                                       ],
       "Build a Varangian HQ.",[(assign, "$g_improvement_type", slot_center_has_quarters_varangian),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
      
            
       ("center_build_quarters_minor_cataphract",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|eq, ":fief_faction", "fac_kingdom_22"), #### only Byzantines
                                      (eq, "$kaos_kings_kingdom", 22), #### only Byzantines
                                      
                                       ],
       "Build a minor Cataphract quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_cataphract),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
            
            
       ("center_build_quarters_major_cataphract",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|eq, ":fief_faction", "fac_kingdom_22"), #### only Byzantines
                                      (eq, "$kaos_kings_kingdom", 22), #### only Byzantines
                                      
                                       ],
       "Build a major Cataphract quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_cataphract),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
                  
            
       ("center_build_quarters_hq_cataphract",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_cataphract, 0),
                                      (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      (this_or_next|eq, ":fief_faction", "fac_kingdom_22"), #### only Byzantines
                                      (eq, "$kaos_kings_kingdom", 22), #### only Byzantines
                                      
                                       ],
       "Build a Cataphract HQ.",[(assign, "$g_improvement_type", slot_center_has_quarters_cataphract),
                                  (jump_to_menu, "mnu_center_improve"),]),
################################################
      
      

                  
                  
######################## GENOESE CROSSBOWMEN
       ("center_build_quarters_minor_genoese",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      
                                      
                                      ########### PAPAL STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_2"),
                                      
                                      
                                      ########### VENICE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                                                            
                                      ########### GENOA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      
                                      
                                      ########### PISA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      
                                      
                                      ########### GUELPHS
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_2"),
                                      
                                      
                                      ########### GHIBELLINES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_1"),
                                      (eq, "$g_encountered_party", "p_town_41_2"),
                                      
                                       ],
       "Build a minor Genoese Crossbowmen quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_genoese),
                                  (jump_to_menu, "mnu_center_improve"),]),
                          
            
       ("center_build_quarters_major_genoese",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      
                                      
                                      ########### PAPAL STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_2"),
                                      
                                      
                                      ########### VENICE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                                                            
                                      ########### GENOA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      
                                      
                                      ########### PISA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      
                                      
                                      ########### GUELPHS
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_2"),
                                      
                                      
                                      ########### GHIBELLINES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_1"),
                                      (eq, "$g_encountered_party", "p_town_41_2"),
                                      
                                      
                                       ],
       "Build a major Genoese Crossbowmen quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_genoese),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
              
       ("center_build_quarters_hq_genoese",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_genoese, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      
                                      
                                      ########### PAPAL STATES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_21_2"),
                                      
                                      
                                      ########### VENICE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_32_3"),
                                      
                                                                            
                                      ########### GENOA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_38_1"),
                                      
                                      
                                      ########### PISA
                                      (this_or_next|eq, "$g_encountered_party", "p_town_39_1"),
                                      
                                      
                                      ########### GUELPHS
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_40_2"),
                                      
                                      
                                      ########### GHIBELLINES
                                      (this_or_next|eq, "$g_encountered_party", "p_town_41_1"),
                                      (eq, "$g_encountered_party", "p_town_41_2"),
                                      
                                      
                                       ],
       "Build a Genoese Crossbowmen HQ.",[(assign, "$g_improvement_type", slot_center_has_quarters_genoese),
                                  (jump_to_menu, "mnu_center_improve"),]),
                                  
########################################################################
      
            
      
                        
######################## BRABANTINE MERCENARIES
       ("center_build_quarters_minor_brabantine",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      

                                      ########### HOLY ROMAN EMPIRE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_5"),
                                      (eq, "$g_encountered_party", "p_town_6_6"),
                                      
                                      
                                       ],
       "Build a minor Brabantine Mercenary quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_brabantine),
                                  (jump_to_menu, "mnu_center_improve"),]),
                          
            
       ("center_build_quarters_major_brabantine",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      
                                      ########### HOLY ROMAN EMPIRE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_5"),
                                      (eq, "$g_encountered_party", "p_town_6_6"),
                                       ],
       "Build a major Brabantine Mercenary quarters.",[(assign, "$g_improvement_type", slot_center_has_quarters_brabantine),
                                  (jump_to_menu, "mnu_center_improve"),]),
      
              
       ("center_build_quarters_hq_brabantine",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      # (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 1),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_quarters_brabantine, 0),
                                      # (store_faction_of_party, ":fief_faction", "$g_encountered_party"),
                                      
                                      ########### HOLY ROMAN EMPIRE
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_1"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_2"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_3"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_4"),
                                      (this_or_next|eq, "$g_encountered_party", "p_town_6_5"),
                                      (eq, "$g_encountered_party", "p_town_6_6"),
                                       ],
       "Build a Brabantine Mercenary HQ.",[(assign, "$g_improvement_type", slot_center_has_quarters_brabantine),
                                  (jump_to_menu, "mnu_center_improve"),]),
      

########################################################################
      
      
      
      ("center_build_merc_quarter_exit",[], "Go back.",
       [
           (jump_to_menu, "mnu_improvement_military_select"),
        ]
       ),
      
      
      
    ],
  ),
######################################################



####################################################
   ("town_cheat_menus",0,
    "Fief Cheat Menus",
    "none",
    [],

    [
      ("castle_cheat_town_walls",
      [
        (eq, "$cheat_mode", 1),
        (party_slot_eq, "$current_town",slot_party_type, spt_town),
      ],
      "{!}CHEAT! Town Walls.",
      [
        (party_get_slot, ":scene", "$current_town", slot_town_walls),
        (set_jump_mission, "mt_ai_training"),
        (jump_to_scene, ":scene"),
        (change_screen_mission),
      ]),

      ("cheat_town_start_siege",
      [
        (eq, "$cheat_mode", 1),
        (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
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

      ("center_reports",
      [
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT! Show reports.",
      [
        (jump_to_menu, "mnu_center_reports"),
      ]),

      ("sail_from_port",
      [
        (party_slot_eq, "$current_town",slot_party_type, spt_town),
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT: Sail from port.",
      [
        (assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
      ]),

      

      ("castle_cheat_interior",
      [
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT! Interior.",
      [
        (set_jump_mission, "mt_ai_training"),
        (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
        (jump_to_scene, ":castle_scene"),
        (change_screen_mission),
      ]),

      ("castle_cheat_town_exterior",
      [
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT! Exterior.",
      [
        (try_begin),
          (party_slot_eq, "$current_town",slot_party_type, spt_castle),
          (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
        (else_try),
          (party_get_slot, ":scene", "$current_town", slot_town_center),
        (try_end),
        (set_jump_mission, "mt_ai_training"),
        (jump_to_scene, ":scene"),
        (change_screen_mission),
      ]),

      ("castle_cheat_dungeon",
      [
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT! Prison.",
      [
        (set_jump_mission, "mt_ai_training"),
        (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
        (jump_to_scene, ":castle_scene"),
        (change_screen_mission),
      ]),
      
      ("town_alley",
      [
        (party_slot_eq, "$current_town",slot_party_type, spt_town),
        (eq, "$cheat_mode", 1),
           ],
       "{!}CHEAT: Go to the alley.",
       [
           (party_get_slot, reg11, "$current_town", slot_town_alley),
           (set_jump_mission, "mt_ai_training"),
           (jump_to_scene, reg11),
           (change_screen_mission),
        ]),
        
              
      ("cheat_conquer_castle",[(eq, "$cheat_mode", 1),
                                   ],
       "{!}CHEAT: Instant conquer castle.",
       [
        (assign, "$g_next_menu", "mnu_castle_taken"),
        (jump_to_menu, "mnu_total_victory"),
       ]),    
        
########################## NEW SCENE REPORT
      ("debug_scene_report_1",
      [
        (eq, "$cheat_mode", 1),
      ],
      "Display siege scene",
      [
        (store_encountered_party, ":town_no"),
        (party_get_slot, ":siege_scene_id", ":town_no", slot_town_walls),
        (assign, reg60, ":siege_scene_id"),
        (display_message, "@Current siege scene is {reg60}"),
      ]),
      
      
      ("debug_scene_report_2",
      [
        (eq, "$cheat_mode", 1),
      ],
      "Display current town scene",
      [
        (store_encountered_party, ":town_no"),
        (party_get_slot, ":siege_scene_id", ":town_no", slot_town_center),
        (assign, reg60, ":siege_scene_id"),
        (display_message, "@Current town scene is {reg60}"),
      ]),
      
      # ("debug_scene_report_3",
      # [
        # (eq, "$cheat_mode", 1),
      # ],
      # "Display current siege scene",
      # [
        # (store_encountered_party, ":town_no"),
        # (party_get_slot, ":siege_scene_id", ":town_no", slot_town_walls),
        # (assign, reg60, ":siege_scene_id"),
        # (display_message, "@Current siege scene is {reg60}"),
      # ]),
      
     ("debug_go_back_dot",[], "Go back.",[(jump_to_menu, "mnu_town")]),

    ],
  ),
####################################################



####################################################
   ("change_culture",0,
    "Here you can change this fief's culture to one that you have familiarity of. ^ It costs {reg15} coins to apply the effect. ^ Your faction culture: {s11} ^ Current fief culture: {s12}",
    "none",
    [
    (try_begin),
      (party_slot_eq, "$current_town",slot_party_type, spt_castle),
        (assign, ":cost_orig", 7000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (assign, ":cost_orig", 10000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_village),
          (assign, ":cost_orig", 4000),
    (try_end),
    
    (assign, ":cost", ":cost_orig"),

    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    
    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    (assign, reg15, ":cost"),

    
    (store_sub, ":offset", "$g_player_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s11, ":offset"),
          
    (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
    (store_sub, ":offset", ":cur_center_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s12, ":offset"),

    ],
######################################
    [
      ("change_culture_finnish",
      [
        (eq, "$g_player_know_culture_finnish", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_finnish"),
      ],
      "Change it to Finnish.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_finnish"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Finnish.", 0x0000ff),
      ]),

      
      ("change_culture_mazovian",
      [
        (eq, "$g_player_know_culture_mazovian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_mazovian"),
      ],
      "Change it to Mazovian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_mazovian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Mazovian.", 0x0000ff),
      ]),

      
      ("change_culture_serbian",
      [
        (eq, "$g_player_know_culture_serbian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_serbian"),
      ],
      "Change it to Serbian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_serbian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Serbian.", 0x0000ff),
      ]),

      
      ("change_culture_welsh",
      [
        (eq, "$g_player_know_culture_welsh", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_welsh"),
      ],
      "Change it to Welsh.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_welsh"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Welsh.", 0x0000ff),
      ]),

      
      ("change_culture_teutonic",
      [
        (eq, "$g_player_know_culture_teutonic", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_teutonic"),
      ],
      "Change it to Teutonic.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_teutonic"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Teutonic.", 0x0000ff),
      ]),

      
      ("change_culture_balkan",
      [
        (eq, "$g_player_know_culture_balkan", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_balkan"),
      ],
      "Change it to Balkanese.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_balkan"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Balkan.", 0x0000ff),
      ]),

      
      ("change_culture_rus",
      [
        (eq, "$g_player_know_culture_rus", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_rus"),
      ],
      "Change it to Rus.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_rus"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Rus.", 0x0000ff),
      ]),
##################################
################ NEW v3.9
     ("change_culture_go_back_dot",[], "Next page.",
     [
       (jump_to_menu, "mnu_ee_change_culture_2"), 
     ]),
##################################
      
     ("change_culture_go_back_dot",[], "Go back.",
     [
       (assign, reg15, 0),
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
           # (jump_to_menu, "mnu_town"),
           (jump_to_menu, "mnu_ee_center_manage"),  #### NEW v2.4
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
       (try_end),
     ]),

    ],
  ),
####################################################





################################ NEW v3.9
   ("ee_change_culture_2",0,
    "Here you can change this fief's culture to one that you have familiarity of. ^ It costs {reg15} coins to apply the effect. ^ Your faction culture: {s11} ^ Current fief culture: {s12}",
    "none",
    [
    (try_begin),
      (party_slot_eq, "$current_town",slot_party_type, spt_castle),
        (assign, ":cost_orig", 7000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (assign, ":cost_orig", 10000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_village),
          (assign, ":cost_orig", 4000),
    (try_end),
    
    (assign, ":cost", ":cost_orig"),

    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    
    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    (assign, reg15, ":cost"),

    
    (store_sub, ":offset", "$g_player_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s11, ":offset"),
          
    (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
    (store_sub, ":offset", ":cur_center_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s12, ":offset"),

    ],

    [
##################################
      ("change_culture_nordic",
      [
        (eq, "$g_player_know_culture_nordic", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_nordic"),
      ],
      "Change it to Nordic.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_nordic"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Nordic.", 0x0000ff),
      ]),

      
      ("change_culture_baltic",
      [
        (eq, "$g_player_know_culture_baltic", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_baltic"),
      ],
      "Change it to Baltic.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_baltic"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Baltic.", 0x0000ff),
      ]),

      
      ("change_culture_marinid",
      [
        (eq, "$g_player_know_culture_marinid", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_marinid"),
      ],
      "Change it to Marinid.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_marinid"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Marinid.", 0x0000ff),
      ]),

      
      ("change_culture_mamluke",
      [
        (eq, "$g_player_know_culture_mamluke", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_mamluke"),
      ],
      "Change it to Mamluke.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_mamluke"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Mamluke.", 0x0000ff),
      ]),

      
      ("change_culture_byzantium",
      [
        (eq, "$g_player_know_culture_byzantium", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_byzantium"),
      ],
      "Change it to Byzantine.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_byzantium"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Byzantine.", 0x0000ff),
      ]),


      ("change_culture_iberian",
      [
        (eq, "$g_player_know_culture_iberian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_iberian"),
      ],
      "Change it to Iberian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_iberian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Iberian.", 0x0000ff),
      ]),

      
      ("change_culture_italian",
      [
        (eq, "$g_player_know_culture_italian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_italian"),
      ],
      "Change it to Italian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_italian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Italian.", 0x0000ff),
      ]),
	  
      ("change_culture_player",
      [
        (eq, "$g_player_know_culture_player", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_player"),
      ],
      "Change it to Player Culture.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_player"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Player Culture.", 0x0000ff),
      ]),
##################################
     ("change_culture_next_dot",[], "Next page.",
     [
       (jump_to_menu, "mnu_ee_change_culture_3"), 
     ]),
	 
     ("change_culture_previous_dot",[], "Previous page.",
     [
       (jump_to_menu, "mnu_change_culture"), 
     ]),
##################################
      
     ("change_culture_go_back_dot",[], "Go back.",
     [
       (assign, reg15, 0),
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
           # (jump_to_menu, "mnu_town"),
           (jump_to_menu, "mnu_ee_center_manage"),  #### NEW v2.4
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
       (try_end),
     ]),

    ],
  ),
###################################################

################################ 
   ("ee_change_culture_3",0,
    "Here you can change this fief's culture to one that you have familiarity of. ^ It costs {reg15} coins to apply the effect. ^ Your faction culture: {s11} ^ Current fief culture: {s12}",
    "none",
    [
    (try_begin),
      (party_slot_eq, "$current_town",slot_party_type, spt_castle),
        (assign, ":cost_orig", 7000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (assign, ":cost_orig", 10000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_village),
          (assign, ":cost_orig", 4000),
    (try_end),
    
    (assign, ":cost", ":cost_orig"),

    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    
    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    (assign, reg15, ":cost"),

    
    (store_sub, ":offset", "$g_player_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s11, ":offset"),
          
    (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
    (store_sub, ":offset", ":cur_center_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s12, ":offset"),

    ],

    [
##################################
      ("change_culture_andalus",
      [
        (eq, "$g_player_know_culture_andalus", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_andalus"),
      ],
      "Change it to Andalusian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_andalus"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Andalusian.", 0x0000ff),
      ]),

      
      ("change_culture_gaelic",
      [
        (eq, "$g_player_know_culture_gaelic", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_gaelic"),
      ],
      "Change it to Gaelic.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_gaelic"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Gaelic.", 0x0000ff),
      ]),

      
      ("change_culture_anatolian_christian",
      [
        (eq, "$g_player_know_culture_anatolian_christian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_anatolian_christian"),
      ],
      "Change it to Anatolian Christian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_anatolian_christian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Anatolian Christian.", 0x0000ff),
      ]),

      
      ("change_culture_anatolian",
      [
        (eq, "$g_player_know_culture_anatolian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_anatolian"),
      ],
      "Change it to Anatolian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_anatolian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Anatolian.", 0x0000ff),
      ]),

      
      ("change_culture_western",
      [
        (eq, "$g_player_know_culture_western", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_western"),
      ],
      "Change it to Western European.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_western"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Western European.", 0x0000ff),
      ]),

      
      ("change_culture_mongol",
      [
        (eq, "$g_player_know_culture_mongol", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_mongol"),
      ],
      "Change it to Mongolian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_mongol"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Mongolian.", 0x0000ff),
      ]),
      
      
      ("change_culture_templar",
      [
        (eq, "$g_player_know_culture_templar", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_templar"),
      ],
      "Change it to Templar.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_templar"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Templar.", 0x0000ff),
      ]),
      
      ("change_culture_cuman",
      [
        (eq, "$g_player_know_culture_cuman", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_cuman"),
      ],
      "Change it to Cuman.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_cuman"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Cuman.", 0x0000ff),
      ]),
################################## NEW v3.10
      ("change_culture_english",
      [
        (eq, "$g_player_know_culture_english", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_english"),
      ],
      "Change it to english.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_english"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to english.", 0x0000ff),
      ]),      
      
      ("change_culture_french",
      [
        (eq, "$g_player_know_culture_french", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_french"),
      ],
      "Change it to french.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_french"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to french.", 0x0000ff),
      ]),
      
      ("change_culture_hungarian",
      [
        (eq, "$g_player_know_culture_hungarian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_hungarian"),
      ],
      "Change it to hungarian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_hungarian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to hungarian.", 0x0000ff),
      ]),
            
      ("change_culture_polish",
      [
        (eq, "$g_player_know_culture_polish", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_polish"),
      ],
      "Change it to polish.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_polish"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to polish.", 0x0000ff),
      ]),
##################################
     ("change_culture_next_dot",[], "Next page.",
     [
       (jump_to_menu, "mnu_ee_change_culture_4"), 
     ]),
	 
     ("change_culture_previous_dot",[], "Previous page.",
     [
       (jump_to_menu, "mnu_ee_change_culture_2"), 
     ]),
##################################
     ("change_culture_go_back_dot",[], "Go back.",
     [
       (assign, reg15, 0),
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
           # (jump_to_menu, "mnu_town"),
           (jump_to_menu, "mnu_ee_center_manage"),  #### NEW v2.4
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    ],
  ),
####################################################
####################################################
####################################################
####################################################
####################################################

################################ 
   ("ee_change_culture_4",0,
    "Here you can change this fief's culture to one that you have familiarity of. ^ It costs {reg15} coins to apply the effect. ^ Your faction culture: {s11} ^ Current fief culture: {s12}",
    "none",
    [
    (try_begin),
      (party_slot_eq, "$current_town",slot_party_type, spt_castle),
        (assign, ":cost_orig", 7000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_town),
          (assign, ":cost_orig", 10000),
    (else_try),
      (party_slot_eq, "$current_town",slot_party_type, spt_village),
          (assign, ":cost_orig", 4000),
    (try_end),
    
    (assign, ":cost", ":cost_orig"),

    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    
    (try_begin),
      (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
      (assign, ":max_skill", reg0),
      # (assign, ":max_skill_owner", reg1),
      (store_mul, ":cost_reduction_percent", ":max_skill", 3),
      (assign, ":cost_temp", ":cost_orig"),
      (val_div, ":cost_temp", 100),
      (val_mul, ":cost_temp", ":cost_reduction_percent"),
      (val_sub, ":cost", ":cost_temp"),
    (try_end),
    (assign, reg15, ":cost"),

    
    (store_sub, ":offset", "$g_player_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s11, ":offset"),
          
    (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
    (store_sub, ":offset", ":cur_center_culture", cultures_begin),
    (val_add, ":offset", "str_culture_1_adjective"),
    (str_store_string, s12, ":offset"),

    ],

    [
##################################
      ("change_culture_hospitaller",
      [
        (eq, "$g_player_know_culture_hospitaller", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_hospitaller"),
      ],
      "Change it to Hospitaller.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_hospitaller"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Hospitaller.", 0x0000ff),
      ]),

      
      ("change_culture_antioch",
      [
        (eq, "$g_player_know_culture_antiochian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_antioch"),
      ],
      "Change it to Antiochian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_antioch"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Antiochian.", 0x0000ff),
      ]),

      
      ("change_culture_tripoli",
      [
        (eq, "$g_player_know_culture_tripoli", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_tripoli"),
      ],
      "Change it to Tripoli.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_tripoli"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Tripoli.", 0x0000ff),
      ]),

      
      ("change_culture_ibelin",
      [
        (eq, "$g_player_know_culture_ibelin", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_ibelin"),
      ],
      "Change it to Ibelian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_ibelin"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Ibelian.", 0x0000ff),
      ]),

      
      ("change_culture_jerusalem",
      [
        (eq, "$g_player_know_culture_jerusalem", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_jerusalem"),
      ],
      "Change it to Jerusalem.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_jerusalem"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Jerusalem.", 0x0000ff),
      ]),
	  
      ("change_culture_crusader",
      [
        (eq, "$g_player_know_culture_crusader", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_crusader"),
      ],
      "Change it to Crusader.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_crusader"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to Crusader.", 0x0000ff),
      ]),
##################################
############### NEW v3.13 - 
      ("change_culture_swedish",
      [
        (eq, "$g_player_know_culture_swedish", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_swedish"),
      ],
      "Change it to swedish.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_swedish"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to swedish.", 0x0000ff),
      ]),
      
      ("change_culture_norwegian",
      [
        (eq, "$g_player_know_culture_norwegian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_norwegian"),
      ],
      "Change it to norwegian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_norwegian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to norwegian.", 0x0000ff),
      ]),
      
      
      ("change_culture_castile",
      [
        (eq, "$g_player_know_culture_castile", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_castile"),
      ],
      "Change it to castile.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_castile"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to castile.", 0x0000ff),
      ]),
      
      ("change_culture_portuguese",
      [
        (eq, "$g_player_know_culture_portuguese", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_portuguese"),
      ],
      "Change it to portuguese.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_portuguese"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to portuguese.", 0x0000ff),
      ]),
      
      ("change_culture_hre",
      [
        (eq, "$g_player_know_culture_hre", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_hre"),
      ],
      "Change it to hre.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_hre"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to hre.", 0x0000ff),
      ]),
      
      
      
      ("change_culture_sicilian",
      [
        (eq, "$g_player_know_culture_sicilian", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_sicilian"),
      ],
      "Change it to sicilian.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_sicilian"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to sicilian.", 0x0000ff),
      ]),
      
      ("change_culture_aragon",
      [
        (eq, "$g_player_know_culture_aragon", 1),
        (party_get_slot, ":cur_center_culture", "$current_town", slot_center_culture),
        (neq, ":cur_center_culture", "fac_culture_aragon"),
      ],
      "Change it to aragon.",
      [
        (call_script, "script_update_fief_culture", "$current_town", "fac_culture_aragon"),
        (troop_remove_gold, "trp_player", reg15),
        (display_message, "@Fief culture changed to aragon.", 0x0000ff),
      ]),
############### 
     # ("change_culture_next_dot",[], "Next page.",
     # [
       # (jump_to_menu, "mnu_ee_change_culture_5"), 
     # ]),
	 
     ("change_culture_previous_dot",[], "Previous page.",
     [
       (jump_to_menu, "mnu_ee_change_culture_3"), 
     ]),
##################################
     ("change_culture_go_back_dot",[], "Go back.",
     [
       (assign, reg15, 0),
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
           # (jump_to_menu, "mnu_town"),
           (jump_to_menu, "mnu_ee_center_manage"),  #### NEW v2.4
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
       (try_end),
     ]),
    ],
  ),
####################################################
####################################################
####################################################
####################################################




######################### NEW v1.9 - fixes bug where if there was a tournament in town player was unable to leave because the option disappeared.
   ("fief_misc_options",0,
    "Misc. Options.",
    "none",
    [
  
    ],

    [
    
     ("call_retinue", ##TOWN
      [
        (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
        (this_or_next|eq, ":town_lord", "trp_player"),
        (ge, "$cheat_mode", 1),
        ], "Invite local nobles to your court.",
       [
          #(call_script, "script_enter_court", "$current_town"),
          (set_jump_mission, "mt_visit_town_castle"),
          (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
          (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
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
          (party_get_slot, ":culture", "$current_town",slot_center_culture),
          (faction_get_slot, ":fac_troop", ":culture",slot_faction_tier_1_castle_troop),
          
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
    

      #tom
      ("town_spawn_manor",[
           (neg|party_slot_eq, "$current_town",slot_party_type, spt_castle),
           (party_slot_eq, "$current_town",slot_town_lord, "trp_player"),
           
           #rev3
           (party_get_slot, ":manor", "$current_town", village_slot_manor),
           # (party_get_template_id, ":manor_template", ":manor"),
           # (eq, ":manor_template", "pt_empty"),
           # (assign, "$current_manor_id", ":manor"),
           (le, ":manor", 0),
        ],
       "Invest into regional manors.",
       [
          (assign, "$g_next_menu", "mnu_town"),
          (jump_to_menu, "mnu_center_spawn_manor"),
        ]),
        

        
        
    ("visit_lady",
    [

    (neg|troop_slot_ge, "trp_player", slot_troop_spouse, kingdom_ladies_begin),

    (assign, "$love_interest_in_town", 0),
    (assign, "$love_interest_in_town_2", 0),
    (assign, "$love_interest_in_town_3", 0),
    (assign, "$love_interest_in_town_4", 0),
    (assign, "$love_interest_in_town_5", 0),
    (assign, "$love_interest_in_town_6", 0),
    (assign, "$love_interest_in_town_7", 0),
    (assign, "$love_interest_in_town_8", 0),

    (try_for_range, ":lady_no", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_slot_eq, ":lady_no", slot_troop_cur_center, "$current_town"),
        (call_script, "script_get_kingdom_lady_social_determinants", ":lady_no"),
        (assign, ":lady_guardian", reg0),

        (troop_slot_eq, ":lady_no", slot_troop_spouse, -1),
        (ge, ":lady_guardian", 0), #not sure when this would not be the case


        #must have spoken to either father or lady
        (this_or_next|troop_slot_ge, ":lady_no", slot_troop_met, 2),
            (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),

        (neg|troop_slot_eq, ":lady_no", slot_troop_met, 4),

        #must have approached father
#        (this_or_next|troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
#            (troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, -1),


        (try_begin),
            (eq, "$love_interest_in_town", 0),
            (assign, "$love_interest_in_town", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_2", 0),
            (assign, "$love_interest_in_town_2", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_3", 0),
            (assign, "$love_interest_in_town_3", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_4", 0),
            (assign, "$love_interest_in_town_4", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_5", 0),
            (assign, "$love_interest_in_town_5", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_6", 0),
            (assign, "$love_interest_in_town_6", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_7", 0),
            (assign, "$love_interest_in_town_7", ":lady_no"),
        (else_try),
            (eq, "$love_interest_in_town_8", 0),
            (assign, "$love_interest_in_town_8", ":lady_no"),
        (try_end),
    (try_end),

    (gt, "$love_interest_in_town", 0),
    ],
      "Attempt to visit a lady.",
       [
        (jump_to_menu, "mnu_lady_visit"),
        ], "Door to the garden."),
        
        
      
     ("fief_misc_options_go_back_dot",[], "Go back.",
     [
       (assign, reg15, 0),
       (try_begin),
         (this_or_next|party_slot_eq, "$current_town", slot_party_type, spt_town),
         (party_slot_eq, "$current_town", slot_party_type, spt_castle),
           (jump_to_menu, "mnu_town"),
       (else_try),
         (party_slot_eq, "$current_town", slot_party_type, spt_village),
           (jump_to_menu, "mnu_village"),
       (try_end),
     ]),

    ],
  ),
####################################################


######################## NEW v2.1 - execution by player notification 
   ("lord_executed_by_player",0,
    "By your orders, {s1} was {s2} in {s3}.",
    "none",
    [
      (str_clear, s1),
      (str_clear, s2),
      (str_clear, s3),
      
      (str_store_troop_name, s1, "$lord_to_execute"),
      (str_store_party_name, s3, "$g_execution_center"),
      
      (try_begin),
       (eq, "$g_method_of_execution", 1),
         (str_store_string, s2, "@Beheaded"),
      (else_try),
       (eq, "$g_method_of_execution", 2),
         (str_store_string, s2, "@Hanged"),
      (else_try),
       (eq, "$g_method_of_execution", 3),
         (str_store_string, s2, "@Burned alive"),
      (else_try),
       (eq, "$g_method_of_execution", 4),
         (str_store_string, s2, "@Hanged, strangled and quartered"),
      (try_end),
      
      ######## clear globals 
      (assign, "$g_execution_scheduled", 0),
      (assign, "$lord_to_execute", -1),
      (assign, "$g_execution_center", -1),
      (assign, "$g_method_of_execution", -1),
      ],
    [
      ("lord_executed_by_player_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
####################################################
######################## NEW v3.9
   ("lord_executed_by_player_field",0,
    "By your orders, {s1} was {s2}.",
    "none",
    [
      (str_clear, s1),
      (str_clear, s2),
      
      (str_store_troop_name, s1, "$lord_to_execute"),
      
      (try_begin),
       (eq, "$g_method_of_execution", 1),
         (str_store_string, s2, "@Beheaded"),
      (else_try),
       (eq, "$g_method_of_execution", 2),
         (str_store_string, s2, "@Hanged"),
      (else_try),
       (eq, "$g_method_of_execution", 3),
         (str_store_string, s2, "@Burned alive"),
      (else_try),
       (eq, "$g_method_of_execution", 4),
         (str_store_string, s2, "@Hanged, strangled and quartered"),
      (try_end),
      
      ######## clear globals 
      # (assign, "$g_execution_scheduled", 0),
      # (assign, "$lord_to_execute", -1),
      # (assign, "$g_execution_center", -1),
      # (assign, "$g_method_of_execution", -1),
      ],
    [
      ("lord_executed_by_player_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
####################################################


######################## NEW v2.1 - execution by player notification - if he escaped before
   ("lord_executed_by_player_escaped",0,
    "Unfortunately, {s1} has escaped from {s2} before his execution.",
    "none",
    [
      (str_clear, s1),
      (str_clear, s2),
      (str_clear, s3),
      
      (str_store_troop_name, s1, "$lord_to_execute"),
      (str_store_party_name, s2, "$g_execution_center"),
      
      ######## clear globals 
      (assign, "$g_execution_scheduled", 0),
      (assign, "$lord_to_execute", -1),
      (assign, "$g_execution_center", -1),
      (assign, "$g_method_of_execution", -1),
      ],
    [
      ("lord_executed_by_player_escaped_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
####################################################





######################## NEW v2.1 - assassination by player notification - suceeded
   ("lord_assassination_by_player_suceeded",0,
    "By your orders, {s1} was successfully assassinated! Now you pay the remainder of the contract cost.",
    "none",
    [
      (str_clear, s1),
      (str_store_troop_name, s1, "$lord_to_assassinate"),
      
      ######## clear globals 
      (assign, "$g_assassination_scheduled", 0),
      (assign, "$lord_to_assassinate", -1),
      ],
    [
     ("lord_assassination_by_player_suceeded_continue",[], "Continue...",
      [
      (troop_remove_gold, "trp_player", "$g_assassination_cost_success"),
      (assign, "$g_assassination_cost_success", 0),
      (change_screen_return),
      ]),
    ]
  ),
####################################################


######################## NEW v2.1 - assassination by player notification - failed
   ("lord_assassination_by_player_failed",0,
    "Unfortunately, {s1} has avoided being killed by the hired assassins.",
    "none",
    [
      (str_clear, s1),
      (str_store_troop_name, s1, "$lord_to_assassinate"),
      
      ######## clear globals 
      (assign, "$g_assassination_scheduled", 0),
      (assign, "$lord_to_assassinate", -1),
      ],
    [
      ("lord_assassination_by_player_failed_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
####################################################


######################## NEW v2.1 - assassination by player notification - if he escaped before
   ("lord_assassination_by_player_died_before",0,
    "Unfortunately, {s1} has died before the assassins could carry their mission.",
    "none",
    [
      (str_clear, s1),
      (str_store_troop_name, s1, "$lord_to_assassinate"),
      
      ######## clear globals 
      (assign, "$g_assassination_scheduled", 0),
      (assign, "$lord_to_assassinate", -1),
      ],
    [
      ("lord_assassination_by_player_died_before_continue",[], "Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
####################################################



########################### NEW v2.1 - EE menu sorting options
  ("ee_sort",mnf_scale_picture,
   "Select what and how to sort.",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
    (set_background_mesh, "mesh_pic_camp"),
   ],     
    [      
       ("sort_inventory_1",[], "Sort your inventory (compact).",
       [
         (call_script, "script_rearrange_inventory", "trp_player", 0),
         (display_message, "@Inventory sorted (compact)."),
       ]
       ),
       
       ("sort_inventory_2",[], "Sort your inventory (by cost).",
       [
         (call_script, "script_rearrange_inventory", "trp_player", 1),
         (display_message, "@Inventory sorted by item cost."),
       ]
       ),
       
       ("sort_inventory_3",[], "Sort your inventory (by type).",
       [
         (call_script, "script_rearrange_inventory", "trp_player", 2),
         (display_message, "@Inventory sorted by item type."),
       ]
       ),
       
       # ("sort_party_1",[], "Sort your party (by level)",
       # [
         # (call_script, "script_sort_party_by_troop_level", "p_main_party", 0),
         # (display_message, "@Party sorted by troop level."),
       # ]
       # ),    
       
       ("ee_sort_1",[], "Go back.",
       [
           (jump_to_menu, "mnu_enhanced_mod_options"),
        ]
       ),
    ]
  ),
######################################################



######################################################
  ("ee_center_manage",mnf_scale_picture, #### mnf_disable_all_keys
    "Choose an action.",
    "none",
    [],
    [
      ("build_improvement",
      [
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
       ],
       "Build an improvement.",
       [
         (assign, "$g_next_menu", "mnu_ee_center_manage"),
         (jump_to_menu, "mnu_center_manage"),
       ]),
	   

      ("walled_center_move_court",
      [
      (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
      # (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
      (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),  ######### NEW v3.3
      (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
      # (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
      (eq, "$g_encountered_party_faction", "$players_kingdom"),  ######### NEW v3.3
      (neq, "$g_player_court", "$current_town"),
      ],
      "Move your court here.",
       [
           (jump_to_menu, "mnu_establish_court"),
        ]),
		
######################### NEW v1.8
      ("change_culture_walled_center",
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
       , "Change this fief's culture.",
       [
         (jump_to_menu, "mnu_change_culture"),
         
        ]),
################################################################


     ("return",[], "Return.",
       [
         (jump_to_menu, "mnu_town"),
        ]
       ),
    ],
  ),  
######################################################
  


  
######################################################
  
   ("ee_minister_appoint",0,
    "It seems you don't have a minister appointed yet, therefore, one of your first steps should be to appoint a chief minister from among your companions, to handle affairs of state.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister.",
    "none",
    [
    ],
    [
      ("yes",[], "Appoint a prominient citizen from the area...",
       [
        (assign, "$g_player_minister", "trp_temporary_minister"),
        (troop_set_faction, "trp_temporary_minister", "$players_kingdom"), 
		(change_screen_return)
        ]),
		
      ("no",[], "Leave that for later (48 hours).",
       [
        (assign, "$g_minister_notification_hours", 48),
		(change_screen_return)
        ]),
     ]
  ),
######################################################

############## MF for testing start ########################### NEW v2.9-KOMKE START-

  ("camp_modding",0,
   "Select an option:",
   "none",
   [ ],
    [
      ("camp_mod_1",
		[],"Increase player's renown.",
       [(str_store_string, s1, "@Player renown is increased by 1000. "),
        (call_script, "script_change_troop_renown", "trp_player" ,1000),
        # (jump_to_menu, "mnu_camp_modding"),
        ]
       ),
### MF - change attributes and skills below, or add weapon proficiencies with (troop_raise_proficiency, "trp_player", wpt_). See header.troops.py for options   
		("camp_mod_2",
			[],
			"Raise player's attributes and skills.",
		[
		   (troop_raise_attribute, "trp_player",ca_strength,30),
           (troop_raise_attribute, "trp_player",ca_agility,30),
           (troop_raise_attribute, "trp_player",ca_intelligence,30),
           (troop_raise_attribute, "trp_player",ca_charisma,30),
		   (troop_raise_skill, "trp_player",skl_trade,10),
           (troop_raise_skill, "trp_player",skl_leadership,10),
		   (troop_raise_skill, "trp_player",skl_prisoner_management,10),
           (troop_raise_skill, "trp_player",skl_persuasion,10),
           (troop_raise_skill, "trp_player",skl_engineer,10),
           (troop_raise_skill, "trp_player",skl_first_aid,10),
           (troop_raise_skill, "trp_player",skl_surgery,10),
           (troop_raise_skill, "trp_player",skl_wound_treatment,10),
           (troop_raise_skill, "trp_player",skl_inventory_management,10),
           (troop_raise_skill, "trp_player",skl_spotting,10),
           (troop_raise_skill, "trp_player",skl_pathfinding,10),
           (troop_raise_skill, "trp_player",skl_tactics,10),
           (troop_raise_skill, "trp_player",skl_tracking,10),
           (troop_raise_skill, "trp_player",skl_trainer,10),
           (troop_raise_skill, "trp_player",skl_foraging,10),
           (troop_raise_skill, "trp_player",skl_looting,10),
           (troop_raise_skill, "trp_player",skl_horse_archery,10),
           (troop_raise_skill, "trp_player",skl_riding,10),
           (troop_raise_skill, "trp_player",skl_athletics,10),
           (troop_raise_skill, "trp_player",skl_shield,10),
           (troop_raise_skill, "trp_player",skl_weapon_master,10),
           (troop_raise_skill, "trp_player",skl_power_draw,10),
           (troop_raise_skill, "trp_player",skl_power_throw,10),
           (troop_raise_skill, "trp_player",skl_power_strike,10),
           (troop_raise_skill, "trp_player",skl_ironflesh,10),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 300),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 300),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 300),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_archery, 300),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 300),
           (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 300),
		   (display_message, "@Skills and attributes raised."),
		  ]
		),	   

### MF - Change items below to anything you want to test out, look in items.py for item_id
	  ("camp_mod_3",
		[],
		"Add gear and gold to player.",
       [
		   (troop_add_gold, "trp_player", 1000000),
		   (troop_add_item, "trp_player","itm_warhorse",imod_champion),
		   (troop_add_item, "trp_player","itm_heraldic_mail_with_surcoat",imod_lordly),
           (troop_add_item, "trp_player","itm_maciejowski_helm",imod_lordly),
           (troop_add_item, "trp_player","itm_mail_boots_long",imod_lordly),
           (troop_add_item, "trp_player","itm_mail_mittens",imod_lordly),
           (troop_add_item, "trp_player","itm_sword_type_xiiia",imod_balanced),
           (troop_add_item, "trp_player","itm_throwing_spears",imod_balanced),
           (troop_add_item, "trp_player","itm_heraldic_lance",imod_balanced),
           (troop_add_item, "trp_player","itm_tab_shield_heater_cav_b",imod_reinforced),
           
		   (troop_equip_items, "trp_player"),
           (troop_add_item, "trp_player","itm_smoked_fish",0),
           (troop_add_item, "trp_player","itm_grain",0),
           (troop_add_item, "trp_player","itm_apples",0),
           (troop_add_item, "trp_player","itm_tools",0),
           (troop_add_item, "trp_player","itm_tools",0),
           (troop_add_item, "trp_player","itm_tools",0),
           (troop_add_item, "trp_player","itm_velvet",0),
           (troop_add_item, "trp_player","itm_velvet",0),
           (troop_add_item, "trp_player","itm_wool_cloth",0),
			(display_message, "@Items added to player inventory."),
        ]
       ),
### MF - Add any units you want to test with below, look in troop.py for the troop_id	   
	   ("camp_mod_4",
		[],
		"Add units to player party.",
		[
		  (party_add_members, "p_main_party", "trp_euro_horse_4", 5),
		  (party_add_members, "p_main_party", "trp_euro_horse_3", 10),
		  (display_message, "@Party members added."),
		]
		),
		
### MF - Spawn any party you want near your party. Look in party_templates.py for pt_id
		("camp_mod_5",
			[],
		# "Spawn a party nearby",
        "Show faction AI and lords AI",##do it right after center is conquered and while being very close
		[
			# (spawn_around_party, "p_main_party", "pt_looters"),
			# (display_message, "@Party spawned nearby."),
###############################################################################################            
        (try_for_range, ":center_no", centers_begin, centers_end),
            (store_distance_to_party_from_party, ":party_distance", "p_main_party", ":center_no"),
            (lt, ":party_distance", 1),## if center is within min distance
            (str_store_party_name_link, s20, ":center_no"),
            (store_faction_of_party, ":center_faction", ":center_no"),
            (str_store_faction_name_link, s21, ":center_faction"),
        (try_end),
        (faction_get_slot, ":faction_ai_state", ":center_faction", slot_faction_ai_state),
        (try_begin),
            (eq, ":faction_ai_state", sfai_default),
            (str_store_string, s50, "@default"),
        (else_try),
            (eq, ":faction_ai_state", sfai_gathering_army),
            (str_store_string, s50, "@gathering army"),
        (else_try),
            (eq, ":faction_ai_state", sfai_attacking_center),
            (str_store_string, s50, "@attacking center"),
        (else_try),
            (eq, ":faction_ai_state", sfai_raiding_village),
            (str_store_string, s50, "@raiding village"),
        (else_try),
            (eq, ":faction_ai_state", sfai_attacking_enemy_army),
            (str_store_string, s50, "@attacking enemy army"),
        (else_try),
            (eq, ":faction_ai_state", sfai_attacking_enemies_around_center),
            (str_store_string, s50, "@attacking enemies around center"),
        (else_try),
            (eq, ":faction_ai_state", sfai_feast),
            (str_store_string, s50, "@feast"),
        (else_try),
            (eq, ":faction_ai_state", sfai_nascent_rebellion),
            (str_store_string, s50, "@nascent rebellion"),
        (try_end),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", slot_troop_is_alive, 1),  ## he's alive/active
            (store_troop_faction, ":troop_faction", ":troop_no"),
            (eq, ":troop_faction", ":center_faction"),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),
            (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
            (party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
            (try_begin),
                (eq, ":ai_state", spai_undefined),
                (str_store_string, s51, "@undefined"),
            (else_try),
                (eq, ":ai_state", spai_besieging_center),
                (str_store_string, s51, "@besieging center"),
            (else_try),
                (eq, ":ai_state", spai_patrolling_around_center),
                (str_store_string, s51, "@patrolling around center"),
            (else_try),
                (eq, ":ai_state", spai_raiding_around_center),
                (str_store_string, s51, "@raiding around_center"),
            (else_try),
                (eq, ":ai_state", spai_holding_center),
                (str_store_string, s51, "@holding center"),
            (else_try),
                (eq, ":ai_state", spai_engaging_army),
                (str_store_string, s51, "@engaging army"),
            (else_try),
                (eq, ":ai_state", spai_accompanying_army),
                (str_store_string, s51, "@accompanying army"),
            (else_try),
                (eq, ":ai_state", spai_screening_army),
                (str_store_string, s51, "@screening army"),
            (else_try),
                (eq, ":ai_state", spai_trading_with_town),
                (str_store_string, s51, "@trading with town"),
            (else_try),
                (eq, ":ai_state", spai_retreating_to_center),
                (str_store_string, s51, "@retreating to center"),
            (else_try),
                (eq, ":ai_state", spai_visiting_village),
                (str_store_string, s51, "@visiting village"),
            (try_end),
            (str_store_troop_name_link, s52, ":troop_no"),
            (str_store_party_name_link, s53, ":ai_object"),
            # (str_store_party_name, s51, ":center_no"),
            # (str_store_faction_name, s52, ":faction_no"),
            # (str_store_faction_name, s53, ":center_faction"),
            (display_log_message, "@{s20} {s21} {s50} {s52} {s51} {s53}", 0xffffff),
        (try_end),
		]
		),
        
		("camp_mod_6",
			[],
		"Give me 1000 experience",
        # "Show me player kingdom slot_faction_reinforcements_a",
        [
			(add_xp_to_troop, 1000, "trp_player"),
			(display_message, "@+1000 EXP."),
            
            # (faction_get_slot, ":reinforcements_a", "fac_player_supporters_faction", slot_faction_reinforcements_a),
            # (assign, reg50, ":reinforcements_a"),
            # (display_log_message, "@{reg50}", 0xffffff),
            
            # (try_for_range, ":center_no", centers_begin, centers_end),
            #     (store_distance_to_party_from_party, ":party_distance", "p_main_party", ":center_no"),
            #     (lt, ":party_distance", 1),## if center is within min distance
            #         (party_get_slot, reg20, ":center_no", slot_spec_mercs1),
            #         (party_get_slot, reg21, ":center_no", slot_spec_mercs1_number),
            #         (party_get_slot, reg22, ":center_no", slot_spec_mercs2),
            #         (party_get_slot, reg23, ":center_no", slot_spec_mercs2_number),
            #         (str_store_party_name, s20, ":center_no"),
            #         (store_faction_of_party, ":party_faction", ":center_no"),
            #         (str_store_faction_name, s21, ":party_faction"),
            #         (display_log_message, "@party = {s20}, faction = {s21}, mercs1 = {reg20}, mercs1_number = {reg21}, mercs2 = {reg22}, mercs2_number = {reg23}, ", 0xffffff),
            # (try_end),
            # (try_for_range, ":lord_no", kings_begin, lords_end),
            #     (troop_get_slot, ":kingdom_hero_party", ":lord_no", slot_troop_leaded_party),
            #     (gt, ":kingdom_hero_party", 0),## if lord party is not -1 or main party
            #         (party_is_active, ":kingdom_hero_party"),## if active
            #             (store_distance_to_party_from_party, ":party_distance", "p_main_party", ":kingdom_hero_party"),
            #             (lt, ":party_distance", 1),## if party is within min distance
            #             (troop_get_slot, ":controversy", ":lord_no", slot_troop_controversy),
            #             (troop_set_slot, ":lord_no", slot_troop_controversy, 100),
            #             (assign, reg50, ":controversy"),
            #             (str_store_troop_name, s50, ":lord_no"),
            #             (display_log_message, "@lord = {s50}, previous controversy = {reg50}", 0xffffff),
            # (try_end),

		]
		),

		("camp_mod_7",
			[],
		"Show me player status",
		[
            (store_current_hours, reg29),
            (try_begin),
                (eq, "$g_player_cur_role", 0),
                (str_store_string, s29, "@none"),
            (else_try),
                (eq, "$g_player_cur_role", 1),
                (str_store_string, s29, "@adventurer"),
            (else_try),
                (eq, "$g_player_cur_role", 2),
                (str_store_string, s29, "@bandit"),
            (else_try),
                (eq, "$g_player_cur_role", 3),
                (str_store_string, s29, "@mercenary captain"),
            (else_try),
                (eq, "$g_player_cur_role", 4),
                (str_store_string, s29, "@vassal"),
            (else_try),
                (eq, "$g_player_cur_role", 5),
                (str_store_string, s29, "@prince"),
            (else_try),
                (eq, "$g_player_cur_role", 6),
                (str_store_string, s29, "@king"),
            (try_end),
            (str_store_faction_name, s30, "fac_player_supporters_faction"),
            (faction_get_slot, ":supporters_leader", "fac_player_supporters_faction", slot_faction_leader),
            (str_store_troop_name, s31, ":supporters_leader"),
            (faction_get_slot, ":supporters_marshall", "fac_player_supporters_faction", slot_faction_marshall),
            (try_begin),
                (ge, ":supporters_marshall", 0),
                (str_store_troop_name, s32, ":supporters_marshall"),
            (else_try),
                (str_store_string, s32, "@No one"),
            (try_end),
            (faction_get_slot, ":supporters_faction_status", "fac_player_supporters_faction", slot_faction_state),
            (try_begin),
                (eq, ":supporters_faction_status", 0),
                (str_store_string, s33, "@active"),
            (else_try),
                (eq, ":supporters_faction_status", 1),
                (str_store_string, s33, "@defeated"),
            (else_try),
                (eq, ":supporters_faction_status", 2),
                (str_store_string, s33, "@inactive"),
            (else_try),
                (eq, ":supporters_faction_status", 3),
                (str_store_string, s33, "@inactive rebellion"),
            (else_try),
                (eq, ":supporters_faction_status", 4),
                (str_store_string, s33, "@beginning rebellion"),
            (try_end),
            (str_store_faction_name, s34, "$players_kingdom"),
            (faction_get_slot, ":player_kingdom_leader", "$players_kingdom", slot_faction_leader),
            (str_store_troop_name, s35, ":player_kingdom_leader"),
            (faction_get_slot, ":player_kingdom_marshall", "$players_kingdom", slot_faction_marshall),
            (try_begin),
                (ge, ":player_kingdom_marshall", 0),
                (str_store_troop_name, s36, ":player_kingdom_marshall"),
            (else_try),
                (str_store_string, s36, "@No one"),
            (try_end),
            (faction_get_slot, ":player_kingdom_status", "$players_kingdom", slot_faction_state),
            (try_begin),
                (eq, ":player_kingdom_status", 0),
                (str_store_string, s37, "@active"),
            (else_try),
                (eq, ":player_kingdom_status", 1),
                (str_store_string, s37, "@defeated"),
            (else_try),
                (eq, ":player_kingdom_status", 2),
                (str_store_string, s37, "@inactive"),
            (else_try),
                (eq, ":player_kingdom_status", 3),
                (str_store_string, s37, "@inactive rebellion"),
            (else_try),
                (eq, ":player_kingdom_status", 4),
                (str_store_string, s37, "@beginning rebellion"),
            (try_end),
            (str_store_faction_name, s38, "$g_player_culture"),
            (faction_get_slot, ":supporters_culture", "fac_player_supporters_faction", slot_faction_culture),
            (str_store_faction_name, s39, ":supporters_culture"),
            (display_log_message, "@current hours = {reg29}", 0xffffff),
            (display_log_message, "@player role = {s29}", 0xffffff),
            (try_begin),
                (neq, ":supporters_faction_status", 2),##if inactive do not display
                (display_log_message, "@Player followers belong to {s30}", 0xffffff),
                (display_log_message, "@Leader of followers is {s31}", 0xffffff),
                (display_log_message, "@Marshall of followers is {s32}", 0xffffff),
                (display_log_message, "@Followers faction is {s33}", 0xffffff),
                (display_log_message, "@Followers culture is {s39}", 0xffffff),
            (else_try),
                (display_log_message, "@Player doesn't have any followers", 0xffffff),
            (try_end),
            (try_begin),
                (neq, "$players_kingdom", 0),##if no kingdom do not display
                (display_log_message, "@Player belongs to {s34}", 0xffffff),
                (display_log_message, "@Leader of player's kingdom is {s35}", 0xffffff),
                (display_log_message, "@Marshall of player's kingdom is {s36}", 0xffffff),
                (display_log_message, "@Player's kingdom is {s37}", 0xffffff),
                (display_log_message, "@Player's culture is {s38}", 0xffffff),
            (else_try),
                (display_log_message, "@player doesn't belong to any kingdom", 0xffffff),
            (try_end),
		]
		),
        
		("camp_mod_8",
			[],
		"Reduce party to 1",## I need to reduce the enemy party (lord or walled fief), to test battles, fiefs, kingdoms...
		[
            (try_for_range, ":center_no", centers_begin, centers_end),
                (store_distance_to_party_from_party, ":party_distance", "p_main_party", ":center_no"),
                (party_get_num_companions, ":party_no", ":center_no"),
                (lt, ":party_distance", 1),## if center is within min distance
                    (gt, ":party_no", 1),## if center troops > 1
                        (party_clear, ":center_no"),
                        (party_add_members, ":center_no", "trp_looter", 1),
                        (str_store_party_name, s20, ":center_no"),
                        (store_faction_of_party, ":party_faction", ":center_no"),
                        (str_store_faction_name, s21, ":party_faction"),
                        (set_relation, "fac_player_faction", ":party_faction", -5),
                        (set_relation, "fac_player_supporters_faction", ":party_faction", -5),
                        (display_log_message, "@party = {s20}, number of troops reduced to 1, faction = {s21}, relation with player set to -5", 0xffffff),
            (try_end),
            (try_for_range, ":lord_no", kings_begin, lords_end),
                (troop_get_slot, ":kingdom_hero_party", ":lord_no", slot_troop_leaded_party),
                (gt, ":kingdom_hero_party", 0),## if lord party is not -1 or main party
                    (party_is_active, ":kingdom_hero_party"),## if active
                        (store_distance_to_party_from_party, ":party_distance", "p_main_party", ":kingdom_hero_party"),
                        (party_get_num_companions, ":party_no", ":kingdom_hero_party"),
                        (lt, ":party_distance", 1),## if party is within min distance
                            (gt, ":party_no", 1),## if party troops > 1
                                (party_clear, ":kingdom_hero_party"),
                                (party_add_members, ":kingdom_hero_party", "trp_looter", 1),
                                (str_store_party_name, s20, ":kingdom_hero_party"),
                                (store_faction_of_party, ":party_faction", ":kingdom_hero_party"),
                                (str_store_faction_name, s21, ":party_faction"),
                                (set_relation, "fac_player_faction", ":party_faction", -5),
                                (set_relation, "fac_player_supporters_faction", ":party_faction", -5),
                                (display_log_message, "@party = {s20}, number of troops reduced to 1, faction = {s21}, relation with player set to -5", 0xffffff),
            (try_end),
		]
		),

		("camp_mod_9",
			[],
		"Fast safe waiting",
		[
            (rest_for_hours_interactive, 24 * 365, 60, 0),##infinite waiting speed 60, not attackable.
            (change_screen_return),
		]
		),

      ("camp_mod_10",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
 
############## MF for testing end ########################### NEW v2.9-KOMKE END- 

  

########################### NEW v3.0 - things didn't fit so i had to create this new menu
  ("debug_options_new_1",mnf_scale_picture,
   "Debug 2",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
   ],     
    [      
	   ######### NEW v3.0
       ("debug_options_new_1_1",[], "Spawn a patrol in a player fief.",
       [
       (assign, ":loop_end", 0),
       (try_for_range, ":cur_fief", centers_begin, ":loop_end"),
         (party_slot_eq, ":cur_fief", slot_town_lord, "trp_player"),
		   (call_script, "script_dplmc_send_patrol", ":cur_fief", ":cur_fief", 3, "$players_kingdom", "trp_player"),
           (str_store_party_name_link, s11, ":cur_fief"),  
           (display_message, "@Patrol spawned at {s11}."),
           (assign, ":loop_end", -1),		 
       (try_end),
       ]
       ),
	   #########
	   
	   ######### NEW v3.0
       ("debug_options_new_1_2",[], "Print current statistics.",
       [
       (assign, ":pt_looters", 0),
       (assign, ":pt_curonians", 0),
       (assign, ":pt_prussians", 0),
       (assign, ":pt_samogitians", 0),
       (assign, ":pt_yotvingians", 0),
       (assign, ":pt_welsh", 0),
       (assign, ":pt_guelphs", 0),
       (assign, ":pt_ghibellines", 0),
       (assign, ":pt_crusaders", 0),
       (assign, ":pt_jihadist_raiders", 0),
       (assign, ":pt_manor", 0),
       (assign, ":pt_peasant_rebels_euro", 0),
       (assign, ":pt_steppe_bandits", 0),
       (assign, ":pt_taiga_bandits", 0),
       (assign, ":pt_desert_bandits", 0),
       (assign, ":pt_forest_bandits", 0),
       (assign, ":pt_mountain_bandits", 0),
       (assign, ":pt_sea_raiders", 0),
       (assign, ":pt_robber_knights", 0),
       (assign, ":pt_deserters", 0),
       (assign, ":pt_merchant_caravan", 0),
       (assign, ":pt_runaway_serfs", 0),
       (assign, ":pt_forager_party", 0),
       (assign, ":pt_scout_party", 0),
       (assign, ":pt_patrol_party", 0),
       (assign, ":pt_raider_party", 0),
       (assign, ":pt_kingdom_caravan_party", 0),
       (assign, ":pt_prisoner_train_party", 0),
       (assign, ":pt_kingdom_hero_party", 0),
       (assign, ":pt_war_party", 0),
       (assign, ":pt_mercenary_company", 0),
       (assign, ":pt_mercenary_warband", 0),
       (assign, ":pt_rogue_mercenaries", 0),
       (assign, ":pt_rebels", 0),
	   
       (assign, ":garrison_troops", 0),
       (assign, ":field_troops", 0),
       (assign, ":total_troops", 0),
       (assign, ":total_prisoners", 0),
	   
       (assign, ":lord_count", 0),
       (assign, ":besieged_centers", 0),
	   
       (try_for_parties, ":party"),
         (party_is_active, ":party"),
         (party_get_template_id, ":party_template", ":party"),
         (try_begin),
           (eq, ":party_template", "pt_looters"),
             (val_add, ":pt_looters", 1),
         (else_try),
           (eq, ":party_template", "pt_curonians"),
             (val_add, ":pt_curonians", 1),
         (else_try),
           (eq, ":party_template", "pt_prussians"),
             (val_add, ":pt_prussians", 1),
         (else_try),
           (eq, ":party_template", "pt_samogitians"),
             (val_add, ":pt_samogitians", 1),
         (else_try),
           (eq, ":party_template", "pt_yotvingians"),
             (val_add, ":pt_yotvingians", 1),
         (else_try),
           (eq, ":party_template", "pt_welsh"),
             (val_add, ":pt_welsh", 1),
         (else_try),
           (eq, ":party_template", "pt_guelphs"),
             (val_add, ":pt_guelphs", 1),
         (else_try),
           (eq, ":party_template", "pt_ghibellines"),
             (val_add, ":pt_ghibellines", 1),
         (else_try),
           (eq, ":party_template", "pt_crusaders"),
             (val_add, ":pt_crusaders", 1),
         (else_try),
           (eq, ":party_template", "pt_jihadist_raiders"),
             (val_add, ":pt_jihadist_raiders", 1),
         (else_try),
           (eq, ":party_template", "pt_manor"),
             (val_add, ":pt_manor", 1),
         (else_try),
           (eq, ":party_template", "pt_peasant_rebels_euro"),
             (val_add, ":pt_peasant_rebels_euro", 1),
         (else_try),
           (eq, ":party_template", "pt_steppe_bandits"),
             (val_add, ":pt_steppe_bandits", 1),
         (else_try),
           (eq, ":party_template", "pt_taiga_bandits"),
             (val_add, ":pt_taiga_bandits", 1),
         (else_try),
           (eq, ":party_template", "pt_desert_bandits"),
             (val_add, ":pt_desert_bandits", 1),
         (else_try),
           (eq, ":party_template", "pt_forest_bandits"),
             (val_add, ":pt_forest_bandits", 1),
         (else_try),
           (eq, ":party_template", "pt_mountain_bandits"),
             (val_add, ":pt_mountain_bandits", 1),
         (else_try),
           (eq, ":party_template", "pt_sea_raiders"),
             (val_add, ":pt_sea_raiders", 1),
         (else_try),
           (eq, ":party_template", "pt_robber_knights"),
             (val_add, ":pt_robber_knights", 1),
         (else_try),
           (eq, ":party_template", "pt_deserters"),
             (val_add, ":pt_deserters", 1),
         (else_try),
           (eq, ":party_template", "pt_runaway_serfs"),
             (val_add, ":pt_runaway_serfs", 1),
         (else_try),
           (eq, ":party_template", "pt_forager_party"),
             (val_add, ":pt_forager_party", 1),
         (else_try),
           (eq, ":party_template", "pt_scout_party"),
             (val_add, ":pt_scout_party", 1),
         (else_try),
           (eq, ":party_template", "pt_patrol_party"),
             (val_add, ":pt_patrol_party", 1),
         (else_try),
           (eq, ":party_template", "pt_raider_party"),
             (val_add, ":pt_raider_party", 1),
         (else_try),
           (eq, ":party_template", "pt_kingdom_caravan_party"),
             (val_add, ":pt_kingdom_caravan_party", 1),
         (else_try),
           (eq, ":party_template", "pt_prisoner_train_party"),
             (val_add, ":pt_prisoner_train_party", 1),
         (else_try),
           (eq, ":party_template", "pt_kingdom_hero_party"),
             (val_add, ":pt_kingdom_hero_party", 1),
         (else_try),
           (eq, ":party_template", "pt_war_party"),
             (val_add, ":pt_war_party", 1),
         (else_try),
           (eq, ":party_template", "pt_mercenary_company"),
             (val_add, ":pt_mercenary_company", 1),
         (else_try),
           (eq, ":party_template", "pt_mercenary_warband"),
             (val_add, ":pt_mercenary_warband", 1),
         (else_try),
           (eq, ":party_template", "pt_rogue_mercenaries"),
             (val_add, ":pt_rogue_mercenaries", 1),
         (else_try),
           (eq, ":party_template", "pt_rebels"),
             (val_add, ":pt_rebels", 1),
         (try_end),
		 
         (try_begin),
           (is_between, ":party", centers_begin, centers_end),
             (party_get_num_companions, ":number", ":party"),
             (val_add, ":garrison_troops", ":number"),
             (val_add, ":total_troops", ":number"),
             (party_get_num_prisoners, ":number", ":party"),
             (val_add, ":total_prisoners", ":number"),
         (else_try),
           (neg|is_between, ":party", centers_begin, centers_end),
             (party_get_num_companions, ":number", ":party"),
             (val_add, ":field_troops", ":number"),
             (val_add, ":total_troops", ":number"),
             (party_get_num_prisoners, ":number", ":party"),
             (val_add, ":total_prisoners", ":number"),
         (try_end),
		 
         (try_begin),
           (is_between, ":party", walled_centers_begin, walled_centers_end),
           (party_slot_ge, ":party", slot_center_is_besieged_by, 0),
             (val_add, ":besieged_centers", 1),
         (try_end),
		 
       (try_end),
	   
       (try_for_range, ":cur_lord", lords_begin, lords_end),
         (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),
           (val_add, ":lord_count", 1),		 
       (try_end),
	   
       (assign, reg20, ":pt_looters"),
       (assign, reg21, ":pt_curonians"),
       (assign, reg22, ":pt_prussians"),
       (assign, reg23, ":pt_samogitians"),
       (assign, reg24, ":pt_yotvingians"),
       (assign, reg25, ":pt_welsh"),
       (assign, reg26, ":pt_guelphs"),
       (assign, reg27, ":pt_ghibellines"),
       (assign, reg28, ":pt_crusaders"),
       (assign, reg29, ":pt_jihadist_raiders"),
       (assign, reg30, ":pt_manor"),
       (assign, reg31, ":pt_peasant_rebels_euro"),
       (assign, reg32, ":pt_steppe_bandits"),
       (assign, reg33, ":pt_taiga_bandits"),
       (assign, reg34, ":pt_desert_bandits"),
       (assign, reg35, ":pt_forest_bandits"),
       (assign, reg36, ":pt_mountain_bandits"),
       (assign, reg37, ":pt_sea_raiders"),
       (assign, reg38, ":pt_robber_knights"),
       (assign, reg39, ":pt_deserters"),
       (assign, reg40, ":pt_merchant_caravan"),
       (assign, reg41, ":pt_runaway_serfs"),
       (assign, reg42, ":pt_forager_party"),
       (assign, reg43, ":pt_scout_party"),
       (assign, reg44, ":pt_raider_party"),
       (assign, reg45, ":pt_kingdom_caravan_party"),
       (assign, reg46, ":pt_prisoner_train_party"),
       (assign, reg47, ":pt_kingdom_hero_party"),
       (assign, reg48, ":pt_war_party"),
       (assign, reg49, ":pt_mercenary_company"),
       (assign, reg50, ":pt_mercenary_warband"),
       (assign, reg51, ":pt_rogue_mercenaries"),
       (assign, reg52, ":pt_rebels"),
	   
       (assign, reg53, ":garrison_troops"),
       (assign, reg54, ":field_troops"),
       (assign, reg55, ":total_troops"),
       (assign, reg56, ":total_prisoners"),
	   
       (assign, reg57, ":lord_count"),
       (assign, reg58, ":besieged_centers"),
	   
       (display_message, "@########################"),
       (display_message, "@Manor count: {reg30}"),
       (display_message, "@Fiefs under siege: {reg58}"),
       (display_message, "@########################"),
       (display_message, "@Lord count: {reg57}"),
       (display_message, "@Kingdom hero party count: {reg47}"),
       (display_message, "@########################"),
       (display_message, "@Looter party count: {reg20}"),
       (display_message, "@Steppe bandit party count: {reg32}"),
       (display_message, "@Taiga bandit party count: {reg33}"),
       (display_message, "@Desert bandit party count: {reg34}"),
       (display_message, "@Forest bandit party count: {reg35}"),
       (display_message, "@Mountain bandit party count: {reg36}"),
       (display_message, "@Sea raiders bandit party count: {reg37}"),
       (display_message, "@Robber knight party count: {reg38}"),
       (display_message, "@Deserter party count: {reg39}"),
       (display_message, "@Mercenary warband party count: {reg50}"),
       (display_message, "@Runaway serf party count: {reg41}"),
       (display_message, "@Rogue mercenary company count: {reg51}"),
       (display_message, "@Rebel party count: {reg52}"),
       (display_message, "@########################"),
       (display_message, "@Forager party count: {reg42}"),
       (display_message, "@Scout party count: {reg43}"),
       (display_message, "@Raider party count: {reg44}"),
       (display_message, "@Caravan party count: {reg45}"),
       (display_message, "@Prisoner train party count: {reg46}"),
       (display_message, "@War party count: {reg48}"),
       (display_message, "@Mercenary company count: {reg49}"),
       (display_message, "@Prisoner train party count: {reg46}"),
       (display_message, "@########################"),
       (display_message, "@Garrisoned troop count: {reg53}"),
       (display_message, "@Troops in the field: {reg54}"),
       (display_message, "@Total deployed troops: {reg55}"),
       (display_message, "@Total prisoners: {reg56}"),
       (display_message, "@########################"),
       ]
       ),
	   #########
	   
       ("debug_options_new_1_3",[], "Activate player faction.",
       [
       (call_script, "script_activate_player_faction", "trp_player"),
       ]
       ),
	   #######################################
       ("debug_options_new_1_4",[], "Display belligerent drunk locations and troop types.",
	   [
          (try_for_range, ":belligerent_drunk_tavern", towns_begin, towns_end),
            (party_slot_ge, ":belligerent_drunk_tavern", slot_center_tavern_troop, 1),
              (party_get_slot, ":troop", ":belligerent_drunk_tavern", slot_center_tavern_troop),
              (str_store_party_name_link, s40, ":belligerent_drunk_tavern"),
              (str_store_troop_name, s41, ":troop"),
              (display_message, "@{s40} has {s41} as belligerent drunk."),
          (try_end),
		      
	   ]),
	   #######################################
       ("debug_options_new_1_5",[], "Add 5 random lords as prisoners to the main party.",
	   [
          (try_for_range, ":unused", 0, 5),
            (store_random_in_range, ":random_lord", lords_begin, lords_end),
            (party_add_prisoners, "p_main_party", ":random_lord", 1),
            (troop_set_slot, ":random_lord", slot_troop_is_alive, 1),
          (try_end),
	   ]),
	   #######################################
       ("debug_options_new_1_6",[], "Give player staff and culture.",
	   [
       (assign, "$g_player_minister", "trp_temporary_minister"),
       (troop_set_faction, "trp_temporary_minister", "$players_kingdom"),
       (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
       (troop_set_faction, "trp_dplmc_chamberlain", "$players_kingdom"),
       (assign, "$g_player_chancellor", "trp_dplmc_chancellor"),
       (troop_set_faction, "trp_dplmc_chancellor", "$players_kingdom"),
       (assign, "$g_player_constable", "trp_dplmc_constable"),
       (troop_set_faction, "trp_dplmc_constable", "$players_kingdom"),
       (faction_get_slot, ":culture", "$players_kingdom", slot_faction_culture),
       (troop_set_slot, "trp_player", slot_troop_cur_culture, ":culture"),
	   ]),
	   #######################################
       ("debug_options_new_1_7",[], "Remove all non-kingdom parties on the map.",
	   [
       (try_for_parties, ":party"),
         (party_is_active, ":party"),
         (party_get_template_id, ":party_template", ":party"),
         (this_or_next|eq, ":party_template", "pt_looters"),
         (this_or_next|eq, ":party_template", "pt_curonians"),
         (this_or_next|eq, ":party_template", "pt_prussians"),
         (this_or_next|eq, ":party_template", "pt_samogitians"),
         (this_or_next|eq, ":party_template", "pt_yotvingians"),
         (this_or_next|eq, ":party_template", "pt_welsh"),
         (this_or_next|eq, ":party_template", "pt_guelphs"),
         (this_or_next|eq, ":party_template", "pt_ghibellines"),
         (this_or_next|eq, ":party_template", "pt_crusaders"),
         (this_or_next|eq, ":party_template", "pt_jihadist_raiders"),
         (this_or_next|eq, ":party_template", "pt_peasant_rebels_euro"),
         (this_or_next|eq, ":party_template", "pt_steppe_bandits"),
         (this_or_next|eq, ":party_template", "pt_taiga_bandits"),
         (this_or_next|eq, ":party_template", "pt_desert_bandits"),
         (this_or_next|eq, ":party_template", "pt_forest_bandits"),
         (this_or_next|eq, ":party_template", "pt_mountain_bandits"),
         (this_or_next|eq, ":party_template", "pt_sea_raiders"),
         (this_or_next|eq, ":party_template", "pt_robber_knights"),
         (this_or_next|eq, ":party_template", "pt_deserters"),
         (this_or_next|eq, ":party_template", "pt_runaway_serfs"),
         (this_or_next|eq, ":party_template", "pt_forager_party"),
         (this_or_next|eq, ":party_template", "pt_scout_party"),
         (this_or_next|eq, ":party_template", "pt_patrol_party"),
         (this_or_next|eq, ":party_template", "pt_raider_party"),
         (this_or_next|eq, ":party_template", "pt_kingdom_caravan_party"),
         (this_or_next|eq, ":party_template", "pt_prisoner_train_party"),
         #(this_or_next|eq, ":party_template", "pt_kingdom_hero_party"),
         (this_or_next|eq, ":party_template", "pt_war_party"),
         (this_or_next|eq, ":party_template", "pt_mercenary_company"),
         (this_or_next|eq, ":party_template", "pt_mercenary_warband"),
         (this_or_next|eq, ":party_template", "pt_rogue_mercenaries"),
         (this_or_next|eq, ":party_template", "pt_escaped_prisoners_party"), ############### NEW v3.11 - 
         (eq, ":party_template", "pt_rebels"),
		   (remove_party, ":party"),
       (try_end),
	   ]),
	   #######################################
       ("debug_options_new_1_8",[], "Give king of england a random face (Face key slot undefined).",
	   [
       (store_random_in_range, ":random", "str_ee_face_key_euro_1", "str_ee_face_key_muslim_1"),   ### european
       (troop_set_slot, "trp_kingdom_9_lord", slot_troop_face_key, ":random"),  
       # (str_store_troop_name_link, s2, ":cur_lord"),  
       # (display_message, "@{s2} face key is {s1}"),  
       (troop_set_face_keys, "trp_kingdom_9_lord", ":random"),  
	   ]),
	   #######################################
       ("debug_options_new_1_9",[], "Give king of england a random face (Both face keys).",
	   [
       (store_random_in_range, ":random", "str_ee_face_key_euro_1", "str_ee_face_key_muslim_1"),   ### european
       (troop_set_slot, "trp_kingdom_9_lord", slot_troop_face_key, ":random"),  
       # (str_store_troop_name_link, s2, ":cur_lord"),  
       # (display_message, "@{s2} face key is {s1}"),  
       (troop_set_face_keys, "trp_kingdom_9_lord", ":random", 0),  
       (troop_set_face_keys, "trp_kingdom_9_lord", ":random", 1),  
	   ]),
	   ####################################### NEW 3.5
       ("debug_options_new_1_10",[], "Test marshall elections for current player faction.",
	   [
         (try_for_range, ":cur_lord", lords_begin, lords_end),
           (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),
             (store_troop_faction, ":cur_faction", ":cur_lord"),
             (eq, ":cur_faction", "$players_kingdom"),
               (troop_set_slot, ":cur_lord",  slot_troop_controversy, 85),
         (try_end),
         (call_script, "script_decide_faction_ai", "$players_kingdom"),
	   ]),
	   #######################################
       ("debug_options_new_1_11",[], "Test marshall elections for all factions.",
	   [
         (try_for_range, ":cur_lord", lords_begin, lords_end),
           (troop_slot_eq, ":cur_lord", slot_troop_is_alive, 1),
             # (store_troop_faction, ":lord_faction", ":cur_lord"),
             # (eq, ":lord_faction", ":cur_faction"),
               (troop_set_slot, ":cur_lord",  slot_troop_controversy, 85),
         (try_end),
		   
         (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
		   (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (call_script, "script_decide_faction_ai", ":cur_faction"),
         (try_end),
	   ]),
	   #######################################
	   #######################################
       ("debug_options_new_1_12",[], "Test crusades.",
	   [
        (assign, "$crusader_faction", "fac_papacy"),
        
        #crusade at
        (try_for_range, ":faction_no", 0, 80),  ######## NEW v3.7
          (troop_set_slot, "trp_temp_lord", ":faction_no", -1),#muslim factions
        (try_end),
        (assign, reg0, 0),
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (neg|faction_slot_eq, ":faction_no", slot_faction_religion, religion_catholic), 
          (neg|faction_slot_eq, ":faction_no", slot_faction_religion, religion_orthodox),
          (troop_set_slot, "trp_temp_lord",reg0, ":faction_no"), #muslim factions
          (val_add, reg0, 1),
        (try_end),
        (gt, reg0, 0),
        #(val_add, reg0, 1),
        (store_random_in_range, ":i", 0, reg0),
        (troop_get_slot, ":faction_no", "trp_temp_lord", ":i"), 
        (assign, "$crusade_target_faction", ":faction_no"),
		
        (str_store_faction_name_link, s1, "$crusader_faction"),
        (str_store_faction_name_link, s2, "$crusade_target_faction"),
		(display_message, "@Started crusade for {s2} by {s1}."),
	   ]),
	   #######################################
	   #######################################
       ("debug_options_new_1_13",[], "Test enlopment.",
	   [
       (assign, ":end", kingdom_ladies_end),
       (try_for_range, ":cur_lady", kingdom_ladies_begin, ":end"),
         (troop_slot_eq, ":cur_lady", slot_troop_is_alive, 1),
           (call_script, "script_courtship_event_bride_marry_groom", ":cur_lady", "trp_player", 1), #1 is elopement
           (assign, ":end", -1),
       (try_end),
	   ]),
	   #######################################
       ("debug_options_new_1_14",[], "More options.",
       [
       (jump_to_menu, "mnu_debug_options_new_2"),
       ]
       ),
	   
       ("debug_options_new_1_99",[], "Go back.",
       [
         (jump_to_menu, "mnu_debug_options"),
       ]
       ),
#######################################
    ]),
	
###################### NEW v3.7
  ("debug_options_new_2",mnf_scale_picture,
   "Debug 3",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
   ],     
   [      
	   #######################################
       ("debug_options_new2_1",[], "Give 50 random prisoners to player.",
	   [
       (try_for_range, ":unused", 0, 50),
         (store_random_in_range, ":troop", soldiers_begin, soldiers_end),
           (party_add_prisoners, "p_main_party", ":troop", 1),
       (try_end),
	   ]),
	   #######################################
	   #######################################
       ("debug_options_new2_2",[], "Give all companions their culture equipment.",
	   [
       (try_for_range, ":cur_companion", companions_begin, companions_end),
         (try_begin),
           (this_or_next|is_between, ":cur_companion", "trp_npc1", "trp_npc4"),## Balt
           (this_or_next|eq, ":cur_companion", "trp_npc16"),
           (this_or_next|eq, ":cur_companion", "trp_npc19"),
           (eq, ":cur_companion", "trp_npc26"),
             (assign, ":culture", "fac_culture_baltic"),
         (else_try),
           (this_or_next|is_between, ":cur_companion", "trp_npc4", "trp_npc7"),## Western
           (this_or_next|eq, ":cur_companion", "trp_npc21"),
           (this_or_next|eq, ":cur_companion", "trp_npc23"),
           (eq, ":cur_companion", "trp_npc25"),
             (assign, ":culture", "fac_culture_western"),
         (else_try),
           (this_or_next|is_between, ":cur_companion", "trp_npc7", "trp_npc10"),## Rus
           (this_or_next|eq, ":cur_companion", "trp_npc17"),
           (this_or_next|eq, ":cur_companion", "trp_npc22"),
           (eq, ":cur_companion", "trp_npc27"),
             (assign, ":culture", "fac_culture_rus"),
         (else_try),
           (this_or_next|is_between, ":cur_companion", "trp_npc10", "trp_npc13"),## Mamluke
           (this_or_next|eq, ":cur_companion", "trp_npc20"),
           (this_or_next|eq, ":cur_companion", "trp_npc24"),
           (eq, ":cur_companion", "trp_npc28"),
             (assign, ":culture", "fac_culture_mamluke"),
         (else_try),
           (this_or_next|is_between, ":cur_companion", "trp_npc13", "trp_npc16"),## Mongol
           (this_or_next|eq, ":cur_companion", "trp_npc18"),
           (eq, ":cur_companion", "trp_npc29"),
             (assign, ":culture", "fac_culture_mongol"),
         (try_end),
		 ############### NEW v3.7
         (call_script, "script_ee_raise_actor_attribute", ca_strength, ":cur_companion", 18), 
         (call_script, "script_ee_raise_actor_attribute", ca_agility, ":cur_companion", 15), 
         (call_script, "script_ee_raise_actor_attribute", ca_intelligence, ":cur_companion", 12), 
         (call_script, "script_ee_raise_actor_attribute", ca_charisma, ":cur_companion", 15), 
		 
         (call_script, "script_ee_raise_actor_skill", skl_leadership, ":cur_companion", 5), 
         (call_script, "script_ee_raise_actor_skill", skl_trade, ":cur_companion", 3), 
         (call_script, "script_ee_raise_actor_skill", skl_prisoner_management, ":cur_companion", 3), 
         (call_script, "script_ee_raise_actor_skill", skl_persuasion, ":cur_companion", 3), 
         (call_script, "script_ee_raise_actor_skill", skl_inventory_management, ":cur_companion", 5), 
         (call_script, "script_ee_raise_actor_skill", skl_spotting, ":cur_companion", 2), 
         (call_script, "script_ee_raise_actor_skill", skl_pathfinding, ":cur_companion", 2), 
         (call_script, "script_ee_raise_actor_skill", skl_tactics, ":cur_companion", 3), 
         (call_script, "script_ee_raise_actor_skill", skl_riding, ":cur_companion", 5), 
         (call_script, "script_ee_raise_actor_skill", skl_athletics, ":cur_companion", 2), 
         (call_script, "script_ee_raise_actor_skill", skl_shield, ":cur_companion", 3), 
         (call_script, "script_ee_raise_actor_skill", skl_weapon_master, ":cur_companion", 5), 
         (call_script, "script_ee_raise_actor_skill", skl_power_strike, ":cur_companion", 4), 
         (call_script, "script_ee_raise_actor_skill", skl_ironflesh, ":cur_companion", 5), 
		 
         (try_begin),
           (store_skill_level, ":cur_value", ":cur_companion", skl_power_draw),
           (gt, ":cur_value", 0),
             (call_script, "script_ee_raise_actor_skill", skl_power_draw, ":cur_companion", 6), 
         (try_end),
         (try_begin),
           (store_skill_level, ":cur_value", ":cur_companion", skl_power_throw),
           (gt, ":cur_value", 0),
             (call_script, "script_ee_raise_actor_skill", skl_power_throw, ":cur_companion", 6), 
         (try_end),
		 
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_one_handed_weapon),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_one_handed_weapon, ":cur_companion", 280),  
         (try_end),
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_two_handed_weapon),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_two_handed_weapon, ":cur_companion", 280),  
         (try_end),
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_polearm),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_polearm, ":cur_companion", 280),  
         (try_end),
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_archery),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_archery, ":cur_companion", 280),  
         (try_end),
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_crossbow),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_crossbow, ":cur_companion", 280),  
         (try_end),
         (try_begin),
           (store_proficiency_level, ":cur_value", ":cur_companion", wpt_throwing),
           (gt, ":cur_value", 60),
             (call_script, "script_ee_raise_actor_proficiency", wpt_throwing, ":cur_companion", 280),  
         (try_end),
		 #############################################
         (call_script, "script_get_random_equipment_type_from_troop_by_culture", ":cur_companion", ":culture"), 
       (try_end),
	   ]),
	   #############################################
       ("debug_options2_3",[], "Update and test belligerent drunks.",
       [
          (call_script, "script_update_other_taverngoers"), 
          (try_for_range, ":belligerent_drunk_tavern", towns_begin, towns_end),
            (party_slot_ge, ":belligerent_drunk_tavern", slot_center_tavern_troop, 1),
              (party_get_slot, ":troop", ":belligerent_drunk_tavern", slot_center_tavern_troop),
              (str_store_party_name_link, s40, ":belligerent_drunk_tavern"),
              (str_store_troop_name, s41, ":troop"),
              (display_message, "@{s40} has {s41} as belligerent drunk."),
          (try_end),
       ]
       ),
	   #############################################  NEW v3.8
       ("debug_options2_4",[], "Make all factions peaceful.",
       [
          # (store_faction_of_troop, ":faction", "trp_player"),
          # (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
            # (faction_slot_eq, ":faction", slot_faction_state, sfs_active),
            (try_for_range, ":faction2", kingdoms_begin, kingdoms_end),
              (neq, ":faction", ":faction2"),
              # (faction_slot_eq, ":faction2", slot_faction_state, sfs_active),
              (store_relation, ":cur_relation", ":faction", ":faction2"),
              (lt, ":cur_relation", 0), #AT WAR
                (call_script, "script_diplomacy_start_peace_between_kingdoms", ":faction", ":faction2", 1), 
            (try_end),
          (try_end),
       ]
       ),
	   ############################################# 
       ("debug_options2_5",[], "Start war with faction.",
       [
	   (jump_to_menu, "mnu_choose_faction_to_war_1"),
       ]
       ),
	   #############################################
       ("debug_options2_6",[], "Complete all bounty hunter quests.",
       [
          (try_begin),
            (check_quest_active, "qst_bounty_1"),
            (neg|check_quest_succeeded, "qst_bounty_1"),
            (neg|check_quest_failed, "qst_bounty_1"),
            (quest_slot_ge, "qst_bounty_1", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_1"),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_bounty_2"),
            (neg|check_quest_succeeded, "qst_bounty_2"),
            (neg|check_quest_failed, "qst_bounty_2"),
            (quest_slot_ge, "qst_bounty_2", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_2"),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_bounty_3"),
            (neg|check_quest_succeeded, "qst_bounty_3"),
            (neg|check_quest_failed, "qst_bounty_3"),
            (quest_slot_ge, "qst_bounty_3", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_3"),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_bounty_4"),
            (neg|check_quest_succeeded, "qst_bounty_4"),
            (neg|check_quest_failed, "qst_bounty_4"),
            (quest_slot_ge, "qst_bounty_4", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_4"),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_bounty_5"),
            (neg|check_quest_succeeded, "qst_bounty_5"),
            (neg|check_quest_failed, "qst_bounty_5"),
            (quest_slot_ge, "qst_bounty_5", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_5"),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_bounty_6"),
            (neg|check_quest_succeeded, "qst_bounty_6"),
            (neg|check_quest_failed, "qst_bounty_6"),
            (quest_slot_ge, "qst_bounty_6", slot_quest_current_state, 0),
            (call_script, "script_succeed_quest_bounty", "qst_bounty_6"),
          (try_end),
       ]
       ),
	   #############################################
	   #######################################
       ("debug_options2_7",[], "Spawn Varangians in Constantinople.",
       [
        (faction_get_slot, ":player_culture", "$players_kingdom", slot_faction_culture),
        (eq, ":player_culture", "fac_culture_byzantium"),  ######### NEW v2.4
		##########
          # (faction_set_name, "$players_kingdom", "@Roman Empire"),
          # (display_message, "@The Roman Empire has been restored!", 0xff0000),
          (party_set_slot, "p_town_26_1", slot_spec_mercs2, merc_varangians),
          (party_set_slot, "p_town_26_1", slot_spec_mercs2_party_template, "pt_company_varangian_1"),
          (party_set_slot, "p_town_26_1", slot_spec_mercs2_number, 1),
          ####### NEW
          (party_set_slot, "p_town_26_1", slot_center_has_quarters_varangian, 1),
       ]
       ),
	   #######################################
	   ############# NEW v3.8 - clear improvements
       ("debug_options2_8",[], "Reset improvements being built in all fiefs.",
       [
	   (try_for_range, ":cur_fief", centers_begin, centers_end),
         (party_get_slot, ":cur_improvement", ":cur_fief", slot_center_current_improvement),
         (gt, ":cur_improvement", 0), 
           (party_set_slot, ":cur_fief", slot_center_current_improvement, 0),
           (party_set_slot, ":cur_fief", slot_center_current_improvement_level, 0),
       (try_end),
       ]
       ),
	   #######################################
	   ############# NEW v3.9.1
       ("debug_options2_9",[], "Display all tavern dwellers and infested village locations.",
	   [
      # (call_script, "script_update_ransom_brokers"),
      # (call_script, "script_update_tavern_travellers"),
      # (call_script, "script_update_tavern_minstrels"),
      # (call_script, "script_update_booksellers"),
	  
          (try_for_range, ":tavern", towns_begin, towns_end),
		    ######## Drunks
            (try_begin),
			  (party_slot_ge, ":tavern", slot_center_tavern_troop, 1),
			    (party_get_slot, ":troop", ":tavern", slot_center_tavern_troop),
			    (str_store_party_name_link, s40, ":tavern"),
			    (str_store_troop_name, s41, ":troop"),
			    (display_message, "@{s40} has {s41} as belligerent drunk."),
            (try_end),
			
		    ######## Ransom Brokers
            (try_begin),
			  (party_slot_ge, ":tavern", slot_center_ransom_broker, 1),
			    (str_store_party_name_link, s40, ":tavern"),
			    (display_message, "@{s40} has a ransom broker."),
            (try_end),
			
		    ######## Traveller
            (try_begin),
			  (party_slot_ge, ":tavern", slot_center_tavern_traveler, 1),
			    (str_store_party_name_link, s40, ":tavern"),
			    (display_message, "@{s40} has a tavern traveler."),
            (try_end),
			
		    ######## Minstrel
            (try_begin),
			  (party_slot_ge, ":tavern", slot_center_tavern_minstrel, 1),
			    (str_store_party_name_link, s40, ":tavern"),
			    (display_message, "@{s40} has a tavern minstrel."),
            (try_end),
			
		    ######## Bookseller
            (try_begin),
			  (party_slot_ge, ":tavern", slot_center_tavern_bookseller, 1),
			    (str_store_party_name_link, s40, ":tavern"),
			    (display_message, "@{s40} has a bookseller."),
            (try_end),
          (try_end),
	  
		  ### promoter
          (try_begin),
            (troop_get_slot, ":tavern", "trp_fight_promoter", slot_troop_cur_center),
		    (str_store_party_name_link, s40, ":tavern"),
		    (str_store_troop_name, s41, "trp_fight_promoter"),
		    (display_message, "@{s41} is in {s40}."),
          (try_end),
			
          (try_for_range, ":village", villages_begin, villages_end),
			(party_slot_ge, ":village", slot_village_infested_by_bandits, 1),
			  (str_store_party_name_link, s40, ":village"),
			  (display_message, "@{s40} is infested by bandits."),
          (try_end),
	   ]),
	   #######################################
       ("debug_options2_10",[], "Start a quest.",
       [
       (jump_to_menu, "mnu_debug_options_quest_select_1"),
       ]
       ),
	   #######################################
       ("debug_options2_11",[], "Make Constantinople have byzantine scenes.",
       [
        (try_begin),
          (party_set_slot, "p_town_26_1", slot_town_center, "scn_byzantine_center"),
          (party_set_slot, "p_town_26_1", slot_town_castle, "scn_town_interior_byz"),
          (party_set_slot, "p_town_26_1", slot_town_prison, "scn_town_eastern_prison"),
          (party_set_slot, "p_town_26_1", slot_town_walls, "scn_byzantine_walls_belfry"),
          (party_set_slot, "p_town_26_1", slot_town_alley, "scn_town_eastern_alley"),
          (party_set_slot, "p_town_26_1", slot_town_tavern, "scn_town_eastern_tavern"),
          (party_set_slot, "p_town_26_1", slot_town_store, "scn_town_eastern_store"),
          (party_set_slot, "p_town_26_1", slot_town_arena, "scn_town_eastern_arena"),
          (party_set_slot, "p_town_26_1", slot_center_siege_with_belfry,   1),
        (try_end),
       ]
       ),
	   #######################################
       ("debug_options2_12",[], "Test compensation money for not receiving a fief.",
       [
        (try_begin),
		  (display_message, "@##################################"),
          (assign, reg6, 500),  ### default
          (try_begin),
	        (troop_slot_ge, "trp_player", slot_troop_renown, 1),
	          (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
	  	    # 1000 * 5 = 5000 + 500 = 5500
	          (store_mul, reg7, ":player_renown", 5),
			  (display_message, "@Renown is {reg7}."),
	          (val_add, reg6, reg7),
          (try_end),
          (try_begin),
            # (call_script, "script_troop_get_player_relation", ":faction_leader"),
			(store_random_in_range, reg7, -100, 101),
			(display_message, "@Relation is {reg7}."),
            (assign, ":relation", reg7),
	        (assign, reg7, 0),
	        (gt, ":relation", 0),
	          (store_mul, reg7, ":relation", 20),
	          (val_add, reg6, reg7),
			  (display_message, "@Positive relation bonus is {reg7}."),
          (else_try), ###### negative relation
	        (lt, ":relation", 0),
	          (assign, reg7, 0),
	          (val_mul, ":relation", -1), ###### turns into positive
	          (store_mul, reg7, ":relation", 20),
	          (val_sub, reg6, reg7),
			  (display_message, "@Negative relation bonus is {reg7}."),
          (try_end),
		  (display_message, "@Final value is {reg6}."),
		  (display_message, "@##################################"),
        (try_end),
       ]
       ),
	   #######################################
       ############### NEW v3.12 - 
       ("debug_options2_13",[], "Make all marshals siege something.",
       [
       (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		   (faction_set_slot, ":faction", slot_faction_ai_state, sfai_gathering_army),
       (try_end),
       ]
       ),
	   #######################################
	   #######################################
       ("debug_options2_98",[], "More options.",
       [
       (jump_to_menu, "mnu_debug_options_new_3"),
       ]
       ),
	   #######################################
       ("debug_options2_99",[], "Go back.",
       [
       (jump_to_menu, "mnu_debug_options_new_1"),
       ]
       ),
##############################################################################
    ]),
##############################################################################


###################### NEW v3.13
  ("debug_options_new_3",mnf_scale_picture,
   "Debug 4",
   "none",
   [     
    (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
   ],     
   [      
	   #######################################
       ("debug_options3_1",[], "Loot all villages.",
       [
       (try_for_range, ":village", villages_begin, villages_end),
            (call_script, "script_village_set_state",  ":village", svs_looted),
       (try_end),
       ]
       ),
	   #######################################
       ("debug_options3_2",[], "Reset acres in all fiefs.",
       [
       (try_for_range, ":fief", centers_begin, centers_end),
            (party_get_slot, ":acres", ":fief", slot_town_player_acres),
            (gt, ":acres", 0),
                (party_get_slot, ":prosp_mod", ":fief", slot_town_prosperity),
                (store_mul, ":price_mod", ":prosp_mod", 10),
                (val_sub, ":price_mod", 500),
                (store_add, ":money_prosperity", 1000, ":price_mod"),									
                (store_mul, ":money", ":money_prosperity", ":acres"),									
                (troop_add_gold, "trp_player", ":money"),
                (party_set_slot, ":fief", slot_town_player_acres, 0),
       (try_end),
       ]
       ),
	   #######################################
       ("debug_options3_99",[], "Go back.",
       [
         (jump_to_menu, "mnu_debug_options_new_2"),
       ]
       ),
###########################
]),
###########################



########################### NEW v3.9.1 - start a quest
  ("debug_options_quest_select_1", mnf_enable_hot_keys,
   "Choose a quest. (Note: This will select a random alive lord/mayor/village elder/lady as the quest giver so it's better to try this in a new adventurer start with neutral relations.)",
   "none",
    [],
    [
	   ########## Lord quests
       ("debug_options_quest_select_1_1",[], "Deliver Message.",
       [
	   (assign, ":loop_end", 50),
	   (try_for_range, ":variable1", 0, ":loop_end"),
         (store_random_in_range, ":random_npc", lords_begin, lords_end),
		 (troop_slot_eq, ":random_npc", slot_troop_is_alive, 1),
         (neg|troop_slot_ge, ":random_npc", slot_troop_prisoner_of_party, 0), 
	       (call_script, "script_ee_get_quest", "qst_deliver_message", ":random_npc"),
	       (assign, ":loop_end", -1), ##### end loop
       (try_end),
       ]
       ),
	   
	   ########## Lady quests
       ("debug_options_quest_select_1_2",[], "Visit lady.",
       [
	   (assign, ":loop_end", 50),
	   (try_for_range, ":variable1", 0, ":loop_end"),
         (store_random_in_range, ":random_npc", kingdom_ladies_begin, kingdom_ladies_end),
		 (troop_slot_eq, ":random_npc", slot_troop_is_alive, 1),
         (neg|troop_slot_ge, ":random_npc", slot_troop_prisoner_of_party, 0), 
	       (call_script, "script_ee_get_quest", "qst_visit_lady", ":random_npc"),
	       (assign, ":loop_end", -1), ##### end loop
       (try_end),
       ]
       ),
	   
	   ########## 
       ("debug_options_quest_select_1_3",[], "Incriminate loyal commander.",
       [
	   (assign, ":loop_end", 50),
	   (try_for_range, ":variable1", 0, ":loop_end"),
         (store_random_in_range, ":random_npc", lords_begin, lords_end),
		 (troop_slot_eq, ":random_npc", slot_troop_is_alive, 1),
         (neg|troop_slot_ge, ":random_npc", slot_troop_prisoner_of_party, 0), 
	       (call_script, "script_ee_get_quest", "qst_incriminate_loyal_commander", ":random_npc"),
	       (assign, ":loop_end", -1), ##### end loop
       (try_end),
       ]
       ),
	   
	   ########## 
       ("debug_options_quest_select_1_4",[], "Rescue lord.",
       [
	   (assign, ":loop_end", 50),
	   (try_for_range, ":variable1", 0, ":loop_end"),
         (store_random_in_range, ":random_npc", kingdom_ladies_begin, kingdom_ladies_end),
		 (troop_slot_eq, ":random_npc", slot_troop_is_alive, 1),
         (neg|troop_slot_ge, ":random_npc", slot_troop_prisoner_of_party, 0), 
	       (call_script, "script_ee_get_quest", "qst_rescue_lord_by_replace", ":random_npc"),
	       (assign, ":loop_end", -1), ##### end loop
       (try_end),
       ]
       ),
       
############### 
###########################
       ("debug_options_quest_select_1_20",[], "Go back.",
       [
       (jump_to_menu, "mnu_debug_options_new_2"),
       ]
       ),
###########################
	]),
###########################

########################### NEW v3.7 - start war with faction
  ("choose_faction_to_war_1", mnf_enable_hot_keys,
   "Choose a faction to start a war with.",
   "none",
    [],
    [
      ("debug_choose_faction_to_war_back",[], "Go back.", [(jump_to_menu, "mnu_debug_options_new_2")]),
########################
    ]+[("choose_faction_1"+str(x+1),
        [
        (store_add, ":faction", kingdoms_begin, x),
        ########(party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
        ], "{s0}",
        [
        (store_add, ":faction", kingdoms_begin, x),
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(0, 8)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_war_2")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_war_2", mnf_enable_hot_keys,
    "Choose a faction to start a war with.",
    "none",
     [],
    [
      ("debug_choose_faction_to_war_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options_new_2")]),
      ("debug_choose_faction_to_war_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_war_1")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        ########((party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(8, 16)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_war_3")]),
    ]
  ),

################################################
  ("choose_faction_to_war_3", mnf_enable_hot_keys,
    "Choose a faction to start a war with.",
    "none",
     [],
    [
      ("debug_choose_faction_to_war_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options_new_2")]),
      ("debug_choose_faction_to_war_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_war_2")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        ########((party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(16, 24)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_war_4")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_war_4", mnf_enable_hot_keys,
    "Choose a faction to start a war with.",
    "none",
     [],
    [
      ("debug_choose_faction_to_war_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options_new_2")]),
      ("debug_choose_faction_to_war_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_war_3")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        ########((party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),                 
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(24, 32)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_war_5")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_war_5", mnf_enable_hot_keys,
    "Choose a faction to start a war with.",
    "none",
     [],
    [
      ("debug_choose_faction_to_war_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options_new_2")]),
      ("debug_choose_faction_to_war_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_war_4")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        ########((party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(32, 40)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_war_6")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_war_6", mnf_enable_hot_keys,
    "Choose a faction to start a war with.",
    "none",
     [],
    [
      ("debug_choose_faction_to_war_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_war_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_war_5")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        ########((party_slot_eq, ":faction", slot_faction_state, sfs_active),  ####### NEW v3.8
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
		(call_script, "script_diplomacy_start_war_between_kingdoms", ":faction", "$players_kingdom", 1),
        ]) for x in range(40, 42)]
      # ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_6")]),
  ),
################################################





####### NEW v3.0-KOMKE START-This will notify the player when a fief improvement is finished
   ("notification_building_constructed",0,
    "Construction of {s0} in {s1} has finished.",
    "none",
    [
      (assign, ":cur_improvement", "$g_notification_menu_var1"),## improvement in parameter 1
      (assign, ":cur_improvement_level", "$g_notification_menu_var3"),## NEW v3.8
      (call_script, "script_get_improvement_details", ":cur_improvement", ":cur_improvement_level"),## improvement string stored in s0
      (str_store_party_name_link, s1, "$g_notification_menu_var2"),## fief in parameter 2
      ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),
####### NEW v3.0-KOMKE END-
  
######################################################
  
####### NEW v3.1-KOMKE START-New menus to separate court, lords and ladies and to allow enough scene positions during tournaments 
    ("castle_entered",0,
    "You are allowed to enter the castle, what do you want to do?",
    "none",
    [],
    [
      ("attend_court",
        [
        
        ], "Attend court",
        [
        (assign, ":center_no", "$current_town"),
        (assign, "$talk_context", tc_court_talk),
        (set_jump_mission, "mt_visit_town_castle"),
        (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
        #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site, ":castle_scene"),
        (reset_visitors),
        
        #Adding guards
        (store_faction_of_party, ":center_faction", ":center_no"),
        # (faction_get_slot, ":guard_troop", ":center_faction", slot_faction_castle_guard_troop), #### bugfix  
		
		############## NEW v3.3 - castle guards are taken from the current fief owner's culture
        (try_begin),
          (party_slot_ge, ":center_no", slot_town_lord, 0), 
            (party_get_slot, ":town_lord", ":center_no", slot_town_lord), 
		    (troop_get_slot, ":town_lord_culture", ":town_lord", slot_troop_cur_culture), 
		    (faction_get_slot, ":guard_troop", ":town_lord_culture", slot_faction_castle_guard_troop), 
        (else_try),
          # (le, ":guard_troop", 0),
          (assign, ":guard_troop", "trp_euro_spearman_3"),
        (try_end),
        ############################
		
        ############ NEW v1.8 - checking center culture instead of faction culture  
        # (party_get_slot, ":center_culture", ":center_no", slot_center_culture),
        # (faction_get_slot, ":guard_troop", ":center_culture", slot_faction_castle_guard_troop), #### bugfix
        (set_visitor, 6, ":guard_troop"),
        (set_visitor, 7, ":guard_troop"),
        (assign, ":cur_pos", 16),

        (try_begin),
          (eq, "$g_player_court", ":center_no"),##spouse only if center is player court
          (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (gt, ":player_spouse", 0),
          (troop_slot_eq, ":player_spouse", slot_troop_cur_center, ":center_no"),
          (set_visitor, ":cur_pos", ":player_spouse"),
          (val_add, ":cur_pos", 1),
        (try_end),
        (try_begin),##KOMKE I have to use leaded party because slot_troop_cur_center does not work for lords ???
            (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
            (gt, ":center_lord", 0),##not including player
            (troop_get_slot, ":center_lord_party", ":center_lord", slot_troop_leaded_party),
            (party_get_attached_to, ":lord_party_located", ":center_lord_party"),
            (eq, ":lord_party_located", ":center_no"),
            (set_visitor, ":cur_pos", ":center_lord"),
            (val_add, ":cur_pos", 1),
        (try_end),
        (try_begin),
          (ge, ":center_lord", 0),## if there is no lord the next line gives a script error
          (troop_get_slot, ":center_lady", ":center_lord", slot_troop_spouse),
          (gt, ":center_lady", 0),##not including player
          (troop_slot_eq, ":center_lady", slot_troop_cur_center, ":center_no"),
          (set_visitor, ":cur_pos", ":center_lady"),
          (val_add, ":cur_pos", 1),
        (try_end),
        (try_begin),
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),#minister and advisors if center belongs to player
          (eq, ":town_lord", "trp_player"),          
          (gt, "$g_player_minister", 0),
          (assign, "$g_player_minister", "trp_temporary_minister"),  #fix for wrong troops after update
          (set_visitor, ":cur_pos", "$g_player_minister"),
          (val_add, ":cur_pos", 1),
        (try_end),
        ##diplomacy begin
        (try_begin),
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),#minister and advisors if center belongs to player
          (eq, ":town_lord", "trp_player"),          
          (gt, "$g_player_chamberlain", 0),
          (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),  #fix for wrong troops after update
          (set_visitor, ":cur_pos", "$g_player_chamberlain"),
          (val_add, ":cur_pos", 1),
        (try_end),
        
        (try_begin),
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),#minister and advisors if center belongs to player
          (eq, ":town_lord", "trp_player"),          
          (gt, "$g_player_constable", 0),
          (assign, "$g_player_constable", "trp_dplmc_constable"),  #fix for wrong troops after update
          (set_visitor, ":cur_pos", "$g_player_constable"),
          (val_add, ":cur_pos", 1),
        (try_end),
        
        (try_begin),
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),#minister and advisors if center belongs to player
          (eq, ":town_lord", "trp_player"),          
          (gt, "$g_player_chancellor", 0),
          (assign, "$g_player_chancellor", "trp_dplmc_chancellor"), #fix for wrong troops after update
          (set_visitor, ":cur_pos", "$g_player_chancellor"),
          (val_add, ":cur_pos", 1),
        (try_end),
        ##diplomacy end
        
        #Lords wishing to pledge allegiance - inactive, but part of player faction
        (try_begin),
          (eq, "$g_player_court", ":center_no"),
          (faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
          (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":active_npc", slot_troop_is_alive, 1),  ## he's alive/active
            (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
            # (eq, ":active_npc_faction", "fac_player_supporters_faction"),
            (eq, ":active_npc_faction", "$players_kingdom"), ######## NEW v3.3
            (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
            (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
            (neq, ":active_npc", "$g_player_minister"),
            (set_visitor, ":cur_pos", ":active_npc"),
            (val_add, ":cur_pos", 1),
          (try_end),
        (try_end),
        
        (set_jump_entry, 0),
        (jump_to_scene, ":castle_scene"),
        (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
        (change_screen_mission),
        ]),
      
      ("talk_to_lords.",
        [
        (str_clear, s1),
        (try_begin),
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
          (str_store_string, s1, "str__join_the_feast"),
        (try_end),
        ], "Talk to the lords {s1}",
        [
        (assign, ":center_no", "$current_town"),
        (assign, "$talk_context", tc_court_talk),
        (set_jump_mission, "mt_visit_town_castle"),
        (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
        #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site, ":castle_scene"),
        (reset_visitors),
        (assign, ":cur_pos", 16),
        
        (call_script, "script_get_heroes_attached_to_center", ":center_no", "p_temp_party"),
        (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_temp_party", ":i_stack"),
          (neq, ":stack_troop", "trp_player"),##not including player
          (lt, ":cur_pos", 32), # spawn up to entry point 32 - is it possible to add another 10 spots?
          (set_visitor, ":cur_pos", ":stack_troop"),
          (val_add, ":cur_pos", 1),
        (try_end),
        
        (set_jump_entry, 0),
        (jump_to_scene, ":castle_scene"),
        (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
        (change_screen_mission),
        ]),
      
      ("talk_to_ladies.",
        [
        (str_clear, s1),
        (try_begin),
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
          (str_store_string, s1, "str__join_the_feast"),
        (try_end),
        ], "Talk to the ladies {s1}",
        [
        (assign, ":center_no", "$current_town"),
        (assign, "$talk_context", tc_court_talk),
        (set_jump_mission, "mt_visit_town_castle"),
        (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
        #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site, ":castle_scene"),
        (reset_visitors),
        (assign, ":cur_pos", 16),
        
        (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
          (neq, ":cur_troop", "trp_knight_1_1_wife"), #The one who should not appear in game
          #(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
          (troop_slot_eq, ":cur_troop", slot_troop_cur_center, ":center_no"),
          (assign, ":lady_meets_visitors", 0),
          
          (try_begin),
            (this_or_next|troop_slot_eq, "trp_player", slot_troop_betrothed, ":cur_troop"),##betrothed allowed
            (troop_slot_eq, ":cur_troop", slot_troop_betrothed, "trp_player"),
            (assign, ":lady_meets_visitors", 1), 
          (try_end),
          (try_begin), 
            (call_script, "script_get_kingdom_lady_social_determinants", ":cur_troop"),##single ladies check 
            (gt, reg0, -1),  ####### NEW v3.0
            (call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", reg0, "trp_player"),
            (gt, reg0, 0),
            (assign, ":lady_meets_visitors", 1),
          (try_end),
          (try_begin),
            (troop_slot_ge, ":cur_troop", slot_troop_spouse, 1),##married ladies allowed
            (assign, ":lady_meets_visitors", 1),
          (try_end),
          
          (eq, ":lady_meets_visitors", 1),
          (lt, ":cur_pos", 32), # spawn up to entry point 32
          (set_visitor, ":cur_pos", ":cur_troop"),
          (val_add, ":cur_pos", 1),
        (try_end),
        
        (set_jump_entry, 0),
        (jump_to_scene, ":castle_scene"),
        (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
        (change_screen_mission),
        ]),
      
      ("continue",[], "Continue",
        [
        (jump_to_menu, "mnu_town"),
        ]),
    ]
    ),
####### NEW v3.1-KOMKE END- 
    
####### NEW v3.1-KOMKE START-This will notify the player when a new lord is created in his kingdom
   ("notification_lord_created",0,
    "{s0} has joined your kingdom at {s1}.",
    "none",
    [
      (str_store_troop_name_link, s0, "$g_notification_menu_var1"),## lord in parameter 1
      (str_store_party_name_link, s1, "$g_notification_menu_var2"),## center in parameter 2
      
      ],
    [
      ("continue",[], "Continue",
       [
       (change_screen_return),
        ]),
     ]
  ),
####### NEW v3.1-KOMKE END-
    
######################################################
  


########################### NEW v2.1 - spawn a lord for a faction
  ("choose_faction_to_spawn_lord_1", mnf_enable_hot_keys,
   "Choose a faction to create a new lord.",
   "none",
    [],
    [
      ("debug_choose_faction_to_spawn_lord_back",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
########################
    ]+[("choose_faction_1"+str(x+1),
        [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
        ], "{s0}",
        [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(0, 8)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_2")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_spawn_lord_2", mnf_enable_hot_keys,
    "Choose a faction to create a new lord.",
    "none",
     [],
    [
      ("debug_choose_faction_to_spawn_lord_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_spawn_lord_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_1")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(8, 16)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_3")]),
    ]
  ),

################################################
  ("choose_faction_to_spawn_lord_3", mnf_enable_hot_keys,
    "Choose a faction to create a new lord.",
    "none",
     [],
    [
      ("debug_choose_faction_to_spawn_lord_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_spawn_lord_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_2")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(16, 24)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_4")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_spawn_lord_4", mnf_enable_hot_keys,
    "Choose a faction to create a new lord.",
    "none",
     [],
    [
      ("debug_choose_faction_to_spawn_lord_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_spawn_lord_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_3")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(24, 32)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_5")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_spawn_lord_5", mnf_enable_hot_keys,
    "Choose a faction to create a new lord.",
    "none",
     [],
    [
      ("debug_choose_faction_to_spawn_lord_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_spawn_lord_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_4")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(32, 40)]+[
      ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_6")]),
    ]
  ),
################################################

################################################
  ("choose_faction_to_spawn_lord_6", mnf_enable_hot_keys,
    "Choose a faction to create a new lord.",
    "none",
     [],
    [
      ("debug_choose_faction_to_spawn_lord_back_2",[], "Go back.", [(jump_to_menu, "mnu_debug_options")]),
      ("debug_choose_faction_to_spawn_lord_back",[], "Previous page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_5")]),
########################
    ]+[("export_import_npc"+str(x+1),
      [
        (store_add, ":faction", kingdoms_begin, x),
        (str_store_faction_name, s0, ":faction"),
      ], "{s0}",
      [
        (store_add, ":faction", kingdoms_begin, x),
        (call_script, "script_create_new_lord_for_faction", ":faction"),
        ]) for x in range(40, 42)]
      # ("export_import_next",[], "Next page", [(jump_to_menu, "mnu_choose_faction_to_spawn_lord_6")]),
  ),
################################################







######################## NEW v3.5 - moved those things here because they weren't appearing when player conquered a castle/town
  ("ee_recruits_garrison_options",0,
    "Recruits and garrison options.",
    "none",
    [
    ],
    [
########################
    # recruitment
      ("recruit_volunteers",
      [
        (call_script, "script_cf_town_recruit_volunteers_cond"),
        #tom
        (assign, ":continue", 0),
        (try_begin),
          (eq, "$use_feudal_lance", 1),
          (assign, ":continue", 1),
          # (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
          # (eq, ":town_lord", "trp_player"),
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
           (eq, "$use_feudal_lance", 0),
           (jump_to_menu, "mnu_recruit_volunteers"),
         (else_try),
           (eq, "$use_feudal_lance", 1),
           (jump_to_menu, "mnu_lance_recruitment"),
         (try_end),
        ]),
########################################
#retinue
       ("recruit_specialists",
       [
         #only in towns:
         (is_between, "$current_town", towns_begin, towns_end),
       ],
       "Recruit mercenary companions.",
       [
         (start_presentation, "prsnt_recruit_npc"),
       ]),
########################################
      ("castle_station_troops",
      [
        (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":faction", "$g_encountered_party"),   ###### NEW v3.8
        (str_clear, s10),
        
        (assign, ":player_can_draw_from_garrison", 0),
        (try_begin), #option 1 - player is town lord
          (eq, ":town_lord", "trp_player"),
          (assign, ":player_can_draw_from_garrison", 1),
        (else_try), #option 2 - town is unassigned and part of the player faction
          # (eq, ":faction", "fac_player_supporters_faction"),
          (eq, ":faction", "$players_kingdom"), ######## NEW v3.3
          (neg|party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin), #ie, zero or -1
          (assign, ":player_can_draw_from_garrison", 1),
        (else_try), #option 3 - town was captured by player
          (lt, ":town_lord", 0), #ie, unassigned
          (eq, "$players_kingdom", ":faction"),
          (eq, "$g_encountered_party", "$g_castle_requested_by_player"),
          (str_store_string, s10, "str_retrieve_garrison_warning"),
          (assign, ":player_can_draw_from_garrison", 1),
		############## NEW v3.5
         # (else_try),          
		   # (party_get_slot, ":last_besieger", "$g_encountered_party", slot_center_last_besieger), 
           # (eq, ":last_besieger", "$players_kingdom"),
             # (str_store_string, s10, "str_retrieve_garrison_warning"),
             # (assign, ":player_can_draw_from_garrison", 1),
	    ############################
        (else_try),
          (lt, ":town_lord", 0), #ie, unassigned
          (eq, "$players_kingdom", ":faction"),
            (str_store_string, s10, "str_retrieve_garrison_warning"),
            (assign, ":player_can_draw_from_garrison", 1),
        (else_try),
          (party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin),
          (eq, "$players_kingdom", ":faction"),
          (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
            (assign, ":player_can_draw_from_garrison", 1),
        (try_end),
        (eq, ":player_can_draw_from_garrison", 1),
      ],
         "Manage the garrison {s10}.",
         [
           (party_clear, "p_temp_party"),
           (jump_to_menu, "mnu_lance_prison"),
           #tom
      ]),
########################################
	  ##diplomacy start+
	  #Other option to add troops to garrison
      ("dplmc_castle_give_troops",
      [
		(party_get_slot, ":town_lord", "$current_town", slot_town_lord),
		(store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		(is_between, ":castle_faction", kingdoms_begin, kingdoms_end),

		#The player can add troops but not remove them:
		#Not owned by the player
		(neq, ":town_lord", "trp_player"),
		#Not unassigned
		(ge, ":town_lord", heroes_begin),
		#Not owned by the player's spouse
		(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
		(neg|troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
		#But nevertheless the owner will accept troops
		(call_script, "script_dplmc_player_can_give_troops_to_troop", ":town_lord"),
        (ge, reg0, 1),
      ],
      "Give troops to the garrison (cannot remove)",
      [
        (change_screen_give_members, "$current_town"),
      ]),
      ##diplomacy end+
########################################
      ("ee_back_to_town_menu",[], "Go back.",
      [
        (jump_to_menu, "mnu_town"),
      ]),
########################################
########################
    ]
  ),
######################################################

############### NEW v3.9
   ("ee_horse_ready_merchant",0,
    "Your {s1} is ready. Go pick it up at {s2}'s horse merchant.",
    "none",
    [
    ],
    [
      ("Ok",[], "Ok.",
       [
		(change_screen_return)
        ]),
     ]
  ),
#########################
   ("ee_horse_ready_constable",0,
    "Your {s1} is ready. It is in your stable in {s2}.",
    "none",
    [
    ],
    [
      ("Ok",[], "Ok.",
       [
		(change_screen_return)
        ]),
     ]
  ),
#########################
   ("ee_stable_move_constable",0,
    "Your horses and staff have arrived in {s1}.",
    "none",
    [
    ],
    [
      ("Ok",[], "Ok.",
       [
		(change_screen_return)
        ]),
     ]
  ),
#########################
   ("ee_stable_move_constable_fail",0,
    "Your horses and staff have arrived in {s1}, only to find out that the center was no longer yours. They are returning to {s2}.",
    "none",
    [
    ],
    [
      ("Ok",[], "Ok!",
       [
		(change_screen_return)
        ]),
     ]
  ),
######################################################
  
  

######################
]#####################
######################
from util_wrappers import *
from util_common import *


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]

        #swy--additional game menus, inserted at the end!
        orig_game_menus.extend(game_menus)

    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)