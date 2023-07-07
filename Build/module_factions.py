# -*- coding: utf-8 -*-
from header_factions import *
# from compiler import *


####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################
# 249f6c

default_kingdom_relations = [("outlaws",-0.3),("peasant_rebels", -0.5),("deserters", -0.5),("mountain_bandits", -0.3),("forest_bandits", -0.3),("escaped_prisoners_faction", -0.3)]
factions = [
  ("no_faction", "No Faction",0, 0.9, [], []),
  ("commoners", "Commoners",0, 0.1,[("player_faction",0.1)], [],0xFFFFFF),
  ("outlaws", "Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xFF00FF),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral", "Neutral Parties",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents", "Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], [],0xFFFFFF),
  ("merchants", "Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], [],0xFFFFFF),

  ("culture_finnish",  "Finnish", 0, 0.9, [], []),  #
  ("culture_mazovian",  "Mazovian", 0, 0.9, [], []), #
  ("culture_serbian",  "Serbian", 0, 0.9, [], []), #kingdom_29
  ("culture_welsh",  "Welsh", 0, 0.9, [], []), #kingdom_37
  ("culture_teutonic",  "Teutonic", 0, 0.9, [], []), #kingdom_1
  ("culture_balkan",  "Balkan", 0, 0.9, [], []), #kingdom_30
  ("culture_rus",  "Rus", 0, 0.9, [], []), #kingdom_15, kingdom_8
  ("culture_nordic",  "Nordic", 0, 0.9, [], []), # kingdom_11, kingdom_14, kingdom_4
  ("culture_baltic",  "Baltic", 0, 0.9, [], []), #kingdom_2, kingdom_33, kingdom_34, kingdom_35, kingdom_36
  ("culture_marinid",  "Marinid", 0, 0.9, [], []), #kingdom_31 #kingdom_28
  ("culture_mamluke",  "Mamluke", 0, 0.9, [], []), #kingdom_25
  ("culture_byzantium",  "Byzantium", 0, 0.9, [], []), #kingdom_22, kingdom_26
  ("culture_iberian",  "Iberian", 0, 0.9, [], []), #kingdom_16, kingdom_17, kingdom_18, kingdom_21, kingdom_32,
  ("culture_italian",  "Italian", 0, 0.9, [], []), #papacy, kingdom_24, kingdom_38, kingdom_39, kingdom_40, kingdom_41
  ("culture_andalus",  "Andalus", 0, 0.9, [], []), #kingdom_20
  ("culture_gaelic",  "Gaelic", 0, 0.9, [], []),  #kingdom_13
  ("culture_anatolian_christian",  "Armenian", 0, 0.9, [], []),  
  ("culture_anatolian",  "Anatolia", 0, 0.9, [], []),
  ("culture_scotish",  "Scottish", 0, 0.9, [], []), #kingdom_12
  ("culture_western",  "Western European", 0, 0.9, [], []), #kingdom_5, kingdom_6, kingdom_7, kingdom_9, kingdom_10, kingdom_19, kingdom_42, kingdom_23
  ("culture_mongol",  "Mongol", 0, 0.9, [], []), #kingdom_3, kingdom_27
############## NEW v1.8
  ("culture_templar",  "Templar", 0, 0.9, [], []), 
  ("culture_hospitaller",  "Hospitaller", 0, 0.9, [], []), 
############################
  
############## NEW v2.1
  ("culture_antioch",  "Antioch", 0, 0.9, [], []), 
  ("culture_tripoli",  "Tripoli", 0, 0.9, [], []), 
  ("culture_ibelin",  "Ibelin", 0, 0.9, [], []), 
  ("culture_jerusalem",  "Jerusalem", 0, 0.9, [], []),
  # ("culture_hre",  "Germanic", 0, 0.9, [], []),  
############################

############## NEW v3.3
  ("culture_crusader",  "Crusader", 0, 0.9, [], []), 
  ("culture_cuman",  "Cuman", 0, 0.9, [], []), 
############################

############## NEW v3.10
  ("culture_english",  "English", 0, 0.9, [], []), 
  ("culture_french",  "French", 0, 0.9, [], []), 
  ("culture_hungarian",  "Hungarian", 0, 0.9, [], []), 
  ("culture_polish",  "Polish", 0, 0.9, [], []), 
############################
  
  ("culture_player",  "Custom", 0, 0.9, [], []), #####player faction culture needed to make custom troops appear in villages, lances or not
  
  ("player_faction", "Player",0, 0.9, [], [], 0x00FFFF),
  ("player_supporters_faction", "Player's Kingdom",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x00FFFF), #changed name so that can tell difference if shows up on map

  ("kingdom_1",  "Ordo Teutonicus",
  #"Teutonic Order (Livonia and Prussia)",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_8",-0.2),
      ("kingdom_14",0.10),
      ("kingdom_4",0.10),
      ("kingdom_6",0.50),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0xe9e9e9
  ),

  ("kingdom_2",  "Regnum Litus",
  #"Kingdom of Lithuania",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_33", 0.5),
    ],
    [],
    0xbadeb2
  ),

  ("kingdom_3",  "Altan Ordyn Uls",
  #"Golden Horde",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("kingdom_2",0.1),
      ("kingdom_8",0.2),
      ("kingdom_7",-1.0),
      ("kingdom_5",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xa33e32
  ),
  ("kingdom_4", "Regnum Daniae",
  #  "Kingdom of Denmark",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.10),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x9b1a1a
  ),
  ("kingdom_5", "Regnum Poloniae",
  # "Polish Principalities",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_7",0.10),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
      [],
      0xff0000
  ),
  ("kingdom_6",  "Sacrum Imperium Romanum",
  #"Holy Roman Empire",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.50),
      ("kingdom_38",0.50),
      ("kingdom_41",1.0),
      ("kingdom_42",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0xffcc00
  ),
  ("kingdom_7",  "Regnum Hungariae",
  #"Kingdom of Hungary",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_5",0.10),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x289327
  ),

  ("kingdom_8",  "Novgorod Weliki",
  #"Novgorod Republic",
    0, 0.9,
    [
      ("kingdom_1",-0.20),
      ("kingdom_3",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0x9e0b6f
  ),
  ("kingdom_9",  "Regnum Angliae",
  #"Kingdom of England",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_37", -1),
    ], [],
    0x931124
  ),
  ("kingdom_10",  "Regnum Franciae",
  #"Kingdom of France",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    # 0x002395
    0x006de2
  ),
  ("kingdom_11",  "Kongeriket Norge",
  #"Kingdom of Norway",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_13",-0.2),
      ("kingdom_12",-0.2),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0x6669d6 
  ),
  ("kingdom_12",  "Regnum Scotiae",
  #"Kingdom of Scotland",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x22D8A7
  ),
  ("kingdom_13",  "Scotia Maior",
  #"Gaelic Kingdoms",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ], [],
    0x77b322
  ),
  ("kingdom_14",  "Konungariket Sverige",
  #"Kingdom of Sweden",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_1",0.1),
      ("kingdom_8",-0.2),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x3254b5
  ),

  ("kingdom_15",  "Regnum Galiciae et Lodomeriae",
  #"Kingdom of Halych-Volhynia",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xece874
  ),

  ("kingdom_16",  "Regnum Portugaliae",
  #"Kingdom of Portugal",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_20", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    # 0x003399
    0x27837a
  ),
  ("kingdom_17",  "Corona Aragonae",
  #"Crown of Aragon",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x07b233
  ),

  ("kingdom_18",  "Corona Castiliae",
  #"Crown of Castile",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_20", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xd85ac4
  ),
  
  ("kingdom_19",  "Regnum Navarrae",
  #"Kingdom of Navarra",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xf7f497
  ),

  ("kingdom_20",  "Imarat al Nasri",
  #"Emirate of Granada",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("kingdom_16", -40),
      ("kingdom_18", -40),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xabc904
  ),

    ("papacy",  "Patrimonium Sancti Petri",
    0, 0.9,
    [
      ("kingdom_40", 1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),      
    ],
    [],
    0xfff17a
  ),
  
  ("kingdom_22",  "Basileia ton Rhomaion",
  #"Roman Empire of Nicaea",
    0, 0.9,
    [
      ("kingdom_26",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x760d0d
  ),

  ("kingdom_23",  "Regnum Hierosolymitanum",
  #"Crusader States",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_25",-1.0),
      ("kingdom_27",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0xf3efb8
  ),

  ("kingdom_24",  "Regnum Siciliae",
  #"Kingdom of Sicily",
    0, 0.9,
    [
      ("papacy",0.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0x799cb5
  ),

  ("kingdom_25",  "Sultanat al Mamalik",
  #"Mamluk Sultanate",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("kingdom_23",-1.0),
      ("kingdom_27",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xebe800
  ),

  ("kingdom_26",  "Imperium Romaniae",
  #"Latin Empire",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_22",-1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xb26248
  ),


  ("kingdom_27",  "Ilkhanate",
  #"Il-khanate",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("kingdom_25",-1.0),
      ("kingdom_23",0.1),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xe19004
  ),

  ("kingdom_28",  "Sultanat al Hafsi",
  #"Hafsid Dynasty",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xa48460
  ),

  ("kingdom_29",  "Kraljevstvo Srbsko",
  #"Kingdom of Serbia",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xb38263
  ),

  ("kingdom_30",  "Balgarsko Tsarstvo",
  #"Kingdom of Bulgaria",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x76a296
  ),

  ("kingdom_31",  "Sultanat al Marini",
  #"Marinid Dynasty",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xc1272d
  ),
  
  ("kingdom_32",  "Repubblica di Venezia",
  #"Republic of Venice",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xc1172d
  ),  
  
  ("kingdom_33",  "Jotvingiai",
  #"Jotvingians",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_2", 0.5),
    ],
    [],
    0x3e7583
  ),
  
  ("kingdom_34",  "Pruteni",
  #"Prussians",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_2", 0.5),
    ],
    [],
    0x65c0d7
  ),
  
  
  ("kingdom_35",  "Kursi",
  #"Curonians",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_2", 0.5),
    ],
    [],
    0x3e7583
  ),
  
    ("kingdom_36",  "Zemaiciai",
  #"Samagotians",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_2", 0.5),
    ],
    [],
    0x529cae
  ),


      ("kingdom_37",  "Cymry",
  #"Welsh",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("kingdom_9", -1.0),
    ],
    [],
    0x00dc00
  ),  
  
  ("kingdom_38",  "Respublica Ianuensis",
  #"Genoa",
    0, 0.9,
    [
      ("crusade", -0.5),
      ("kingdom_39",-0.5),
      ("kingdom_6",0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xe1900a
  ),
  
    ("kingdom_39",  "Respublica Pisarum",
    #"Pisa",
    0, 0.9,
    [
      ("kingdom_38", -0.5),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0xebe800
  ),
  
    ("kingdom_40",  "Comuni Guelfi",
    #"Guelphs",
    0, 0.9,
    [
      ("papacy",0.0),
      ("kingdom_41",-0.8),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05)
    ],
    [],
    0x3254e5
  ),
  
    ("kingdom_41",  "Comuni Ghibellini",
    #"Ghibellines",
    0, 0.9,
    [
      ("kingdom_40",-0.80),
      ("kingdom_6",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0x9e026a
  ),
  
    ("kingdom_42",  "České Království",
    #"Bohemia",
    0, 0.9,
    [
      ("kingdom_6",1.0),
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
    ],
    [],
    0xe8e8e8
  ),
  
################################ NEW v2.1 - factions for the civil war - if editing this make sure that slot_faction_truce_days_with_factions_begin has enough slots
 ("enhanced_kingdom_1", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_2", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_3", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_4", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_5", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_6", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_7", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_8", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_9", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_10", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_11", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_12", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_13", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_14", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_15", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_16", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_17", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_18", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_19", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_20", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_21", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_22", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_23", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_24", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_25", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_26", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_27", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_28", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_29", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 ("enhanced_kingdom_30", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_31", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_32", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_33", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_34", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_35", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_36", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_37", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_38", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_39", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
 # ("enhanced_kingdom_40", "Random Faction", 0, 0.9,[], [], 0xe8e8e8),
##########################################

  ("kingdoms_end", "{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("manhunters", "Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [],0xFFFFFF),
  ("deserters", "Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0xFF00FF),
  ("mountain_bandits", "Allied Factions", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x006DE2),
  ("forest_bandits", "Friendly Factions", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x00FF00),

  ("undeads", "Enemy Factions", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], [], 0xFF0000),
  ("peasant_rebels", "Peasant Rebels", 0, 1.0,
    [
      ("outlaws",-0.1),
      ("deserters", -0.05),
      ("mountain_bandits", -0.1),
      ("forest_bandits", -0.1),
      ("player_faction",0.0)
    ], 
    []
  , 0xFF00FF),
  
    ("crusade",  "Crusaders",
    0, 0.9,
    [
      ("outlaws",-0.05),
      ("peasant_rebels", -0.1),
      ("deserters", -0.02),
      ("mountain_bandits", -0.05),
      ("forest_bandits", -0.05),
      ("papacy", -0.5),
      ("kingdom_33", -0.5)
    ],
    # [],0xFF00FF),
    [],0xE5E5E5),  ######### NEW v3.5
 
 
 ############### NEW v2.1 - escaped prisoner faction
  ("escaped_prisoners_faction", "Escaped Prisoners", 0, 1.0,
    [
      ("outlaws",-0.2),
      ("deserters", -0.1),
      ("mountain_bandits", -0.2),
      ("forest_bandits", -0.2),
      ("player_faction",-0.2),
      ("peasant_rebels", -0.1),
      ("escaped_prisoners_faction", 1.0),
    ], 
    [], 0x00FFFF),
##############################
  ("end_minor_faction", "Village Idiots",
  0, 0.9,
  [],
  [],
  0xfff17a
  ),
  
###############################
]##############################
###############################
# modmerger_start version=201 type=4


try:
    component_name = "factions"
    var_set = { "factions":factions, "default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
