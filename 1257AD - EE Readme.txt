############################
#### MENU DOCUMENTATION ####
############################

This is documentation for the menus found under Camp > Enhanced Options

The ones that i not mention are obvious so no need to explain them.
Rate = amount of hours


PARTY OPTIONS
Bonus for faction leaders: bonus to party size that kings get (player as king included)
Bonus for marshals: same as above but for marshals
Bonus per castle: bonus to party size that a lord earns for each castle he owns

Garrison reinforcement rate: the amount of hours it takes for a garrison to get a reinforcement round (those are defined in party_templates.txt)
Lord reinforcement rate: same as above but for NPC lords.

Town mercenary companies refill rate: amount of hours it takes for a town mercenary company (not tavern mercs) to refill. This also includes special mercs like cumans and genoese crossbowman, as well as manor knight orders.

NPC lords upgrade their troops like the player does: Once a day a lord will upgrade his troops based on his party's training skill.

Prevent prisoners in fiefs from dying: Once a week a small random percentage of prisoners in fiefs will get removed. This is to simulate they dying in prison, being ransomed/set free. Turn this option on to disable this.

Number of men in party affects morale: If turned on, each men in your party will negate 1 morale (This can be countered in v1.7 thanks to the addition of "Morale penalty based on troops quality v2.0" by kt0).




MERCHANT OPTIONS
The ones with "faction" in their name: Those are the items of the current faction that has control over that town.
So, if for example, the Teutonic order takes Russa from Novgorod and after some days the merchant respawns, and the "armorer (faction) head armor" option is set to 10, the armorer will have rus items + 10 teutonic faction helmets in their item selection.





v2.1 Diplomatic changes (requirements for them to be successful when sending a companion in a mission)

TRADE AGREEMENTS
Before:
15-50 relations with target faction
10-25 honor
5-15 right to rule

After:
5-10 relations with target faction
20-30 honor
10-20 right to rule



NON AGGRESSION PACTS
Before:
5-25 relations with target faction
0-20 honor
5-10 right to rule

After:
5-15 relations with target faction
10-20 honor
10-15 right to rule



DEFENSIVE PACTS
Before:
15-70 relations with target faction
0-50 honor
5-30 right to rule

After:
25-30 relations with target faction
30-50 honor
25-30 right to rule




ALLIANCES
Before:
20-95 relations with target faction
5-75 honor
5-50 right to rule

After:
40-50 relations with target faction
50-70 honor
40-50 right to rule




v2.1 
LORD CREATION SYSTEM 
Every time a faction lord count falls below a threshold (which is determined by the amount of fiefs it has), a new lord for that faction will be created. 
The lord has randomly generated name, equipment (which is dependant on his culture which is also random).
The lord will behave just like a vanilla lord. He will recruit troops, participate in campaigns, be granted fiefs or even become the king when the former dies.
The culture of the lord will depend on the faction they're created for (e.g. England have a small chance of getting Welsh, Scottish, Gaelic, Templar and Hospitaller lords).


If the player factions is using the custom culture, the process is somewhat different.
When switching to the custom culture, a new dialogue will be shown which prompts the player to select a language for his faction. The language determines the name of the lords that are created for the player faction.

The player can also select the language to be "custom". I made this so the player could add names on their own. However he will have to go to the module directory and open "strings.txt" file and search within it for "str_enhanced_name_custom_1".
strings "str_enhanced_name_custom_1" to "str_enhanced_name_custom_30" are tje first name of the lords that will be generated. 
strings "str_enhanced_surname_custom_1" to "str_enhanced_surname_custom_30" are the surnames of the lords. 
You can change the content of these strings to anything you want and they will be used for generating the names if you have set the faction language to custom. 


The equipment of the custom lords is determined by the ones used by the last tier of your CTT troops.
For 1 tier tree = troop A7
For 2 tiers tree = troop B6
For 3 tiers tree = troop C5
But you MUST go to the enhanced menu and select the number of tiers you're using in the "CTT fix" menu, otherwise the lord's equipment will default to a random set from the euro senior knight.
It will also default if the CTT troops above didn't get their equipment set before the lord generation occurs.



LORDS CAN BE KILLED IN BATTLE. 
Kings have a lower chance.

LORDS CAN BE EXECUTED WHILE BEING HELD PRISONER. 
The chance of execution depends on the several factor such as the relation between the prisoner and captor factions, the prisoner personality (asshole lords have a greater chance of going to the block).
The method of execution depends on the chance of execution. The greater the chance, the more brutal the execution will be. 
The player can also execute lords by talking to his constable. After choosing who to execute and by which method, the player will be notified when it happens (it may take up to 3 days). There's severe consequences however (this also applies to AI lords).

LORDS CAN BE ASSASSINATED. 
Every day there's a small chance that a lord will be assassinated. This only happens if they have a rival lord with -30 or less relation. Kings have half that chance. 
Player can also comission a assassination by talking to his constable. The price is dependant on the lord's renown. Player pays 30% of the contract upfront and the rest IF the assassination suceeds.



NEW MISC MENU
Lord battle death chance: Self explanatory. Set it to 0 to disable lord battle deaths. Range is 0|100.
King battle death chance: This one is for kings. Range is 0|100.

Lord assassination chance: Chance that a lord will be assassinated (this is checked once every 3 days for each lord). Set it to 0 to disable AI lord assassinations. Range is 0|1000
King assassination chance: Same as above but for kings. Range is 0|1000

Lord base execution chance: Base chance before other modifers such as relations and personality. Set it to 0 to disable AI executions. Range is 0|100
King execution chance value: Value that gets added or subtracted from the chance of execution when the lord is a faction leader. Range is -100|100
Lord execution chance faction relation divider: The negative relation between the prisoner and captor factions gets divided by this value and added to the chance of execution. Range is 1|100

Random lord creation rate: The amount of time in hours that a faction will be checked to see if their current lord amount is below the lord creation threshold. If yes, a new random lord will be generated for it. Range is 24|720
Random lord creation (minimum lords): If a faction has less than this number of lords, its fief threshold will be ignored and their lord threshold will be assigned to this number. Range is 0|5
Random lord creation (town threshold): The amount of towns that a faction needs to own to increase their lord threshold by 1. Range is 0|5
Random lord creation (castle threshold): Same as above but for castles. Range is 0|5
Random lord creation (village threshold): For villages. Range is 0|5

Crusade daily percent chance: Daily percent chance that a crusade will be created. Range is 0|400 (4 will be a 1% chance in this case, while 2 is 0,5%)

Faction diplomacy rate: Amount of hours it takes for a faction to engage in diplomatic affairs such as declaring war, making peace, trade agreements, etc. Range is 72|720.

Disable player weekly morale loss (0.5%): In vanilla warband (and most of the mods out there), once a week, a script is executed which reduces the player renown by 0.5%. This disable the thing.

Make parties drop their prisoners to a walled fief: If enabled parties like patrols will occasionally drop their prisoners on the walled center they're patrolling.

Civil war chance: The chance that the civil war script will run if its requirements are met. Set it to 0 to disable civil wars. Range is 0|100.
Civil war rate: The amount of time in hours it takes for the civil war trigger to check if there's enough disgruntled lords to start a civil war. Range is 72|720.
Civil war lords needed (percent): Amount of disgruntled lords (30 or less negative relation with faction leader) needed to meet the requirements for the civil war. Range is 0|100.

Player receives landowner money directly: If you played a mod with the Floris moneylender and landowner feature before, you know that you have to go to the fief to collect the accumulated rents.
If this is turned on, the player receives the money directly once a week without needing to go to the fief.









