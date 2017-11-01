EMEDF -- Guesses / Partial Documentation

# Table of Contents
* [0 - Register comparisons](#0---register-comparisons)
* [1 - Timer comparisons](#1---timer-comparisons)
* [3 - Event comparisons](#3---event-comparisons)
* [4 - Character comparisons](#4---character-comparisons)
* [5 - Object comparisons](#5---object-comparisons)
* [11 - Hitbox comparisons](#11---hitbox-comparisons)
* [1000 - Program control flow - Registers](#1000---program-control-flow---registers)
* [1001 - Frame and Second Timers](#1001---frame-and-second-timers)
* [1003 - Program control flow - Events](#1003---program-control-flow---events)
* [1005 - Program control flow](#1005---program-control-flow)
* [2000 - System Events](#2000---system-events)
* [2001 - Timer](#2001---timer)
* [2002 - Cutscenes](#2002---cutscenes)
* [2003 - Events](#2003---events)
* [2004 - Character](#2004---character)
* [2005 - Objects](#2005---objects)
* [2006 - SFX](#2006---sfx)
* [2007 - Message](#2007---messages)
* [2008 - Camera](#2008---camera)
* [2009 - Misc](#2009---misc)
* [2010 - Sound](#2010---sound)
* [2011 - Hitboxes](#2011---hitboxes)
* [2012 - Map](#2012---map)

---
## 0 - Register comparisons

### 0 - Condition (Evaluate register): Evaluates target register (according to its type),

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Target Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 1 - パラメータ比較状態で判定

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Left operand | i (%d) | -1:1:1000000000 | 0 | |
| Right operand | i (%d) | -1:1:1000000000 | 0 | |

## 1 - Timer Conditions

### 0 - Condition (Seconds passed)

*Checks whether a given number of seconds have passed?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Seconds Quantity | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |

### 1 - Condition (Frames passed)

*Checks whether a given number of frames have passed?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Frames Quantity | i (%d) | 0:1:99999 | 0 | |

### 2 - 経過ランダム秒Quantityで判定

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Seconds Quantity Min | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |
| Seconds Quantit yMax | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |

### 3 - 経過ランダムフレームQuantityで判定
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Frames Quantity Min | i (%d) | 0:1:99999 | 0 | |
| Frames Quantity Max | i (%d) | 0:1:99999 | 0 | |

## 3 - Event comparisons

### 0 - Condition (Event Flag Status)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired Flag State | B (%d) | [ENUM_ON_OFF_CHANGE](enums.md#ENUM_ON_OFF_CHANGE) | 1 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Event flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 1 - Condition (Batch Event Flag Status)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired Flag State | B (%d) | [ENUM_LOGICAL_OPERATION_TYPE](enums.md#ENUM_LOGICAL_OPERATION_TYPE) | 0 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Start Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| End Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 2 - Condition (Trigger Volume)

Checks if the target entity is inside/outside the given trigger volume.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Inside or outside? | B (%d) | [ENUM_CONTAINED](enums.md#ENUM_CONTAINED) | 1 | Are we checking whether the object is inside or outside the volume? |
| Target Entity ID | i (%08d) | 0:1:100000000 | 0 | |
| Area ID | i (%08d) | 0:1:100000000 | 0 | |

### 3 - Condition (Entity Within Radius of Entity)

Checks if Entity A is within / without a certain distance of Entity B.

*Please check: Is the radius spherical or cylindrical?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Inside or outside? | B (%d) | [ENUM_CONTAINED](enums.md#ENUM_CONTAINED) | 1 | Are we checking whether the object is inside or outside the radius? |
| Entity A ID | i (%08d) | 0:1:100000000 | 0 | |
| Entity B ID | i (%08d) | 0:1:100000000 | 0 | |
| Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |

### 4 - Condition (PC Has(n't) Item)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Item type | B (%08d) | [ENUM_ITEM_TYPE](enums.md#ENUM_ITEM_TYPE) | 0 | |
| Item ID | i (%08d) | 0:1:100000000 | 0 | |
| Owned state | B (%d) | [ENUM_OWN_STATE](enums.md#ENUM_OWN_STATE) | 1 | Are we checking whether the PC has the item or not? |

### 5 - Condition (Action Button State)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Category | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Target Entity ID | i (%08d) | 0:1:100000000 | 0 | |
| Reaction Angle | f (%0.3ｆ) | 0.0:1.0:100000000.0 | 0.0 | |
| Damipoly ID | h (%d) | -1:1:255 | 0 | |
| Reaction Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| Help ID | i (%d) | 0:1:100000000 | 0 | |
| Reaction Attribute | B (%d) | [ENUM_REACTION_ATTRIBUTE](enums.md#ENUM_REACTION_ATTRIBUTE) | 255 | |
| Pad ID | i (%d) | 0:1:100000000 | 0 | |

### 6 - Condition (Multiplayer State): Used to check if the PC is Host/Client or Multiplayer/Singleplayer.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired multiplayer status | b (%d) | [ENUM_MULTIPLAYER_STATE](enums.md#ENUM_MULTIPLAYER_STATE) | 0 | |

### 7 - Condition (Trigger Volume for all players)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
Inside or outside? | B (%d) | [ENUM_CONTAINED](enums.md#ENUM_CONTAINED) | 1 | Are we checking whether the object is inside or outside the volume? |
| Area ID | i (%08d) | 0:1:100000000 | 0 | |

### 8 - Condition (Game Area): Used to check if the PC is in / not in the given Area/Block (i.e. Map)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Inside / Outside | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | Are we checking whether the object is inside or outside the area/block? |
| Area ID | B (%d) | 0:1:99 | 10 | |
| Block ID | B (%d) | 0:1:99 | 0 | |

### 9 - Condition (Multiplayer Event)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Multiplayer Event ID | I (%08d) | 0:1:100000000 | 0 | |

### 10 - Condition (Count True Event Flags)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Start Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| End Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 4 | |
| Count Threshold | i (%d) | 0:1:1000000000 | 0 | |

### 11 - Condition (World Tendency): Used to check if the PC is gravelorded

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Tendency type | B (%d) | [ENUM_TENDENCY_TYPE](enums.md#ENUM_TENDENCY_TYPE) | 0 | |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Tendency threshold | B (%d) | 0:1:100 | 0 | |

### 12 - Condition (Event Value)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Start of Event Flag ID | i (%08d) | 0:1:1000000000 | 0 | |
| Number of Bits | B (%d) | 1:1:32 | 1 | |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Threshold | I (%08d) | 0:1:100000000 | 0 | |

### 13 - Condition (Action Button State (Boss Room))

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Category | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Target typeEntity ID | i (%08d) | 0:1:100000000 | 0 | |
| Reaction Angle | f (%0.3ｆ) | 0.0:1.0:100000000.0 | 0.0 | |
| Damipoly ID | h (%d) | -1:1:255 | 0 | |
| Reaction Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| Help ID | i (%d) | 0:1:100000000 | 0 | |
| Reaction Attribute | B (%d) | [ENUM_REACTION_ATTRIBUTE](enums.md#ENUM_REACTION_ATTRIBUTE) | 255 | |
| Pad ID | i (%d) | 0:1:100000000 | 0 | |

### 14 - Condition (Item Dropped In Area)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Area ID | i (%08d) | 0:1:100000000 | 0 | |

### 15 - Condition (Dropped Item)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Item type | i (%08d) | [ENUM_ITEM_TYPE](enums.md#ENUM_ITEM_TYPE) | 0 | |
| Item ID | i (%08d) | 0:1:100000000 | 0 | |

### 16 - Condition (PC Has(n't) Item -- Including Bottomless Box)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Item type | B (%08d) | [ENUM_ITEM_TYPE](enums.md#ENUM_ITEM_TYPE) | 0 | |
| Item ID | i (%08d) | 0:1:100000000 | 0 | |
| Owned state | B (%d) | [ENUM_OWN_STATE](enums.md#ENUM_OWN_STATE) | 1 | |

### 17 - Condition (NG+ Cycle)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Number of completed playthroughs | B (%03d) | 0:1:255 | 0 | |

### 18 - Condition (Line Segment Direction & Action Button)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Category | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Target typeEntity ID | i (%08d) | 0:1:100000000 | 0 | |
| Reaction Angle | f (%0.3ｆ) | 0.0:1.0:100000000.0 | 0.0 | |
| Damipoly ID | h (%d) | -1:1:255 | 0 | |
| Reaction Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| Help ID | i (%d) | 0:1:100000000 | 0 | |
| Reaction Attribute | B (%d) | [ENUM_REACTION_ATTRIBUTE](enums.md#ENUM_REACTION_ATTRIBUTE) | 255 | |
| Pad ID | i (%d) | 0:1:100000000 | 0 | |
| Line Segment Endpoint Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 19 - Condition (Line Segment Direction & Action Button (Boss Room))

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Category | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Target typeEntity ID | i (%08d) | 0:1:100000000 | 0 | |
| Reaction Angle | f (%0.3ｆ) | 0.0:1.0:100000000.0 | 0.0 | |
| Damipoly ID | h (%d) | -1:1:255 | 0 | |
| Reaction Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| Help ID | i (%d) | 0:1:100000000 | 0 | |
| Reaction Attribute | B (%d) | [ENUM_REACTION_ATTRIBUTE](enums.md#ENUM_REACTION_ATTRIBUTE) | 255 | |
| Pad ID | i (%d) | 0:1:100000000 | 0 | |
| Line Segment Endpoint Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 20 - Condition (Compare Event Flag Values)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Left-side Event Flag | i (%08d) | 0:1:1000000000 | 0 | |
| Left-side Number of Bits | B (%d) | 1:1:32 | 1 | |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Right-side Event Flag | i (%08d) | 0:1:1000000000 | 0 | |
| Right-side Number of Bits | B (%d) | 1:1:32 | 1 | |

### 21 - Condition (Owns DLC)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Owns DLC? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | Are we checking if the PC does or doesn't own the DLC? |

### 22 - Condition (Online Mode)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Online state | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | Are we checking if the PC does or doesn't own the DLC? |

## 4 - Character comparisons

### 0 - Condition (Entity Dead)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Desired death status | B (%d) | [ENUM_DEATH_STATUS](enums.md#ENUM_DEATH_STATUS) | 1 | |

### 1 - Condition (Entity Hostile)

Checks whether an entity is an enemy to a given entity.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Enemy Entity ID | i (%08d) | 0:1:1000000000 | 0 | |

### 2 - Condition (Entity Health Ratio)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Comparand Ratio | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | *Possibly meant to be the enemy entity ID?* |

### 3 - Condition (Character Type)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Character Type | b (%d) | [ENUM_CHARACTER_TYPE](enums.md#ENUM_CHARACTER_TYPE) | 0 | |

### 4 - Condition (Entity Target):

*Possibly conditional on if the specified entity is targeting the targeted entity?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Targeted Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Desired target presence | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 5 - Condition (Special Effect)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Special Effect ID | i (%d) | -1:1:1000000000 | -1 | |
| Desired effect presence | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 6 - Condition (NPC Part HP)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Part NPC type | i (%d) | 0:1:1000000000 | 0 | |
| HP Threshold | i (%d) | 0:1:1000000000 | 0 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 4 | |

### 7 - Condition (Character "Back lead" Status)

Possibly conditional on character being background loaded

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| *Back lead OK?* | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 8 - Condition (Event Message ID Match)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Event Message ID | i (%08d) | -1:1:1000000000 | -1 | |
| Desired match? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 9 - Condition (AI State)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Character Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| AI State | B (%d) | [ENUM_AI_STATUS_TYPE](enums.md#ENUM_AI_STATUS_TYPE) | 0 | |

### 10 - Condition (Player Using Skull Lantern)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired lamp state? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 11 - Condition (Player's Class)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Player Class Type | B (%d) | [ENUM_CLASS_TYPE](enums.md#ENUM_CLASS_TYPE) | 0 | |

### 12 - Condition (Player's Covenent)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Player Covenant Type | B (%d) | [ENUM_COVENANT_TYPE](enums.md#ENUM_COVENANT_TYPE) | 0 | |

### 13 - Condition (Player's Soul Level)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Soul value | I (%08d) | 0:1:100000000 | 0 | |

### 14 - Condition (Entity HP Value)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Target Entity ID | i (%08d) | 0:1:1000000000 | 0 | |
| Comparison type | B (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Health value | i (%08d) | 0:1:100000000 | 0 | |

## 5 - Object comparisons

### 0 - Condition (Destroyed Object)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Desired object damage state | B (%d) | [ENUM_DAMAGE_STATE](enums.md#ENUM_DAMAGE_STATE) | 1 | |
| Object Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 1 - Condition (Damaged Object)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Object Entity ID | i (%08d) | 0:1:100000000 | 0 | |
| Attacker Entity ID | i (%08d) | -1:1:100000000 | 0 | |

### 2 - "ObjAct Execution Judgement"

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| 実行Event ID | i (%08d) | 0:1:100000000 | 0 | |

### 3 - Condition (Object HP)
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Object Entity ID | i (%08d) | 0:1:100000000 | 0 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 4 | |
| HP Threshold | i (%d) | 0:1:1000000000 | 0 | |

## 11 - Condition registration hitbox

### 0 - Condition (Moving on Hitbox):

Checks if there is a local player moving on the specified hitbox

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Hitbox Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 1 - Condition (Running on Hitbox):

Checks if there is a local player running on the specified hitbox

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Hitbox Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 2 - Condition (Standing on Hitbox):

Checks if there is a local player standing on the specified hitbox

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Result Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | Where the result is stored |
| Hitbox Entity ID | i (%08d) | 0:1:100000000 | 0 | |

## 1000 - Program control flow - Registers

A collection of program flow controls that select behaviour based on the state in the **comparison register only**.

### 0 - 条件グループ条件状態で待機
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Condition Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 1 - Skip instructions, conditional on register state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Condition Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 2 - Terminate event, conditional on register state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Condition Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 3 - Unconditional instruction skip

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |

### 4 - Unconditional event end

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |

### 5 - Conditionally skip instructions depending on value comparison

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Left operand | i (%d) | -1:1:1000000000 | 0 | |
| Right operand | i (%d) | -1:1:1000000000 | 0 | |

### 6 - Terminate event, conditional on value comparison

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Comparison type | b (%d) | [ENUM_COMPARISON_TYPE](enums.md#ENUM_COMPARISON_TYPE) | 0 | |
| Left operand | i (%d) | -1:1:1000000000 | 0 | |
| Right operand | i (%d) | -1:1:1000000000 | 0 | |

### 7 - Skip instructions, conditional on register state

*What is the difference?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Condition Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 8 - Terminate event, conditional on register state

*What is the difference?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired register state | B (%d) | [ENUM_CONDITION_STATE](enums.md#ENUM_CONDITION_STATE) | 1 | |
| Condition Register | b (%d) | [ENUM_REGISTER](enums.md#ENUM_REGISTER) | 0 | |

### 9 - Wait for network to approve event

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Timeout (seconds) | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 3.0 | |

## 1001 - Frame and Second Timers

### 0 - Wait for a set number of seconds.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Seconds | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |

### 1 - Wait for a set number of frames.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Frames | i (%d) | 0:1:99999 | 0 | |

### 2 - Wait for a random number of seconds

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Seconds Min | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |
| Seconds Max | f (%0.3f) | 0.0:0.00999999977648:9999.0 | 0.0 | |

### 3 - Wait for a random number of frames

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Frames Min | i (%d) | 0:1:99999 | 0 | |
| Frames Max | i (%d) | 0:1:99999 | 0 | |

## 1003 - Program control flow - Events

A collection of program flow controls that select behaviour based on the state in **other events**.

### 0 - イベントフラグ状態で待機
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Desired Flag State | B (%d) | [ENUM_ON_OFF_CHANGE](enums.md#ENUM_ON_OFF_CHANGE) | 1 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Event flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 1 - Conditionally skip instructions depending on event flag state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired Flag State | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 1 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Event flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 2 - Terminate event, conditional on event flag state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired Flag State | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 1 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Event flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 3 - Skip instructions, conditional on batch event flag state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired Flag State | B (%d) | [ENUM_LOGICAL_OPERATION_TYPE](enums.md#ENUM_LOGICAL_OPERATION_TYPE) | 0 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Start Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| End Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 4 - Terminate event, conditional on batch event flag state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired Flag State | B (%d) | [ENUM_LOGICAL_OPERATION_TYPE](enums.md#ENUM_LOGICAL_OPERATION_TYPE) | 0 | |
| Event flag type | B (%d) | [ENUM_FLAG_TYPE](enums.md#ENUM_FLAG_TYPE) | 0 | |
| Start Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| End Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 5 - Skip instructions, conditional on multiplayer status

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired multiplayer status | b (%d) | [ENUM_MULTIPLAYER_STATE](enums.md#ENUM_MULTIPLAYER_STATE) | 0 | |

### 6 - Terminate event, conditional on multiplayer status

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired multiplayer status | b (%d) | [ENUM_MULTIPLAYER_STATE](enums.md#ENUM_MULTIPLAYER_STATE) | 0 | |

### 7 - Conditionally skip instructions depending on PC current area

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Inside? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |
| Area ID | B (%d) | 0:1:99 | 10 | |
| Block ID | B (%d) | 0:1:99 | 10 | |

### 8 - マップIDでイベント終了

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Inside? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |
| Area ID | B (%d) | 0:1:99 | 10 | |
| Block ID | B (%d) | 0:1:99 | 10 | |

## 1005 - Script Execution Controls (Object parameters)

### 0 - オブジェクト破壊状態で待機
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Desired object damage state | B (%d) | [ENUM_DAMAGE_STATE](enums.md#ENUM_DAMAGE_STATE) | 1 | |
| Target Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 1 - Conditionally skip instructions depending on object destruction state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Lines to skip | B (%d) | 0:1:99 | 1 | |
| Desired object damage state | B (%d) | [ENUM_DAMAGE_STATE](enums.md#ENUM_DAMAGE_STATE) | 1 | |
| Object Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 2 - Terminate event, conditional on object destruction state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 0 | |
| Desired object damage state | B (%d) | [ENUM_DAMAGE_STATE](enums.md#ENUM_DAMAGE_STATE) | 1 | |
| Object Entity ID | i (%08d) | 0:1:100000000 | 0 | |

## 2000 - System Events

### 0 - Initialize Event (iII)

Registers a new event within the system.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event Slot Number | i (%d) | -1:1:99 | 0 | Used to distinguish different initialisations of the same event slot. |
| Event ID | I (%d) | 0:0:0 | 0 | |
| Vararg | I (%d) | 0:0:0 | 0 | List of values to pass onto the event being registered |

Usage:
```
2000[00] (iII)[0, 260, 0]
```
With additional arguments
```
2000[00] (iII|II)[0, 260, 11810000, 10010600, 0]
```

### 1 -	Terminate Event (iI)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event Slot Number | i (%d) | -1:1:99 | 0 | Used to distinguish different initialisations of the same event slot. |
| Event ID | I (%d) | 0:0:0 | 0 | |

### 2 - Set network sync

Sets the desired network sync state.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Is enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 3 - 終了済み条件グループ条件状態クリア
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:0:0 | 0 | |

### 4 - Issue Prefetch Request
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Request ID | I (%d) | 0:1:1000000000 | 0 | |

### 5 - Save request
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:0:0 | 0 | |

## 2001 - Timer

## 2002 - Cutscenes

### 1 - *Play Cutscene?*
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Cutscene ID | i (%d) | 0:1:1000000000 | 0 | |
| Playback method | I (%d) | [ENUM_CUTSCENE_TYPE](enums.md#ENUM_CUTSCENE_TYPE) | 0 | |

### 2 - Play cutscene and warp player
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Cutscene ID | i (%d) | 0:1:1000000000 | 0 | |
| Playback method | I (%d) | [ENUM_CUTSCENE_TYPE](enums.md#ENUM_CUTSCENE_TYPE) | 0 | |
| Point Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Area ID | B (%d) | 0:1:255 | 0 | |
| Block ID | B (%d) | 0:1:255 | 0 | |

### 3 - Play cutscene to player

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Cutscene ID | i (%d) | 0:1:1000000000 | 0 | |
| Playback method | I (%d) | [ENUM_CUTSCENE_TYPE](enums.md#ENUM_CUTSCENE_TYPE) | 0 | |
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 4 - Play cutscene and warp specific player

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Cutscene ID | i (%d) | 0:1:1000000000 | 0 | |
| Playback method | I (%d) | [ENUM_CUTSCENE_TYPE](enums.md#ENUM_CUTSCENE_TYPE) | 0 | |
| Point Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Area ID | B (%d) | 0:1:255 | 0 | |
| Block ID | B (%d) | 0:1:255 | 0 | |
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 5 - Play cutscene and rotate player around axis parallel to Y-axis

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Cutscene ID | i (%d) | 0:1:1000000000 | 0 | |
| Playback method | I (%d) | [ENUM_CUTSCENE_TYPE](enums.md#ENUM_CUTSCENE_TYPE) | 0 | |
| Axis X[m] | f (%.2f) | 0.0:0.10000000149:9999.0 | 0.0 | |
| Axis Y[m] | f (%.2f) | 0.0:1.0:9999.0 | 0.0 | |
| Rotation[deg] | i (%.2f) | -359:1:359 | 0 | |
| Vertical translation[m] | f (%.2f) | -9999.0:0.10000000149:9999.0 | 0.0 | |
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

## 2003 - Events

### 1 - Animation Playback Request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Animation ID | i (%d) | -1:1:1000000000 | -1 | |
| Loop? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |
| Wait for completion? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |

### 2 - Set event flag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Desired state | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 1 | |

### 3 - Enable/disable Spawner

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 4 - Award item lot

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Item Lot ID | i (%d) | 0:1:1000000000 | 0 | |

### 5 - Shoot Projectile

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Owner Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Projectile Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:255 | -1 | |
| Behavior ID | i (%d) | 0:1:1000000000 | 0 | |
| Launch Angle X | i (%d) | 0:1:359 | 0 | |
| Launch Angle Y | i (%d) | 0:1:359 | 0 | |
| Launch Angle Z | i (%d) | 0:0:359 | 0 | |

### 6 - Map当たり有効化

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 7 - Map表示有効化

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 8 - Set event state: Cancels / restarts the specified event.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event ID | i (%d) | 0:1:1000000000 | 0 | |
| Event Slot ID | i (%d) | 0:1:1000000000 | 0 | |
| Event end type | B (%d) | [ENUM_EVENT_END_TYPE](enums.md#ENUM_EVENT_END_TYPE) | 1 | |

### 9 - イベントフラグ反転

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |

### 10 - イベントナビメッシュ設定

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Is Enabled | h (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 11 - Show/Hide Boss Health Bar

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Is Enabled | b (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Slot number | h (%d) | 0:1:1 | 0 | |
| Name ID | h (%d) | 0:1:9999 | 0 | |

### 12 - Kill Boss

| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 13 - Modify Navimesh Collision Bitflags

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Navimesh Collision Bit | I (%d) | [ENUM_NAVIMESH_TYPE](enums.md#ENUM_NAVIMESH_TYPE) | 128 | |
| Modification Type | B (%d) | [ENUM_BITOP](enums.md#ENUM_BITOP) | 1 | |

### 14 - Warp Player

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Area ID | B (%d) | 0:1:99 | 0 | |
| Block ID | B (%d) | 0:1:99 | 0 | |
| Area Entity ID | i (%d) | -1:1:1000000000 | -1 | |

### 15 - 中ボス撃破処理

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 16 - Trigger Multiplayer Event

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Multiplayer Event ID | I (%d) | 0:1:1000000000 | 0 | |

### 17 - Randomly set one of the flags in range to the desired state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID Min | I (%d) | 0:1:1000000000 | 0 | |
| Event flag ID Max | I (%d) | 0:1:1000000000 | 0 | |
| Desired state | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 1 | |

### 18 - Force animation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Animation ID | i (%d) | -1:1:1000000000 | -1 | |
| Loop? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |
| Wait for completion? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |
| Does not wait for transition | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |

### 19 - Set Area Texture ParamBank Slot Index

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Area ID | h (%d) | 0:1:9999 | 0 | |
| Texture ParamBank Slot Index | h (%d) | 0:1:9999 | 0 | |

### 20 - Set temporary spawn point

*Possibly used when encountering Seath for the first time?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Respawn Point ID | i (%d) | 0:1:1000000000 | 0 | |

### 21 - Increment NG+ Counter

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:1:1 | 0 | |

### 22 - Batch set event flag to given state

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Starting event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Ending event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Desired state | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 1 | |

### 23 - Set Player Respawn Point

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Respawn Point ID | i (%d) | 0:1:1000000000 | 0 | |

### 24 - Remove Items From Player

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Item type | i (%d) | [ENUM_ITEM_TYPE](enums.md#ENUM_ITEM_TYPE) | 1 | |
| Item ID | i (%d) | 0:1:1000000000 | 0 | |
| Quantity | i (%d) | 0:1:999 | 0 | |

### 25 - Place NPC Summon Sign

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Sign Type | i (%d) | [ENUM_SIGN_TYPE](enums.md#ENUM_SIGN_TYPE) | 0 | |
| Called NPC Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Creation point entity ID| i (%d) | 0:1:1000000000 | 0 | |
| Summon Event Flag ID | i (%d) | -1:1:1000000000 | 0 | |
| Dismissal Event Flag ID | i (%d) | -1:1:1000000000 | 0 | |

### 26 - Set Visibility of Tip Message

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Blood Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is visible | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 27 - タイトル抜け
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:1:1 | 0 | |

### 28 - Award Achivement

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Achievement ID | i (%d) | 0:1:1000000000 | 0 | |

### 29 - *Add to trend value?*
| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| *Trend Type?* | B (%d) | [ENUM_TENDENCY_TYPE](enums.md#ENUM_TENDENCY_TYPE) | 0 | |
| Amount | b (%d) | -100:1:100 | 0 | |

### 30 - Disable Vagrant Spawning

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Is disabled | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 31 - Increment Event Value

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Start Event Flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Number of Bits | I (%d) | 1:1:32 | 1 | |
| Maximum Value | I (%d) | 0:1:1000000000 | 0 | |

### 32 - Clear event value

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Start of Event Flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Number of Bits | I (%d) | 1:1:32 | 1 | |

### 33 - Set Snuggly Next Trade

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |

### 34 - Snuggly Item Drop

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Item Lot ID | i (%d) | 0:1:1000000000 | 0 | |
| Area Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Hitbox Entity ID | i (%d) | -1:1:1000000000 | 0 | |

### 35 - Move dropped items & bloodstains

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Source Area Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Destination Area Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 36 - Award Item (Except to Clients)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Item Lot ID | i (%d) | 0:1:1000000000 | 0 | |

### 37 - Battle of Stoicism 1v1 Ranking Request

### 38 - Battle of Stoicism 2v2 Ranking Request

### 39 - Battle of Stoicism FFA Ranking Request

### 40 - Battle of Stoicism Exit Request

### 41 - Activate player killplane

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Map ID | i (%d) | 0:1:99 | 0 | |
| Block ID | i (%d) | 0:1:99 | 0 | |
| Y coordinate threshold | f (%0.3f) | -9999.0:0.00999999977648:9999.0 | 0.0 | |
| Target Model ID | i (%d) | 0:1:9999 | 0 | |

## 2004 - Character

### 1 - Enable/disable character's AI

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 2 - Switch character allegiance

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Team Type | B (%d) | [ENUM_TEAM_TYPE](enums.md#ENUM_TEAM_TYPE) | 0 | |

### 3 - Warp Request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Warp Destination Type | B (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Destination Target ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:255 | -1 | |

### 4 - Forced death request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Yield souls | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 5 - Invalidate character

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 6 - EzState instruction request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Command | i (%d) | 0:1:1000000000 | 0 | |
| Slot | B (%d) | 0:1:3 | 0 | |

### 7 - "Create Bullet Owner"

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 8 - "Set Special Effect"

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Special Effect ID | i (%d) | 0:1:1000000000 | 0 | |

### 9 - "Special Standby Setting"

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Standby animation | i (%d) | -1:1:1000000000 | -1 | |
| Damage animation | i (%d) | -1:1:1000000000 | -1 | |
| Cancel animation | i (%d) | -1:1:1000000000 | -1 | |
| Death animation | i (%d) | -1:1:1000000000 | -1 | |
| Standby return animation | i (%d) | -1:1:1000000000 | -1 | |

### 10 - Gravity Invalidation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 11 - イベントターゲット指定

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID 2 | i (%d) | 0:1:1000000000 | 0 | |

### 12 - Enables/disables character immortality:

Sets whether the character can take damage and will not die from said damage

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 13 - Set character's "Nest" (Probably AI Home Location)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Area ID | i (%d) | 0:1:1000000000 | 0 | |

### 14 - "Rotate Character"

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID to Face | i (%d) | 0:1:1000000000 | 0 | |

### 15 - Set Character Invicibility:

Set whether the character is invicible to damage

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 16 - Clear AI Target List

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 17 - AI instruction request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Command ID | i (%d) | -1:1:1000000000 | 0 | |
| Slot number | B (%d) | 0:1:3 | 0 | |

### 18 - Set Event Point

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Event Area Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Reaction Range | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |

### 19 - Set AI ID

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| AI ID | i (%d) | 0:1:1000000000 | 0 | |

### 20 - AI Re-plan

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 21 - Cancel Special Effect

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Special Effect ID | i (%d) | 0:1:1000000000 | 0 | |

### 22 - Create multipart-NPC part

*Possibly relates to bosses with detachable tails? e.g Gargoyles, Gaping Dragon, and Sanctuary Guardian.*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Part NPC type | h (%d) | 0:1:10000 | 0 | |
| Part Index | h (%d) | [ENUM_SITE_TYPE](enums.md#ENUM_SITE_TYPE) | 1 | |
| Part HP | i (%d) | -1:1:1000000000 | 0 | |
| Partial Damage Correction | f (%d) | 0.0:1.0:9999.0 | 1.0 | |
| Body Damage Correction | f (%d) | 0.0:1.0:9999.0 | 1.0 | |
| Is Invincible | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |
| Start in stop state? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |

### 23 - Set multipart-NPC part HP

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Part NPC type | i (%d) | 0:1:10000 | 0 | |
| Desired HP | i (%d) | -100000000:1:100000000 | 0 | |
| Overwrite Max HP? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 0 | |

### 24 - Set multipart-NPC part SE and SFX

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Part NPC type | i (%d) | 0:1:10000 | 0 | |
| Defense Material SE ID | i (%d) | -1:1:1000000000 | -1 | *SE means Special Effect?* |
| Defense Material SFX ID | i (%d) | -1:1:1000000000 | -1 | |

### 25 - Set multipart-NPC part bullet damage magnification

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Part NPC type | i (%d) | 0:1:10000 | 0 | |
| Desired magnification | f (%d) | 0.0:1.0:9999.0 | 1.0 | |

### 26 - Change character display mask

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Bit Number | B (%d) | 0:1:32 | 0 | |
| Switch type | B (%d) | [ENUM_ON_OFF_CHANGE](enums.md#ENUM_ON_OFF_CHANGE) | 1 | |

### 27 - Change character hitbox mask

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Bit Number | B (%d) | 0:1:32 | 0 | |
| Switch type | B (%d) | [ENUM_ON_OFF_CHANGE](enums.md#ENUM_ON_OFF_CHANGE) | 1 | |

### 28 - Set Network Update Authority

Sets if this player should be the authority for the data about a given entity.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Authority Level | i (%d) | [ENUM_UPDATE_AUTH](enums.md#ENUM_UPDATE_AUTH) | 0 | |

### 29 - "Setting to remove from back lead"

*Possibly requests an entity to remove from background loading?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Should be Removed? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 30 - Set Health Bar Display

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 31 - Set Character Map Collision

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Disable Collision? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 32 - Issue AI Event Request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Command ID | i (%d) | -1:1:1000000000 | 0 | |
| Slot number | B (%d) | 0:1:3 | 0 | |
| Start Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |
| End Event Flag ID | i (%08d) | 0:1:100000000 | 0 | |

### 33 - Create Referred Damage Pair

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Source Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 34 - Set Network Update Rate for Entity

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Fixed Frequency? | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |
| Frequency | b (%d) | [ENUM_CHARACTER_UPDATE_RATE](enums.md#ENUM_CHARACTER_UPDATE_RATE) | 0 | |

### 35 - Set Entity "Back Lead" Status

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 36 - Hellkite Breath Control

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Character Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| ObjEntity ID | i (%d) | 0:1:1000000000 | 0 | |
| Character Animation ID | i (%d) | 0:1:1000000000 | 0 | |

### 37 - Mandatory treasure

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Character Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 38 - Betray Current Covenant

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:1:1 | 0 | |

### 39 - Enable/Disable Entity Animations

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Is Enabled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 40 - Issue Warp Request and set floor

"Floor" possibly refers to the hitbox the entity should stand on.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Warp Destination Type | B (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Destination Target ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:255 | -1 | |
| Warp Desination Hitbox Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 41 - Short Warp Request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Warp Destination Type | B (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Destination Target ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:255 | -1 | |

### 42 - Issue Warp Request and copy "floor setting" of Entity

"Floor" possibly refers to the hitbox the entity should stand on.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Warp Destination Type | B (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Destination Target ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:255 | -1 | |
| Floor Entity ID to copy | i (%d) | 0:1:1000000000 | 0 | |

### 43 - Animation Reset Request

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Interpolation Method | B (%d) | [ENUM_INTERPOLATION_STATE](enums.md#ENUM_INTERPOLATION_STATE) | 0 | |

### 44 - Switch character allegience and exit forced standby animation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Team Type | B (%d) | [ENUM_TEAM_TYPE](enums.md#ENUM_TEAM_TYPE) | 0 | |

### 45 - NPC Humanity Registration

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:1:1 | 0 | |

### 47 - "Equal Recovery": Possibly trigger a garbage collection?

## 2005 - Objects

### 1 - Request Object destruction

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Slot number | b (%d) | 0:1:3 | 0 | |

### 2 - Request Object restoration

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 3 - Object activation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 4 - Treasure activation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 5 - ObjAct start

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Object parameter ID | i (%d) | -1:1:1000000000 | -1 | |
| Relative Target Index | i (%d) | -1:1:1000000000 | -1 | |

### 6 - ObjAct activation

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Object parameter ID | i (%d) | -1:1:1000000000 | -1 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 7 - "Reproduction of object animation"

*Possibly sets the object as though it just completed the given animation?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Animation ID | i (%d) | 0:1:1000000000 | 0 | |

### 8 - "Reproduction of object destruction"

*Perhaps sets the object as though it was just destroyed?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Slot number | b (%d) | 0:1:3 | 0 | |

### 9 - Create damage-dealing Object

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | 0:1:1000000000 | 0 | |
| Behavior ID | i (%d) | 0:1:1000000000 | 0 | |
| Target type | i (%d) | [ENUM_DAMAGE_TARGET_TYPE](enums.md#ENUM_DAMAGE_TARGET_TYPE) | 1 | |
| Radius | f (%0.3f) | 0.0:1.0:9999.0 | 0.0 | |
| Life | f (%0.3f) | 0.0:1.0:9999.0 | 0.0 | |
| Repetition Time (seconds) | f (%0.3f) | 0.0:1.0:9999.0 | 0.0 | |

### 10 - Register Statue Object

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Area ID | B (%d) | 0:1:99 | 0 | |
| Block ID | B (%d) | 0:1:99 | 0 | |
| Statue type | B (%d) | [ENUM_STATUE_TYPE](enums.md#ENUM_STATUE_TYPE) | 0 | |

### 11 - Warp Object to Character

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Object Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Character Entity ID | i (%d) | -1:1:1000000000 | -1 | |
| Damipoly ID | h (%d) | -1:1:255 | -1 | |

### 12 - Remove Object Event Flag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Object Event flag ID | i (%d) | 0:1:1000000000 | 0 | |

### 13 - Set Object invulnerability

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Invulnerable? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 14 - ObjAct activation (IDX Designation)

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Object parameter ID | i (%d) | -1:1:1000000000 | -1 | |
| Relative Target Index | i (%d) | -1:1:1000000000 | -1 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 15 - "Treasure redemption"

*Possibly makes the "Pick up item / Open Chest" prompt visible?*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Target Entity ID | i (%d) | 0:1:1000000000 | 0 | |

## 2006 - SFX

### 1 - Delete Map SFX

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Should Erase only root | B (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

### 2 - Create Map SFX

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 3 - Create one-off SFX

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| SFX Type | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:1000000000 | -1 | |
| SFX ID | i (%d) | 0:1:1000000000 | 0 | |

### 4 - Create SFX attached to Object

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Object Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | 0:1:1000000000 | 0 | |
| SfxID | i (%d) | 0:1:1000000000 | 0 | |

### 5 - Delete SFX attached to Object

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Object Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Delete root? | i (%d) | [ENUM_BOOL](enums.md#ENUM_BOOL) | 1 | |

## 2007 - Messages

### 1 - Display Generic Dialog

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Message ID | i (%d) | 0:1:1000000000 | 0 | |
| Button Type | h (%d) | [ENUM_BUTTON_TYPE](enums.md#ENUM_BUTTON_TYPE) | 0 | |
| Number of Buttons | h (%d) | [ENUM_BUTTON_NUMBER](enums.md#ENUM_BUTTON_NUMBER) | 6 | |
| Entity ID | i (%d) | -1:1:1000000000 | -1 | |
| Display Distance | f (%.3f) | 0.0:0.00999999977648:100.0 | 0.0 | |

### 2 - Display Text Banner

Displays texts such as the "Victory Achieved" and "You Died" messages.

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Banner Type | B (%d) | [ENUM_TEXT_BANNER_TYPE](enums.md#ENUM_TEXT_BANNER_TYPE) | 8 | |

### 3 - Display Status Explanation Message

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Message ID | i (%d) | 0:1:1000000000 | 0 | |
| Pad Enabled? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 4 - Display Battlefield Message

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Message ID | i (%d) | 0:1:1000000000 | 0 | |
| Display Location Index | B (%d) | 0:1:1 | 0 | |

### 5 - Set Battle of Stoicism Participant 1 Nametag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 6 - Set Battle of Stoicism Participant 2 Nametag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 7 - Set Battle of Stoicism Participant 3 Nametag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 8 - Set Battle of Stoicism Participant 4 Nametag

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Player Entity ID | i (%08d) | 0:1:100000000 | 0 | |

### 9 - Display Battle of Stoicism Dissolution Message

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Message ID | i (%d) | 0:1:1000000000 | 0 | |

## 2008 - Camera

### 1 - *Change Camera ID*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| *Normal Camera ID* | i (%d) | -1:1:1000000000 | -1 | |
| *Lock Camera ID* | i (%d) | -1:1:1000000000 | -1 | |

### 2 - Shake Camera

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Vibration ID | i (%d) | 0:1:1000000000 | 0 | |
| SFX Type | i (%d) | [ENUM_CATEGORY](enums.md#ENUM_CATEGORY) | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Damipoly ID | i (%d) | -1:1:1000000000 | -1 | |
| Shake offset | f (%.3f) | 0.0:0.00999999977648:999.0 | 0.0 | |
| Dampening | f (%.3f) | 0.0:0.00999999977648:999.0 | 0.0 | |

### 3 - Set locked camera slot number

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Area ID | B (%d) | 0:1:255 | 0 | |
| Block ID | B (%d) | 0:1:255 | 0 | |
| Locked camera slot number | H (%d) | 0:1:9999 | 0 | |

## 2009 - Misc

### 0 - Register Ladder

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Event flag ID2 | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 1 - 徘徊デーモン初期化

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| 出現用Event flag ID | i (%d) | 0:1:1000000000 | 0 | |

### 2 - 徘徊デーモン登録

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID2 | i (%d) | 0:1:1000000000 | 0 | |

### 3 - Register Bonfire

"Initial Basic Spot Point" is possibly the kindle level of the bonfire? 10 = kindled once, 30 = kindled 3 times?

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Interaction Radius | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| Interaction Angle | f (%0.3f) | 0.0:1.0:100000000.0 | 0.0 | |
| *Initial basic spot point* | i (%d) | 0:1:1000000000 | 0 | |

### 4 - Activate NPC buffs

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 5 - 回復の泉登録

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Event flag ID | i (%d) | 0:1:1000000000 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |

### 6 - Issue Boss Room Entry Notification

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Dummy | B (%d) | 0:1:1 | 0 | |

## 2010 - Sound

### 1 - Play Background Music

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Playback settings | B (%d) | [ENUM_ON_OFF](enums.md#ENUM_ON_OFF) | 0 | Param name could be 'Enabled' |
| SlotNo | H (%.d) | 0:1:20 | 0 | |
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Sound Type | i (%d) | [ENUM_SOUND_TYPE](enums.md#ENUM_SOUND_TYPE) | 0 | |
| Sound ID | i (%d) | 0:1:1000000000 | 0 | |

### 2 - Play Sound Effect

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Sound type | i (%d) | [ENUM_SOUND_TYPE](enums.md#ENUM_SOUND_TYPE) | 0 | |
| Sound ID | i (%d) | 0:1:1000000000 | 0 | |

### 3 - Enable Map Sound

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Enalbled | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

## 2011 - Hitboxes

### 1 - Activate hitbox

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Hitbox Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

### 2 - *Activate Hit Part Back Lead Mask*

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Hitbox Entity ID | i (%d) | 0:1:1000000000 | 0 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

## 2012 - Map

### 1 - Activate map part

| Name | Type (Format) | Values | Default Value | Notes |
|-|-|-|-|-|
| Map Part ID | i (%d) | 0:1:1000000000 | 0 | |
| Activated? | B (%d) | [ENUM_ENABLE_STATE](enums.md#ENUM_ENABLE_STATE) | 0 | |

^\t\t([iIBfh])\s[0-9]+\s(%[0-9]*d|%[0-9.]+[fｆ])\s(.*)?\s\[(-?\d+(.[0-9]+)?:-?\d+(.[0-9]+)?:-?\d+(.[0-9]+)?|ENUM[a-zA-Z\_]+)\]\((Default: -?\d+(.[0-9]+)?)\)$
| $3 | $1 ($2) | $4 | $8 | |
