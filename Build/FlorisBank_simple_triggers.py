from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *

# Manualy all lines under the `simple_triggers` into the bottom of the module_simple_triggers at the bottom of the file
simple_triggers=[
########################################################################################################################
#  FLORIS BANK START                                                                                               #
########################################################################################################################
    (1,                                                                                 
    [    
        (try_for_range, ":town_no", towns_begin, towns_end),                            #    Floris Moneylenders // Not paying debts has consequences
            (party_get_slot, ":debt", ":town_no", slot_town_bank_debt),
            (gt, ":debt", 0),                                                            #    If a debt exists, a deadline exists
            (party_get_slot, ":deadline", ":town_no", slot_town_bank_deadline),
            (store_current_hours, ":date"),
            (ge, ":date", ":deadline"),
            (call_script, "script_change_player_relation_with_center", ":town_no", -5, 0xff3333),
            (try_begin),
                (lt, ":debt", 100000),
                (val_mul, ":debt", 14),
                (val_div, ":debt", 10),
                (try_begin),
                    (gt, ":debt", 100000),                                                #Debt doesnt get higher than 100000 denars
                    (assign, ":debt", 100000),
                (try_end),
                (val_add, ":deadline", 24*14),
                (party_set_slot, ":town_no", slot_town_bank_debt, ":debt"),
                (party_set_slot, ":town_no", slot_town_bank_deadline, ":deadline"),
                (str_store_party_name, s1, ":town_no"),
                (display_message, "@You missed the deadline to pay back your debts in {s1}. They now grow at an interest of 50%."),
            (else_try),
                (assign, ":debt", 100000),                                                #If debt = 100000 denars, then additionally to -5 relation with town, you get -1 relation with Faction.
                (val_add, ":deadline", 24*14),
                (party_set_slot, ":town_no", slot_town_bank_debt, ":debt"),
                (party_set_slot, ":town_no", slot_town_bank_deadline, ":deadline"),
                (store_faction_of_party, ":faction_no", ":town_no"),
                (call_script, "script_change_player_relation_with_faction_ex", ":faction_no", -1),
                (str_store_party_name, s1, ":town_no"),
                (display_message, "@Your debt in {s1} is now so high that the King himself has taken notice. He has frozen your debt, but is displeased with the situation.", 0xff3333),
            (try_end),
        (try_end),         
        
    ]),
    
########################################################################################################################
#  Population increase
########################################################################################################################
   
    (24*14,
    [
        (try_for_range, ":town_no", centers_begin, centers_end),                            #    Floris Moneylenders // Not paying debts has consequences
            (neg|party_slot_eq, ":town_no", slot_party_type, spt_castle),      ### no castle
            (party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),  #    Floris    //    Adjust Population Depending on Prosperity
            (party_get_slot, ":population", ":town_no", slot_center_population),
            (assign,":change",0),
            (try_begin),
                (ge, ":prosperity", 60),
                (store_sub, ":change", ":prosperity",60),
                (val_div, ":change", 5),
                (val_add, ":change", 3),
            (else_try),
                (le, ":prosperity", 40),
                (store_sub, ":change", ":prosperity", 40),                              # Fixed typo
                (val_div, ":change", 5),
                (val_sub, ":change", 3),
            (try_end),
            (store_div,":base",":population",100),                                        #    Base population change is 1% of pop
            (val_mul,":change",":base"),                
            (val_add,":population", ":change"),            
            (try_begin),
              (party_slot_eq, ":town_no", slot_party_type, spt_town),
              (try_begin),
                (gt, ":population", 100000),
                  (assign, ":population", 100000),
                  (party_set_slot, ":town_no", slot_center_population, ":population"),
              (else_try),
                (lt, ":population", 5000),
                  (assign, ":population", 5000),
                  (party_set_slot, ":town_no", slot_center_population, ":population"),
              (else_try),
                (party_set_slot, ":town_no", slot_center_population, ":population"),
              (try_end),
            (else_try),
              (party_slot_eq, ":town_no", slot_party_type, spt_village),
              (try_begin),
                (gt, ":population", 10000),
                  (assign, ":population", 10000),
                  (party_set_slot, ":town_no", slot_center_population, ":population"),
              (else_try),
                (lt, ":population", 500),
                  (assign, ":population", 500),
                  (party_set_slot, ":town_no", slot_center_population, ":population"),
              (else_try),
                (party_set_slot, ":town_no", slot_center_population, ":population"),
              (try_end),
            (try_end),
        (try_end),    
    
        (try_for_range, ":town_no", centers_begin, centers_end),                            #    Floris Moneylenders // Not paying debts has consequences
            (neg|party_slot_eq, ":town_no", slot_party_type, spt_castle),                         #    Floris    //    Calculating Land Demand and Consequences for supply, pricing and renting
            (party_get_slot, ":population", ":town_no", slot_center_population),
            (party_get_slot, ":land_town", ":town_no", slot_town_acres),
            (party_get_slot, ":land_player", ":town_no", slot_town_player_acres),
            (party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
            (store_sub, ":revenue", ":prosperity", 50),
            (val_add, ":revenue", 100),
            (try_begin),
                (store_div, ":acres_needed", ":population", 200),                        #    200 People warrant 1 acre of cultivated land
                (store_add, ":total_land", ":land_town", ":land_player"),
                (store_sub, ":surplus", ":total_land", ":acres_needed"),
                
                (try_begin),                                                            #    AI Consequences
                    (lt, ":total_land", ":acres_needed"),
                    (store_sub, ":new_acres", ":acres_needed", ":total_land"),
                    (val_add, ":land_town", ":new_acres"),
                    (party_set_slot, ":town_no", slot_town_acres, ":land_town"),
                (else_try),
                    (ge, ":surplus", 20),
                    (ge, ":land_town", 10),
                    (val_sub, ":land_town", 10),                                        #    Changed from 2 / Faster rebalancing in case of player screw up
                    (party_set_slot, ":town_no", slot_town_acres, ":land_town"),
                (try_end),
                
                (try_begin),
                    (gt, ":land_player", 0),                                                #     New Fix / Before it was possible for the towns land to cause the player a deficit
                    (try_begin),                                                            #    Player Consequences
                        (le, ":total_land", ":acres_needed"),
                        (val_mul, ":land_player", ":revenue"),                                        
                        (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                    (else_try),
                        (store_mul, ":penalty", ":surplus", -1),
                        (val_add, ":penalty", ":revenue"),
                        (try_begin),
                            (ge, ":penalty", 85),
                            (val_mul, ":land_player", ":penalty"),
                            (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                        (else_try),
                            (store_sub, ":non_rented", ":surplus", 15),
                            (val_sub, ":land_player", ":non_rented"),
                            (try_begin),                                                    #    Safety check // No penalty on rent should turn rent negative.
                                (lt, ":penalty", 0),
                                (assign, ":penalty", 0),
                            (try_end),
                            (val_mul, ":land_player", ":penalty"),
                            (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                            (val_mul, ":non_rented", -50),
                            (party_set_slot, ":town_no", slot_town_bank_upkeep, ":non_rented"),
                        (try_end),
                    (try_end),
                    (party_get_slot, ":assets", ":town_no", slot_town_bank_assets),                        #    Adding/Subtracting profits/losses
                    (party_get_slot, ":rent", ":town_no", slot_town_bank_rent),
                    (party_get_slot, ":upkeep", ":town_no", slot_town_bank_upkeep),
                    (val_add, ":assets", ":rent"),
                    (val_add, ":assets", ":upkeep"),
                    (party_set_slot, ":town_no", slot_town_bank_assets, ":assets"),    
                (try_end),
                
            (try_end),
        
        (try_end),
    
    ]),    
    

#LAZERAS MODIFIED  {BANK OF CALRADIA}        #    Floris Overhaul

  (24 * 7,
   [
    (this_or_next|neq, "$g_infinite_camping", 1),
    (eq, "$freelancer_state", 1),  ####### NEW v1.1 - bugfix for player not receiving rents from land when enlisted
    (assign, ":end", centers_end),
    (try_for_range, ":center_no", centers_begin, ":end"),                
      (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle), 
      (this_or_next|party_slot_ge, ":center_no", slot_town_player_acres, 1),
      (this_or_next|party_slot_ge, ":center_no", slot_town_bank_assets, 1),
      (party_slot_ge, ":center_no",slot_town_bank_debt, 1),
        (assign, ":end", centers_begin), #break
    (try_end),
    (eq, ":end", centers_begin), #ONLY DISPLAY BANK PRESENTATION IF THE PLAYER IS USING BANK
    
    (try_begin),  #### Player receives money directly if option is turned on
      (eq, "$g_misc_floris_bank_receive_directly", 1),  #### Enabled
      (try_for_range, ":center_no", centers_begin, centers_end),  
        (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle), 
        (party_slot_ge, ":center_no", slot_town_bank_assets, 1),
          (party_get_slot, reg15, ":center_no", slot_town_bank_assets),
          (troop_add_gold, "trp_player", reg15),
          (party_set_slot, ":center_no", slot_town_bank_assets, 0),
          (str_store_party_name_link, s1, ":center_no"),
          (display_message, "@You got {reg15} denars from the lands you own in {s1}."),
      (try_end),
    (try_end),
    
	############ Deposit interests
    (try_for_range, ":center_no", towns_begin, towns_end),  
      (party_slot_ge, ":center_no", slot_town_bank_deposit_assets, 1),
        (party_get_slot, ":assets", ":center_no", slot_town_bank_deposit_assets),
        (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
        (store_div, ":interest_rate", ":prosperity", 20), #### 1% more interest for every 20 prosperity
        (val_div, ":assets", 100),                                                        
        (store_mul, reg16, ":assets", ":interest_rate"),                                                        
        (troop_add_gold, "trp_player", reg16),
        (str_store_party_name_link, s2, ":center_no"),
        (display_message, "@You got {reg16} denars from the interest in your deposits in {s2}."),
    (try_end),
    (start_presentation, "prsnt_bank_quickview"),
    ]),
#LAZERAS MODIFIED  {BANK OF CALRADIA}
########################################################################################################################
#  FLORIS BANK END                                                                                                   #
########################################################################################################################
]



from util_common import *
def modmerge(var_set):
    try:
        from modmerger_options import module_sys_info
        version = module_sys_info["version"]
    except:
        version = 1158 # version not specified.  assume latest warband at this time

    try:
        var_name_1 = "simple_triggers"
        orig_simple_triggers = var_set[var_name_1]
        
        add_objects(orig_simple_triggers, simple_triggers, False)
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)