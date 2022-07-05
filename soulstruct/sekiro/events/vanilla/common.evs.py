"""
linked:


strings:

"""
from soulstruct.darksouls3.events import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(200)
    RunEvent(230)
    RunEvent(9570, slot=0, args=(4500, 3740))
    RunEvent(9570, slot=1, args=(4510, 3750))
    EndIfClient()
    EndIfFlagEnabled(2052)
    RunEvent(130, slot=0, args=(40, 0, 4004110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=1, args=(30, 0, 3004110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=2, args=(31, 0, 3104110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=3, args=(33, 0, 3304110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=4, args=(35, 0, 3504110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=5, args=(33, 0, 3304111, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=6, args=(38, 0, 3804110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=7, args=(38, 0, 3804111, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=8, args=(37, 0, 3704110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=9, args=(37, 0, 3704111, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=10, args=(39, 0, 3904110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=11, args=(32, 0, 3204110, 0, 26), arg_types="BBiHi")
    RunEvent(130, slot=12, args=(30, 0, 3004111, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=13, args=(34, 1, 3414110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=14, args=(40, 0, 4004111, 10, 25), arg_types="BBiHi")
    RunEvent(130, slot=15, args=(41, 0, 4104110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=16, args=(45, 0, 4504110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=17, args=(50, 0, 5004110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=18, args=(51, 0, 5104110, 0, -1), arg_types="BBiHi")
    RunEvent(130, slot=19, args=(51, 1, 5114110, 0, -1), arg_types="BBiHi")
    RunEvent(9004, slot=0, args=(9007,))
    RunEvent(9005, slot=0, args=(9008,))
    RunEvent(9006, slot=0, args=(9009,))
    RunEvent(9000, slot=0, args=(9001, 9007, 9008, 9009))
    RunEvent(9002, slot=0, args=(9003,))
    RunEvent(9010)
    RunEvent(970, slot=0, args=(13000800, 2000, 0, 0))
    RunEvent(970, slot=1, args=(13000890, 2010, 0, 0))
    RunEvent(970, slot=2, args=(13000830, 2020, 0, 0))
    RunEvent(970, slot=3, args=(13010800, 2030, 0, 0))
    RunEvent(970, slot=9, args=(13410830, 2040, 0, 0))
    RunEvent(970, slot=10, args=(13410860, 2050, 0, 0))
    RunEvent(970, slot=4, args=(13100800, 2060, 0, 0))
    RunEvent(970, slot=5, args=(13200800, 2070, 0, 0))
    RunEvent(970, slot=6, args=(13200850, 2080, 0, 0))
    RunEvent(970, slot=7, args=(13300850, 2090, 0, 0))
    RunEvent(970, slot=8, args=(13300800, 2100, 0, 0))
    RunEvent(970, slot=11, args=(13500800, 2110, 0, 0))
    RunEvent(970, slot=12, args=(13700850, 2120, 0, 0))
    RunEvent(970, slot=13, args=(13700800, 2130, 0, 0))
    RunEvent(970, slot=14, args=(13800800, 2140, 0, 0))
    RunEvent(970, slot=15, args=(13800830, 2150, 0, 0))
    RunEvent(970, slot=17, args=(13900800, 2170, 0, 0))
    RunEvent(970, slot=18, args=(14000800, 2180, 0, 0))
    RunEvent(970, slot=19, args=(14000830, 2190, 0, 0))
    RunEvent(970, slot=20, args=(14100800, 2200, 0, 0))
    RunEvent(970, slot=21, args=(14500800, 2300, 0, 0))
    RunEvent(970, slot=22, args=(14500860, 2310, 0, 0))
    RunEvent(970, slot=23, args=(15000800, 2330, 0, 0))
    RunEvent(970, slot=24, args=(15100800, 2340, 0, 0))
    RunEvent(970, slot=25, args=(15100850, 2350, 0, 0))
    RunEvent(970, slot=26, args=(15110800, 2360, 0, 0))
    RunEvent(250, slot=10, args=(17, 6700, 0.0), arg_types="iif")
    RunEvent(250, slot=11, args=(18, 6770, 0.0), arg_types="iif")
    RunEvent(250, slot=12, args=(19, 6740, 0.0), arg_types="iif")
    RunEvent(250, slot=13, args=(20, 6750, 0.0), arg_types="iif")
    RunEvent(250, slot=14, args=(21, 6760, 0.0), arg_types="iif")
    RunEvent(250, slot=15, args=(22, 6710, 0.0), arg_types="iif")
    RunEvent(250, slot=16, args=(23, 6720, 0.0), arg_types="iif")
    RunEvent(250, slot=17, args=(24, 6730, 0.0), arg_types="iif")
    RunEvent(250, slot=20, args=(4, 13300800, 0.0), arg_types="iif")
    RunEvent(250, slot=21, args=(5, 13900800, 0.0), arg_types="iif")
    RunEvent(250, slot=22, args=(6, 13700800, 0.0), arg_types="iif")
    RunEvent(250, slot=23, args=(7, 13410830, 0.0), arg_types="iif")
    RunEvent(250, slot=24, args=(27, 14000800, 0.0), arg_types="iif")
    RunEvent(250, slot=25, args=(28, 13000800, 0.0), arg_types="iif")
    RunEvent(250, slot=26, args=(29, 13100800, 0.0), arg_types="iif")
    RunEvent(250, slot=27, args=(30, 13300850, 0.0), arg_types="iif")
    RunEvent(250, slot=28, args=(31, 13500800, 0.0), arg_types="iif")
    RunEvent(250, slot=29, args=(32, 13800800, 0.0), arg_types="iif")
    RunEvent(250, slot=30, args=(33, 13700850, 0.0), arg_types="iif")
    RunEvent(250, slot=31, args=(34, 13000890, 0.0), arg_types="iif")
    RunEvent(250, slot=32, args=(35, 13010800, 0.0), arg_types="iif")
    RunEvent(250, slot=33, args=(36, 13800830, 0.0), arg_types="iif")
    RunEvent(250, slot=34, args=(37, 13000830, 0.0), arg_types="iif")
    RunEvent(250, slot=35, args=(38, 14000830, 0.0), arg_types="iif")
    RunEvent(250, slot=36, args=(39, 13200800, 0.0), arg_types="iif")
    RunEvent(250, slot=37, args=(40, 13200850, 0.0), arg_types="iif")
    RunEvent(6099)
    RunEvent(6100, slot=0, args=(6100, 13300800))
    RunEvent(6100, slot=1, args=(6101, 13900800))
    RunEvent(6100, slot=2, args=(6102, 13700800))
    RunEvent(6100, slot=3, args=(6103, 13410830))
    RunEvent(6100, slot=4, args=(6104, 14000800))
    RunEvent(6100, slot=5, args=(6105, 13000800))
    RunEvent(6100, slot=6, args=(6106, 13300850))
    RunEvent(6100, slot=7, args=(6107, 13500800))
    RunEvent(6100, slot=8, args=(6108, 13800800))
    RunEvent(6100, slot=9, args=(6109, 13700850))
    RunEvent(6100, slot=10, args=(6110, 13000890))
    RunEvent(6100, slot=11, args=(6111, 13010800))
    RunEvent(6100, slot=12, args=(6112, 110))
    RunEvent(702)
    RunEvent(710)
    RunEvent(9510)
    RunEvent(9511)
    RunEvent(9512)
    RunEvent(9520, slot=0, args=(4410, 8, 9013, 6058), arg_types="iHii")
    RunEvent(9525, slot=0, args=(4430, 4, 9005, 6054), arg_types="iHii")
    RunEvent(9530, slot=0, args=(4420, 18, 9020, 6068), arg_types="iHii")
    RunEvent(9540, slot=0, args=(15, 9017, 6065), arg_types="Hii")
    RunEvent(9100, slot=0, args=(70000007,))
    RunEvent(9101, slot=0, args=(70000008,))
    RunEvent(9102, slot=0, args=(70000012,))
    RunEvent(9103, slot=0, args=(70000013,))
    RunEvent(9104, slot=0, args=(70000017,))
    RunEvent(9105, slot=0, args=(70000019, 70000020, 70000021))
    RunEvent(9111, slot=0, args=(70000022, 70000023))
    RunEvent(9106, slot=0, args=(70000000,))
    RunEvent(9107, slot=0, args=(70000001,))
    RunEvent(9108, slot=0, args=(70000002,))
    RunEvent(9109, slot=0, args=(70000003,))
    RunEvent(9110, slot=0, args=(70000004,))
    RunEvent(9112, slot=0, args=(70000005,))
    RunEvent(9113, slot=0, args=(70000030,))
    RunEvent(9114, slot=0, args=(70000031,))
    RunEvent(9120, slot=0, args=(74000756, 74000760, 74000760, 1, 1, 1, 0), arg_types="iiiIBIi")
    RunEvent(9120, slot=1, args=(74000591, 74000552, 74000592, 3, 3, 3, 0), arg_types="iiiIBIi")
    RunEvent(9120, slot=2, args=(74000552, 74000553, 74000592, 3, 3, 6, 0), arg_types="iiiIBIi")
    RunEvent(9120, slot=3, args=(74000303, 74000316, 74000316, 1, 1, 1, 1), arg_types="iiiIBIi")
    RunEvent(9120, slot=4, args=(74000306, 74000318, 74000318, 1, 1, 1, 1), arg_types="iiiIBIi")
    RunEvent(9120, slot=5, args=(74000921, 74000925, 74000925, 1, 1, 1, 1), arg_types="iiiIBIi")
    RunEvent(9120, slot=6, args=(74000916, 74000913, 74000913, 1, 1, 1, 1), arg_types="iiiIBIi")
    RunEvent(9120, slot=7, args=(73500265, 73500264, 73500264, 1, 1, 1, 0), arg_types="iiiIBIi")
    RunEvent(9016)
    RunEvent(9011, slot=0, args=(74000132,))
    RunEvent(9014)
    RunEvent(9018)
    RunEvent(9019, slot=0, args=(74000669,))
    RunEvent(9015)
    RunEvent(6900)
    RunEvent(9020, slot=0, args=(73500300, 1621, 1634, 6951, 35, 0), arg_types="iiiiBB")
    RunEvent(9020, slot=1, args=(14100511, 14100512, 14100512, 6952, 41, 0), arg_types="iiiiBB")
    RunEvent(9020, slot=2, args=(14500161, 14500162, 14500162, 6952, 45, 0), arg_types="iiiiBB")


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(231)
    RunEvent(232)
    RunEvent(701)
    RunEvent(700)
    RunEvent(9012)
    RunEvent(741)
    RunEvent(740)
    RunEvent(9080, slot=0, args=(2, 10040, 6700), arg_types="Bii")
    RunEvent(9080, slot=1, args=(2, 10050, 6710), arg_types="Bii")
    RunEvent(9080, slot=2, args=(2, 10020, 6720), arg_types="Bii")
    RunEvent(9080, slot=3, args=(2, 10030, 6730), arg_types="Bii")
    RunEvent(9080, slot=4, args=(2, 10070, 6740), arg_types="Bii")
    RunEvent(9080, slot=5, args=(2, 10000, 6750), arg_types="Bii")
    RunEvent(9080, slot=6, args=(2, 10080, 6760), arg_types="Bii")
    RunEvent(9080, slot=7, args=(2, 10060, 6770), arg_types="Bii")
    RunEvent(9080, slot=10, args=(3, 520, 6790), arg_types="Bii")
    RunEvent(9080, slot=11, args=(3, 521, 6791), arg_types="Bii")
    RunEvent(9080, slot=12, args=(3, 522, 6792), arg_types="Bii")
    RunEvent(9080, slot=13, args=(3, 523, 6793), arg_types="Bii")
    RunEvent(9080, slot=14, args=(3, 524, 6794), arg_types="Bii")
    RunEvent(9080, slot=15, args=(3, 102, 6780), arg_types="Bii")
    RunEvent(9080, slot=16, args=(3, 101, 6781), arg_types="Bii")
    RunEvent(9080, slot=17, args=(3, 108, 6782), arg_types="Bii")
    RunEvent(9080, slot=18, args=(2, 10090, 6830), arg_types="Bii")
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2052)
    IfFlagEnabled(1, 6400)
    IfFlagDisabled(1, 14000100)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    RemoveGoodFromPlayer(115, quantity=1)
    RemoveGoodFromPlayer(384, quantity=1)
    RemoveGoodFromPlayer(386, quantity=1)
    RemoveGoodFromPlayer(390, quantity=1)
    RemoveGoodFromPlayer(490, quantity=8)
    RemoveGoodFromPlayer(2001, quantity=1)
    RemoveGoodFromPlayer(2005, quantity=1)
    RemoveGoodFromPlayer(2007, quantity=1)
    RemoveGoodFromPlayer(2008, quantity=1)
    RemoveGoodFromPlayer(2009, quantity=1)
    RemoveGoodFromPlayer(2010, quantity=1)
    RemoveGoodFromPlayer(2011, quantity=1)
    RemoveGoodFromPlayer(2012, quantity=1)
    RemoveGoodFromPlayer(2013, quantity=1)
    RemoveGoodFromPlayer(2014, quantity=1)
    RemoveGoodFromPlayer(2015, quantity=1)
    RemoveGoodFromPlayer(2102, quantity=1)
    RemoveGoodFromPlayer(2103, quantity=1)
    RemoveGoodFromPlayer(2104, quantity=1)
    RemoveGoodFromPlayer(2105, quantity=1)
    RemoveGoodFromPlayer(2106, quantity=1)
    RemoveGoodFromPlayer(2107, quantity=1)
    RemoveGoodFromPlayer(2108, quantity=1)
    RemoveGoodFromPlayer(2109, quantity=1)
    RemoveGoodFromPlayer(2110, quantity=1)
    RemoveGoodFromPlayer(2111, quantity=1)
    RemoveGoodFromPlayer(2112, quantity=1)
    RemoveGoodFromPlayer(2113, quantity=1)
    RemoveGoodFromPlayer(2114, quantity=1)
    RemoveGoodFromPlayer(2115, quantity=1)
    RemoveGoodFromPlayer(2116, quantity=1)
    RemoveGoodFromPlayer(2117, quantity=1)
    RemoveGoodFromPlayer(2119, quantity=1)
    RemoveGoodFromPlayer(2120, quantity=1)
    RemoveGoodFromPlayer(2121, quantity=1)
    RemoveGoodFromPlayer(2123, quantity=1)
    RemoveGoodFromPlayer(2124, quantity=1)
    RemoveGoodFromPlayer(2125, quantity=1)
    RemoveGoodFromPlayer(2126, quantity=1)
    RemoveGoodFromPlayer(2127, quantity=1)
    RemoveGoodFromPlayer(2128, quantity=1)
    RemoveGoodFromPlayer(2129, quantity=1)
    RemoveGoodFromPlayer(2130, quantity=1)
    RemoveGoodFromPlayer(2131, quantity=1)
    RemoveGoodFromPlayer(2132, quantity=1)
    RemoveGoodFromPlayer(2133, quantity=1)
    RemoveGoodFromPlayer(2134, quantity=1)
    RemoveGoodFromPlayer(2135, quantity=1)
    RemoveGoodFromPlayer(2137, quantity=1)
    RemoveGoodFromPlayer(2138, quantity=1)
    RemoveGoodFromPlayer(2139, quantity=1)
    RemoveGoodFromPlayer(2140, quantity=1)
    RemoveGoodFromPlayer(2142, quantity=1)
    RemoveGoodFromPlayer(2144, quantity=1)
    RemoveGoodFromPlayer(2145, quantity=1)
    RemoveGoodFromPlayer(2146, quantity=1)
    RemoveGoodFromPlayer(2147, quantity=1)
    RemoveGoodFromPlayer(2148, quantity=1)
    RemoveGoodFromPlayer(2149, quantity=1)
    RemoveGoodFromPlayer(2150, quantity=1)
    RemoveGoodFromPlayer(2151, quantity=1)
    RemoveGoodFromPlayer(2152, quantity=1)
    RemoveGoodFromPlayer(2154, quantity=1)
    RemoveGoodFromPlayer(2155, quantity=1)
    RemoveGoodFromPlayer(2156, quantity=1)
    RemoveGoodFromPlayer(2157, quantity=1)
    RemoveGoodFromPlayer(2158, quantity=1)
    DisableFlag(6400)

    # --- 0 --- #
    DefineLabel(0)


def Event130(_, arg_0_0: uchar, arg_1_1: uchar, arg_4_7: int, arg_8_9: ushort, arg_12_15: int):
    """ 130: Event 130 """
    EndIfThisEventSlotFlagEnabled()
    IfInsideMap(1, game_map=(arg_0_0, arg_1_1))
    IfPlayerStandingOnCollision(1, arg_4_7)
    IfInsideMap(2, game_map=FIRELINK_SHRINE)
    SkipLinesIfConditionFalse(1, 2)
    IfMapInCeremony(1, game_map=(arg_0_0, arg_1_1), ceremony_id=arg_8_9)
    IfConditionTrue(0, input_condition=1)
    EndIfValueEqual(left=arg_12_15, right=-1)
    AwardAchievement(arg_12_15)
    End()


@RestartOnRest
def Event200():
    """ 200: Event 200 """
    DisableNetworkSync()
    EndIfPlayerInOwnWorld()
    EnableFlag(201)


@RestartOnRest
def Event230():
    """ 230: Event 230 """
    EndIfFlagEnabled(230)
    IfFlagEnabled(1, 9314)
    IfFlagEnabled(1, 9318)
    IfConditionTrue(0, input_condition=1)
    SetMapCeremony(game_map=HIGH_WALL_OF_LOTHRIC, ceremony_id=10)
    SetMapCeremony(game_map=LOTHRIC_CASTLE, ceremony_id=10)
    SetMapCeremony(game_map=GRAND_ARCHIVES, ceremony_id=10)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=10)
    SetMapCeremony(game_map=FARRON_KEEP, ceremony_id=10)
    SetMapCeremony(game_map=CATHEDRAL_OF_THE_DEEP, ceremony_id=10)
    EnableFlag(230)


@RestartOnRest
def Event231():
    """ 231: Event 231 """
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    EndIfConditionTrue(1)
    SetMapCeremony(game_map=FIRELINK_SHRINE, ceremony_id=10)
    End()


def Event232():
    """ 232: Event 232 """
    GotoIfFlagEnabled(Label.L1, 8221)
    GotoIfFlagEnabled(Label.L0, 230)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=0)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=10)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    IfInsideMap(-1, game_map=HIGH_WALL_OF_LOTHRIC)
    IfInsideMap(-1, game_map=LOTHRIC_CASTLE)
    IfInsideMap(-1, game_map=GRAND_ARCHIVES)
    IfInsideMap(-1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    GotoIfFlagEnabled(Label.L2, 230)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=20)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    SetMapCeremony(game_map=UNDEAD_SETTLEMENT, ceremony_id=30)
    Goto(Label.L3)

    # --- 3 --- #
    DefineLabel(3)
    IfOutsideMap(1, game_map=HIGH_WALL_OF_LOTHRIC)
    IfOutsideMap(1, game_map=LOTHRIC_CASTLE)
    IfOutsideMap(1, game_map=GRAND_ARCHIVES)
    IfOutsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    Restart()


def Event250(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 250: Event 250 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_4_7)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_8_11)
    AwardAchievement(arg_0_3)


def Event6100(_, arg_0_3: int, arg_4_7: int):
    """ 6100: Event 6100 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_4_7)
    IfPlayerInOwnWorld(1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)


def Event700():
    """ 700: Event 700 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2052)
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(50006020)
    EnableFlag(9215)
    SetPlayerRemainingYoelLevels(level_count=5)
    EnableFlag(70000125)
    EnableFlag(70000128)
    EnableFlag(70000129)
    IfPlayerClass(-15, ClassType.Sorcerer)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(74000587)
    IfPlayerClass(-14, ClassType.Pyromancer)
    SkipLinesIfConditionFalse(1, -14)
    EnableFlag(74000465)
    EnableFlag(50006162)
    EnableFlag(50006163)
    EnableFlag(73501010)
    EnableFlag(73501020)
    EnableFlag(73501030)
    EnableFlag(73501040)
    EnableFlag(73501050)
    IfNewGameCycleGreaterThanOrEqual(-13, completion_count=1)
    SkipLinesIfConditionFalse(1, -13)
    EnableFlag(70000900)
    IfNewGameCycleGreaterThanOrEqual(6, completion_count=6)
    SkipLinesIfConditionFalse(2, 6)
    EnableFlag(56)
    End()
    IfNewGameCycleEqual(5, completion_count=5)
    SkipLinesIfConditionFalse(2, 5)
    EnableFlag(55)
    End()
    IfNewGameCycleEqual(4, completion_count=4)
    SkipLinesIfConditionFalse(2, 4)
    EnableFlag(54)
    End()
    IfNewGameCycleEqual(3, completion_count=3)
    SkipLinesIfConditionFalse(2, 3)
    EnableFlag(53)
    End()
    IfNewGameCycleEqual(2, completion_count=2)
    SkipLinesIfConditionFalse(2, 2)
    EnableFlag(52)
    End()
    IfNewGameCycleEqual(1, completion_count=1)
    SkipLinesIfConditionFalse(2, 1)
    EnableFlag(51)
    End()
    EnableFlag(50)
    End()


def Event701():
    """ 701: Event 701 """
    DisableFlag(6000)
    EnableFlag(6001)


def Event702():
    """ 702: Event 702 """
    EndIfFlagEnabled(6600)
    IfFlagEnabled(0, 6600)
    EnableFlag(703)


def Event710():
    """ 710: Event 710 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventSlotFlagEnabled()
    IfPlayerHasGood(15, 2014, including_box=False)
    EndIfConditionTrue(15)
    IfPlayerInOwnWorld(1)
    IfFlagEnabled(1, 9314)
    IfFlagEnabled(1, 9318)
    IfCharacterInsideRegion(-1, PLAYER, region=3702890)
    IfCharacterInsideRegion(-1, PLAYER, region=3902890)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4900)
    AddSpecialEffect(PLAYER, 4901)
    GotoIfInsideMap(Label.L0, IRITHYLL)
    GotoIfInsideMap(Label.L1, PROFANED_CAPITAL)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    Wait(3.0)
    EnableFlag(13700002)
    IfFlagEnabled(8, 13000896)
    IfFlagDisabled(8, 13000890)
    SkipLinesIfConditionTrue(2, 8)
    PlayCutsceneAndMovePlayer_WithSecondRegion(
        37000030,
        CutsceneFlags.Skippable,
        move_to_region=3002100,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
        player_id=PLAYER,
        other_region=3002890,
    )
    SkipLines(1)
    PlayCutsceneAndMovePlayer_WithSecondRegion(
        37000030,
        CutsceneFlags.Skippable,
        move_to_region=3002890,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
        player_id=PLAYER,
        other_region=3002890,
    )
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagRangeAllDisabled(Label.L19, (1388, 1389))
    IfFlagEnabled(-2, 73900164)
    IfFlagEnabled(-2, 1398)
    IfCharacterOutsideRegion(2, PLAYER, region=3902890)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L20, input_condition=2)

    # --- 19 --- #
    DefineLabel(19)
    Wait(3.0)

    # --- 20 --- #
    DefineLabel(20)
    EnableFlag(13900001)
    IfFlagEnabled(9, 13000896)
    IfFlagDisabled(9, 13000890)
    SkipLinesIfConditionTrue(2, 9)
    PlayCutsceneAndMovePlayer_WithSecondRegion(
        39000030,
        CutsceneFlags.Skippable,
        move_to_region=3002100,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
        player_id=PLAYER,
        other_region=3002890,
    )
    SkipLines(1)
    PlayCutsceneAndMovePlayer_WithSecondRegion(
        39000030,
        CutsceneFlags.Skippable,
        move_to_region=3002890,
        move_to_map=HIGH_WALL_OF_LOTHRIC,
        player_id=PLAYER,
        other_region=3002890,
    )
    Goto(Label.L2)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(711)
    WaitFrames(0)
    CancelSpecialEffect(PLAYER, 4900)
    CancelSpecialEffect(PLAYER, 4901)
    End()


def Event730():
    """ 730: Event 730 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(1)
    IfCharacterHasSpecialEffect(1, PLAYER, 100)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    CancelSpecialEffect(PLAYER, 11907)
    Wait(1.0)
    Restart()


def Event740():
    """ 740: Event 740 """
    DisableNetworkSync()
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


def Event741():
    """ 741: Event 741 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2052)
    DisableFlag(74000013)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfMapInCeremony(1, game_map=FIRELINK_SHRINE, ceremony_id=10)
    IfConditionFalse(0, input_condition=1)
    EnableFlag(743)
    IfInsideMap(2, game_map=FIRELINK_SHRINE)
    IfMapInCeremony(2, game_map=FIRELINK_SHRINE, ceremony_id=10)
    IfPlayerStandingOnCollision(3, 4004120)
    IfConditionFalse(2, input_condition=3)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest
def Event750():
    """ 750: Event 750 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    RemoveGoodFromPlayer(10110, quantity=99)
    RemoveGoodFromPlayer(10120, quantity=99)
    RemoveGoodFromPlayer(10200, quantity=99)
    RemoveGoodFromPlayer(10210, quantity=99)
    RemoveGoodFromPlayer(10220, quantity=99)
    RemoveGoodFromPlayer(10230, quantity=99)


def Event970(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 970: Event 970 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfValueEqual(1, left=arg_4_7, right=0)
    AwardItemLot(arg_4_7, host_only=True)
    DisableNetworkSync()
    Wait(5.0)
    SkipLinesIfValueEqual(1, left=arg_8_11, right=0)
    AwardItemLot(arg_8_11, host_only=True)
    SkipLinesIfValueEqual(1, left=arg_12_15, right=0)
    AwardItemLot(arg_12_15, host_only=True)


def Event6099():
    """ 6099: Event 6099 """
    DisableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, 6050)
    IfFlagEnabled(1, 6051)
    IfFlagEnabled(1, 6054)
    IfFlagEnabled(1, 6056)
    IfFlagEnabled(1, 6057)
    IfFlagEnabled(1, 6058)
    IfFlagEnabled(1, 6059)
    IfFlagEnabled(1, 6062)
    IfFlagEnabled(1, 6065)
    IfFlagEnabled(1, 6066)
    IfFlagEnabled(1, 6067)
    IfFlagEnabled(1, 6068)
    IfFlagEnabled(1, 6069)
    IfFlagEnabled(1, 6072)
    IfFlagEnabled(1, 6073)
    IfFlagEnabled(1, 6074)
    IfFlagEnabled(1, 6075)
    IfFlagEnabled(1, 6076)
    IfFlagEnabled(1, 6077)
    IfFlagEnabled(1, 6078)
    IfFlagEnabled(1, 6079)
    IfFlagEnabled(1, 6080)
    IfFlagEnabled(1, 6081)
    IfFlagEnabled(1, 6082)
    IfFlagEnabled(1, 6083)
    IfFlagEnabled(1, 6084)
    IfConditionTrue(0, input_condition=1)
    AwardAchievement(14)
    EnableFlag(6099)


def Event6900():
    """ 6900: Event 6900 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventSlotFlagEnabled()
    IfPlayerDoesNotHaveGood(1, 170, including_box=False)
    IfPlayerDoesNotHaveGood(1, 171, including_box=False)
    EndIfConditionTrue(1)
    EnableFlag(6030)


def Event9510():
    """ 9510: Event 9510 """
    EndIfThisEventSlotFlagEnabled()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 13500193)
    IfFlagEnabled(1, 8240)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9510)


def Event9511():
    """ 9511: Event 9511 """
    EndIfThisEventSlotFlagEnabled()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 13500194)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9511)


def Event9512():
    """ 9512: Event 9512 """
    EndIfThisEventSlotFlagEnabled()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 13700194)
    IfFlagEnabled(1, 13300184)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9512)


@RestartOnRest
def Event9520(_, arg_0_3: int, arg_4_5: ushort, arg_8_11: int, arg_12_15: int):
    """ 9520: Event 9520 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(0, 13304194)
    AICommand(3300194, command_id=99, slot=2)
    ReplanAI(3300194)
    IfCharacterHasSpecialEffect(0, 3300194, arg_0_3)
    AICommand(3300194, command_id=-1, slot=2)
    ReplanAI(3300194)
    EndIfFlagEnabled(arg_12_15)
    AwardGestureItem(gesture_id=arg_4_5, item_type=ItemType.Good, item_id=arg_8_11)
    EnableFlag(arg_12_15)


@RestartOnRest
def Event9525(_, arg_0_3: int, arg_4_5: ushort, arg_8_11: int, arg_12_15: int):
    """ 9525: Event 9525 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(-1, 13304195)
    IfFlagEnabled(-1, 13704192)
    IfFlagEnabled(-1, 14104190)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(2, 13304195)
    AICommand(3300195, command_id=99, slot=2)
    ReplanAI(3300195)
    SkipLinesIfFlagDisabled(2, 13704192)
    AICommand(3700192, command_id=99, slot=2)
    ReplanAI(3700192)
    SkipLinesIfFlagDisabled(2, 14104190)
    AICommand(4100190, command_id=99, slot=2)
    ReplanAI(4100190)
    IfCharacterHasSpecialEffect(-2, 3300195, arg_0_3)
    IfCharacterHasSpecialEffect(-2, 3700192, arg_0_3)
    IfCharacterHasSpecialEffect(-2, 4100191, arg_0_3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFlagDisabled(2, 13304195)
    AICommand(3300195, command_id=-1, slot=2)
    ReplanAI(3300195)
    SkipLinesIfFlagDisabled(2, 13704192)
    AICommand(3700192, command_id=-1, slot=2)
    ReplanAI(3700192)
    SkipLinesIfFlagDisabled(2, 14104191)
    AICommand(4100190, command_id=-1, slot=2)
    ReplanAI(4100190)
    EndIfFlagEnabled(arg_12_15)
    AwardGestureItem(gesture_id=arg_4_5, item_type=ItemType.Good, item_id=arg_8_11)
    EnableFlag(arg_12_15)


@RestartOnRest
def Event9530(_, arg_0_3: int, arg_4_5: ushort, arg_8_11: int, arg_12_15: int):
    """ 9530: Event 9530 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(-1, 13304913)
    IfFlagEnabled(-1, 13704191)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(2, 13304913)
    AICommand(3300193, command_id=99, slot=2)
    ReplanAI(3300193)
    SkipLinesIfFlagDisabled(2, 13704191)
    AICommand(3700191, command_id=99, slot=2)
    ReplanAI(3700191)
    IfCharacterHasSpecialEffect(-2, 3300193, arg_0_3)
    IfCharacterHasSpecialEffect(-2, 3700191, arg_0_3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFlagDisabled(2, 13304913)
    AICommand(3300193, command_id=-1, slot=2)
    ReplanAI(3300193)
    SkipLinesIfFlagDisabled(2, 13704191)
    AICommand(3700191, command_id=-1, slot=2)
    ReplanAI(3700191)
    EndIfFlagEnabled(arg_12_15)
    AwardGestureItem(gesture_id=arg_4_5, item_type=ItemType.Good, item_id=arg_8_11)
    EnableFlag(arg_12_15)


@RestartOnRest
def Event9540(_, arg_0_1: ushort, arg_4_7: int, arg_8_11: int):
    """ 9540: Event 9540 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 13804196)
    IfFlagDisabled(1, 13805196)
    IfEntityWithinDistance(1, PLAYER, 3800196, radius=20.0)
    IfHasAIStatus(2, 3800198, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, PLAYER, 3800198, radius=20.0)
    IfPlayerInOwnWorld(3)
    IfHealthLessThanOrEqual(3, PLAYER, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(4, input_condition=-1)
    IfConditionTrue(4, input_condition=3)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFinishedConditionFalse(2, 1)
    AICommand(3800196, command_id=99, slot=2)
    ReplanAI(3800196)
    SkipLinesIfFinishedConditionFalse(2, 2)
    AICommand(3800198, command_id=99, slot=2)
    ReplanAI(3800198)
    Wait(1.0)
    SkipLinesIfFinishedConditionFalse(2, 1)
    AICommand(3800196, command_id=-1, slot=2)
    ReplanAI(3800196)
    SkipLinesIfFinishedConditionFalse(2, 2)
    AICommand(3800198, command_id=-1, slot=2)
    ReplanAI(3800198)
    EndIfFlagEnabled(arg_8_11)
    AwardGestureItem(gesture_id=arg_0_1, item_type=ItemType.Good, item_id=arg_4_7)
    EnableFlag(arg_8_11)


@RestartOnRest
def Event9570(_, arg_0_3: int, arg_4_7: int):
    """ 9570: Event 9570 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, arg_4_7)
    AwardItemLot(arg_0_3, host_only=True)
    Wait(1.5)
    Restart()


def Event9000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 9000: Event 9000 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(-1, arg_4_7)
    IfFlagEnabled(-1, arg_8_11)
    IfFlagEnabled(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    IfFlagEnabled(-2, arg_4_7)
    IfFlagEnabled(-2, arg_8_11)
    IfFlagEnabled(-2, arg_12_15)
    IfConditionFalse(0, input_condition=-2)
    Restart()


def Event9002(_, arg_0_3: int):
    """ 9002: Event 9002 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    EnableFlag(70000050)
    EnableFlag(70000051)
    EnableFlag(70000052)
    EnableFlag(70000053)
    EnableFlag(70000054)
    EnableFlag(70000055)
    EnableFlag(70000056)
    EnableFlag(70000057)
    EnableFlag(70000058)
    EnableFlag(70000059)
    EnableFlag(70000060)
    EnableFlag(70000061)
    EnableFlag(70000062)
    EnableFlag(70000063)
    EnableFlag(70000064)
    EnableFlag(70000065)
    EnableFlag(70000066)
    EnableFlag(70000067)
    EnableFlag(70000068)
    EnableFlag(70000069)
    EnableFlag(70000070)
    EnableFlag(70000071)
    EnableFlag(70000072)
    EnableFlag(70000073)
    EnableFlag(70000074)
    EnableFlag(70000075)
    EnableFlag(70000076)
    EnableFlag(70000077)
    EnableFlag(70000078)
    EnableFlag(70000079)
    EnableFlag(70000080)
    EnableFlag(70000081)
    EnableFlag(70000082)
    EnableFlag(70000083)
    EnableFlag(70000084)
    EnableFlag(70000085)
    EnableFlag(70000086)
    EnableFlag(70000087)
    EnableFlag(70000088)
    EnableFlag(70000089)
    EnableFlag(70000090)
    EnableFlag(70000091)
    EnableFlag(70000092)
    EnableFlag(70000093)
    EnableFlag(70000094)
    EnableFlag(70000095)
    EnableFlag(70000096)
    EnableFlag(70000097)
    EnableFlag(70000098)
    EnableFlag(70000099)
    EnableFlag(70001073)
    Restart()


def Event9004(_, arg_0_3: int):
    """ 9004: Event 9004 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1016)
    IfFlagDisabled(1, 70000052)
    IfFlagEnabled(2, 1036)
    IfFlagDisabled(2, 70000053)
    IfFlagEnabled(3, 1056)
    IfFlagDisabled(3, 70000054)
    IfFlagEnabled(4, 1076)
    IfFlagDisabled(4, 70000055)
    IfFlagEnabled(5, 1096)
    IfFlagDisabled(5, 70000056)
    IfFlagEnabled(6, 1116)
    IfFlagDisabled(6, 70000057)
    IfFlagEnabled(7, 1136)
    IfFlagDisabled(7, 70000058)
    IfFlagEnabled(8, 1156)
    IfFlagDisabled(8, 70000059)
    IfFlagEnabled(9, 1176)
    IfFlagDisabled(9, 70000060)
    IfFlagEnabled(10, 1196)
    IfFlagDisabled(10, 70000061)
    IfFlagEnabled(11, 1216)
    IfFlagDisabled(11, 70000062)
    IfFlagEnabled(12, 1236)
    IfFlagDisabled(12, 70000063)
    IfFlagEnabled(13, 1256)
    IfFlagDisabled(13, 70000064)
    IfFlagEnabled(14, 1276)
    IfFlagDisabled(14, 70000065)
    IfFlagEnabled(15, 1296)
    IfFlagDisabled(15, 70000066)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(-1, input_condition=10)
    IfConditionTrue(-1, input_condition=11)
    IfConditionTrue(-1, input_condition=12)
    IfConditionTrue(-1, input_condition=13)
    IfConditionTrue(-1, input_condition=14)
    IfConditionTrue(-1, input_condition=15)
    IfConditionTrue(0, input_condition=-1)
    ClearMainCondition(0)
    EnableFlag(arg_0_3)
    IfFlagEnabled(1, 1016)
    IfFlagDisabled(1, 70000052)
    IfFlagEnabled(2, 1036)
    IfFlagDisabled(2, 70000053)
    IfFlagEnabled(3, 1056)
    IfFlagDisabled(3, 70000054)
    IfFlagEnabled(4, 1076)
    IfFlagDisabled(4, 70000055)
    IfFlagEnabled(5, 1096)
    IfFlagDisabled(5, 70000056)
    IfFlagEnabled(6, 1116)
    IfFlagDisabled(6, 70000057)
    IfFlagEnabled(7, 1136)
    IfFlagDisabled(7, 70000058)
    IfFlagEnabled(8, 1156)
    IfFlagDisabled(8, 70000059)
    IfFlagEnabled(9, 1176)
    IfFlagDisabled(9, 70000060)
    IfFlagEnabled(10, 1196)
    IfFlagDisabled(10, 70000061)
    IfFlagEnabled(11, 1216)
    IfFlagDisabled(11, 70000062)
    IfFlagEnabled(12, 1236)
    IfFlagDisabled(12, 70000063)
    IfFlagEnabled(13, 1256)
    IfFlagDisabled(13, 70000064)
    IfFlagEnabled(14, 1276)
    IfFlagDisabled(14, 70000065)
    IfFlagEnabled(15, 1296)
    IfFlagDisabled(15, 70000066)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(-1, input_condition=10)
    IfConditionTrue(-1, input_condition=11)
    IfConditionTrue(-1, input_condition=12)
    IfConditionTrue(-1, input_condition=13)
    IfConditionTrue(-1, input_condition=14)
    IfConditionTrue(-1, input_condition=15)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(arg_0_3)
    Restart()


def Event9005(_, arg_0_3: int):
    """ 9005: Event 9005 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1316)
    IfFlagDisabled(1, 70000067)
    IfFlagEnabled(2, 1336)
    IfFlagDisabled(2, 70000068)
    IfFlagEnabled(3, 1356)
    IfFlagDisabled(3, 70000069)
    IfFlagEnabled(4, 1376)
    IfFlagDisabled(4, 70000070)
    IfFlagEnabled(5, 1396)
    IfFlagDisabled(5, 70000071)
    IfFlagEnabled(6, 1416)
    IfFlagDisabled(6, 70000072)
    IfFlagEnabled(7, 1436)
    IfFlagDisabled(7, 70000073)
    IfFlagEnabled(8, 1456)
    IfFlagDisabled(8, 70000074)
    IfFlagEnabled(9, 1476)
    IfFlagDisabled(9, 70000075)
    IfFlagEnabled(10, 1496)
    IfFlagDisabled(10, 70000076)
    IfFlagEnabled(11, 1516)
    IfFlagDisabled(11, 70000077)
    IfFlagEnabled(12, 1536)
    IfFlagDisabled(12, 70000078)
    IfFlagEnabled(13, 1556)
    IfFlagDisabled(13, 70000079)
    IfFlagEnabled(14, 1576)
    IfFlagDisabled(14, 70000080)
    IfFlagEnabled(15, 1596)
    IfFlagDisabled(15, 70000081)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(-1, input_condition=10)
    IfConditionTrue(-1, input_condition=11)
    IfConditionTrue(-1, input_condition=12)
    IfConditionTrue(-1, input_condition=13)
    IfConditionTrue(-1, input_condition=14)
    IfConditionTrue(-1, input_condition=15)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    ClearMainCondition(0)
    IfFlagEnabled(1, 1316)
    IfFlagDisabled(1, 70000067)
    IfFlagEnabled(2, 1336)
    IfFlagDisabled(2, 70000068)
    IfFlagEnabled(3, 1356)
    IfFlagDisabled(3, 70000069)
    IfFlagEnabled(4, 1376)
    IfFlagDisabled(4, 70000070)
    IfFlagEnabled(5, 1396)
    IfFlagDisabled(5, 70000071)
    IfFlagEnabled(6, 1416)
    IfFlagDisabled(6, 70000072)
    IfFlagEnabled(7, 1436)
    IfFlagDisabled(7, 70000073)
    IfFlagEnabled(8, 1456)
    IfFlagDisabled(8, 70000074)
    IfFlagEnabled(9, 1476)
    IfFlagDisabled(9, 70000075)
    IfFlagEnabled(10, 1496)
    IfFlagDisabled(10, 70000076)
    IfFlagEnabled(11, 1516)
    IfFlagDisabled(11, 70000077)
    IfFlagEnabled(12, 1536)
    IfFlagDisabled(12, 70000078)
    IfFlagEnabled(13, 1556)
    IfFlagDisabled(13, 70000079)
    IfFlagEnabled(14, 1576)
    IfFlagDisabled(14, 70000080)
    IfFlagEnabled(15, 1596)
    IfFlagDisabled(15, 70000081)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(-1, input_condition=10)
    IfConditionTrue(-1, input_condition=11)
    IfConditionTrue(-1, input_condition=12)
    IfConditionTrue(-1, input_condition=13)
    IfConditionTrue(-1, input_condition=14)
    IfConditionTrue(-1, input_condition=15)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(arg_0_3)
    Restart()


def Event9006(_, arg_0_3: int):
    """ 9006: Event 9006 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1816)
    IfFlagDisabled(1, 70001073)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    ClearMainCondition(0)
    IfFlagEnabled(1, 1816)
    IfFlagDisabled(1, 70001073)
    IfConditionTrue(-1, input_condition=1)
    IfConditionFalse(0, input_condition=-1)
    DisableFlag(arg_0_3)
    Restart()


def Event9010():
    """ 9010: Event 9010 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(0, 70000061)
    SkipLinesIfFlagDisabled(2, 74000295)
    DisableFlag(74000295)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(2, 74000294)
    DisableFlag(74000294)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(2, 74000293)
    DisableFlag(74000293)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(2, 74000292)
    DisableFlag(74000292)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(2, 74000291)
    DisableFlag(74000291)
    Goto(Label.L20)
    SkipLinesIfFlagDisabled(4, 74000290)
    DisableFlag(74000290)
    SetNetworkConnectedFlagRangeState((1195, 1199), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1195, state=FlagState.On)
    Goto(Label.L20)

    # --- 20 --- #
    DefineLabel(20)
    DisableFlag(70000061)
    Restart()


def Event9011(_, arg_0_3: int):
    """ 9011: Event 9011 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 700)
    IfFlagDisabled(1, 50006020)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L1, 14000110)
    IfFlagEnabled(2, 9307)
    IfFlagEnabled(2, 9309)
    IfFlagEnabled(2, 9314)
    IfFlagEnabled(2, 9318)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    SkipLinesIfFlagEnabled(1, 9307)
    IfFlagEnabled(-1, 9307)
    SkipLinesIfFlagEnabled(1, 9309)
    IfFlagEnabled(-1, 9309)
    SkipLinesIfFlagEnabled(1, 9314)
    IfFlagEnabled(-1, 9314)
    SkipLinesIfFlagEnabled(1, 9318)
    IfFlagEnabled(-1, 9318)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 14000110)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(-2, 50006020)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, -2)
    DisableFlag(arg_0_3)
    Restart()
    EnableFlag(arg_0_3)
    Restart()


def Event9012():
    """ 9012: Event 9012 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2052)
    IfPlayerGender(0, Gender.Male)
    SetNetworkConnectedFlagState(flag=9013, state=FlagState.On)
    IfPlayerGender(0, Gender.Female)
    SetNetworkConnectedFlagState(flag=9013, state=FlagState.Off)
    Restart()


@RestartOnRest
def Event9014():
    """ 9014: Event 9014 """
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, 9014)
    GotoIfFlagDisabled(Label.L0, 13300761)
    DisplayDialog(
        13007000,
        anchor_entity=10000,
        display_distance=0.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 9014)
    EnableFlag(9014)


def Event9015():
    """ 9015: Event 9015 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(70000118)
    IfFlagEnabled(-1, 1124)
    IfFlagEnabled(-1, 1126)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 9303)
    IfFlagEnabled(1, 9314)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(70000118)


@RestartOnRest
def Event9016():
    """ 9016: Event 9016 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(9017)
    IfPlayerClass(0, ClassType.Cleric)
    EnableFlag(9017)
    IfPlayerClass(1, ClassType.Cleric)
    IfConditionFalse(0, input_condition=1)
    Restart()


@RestartOnRest
def Event9018():
    """ 9018: Event 9018 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(73300202)
    IfFlagEnabled(-1, 13204190)
    IfFlagEnabled(-1, 13005710)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(73300202)


@RestartOnRest
def Event9019(_, arg_0_3: int):
    """ 9019: Event 9019 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(-1, 13304192)
    IfFlagEnabled(-1, 13014192)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)


def Event9020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 9020: Event 9020 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagRangeAnyEnabled((arg_4_7, arg_8_11))
    DisableFlag(arg_0_3)
    IfOutsideMap(-1, game_map=(arg_16_16, arg_17_17))
    IfFlagEnabled(-1, 74000013)
    IfFlagEnabled(1, arg_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfOutsideMap(-2, game_map=(arg_16_16, arg_17_17))
    IfFlagEnabled(-2, 74000013)
    IfFlagEnabled(2, arg_12_15)
    IfConditionTrue(2, input_condition=-2)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9080(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """ 9080: Event 9080 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(2052)
    EndIfThisEventSlotFlagEnabled()
    IfPlayerHasItem(1, arg_4_7, item_type=arg_0_0, including_box=True)
    EndIfConditionTrue(1)
    DisableFlag(arg_8_11)


def Event9100(_, arg_0_3: int):
    """ 9100: Event 9100 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, 1103)
    EnableFlag(arg_0_3)
    IfFlagDisabled(0, 1103)
    Restart()


def Event9101(_, arg_0_3: int):
    """ 9101: Event 9101 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfInsideMap(-1, game_map=GRAND_ARCHIVES)
    IfInsideMap(-1, game_map=LOTHRIC_CASTLE)
    IfInsideMap(-1, game_map=FARRON_KEEP)
    IfInsideMap(-1, game_map=CATHEDRAL_OF_THE_DEEP)
    IfConditionTrue(0, input_condition=-1)
    GotoIfInsideMap(Label.L0, GRAND_ARCHIVES)
    GotoIfInsideMap(Label.L1, LOTHRIC_CASTLE)
    GotoIfInsideMap(Label.L2, FARRON_KEEP)
    GotoIfInsideMap(Label.L3, CATHEDRAL_OF_THE_DEEP)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-2, 1128)
    IfConditionTrue(1, input_condition=-2)
    IfFlagDisabled(1, 73500150)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=GRAND_ARCHIVES)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(-3, 1128)
    IfConditionTrue(2, input_condition=-3)
    IfFlagDisabled(2, 73500150)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=LOTHRIC_CASTLE)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(-4, 1124)
    IfFlagEnabled(-4, 1126)
    IfFlagEnabled(-4, 1128)
    IfConditionTrue(3, input_condition=-4)
    IfFlagDisabled(3, 73500150)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=FARRON_KEEP)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(-5, 1124)
    IfFlagEnabled(-5, 1126)
    IfFlagEnabled(-5, 1128)
    IfConditionTrue(4, input_condition=-5)
    IfFlagDisabled(4, 73500150)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=CATHEDRAL_OF_THE_DEEP)
    Restart()


def Event9102(_, arg_0_3: int):
    """ 9102: Event 9102 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfInsideMap(-1, game_map=UNDEAD_SETTLEMENT)
    IfInsideMap(-1, game_map=IRITHYLL)
    IfConditionTrue(0, input_condition=-1)
    GotoIfInsideMap(Label.L0, UNDEAD_SETTLEMENT)
    GotoIfInsideMap(Label.L1, IRITHYLL)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(1, 1202)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=UNDEAD_SETTLEMENT)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(1, 1204)
    EnableFlag(arg_0_3)
    IfOutsideMap(0, game_map=IRITHYLL)
    Restart()


def Event9103(_, arg_0_3: int):
    """ 9103: Event 9103 """
    RestartIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, 1223)
    EnableFlag(arg_0_3)
    IfFlagDisabled(0, 1223)
    Restart()


def Event9104(_, arg_0_3: int):
    """ 9104: Event 9104 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(-1, 1301)
    IfFlagEnabled(-1, 1303)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1295)
    IfFlagDisabled(1, 73101710)
    IfFlagDisabled(1, 73101720)
    IfFlagDisabled(1, 73101730)
    IfFlagDisabled(1, 73101740)
    IfFlagDisabled(1, 73101750)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfFlagEnabled(-2, 1301)
    IfFlagEnabled(-2, 1303)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 1295)
    IfFlagDisabled(2, 73101710)
    IfFlagDisabled(2, 73101720)
    IfFlagDisabled(2, 73101730)
    IfFlagDisabled(2, 73101740)
    IfFlagDisabled(2, 73101750)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9105(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 9105: Event 9105 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    IfFlagEnabled(1, 1341)
    IfFlagDisabled(1, 9311)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagDisabled(Label.L10, 9013)
    EnableFlag(arg_0_3)
    Goto(Label.L20)

    # --- 10 --- #
    DefineLabel(10)
    EnableFlag(arg_4_7)
    Goto(Label.L20)

    # --- 20 --- #
    DefineLabel(20)
    EnableFlag(arg_8_11)
    IfFlagEnabled(2, 1341)
    IfFlagDisabled(2, 9311)
    IfConditionFalse(0, input_condition=2)
    Restart()


@RestartOnRest
def Event9106(_, arg_0_3: int):
    """ 9106: Event 9106 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1130)
    IfFlagDisabled(1, 1138)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfFlagEnabled(2, 1130)
    IfFlagDisabled(2, 1138)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9107(_, arg_0_3: int):
    """ 9107: Event 9107 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1042)
    IfFlagEnabled(1, 1055)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfFlagEnabled(2, 1042)
    IfFlagEnabled(2, 1055)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9108(_, arg_0_3: int):
    """ 9108: Event 9108 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagRangeAnyEnabled(1, (1041, 1042))
    IfFlagEnabled(1, 1055)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfFlagRangeAnyEnabled(2, (1041, 1042))
    IfFlagEnabled(2, 1055)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9109(_, arg_0_3: int):
    """ 9109: Event 9109 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(1, 1042)
    IfFlagEnabled(1, 1055)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfFlagEnabled(2, 1042)
    IfFlagEnabled(2, 1055)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9110(_, arg_0_3: int):
    """ 9110: Event 9110 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagRangeAnyEnabled(2, (1041, 1042))
    IfFlagEnabled(-2, 1058)
    IfFlagEnabled(-2, 1056)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfFlagRangeAnyEnabled(-1, (1043, 1044))
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    IfFlagRangeAnyEnabled(4, (1041, 1042))
    IfFlagEnabled(-4, 1058)
    IfFlagEnabled(-4, 1056)
    IfConditionTrue(4, input_condition=-4)
    IfConditionTrue(-3, input_condition=4)
    IfFlagRangeAnyEnabled(-3, (1043, 1044))
    IfConditionFalse(0, input_condition=-3)
    Restart()


def Event9111(_, arg_0_3: int, arg_4_7: int):
    """ 9111: Event 9111 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    IfFlagEnabled(1, 1347)
    IfFlagEnabled(1, 1355)
    IfFlagEnabled(1, 13700651)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagDisabled(Label.L10, 9013)
    EnableFlag(arg_0_3)
    Goto(Label.L20)

    # --- 10 --- #
    DefineLabel(10)
    EnableFlag(arg_4_7)
    Goto(Label.L20)

    # --- 20 --- #
    DefineLabel(20)
    IfFlagEnabled(2, 1347)
    IfFlagEnabled(2, 1355)
    IfFlagEnabled(2, 13700651)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event9112(_, arg_0_3: int):
    """ 9112: Event 9112 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, 8200)
    EnableFlag(arg_0_3)
    IfFlagDisabled(0, 8200)
    Restart()


def Event9113(_, arg_0_3: int):
    """ 9113: Event 9113 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfInsideMap(1, game_map=DREG_HEAP)
    IfFlagRangeAnyEnabled(1, (1803, 1804))
    IfInsideMap(2, game_map=RINGED_CITY)
    IfFlagEnabled(2, 1811)
    IfInsideMap(3, game_map=(51, 1))
    IfFlagEnabled(3, 1811)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    IfInsideMap(4, game_map=DREG_HEAP)
    IfFlagRangeAnyEnabled(4, (1803, 1804))
    IfInsideMap(5, game_map=RINGED_CITY)
    IfFlagEnabled(5, 1811)
    IfInsideMap(6, game_map=(51, 1))
    IfFlagEnabled(6, 1811)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionFalse(0, input_condition=-2)
    Restart()


def Event9114(_, arg_0_3: int):
    """ 9114: Event 9114 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, 1821)
    EnableFlag(arg_0_3)
    IfFlagDisabled(0, 1821)
    Restart()


@RestartOnRest
def Event9120(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: uint,
    arg_16_16: uchar,
    arg_20_23: uint,
    arg_24_27: int,
):
    """ 9120: Event 9120 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(arg_4_7)
    IfMapNotInCeremony(1, game_map=FIRELINK_SHRINE, ceremony_id=0)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFlagDisabled(-1, arg_0_3)
    SkipLinesIfFlagEnabled(1, 9300)
    IfFlagEnabled(-1, 9300)
    SkipLinesIfFlagEnabled(1, 9301)
    IfFlagEnabled(-1, 9301)
    SkipLinesIfFlagEnabled(1, 9302)
    IfFlagEnabled(-1, 9302)
    SkipLinesIfFlagEnabled(1, 9303)
    IfFlagEnabled(-1, 9303)
    SkipLinesIfFlagEnabled(1, 9304)
    IfFlagEnabled(-1, 9304)
    SkipLinesIfFlagEnabled(1, 9305)
    IfFlagEnabled(-1, 9305)
    SkipLinesIfFlagEnabled(1, 9306)
    IfFlagEnabled(-1, 9306)
    SkipLinesIfFlagEnabled(1, 9307)
    IfFlagEnabled(-1, 9307)
    SkipLinesIfFlagEnabled(1, 9308)
    IfFlagEnabled(-1, 9308)
    SkipLinesIfFlagEnabled(1, 9309)
    IfFlagEnabled(-1, 9309)
    SkipLinesIfFlagEnabled(1, 9311)
    IfFlagEnabled(-1, 9311)
    SkipLinesIfFlagEnabled(1, 9313)
    IfFlagEnabled(-1, 9313)
    SkipLinesIfFlagEnabled(1, 9314)
    IfFlagEnabled(-1, 9314)
    SkipLinesIfFlagEnabled(1, 9315)
    IfFlagEnabled(-1, 9315)
    SkipLinesIfFlagEnabled(1, 9317)
    IfFlagEnabled(-1, 9317)
    SkipLinesIfFlagEnabled(1, 9318)
    IfFlagEnabled(-1, 9318)
    SkipLinesIfFlagEnabled(1, 9319)
    IfFlagEnabled(-1, 9319)
    SkipLinesIfFlagEnabled(1, 9320)
    IfFlagEnabled(-1, 9320)
    SkipLinesIfFlagEnabled(1, 9321)
    IfFlagEnabled(-1, 9321)
    SkipLinesIfFlagEnabled(1, 9322)
    IfFlagEnabled(-1, 9322)
    SkipLinesIfFlagEnabled(1, 9323)
    IfFlagEnabled(-1, 9323)
    SkipLinesIfFlagEnabled(1, 9324)
    IfFlagEnabled(-1, 9324)
    SkipLinesIfFlagEnabled(1, 9325)
    IfFlagEnabled(-1, 9325)
    SkipLinesIfFlagEnabled(1, 9326)
    IfFlagEnabled(-1, 9326)
    SkipLinesIfFlagEnabled(1, 9327)
    IfFlagEnabled(-1, 9327)
    GotoIfValueComparison(Label.L0, ComparisonType.NotEqual, left=arg_24_27, right=1)
    IfFlagRangeAllEnabled(2, (9300, 9309))
    IfFlagEnabled(2, 9311)
    IfFlagRangeAllEnabled(2, (9313, 9315))
    IfFlagRangeAllEnabled(2, (9317, 9321))
    SkipLinesIfFlagDisabled(1, 6951)
    IfFlagRangeAllEnabled(2, (9322, 9323))
    SkipLinesIfFlagDisabled(1, 6952)
    IfFlagRangeAllEnabled(2, (9324, 9327))
    IfConditionTrue(-1, input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFlagDisabled(arg_0_3)
    IncrementEventValue(arg_8_11, bit_count=arg_12_15, max_value=arg_20_23)
    IfEventValueEqual(-2, arg_8_11, bit_count=arg_16_16, value=arg_20_23)
    RestartIfConditionFalse(-2)
    EnableFlag(arg_4_7)


def Event690(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """ 690: Event 690 """
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfFlagEnabled(0, arg_12_15)
    SkipLinesIfFlagEnabled(1, 2)
    IfFlagEnabled(-1, 2)
    SkipLinesIfFlagEnabled(1, 3)
    IfFlagEnabled(-1, 3)
    SkipLinesIfFlagEnabled(1, 4)
    IfFlagEnabled(-1, 4)
    SkipLinesIfFlagEnabled(1, 5)
    IfFlagEnabled(-1, 5)
    SkipLinesIfFlagEnabled(1, 6)
    IfFlagEnabled(-1, 6)
    SkipLinesIfFlagEnabled(1, 7)
    IfFlagEnabled(-1, 7)
    SkipLinesIfFlagEnabled(1, 8)
    IfFlagEnabled(-1, 8)
    SkipLinesIfFlagEnabled(1, 9)
    IfFlagEnabled(-1, 9)
    SkipLinesIfFlagEnabled(1, 10)
    IfFlagEnabled(-1, 10)
    SkipLinesIfFlagEnabled(1, 11)
    IfFlagEnabled(-1, 11)
    SkipLinesIfFlagEnabled(1, 12)
    IfFlagEnabled(-1, 12)
    SkipLinesIfFlagEnabled(1, 13)
    IfFlagEnabled(-1, 13)
    SkipLinesIfFlagEnabled(1, 14)
    IfFlagEnabled(-1, 14)
    SkipLinesIfFlagEnabled(1, 15)
    IfFlagEnabled(-1, 15)
    IfConditionTrue(0, input_condition=-1)
    IncrementEventValue(arg_0_3, bit_count=arg_4_7, max_value=arg_8_11)
    Restart()


def Event840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 840: Event 840 """
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfFlagEnabled(2, 844)
    SkipLinesIfFlagEnabled(1, 847)
    RotateToFaceEntity(PLAYER, arg_8_11, animation=-1, wait_for_completion=False)
    ForceAnimation(PLAYER, arg_4_7)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=123456789)
    Wait(4.0)
    SkipLinesIfValueEqual(1, left=arg_12_15, right=-1)
    ForceAnimation(PLAYER, arg_12_15, loop=True)
    Restart()


def Event870(_, arg_0_0: uchar, arg_4_7: int):
    """ 870: Event 870 """
    IfPlayerCovenant(0, arg_0_0)
    EnableFlag(arg_4_7)
    IfPlayerCovenant(1, arg_0_0)
    IfConditionFalse(0, input_condition=1)
    DisableFlag(arg_4_7)
    Restart()
