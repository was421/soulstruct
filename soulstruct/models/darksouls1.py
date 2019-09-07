
# TODO: More sensible ordering.
MODEL_IDS = {
    0: 'Player Character',
    1200: 'Large Rat',
    1201: 'Small Rat',
    1202: 'Giant Rat',
    1203: 'Snow Rat',
    2060: 'Infested Ghoul',
    2230: 'Stray Demon',
    2231: 'Demon Firesage',
    2232: 'Asylum Demon',
    2240: 'Capra Demon',
    2250: 'Taurus Demon',
    2260: 'Batwing Demon',
    2270: 'Mushroom Parent',
    2280: 'Mushroom Child',
    # 2290: 'Chained Prisoner (unused)',
    2300: 'Titanite Demon',
    2310: 'Crow Demon',
    2320: 'Iron Golem',
    2330: 'Demonic Foliage',
    2360: 'Executioner Smough',  # both versions
    2370: 'Channeler',
    2380: 'Stone Knight',
    2390: 'Darkwraith',
    2400: 'Painting Guardian',
    2410: 'Silver Knight',
    2430: 'Demonic Statue',
    2500: 'Hollow',
    2510: 'Undead Merchant',  # both genders
    2520: 'Hollow Assassin',
    2530: 'Blowdart Sniper',
    2540: 'Hollow Warrior',
    2550: 'Hollow Soldier',
    2560: 'Balder Knight',
    2570: 'Berenike Knight',
    # 2590: 'Marvelous Chester (unused 1)',
    # 2591: 'Marvelous Chester (unused 2)',
    # 2600: 'Young Witch Beatrice (unused)',
    2640: 'Andre',
    2650: 'Necromancer',
    2660: 'Butcher',
    2670: 'Ghost (Male)',
    2680: 'Ghost (Female)',
    2690: 'Serpent Soldier',
    2700: 'Serpent Mage',
    2710: 'Crystal Golem',
    2711: 'Golden Crystal Golem',
    2730: 'Crossbreed Priscilla',
    2731: 'Crossbreed Priscilla (tail)',
    2750: 'Anastacia',
    2780: 'Mimic',
    2790: 'Black Knight',
    2800: 'Undead Crystal Soldier',
    2810: 'Infested Barbarian (club)',
    2811: 'Infested Barbarian (boulder)',
    # 2820: 'Spider Hollow (unused)',
    2830: 'Phalanx',
    2840: 'Engorged Hollow',
    2860: 'Giant',
    2870: 'Sentinel',  # includes Royal Sentinel
    2900: 'Skeleton',
    2910: 'Giant Skeleton',
    2920: 'Vamos',
    2930: 'Bonewheel Skeleton',
    2940: 'Skeleton Baby',
    2950: 'Skeleton Beast',
    2960: 'Bone Tower',
    3090: 'Giant Mosquito',
    # 3110: 'Crystal Lizard (unused)',  # from Demon's Souls
    3200: 'Slime',
    3210: 'Egg Carrier',
    3220: 'Vile Maggot',
    3230: 'Moonlight Butterfly',
    3240: 'Chaos Eater',
    3250: 'Man-Eater Shell',
    3270: 'Basilisk',
    # 3290: 'Brain Bug (unused)',
    3300: 'Crystal Lizard',
    3320: 'Pinwheel',
    3330: 'Pisaca',
    3340: 'Attack Dog',
    3341: 'Flaming Attack Dog',
    3350: 'Possessed Tree',
    3370: 'Tree Lizard',
    3380: 'Giant Leech',
    3390: 'Burrowing Rockworm',
    3400: 'Cragspider',
    3410: 'Frog-Ray',
    3420: 'Undead Dragon',
    3421: 'Bounding Demon',  # Undead Dragon legs
    3422: 'Undead Dragon (wing)',
    3430: 'Hellkite Dragon',
    3431: 'Hellkite Dragon (tail)',
    # 3440: 'Kalameet (unused)',
    3450: 'Everlasting Dragon',
    3451: 'Everlasting Dragon (tail)',
    3460: 'Armored Tusk',
    3461: 'Armored Tusk (rear guard)',
    # 3470: 'Sanctuary Guardian (unused)',
    3471: 'Sanctuary Guardian',
    3480: 'Chaos Bug',
    3490: 'Good Vagrant',
    3491: 'Evil Vagrant',
    3500: 'Mass of Souls',
    3501: 'Wisp',
    3510: 'Giant Crow',
    3511: 'Giant Crow (cutscene)',
    3520: 'Drake',
    3530: 'Hydra',
    3531: 'Hydra (head)',
    4090: 'Marvelous Chester',
    # 4091: 'Marvelous Chester (unused 3)',
    # 4095: 'Marvelous Chester (unused 4)',
    4100: 'Artorias',
    4110: 'Hawkeye Gough',
    4120: 'Stone Guardian',
    4130: 'Scarecrow',
    4140: 'Elizabeth',
    4150: 'Bloathead',
    4160: 'Bloathead Sorcerer',
    4170: 'Humanity Phantom (small)',
    4171: 'Humanity Phantom (medium)',
    4172: 'Humanity Phantom (large)',
    4180: 'Chained Prisoner',
    4190: 'Abyss Attack Dog',
    4500: 'Manus',
    4510: 'Black Dragon Kalameet',
    4511: 'Black Dragon Kalameet (tail)',
    4520: 'Young Sif',
    # 4530: 'Young Alvina (unused)',
    4531: 'Young Alvina',
    5200: 'Centipede Demon',
    5201: 'Centipede Demon (arm)',
    5202: 'Centipede Demon (tail)',
    5210: 'Sif',
    5220: 'Gravelord Nito',
    5230: 'Bed of Chaos',
    # 5231: 'Bed of Chaos (unused)',  # incomplete mobile version
    5240: 'Parasitic Wall Hugger',
    5250: 'Ceaseless Discharge',
    5260: 'Gaping Dragon',
    5261: 'Gaping Dragon (tail)',
    5270: 'Ornstein',
    5271: 'Giant Ornstein',
    5280: 'Quelaag',
    5290: 'Seath the Scaleless',
    # 5300: 'Undead King Jareel',  # incomplete New Londo Ruins boss
    5310: 'Gwynevere',
    5320: 'Gwyndolin',
    5330: 'Primordial Serpent',  # Frampt / Kaathe
    5340: 'Fair Lady',  # ala Daughter of Chaos, ala Quelaag's Sister
    5350: 'Bell Gargoyle',
    5351: 'Lightning Gargoyle',
    5352: 'Bell Gargoyle (tail)',
    5353: 'Lightning Gargoyle (tail)',
    5360: 'Great Feline',
    5361: 'Alvina',
    # 5362: 'Alvina (unused)',
    5370: 'Gwyn',
    5390: 'Four Kings',
    5400: 'Bed of Chaos (spirit)',
}
