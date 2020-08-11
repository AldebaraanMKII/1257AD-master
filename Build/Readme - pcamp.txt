Features:

  * Leave a companion to command a permanent camp near a center for a small sum.

    - Garrison size is limited to player party size + commander skill bonus.
    - Prisoner count is limited based on commander skill + garrison troop count.
    - Troops draw full wage, but are assumed to buy their own food from locals.
    - If unpaid, troops desert; this can't be countered by any morale boosts.
    - Can store items, which increases bandit attraction.

  * Camps can and will be attacked by hostile parties.

    - All stored items are lost if camp is destroyed.
    - If defeated, companion will return to party unless imprisoned by a lord.
    - Camp will join in the battle if player is attacked right on top of it.
    - Player will stop resting and join battle if current camp is attacked.

  * Miscellaneous features.

    - Camp can auto-ransom prisoners when there is a broker in the nearest town.

Configuration:

  There are some options at the start of pcamp_constants.py. The absolute maximum
  number of camps is determined by the number of player_camp_chest_* troops before
  player_camp_chest_end in pcamp_troops.py

  When merging with other mods, check that spt_player_type doesn't conflict with
  any other new spt_* constant.

  If building module fails with messages about pt_player_camp, add this to
  ID_party_templates.py and then build module _twice_ before using:

    pt_player_camp=0

Bugs:

  * Camps are ordinary parties told to stay put, but they technically can still move
    if AI decides to for some reason. Haven't seen this for a while after some fixes.

  * Camp interactions leave spurious battle marks that can be seen with tracking
    skill after disbanding the camp.

  * AI is unaware that camps will always join in on the battle and can be easily
    tricked into attacking against the odds.
