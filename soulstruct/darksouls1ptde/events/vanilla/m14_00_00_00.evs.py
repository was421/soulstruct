"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *
from soulstruct.darksouls1ptde.events.tests import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11400992, obj=1401960, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11400984, obj=1401961)
    RegisterBonfire(bonfire_flag=11400976, obj=1401962)
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=1401140)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=1401141)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=1401142)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=1401143)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=1401144)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=1401145)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=1401146)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=1401147)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=1401148)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=1401149)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=1401150)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=1401151)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=1401152)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=1401153)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=1401154)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=1401155)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=1401156)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=1401157)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=1401158)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=1401159)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=1401160)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=1401161)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=1401162)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=1401163)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=1401164)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=1401165)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=1401166)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=1401167)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=1401168)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=1401169)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=1401170)
    SkipLinesIfClient(6)
    DisableObject(1401994)
    DeleteVFX(1401995, erase_root_only=False)
    DisableObject(1401996)
    DeleteVFX(1401997, erase_root_only=False)
    DisableObject(1401998)
    DeleteVFX(1401999, erase_root_only=False)
    IfFlagEnabled(1, 11000810)
    IfFlagEnabled(1, 11410810)
    IfFlagEnabled(1, 11410811)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(1401601)
    SkipLines(1)
    EnableTreasure(obj=1401601)
    Event_11400090(1, obj=1401702, vfx_id=1401703, destination=1402602, destination_1=1402603)
    Event_11405090()
    Event_11405091()
    Event_11405092()
    Event_11400900()
    Event_11400800()
    Event_11405000()
    Event_11400200()
    Event_11400210()
    Event_11400220()
    Event_11400230()
    Event_140()
    DisableSoundEvent(sound_id=1403800)
    SkipLinesIfFlagDisabled(6, 9)
    Event_11405392()
    DisableObject(1401990)
    DeleteVFX(1401991, erase_root_only=False)
    DisableObject(1401992)
    DeleteVFX(1401993, erase_root_only=False)
    SkipLines(7)
    Event_11405390()
    Event_11405391()
    Event_11405393()
    Event_11405392()
    Event_11400001()
    Event_11405394()
    Event_11405395()
    Event_11405100(0, entity=1401000, region=1402000, region_1=1402001, region_2=1402002)
    Event_11405110(
        0,
        entity=1401002,
        region=1402020,
        region_1=1402021,
        region_2=1402022,
        region_3=1402023,
        region_4=1402024
    )
    Event_11405350(
        0,
        character=6160,
        character_1=1400411,
        character_2=1400412,
        character_3=1400413,
        character_4=1400414,
        character_5=1400415,
        left=1
    )
    Event_11405350(
        3,
        character=1400402,
        character_1=1400426,
        character_2=1400427,
        character_3=1400428,
        character_4=1400429,
        character_5=1400430,
        left=0
    )
    Event_11405350(
        4,
        character=1400403,
        character_1=1400431,
        character_2=1400432,
        character_3=1400433,
        character_4=1400434,
        character_5=1400435,
        left=0
    )
    Event_11400100(0, flag=11405340, region=1402200, entity=1403000)
    Event_11400100(1, flag=11405341, region=1402201, entity=1403001)
    Event_11400100(2, flag=11405342, region=1402202, entity=1403002)
    Event_11405200(0, character=1400450, obj=1401300)
    Event_11405250(0, character=1400100)
    Event_11405250(1, character=1400101)
    Event_11405250(2, character=1400102)
    Event_11405250(3, character=1400103)
    Event_11405250(4, character=1400104)
    Event_11400850(0, character=1400200, item_lot_param_id=25300200)
    Event_11400850(1, character=1400201, item_lot_param_id=25300200)
    Event_11400850(2, character=1400202, item_lot_param_id=25300200)
    Event_11400850(3, character=1400203, item_lot_param_id=25300200)
    Event_11400850(4, character=1400204, item_lot_param_id=25300200)
    Event_11400850(5, character=1400205, item_lot_param_id=25300200)
    Event_11400850(6, character=1400206, item_lot_param_id=25300200)
    Event_11400850(7, character=1400207, item_lot_param_id=25300200)
    Event_11400850(8, character=1400208, item_lot_param_id=25300200)
    Event_11400600(0, obj=1401650, obj_act_id=11400600)
    Event_11400600(1, obj=1401651, obj_act_id=11400601)
    Event_11400600(2, 1401652, 11400602)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6531, event_flag=8940)
    HumanityRegistration(6530, event_flag=8940)
    Event_11405030()
    Event_11405032()
    Event_11405035()
    Event_11400901()
    SkipLinesIfFlagEnabled(1, 1257)
    DisableCharacter(6132)
    SetTeamTypeAndExitStandbyAnimation(6132, team_type=TeamType.HostileAlly)
    Event_11400520(0, character=6132, first_flag=1250, last_flag=1259, flag=1254)
    Event_11400530(0, character=6132, first_flag=1250, last_flag=1259, flag=1257)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    Event_11400520(1, character=1400700, first_flag=1270, last_flag=1279, flag=1272)
    SkipLinesIfFlagEnabled(2, 1280)
    SetNest(6160, region=1402300)
    Move(6160, destination=1402300, destination_type=CoordEntityType.Region, short_move=True)
    Event_11400520(2, character=6160, first_flag=1280, last_flag=1289, flag=1284)
    Event_11400531(0, character=6160, first_flag=1280, last_flag=1289, flag=1281)
    Event_11400532(0, character=6160, first_flag=1280, last_flag=1289, flag=1286)
    Event_11400501(0, character=6160, flag=1282)
    Event_11400502(0, character=6160, flag=1283)
    Event_11400503(0, character=6160, flag=1287)
    Event_11400533()
    HumanityRegistration(6170, event_flag=8398)
    SkipLinesIfFlagEnabled(2, 1296)
    SkipLinesIfFlagEnabled(1, 1290)
    SkipLines(1)
    DisableCharacter(6170)
    Event_11400510(3, character=6170, flag=1294)
    Event_11400520(3, character=6170, first_flag=1290, last_flag=1309, flag=1295)
    Event_11400536(0, character=6170, first_flag=1290, last_flag=1309, flag=1291)
    Event_11400537(0, character=6170, first_flag=1290, last_flag=1309, flag=1292)
    Event_11400538(0, character=6170, first_flag=1290, last_flag=1309, flag=1293)
    Event_11400539(0, character=6170, first_flag=1290, last_flag=1309, flag=1296)
    HumanityRegistration(6282, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1502)
    SkipLinesIfFlagEnabled(1, 1501)
    DisableCharacter(6282)
    Event_11400510(4, character=6282, flag=1512)
    Event_11400520(4, character=6282, first_flag=1490, last_flag=1514, flag=1513)
    Event_11400551(0, character=6282, first_flag=1490, last_flag=1514, flag=1501)
    Event_11400552(0, character=6282, first_flag=1490, last_flag=1514, flag=1502)
    Event_11400553()
    Event_11400554(0, character=6282)
    HumanityRegistration(6311, event_flag=8470)
    HumanityRegistration(6421, event_flag=8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagEnabled(8, 11405022)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagEnabled(1, 1601)
    SkipLinesIfConditionTrue(2, 1)
    DisableCharacter(6311)
    DisableCharacter(6421)
    Event_11400520(5, character=6311, first_flag=1600, last_flag=1619, flag=1604)
    Event_11400520(6, character=6421, first_flag=1760, last_flag=1769, flag=1764)
    Event_11400504(0, character=6311, flag=1603, character_1=6421)
    Event_11400560(0, character=6311, first_flag=1600, last_flag=1619, flag=1601, character_1=6421)
    Event_11400566(0, character=6311, character_1=6421)
    Event_11400567(0, character=6311, character_1=6421)
    SkipLinesIfConditionFalse(2, 1)
    WaitFrames(frames=1)
    EnableFlag(11405022)
    DisableFlag(1766)


@NeverRestart(11400090)
def Event_11400090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11400090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11405090)
def Event_11405090():
    """Event 11405090"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(1400900)
    DisableCharacter(1400901)
    DisableCharacter(1400902)
    DisableCharacter(1400903)
    DisableCharacter(1400904)
    DisableCharacter(1400905)
    DisableCharacter(1400906)
    DisableCharacter(1400907)
    DisableCharacter(1400908)
    DisableCharacter(1400909)
    IfFlagEnabled(0, 11400080)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1400900)
    EnableCharacter(1400901)
    EnableCharacter(1400902)
    EnableCharacter(1400903)
    EnableCharacter(1400904)
    EnableCharacter(1400905)
    EnableCharacter(1400906)
    EnableCharacter(1400907)
    EnableCharacter(1400908)
    EnableCharacter(1400909)


@RestartOnRest(11405091)
def Event_11405091():
    """Event 11405091"""
    IfFlagEnabled(-1, 11405095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11400080)
    DisableFlag(11405095)
    EnableFlag(5001)
    Kill(1400900)
    Kill(1400901)
    Kill(1400902)
    Kill(1400903)
    Kill(1400904)
    Kill(1400905)
    Kill(1400906)
    Kill(1400907)
    Kill(1400908)
    Kill(1400909)


@RestartOnRest(11405092)
def Event_11405092():
    """Event 11405092"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11400080)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=BLIGHTTOWN)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11400080)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=BLIGHTTOWN)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11400080)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=BLIGHTTOWN)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11400080)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=BLIGHTTOWN)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11400080)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=BLIGHTTOWN)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11400080)
    RestartIfConditionFalse(-6)
    EnableFlag(11400080)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=BLIGHTTOWN)
    RestartIfConditionFalse(7)
    DisableFlag(11400080)
    EnableFlag(11405095)


@NeverRestart(11405390)
def Event_11405390():
    """Event 11405390"""
    IfFlagDisabled(1, 9)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1401990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11405391)
def Event_11405391():
    """Event 11405391"""
    IfFlagDisabled(1, 9)
    IfFlagEnabled(1, 11405393)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1401990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11405393)
def Event_11405393():
    """Event 11405393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 9)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1400800)


@RestartOnRest(11405392)
def Event_11405392():
    """Event 11405392"""
    SkipLinesIfFlagDisabled(3, 9)
    DisableBackread(1400800)
    Kill(1400800)
    End()
    Event_11405396()
    Event_11405397()
    SkipLinesIfFlagEnabled(1, 11400000)
    DisableCharacter(1400800)
    DisableAI(1400800)
    IfFlagEnabled(1, 11405393)
    IfCharacterInsideRegion(1, PLAYER, region=1402996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(11, 11400000)
    DeleteVFX(1401991, erase_root_only=False)
    DeleteVFX(1401993, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    CreateVFX(1401991)
    CreateVFX(1401993)
    EnableCharacter(1400800)
    EnableFlag(11400000)
    EnableAI(1400800)
    EnableBossHealthBar(1400800, name=5280)


@NeverRestart(11400001)
def Event_11400001():
    """Event 11400001"""
    IfCharacterDead(0, 1400800)
    EnableFlag(9)
    KillBoss(game_area_param_id=1400800)
    DisableObject(1401990)
    DeleteVFX(1401991)
    DisableObject(1401992)
    DeleteVFX(1401993)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(1400800)


@NeverRestart(11405394)
def Event_11405394():
    """Event 11405394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 9)
    IfFlagEnabled(1, 11405392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11405391)
    IfCharacterInsideRegion(1, PLAYER, region=1402990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1403800)


@NeverRestart(11405395)
def Event_11405395():
    """Event 11405395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 9)
    IfFlagEnabled(1, 11405394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1403800)


@UnknownRestart(11405396)
def Event_11405396():
    """Event 11405396"""
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5281, part_index=NPCPartType.Part2, part_health=300)
    SetNPCPartEffects(1400800, npc_part_id=5281, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, 1400800, npc_part_id=5281, value=0)
    IfHealthLessThanOrEqual(3, 1400800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ForceAnimation(1400800, 3011, wait_for_completion=True)
    Restart()


@UnknownRestart(11405397)
def Event_11405397():
    """Event 11405397"""
    IfCharacterAlive(1, 1400800)
    SkipLinesIfConditionTrue(1, 1)
    End()
    IfCharacterBackreadEnabled(0, 1400800)
    CreateNPCPart(1400800, npc_part_id=5280, part_index=NPCPartType.Part1, part_health=1)
    SetNPCPartEffects(1400800, npc_part_id=5280, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, 1400800, npc_part_id=5280, value=0)
    IfHealthLessThanOrEqual(3, 1400800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ForceAnimation(1400800, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest(11400800)
def Event_11400800():
    """Event 11400800"""
    SkipLinesIfThisEventFlagDisabled(5)
    DisableCharacter(1400700)
    DisableSoundEvent(sound_id=1403801)
    DisableMapCollision(collision=1403100)
    DisableMapCollision(collision=1403101)
    End()
    IfCharacterDead(0, 1400700)
    EnableFlag(140)
    DisableSoundEvent(sound_id=1403801)
    DisableMapCollision(collision=1403100)
    DisableMapCollision(collision=1403101)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.ChaosServant)
    EndIfConditionFalse(1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


@NeverRestart(11405000)
def Event_11405000():
    """Event 11405000"""
    SkipLinesIfThisEventFlagDisabled(2)
    AddSpecialEffect(1400700, 5401)
    End()
    IfHealthNotEqual(0, 1400700, value=1.0)
    AddSpecialEffect(1400700, 5401)


@RestartOnRest(11400900)
def Event_11400900():
    """Event 11400900"""
    SkipLinesIfFlagDisabled(2, 11400902)
    DisableCharacter(1400000)
    End()
    IfCharacterAlive(1, 1400000)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    IfHealthLessThanOrEqual(0, 1400000, value=0.0)
    EnableNetworkSync()
    EzstateAIRequest(1400000, command_id=1200, command_slot=0)
    Restart()


@NeverRestart(11405100)
def Event_11405100(_, entity: int, region: int, region_1: int, region_2: int):
    """Event 11405100"""
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterInsideRegion(-1, PLAYER, region=region_2)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=region)
    IfCharacterOutsideRegion(1, PLAYER, region=region_1)
    IfCharacterOutsideRegion(1, PLAYER, region=region_2)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@NeverRestart(11405110)
def Event_11405110(_, entity: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 11405110"""
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterInsideRegion(-1, PLAYER, region=region_2)
    IfCharacterInsideRegion(-1, PLAYER, region=region_3)
    IfCharacterInsideRegion(-1, PLAYER, region=region_4)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=region)
    IfCharacterOutsideRegion(1, PLAYER, region=region_1)
    IfCharacterOutsideRegion(1, PLAYER, region=region_2)
    IfCharacterOutsideRegion(1, PLAYER, region=region_3)
    IfCharacterOutsideRegion(1, PLAYER, region=region_4)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


@RestartOnRest(11405250)
def Event_11405250(_, character: int):
    """Event 11405250"""
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(
        character,
        npc_part_id=2811,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2811, material_sfx_id=1, material_vfx_id=1)
    IfHealthLessThanOrEqual(0, character, value=0.0)
    SetNPCPartHealth(character, npc_part_id=2811, desired_health=0, overwrite_max=False)


@RestartOnRest(11405300)
def Event_11405300():
    """Event 11405300"""
    Event_11405301(0, character=1400500, part_index=1, npc_part_id=3290, npc_part_id_1=3290, flag=11405301)
    Event_11405310(0, character=1400500, flag=11405301, bit_index=0, bit_index_1=1)
    Event_11405310(1, character=1400500, flag=11405301, bit_index=2, bit_index_1=3)
    Event_11405320(0, character=1400500, flag=11405301, obj=1401500, obj_1=1401501, model_point=120, model_point_1=123)
    Event_11405320(1, character=1400500, flag=11405301, obj=1401502, obj_1=1401503, model_point=126, model_point_1=129)
    Event_11405330(
        0,
        character=1400500,
        flag=11405301,
        character_1=1400600,
        character_2=1400601,
        model_point=120,
        model_point_1=123
    )
    Event_11405330(
        1,
        character=1400500,
        flag=11405301,
        character_1=1400602,
        character_2=1400603,
        model_point=126,
        model_point_1=129
    )
    Event_11405301(1, character=1400500, part_index=2, npc_part_id=3291, npc_part_id_1=3291, flag=11405302)
    Event_11405310(2, character=1400500, flag=11405302, bit_index=5, bit_index_1=11)
    Event_11405320(2, character=1400500, flag=11405302, obj=1401504, obj_1=1401505, model_point=135, model_point_1=137)
    Event_11405330(
        2,
        character=1400500,
        flag=11405302,
        character_1=1400604,
        character_2=1400605,
        model_point=135,
        model_point_1=137
    )
    Event_11405330(
        3,
        character=1400500,
        flag=11405302,
        character_1=1400606,
        character_2=1400607,
        model_point=153,
        model_point_1=155
    )
    Event_11405301(2, character=1400500, part_index=3, npc_part_id=3292, npc_part_id_1=3292, flag=11405303)
    Event_11405310(3, character=1400500, flag=11405303, bit_index=6, bit_index_1=7)
    Event_11405310(4, character=1400500, flag=11405303, bit_index=8, bit_index_1=10)
    Event_11405320(3, character=1400500, flag=11405303, obj=1401506, obj_1=1401507, model_point=138, model_point_1=141)
    Event_11405320(4, character=1400500, flag=11405303, obj=1401508, obj_1=1401509, model_point=144, model_point_1=150)
    Event_11405330(
        4,
        character=1400500,
        flag=11405303,
        character_1=1400608,
        character_2=1400609,
        model_point=138,
        model_point_1=141
    )
    Event_11405330(
        5,
        character=1400500,
        flag=11405303,
        character_1=1400610,
        character_2=1400611,
        model_point=144,
        model_point_1=150
    )
    Event_11405301(3, character=1400500, part_index=4, npc_part_id=3293, npc_part_id_1=3293, flag=11405304)
    Event_11405310(5, character=1400500, flag=11405304, bit_index=4, bit_index_1=9)
    Event_11405320(5, character=1400500, flag=11405304, obj=1401510, obj_1=1401511, model_point=132, model_point_1=134)
    Event_11405330(
        6,
        character=1400500,
        flag=11405304,
        character_1=1400612,
        character_2=1400613,
        model_point=132,
        model_point_1=134
    )
    Event_11405330(7, 1400500, 11405304, 1400614, 1400615, 150, 152)


@UnknownRestart(11405301)
def Event_11405301(_, character: int, part_index: short, npc_part_id: short, npc_part_id_1: int, flag: int):
    """Event 11405301"""
    if ThisEventSlotFlagEnabled():
        return
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=100)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=npc_part_id_1, value=0)
    IfCharacterDead(2, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11405290, 11405291))
    IfFlagEnabled(3, 11405290)
    IfFlagEnabled(4, 11405291)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, condition=4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(flag)
    SkipLinesIfFlagDisabled(1, 11405301)
    ForceAnimation(character, 8000)
    SkipLinesIfFlagDisabled(1, 11405302)
    ForceAnimation(character, 8010)


@UnknownRestart(11405310)
def Event_11405310(_, character: int, flag: int, bit_index: uchar, bit_index_1: uchar):
    """Event 11405310"""
    SkipLinesIfFlagEnabled(6, flag)
    IfFlagEnabled(1, flag)
    IfCharacterDead(2, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)


@UnknownRestart(11405320)
def Event_11405320(_, character: int, flag: int, obj: int, obj_1: int, model_point: short, model_point_1: short):
    """Event 11405320"""
    DisableObject(obj)
    DisableObject(obj_1)
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag)
    IfCharacterDead(2, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EnableObject(obj)
    EnableObject(obj_1)
    MoveObjectToCharacter(obj, character=character, model_point=model_point)
    MoveObjectToCharacter(obj_1, character=character, model_point=model_point_1)
    DestroyObject(obj)
    DestroyObject(obj_1)


@UnknownRestart(11405330)
def Event_11405330(
    _,
    character: int,
    flag: int,
    character_1: int,
    character_2: int,
    model_point: int,
    model_point_1: int,
):
    """Event 11405330"""
    EndIfFlagEnabled(flag)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    IfFlagEnabled(1, flag)
    IfCharacterDead(2, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(character)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point_1,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)


@RestartOnRest(11405350)
def Event_11405350(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    left: int,
):
    """Event 11405350"""
    SkipLinesIfValueEqual(1, left=left, right=0)
    SkipLinesIfFlagEnabled(1, 11400533)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
        End()
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    IfCharacterDead(0, character)
    SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=character,
    )
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=character,
    )
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=character,
    )
    Move(
        character_5,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableCharacter(character_5)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)
    ForceAnimation(character_3, 7000)
    ForceAnimation(character_4, 7000)
    ForceAnimation(character_5, 7000)


@NeverRestart(11400100)
def Event_11400100(_, flag: int, region: int, entity: int):
    """Event 11400100"""
    SkipLinesIfFlagEnabled(1, flag)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    EnableFlag(flag)
    DisableSpawner(entity=entity)
    IfAllPlayersOutsideRegion(0, region=region)
    DisableFlag(flag)
    EnableSpawner(entity=entity)
    Restart()


@RestartOnRest(11400850)
def Event_11400850(_, character: int, item_lot_param_id: int):
    """Event 11400850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    IfCharacterDead(0, character)
    EndIfValueEqual(left=item_lot_param_id, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)


@NeverRestart(11400600)
def Event_11400600(_, obj: int, obj_act_id: int):
    """Event 11400600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@NeverRestart(11400200)
def Event_11400200():
    """Event 11400200"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObjectActivation(1401110, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=11400201)
    IfHealthGreaterThan(0, PLAYER, value=0.0)
    DisableBackread(1400800)
    DisableBackread(1400700)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(2, 11010700)
    PlayCutscene(140010, cutscene_flags=0, player_id=10000)
    SkipLines(2)
    PlayCutscene(140015, cutscene_flags=0, player_id=10000)
    EnableFlag(11500200)
    WaitFrames(frames=1)
    SkipLinesIfFlagEnabled(1, 9)
    EnableBackread(1400800)
    EnableBackread(1400700)
    EnableFlag(11400200)
    AwardAchievement(achievement_id=30)
    AwardItemLot(9030, host_only=True)


@NeverRestart(11400210)
def Event_11400210():
    """Event 11400210"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1401200)
    End()
    IfObjectDestroyed(0, 1401200)
    EnableFlag(11400210)


@NeverRestart(11400220)
def Event_11400220():
    """Event 11400220"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1402400)
    AddSpecialEffect(PLAYER, 4140)
    Restart()


@NeverRestart(11400230)
def Event_11400230():
    """Event 11400230"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(2, 590)
    EndOfAnimation(obj=1001200, animation_id=1)
    End()
    IfSingleplayer(1)
    IfFlagDisabled(1, 590)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1001200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010161, anchor_entity=1001200)
    Restart()


@RestartOnRest(11405200)
def Event_11405200(_, character: int, obj: int):
    """Event 11405200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    RestoreObject(obj)
    DisableCharacterCollision(character)
    DisableGravity(character)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfObjectDestroyed(-1, obj)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(character)
    EnableCharacterCollision(character)
    EnableGravity(character)


@NeverRestart(11400510)
def Event_11400510(_, character: int, flag: int):
    """Event 11400510"""
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, flag)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(character)
    IfFlagEnabled(0, 703)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400520)
def Event_11400520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11400501)
def Event_11400501(_, character: int, flag: int):
    """Event 11400501"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1284)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1272)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400502)
def Event_11400502(_, character: int, flag: int):
    """Event 11400502"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(-2, 1280)
    IfFlagEnabled(-2, 1281)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400503)
def Event_11400503(_, character: int, flag: int):
    """Event 11400503"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1286)
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11400504)
def Event_11400504(_, character: int, flag: int, character_1: int):
    """Event 11400504"""
    IfFlagDisabled(1, 1603)
    IfFlagEnabled(1, 1601)
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfThisEventFlagDisabled(1)
    IfFlagDisabled(2, 1763)
    IfFlagEnabled(2, 1760)
    IfHealthLessThanOrEqual(2, character_1, value=0.8999999761581421)
    IfHealthGreaterThan(2, character_1, value=0.0)
    IfAttacked(2, attacked_entity=character_1, attacker=PLAYER)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(-2, flag)
    IfFlagEnabled(-2, 1763)
    IfFlagEnabled(-2, 745)
    IfConditionTrue(3, input_condition=-2)
    IfThisEventFlagDisabled(3)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventFlagEnabled(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=4)
    SkipLinesIfFlagEnabled(1, 1604)
    EnableFlag(flag)
    SkipLinesIfFlagEnabled(1, 1764)
    EnableFlag(1763)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Enemy)
    EnableCharacter(character_1)
    SetTeamTypeAndExitStandbyAnimation(character_1, team_type=TeamType.Enemy)
    if ThisEventFlagEnabled():
        return
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(7, input_condition=-7)
    IfPlayerCovenant(7, Covenant.ForestHunter)
    EndIfConditionFalse(7)
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


@NeverRestart(11400530)
def Event_11400530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400530"""
    IfFlagDisabled(1, 1253)
    IfFlagEnabled(1, 1256)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)


@NeverRestart(11400531)
def Event_11400531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400531"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1280)
    IfFlagEnabled(1, 11400593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11405001)
    SetNest(character, region=1402301)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.FightingAlly)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    IfCharacterInsideRegion(2, character, region=1402300)
    IfAttacked(3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11405001)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Ally)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@NeverRestart(11400532)
def Event_11400532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400532"""
    IfFlagDisabled(1, 1282)
    IfFlagDisabled(1, 1283)
    IfFlagDisabled(1, 1287)
    IfFlagEnabled(1, 1281)
    IfFlagEnabled(1, 753)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@RestartOnRest(11400533)
def Event_11400533():
    """Event 11400533"""
    SkipLinesIfThisEventFlagDisabled(6)
    DisableCharacter(1400411)
    DisableCharacter(1400412)
    DisableCharacter(1400413)
    DisableCharacter(1400414)
    DisableCharacter(1400415)
    End()
    IfCharacterDead(0, 6160)
    End()


@NeverRestart(11400536)
def Event_11400536(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400536"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1290)
    IfPlayerHasWeapon(-1, 1331000)
    IfPlayerHasWeapon(-1, 1331100)
    IfPlayerHasWeapon(-1, 1331200)
    IfPlayerHasWeapon(-1, 1331300)
    IfPlayerHasWeapon(-1, 1331400)
    IfPlayerHasWeapon(-1, 1331500)
    IfPlayerHasWeapon(-1, 1332000)
    IfPlayerHasWeapon(-1, 1332100)
    IfPlayerHasWeapon(-1, 1332200)
    IfPlayerHasWeapon(-1, 1332300)
    IfPlayerHasWeapon(-1, 1332400)
    IfPlayerHasWeapon(-1, 1332500)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11400537)
def Event_11400537(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400537"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1293)
    IfFlagEnabled(1, 11400595)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11400538)
def Event_11400538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400538"""
    IfFlagDisabled(1, 1294)
    IfFlagEnabled(1, 1291)
    IfFlagEnabled(1, 10)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11400539)
def Event_11400539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400539"""
    IfFlagEnabled(1, 1290)
    IfFlagEnabled(1, 10)
    IfFlagDisabled(2, 1294)
    IfFlagEnabled(2, 1291)
    IfFlagDisabled(2, 71400061)
    IfFlagEnabled(2, 10)
    IfFlagDisabled(3, 1294)
    IfFlagEnabled(3, 1292)
    IfCharacterBackreadDisabled(3, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@NeverRestart(11400551)
def Event_11400551(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400551"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1497)
    IfFlagEnabled(1, 11020592)
    IfInsideMap(1, game_map=BLIGHTTOWN)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(814)


@NeverRestart(11400552)
def Event_11400552(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11400552"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1501)
    IfFlagEnabled(1, 11400590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11400553)
def Event_11400553():
    """Event 11400553"""
    EndIfClient()
    if ThisEventFlagEnabled():
        return
    IfFlagEnabled(0, 11400590)
    End()


@NeverRestart(11400554)
def Event_11400554(_, character: int):
    """Event 11400554"""
    SkipLinesIfThisEventFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    IfThisEventFlagEnabled(-1)
    IfFlagEnabled(-1, 1501)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventFlagEnabled(1)
    IfFlagDisabled(0, 814)
    SetStandbyAnimationSettings(character, cancel_animation=7856)


@NeverRestart(11400560)
def Event_11400560(_, character: int, first_flag: int, last_flag: int, flag: int, character_1: int):
    """Event 11400560"""
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfFlagDisabled(1, 1603)
    IfFlagEnabled(1, 1600)
    IfFlagEnabled(1, 11400582)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableCharacter(character_1)
    DisableFlag(1766)
    EnableFlag(11405022)


@NeverRestart(11400566)
def Event_11400566(_, character: int, character_1: int):
    """Event 11400566"""
    SkipLinesIfHost(1)
    EndIfFlagEnabled(11405022)
    IfFlagEnabled(1, 746)
    EndIfConditionFalse(1)
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableFlag(1766)
    DisableFlag(11405022)


@NeverRestart(11400567)
def Event_11400567(_, character: int, character_1: int):
    """Event 11400567"""
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfFlagDisabled(1, 746)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableFlag(11405022)


@NeverRestart(140)
def Event_140():
    """Event 140"""
    DisableNetworkSync()
    IfThisEventFlagEnabled(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=1401960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        text=10010184,
        anchor_entity=1401960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@NeverRestart(11405030)
def Event_11405030():
    """Event 11405030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6531, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11405033)
    IfClient(2)
    IfFlagEnabled(2, 11405031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6531)
    EndIfFlagEnabled(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 11400901)
    IfCharacterBackreadEnabled(1, 6531)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6531,
        region=1402050,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


@NeverRestart(11405032)
def Event_11405032():
    """Event 11405032"""
    if ThisEventFlagEnabled():
        return
    IfFlagEnabled(1, 11405031)
    IfFlagEnabled(1, 11405393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6531, command_id=10, command_slot=0)
    ReplanAI(6531)
    IfCharacterInsideRegion(0, 6531, region=1402998)
    RotateToFaceEntity(6531, target_entity=1402997)
    ForceAnimation(6531, 7410)
    AICommand(6531, command_id=-1, command_slot=0)
    ReplanAI(6531)


@NeverRestart(11405035)
def Event_11405035():
    """Event 11405035"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(11405036)
    EndIfFlagEnabled(9)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11400901)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(1, PLAYER, region=1402061)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=6530,
        region=1402060,
        summon_flag=11405036,
        dismissal_flag=11405037,
    )
    Wait(20.0)
    Restart()


@NeverRestart(11400901)
def Event_11400901():
    """Event 11400901"""
    SkipLinesIfHost(3)
    IfFlagEnabled(1, 11405036)
    IfFlagDisabled(1, 11405037)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6530)
    if ThisEventFlagEnabled():
        return
    IfCharacterDead(0, 6530)
    EnableFlag(11400901)
