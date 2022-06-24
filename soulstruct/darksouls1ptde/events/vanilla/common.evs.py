"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    EndIfClient()
    DisableFlag(760)
    DisableFlag(762)
    DisableFlag(765)
    Event_260(0, 11810000, 10010600, 0.0)
    Event_260(1, 257, 10010610, 0.0)
    Event_260(2, 710, 10010620, 0.0)
    Event_761()
    Event_763()
    Event_290()
    Event_701()
    Event_702()
    Event_717()
    Event_718()
    Event_706()
    Event_740()
    Event_750()
    Event_752()
    Event_757()
    Event_758()
    Event_759()
    Event_754()
    Event_770()
    Event_772()
    Event_730()
    Event_731()
    Event_766()
    Event_710()
    Event_711(0, 2500, 711)
    Event_711(1, 2501, 712)
    Event_711(2, 2502, 713)
    Event_711(3, 2504, 714)
    Event_715()
    Event_716()
    Event_8131(0, 202, 203)
    Event_8131(1, 204, 205)
    Event_8131(2, 206, 207)
    Event_8131(3, 208, 209)
    Event_8131(4, 210, 211)
    Event_8131(5, 212, 213)
    Event_8131(6, 214, 215)
    Event_819()
    Event_970(0, 2, 2500, 9020, 9030)
    Event_970(1, 11010901, 0, 9000, 9030)
    Event_970(2, 11010902, 2510, 9000, 9030)
    Event_970(3, 3, 0, 9020, 0)
    Event_970(4, 4, 2520, 9020, 0)
    Event_970(5, 11200900, 2530, 9000, 0)
    Event_970(6, 5, 2540, 9000, 9030)
    Event_970(7, 6, 2550, 9000, 9030)
    Event_970(8, 7, 2560, 9000, 0)
    Event_970(9, 9, 2570, 9020, 0)
    Event_970(10, 11410900, 0, 9000, 9030)
    Event_970(11, 11410410, 0, 9000, 0)
    Event_970(12, 11410901, 0, 9000, 9030)
    Event_970(13, 10, 2580, 9000, 0)
    Event_970(14, 11, 2590, 9000, 0)
    Event_970(15, 11510900, 2600, 0, 0)
    Event_970(16, 11510902, 2610, 9000, 0)
    Event_970(17, 11510903, 2620, 9000, 0)
    Event_970(18, 13, 2630, 9010, 0)
    Event_970(19, 14, 2640, 9000, 0)
    Event_970(20, 15, 2650, 0, 0)
    Event_970(21, 16, 2660, 9000, 0)
    Event_970(22, 11810900, 0, 9000, 9030)
    Event_970(23, 11210000, 2680, 9000, 0)
    Event_970(24, 11210001, 2690, 0, 0)
    Event_970(25, 17, 2700, 9040, 0)
    Event_970(26, 11210004, 2710, 0, 0)
    Event_250(0, 2600, 250)
    Event_250(1, 2601, 251)
    Event_250(2, 2602, 252)
    Event_250(3, 2603, 253)
    Event_250(4, 2604, 254)
    Event_250(5, 2605, 255)
    Event_250(6, 2606, 256)
    Event_250(7, 2607, 257)
    Event_250(8, 2608, 258)
    Event_250(9, 2609, 259)
    Event_350(0, 350, 800)
    Event_350(1, 351, 801)
    Event_350(2, 352, 802)
    Event_350(6, 356, 806)
    Event_350(7, 357, 807)
    Event_350(8, 358, 808)
    Event_350(9, 359, 809)
    Event_350(10, 360, 810)
    Event_350(12, 362, 812)
    Event_350(13, 363, 813)
    Event_780(0, 1000, 780)
    Event_780(1, 1010, 781)
    Event_780(2, 1020, 782)
    Event_780(3, 1030, 783)
    Event_780(4, 1040, 784)
    Event_780(5, 1050, 785)
    Event_780(6, 1060, 786)
    Event_780(7, 1070, 787)
    Event_780(8, 1080, 788)
    Event_780(9, 1090, 789)
    Event_780(10, 1100, 790)
    Event_780(11, 1110, 791)
    Event_780(12, 1120, 792)
    Event_780(13, 1130, 793)
    Event_870(0, 0, 850)
    Event_870(1, 1, 851)
    Event_870(2, 2, 852)
    Event_870(3, 3, 853)
    Event_870(4, 4, 854)
    Event_870(5, 5, 855)
    Event_870(6, 6, 856)
    Event_870(7, 7, 857)
    Event_870(8, 8, 858)
    Event_870(9, 9, 859)
    Event_840(0, 840, 7905, 6370, -1)
    Event_840(1, 841, 7905, 6072, -1)
    Event_840(2, 842, 7905, 6080, -1)
    Event_840(3, 843, 7905, 6001, -1)
    Event_840(4, 844, 7898, 10000, 7896)
    Event_840(5, 845, 7905, 6340, -1)
    Event_840(6, 846, 7905, 6341, -1)
    Event_840(7, 847, 7913, 10000, 7911)
    Event_840(8, 848, 7905, 6380, -1)
    Event_840(9, 849, 7905, 1400700, -1)
    Event_690(0, 600, 4, 16, 1175)
    Event_719()
    Event_720()
    Event_721()
    Event_722()
    Event_723()
    Event_724()
    Event_725()
    Event_726()
    Event_727()
    Event_745()
    Event_818()
    Event_810()
    Event_812(0, 51400350)
    Event_812(1, 51010050)
    Event_822()
    Event_823()
    Event_910(0, 11400591, 1280)
    Event_911(0, 11010591, 1000, 1)
    Event_911(1, 11510590, 1010, 1)
    Event_911(2, 11700591, 1020, 1)
    Event_911(3, 11000591, 1030, 1)
    Event_911(4, 11400590, 1040, 1)
    Event_911(5, 11410594, 1050, 1)
    Event_911(6, 11020594, 1060, 1)
    Event_911(7, 11020595, 1070, 1)
    Event_911(8, 11810590, 1082, 1)
    Event_911(9, 11810591, 1080, 1)
    Event_911(10, 11510592, 1090, 1)
    Event_911(11, 11600592, 1100, 1)
    Event_911(12, 11020602, 1110, 1)
    Event_911(13, 11010594, 1120, 1)
    Event_911(14, 11010595, 1130, 1)
    Event_911(15, 11020599, 1140, 1)
    Event_911(16, 11020607, 1150, 1)
    Event_911(17, 11200592, 1160, 1)
    Event_911(18, 11200593, 1170, 1)
    Event_911(19, 11200594, 1180, 1)
    Event_911(20, 11300590, 1190, 1)
    Event_911(21, 11300591, 1200, 1)
    Event_911(22, 11310590, 1210, 1)
    Event_911(23, 11310592, 1220, 1)
    Event_911(24, 11310593, 1230, 1)
    Event_911(25, 11310594, 1240, 1)
    Event_911(26, 11320590, 1250, 1)
    Event_911(27, 11320581, 1260, 1)
    Event_911(28, 11320593, 1270, 1)
    Event_911(29, 11400592, 1290, 1)
    Event_911(30, 11400594, 1300, 1)
    Event_911(31, 11400596, 1310, 1)
    Event_911(32, 11400597, 1320, 1)
    Event_911(33, 11400598, 1330, 1)
    Event_911(34, 11400599, 1340, 1)
    Event_911(35, 11510595, 1350, 1)
    Event_911(36, 11510596, 1360, 1)
    Event_911(37, 11510597, 1370, 1)
    Event_911(38, 11600594, 1380, 1)
    Event_911(39, 11600595, 1390, 1)
    Event_911(40, 11600596, 1400, 1)
    Event_911(41, 11010598, 1410, 0)
    Event_911(42, 11210590, 1500, 1)
    Event_911(43, 11210593, 1510, 1)
    Event_911(44, 11210594, 1520, 1)
    Event_911(45, 11600580, 1401, 1)
    Event_911(46, 11600581, 1402, 1)
    Event_911(47, 11600582, 1403, 1)
    Event_911(48, 11600583, 1404, 1)
    Event_890(0, 11310580, 1221, 1)
    Event_890(1, 11510580, 1361, 1)
    Event_890(2, 11510581, 1371, 1)
    Event_890(3, 11320592, 1261, 1)
    Event_960(0, 1322, 6190, 6190)
    Event_960(1, 1315, 6180, 1100)
    Event_960(2, 1402, 6230, 6230)
    Event_960(3, 1402, 6230, 6231)
    Event_8200(0, 3, 5500, 50000120, 11010594)
    Event_8200(1, 3, 5510, 50000130, 11010595)
    Event_8200(2, 2, 103, 50000160, 11200592)
    Event_8200(3, 3, 240, 50000170, 11200593)
    Event_8200(4, 2, 124, 50000180, 11200594)
    Event_8200(5, 0, 453000, 50000220, 11310592)
    Event_8200(6, 3, 5100, 50000225, 11310580)
    Event_8200(7, 3, 5110, 50000230, 11310593)
    Event_8200(8, 3, 114, 50000265, 11320581)
    Event_8200(9, 3, 377, 50000260, 11320592)
    Event_8200(10, 3, 378, 50000270, 11320593)
    Event_8200(11, 3, 4500, 50000310, 11400596)
    Event_8200(12, 3, 4520, 50000320, 11400597)
    Event_8200(13, 3, 4510, 50000330, 11400598)
    Event_8200(14, 2, 130, 50000350, 11510595)
    Event_8200(15, 3, 113, 50000360, 11510596)
    Event_8200(16, 2, 102, 50000365, 11510580)
    Event_8200(17, 3, 5910, 50000370, 11510597)
    Event_8200(18, 0, 1366000, 50000375, 11510581)
    Event_8200(19, 0, 904000, 50000380, 11600594)
    Event_8200(20, 3, 102, 50000390, 11600595)
    Event_8200(21, 0, 210000, 50000400, 11600596)
    Event_8200(22, 1, 40000, 50000410, 11600580)
    Event_8200(23, 1, 41000, 50000420, 11600581)
    Event_8200(24, 1, 42000, 50000430, 11600582)
    Event_8200(25, 1, 43000, 50000440, 11600583)
    Event_8300(0, 3, 100, 50000000)
    Event_8300(1, 3, 101, 51100330)
    Event_8300(2, 3, 102, 50000390)
    Event_8300(3, 3, 106, 11017020)
    Event_8300(4, 3, 108, 11607020)
    Event_8300(5, 3, 112, 11407080)
    Event_8300(6, 3, 2508, 11007010)
    Event_8090(0, 3, 510, 11217010)
    Event_8090(1, 3, 511, 11217020)
    Event_8090(2, 3, 512, 11217030)
    Event_8090(3, 3, 513, 11217040)
    Event_8090(4, 3, 514, 11217050)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    SkipLinesIfFlagEnabled(80, 909)
    SkipLinesIfFlagRangeAnyEnabled(1, (1000, 1029))
    EnableFlag(1000)
    SkipLinesIfFlagRangeAnyEnabled(1, (1030, 1059))
    EnableFlag(1030)
    SkipLinesIfFlagRangeAnyEnabled(1, (1060, 1089))
    EnableFlag(1060)
    SkipLinesIfFlagRangeAnyEnabled(1, (1090, 1109))
    EnableFlag(1090)
    SkipLinesIfFlagRangeAnyEnabled(1, (1110, 1119))
    EnableFlag(1110)
    SkipLinesIfFlagRangeAnyEnabled(1, (1120, 1139))
    EnableFlag(1120)
    SkipLinesIfFlagRangeAnyEnabled(1, (1140, 1169))
    EnableFlag(1140)
    SkipLinesIfFlagRangeAnyEnabled(1, (1170, 1189))
    EnableFlag(1170)
    SkipLinesIfFlagRangeAnyEnabled(1, (1190, 1209))
    EnableFlag(1202)
    SkipLinesIfFlagRangeAnyEnabled(1, (1210, 1219))
    EnableFlag(1210)
    SkipLinesIfFlagRangeAnyEnabled(1, (1220, 1229))
    EnableFlag(1220)
    SkipLinesIfFlagRangeAnyEnabled(1, (1230, 1239))
    EnableFlag(1230)
    SkipLinesIfFlagRangeAnyEnabled(1, (1240, 1249))
    EnableFlag(1240)
    SkipLinesIfFlagRangeAnyEnabled(1, (1250, 1259))
    EnableFlag(1250)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    SkipLinesIfFlagRangeAnyEnabled(1, (1280, 1289))
    EnableFlag(1280)
    SkipLinesIfFlagRangeAnyEnabled(1, (1290, 1309))
    EnableFlag(1290)
    SkipLinesIfFlagRangeAnyEnabled(1, (1310, 1319))
    EnableFlag(1310)
    SkipLinesIfFlagRangeAnyEnabled(1, (1320, 1339))
    EnableFlag(1320)
    SkipLinesIfFlagRangeAnyEnabled(1, (1340, 1359))
    EnableFlag(1340)
    SkipLinesIfFlagRangeAnyEnabled(1, (1360, 1379))
    EnableFlag(1360)
    SkipLinesIfFlagRangeAnyEnabled(1, (1380, 1399))
    EnableFlag(1380)
    SkipLinesIfFlagRangeAnyEnabled(1, (1400, 1409))
    EnableFlag(1400)
    SkipLinesIfFlagRangeAnyEnabled(1, (1410, 1419))
    EnableFlag(1410)
    SkipLinesIfFlagRangeAnyEnabled(1, (1420, 1429))
    EnableFlag(1420)
    SkipLinesIfFlagRangeAnyEnabled(1, (1430, 1459))
    EnableFlag(1430)
    SkipLinesIfFlagRangeAnyEnabled(1, (1460, 1489))
    EnableFlag(1460)
    SkipLinesIfFlagRangeAnyEnabled(1, (1490, 1539))
    EnableFlag(1490)
    SkipLinesIfFlagRangeAnyEnabled(1, (1540, 1569))
    EnableFlag(1540)
    SkipLinesIfFlagRangeAnyEnabled(1, (1570, 1599))
    EnableFlag(1570)
    SkipLinesIfFlagRangeAnyEnabled(1, (1600, 1619))
    EnableFlag(1600)
    SkipLinesIfFlagRangeAnyEnabled(1, (1620, 1639))
    EnableFlag(1620)
    SkipLinesIfFlagRangeAnyEnabled(1, (1640, 1669))
    EnableFlag(1640)
    SkipLinesIfFlagRangeAnyEnabled(1, (1670, 1679))
    EnableFlag(1670)
    SkipLinesIfFlagRangeAnyEnabled(1, (1690, 1699))
    EnableFlag(1690)
    SkipLinesIfFlagRangeAnyEnabled(1, (1700, 1709))
    EnableFlag(1700)
    SkipLinesIfFlagRangeAnyEnabled(1, (1710, 1729))
    EnableFlag(1710)
    SkipLinesIfFlagRangeAnyEnabled(1, (1760, 1769))
    EnableFlag(1760)
    SkipLinesIfFlagRangeAnyEnabled(1, (1770, 1779))
    EnableFlag(1770)
    SkipLinesIfFlagRangeAnyEnabled(1, (1780, 1789))
    EnableFlag(1780)
    SkipLinesIfFlagRangeAnyEnabled(1, (1820, 1839))
    EnableFlag(1820)
    SkipLinesIfFlagRangeAnyEnabled(1, (1840, 1859))
    EnableFlag(1840)
    SkipLinesIfFlagRangeAnyEnabled(1, (1860, 1869))
    EnableFlag(1860)
    SkipLinesIfFlagRangeAnyEnabled(1, (1870, 1889))
    EnableFlag(1870)
    SkipLinesIfFlagEnabled(24, 909)
    EnableFlag(11807020)
    EnableFlag(11807030)
    EnableFlag(11807040)
    EnableFlag(11807050)
    EnableFlag(11807060)
    EnableFlag(11807070)
    EnableFlag(11807080)
    EnableFlag(11807090)
    EnableFlag(11807100)
    EnableFlag(11807110)
    EnableFlag(11807120)
    EnableFlag(11807130)
    EnableFlag(11807170)
    EnableFlag(11807180)
    EnableFlag(11807190)
    EnableFlag(11807200)
    EnableFlag(11807210)
    EnableFlag(11807220)
    EnableFlag(11807230)
    EnableFlag(11807240)
    EnableFlag(11217060)
    EnableFlag(11217070)
    EnableFlag(11217080)
    EnableFlag(11217090)
    SkipLinesIfFlagEnabled(4, 909)
    EnableFlag(909)
    EnableFlag(814)
    EnableFlag(50006071)
    EnableFlag(50006080)


@NeverRestart(290)
def Event_290():
    """Event 290"""
    EndIfThisEventFlagEnabled()
    EnableFlagRange((280, 290))
    IfPlayerClass(-1, ClassType.Knight)
    IfPlayerClass(-1, ClassType.Cleric)
    IfConditionTrue(1, input_condition=-1)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisableFlag(287)
    End()
    DisableFlag(288)


@NeverRestart(701)
def Event_701():
    """Event 701"""
    EndIfThisEventFlagEnabled()
    EnableVagrantSpawning()
    IfInsideMap(0, game_map=UNDEAD_ASYLUM)
    DisableVagrantSpawning()
    IfFlagEnabled(0, 11810000)
    EnableVagrantSpawning()


@NeverRestart(702)
def Event_702():
    """Event 702"""
    DisableFlag(702)
    IfFlagDisabled(1, 11800210)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(702)
    IfOutsideMap(-1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagEnabled(-1, 11800210)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(702)
    Restart()


@NeverRestart(717)
def Event_717():
    """Event 717"""
    DisableFlag(717)
    IfFlagDisabled(1, 710)
    IfInsideMap(1, game_map=NEW_LONDO_RUINS)
    IfStandingOnCollision(1, 1603300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(717)
    IfStandingOnCollision(2, 1603300)
    IfConditionFalse(0, input_condition=2)
    DisableFlag(717)
    Restart()


@NeverRestart(718)
def Event_718():
    """Event 718"""
    EndIfFlagDisabled(8120)
    DisplayStatus(10010650)
    DisableFlag(8120)


@NeverRestart(706)
def Event_706():
    """Event 706"""
    IfFlagEnabled(0, 710)
    EnableFlag(706)
    IfFlagEnabled(-1, 11705170)
    IfInsideMap(-1, game_map=PAINTED_WORLD)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(706)
    IfFlagDisabled(1, 11705170)
    IfOutsideMap(1, game_map=PAINTED_WORLD)
    IfConditionTrue(0, input_condition=1)
    Restart()


@NeverRestart(710)
def Event_710():
    """Event 710"""
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(0, 2510)
    EnableFlag(710)


@NeverRestart(711)
def Event_711(_, arg_0_3: int, arg_4_7: int):
    """Event 711"""
    EndIfThisEventSlotFlagEnabled()
    IfPlayerHasGood(0, arg_0_3)
    EnableFlag(arg_4_7)


@NeverRestart(715)
def Event_715():
    """Event 715"""
    DisableFlag(715)
    IfFlagEnabled(1, 11010595)
    IfPlayerHasGood(1, 702)
    IfPlayerDoesNotHaveGood(1, 5520, including_storage=True)
    IfPlayerCovenant(1, Covenant.WarriorOfSunlight)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(715)
    IfPlayerDoesNotHaveGood(-1, 702)
    IfPlayerHasGood(-1, 5520, including_storage=True)
    IfPlayerCovenant(2, Covenant.WarriorOfSunlight)
    IfConditionFalse(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(716)
def Event_716():
    """Event 716"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 50000082)
    EnableFlag(716)


@NeverRestart(8131)
def Event_8131(_, arg_0_3: int, arg_4_7: int):
    """Event 8131"""
    EndIfThisEventSlotFlagEnabled()
    IfPlayerHasGood(-1, arg_0_3)
    IfPlayerHasGood(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=202)
    EnableFlag(8131)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=204)
    EnableFlagRange((8131, 8132))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=206)
    EnableFlagRange((8131, 8133))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=208)
    EnableFlagRange((8131, 8134))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=210)
    EnableFlagRange((8131, 8135))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=212)
    EnableFlagRange((8131, 8136))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=214)
    EnableFlagRange((8131, 8137))


@NeverRestart(819)
def Event_819():
    """Event 819"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 11017040)
    IfFlagEnabled(-1, 11017170)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11017040)
    EnableFlag(11017170)


@NeverRestart(719)
def Event_719():
    """Event 719"""
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(-1, 3000)
    IfPlayerHasGood(-1, 3010)
    IfPlayerHasGood(-1, 3020)
    IfPlayerHasGood(-1, 3030)
    IfPlayerHasGood(-1, 3040)
    IfPlayerHasGood(-1, 3050)
    IfPlayerHasGood(-1, 3060)
    IfPlayerHasGood(-1, 3070)
    IfPlayerHasGood(-1, 3100)
    IfPlayerHasGood(-1, 3110)
    IfPlayerHasGood(-1, 3120)
    IfPlayerHasGood(-1, 3300)
    IfPlayerHasGood(-1, 3310)
    IfPlayerHasGood(-1, 3400)
    IfPlayerHasGood(-1, 3410)
    IfPlayerHasGood(-1, 3500)
    IfPlayerHasGood(-1, 3510)
    IfPlayerHasGood(-1, 3520)
    IfPlayerHasGood(-1, 3530)
    IfPlayerHasGood(-1, 3540)
    IfPlayerHasGood(-1, 3550)
    IfPlayerHasGood(-1, 3600)
    IfPlayerHasGood(-1, 3610)
    IfPlayerHasGood(-1, 3700)
    IfPlayerHasGood(-1, 4000)
    IfPlayerHasGood(-1, 4010)
    IfPlayerHasGood(-1, 4020)
    IfPlayerHasGood(-1, 4030)
    IfPlayerHasGood(-1, 4040)
    IfPlayerHasGood(-1, 4050)
    IfPlayerHasGood(-1, 4060)
    IfPlayerHasGood(-1, 4100)
    IfPlayerHasGood(-1, 4110)
    IfPlayerHasGood(-1, 4200)
    IfPlayerHasGood(-1, 4210)
    IfPlayerHasGood(-1, 4220)
    IfPlayerHasGood(-1, 4300)
    IfPlayerHasGood(-1, 4310)
    IfPlayerHasGood(-1, 4360)
    IfPlayerHasGood(-1, 4400)
    IfPlayerHasGood(-1, 4500)
    IfPlayerHasGood(-1, 4510)
    IfPlayerHasGood(-1, 4520)
    IfPlayerHasGood(-1, 5000)
    IfPlayerHasGood(-1, 5010)
    IfPlayerHasGood(-1, 5020)
    IfPlayerHasGood(-1, 5030)
    IfPlayerHasGood(-1, 5040)
    IfPlayerHasGood(-1, 5050)
    IfPlayerHasGood(-1, 5100)
    IfPlayerHasGood(-1, 5110)
    IfPlayerHasGood(-1, 5200)
    IfPlayerHasGood(-1, 5210)
    IfPlayerHasGood(-1, 5300)
    IfPlayerHasGood(-1, 5310)
    IfPlayerHasGood(-1, 5320)
    IfPlayerHasGood(-1, 5400)
    IfPlayerHasGood(-1, 5500)
    IfPlayerHasGood(-1, 5510)
    IfPlayerHasGood(-1, 5520)
    IfPlayerHasGood(-1, 5600)
    IfPlayerHasGood(-1, 5610)
    IfPlayerHasGood(-1, 5700)
    IfPlayerHasGood(-1, 5710)
    IfPlayerHasGood(-1, 5800)
    IfPlayerHasGood(-1, 5810)
    IfPlayerHasGood(-1, 5900)
    IfPlayerHasGood(-1, 5910)
    IfPlayerHasGood(-1, 3710)
    IfPlayerHasGood(-1, 3720)
    IfPlayerHasGood(-1, 3730)
    IfPlayerHasGood(-1, 3740)
    IfPlayerHasGood(-1, 4530)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(719)


@NeverRestart(720)
def Event_720():
    """Event 720"""
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(-1, 4020)
    IfPlayerHasGood(-1, 4030)
    IfPlayerHasGood(-1, 4040)
    IfPlayerHasGood(-1, 4060)
    IfPlayerHasGood(-1, 4110)
    IfPlayerHasGood(-1, 4500)
    IfPlayerHasGood(-1, 4510)
    IfPlayerHasGood(-1, 4520)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11020102)


@NeverRestart(730)
def Event_730():
    """Event 730"""
    IfFlagDisabled(1, 732)
    IfFlagEnabled(1, 8000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(732)
    EnableFlag(735)
    Restart()


@NeverRestart(731)
def Event_731():
    """Event 731"""
    IfFlagDisabled(0, 8000)
    DisableFlag(732)
    DisableFlag(735)
    IfFlagEnabled(0, 8000)
    Restart()


@NeverRestart(250)
def Event_250(_, arg_0_3: int, arg_4_7: int):
    """Event 250"""
    EndIfThisEventSlotFlagEnabled()
    IfPlayerHasGood(0, arg_0_3)
    EnableFlag(arg_4_7)


@NeverRestart(350)
def Event_350(_, arg_0_3: int, arg_4_7: int):
    """Event 350"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    IfPlayerHasGood(1, arg_4_7)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, arg_0_3)
    RemoveGoodFromPlayer(item=arg_4_7, quantity=1)


@NeverRestart(780)
def Event_780(_, arg_0_3: int, arg_4_7: int):
    """Event 780"""
    DisableFlag(arg_4_7)
    IfPlayerHasGood(0, arg_0_3)
    EnableFlag(arg_4_7)
    IfPlayerDoesNotHaveGood(0, arg_0_3)
    Restart()


@NeverRestart(870)
def Event_870(_, arg_0_0: uchar, arg_4_7: int):
    """Event 870"""
    IfPlayerCovenant(0, arg_0_0)
    EnableFlag(arg_4_7)
    IfPlayerCovenant(1, arg_0_0)
    IfConditionFalse(0, input_condition=1)
    DisableFlag(arg_4_7)
    Restart()


@NeverRestart(260)
def Event_260(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """Event 260"""
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    Wait(arg_8_11)
    DisplayStatus(arg_4_7)


@NeverRestart(970)
def Event_970(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 970"""
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfEqual(1, left=arg_4_7, right=0)
    AwardItemLot(arg_4_7, host_only=True)
    DisableNetworkSync()
    Wait(5.0)
    SkipLinesIfEqual(1, left=arg_8_11, right=0)
    AwardItemLot(arg_8_11, host_only=True)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    AwardItemLot(arg_12_15, host_only=True)


@NeverRestart(911)
def Event_911(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar):
    """Event 911"""
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    SetFlagState(arg_0_3, arg_8_8)
    EndIfFlagEnabled(arg_0_3)
    Restart()


@NeverRestart(890)
def Event_890(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar):
    """Event 890"""
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    SetFlagState(arg_0_3, arg_8_8)
    EndIfFlagEnabled(arg_0_3)
    Restart()


@NeverRestart(960)
def Event_960(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 960"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfCharacterDead(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(arg_8_11, host_only=True)


@NeverRestart(8200)
def Event_8200(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 8200"""
    EndIfFlagEnabled(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_storage=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)
    EnableFlag(arg_12_15)


@NeverRestart(8300)
def Event_8300(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """Event 8300"""
    EndIfFlagEnabled(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_storage=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)


@NeverRestart(8090)
def Event_8090(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """Event 8090"""
    EndIfFlagEnabled(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_storage=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)


@NeverRestart(910)
def Event_910(_, arg_0_3: int, arg_4_7: int):
    """Event 910"""
    SkipLinesIfFlagEnabled(2, arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    IfFlagDisabled(0, arg_0_3)
    Restart()


@NeverRestart(690)
def Event_690(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """Event 690"""
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


@NeverRestart(721)
def Event_721():
    """Event 721"""
    EndIfFlagEnabled(728)
    IfFlagEnabled(1, 11707000)
    IfFlagEnabled(1, 11707010)
    IfFlagEnabled(1, 11707020)
    IfFlagEnabled(1, 11707030)
    IfFlagEnabled(1, 11707040)
    IfFlagEnabled(1, 11707050)
    IfFlagEnabled(1, 11707060)
    IfFlagEnabled(1, 11707070)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(721)
    IfFlagEnabled(2, 11707090)
    IfFlagEnabled(2, 11707100)
    IfFlagEnabled(2, 11707110)
    IfConditionTrue(0, input_condition=2)
    EnableFlag(728)


@NeverRestart(722)
def Event_722():
    """Event 722"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11407120)
    IfFlagEnabled(1, 11407130)
    IfFlagEnabled(1, 11407150)
    IfFlagEnabled(1, 11407160)
    IfFlagEnabled(1, 11407170)
    IfFlagEnabled(1, 11407140)
    IfFlagEnabled(1, 11407180)
    IfFlagEnabled(1, 11407190)
    IfFlagEnabled(1, 10)
    IfPlayerHasWeapon(1, 1332500)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(722)


@NeverRestart(723)
def Event_723():
    """Event 723"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11027130)
    IfFlagEnabled(1, 11027140)
    IfFlagEnabled(1, 11027150)
    IfFlagEnabled(1, 11027160)
    IfFlagEnabled(1, 11027170)
    IfFlagEnabled(1, 11027180)
    IfFlagEnabled(1, 11027190)
    IfFlagEnabled(1, 11027200)
    IfFlagEnabled(1, 11027210)
    IfFlagEnabled(1, 11027220)
    IfFlagEnabled(1, 11027230)
    IfFlagEnabled(1, 11027240)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(723)


@NeverRestart(724)
def Event_724():
    """Event 724"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11017050)
    IfFlagEnabled(1, 11017060)
    IfFlagEnabled(1, 11017070)
    IfFlagEnabled(1, 11017080)
    IfFlagEnabled(1, 11017090)
    IfFlagEnabled(1, 11017100)
    IfFlagEnabled(1, 11017110)
    IfFlagEnabled(1, 11017120)
    IfFlagEnabled(1, 11017130)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(724)


@NeverRestart(725)
def Event_725():
    """Event 725"""
    EndIfThisEventFlagEnabled()
    IfTrueFlagCountGreaterThanOrEqual(0, FlagType.Absolute, flag_range=(11707100, 11707190), value=2)
    EnableFlag(725)


@NeverRestart(726)
def Event_726():
    """Event 726"""
    EndIfThisEventFlagEnabled()
    IfTrueFlagCountGreaterThanOrEqual(0, FlagType.Absolute, flag_range=(11607000, 11607090), value=2)
    EnableFlag(726)


@NeverRestart(727)
def Event_727():
    """Event 727"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11327000)
    IfFlagEnabled(1, 11327010)
    IfFlagEnabled(1, 11327020)
    IfFlagEnabled(1, 11327030)
    IfFlagEnabled(1, 11327040)
    IfFlagEnabled(1, 11327050)
    IfFlagEnabled(1, 11327060)
    IfFlagEnabled(1, 11327070)
    IfFlagEnabled(1, 11327080)
    IfFlagEnabled(1, 11327090)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(727)


@NeverRestart(740)
def Event_740():
    """Event 740"""
    IfPlayerClass(0, ClassType.Pyromancer)
    EnableFlag(740)


@NeverRestart(745)
def Event_745():
    """Event 745"""
    IfFlagEnabled(7, 1604)
    IfFlagEnabled(7, 1764)
    SkipLinesIfConditionFalse(1, 7)
    IfFlagEnabled(0, 703)
    SkipLinesIfFlagEnabled(1, 1604)
    IfFlagEnabled(-1, 1604)
    SkipLinesIfFlagEnabled(1, 1764)
    IfFlagEnabled(-1, 1764)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    End()


@NeverRestart(754)
def Event_754():
    """Event 754"""
    DisableFlag(754)
    IfFlagEnabled(0, 754)
    DisableFlag(754)
    AddSpecialEffect(PLAYER, 4600)
    AddSpecialEffect(PLAYER, 4601)
    CreateTemporaryVFX(vfx_id=22715, anchor_entity=PLAYER, model_point=7, anchor_type=CoordEntityType.Character)
    Restart()


@NeverRestart(770)
def Event_770():
    """Event 770"""
    IfFlagEnabled(0, 755)
    DisableFlag(755)
    DisableFlag(742)
    DisableFlag(743)
    DisableFlag(744)
    DisableFlag(745)
    DisableFlag(746)
    DisableFlagRange((11000501, 11000519))
    DisableFlagRange((11010501, 11010519))
    DisableFlagRange((11020501, 11020529))
    DisableFlagRange((11100501, 11100519))
    DisableFlagRange((11200501, 11200519))
    DisableFlagRange((11300501, 11300519))
    DisableFlagRange((11310501, 11310519))
    DisableFlagRange((11320501, 11320519))
    DisableFlagRange((11400501, 11400519))
    DisableFlagRange((11410501, 11410519))
    DisableFlagRange((11500501, 11500519))
    DisableFlagRange((11510501, 11510519))
    DisableFlagRange((11600501, 11600519))
    DisableFlagRange((11700501, 11700519))
    DisableFlagRange((11800501, 11800519))
    DisableFlagRange((11810501, 11810519))
    DisableFlagRange((11210501, 11210519))
    DisableFlag(1004)
    DisableFlag(1033)
    DisableFlag(1096)
    DisableFlag(1114)
    DisableFlag(1176)
    DisableFlag(1179)
    DisableFlag(1195)
    DisableFlag(1197)
    DisableFlag(1213)
    DisableFlag(1223)
    DisableFlag(1241)
    DisableFlag(1253)
    DisableFlag(1282)
    DisableFlag(1283)
    DisableFlag(1287)
    DisableFlag(1294)
    DisableFlag(1314)
    DisableFlag(1321)
    DisableFlag(1341)
    DisableFlag(1361)
    DisableFlag(1381)
    DisableFlag(1401)
    DisableFlag(1411)
    DisableFlag(1421)
    DisableFlag(1434)
    DisableFlag(1461)
    DisableFlag(1512)
    DisableFlag(1547)
    DisableFlag(1574)
    DisableFlag(1603)
    DisableFlag(1627)
    DisableFlag(1646)
    DisableFlag(1675)
    DisableFlag(1691)
    EnableFlag(1710)
    DisableFlag(1711)
    DisableFlag(1712)
    DisableFlag(11200596)
    DisableFlag(71200035)
    DisableFlag(71200042)
    DisableFlag(1763)
    DisableFlag(1822)
    DisableFlag(1841)
    DisableFlag(1863)
    DisableFlag(1871)
    SetTeamType(6001, TeamType.Ally)
    SetTeamType(6040, TeamType.Ally)
    SetTeamType(6072, TeamType.Ally)
    SetTeamType(6190, TeamType.Ally)
    SetTeamType(6230, TeamType.Ally)
    SetTeamType(6300, TeamType.Ally)
    Restart()


@NeverRestart(772)
def Event_772():
    """Event 772"""
    IfFlagDisabled(0, 744)
    IfFlagEnabled(-1, 1004)
    IfFlagEnabled(-1, 1033)
    IfFlagEnabled(-1, 1096)
    IfFlagEnabled(-1, 1114)
    IfFlagEnabled(-1, 1176)
    IfFlagEnabled(-1, 1179)
    IfFlagEnabled(-1, 1195)
    IfFlagEnabled(-1, 1197)
    IfFlagEnabled(-1, 1213)
    IfFlagEnabled(-1, 1223)
    IfFlagEnabled(-1, 1241)
    IfFlagEnabled(-1, 1253)
    IfFlagEnabled(-1, 1282)
    IfFlagEnabled(-1, 1283)
    IfFlagEnabled(-1, 1287)
    IfFlagEnabled(-1, 1294)
    IfFlagEnabled(-1, 1314)
    IfFlagEnabled(-1, 1321)
    IfFlagEnabled(-1, 1341)
    IfFlagEnabled(-1, 1361)
    IfFlagEnabled(-1, 1381)
    IfFlagEnabled(-1, 1401)
    IfFlagEnabled(-1, 1411)
    IfFlagEnabled(-1, 1421)
    IfFlagEnabled(-1, 1434)
    IfFlagEnabled(-1, 1461)
    IfFlagEnabled(-1, 1512)
    IfFlagEnabled(-1, 1547)
    IfFlagEnabled(-1, 1574)
    IfFlagEnabled(-1, 1603)
    IfFlagEnabled(-1, 1627)
    IfFlagEnabled(-1, 1646)
    IfFlagEnabled(-1, 1675)
    IfFlagEnabled(-1, 1691)
    IfFlagEnabled(-1, 1711)
    IfFlagEnabled(-1, 1712)
    IfFlagEnabled(-1, 71200035)
    IfFlagEnabled(-1, 71200042)
    IfFlagEnabled(-1, 1763)
    IfFlagEnabled(-1, 1822)
    IfFlagEnabled(-1, 1841)
    IfFlagEnabled(-1, 1863)
    IfFlagEnabled(-1, 1871)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(744)
    IfFlagDisabled(0, 744)
    Restart()


@NeverRestart(761)
def Event_761():
    """Event 761"""
    DisableNetworkSync()
    IfFlagEnabled(0, 760)
    WaitFrames(frames=200)
    DisableFlag(760)
    Restart()


@NeverRestart(763)
def Event_763():
    """Event 763"""
    DisableNetworkSync()
    IfFlagEnabled(0, 762)
    ForceAnimation(PLAYER, 7697)
    Wait(3.5)
    DisableFlag(762)
    Wait(2.799999952316284)
    DisableFlag(764)
    ForceAnimation(PLAYER, 7701, loop=True)
    Restart()


@NeverRestart(750)
def Event_750():
    """Event 750"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 71)
    IfCharacterHasSpecialEffect(-1, PLAYER, 72)
    IfCharacterHasSpecialEffect(-1, PLAYER, 73)
    IfCharacterHasSpecialEffect(-1, PLAYER, 74)
    IfFlagEnabled(-1, 751)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(751)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 71)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 72)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 73)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 74)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(751)
    Restart()


@NeverRestart(752)
def Event_752():
    """Event 752"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 5213)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5214)
    IfFlagEnabled(-1, 753)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(753)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5213)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5214)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(753)
    DisableFlag(11400591)
    Restart()


@NeverRestart(757)
def Event_757():
    """Event 757"""
    SkipLinesIfFlagDisabled(1, 757)
    DisplayStatus(10010660)
    DisableFlag(757)
    IfHost(1)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 71)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 72)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 73)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 74)
    IfCharacterHasSpecialEffect(-1, PLAYER, 33)
    IfCharacterHasSpecialEffect(-1, PLAYER, 34)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    End()


@NeverRestart(758)
def Event_758():
    """Event 758"""
    SkipLinesIfThisEventFlagDisabled(1)
    DisplayStatus(10010670)
    DisableFlag(758)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, value=0.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 2130)
    IfConditionTrue(0, input_condition=1)
    IfHost(2)
    IfCharacterDead(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2130)
    IfConditionTrue(0, input_condition=2)
    End()


@NeverRestart(759)
def Event_759():
    """Event 759"""
    SkipLinesIfThisEventFlagDisabled(1)
    DisplayStatus(10010680)
    DisableFlag(759)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, value=0.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 2131)
    IfConditionTrue(0, input_condition=1)
    IfHost(2)
    IfCharacterDead(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2131)
    IfConditionTrue(0, input_condition=2)
    End()


@NeverRestart(818)
def Event_818():
    """Event 818"""
    SkipLinesIfFlagEnabled(2, 11510150)
    IfFlagEnabled(0, 11510150)
    DisplayStatus(10010690)
    IfFlagEnabled(1, 11510150)
    IfOutsideMap(1, game_map=ANOR_LONDO)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11510150)
    Restart()


@NeverRestart(810)
def Event_810():
    """Event 810"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 50001031)
    EnableFlag(810)


@NeverRestart(812)
def Event_812(_, arg_0_3: int):
    """Event 812"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, arg_0_3)
    End()


@NeverRestart(822)
def Event_822():
    """Event 822"""
    IfFlagEnabled(0, 830)
    IfTimeElapsed(1, seconds=0.5)
    IfOutsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(830)
    Restart()


@NeverRestart(823)
def Event_823():
    """Event 823"""
    IfFlagEnabled(0, 831)
    IfTimeElapsed(1, seconds=0.5)
    IfOutsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(831)
    Restart()


@NeverRestart(840)
def Event_840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 840"""
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfFlagEnabled(2, 844)
    SkipLinesIfFlagEnabled(1, 847)
    RotateToFaceEntity(PLAYER, target_entity=arg_8_11)
    ForceAnimation(PLAYER, arg_4_7)
    Wait(1.0)
    PlaySoundEffect(PLAYER, 123456789, sound_type=SoundType.s_SFX)
    Wait(4.0)
    SkipLinesIfEqual(1, left=arg_12_15, right=-1)
    ForceAnimation(PLAYER, arg_12_15, loop=True)
    Restart()


@NeverRestart(766)
def Event_766():
    """Event 766"""
    IfOnline(1)
    EndIfConditionTrue(1)
    EnableFlag(765)
