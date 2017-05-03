# -*- coding: utf-8 -*-

#[サウンドタイプ]{0: a:環境音, 1: c:キャラモーション, 2: f:メニューSE, 3: o:オブジェクト, 4: p:ポリ劇専用SE, 5: s:SFX, 6: m:BGM, 7: v:音声, 8: x:床材質依存, 9: b:鎧材質依存, 10: g:ゴースト}
ENUM_SOUND_TYPE = {0: "a: Evironmental Sound", 1: "c: Character Motion", 2: "f: Menu SE", 3: "o: Object", 4: "p: Poly Drama", \
    5: "s: SFX", 6: "m: BGM", 7: "v: Voice", 8: "x: Floor Material Dependence", 9: "b: Armor Material Dependence", 10: "g: Ghost"}

#[ボタンタイプ]{0: YES/NO, 1: OK/CANCEL}
ENUM_BUTTON_TYPE = {0: "YES/NO", 1: "OK/CANCEL"}

#[アーキタイプ]{0: 戦士, 1: 騎士, 2: 放浪者, 3: 盗賊, 4: 狩人, 5: 魔術師, 6: 呪術師, 7: 僧侶, 8: 野武士, 9: 持たざるもの, 20: 仮：戦士, 21: 仮：騎士, 22: 仮：魔術師, 23: 仮：呪術師, 24: チ：戦士, 25: チ：騎士, 26: チ：魔術師, 27: チ：呪術師}
# Note: The translations are not accurate. Instead, they are based on what classes the game actually has corresponding to each value.
ENUM_CLASS_TYPE = {0: "Warrior", 1: "Knight", 2: "Wanderer", 3: "Thief", 4: "Bandit", 5: "Hunter", 6: "Sorcerer", \
    7: "Pyromancer", 8: "Cleric", 9: "Deprived", 20: "Temp: Warrior", 21: "Temp: Knight", 22: "Temp: Sorcerer", \
    23: "Temp: Pyromancer", 24: "Chi: Warrior", 25: "Chi: Knight", 26: "Chi: Sorcerer", 27: "Chi: Pyromancer"}

#[キャラタイプ]{0: 生存, 1: 白ゴースト, 2: 黒ゴースト, 8: グレイゴースト, 12: 侵入者}
ENUM_CHARACTER_TYPE = {0: "Survival", 1: "White Ghost", 2: "Black Ghost", 8: "Gray Ghost", 12: "Intruder"}

#[ナビメッシュタイプ]{1: 通行不可, 2: 出口, 4: 障害物, 8: 壁, 64: 着地点, 128: イベント, 256: 崖, 512: 広い, 1024: 梯子, 2048: 穴, 4096: 扉, 8192: 閉扉, 32: 壁に接する床 }
ENUM_NAVIMESH_TYPE = {1: "Solid", 2: "Exit", 4: "Obstacle", 8: "Wall", 32: "Wall-touching Floor", \
    64: "Landing Point", 128: "Event", 256: "Cliff", 512: "Wide", 1024: "Ladder", 2048: "Hole", 4096: "Door", 8192: "Closed Door"}

#[チームタイプ]{255: デフォルト, 0: 無効, 1: 生存プレイヤー, 2: ホワイトゴースト, 3: ブラックゴースト, 4: グレイゴースト, 5: 徘徊ゴースト, 6: 敵, 7: 強敵, 8: 味方, 9: 味方（怒）, 10: おとり敵, 11: 赤子, 12: 戦う味方, 13: 侵入者}
ENUM_TEAM_TYPE = {255: "Default", 0: "Invalid", 1: "Survival", 2: "White Ghost", 3: "Black Ghost", 4: "Gray Ghost", 5: "Wandering Ghost", \
    6: "Enemy", 7: "Strong Enemy", 8: "Ally", 9: "Hostile Ally", 10: "Decoy Enemy", 11: "Red Child", 12: "Fighting Ally", 13: "Intruder"}
    
#[ai状態タイプ]{0: 通常, 1: 認識, 2: 警戒, 3: 戦闘}
ENUM_AI_STATUS_TYPE = {0: "Normal", 1: "Recognition", 2: "Alert", 3: "Battle"}

#[BOOL]{0: いいえ, 1: はい}
ENUM_BOOL = {0: "FALSE", 1: "TRUE"}

#[ON・OFF]{0: OFF, 1: ON}
ENUM_ON_OFF = {0: "OFF", 1: "ON"}

#[ON・OFF・CHANGE]{0: OFF, 1: ON, 2: CHANGE}
ENUM_ON_OFF_CHANGE = {0: "OFF", 1: "ON", 2: "CHANGE"}

#[SOSサインタイプ]{0: 青瞳サイン, 1: 黒瞳サイン, 2: 赤瞳サイン, 3: 探知サイン, 4: 白救援サイン, 5: 黒救援サイン}
ENUM_SIGN_TYPE = {0: "Blue Eye Sign", 1: "Black Eye Sign", 2: "Red Eye Sign", 3: "Detection Sign", 4: "White Help Sign", 5: "Black Help Sign"}

#[傾向タイプ]{0: 白傾向, 1: 黒傾向}
ENUM_TENDENCY_TYPE = {0: "White Tendency", 1: "Black Tendency"}

#[内外状態]{0: 外側, 1: 内側}
ENUM_CONTAINED = {0: "Outside", 1: "Inside"}

#[判定カテゴリ]{0: オブジェクト, 1: 領域, 2: キャラクター}
ENUM_CATEGORY = {0: "Object", 1: "Area", 2: "Character"}

#[ポリ劇再生タイプ]{0: スキップ有り, 2: スキップ無し, 8: スキップ有り フェードアウトスキップ, 10: スキップ無し フェードアウトスキップ}
ENUM_CUTSCENE_TYPE = {0: "Skippable", 2: "Unskippable", 8: "Skippable with Fade-out", 10: "Unskippable with Fade-out"}

#[反応属性]{48: 生存&グレイ, 255: 全て}
ENUM_REACTION_ATTRIBUTE = {48: "Survival & Gray", 255: "All"}

#[基準イベントフラグIDタイプ]{0: なし, 1: イベントID, 2: イベントID+スロット番号}
ENUM_FLAG_TYPE = {0: "Event Flag ID", 1: "Event ID", 2: "Event ID with Slot Number"}

#[ダメージ対象]{1: キャラ, 2: マップ, 3: キャラ＋マップ}
ENUM_DAMAGE_TARGET_TYPE = {1: "Character", 2: "Map", 3: "Character & Map"}

#[所有状態]{0: 非所有, 1: 所有}
ENUM_OWN_STATE = {0: "Does not own", 1: "Owns"}

#[ビット操作タイプ]{0: 追加, 1: 削除, 2: 反転}
ENUM_BITOP = {0: "Add", 1: "Delete", 2: "Invert"}

#[ボタン数]{1: １ボタン, 2: ２ボタン, 6: ボタン無し}
ENUM_BUTTON_NUMBER = {1: "1 Button", 2: "2 Button", 6: "No Button"}

#[キャラ更新レベル]{-1: 更新なし, 0: 常に更新, 2: 2フレームに1回, 5: 5フレームに1回}
ENUM_CHARACTER_UPDATE_RATE = {-1: "Never", 0: "Always", 2: "Every 2 frames", 5: "Every 5 frames"}

#[更新権限値]{0: 通常, 4095: 強制}
ENUM_UPDATE_AUTH = {0: "Normal", 4095: "Forced"}

#[条件グループ]{-7: OR(07), -6: OR(06), -5: OR(05), -4: OR(04), -3: OR(03), -2: OR(02), -1: OR(01), 0: 実行条件, 1: AND(01), 2: AND(02), 3: AND(03), 4: AND(04), 5: AND(05), 6: AND(06), 7: AND(07)}
ENUM_REGISTER = {-7: "OR(07)", -6: "OR(06)", -5: "OR(05)", -4: "OR(04)", -3: "OR(03)", -2: "OR(02)", -1: "OR(01)", 0: "MAIN", \
    1: "AND(01)", 2: "AND(02)", 3: "AND(03)", 4: "AND(04)", 5: "AND(05)", 6: "AND(06)", 7: "AND(07)"}

#[条件状態]{0: 不成立, 1: 成立}
ENUM_CONDITION_STATE = {0: "FALSE", 1: "TRUE"}

#[死亡状態]{0: 生存, 1: 死亡}
ENUM_DEATH_STATUS = {0: "Alive", 1: "Dead"}

#[比較タイプ]{0: ＝, 1: ！＝, 2: ＞, 3: ＜, 4: ＞＝, 5: ＜＝}
ENUM_COMPARISON_TYPE = {0: "==", 1: "!=", 2: ">", 3: "<", 4: ">=", 5: "<="}

#[テキスト演出タイプ]{1: デーモン撃破, 2: 死亡, 3: 復活, 4: ソウル取得, 5: 目標撃破, 6: ゴースト死亡, 7: 黒ゴースト死亡, 8: マップ名, 12: おめでとう, 15: 闘技場勝利, 16: 闘技場敗北, 17: 闘技場引き分け}
ENUM_TEXT_BANNER_TYPE = {1: "Demon Killed", 2: "Death", 3: "Revival", 4: "Soul Acquisition", 5: "Target Killed", 6: "Ghost Death", \
    7: "Black Ghost Death", 8: "Map Name", 12: "Congratulations", 15: "Stadium Victory", 16: "Stadium Defeat", 17: "Stadium Draw"}

#[無効・有効]{0: 無効, 1: 有効}
ENUM_ENABLE_STATE = {0: "DISABLE", 1: "ENABLE"}

#[マルチプレイ状態]{0: ホスト, 1: クライアント, 2: マルチプレイ中, 3: シングルプレイ中}
ENUM_MULTIPLAYER_STATE = {0: "Host", 1: "Client", 2: "Multiplayer", 3: "Singleplayer"}

#[石像タイプ]{0: 石化像, 1: 結晶化像}
ENUM_STATUE_TYPE = {0: "Petrified", 1: "Crystallized"}

#[破壊状態]{0: 未破壊, 1: 破壊済}
ENUM_DAMAGE_STATE = {0: "Undestroyed", 1: "Destroyed"}

#[イベント終了タイプ]{0: 終了, 1: リスタート}
ENUM_EVENT_END_TYPE = {0: "END", 1: "RESTART"}

#[装備タイプ]{0: 武器, 1: 防具, 2: 装飾, 3: 道具}
ENUM_ITEM_TYPE = {0: "Weapon", 1: "Armor", 2: "Ring", 3: "Item"}

#[補間]{0: 補間有り, 1: 補間無し}
ENUM_INTERPOLATION_STATE = {0: "Interpolated", 1: "Not Interpolated"}

#[論理演算タイプ]{0: 全てON, 1: 全てOFF, 2: どれかがON, 3: どれかがOFF}
ENUM_LOGICAL_OPERATION_TYPE = {0: "all ON", 1: "all OFF", 2: "not all OFF", 3: "not all ON"}

#[部位タイプ]{1: 部位１, 2: 部位２, 3: 部位３, 4: 部位４, 5: 部位５, 6: 部位６, 7: 弱点, 8: 部位７, 9: 部位８}
ENUM_SITE_TYPE = {1: "Part 1", 2: "Part 2", 3: "Part 3", 4: "Part 4", 5: "Part 5", 6: "Part 6", 7: "Weak Point", 8: "Part 7", 9: "Part 8"}


# ADDED ENUMS:

ENUM_COVENANT_TYPE = {0: "None", 1: "Way of White", 2: "Princess's Guard", 3: "Warrior of Sunlight", 4: "Darkwraith", 5: "Path of the Dragon", \
    6: "Gravelord Servant", 7: "Forest Hunter", 8: "Darkmoon Blade", 9: "Chaos Servant"}

ENUMS = {
    "ENUM_SOUND_TYPE": ("Sound Type", ENUM_SOUND_TYPE),
    "ENUM_BUTTON_TYPE": ("Button Type" , ENUM_BUTTON_TYPE),
    "ENUM_CLASS_TYPE": ("Class Type", ENUM_CLASS_TYPE),
    "ENUM_CHARACTER_TYPE": ("Character Type", ENUM_CHARACTER_TYPE),
    "ENUM_NAVIMESH_TYPE": ("Navimesh Type", ENUM_NAVIMESH_TYPE),
    "ENUM_TEAM_TYPE": ("Team Type", ENUM_TEAM_TYPE),
    "ENUM_AI_STATUS_TYPE": ("AI Status Type", ENUM_AI_STATUS_TYPE),
    "ENUM_BOOL": ("BOOL", ENUM_BOOL),
    "ENUM_ON_OFF": ("ON/OFF", ENUM_ON_OFF),
    "ENUM_ON_OFF_CHANGE": ("ON/OFF/CHANGE", ENUM_ON_OFF_CHANGE),
    "ENUM_SIGN_TYPE": ("Sign Type", ENUM_SIGN_TYPE),
    "ENUM_TENDENCY_TYPE": ("Tendency Type", ENUM_TENDENCY_TYPE),
    "ENUM_CONTAINED": ("Contained", ENUM_CONTAINED),
    "ENUM_CATEGORY": ("Category", ENUM_CATEGORY),
    "ENUM_CUTSCENE_TYPE": ("Cutscene Type", ENUM_CUTSCENE_TYPE),
    "ENUM_REACTION_ATTRIBUTE": ("Reaction Attribute", ENUM_REACTION_ATTRIBUTE),
    "ENUM_FLAG_TYPE": ("Flag type", ENUM_FLAG_TYPE),
    "ENUM_DAMAGE_TARGET_TYPE": ("Damage Target Type", ENUM_DAMAGE_TARGET_TYPE),
    "ENUM_OWN_STATE": ("Own State", ENUM_OWN_STATE),
    "ENUM_BITOP": ("BitOp", ENUM_BITOP),
    "ENUM_BUTTON_NUMBER": ("Num of Buttons", ENUM_BUTTON_NUMBER),
    "ENUM_CHARACTER_UPDATE_RATE": ("Character Update Rate", ENUM_CHARACTER_UPDATE_RATE),
    "ENUM_UPDATE_AUTH": ("Update Auth", ENUM_UPDATE_AUTH),
    "ENUM_REGISTER": ("Register", ENUM_REGISTER),
    "ENUM_CONDITION_STATE": ("Condition State", ENUM_CONDITION_STATE),
    "ENUM_DEATH_STATUS": ("Death Status", ENUM_DEATH_STATUS),
    "ENUM_COMPARISON_TYPE": ("Comparison Type", ENUM_COMPARISON_TYPE),
    "ENUM_TEXT_BANNER_TYPE": ("Text Banner Type", ENUM_TEXT_BANNER_TYPE),
    "ENUM_ENABLE_STATE": ("Enable State", ENUM_ENABLE_STATE),
    "ENUM_MULTIPLAYER_STATE": ("Multiplayer State", ENUM_MULTIPLAYER_STATE),
    "ENUM_STATUE_TYPE": ("Statue Type", ENUM_STATUE_TYPE),
    "ENUM_DAMAGE_STATE": ("Damage State", ENUM_DAMAGE_STATE),
    "ENUM_EVENT_END_TYPE": ("Event End Type", ENUM_EVENT_END_TYPE),
    "ENUM_ITEM_TYPE": ("Item Type", ENUM_ITEM_TYPE),
    "ENUM_INTERPOLATION_STATE": ("Interpolation State", ENUM_INTERPOLATION_STATE),
    "ENUM_LOGICAL_OPERATION_TYPE": ("Logial Op Type", ENUM_LOGICAL_OPERATION_TYPE),
    "ENUM_SITE_TYPE": ("Part type", ENUM_SITE_TYPE),
    "ENUM_COVENANT_TYPE": ("Covenant Type", ENUM_COVENANT_TYPE)
}


def stringify_args(format_string_or_enum_list, arg_list):
    """Applies stringify_arg to each element of arg_list, using the
    respective format or enum string in format_string_or_enum_list.
    """
    
    return [stringify_arg(format_string_or_enum, arg) for (format_string_or_enum, arg) in zip(format_string_or_enum_list, arg_list)]

def stringify_arg(format_string_or_enum, arg):
    """Formats arg in accordance with format_string_or_enum. If it is 
    a format string, arg must be of the correct type. Otherwise, if it
    is an enum, then arg is treated as an index into this enum.
    """
    
    if format_string_or_enum in ENUMS:
        return parse_enum(arg, format_string_or_enum)
    else:
        if isinstance(arg, basestring):
            return arg
        else:
            return format_string_or_enum % arg  

def parse_enum(value, enum_name):
    """Indexes the enum enum_name using value. If value is not found in
    enum, then a dummy string representation of enum_name[value] is 
    used instead.
    """
    
    if enum_name not in ENUMS:
        raise ValueError("Enum name '" + enum_name + "' is not a known enum...") 
    (enum_string, enum) = ENUMS[enum_name]
    if value not in enum:
        return enum_string + "[" + str(value) + "]"
    else:
        return enum[value]
        
def default_readable(instr_class, instr_index, fixed_args, var_args):
    """Creates a default readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    Provides no information about the command's purpose.
    """
    
    arg_array_string = ''
    if not var_args:
        arg_array_string = "(" + ", ".join([str(s) for s in fixed_args]) + ")"
    else:
        arg_array_string = "(" + ", ".join([str(s) for s in fixed_args]) + " | " + ", ".join([str(s) for s in var_args]) + ")"
    
    return ("%4d" % instr_class + "[" + "%2d" % instr_index + "] " + arg_array_string)

def translate(instr_class, instr_index, fix_args, var_args):
    """Creates a human-readable representation of the command with
    command instr_class and instr_index with arguments fixed_args and var_args.
    If the command is known, the human-readable representation is
    a string that desribes its function. If not, a default representation
    using default_readable is used as a fallback.
    """
    
    # Commands that make use of varargs come first:
    
    if instr_class == 2000:
        if instr_index == 0:
            return "Initialize Event (Event ID: " + "%d" % fix_args[1] + ", Slot Number: " + "%d" % fix_args[0] + \
                ", Arguments: {" + ", ".join(["%d" % fix_args[2]] + ["%d" % s for s in var_args]) + "})"
        
    # Commands that (we assume) do not make use of varargs come second:
        
    if var_args:
        raise ValueError("Command " + str(instr_class) + "[" + str(instr_index) + "] " + \
            " has varargs when it is assumed that it does not. Handle this!")
        
    if instr_class == 2000: # システム
        if instr_index == 1: #イベント強制終了
            pass
            #5	0	%d	イベントスロット番号	[-1:1:99](Default: 0)
            #2	256	%d	起動イベントID	[0:0:0](Default: 0)
        if instr_index == 2:
            return "{0} network sync.".format(*stringify_args(["ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 3: #終了済み条件グループ条件状態クリア
            #0	0	%d	ダミー	[0:0:0](Default: 0)
            pass
        if instr_index == 4:
            return "Issue Prefetch Request (Request ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 5:
            return "Save Request"
    if instr_class == 2002: #ポリ劇
        if instr_index == 1: #ポリ劇再生
            #5	1	%d	ポリ劇ID	[0:1:1000000000](Default: 0)
            #2	1	%d	再生方法	[ENUM: ENUM_CUTSCENE_TYPE](Default: 0)
            pass
        if instr_index == 2:
            return "Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) and Warp Player to (Warp Point ID: {2}, Map<{3}><{4}>)".format(\
                *stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%d", "%d", "%d"], fix_args))
        if instr_index == 3:
            return "Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) to Player Entity ID: {2}".format(*stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%08d"], fix_args))
        if instr_index == 4:
            return "Play Cutscene (Cutscene ID: {0}, Playback Method: {1}) and Warp Player Entity ID: {5} to (Warp Point ID: {2}, Map<{3}><{4}>)".format(\
                *stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%d", "%d", "%d", "%08d"], fix_args))
        if instr_index == 5:
            return ("Play Cutscene (Cutscene ID: {0}, Playback Method: {1}, Player Entity ID: {6})" + 
             " and Rotate Player Around Vertical Axis (Axis X: {2}, Axis Z: {3}, Rotation: {4} degrees, Apply Vertical Translation to Player: {5})").format(\
             *stringify_args(["%d", "ENUM_CUTSCENE_TYPE", "%.2f", "%.2f","%.2f","%.2f", "%08d"], fix_args))
    if instr_class == 2003: #イベント
        if instr_index == 1: 
            return "Request Animation Playback (Animation ID: {1}, Should loop: {2}, Wait for completion: {3}) for Entity ID: {0}".format(\
                *stringify_args(["%d", "%d", "ENUM_BOOL", "ENUM_BOOL"], fix_args))
        if instr_index == 2:
            return "SET Event Flag ID {0} to {1}".format(*stringify_args(["%d", "ENUM_ON_OFF"], fix_args))
        if instr_index == 3:
            return "{1} spawner with Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 4:
            return "Award Items (Item Lot ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 5:
            return "Shoot Projectile (Owner Entity ID: {0}, Projectile Entity ID: {1}, Damipoly ID: {2}, Behavior ID: {3}, Launch Angle XYZ: ({4}, {5}, {6}))".format(\
                *stringify_args(["%d", "%d", "%d", "%d", "%d", "%d", "%d"], fix_args))
        if instr_index == 6: #Map当たり有効化
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #0	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instr_index == 7: #Map表示有効化
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #0	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instr_index == 8:
            return "{2} Slot Number {1} of Event ID {0}".format(*stringify_args(["%d", "%d", "ENUM_EVENT_END_TYPE"], fix_args))
        if instr_index == 9: #イベントフラグ反転
            #5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 10: #イベントナビメッシュ設定
            #4	1	%d	無効・有効	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
        if instr_index == 11:
            return "{0} Boss Health Bar of Entity ID: {1} (Slot Number: {2}, Name ID: {3})".format(*stringify_args(["ENUM_ENABLE_STATE", "%d", "%d", "%d"], fix_args))
        if instr_index == 12:
            return "Kill Boss (Entity ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 13:
            # Modify the fixed args so that the bit# and its meaning can both be printed.
            mod_fix_args = [fix_args[0], fix_args[1], fix_args[1], fix_args[2]]
            return "{3} Bit# {1} ({2}) for Navimesh Entity ID: {0}".format(*stringify_args(["%d", "%d", "ENUM_NAVIMESH_TYPE", "ENUM_BITOP"], mod_fix_args))
        if instr_index == 14:
            return "Warp Player to Area Entity ID: {2} in Map<{0}><{1}>".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 15: #中ボス撃破処理
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 16:
            return "Trigger Multiplayer Event ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 17:
            return "Randomly SET one of Event Flag ID from {0} to {1} to {2}".format(*stringify_args(["%d", "%d", "ENUM_ON_OFF"], fix_args))
        if instr_index == 18:
            return "Force Entity ID: {0} to play Animation ID: {1} (Loop: {2}, Wait for completion: {3}, Do not wait for transition: {4})".format(\
                *stringify_args(["%d", "%d", "ENUM_BOOL", "ENUM_BOOL", "ENUM_BOOL"], fix_args))
        if instr_index == 19:
            return "Set Area Texture ParamBank Slot Index (Area ID: {0}, Texture ParamBank Slot Index: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 20: #一時復活ポイント設定
            #5	1	%d	復活ポイントエンティティID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 21:
            return "Increment NG+ Counter"
        if instr_index == 22:
            return "Batch SET Event Flag IDs from {0} to {1} to {2}".format(*stringify_args(["%d", "%d", "ENUM_ON_OFF"], fix_args))
        if instr_index == 23:
            return "Set Player respawn point to Point ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 24:
            return "Remove {2} (0=All) of Item (Item Type: {0}, Item ID: {1}) from player".format(*stringify_args(["ENUM_ITEM_TYPE", "%d", "%d"], fix_args))
        if instr_index == 25:
            return "Place Summon Sign for Entity ID: {1} at Point ID: {2} (Sign Type: {0}, When summoned SET Event Flag ID: {3}, When dismissed SET Event Flag ID: {4})".format(\
                *stringify_args(["ENUM_SIGN_TYPE", "%d", "%d", "%d", "%d"], fix_args))
        if instr_index == 26:
            return "{1} Tip Message (Entity ID: {0})".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 27: #タイトル抜け
            #0	1	%d	ダミー	[0:1:1](Default: 0)
            pass
        if instr_index == 28:
            return "Award Achievement ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 29: #傾向値の加算
            #0	1	%d	傾向タイプ	[ENUM: ENUM_TENDENCY_TYPE](Default: 0)
            #3	1	%d	加算値	[-100:1:100](Default: 0)
            pass
        if instr_index == 30:
            return "Disable Vagrant Spawning: {0}".format(*stringify_args(["ENUM_BOOL"], fix_args))
        if instr_index == 31:
            return "Increment Event Flag {0} (Number of Bits: {1}, Maximum: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 32:
            return "Clear Event Flag {0} (Number of Bits: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 33:
            return "Set Snuggly Next Trade Event Flag ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 34:
            return "Snuggly Item Drop: Drop Item Lot ID: {0} (corresponding to Trade Event Flag ID: {2}) at Area Entity ID: {1} on Hitbox Entity ID: {3}".format(\
                *stringify_args(["%d", "%d", "%d", "%d"], fix_args))
        if instr_index == 35:
            return "Move dropped items & bloodstain from Area Entity ID: {0} to Area Entity ID: {1}".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 36:
            return "Award Items (Item Lot ID: {0}) (Except to Clients)".format(*stringify_args(["%d"], fix_args))
        if instr_index == 37:
            return "Battle of Stoicism 1v1 Ranking Request"
        if instr_index == 38:
            return "Battle of Stoicism 2v2 Ranking Request"
        if instr_index == 39:
            return "Battle of Stoicism FFA Ranking Request"
        if instr_index == 40:
            return "Request Battle of Stoicism Exit"
        if instr_index == 41:
            return "Activate player killplane (Target Model ID: {3}) below Y threshold {2} on Map<{0}><{1}>".format(*stringify_args(["%d", "%d", "%0.3f", "%d"], fix_args))
    if instr_class == 2004: #キャラ
        if instr_index == 1:
            return "{1} AI of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 2:
            return "Switch Entity ID: {0} to team {1}".format(*stringify_args(["%d", "ENUM_TEAM_TYPE"], fix_args))
        if instr_index == 3:
            return "Issue Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, Damipoly ID: {3})".format(\
                *stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d"], fix_args))
        if instr_index == 4:
            return "Request forced death of Entity ID: {0} (Yields souls: {1})".format(*stringify_args(["%d", "ENUM_BOOL"], fix_args))
        if instr_index == 5:
            return "{1} Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 6:
            return "EzState instruction request (Entity ID: {0}, Command: {1}, Slot: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 7:
            return "??? \"Create Bullet Owner\" (Entity ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 8:
            return "Set Special Effect (Entity ID: {0}, Special Effect ID: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 9:
            return "Special Standby Setting (Entity ID: {0}, Standby Animation: {1}, Cancel Animation: {2}, Death Animation: {3}, Standby Return Animation: {4})".format(\
                *stringify_args(["%d", "%d", "%d", "%d", "%d", "%d"], fix_args))
        if instr_index == 10:
            return "{1} Gravity for Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 11: #イベントターゲット指定
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #5	1	%d	エンティティID2	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 12:
            return "{1} Immortality for Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 13:
            return "Set \"Nest\" of Entity ID: {0} to Area Entity ID: {1}".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 14:
            return "Rotate Entity ID: {0} to face Entity ID: {1}".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 15:
            return "{1} Invincibility for Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 16:
            return "Clear AI Target List of Entity ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 17:
            return "Issue AI instruction request to Entity ID: {0} (Command ID: {1}, Slot Number: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 18:
            return "Set Event Point (Event Area Entity ID: {1}, Reaction Range: {2}) for Entity ID: {0}".format(*stringify_args(["%d", "%d", "%0.3f"], fix_args))
        if instr_index == 19:
            return "? Set AI ID: {1} for Entity ID: {0}".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 20:
            return "Issue AI Re-plan request to Entity ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 21:
            return "Cancel Special Effect (Entity ID: {0}, Special Effect ID: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 22:
            return ("Create multipart-NPC part (Entity ID: {0}, Part NPC Type: {1}, Part Index: {2}, Part HP: {3}, Damage Correction: {4}, " +\
                    "Body Damage Correction: {5}, Invincible: {6}, Starts in stopped state: {7})").format(\
                    *stringify_args(["%d", "%d", "ENUM_SITE_TYPE", "%d", "%d", "%d", "ENUM_BOOL", "ENUM_BOOL"], fix_args))
        if instr_index == 23:
            return "Set HP of multipart-NPC part (Entity ID: {0}, Part NPC Type: {1}) to {2} (Overwrite max HP if required: {3})".format(\
                *stringify_args(["%d", "%d", "%d", "ENUM_BOOL"], fix_args))
        if instr_index == 24:
            return "Set multipart-NPC (Entity ID: {0}, Part NPC Type: {1}) defense material SE and SFX (SE ID: {2}, SFX ID: {3})".format(*stringify_args(["%d", "%d", "%d", "%d"], fix_args))
        if instr_index == 25:
            return "Set multipart-NPC (Entity ID: {0}, Part NPC Type: {1}) bullet damage magnification to {2}".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 26:
            return "Set display mask of character (Entity ID: {0}, Number of Bits: {1}) to {2}".format(*stringify_args(["%d", "%d", "ENUM_ON_OFF_CHANGE"], fix_args))
        if instr_index == 27:
            return "Set hitbox mask of character (Entity ID: {0}, Number of Bits: {1}) to {2}".format(*stringify_args(["%d", "%d", "ENUM_ON_OFF_CHANGE"], fix_args))
        if instr_index == 28:
            return "Set Network Update Authority of Entity ID: {0} to {1}".format(*stringify_args(["%d", "ENUM_UPDATE_AUTH"], fix_args))
        if instr_index == 29:
            return "??? \"Setting to remove from back lead\" (Entity ID: {0}, Should be removed: {1})".format(*stringify_args(["%d", "ENUM_BOOL"], fix_args))
        if instr_index == 30:
            return "{1} Health Bar for Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 31:
            return "Set Map Collision for Entity ID: {0} to Not {1}".format(*stringify_args(["%d", "ENUM_BOOL"], fix_args))
        if instr_index == 32:
            return "? Issue AI Event Request (Entity ID: {0}, Command ID: {1}, Slot Number: {2}, Start Event Flag ID: {3}, End Event Flag ID: {4})".format(\
                *stringify_args(["%d", "%d", "%d", "%08d", "%08d"], fix_args))
        if instr_index == 33:
            return "Refer damage from Entity ID: {0} to Entity ID: {1}".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 34: 
            return "Set Network Update Frequency of Entity ID: {0} to (Frequency: {2}, Fixed Rate: {1})".format(*stringify_args(["%d", "ENUM_BOOL", "ENUM_CHARACTER_UPDATE_RATE"], fix_args))
        if instr_index == 35:
            return "{1} Entity ID: {0} \"Back Lead\" Status".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 36:
            return "Hellkite Breath Control (Entity ID: {0}, Object Entity ID: {1}, Animation ID: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 37:
            return "Mandatory treasure at Entity ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 38:
            return "Betray player's current covenant"
        if instr_index == 39:
            return "? {1} Animation of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 40:
            return "Issue Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, Damipoly ID: {3}) and SET \"floor\" to Hitbox Entity ID: {4}".format(\
                *stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d", "%d"], fix_args))
        if instr_index == 41:
            return "Issue short-range Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, Damipoly ID: {3})".format(\
                *stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d"], fix_args))
        if instr_index == 42:
            return "Issue Warp request for Entity ID: {0} (Warp Destination Type: {1}, Destination Target ID: {2}, Damipoly ID: {3}) and copy \"floor setting\" from Entity ID: {4}".format(\
                *stringify_args(["%d", "ENUM_CATEGORY", "%d", "%d", "%d"], fix_args))
        if instr_index == 43:
            return "Issue Animation Reset Request for Entity ID: {0} (Interpolation: {1})".format(*stringify_args(["%d", "ENUM_INTERPOLATION_STATE"], fix_args))
        if instr_index == 44: #チームタイプ切り替え＆強制特殊待機解除
            return "Switch character (Entity ID: {0}) to team {1} and exit forced standby animation".format(*stringify_args(["%d", "ENUM_TEAM_TYPE"], fix_args))
        if instr_index == 45:
            return "Humanity Registration for Entity ID: {0} (\"First Event Flag ID to retain humanity ID\": {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 46:
            return "Increment player PvP sin"
        if instr_index == 47:
            return "??? \"Equal Recovery\""
    if instr_class == 2005: #オブジェクト
        if instr_index == 1:
            return "Request destruction of object (Entity ID: {0}, Slot Number: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 2:
            return "Request restoration of object (Entity ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 3:
            return "{1} Object with Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 4: 
            return "{1} Treasure of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 5: 
            return "ObjAct Start (Entity ID: {0}, Object Parameter ID: {1}, Relative IDX: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 6:
            return "ObjAct Activation (Entity ID: {0}, Object Parameter ID: {1}, State: {2})".format(*stringify_args(["%d", "%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 7: 
            return "\"Reproduction of object animation\" (Object Entity ID: {0}, Animation ID: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 8: 
            return "\"Reproduction of object destruction\" (Object Entity ID: {0}, Slot Number: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 9: 
            return ("Create Damage-Dealing Object (Event Flag ID: {0}, Entity ID: {1}, Damipoly ID: {2}, Behavior ID: {3}, Target Type: {4}, " +\
                "Radius: {5}, Life: {6}, Repetition Time: {7})").format(*stringify_args(["%d", "%d", "%d", "%d", "ENUM_DAMAGE_TARGET_TYPE", "%0.3f", "%0.3f", "%0.3f"], fix_args))
        if instr_index == 10: 
            return "Register Statue Object (Entity ID: {0}, Map<{1}><{2}>, Statue Type: {3})".format(*stringify_args(["%d", "%d", "%d", "ENUM_STATUE_TYPE"], fix_args))
        if instr_index == 11:
            return "Warp Object ID: {0} to Character (Entity ID: {1}) (Damipoly ID: {2})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 12:
            return "Remove Object Event Flag ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 13:
            return "{1} invulnerability of object (Entity ID: {0})".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 14:
            return "ObjAct Activation (IDX Designation) (Entity ID: {0}, Object Parameter ID: {1}, Relative IDX: {2}, State: {3})".format(\
                *stringify_args(["%d", "%d", "%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 15:
            return "Treasure Redemption of Entity ID: {0}".format(*stringify_args(["%d"], fix_args))
    if instr_class == 2006: #SFX
        if instr_index == 1:
            return "Delete Map SFX (Entity ID: {0}, Deletes only root: {1})".format(*stringify_args(["%d", "ENUM_BOOL"], fix_args))
        if instr_index == 2:
            return "Create Map SFX (Entity ID: {0})".format(*stringify_args(["%d"], fix_args))
        if instr_index == 3:
            return "Create One-Off SFX (SFX Type: {0}, Entity ID: {1}, Damipoly ID: {2}, SFX ID: {3})".format(*stringify_args(["ENUM_CATEGORY", "%d", "%d", "%d"], fix_args))
        if instr_index == 4:
            return "Create SFX ID: {2} attached to Object (Entity ID: {0}, Damipoly ID: {1})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 5:
            return "Delete SFX attached to Object (Entity ID: {0}) (Should delete root: {1})".format(*stringify_args(["%d", "ENUM_BOOL"], fix_args))
    if instr_class == 2007: #メッセージ
        if instr_index == 1:
            return "Display Generic Dialog (Message ID: {0}, Button Type: {1}, Number of Buttons: {2}, Entity ID: {3}, Display Distance: {4})".format(\
                *stringify_args(["%d", "ENUM_BUTTON_TYPE", "ENUM_BUTTON_NUMBER", "%d", "%.3f"], fix_args))
        if instr_index == 2:
            return "Display Text Banner (Banner Type: {0})".format(*stringify_args(["ENUM_TEXT_BANNER_TYPE"], fix_args))
        if instr_index == 3:
            return "Display Status Explanation Message (Message ID: {0}, {1} Pad)".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 4:
            return "Display Battlefield Message (Message ID: {0}, Display Location Index: {1})".format(*stringify_args(["%d", "%d"], fix_args))
        if instr_index == 5:
            return "Set Battle of Stoicism Participant 1 Nametag"
        if instr_index == 6:
            return "Set Battle of Stoicism Participant 2 Nametag"
        if instr_index == 7:
            return "Set Battle of Stoicism Participant 3 Nametag"
        if instr_index == 8: 
            return "Set Battle of Stoicism Participant 4 Nametag"
        if instr_index == 9: 
            return "Display Battle of Stoicism Dissolution Message (Message ID: {0})".format(*stringify_args(["%d"], fix_args))
    if instr_class == 2008: #カメラ
        if instr_index == 1: #メラ変更
            #5	1	%d	通常カメラID	[-1:1:1000000000](Default: -1)
            #5	1	%d	ロックカメラID	[-1:1:1000000000](Default: -1)
            pass
        if instr_index == 2: #カメラ振動
            #5	1	%d	振動ID	[0:1:1000000000](Default: 0)
            #5	1	%d	タイプ	[ENUM: ENUM_CATEGORY](Default: 0)
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #5	1	%d	ダミポリID	[-1:1:1000000000](Default: -1)
            #6	1	%.3f	減衰開始距離	[0.0:0.00999999977648:999.0](Default: 0.0)
            #6	1	%.3f	減衰完了距離	[0.0:0.00999999977648:999.0](Default: 0.0)
            pass
        if instr_index == 3:
            return "SET locked camera slot #{2} in Map<{0}><{1}>".format(*stringify_args(["%d", "%d", "%d"], fix_args))
    if instr_class == 2009: #スクリプト
        if instr_index == 0:
            return "? Register Ladder (Entity ID: {2}, Unknown Event Flag ID: {0}, Unknown Event Flag ID: {1})".format(*stringify_args(["%d", "%d", "%d"], fix_args))
        if instr_index == 1: #徘徊デーモン初期化
            #5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #5	1	%d	出現用イベントフラグID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 2: #徘徊デーモン登録
            #5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #5	1	%d	エンティティID2	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 3:
            return "Register Bonfire (Event Flag ID: {0}, Entity ID: {1}, Reaction Distance: {2}, Reaction Angle: {3}, Initial Kindle Level: {4})".format(\
                *stringify_args(["%d", "%d", "%0.3f", "%0.3f", "%d"], fix_args))
        if instr_index == 4:
            return "Activate buffs for NPC ID: {0}".format(*stringify_args(["%d"], fix_args))
        if instr_index == 5: #回復の泉登録
            #5	1	%d	イベントフラグID	[0:1:1000000000](Default: 0)
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 6: #ボス部屋侵入通知
            return "Issue Boss Room entry notification"
    if instr_class == 2010: #サウンド
        if instr_index == 1: #BGM再生
            #0	1	%d	再生設定	[ENUM: ENUM_ON_OFF](Default: 0)
            #1	1	%.d	スロットNo	[0:1:20](Default: 0)
            #5	1	%d	エンティティID	[0:1:1000000000](Default: 0)
            #5	1	%d	サウンドタイプ	[ENUM: ENUM_SOUND_TYPE](Default: 0)
            #5	1	%d	サウンドID	[0:1:1000000000](Default: 0)
            pass
        if instr_index == 2:
            return "Play Sound Effect (Sound Type: {1}, Sound ID: {2}) at Entity ID: {0}".format(*stringify_args(["%d", "ENUM_SOUND_TYPE", "%d"], fix_args))
        if instr_index == 3:
            return "{1} Map Sound (Entity ID: {0})".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
    if instr_class == 2011: #ヒット
        if instr_index == 1:
            return "{1} Hitbox of Entity ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
        if instr_index == 2: #ヒットパーツバックリードマスク有効化
            #5	1	%d	ヒットパーツのエンティティID	[0:1:1000000000](Default: 0)
            #0	1	%d	有効化設定	[ENUM: ENUM_ENABLE_STATE](Default: 0)
            pass
    if instr_class == 2012: #マップ
        if instr_index == 1:
            return "{1} Map Part ID: {0}".format(*stringify_args(["%d", "ENUM_ENABLE_STATE"], fix_args))
    if instr_class == 1000: #【実行制御】システム
        if instr_index == 0: #条件グループ条件状態で待機
            #0	0	%d	条件成立条件状態	[ENUM: ENUM_CONDITION_STATE](Default: 1)
            #3	0	%d	対象条件グループ	[ENUM: ENUM_REGISTER](Default: 0)
            pass
        if instr_index == 1:
            return "SKIP {0} lines IF register {2} is {1}".format(*stringify_args(["%d", "ENUM_CONDITION_STATE", "ENUM_REGISTER"], fix_args))
        if instr_index == 2:
            return "{0} event IF register {2} is {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_CONDITION_STATE", "ENUM_REGISTER"], fix_args))
        if instr_index == 3:
            return "SKIP {0} lines".format(*stringify_args(["%d"], fix_args))
        if instr_index == 4:
            return "{0} event".format(*stringify_args(["ENUM_EVENT_END_TYPE"], fix_args))
        if instr_index == 5:
            return "SKIP {0} lines IF (Event Flag ID: {2}) {1} (Event Flag ID: {3})".format(*stringify_args(["%d", "ENUM_COMPARISON_TYPE", "%d", "%d"], fix_args))
        if instr_index == 6:
            return "{0} event IF (Event Flag ID: {2}) {1} (Event Flag ID: {3})".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_COMPARISON_TYPE", "%d", "%d"], fix_args))
        if instr_index == 7:
            return "SKIP {0} lines IF register {2} is {1}".format(*stringify_args(["%d", "ENUM_CONDITION_STATE", "ENUM_REGISTER"], fix_args))
        if instr_index == 8:
            return "{0} event IF register {2} is {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_CONDITION_STATE", "ENUM_REGISTER"], fix_args))
        if instr_index == 9:
            return "WAIT {0}s for network approval".format(*stringify_args(["%0.3f"], fix_args))
    if instr_class == 1001: # 実行制御】タイマー
        if instr_index == 0:
            return "WAIT {0}s".format(*stringify_args(["%0.3f"], fix_args))
        if instr_index == 1:
            return "WAIT {0} frames".format(*stringify_args(["%d"], fix_args))
        if instr_index == 2:
            return "WAIT for a random number of seconds (Min: {0}s, Max: {1}s)".format(*stringify_args(["%0.3f", "%0.3f"], fix_args))
        if instr_index == 3: #経過ランダムフレーム数で待機
            #5	0	%d	目標フレーム最小値	[0:1:99999](Default: 0)
            #5	0	%d	目標フレーム最大値	[0:1:99999](Default: 0)
            pass
    if instr_class == 1003: #【実行制御】イベント
        if instr_index == 0: #イベントフラグ状態で待機
            #0	0	%d	条件成立フラグ状態	[ENUM: ENUM_ON_OFF_CHANGE](Default: 1)
            #0	0	%d	基準イベントフラグIDタイプ	[ENUM: ENUM_FLAG_TYPE](Default: 0)
            #5	0	%08d	対象イベントフラグID	[0:1:100000000](Default: 0)
            pass
        if instr_index == 1:
            return "SKIP {0} lines IF {2}: {3} is {1}".format(*stringify_args(["%d", "ENUM_ON_OFF", "ENUM_FLAG_TYPE", "%08d"], fix_args))
        if instr_index == 2:
            return "{0} event IF {2}: {3} is {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_ON_OFF", "ENUM_FLAG_TYPE", "%08d"], fix_args))
        if instr_index == 3:
            return "SKIP {0} lines IF {2}: {3} to {4} are {1}".format(*stringify_args(["%d", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%08d", "%08d"], fix_args))
        if instr_index == 4:
            return "{0} event IF {2}: {3} to {4} are {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%08d", "%08d"], fix_args))
        if instr_index == 5:
            return "SKIP {0} lines IF muliplayer status is {1}".format(*stringify_args(["%d", "ENUM_MULTIPLAYER_STATE"], fix_args))
        if instr_index == 6:
            return "{0} event IF multiplayer status is {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_MULTIPLAYER_STATE"], fix_args))
        if instr_index == 7:
            return "SKIP {0} lines IF it is {1} that player is in Map<{2}><{3}>".format(*stringify_args(["%d", "ENUM_BOOL", "%d", "%d"], fix_args))
        if instr_index == 8: #マップIDでイベント終了
            #0	0	%d	実行イベント終了タイプ	[ENUM: ENUM_EVENT_END_TYPE](Default: 0)
            #0	0	%d	同じか	[ENUM: ENUM_BOOL](Default: 1)
            #0	0	%d	エリアNo	[0:1:99](Default: 10)
            #0	0	%d	ブロックNo	[0:1:99](Default: 10)
            pass
    if instr_class == 1005: #【実行制御】オブジェクト
        if instr_index == 0: #オブジェクト破壊状態で待機
            #0	0	%d	条件成立破壊状態	[ENUM: ENUM_DAMAGE_STATE](Default: 1)
            #5	0	%08d	対象オブジェクトのエンティティID	[0:1:100000000](Default: 0)
            pass
        if instr_index == 1:
            return "SKIP {0} lines IF object (Entity ID: {2}) is {1}".format(*stringify_args(["%d", "ENUM_DAMAGE_STATE", "%08d"], fix_args))
        if instr_index == 2:
            return "{0} event IF object (Entity ID: {2}) is {1}".format(*stringify_args(["ENUM_EVENT_END_TYPE", "ENUM_DAMAGE_STATE", "%08d"], fix_args))
    if instr_class == 0: #《条件登録》システム
        if instr_index == 0:
            return "CONDITION: IF register {2} is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_CONDITION_STATE", "ENUM_REGISTER"], fix_args))
        if instr_index == 1: #パラメータ比較状態で判定
            #3	0	%d	登録条件グループ	[ENUM: ENUM_REGISTER](Default: 0)
            #3	0	%d	比較タイプ	[ENUM: ENUM_COMPARISON_TYPE](Default: 0)
            #5	1	%d	左辺値	[-1:1:1000000000](Default: 0)
            #5	1	%d	右辺値	[-1:1:1000000000](Default: 0)
            pass
    if instr_class == 1: #《条件登録》タイマー
        if instr_index == 0:
            return "CONDITION: IF {1}s have elapsed --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%0.3f"], fix_args))
        if instr_index == 1:
            return "CONDITION: IF {1} frames have elapsed --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%d"], fix_args))
        if instr_index == 2: #経過ランダム秒数で判定
            #3	0	%d	登録条件グループ	[ENUM: ENUM_REGISTER](Default: 0)
            #6	0	%0.3f	目標秒数最小値	[0.0:0.00999999977648:9999.0](Default: 0.0)
            #6	0	%0.3f	目標秒数最大値	[0.0:0.00999999977648:9999.0](Default: 0.0)
            pass
        if instr_index == 3: #経過ランダムフレーム数で判定
            #3	0	%d	登録条件グループ	[ENUM: ENUM_REGISTER](Default: 0)
            #5	0	%d	目標フレーム数最小値	[0:1:99999](Default: 0)
            #5	0	%d	目標フレーム数最大値	[0:1:99999](Default: 0)
            pass
    if instr_class == 3: #《条件登録》イベント
        if instr_index == 0:
            return "CONDITION: IF {2}: {3} is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_ON_OFF_CHANGE", "ENUM_FLAG_TYPE", "%08d"], fix_args))
        if instr_index == 1:
            return "CONDITION: IF {2}s: {3} to {4} are {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_LOGICAL_OPERATION_TYPE", "ENUM_FLAG_TYPE", "%08d", "%08d"], fix_args))
        if instr_index == 2:
            return "CONDITION: IF Entity ID: {2} is {1} Area Entity ID: {3} --> {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_CONTAINED", "%08d", "%08d"], fix_args))
        if instr_index == 3:
            return "CONDITION: IF Entity ID: {2} is {1} radius {4} of Entity ID: {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_CONTAINED", "%08d", "%08d", "%0.3f"], fix_args))
        if instr_index == 4:
            return "CONDITION: IF player {3} Item (Item Type: {1}, Item ID: {2}) --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_ITEM_TYPE", "%08d", "ENUM_OWN_STATE"], fix_args))
        if instr_index == 5:
            return ("CONDITION: IF Action Button State (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, " + \
                "Reaction Attribute: {7}, Pad ID: {8}) --> Register {0}").format(*stringify_args(["ENUM_REGISTER", "ENUM_CATEGORY", "%08d", "%0.3f", "%d", "%0.3f", "%d", "ENUM_REACTION_ATTRIBUTE", "%d"], fix_args))
        if instr_index == 6:
            return "CONDITION: IF player Multiplayer State is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_MULTIPLAYER_STATE"], fix_args))
        if instr_index == 7:
            return "CONDITION: IF all players are {1} Area Entity ID: {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_CONTAINED", "%08d"], fix_args))
        if instr_index == 8:
            return "CONDITION: IF it is {1} that player is in Map<{2}><{3}> --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_BOOL", "%d", "%d"], fix_args))
        if instr_index == 9:
            return "CONDITION: IF Multiplayer Event ID: {1} was triggered --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        if instr_index == 10:
            return "CONDITION: IF Number of TRUE {1}s from {2} to {3} is {4} {5} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_FLAG_TYPE", "%08d", "%08d", "ENUM_COMPARISON_TYPE", "%d"], fix_args))
        if instr_index == 11:
            return "CONDITION: IF Area {1} {2} {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_TENDENCY_TYPE", "ENUM_COMPARISON_TYPE", "%d"], fix_args))
        if instr_index == 12:
            return "CONDITION: IF (Event Flag ID: {1}, Number of Bits: {2}) has value {3} {4} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%d", "ENUM_COMPARISON_TYPE", "%08d"], fix_args))
        if instr_index == 13:
            return ("CONDITION: IF Action Button State (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, " + \
                "Reaction Attribute: {7}, Pad ID: {8}) (BOSS ROOM) --> Register {0}").format(*stringify_args(["ENUM_REGISTER", "ENUM_CATEGORY", "%08d", "%0.3f", "%d", "%0.3f", "%d", "ENUM_REACTION_ATTRIBUTE", "%d"], fix_args))
        if instr_index == 14:
            return "CONDITION: IF an item was dropped in Area Entity ID: {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        if instr_index == 15:
            return "CONDITION: IF dropped item is (Item Type: {1}, Item ID: {2}) --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_ITEM_TYPE", "%08d"], fix_args))
        if instr_index == 16:
            return "CONDITION: IF player {3} Item (Item Type: {1}, Item ID: {2}) (Including in their BBox)--> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_ITEM_TYPE", "%08d", "ENUM_OWN_STATE"], fix_args))
        if instr_index == 17:
            return "CONDITION: IF player's number of completed playthroughs is {1} {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_COMPARISON_TYPE", "%03d"], fix_args))
        if instr_index == 18:
            return ("CONDITION: IF Action Button State (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, " + \
                "Reaction Attribute: {7}, Pad ID: {8}) and Line Segment Direction (Line Segment Endpoint Entity ID: {9}) --> Register {0}").format(\
                *stringify_args(["ENUM_REGISTER", "ENUM_CATEGORY", "%08d", "%0.3f", "%d", "%0.3f", "%d", "ENUM_REACTION_ATTRIBUTE", "%d", "%08d"], fix_args))
        if instr_index == 19:
            return ("CONDITION: IF Action Button State (Target Type: {1}, Target Entity ID: {2}, Reaction Angle: {3}, Damipoly ID: {4}, Reaction Distance: {5}, Help ID: {6}, " + \
                "Reaction Attribute: {7}, Pad ID: {8}) and Line Segment Direction (Line Segment Endpoint Entity ID: {9}) (BOSS ROOM VERSION) --> Register {0}").format(\
                *stringify_args(["ENUM_REGISTER", "ENUM_CATEGORY", "%08d", "%0.3f", "%d", "%0.3f", "%d", "ENUM_REACTION_ATTRIBUTE", "%d", "%08d"], fix_args))
        if instr_index == 20:
            return "CONDITION: IF (Event Flag: {1}, Number of Bits: {2}) {3} (Event Flag: {4}, Number of Bits: {5}) --> Register {0}".format(\
                *stringify_args(["ENUM_REGISTER", "%08d", "%d", "ENUM_COMPARISON_TYPE", "%08d", "%d"], fix_args))
        if instr_index == 21:
            return "CONDITION: IF it is {1} that the player owns the DLC --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_BOOL"], fix_args))
        if instr_index == 22:
            return "CONDITION: IF it is {1} that the game is in online mode --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_BOOL"], fix_args))
    if instr_class == 4: #《条件登録》キャラ
        if instr_index == 0:
            return "CONDITION: IF Entity ID: {1} is {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_DEATH_STATUS"], fix_args))
        if instr_index == 1:
            return "CONDITION: IF Entity ID: {1} is hostile toward Entity ID: {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%08d"], fix_args))
        if instr_index == 2:
            return "CONDITION: IF Entity ID: {1} has Health Ratio {2} {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_COMPARISON_TYPE", "%0.3f"], fix_args))
        if instr_index == 3:
            return "CONDITION: IF Entity ID: {1} is of Character Type {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_CHARACTER_TYPE"], fix_args))
        if instr_index == 4:
            return "? CONDITION: IF Entity ID: {1} targeting Entity ID: {2} is {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%08d", "ENUM_BOOL"], fix_args))
        if instr_index == 5:
            return "CONDITION: IF Entity ID: {1} has Special Effect ID: {2} is {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%d", "ENUM_BOOL"], fix_args))
        if instr_index == 6:
            return "CONDITION: IF Part NPC ID: {2} of multipart-NPC Entity: {1} has HP {4} {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%d", "%d", "ENUM_COMPARISON_TYPE"], fix_args))
        if instr_index == 7:
            return "??? CONDITION: IF Entity ID: {1} \"Back lead\" status is {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_BOOL"], fix_args))
        if instr_index == 8:
            return "CONDITION: IF it is {3} that Entity ID: {1} has Event Message ID: {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%08d", "ENUM_BOOL"], fix_args))
        if instr_index == 9:
            return "CONDITION: IF Entity ID: {1} has AI State: {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_AI_STATUS_TYPE"], fix_args))
        if instr_index == 10:
            return "CONDITION: IF player currently using Skull Lantern is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_BOOL"], fix_args))
        if instr_index == 11:
            return "CONDITION: IF player's class is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_CLASS_TYPE"], fix_args))
        if instr_index == 12:
            return "CONDITION: IF player's covenant is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_COVENANT_TYPE"], fix_args))
        if instr_index == 13:
            return "CONDITION: IF player's Soul Level is {1} {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_COMPARISON_TYPE", "%08d"], fix_args))
        if instr_index == 14:
            return "CONDITION: IF Entity ID: {1} has Health Value {2} {3} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "ENUM_COMPARISON_TYPE", "%08d"], fix_args))
    if instr_class == 5: #《条件登録》オブジェクト
        if instr_index == 0:
            return "CONDITION: IF Object Entity ID: {2} is {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "ENUM_DAMAGE_STATE", "%08d"], fix_args))
        if instr_index == 1:
            return "CONDITION: IF Object Entity ID: {1} is damaged by Attacker Entity ID: {2} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d", "%08d"], fix_args))
        if instr_index == 2:
            return "CONDITION: IF ObjAct Execution Event ID: {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        if instr_index == 3: #オブジェクトのHP状態で判定
            #3	0	%d	登録条件グループ	[ENUM: ENUM_REGISTER](Default: 0)
            #5	0	%08d	対象エンティティID	[0:1:100000000](Default: 0)
            #3	0	%d	比較タイプ	[ENUM: ENUM_COMPARISON_TYPE](Default: 4)
            #5	0	%d	HP閾値	[0:1:1000000000](Default: 0)
            pass
    if instr_class == 11: #《条件登録》ヒット
        if instr_index == 0:
            return "CONDITION: IF local player is moving on Hitbox Entity ID: {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        if instr_index == 1:
            return "CONDITION: IF local player is running on Hitbox Entity ID: {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        if instr_index == 2:
            return "CONDITION: IF local player is standing on Hitbox Entity ID: {1} --> Register {0}".format(*stringify_args(["ENUM_REGISTER", "%08d"], fix_args))
        
    # If no matching return statement exists, print the default (un-translated) representation.
    return default_readable(instr_class, instr_index, fix_args, var_args)

