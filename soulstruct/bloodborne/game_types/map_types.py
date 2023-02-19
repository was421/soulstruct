from __future__ import annotations

__all__ = [
    "Map",
    "MapTyping",
    "MapEntry",
    "MapEntity",

    "MapModel",
    "MapPieceModel",
    "ObjectModel",
    "CharacterModel",
    "PlayerModel",
    "CollisionModel",
    "NavmeshModel",

    "MapEvent",
    "SoundEvent",
    "VFXEvent",
    "TreasureEvent",
    "SpawnerEvent",
    "MessageEvent",
    "ObjActEvent",
    "SpawnPointEvent",
    "MapOffsetEvent",
    "NavigationEvent",
    "EnvironmentEvent",

    "MapPart",
    "MapPiece",
    "Object",
    "Character",
    "Collision",
    "PlayerStart",
    "Navmesh",
    "UnusedObject",
    "UnusedCharacter",
    "MapConnection",

    "Region",
    "RegionVolume",
    "RegionPoint",
    "RegionCircle",
    "RegionSphere",
    "RegionCylinder",
    "RegionRect",
    "RegionBox",

    "MapPartTyping",
    "CoordEntityTyping",
    "ObjectTyping",
    "RegionTyping",
    "CharacterTyping",
    "AnimatedEntityTyping",
    "MapPieceTyping",
    "CollisionTyping",
    "SoundEventTyping",
    "EnvironmentEventTyping",
    "NavigationEventTyping",
    "VFXEventTyping",
    
    "ID_RANGES",
]

from soulstruct.base.game_types.map_types import *

# TODO
ID_RANGES = {}
#     RegionVolume: (2000, 2499),
#     RegionPoint: (2500, 2899),
#     MapPiece: (3000, 3199),
#     Object: (1000, 1899),
#     Character: (0, 899),
#     PlayerStart: (990, 999),
#     Collision: (3200, 3399),
#     SoundEvent: (3800, 3899),
#     VFXEvent: (3400, 3599),
#     SpawnerEvent: (3600, 3699),
#     MessageEvent: (3700, 3799),
#     SpawnPointEvent: (3900, 3949),
# }
