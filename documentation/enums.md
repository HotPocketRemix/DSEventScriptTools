# Dark Souls Scripting Enums

**ENUM_AI_STATUS_TYPE**

    0. Normal
    1. Recognition
    2. Alert
    3. Battle

**ENUM_BITOP**

    0. Add
    1. Delete
    2. Invert

**ENUM_BOOL**

    0. FALSE
    1. TRUE

**ENUM_BUTTON_NUMBER**

    1. 1 Button
    2. 2 Button
    6. No Button

**ENUM_BUTTON_TYPE**

    0. YES/NO
    1. OK/CANCEL

**ENUM_CATEGORY**

    0. Object
    1. Area
    2. Character

**ENUM_CHARACTER_TYPE**

    0. Survival
    1. White Ghost
    2. Black Ghost
    8. Gray Ghost
    12. Intruder

**ENUM_CHARACTER_UPDATE_RATE**

    -1. Never
    0. Always
    2. Every 2 frames
    5. Every 5 frames


**ENUM_CLASS_TYPE**
 * Note: The translations are not accurate. Instead, they are based on what classes the game actually has corresponding to each value.

    0. Warrior
    1. Knight
    2. Wanderer
    3. Thief
    4. Bandit
    5. Hunter
    6. Sorcerer
    7. Pyromancer
    8. Cleric
    9. Deprived
    20. Temp: Warrior
    21. Temp: Knight
    22. Temp: Sorcerer
    23. Temp: Pyromancer
    24. Chi: Warrior
    25. Chi: Knight
    26. Chi: Sorcerer
    27. Chi: Pyromancer

**ENUM_COMPARISON_TYPE**

    0. ==
    1. !=
    2. >
    3. <
    4. >=
    5. <=

**ENUM_CONDITION_STATE**

    0. FALSE
    1. TRUE

**ENUM_CONTAINED**

    0. Outside
    1. Inside

**ENUM_CUTSCENE_TYPE**

    0. Skippable
    2. Unskippable
    8. Skippable with Fade-out
    10. Unskippable with Fade-out

**ENUM_DAMAGE_TARGET_TYPE**

    1. Character
    2. Map
    3. Character & Map

**ENUM_DEATH_STATUS**

    0. Alive
    1. Dead

**ENUM_ENABLE_STATE**

    0. DISABLE
    1. ENABLE

**ENUM_EVENT_END_TYPE**

    0. END
    1. RESTART

**ENUM_FLAG_TYPE**

    0. Event Flag ID
    1. Event ID
    2. Event ID with Slot Number

**ENUM_INTERPOLATION_STATE**

    0. Interpolated
    1. Not Interpolated

**ENUM_ITEM_TYPE**

    0. Weapon
    1. Armor
    2. Ring
    3. Item

**ENUM_LOGICAL_OPERATION_TYPE**

    0. all ON
    1. all OFF
    2. not all OFF
    3. not all ON

**ENUM_MULTIPLAYER_STATE**

    0. Host
    1. Client
    2. Multiplayer
    3. Singleplayer

**ENUM_NAVIMESH_TYPE**

    1. Solid
    2. Exit
    4. Obstacle
    8. Wall
    32. Wall-touching Floor
    64. Landing Point
    128. Event
    256. Cliff
    512. Wide
    1024. Ladder
    2048. Hole
    4096. Door
    8192. Closed Door

**ENUM_ON_OFF**

    0. OFF
    1. ON

**ENUM_ON_OFF_CHANGE**

    0. OFF
    1. ON
    2. CHANGE

**ENUM_OWN_STATE**

    0. Does not own
    1. Owns

**ENUM_REACTION_ATTRIBUTE**

    48. Survival & Gray
    255. All

**ENUM_REGISTER**

    -7. OR(07)
    -6. OR(06)
    -5. OR(05)
    -4. OR(04)
    -3. OR(03)
    -2. OR(02)
    -1. OR(01)
    0. MAIN
    1. AND(01)
    2. AND(02)
    3. AND(03)
    4. AND(04)
    5. AND(05)
    6. AND(06)
    7. AND(07)

**ENUM_SIGN_TYPE**

    0. Blue Eye Sign
    1. Black Eye Sign
    2. Red Eye Sign
    3. Detection Sign
    4. White Help Sign
    5. Black Help Sign

**ENUM_SITE_TYPE**

    1. Part 1
    2. Part 2
    3. Part 3
    4. Part 4
    5. Part 5
    6. Part 6
    7. Weak Point
    8. Part 7
    9. Part 8

**ENUM_SOUND_TYPE**

    0. a: Evironmental Sound
    1. c: Character Motion
    2. f: Menu SE
    3. o: Object
    4. p: Poly Drama
    5. s: SFX
    6. m: BGM
    7. v: Voice
    8. x: Floor Material Dependence
    9. b: Armor Material Dependence
    10. g: Ghost

**ENUM_STATUE_TYPE**

    0. Petrified
    1. Crystallized

**ENUM_TEAM_TYPE**

    255. Default
    0. Invalid
    1. Survival
    2. White Ghost
    3. Black Ghost
    4. Gray Ghost
    5. Wandering Ghost
    6. Enemy
    7. Strong Enemy
    8. Ally
    9. Hostile Ally
    10. Decoy Enemy
    11. Red Child
    12. Fighting Ally
    13. Intruder

**ENUM_TENDENCY_TYPE**

    0. White Tendency
    1. Black Tendency

**ENUM_TEXT_BANNER_TYPE**

    1. Demon Killed
    2. Death
    3. Revival
    4. Soul Acquisition
    5. Target Killed
    6. Ghost Death
    7. Black Ghost Death
    8. Map Name
    12. Congratulations
    15. Stadium Victory
    16. Stadium Defeat
    17. Stadium Draw

**ENUM_UPDATE_AUTH**

    0. Normal
    4095. Forced

**ENUM_COVENANT_TYPE**
* This is not a real enum in the file, but it's convenient to record these values somewhere.
* It's normally just encoded as integer value between 0 and 20.

    0. None
    1. Way of White
    2. Princess's Guard
    3. Warrior of Sunlight
    4. Darkwraith
    5. Path of the Dragon
    6. Gravelord Servant
    7. Forest Hunter
    8. Darkmoon Blade
    9. Chaos Servant
