#=#######################################
# Lumos: This file contains all the game menus for the Outposts kit.
#        You need to place them in your module_game_menus.
#-#######################################

from header_game_menus import *
from module_constants import *
from header_items import *
from header_parties import *
from header_music import *

######## ATTENTION:
# I experienced a bug in which the fort would disappear after leaving it. Be sure to test this.
# You could disable forts to prevent it as a etmporary fix.
# If you find a solution, contact me (Lumos) ASAP!


# WHERE TO PUT THIS:
# Somewhere in the camp menus. I placed it in camp_action.
outkit_camp_menu = [
    ("action_manage_outposts",[
      ],
      "Manage your Outposts.",[(jump_to_menu, "mnu_manage_outposts"),]),
]




# WHERE TO PLACE THIS: 
# Wherever you want. In the end is good.

game_menus = [
#-## Outposts
	 ("manage_outposts", 0, "The Outpost Management Menu. ^^ Choose an action:", "none", [],
         [("build_outpost", [
		 (neg|party_slot_ge, "$current_outpost", slot_outpost_level, 1),
         (assign, ":base_cost", 3500),
         (party_get_skill_level, ":engineer_skill", "p_main_party", skl_engineer),
         (store_mul, ":engineer_reduction", ":engineer_skill", 5), #### 5% less cost per level
         (store_div, ":cost_modifier", ":base_cost", 100), 
         (val_mul, ":cost_modifier", ":engineer_reduction"), 
         (store_sub, reg10, ":base_cost", ":cost_modifier"), 
		 ], 
		    "Build an Outpost. ({reg10} coins)",
		    [(store_troop_gold, ":gold_amount", "trp_player"),
		     (try_begin),
		        (ge, ":gold_amount", reg10),
				# (assign, ":outpost_party", -1),
				# (try_begin),
				    # (party_slot_eq, "p_outpost_1", slot_outpost_level, 0),
				    # (assign, ":outpost_party", "p_outpost_1"),
				# (else_try),
				    # (party_slot_eq, "p_outpost_2", slot_outpost_level, 0),
					# (assign, ":outpost_party", "p_outpost_2"),
				# (else_try),
                    # (display_message, "@You have reached the outpost limit!"),
				# (try_end),				
				(try_begin),
				  (le, "$g_outpost_count", 0),
				    # (gt, ":outpost_party", 0),
				    (troop_remove_gold, "trp_player", reg10),
				    (rest_for_hours, 6, 5, 1), # Lumos: A crude way to add waiting.
			        # (party_relocate_near_party, ":outpost_party", "p_main_party"),
				    (set_spawn_radius, 1),
				    (spawn_around_party, "p_main_party", "pt_outpost"),
				    (assign, ":outpost_party", reg0),
				    (store_faction_of_party, ":fac_player", "p_main_party"),
				    (call_script, "script_give_center_to_faction_aux", ":outpost_party", ":fac_player"),
				    (call_script, "script_give_center_to_lord", ":outpost_party", "trp_player", 0),
				    (party_set_slot, ":outpost_party", slot_party_type, spt_outpost),
				    (party_set_slot, ":outpost_party", slot_outpost_level, 1),
			        # (enable_party, ":outpost_party"),
				    (assign, "$current_outpost", ":outpost_party"),
				    ### NEW v1.0 - this prevents crashes when managing the garrison
				    (party_add_leader, ":outpost_party", "trp_outpost_captain"), 
			        (display_message, "@Outpost built!"),
				    (assign, "$g_outpost_count", 1),  ########## NEW v3.7
			        (call_script, "script_setup_outpost_scene"),
				    (change_screen_return),
				(else_try),
                  (display_message, "@You have reached the outpost limit!"),
				(try_end),
			(else_try),
				(lt, ":gold_amount", reg10),
		        (display_message, "@You don't have enough money to build an outpost!"),
			(try_end),
			]),
			
		 ("camp_end_outpost", [], "Return to your camp.",
		    [(jump_to_menu, "mnu_camp")]
		  )]
	),

	("outpost", 0, "You pass across the barricades and enter the outpost. ^^ What do you want to do?", "none", [],
         [
			("outpost_walk_around", [], 
				"Walk around",
		    [
             (party_get_slot, ":scene", "$g_encountered_party", slot_outpost_scene),
             (jump_to_scene, ":scene"),
		     (set_jump_mission, "mt_ai_training"),
			 (change_screen_mission),
		    ]),
			
			("outpost_upgrade", [
			(party_slot_eq, "$g_encountered_party", slot_outpost_level, 1),
            (assign, ":base_cost", 7000),
            (party_get_skill_level, ":engineer_skill", "p_main_party", skl_engineer),
            (store_mul, ":engineer_reduction", ":engineer_skill", 5), #### 5% less cost per level
            (store_div, ":cost_modifier", ":base_cost", 100), 
            (val_mul, ":cost_modifier", ":engineer_reduction"), 
            (store_sub, reg10, ":base_cost", ":cost_modifier"), 
			], 
				"Upgrade outpost (better patrols and defenses)({reg10} coins)",
			[
			 (store_troop_gold, ":gold_amount", "trp_player"),
			 (try_begin),
				(ge, ":gold_amount", reg10),
				(troop_remove_gold, "trp_player", reg10),
				(rest_for_hours, 8, 5, 1), # Lumos: I should try thinking of something better.
				(party_set_slot, "$g_encountered_party", slot_outpost_level, 2),
			    (assign, "$current_outpost", "$g_encountered_party"),  ######### NEW v3.7
				(display_message, "@Outpost upgraded."),
			    (call_script, "script_setup_outpost_scene"),
				(change_screen_return),
			 (else_try),
				(lt, ":gold_amount", reg10),
				(display_message, "@You don't have enough money to upgrade the outpost"),
			(try_end),
		    ]),
				
            ("outpost_to_fort", [
			(party_slot_eq, "$g_encountered_party", slot_outpost_level, 2),
			# (neg|party_slot_ge, "p_fort", slot_outpost_level, 1),
            (assign, ":base_cost", 15000),
            (party_get_skill_level, ":engineer_skill", "p_main_party", skl_engineer),
            (store_mul, ":engineer_reduction", ":engineer_skill", 5), #### 5% less cost per level
            (store_div, ":cost_modifier", ":base_cost", 100), 
            (val_mul, ":cost_modifier", ":engineer_reduction"), 
            (store_sub, reg10, ":base_cost", ":cost_modifier"), 
			], 
			"Expand outpost to a fortified stronghold ({reg10})",
			[
			 (store_troop_gold, ":gold_amount", "trp_player"),
			 (try_begin),
			 ###### NEW v3.7 - remove outpost captain and fixed some errors
				(ge, ":gold_amount", reg10),
				(troop_remove_gold, "trp_player", reg10),
				(rest_for_hours, 18, 5, 1), # Lumos: I really don't like it. At all.
				(party_set_slot, "$current_outpost", slot_outpost_level, 0),
				(call_script, "script_party_copy", "p_temp_party", "$current_outpost"),
				(party_set_slot, "$current_outpost", slot_outpost_patrol, 0),
				(party_get_slot, ":patrol", "$current_outpost", slot_outpost_patrol),
				(remove_party, "$current_outpost"),
				(set_spawn_radius, 1),
				(spawn_around_party, "p_main_party", "pt_fort"),
				(assign, ":outpost_party", reg0),
			    (try_begin),
				  # (party_is_active, ":patrol"),
				  (gt, ":patrol", 0),
				    (party_set_ai_object, ":patrol", ":outpost_party"),
				    (party_set_slot, ":outpost_party", slot_outpost_patrol, ":patrol"),
			    (try_end),
				(store_faction_of_party, ":fac_player", "p_main_party"), # Copy the outpost garrison into temp_party
				(call_script, "script_give_center_to_faction_aux", ":outpost_party", ":fac_player"),
				(call_script, "script_give_center_to_lord", ":outpost_party", "trp_player", 0),
				(party_set_slot, ":outpost_party", slot_party_type, spt_fort),
				(party_set_slot, ":outpost_party", slot_outpost_level, 3),
				(call_script, "script_party_copy", ":outpost_party", "p_temp_party"), # Move the temp_party garriosn to the fort
				(party_clear, "p_temp_party"),
				# Lumos: Forts seem to disappear somehow, if there is no garrison.
				(party_add_leader, ":outpost_party", "trp_fort_captain"), # That's why we add an immovable leader.
				(remove_member_from_party, "trp_outpost_captain", ":outpost_party"), 
			    (assign, "$current_outpost", ":outpost_party"),
				(display_message, "@Outpost upgraded!"),
				(change_screen_return),
			####################################
			 (else_try),
				(lt, ":gold_amount", reg10),
				(display_message, "@You don't have enough money to upgrade the outpost"),
			(try_end),
		    ]),
				
			("outpost_enlist_patrol", [(party_slot_eq, "$g_encountered_party", slot_outpost_patrol, 0)], 
				"Enlist a patrol (700 denars)",
	        [(store_troop_gold, ":gold_amount", "trp_player"),
		     (try_begin),
		        (party_slot_ge, "$g_encountered_party", slot_outpost_level, 1),
			    (ge, ":gold_amount", 700),
			    (troop_remove_gold, "trp_player", 700),
			    (set_spawn_radius, 3),
			    (spawn_around_party, "$g_encountered_party", "pt_none"),
			    (assign, ":outpost_patrol", reg0),
				(party_add_members, ":outpost_patrol", "trp_ee_watchman", 20), #ADD TROOPS HERE
				(store_faction_of_party, ":fac_player", "p_main_party"),
				(party_set_faction, ":outpost_patrol", ":fac_player"),
			    (party_set_flags, ":outpost_patrol", pf_default_behavior, 0),
				(party_set_aggressiveness, ":outpost_patrol", 12), # Very aggressive
				(party_set_courage, ":outpost_patrol", 14),        # Even more courageous
				(party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 2), # I use this to dictate tehir behaviour
			    (party_set_ai_behavior, ":outpost_patrol", ai_bhvr_patrol_location),
			    (party_set_ai_object, ":outpost_patrol", "$g_encountered_party"),
				(display_message, "@Patrol enlisted!"),
			    (party_set_slot, "$g_encountered_party", slot_outpost_patrol, ":outpost_patrol"),
				(party_set_slot, ":outpost_patrol", slot_outpost_level, 1),
				(party_set_slot, ":outpost_patrol", slot_party_type, spt_patrol),
				(party_set_name, ":outpost_patrol", "@Outpost Patrol"),
			 (else_try),
			    (lt, ":gold_amount", 700),
				(display_message, "@You don't have enough money to enlist a patrol."),
		     (try_end),
			]),
						
			("outpost_patrol_training", [
			  (party_slot_ge, "$g_encountered_party", slot_outpost_patrol, 1),
			  (party_slot_eq, "$g_encountered_party", slot_outpost_level, 3),
			  (party_get_slot, ":patrol", "$g_encountered_party", slot_outpost_patrol),
			  (party_get_slot, ":level", ":patrol", slot_outpost_level),
              (assign, ":base_cost", 1000),
              (call_script, "script_get_max_skill_of_player_party", skl_trainer),
              (assign, ":trainer_skill", reg0),
              (store_mul, ":trainer_reduction", ":trainer_skill", 5), #### 5% less cost per level
              (store_div, ":cost_modifier", ":base_cost", 100), 
              (val_mul, ":cost_modifier", ":trainer_reduction"), 
              (store_sub, reg10, ":base_cost", ":cost_modifier"), 
			  (lt, ":level", 5),
			  (str_store_string, s1, "@Basic"),
			  (str_store_string, s2, "@Regular"),
			  (str_store_string, s3, "@Advanced"),
			  (str_store_string, s4, "@Expert"),
			  (str_store_string_reg, s0, ":level"),
			  (store_mul, reg0, ":level", reg10),
			  ],
				"Initiate {s0} training for the patrol ({reg0} denars).",
	        [(store_troop_gold, ":gold_amount", "trp_player"),
		     (try_begin),
		        (party_slot_ge, "$g_encountered_party", slot_outpost_level, 1),
			    (ge, ":gold_amount", reg0),
			    (troop_remove_gold, "trp_player", reg0),
				(party_get_slot, ":patrol", "$g_encountered_party", slot_outpost_patrol),
				(party_upgrade_with_xp, ":patrol", 100000, 0), #random #should guarantee all upgrade
				(display_message, "@Patrol trained!"),	
                (party_get_slot, ":level", ":patrol", slot_outpost_level),
                (val_add, ":level", 1),				
			    (party_set_slot, ":patrol", slot_outpost_level, ":level"),
			 (else_try),
			    (lt, ":gold_amount", reg0),
				(display_message, "@You don't have enough money to train the patrol."),
		     (try_end),
			]),
			
			("outpost_demolish", 
			[
		    (party_get_slot, ":level", "$g_encountered_party", slot_outpost_level),
		    (store_mul, reg10, ":level", 2000),
			],
				"Demolish your outpost. ({reg10} denars)",
	        [(store_troop_gold, ":gold_amount", "trp_player"),
		     (try_begin),
		        (ge, ":gold_amount", reg10),
		        (party_slot_ge, "$g_encountered_party", slot_outpost_level, 1),
				# (party_relocate_near_party, "p_main_party", "$g_encountered_party", 1),             
				(rest_for_hours, 2, 5, 1), # Lumos: This is the last one.
			    # (disable_party, "$g_encountered_party"),
			    (display_message, "@Outpost demolished."),
			    (party_set_slot, "$g_encountered_party", slot_outpost_level, 0),
				(party_set_slot, "$g_encountered_party", slot_outpost_patrol, 0),
				(remove_party, "$g_encountered_party"),
				(assign, "$current_outpost", -1),
				########## NEW v3.7
				(assign, "$g_outpost_count", 0),  
				(party_get_slot, ":patrol", "$g_encountered_party", slot_outpost_patrol),
				(party_is_active, ":patrol"),
				(remove_party, ":patrol"),
				##############################
				(change_screen_return),
		     (else_try),
		        (lt, ":gold_amount", reg10),
		        (display_message, "@You don't have enough money to demolish the outpost!"),
		     (try_end),
		    ]),
				
			("outpost_station_garrison", [], 
				"Station a garrison here",
			[
            (change_screen_exchange_members, 1, "$g_encountered_party"),
            ]),
						
		    ("resume_travelling",[],"Resume travelling.",
				[
				 (change_screen_return),
				]
			),
	    ],
	),
	
   (
    "fort",mnf_enable_hot_keys,
    "{s10}{s11}",
    "none",
    [
        (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (store_encountered_party,"$current_town"),
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        # (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (store_relation, ":faction_relation", ":encountered_faction", "$players_kingdom"),
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", 0),
          (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          # (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          (store_relation, ":besieger_party_relation", ":besieger_party_faction", "$players_kingdom"),
          (lt, ":besieger_party_relation", 0),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign,"$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (assign,"$g_permitted_to_center",0),
          (leave_encounter),
          (change_screen_return),
        (try_end),
        
        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),
        
        (str_store_string,s10,"@You are at {s2}."),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_fort),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the fort."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the fort."),
          (else_try),
            (str_store_string,s11,"@ The townsfolk here have declared their independence."),
          (try_end),
        (try_end),

        (assign,"$castle_undefended",0),
        (party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq,":castle_garrison_size",0),
          (assign,"$castle_undefended",1),
        (try_end),
        ],
        
    [
    ("fort_inspect", [
          (party_slot_eq,"$current_town", slot_party_type, spt_fort),
          (this_or_next|ge, "$g_encountered_party_relation", 0),
          (eq,"$castle_undefended",1),
          ],
       "Take a walk around the fort.",
       [
           #(assign, "$talk_context", tc_town_talk),
           
           (assign, "$talk_context", 0),
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             # (party_get_slot, ":fort_scene", "$current_town", slot_town_center),
			 
			 (call_script, "script_setup_fort_scene"),
			 # (assign, ":fort_scene", "scn_fort"),
			 (assign, ":fort_scene", reg1),
			 
             (modify_visitors_at_site, ":fort_scene"),
             (reset_visitors),
             (assign, "$g_mt_mode", tcm_default),
             #(store_faction_of_party, ":town_faction","$current_town"),
             
             # Setup merchants and guard captain
			 # Lumos: I don't want to make new merchants, so I'll just use some old ones instead.
			 ########### NEW v3.7 - pull merchants from nearest town
             (call_script, "script_ee_get_closest_town", "$current_town"),
			 (assign, ":nearest_town", reg0),
			 
             (party_get_slot, ":spawned_troop", ":nearest_town", slot_town_merchant),
             (set_visitor, 8, ":spawned_troop"),
             #(add_troop_to_site,":spawned_troop","scn_fort",4),
             (party_get_slot, ":spawned_troop", ":nearest_town", slot_town_armorer),
             (set_visitor, 9, ":spawned_troop"),
             (party_get_slot, ":spawned_troop", ":nearest_town", slot_town_weaponsmith),
             (set_visitor, 10, ":spawned_troop"),
             # (party_get_slot, ":spawned_troop", "p_fort", slot_town_elder),
             # (set_visitor, 11, ":spawned_troop"),
			 (set_visitor, 11, "trp_fort_captain"),
             (party_get_slot, ":spawned_troop", ":nearest_town", slot_town_horse_merchant),
             (set_visitor, 12, ":spawned_troop"),
             #######################################################
             # Spawn some animated horses at the stables if we have a horse merchant
             (entry_point_get_position, pos1, 13),
             (set_spawn_position, pos1),
             (spawn_horse,"itm_steppe_horse",0),		# this seems to cause a horrible crash anywhere I use it sadly
             (assign, ":horse_agent_id", reg0),       # spawn_agent does as well, I don't know why
             (agent_set_position, reg0, pos1),
             (agent_set_stand_animation, ":horse_agent_id", "anim_horse_stand"),
             (agent_set_walk_forward_animation, ":horse_agent_id", "anim_horse_pace_1"),
             (agent_set_animation, ":horse_agent_id", "anim_horse_stand"),
             (agent_set_animation_progress, ":horse_agent_id", 10),
             
             # Setup peasant walkers
             (try_for_range, ":visiterator", 32, 40),
               (store_random_in_range, ":sex", 0, 100),
               (try_begin),
                 (ge, ":sex", 50),
                 (set_visitor, ":visiterator", "trp_village_walker_1",),
               (else_try),
                 (set_visitor, ":visiterator", "trp_village_walker_2",),
               (try_end),
             (try_end),
             
             # Setup guards based on best type of archer/melee troops currently in garrison
	         (assign, ":highest_archer_lvl", 0),
	         (assign, ":archer_id", 0),
	         (assign, ":highest_infantry_lvl", 0),
	         (assign, ":infantry_id", 0),
	         (assign, ":highest_cavalry_lvl", 0),
	         (assign, ":cavalry_id", 0),
	
			 #(party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
	         (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
	         (try_for_range, ":troop_iterator", 0, ":num_stacks"),
	           (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
	           (neg|troop_is_hero, ":cur_troop_id"),
	           (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
	           (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
	           (val_sub, ":stack_size", ":num_wounded"),
	           (gt, ":stack_size", 0),
		       (store_character_level, ":cur_level", ":cur_troop_id"),
	           (try_begin),
		         (troop_is_guarantee_ranged, ":cur_troop_id"),
		         (gt, ":cur_level", ":highest_archer_lvl"),
		         (assign, ":highest_archer_lvl", ":cur_level"),
		         (assign, ":archer_id", ":cur_troop_id"),
		         (party_stack_get_troop_dna,":archer_dna","$g_encountered_party",":troop_iterator"),
		       (else_try),
		         (gt, ":cur_level", ":highest_infantry_lvl"),
		         (assign, ":highest_infantry_lvl", ":cur_level"),
		         (assign, ":infantry_id", ":cur_troop_id"),
		         (party_stack_get_troop_dna,":infantry_dna","$g_encountered_party",":troop_iterator"),
		       (try_end),
		       (try_begin),
		         (troop_is_guarantee_horse, ":cur_troop_id"),
		         (gt, ":cur_level", ":highest_cavalry_lvl"),
		         (assign, ":highest_cavalry_lvl", ":cur_level"),
		         (assign, ":cavalry_id", ":cur_troop_id"),
		         (party_stack_get_troop_dna,":cavalry_dna","$g_encountered_party",":troop_iterator"),
		       (try_end),
	         (try_end),
	         
	         # Slots 40-49 are the slots I used for archers and guards inside the fort intented for use in sieges as well
	         (try_begin),
	           (gt, ":archer_id", 0),
	           (try_for_range, ":visiterator", 40, 42),
	             (store_random_in_range, ":walker_dna", 0, 1000000),
	             (set_visitor, ":visiterator", ":archer_id", ":walker_dna"),
	           (try_end),
	           (try_for_range, ":visiterator", 48, 50),
	             (store_random_in_range, ":walker_dna", 0, 1000000),
	             (set_visitor, ":visiterator", ":archer_id", ":walker_dna"),
	           (try_end),
	         (try_end),
	         (try_begin),
	           (gt, ":infantry_id", 0),
	           (try_for_range, ":visiterator", 24, 30),	#I used slots 24-29 for stationary guard posts during visits
	             (store_random_in_range, ":walker_dna", 0, 1000000),
	             (set_visitor, ":visiterator", ":infantry_id", ":walker_dna"),
	           (try_end),
	           
	           # these are 'patrols' that will path through specific points in the scene
	           (call_script, "script_set_walker_to_type", "trp_fort_rider", ":cavalry_id"),
	           (try_begin),
	             (gt, ":cavalry_id", 0),
	             (set_visitor, 20, ":cavalry_id", ":cavalry_dna"),	    # guard that patrols the perimeter
	             #(set_visitor, 20, "trp_fort_rider", ":cavalry_dna"),	    # TODO: Go back to using this type now that the patrol is working properly
	           (try_end),
	           (call_script, "script_set_walker_to_type", "trp_ee_watchman", ":infantry_id"),
	           (set_visitor, 30, "trp_ee_watchman", ":archer_dna"),		# guard that patrols the middle walkway
	           (set_visitor, 42, "trp_ee_watchman", ":infantry_dna"),	# guards patrolling the front walls
	           (set_visitor, 44, "trp_ee_watchman", ":walker_dna"),
	         (try_end),

             (call_script, "script_init_town_walkers"),
             (set_jump_mission,"mt_fort_visit"),
#             (assign, ":override_state", af_override_horse),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
#              (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
             (try_begin),
               (eq, "$town_entered", 0),
               (assign, "$town_entered", 1),
               (eq, "$town_nighttime", 0),
             (try_end),
               (set_jump_entry, 1),
             (jump_to_scene, ":fort_scene"),
             (change_screen_mission),
           (try_end),
        ], "To the fort square."),
      
      ("trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_fort)
        ],
         "Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_fort_trade"),  ########### NEW v3.7
           (try_end),
          ]),

      # ("fort_center_manage",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
                      # (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),]
       # ,"Manage the fort.",
       # [
           # (assign, "$g_next_menu", "mnu_fort"),
           # (jump_to_menu, "mnu_center_manage"),
        # ]),
        
     ("fort_station_troops",
      [
          (party_slot_eq,"$current_town",slot_town_lord, "trp_player"),
       ],
         "Station a garrison here...",
         [
           (change_screen_exchange_members,0), # Do not move leader
          ]),

		# Lumos: A little handy feature. May improve it later on.
      ("fort_rename", [],
         "Rename this fort. (To your current name)",
         [
           (str_store_troop_name, s1, "trp_player"),
           (str_store_string, s2, "@{s1}'s Fort"),
		   (party_set_name, "$g_encountered_party", s2),
          ]),

      ("fort_wait",
       [
#           (party_slot_eq,"$current_town",slot_party_type, spt_castle),
           (this_or_next|ge, "$g_encountered_party_relation", 0),
           (eq,"$castle_undefended",1),
           (assign, ":can_rest", 1),
           (str_clear, s1),
           (try_begin),
             (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
             (party_get_num_companions, ":num_men", "p_main_party"),
             (store_div, reg1, ":num_men", 4),
             (val_add, reg1, 1),
             (str_store_string, s1, "@ ({reg1} denars per night)"),
             (store_troop_gold, ":gold", "trp_player"),
             (lt, ":gold", reg1),
             (assign, ":can_rest", 0),
           (try_end),
           (eq, ":can_rest", 1),
##           (eq, "$g_defending_against_siege", 0),
        ],
         "Wait here for some time{s1}.",
         [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_town_visit_after_rest", 1),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),

           (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
           (change_screen_return),
          ]),
          
      # Do NOT add or remove any menu items before this point or it will screw up the passageways
      # if you want to remove an item above, make the condition block fail so it won't show up ever
      # unless you want to edit the scene passageways to reflect the new menu item order
      # You can, of course, change or rearrange the ones above, just not remove or add new ones
      ("visit_crows_nest_1", #6
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit tower.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 15),
           (set_fixed_point_multiplier, 100),
           (position_get_x, ":pos_x", pos1),
           (val_add, ":pos_x", -110),
           (position_set_x, pos1, ":pos_x"),
           (agent_set_position, ":player_agent", pos1),	
          ], "Go inside."),
          
      ("visit_outside_1", #7
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit walkway.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 16),
           (agent_set_position, ":player_agent", pos1),	
          ], "Back outside."),  
          
      ("visit_crows_nest_2", #8
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit tower.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 17),
           (set_fixed_point_multiplier, 100),
           (position_get_x, ":pos_x", pos1),
           (val_add, ":pos_x", -110),
           (position_set_x, pos1, ":pos_x"),
           (agent_set_position, ":player_agent", pos1),	
          ], "Go inside."),
      
      ("visit_outside_2", #9
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit walkway.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 18),
           (agent_set_position, ":player_agent", pos1),	
          ], "Back outside."),  
          
      ("visit_crows_nest_3", #10
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit tower.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 15),
           (set_fixed_point_multiplier, 100),
           (position_get_x, ":pos_x", pos1),
           (val_add, ":pos_x", 110),
           (position_set_x, pos1, ":pos_x"),
           (agent_set_position, ":player_agent", pos1),	
          ], "Go inside."),
          
      ("visit_crows_nest_4", #11
       [
           (disable_menu_option),
           (eq, 1, 0),
        ],
         "Visit tower.",
         [
           (get_player_agent_no, ":player_agent"),
           (entry_point_get_position, pos1, 17),
           (set_fixed_point_multiplier, 100),
           (position_get_x, ":pos_x", pos1),
           (val_add, ":pos_x", 110),
           (position_set_x, pos1, ":pos_x"),
           (agent_set_position, ":player_agent", pos1),	
          ], "Go inside."),
      
      # Add any custom menu items you want AFTER this point otherwise the passages will get messed up
		  
      ("fort_leave",[],"Leave...",[
            (assign, "$g_permitted_to_center",0),
            (change_screen_return,0),
          ],"Leave Area."),  
		  
      ]
  ),
  
############# NEW v3.7 - fort trade
   ("fort_trade",0,
    "You head towards the merchants.",
    "none",
    [
	],
################
    [
      ("trade_with_arms_merchant",
	  [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
		(party_slot_ge, ":nearest_town", slot_town_weaponsmith, 1)
	  ],
      "Trade with the arms merchant.",
      [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
        (party_get_slot, ":merchant_troop", ":nearest_town", slot_town_weaponsmith),
        (change_screen_trade, ":merchant_troop"),
      ]),
################
      ("trade_with_armorer",
	  [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
		(party_slot_ge, ":nearest_town", slot_town_armorer, 1)
	  ],
      "Trade with the armorer.",
      [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
        (party_get_slot, ":merchant_troop", ":nearest_town", slot_town_armorer),
        (change_screen_trade, ":merchant_troop"),
      ]),
################
      ("trade_with_horse_merchant",
	  [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
		(party_slot_ge, ":nearest_town", slot_town_horse_merchant, 1)
	  ],
      "Trade with the horse merchant.",
      [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
        (party_get_slot, ":merchant_troop", ":nearest_town", slot_town_horse_merchant),
        (change_screen_trade, ":merchant_troop"),
      ]),
################
      ("trade_with_goods_merchant",
	  [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
		(party_slot_ge, ":nearest_town", slot_town_merchant, 1)
	  ],
      "Trade with the goods merchant.",
      [
        (call_script, "script_ee_get_closest_town", "$current_town"),
	    (assign, ":nearest_town", reg0),
        (party_get_slot, ":merchant_troop", ":nearest_town", slot_town_merchant),
        (change_screen_trade, ":merchant_troop"),
      ]),
################
      ("back_to_fort_menu",[], "Head back.",
       [
           (jump_to_menu, "mnu_fort"),
        ]),
    ]
  ),
#########################
#-## Outposts end
]
#########################

from util_wrappers import *
from util_common import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "game_menus"
        orig_game_menus = var_set[var_name_1]
        
        
        #swy--insert new menu option in the camp menu as its third option!
        try:
          find_i = list_find_first_match_i(orig_game_menus, "camp_action")
          GameMenuWrapper(orig_game_menus[find_i]).GetMenuOptions().insert(3-1,outkit_camp_menu[0])

        except:
          import sys
          print "Injection failed:", sys.exc_info()[1]
          raise
        
        
        #swy--additional game menus, inserted at the end!
        orig_game_menus.extend(game_menus)
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)