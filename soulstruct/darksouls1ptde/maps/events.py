from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBLightEvent",
    "MSBSoundEvent",
    "MSBVFXEvent",
    "MSBWindEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBMessageEvent",
    "MSBObjActEvent",
    "MSBSpawnPointEvent",
    "MSBMapOffsetEvent",
    "MSBNavigationEvent",
    "MSBEnvironmentEvent",
    "MSBNPCInvasionEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.darksouls1ptde.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb import MSBEntry
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import MSBEventSubtype
from .regions import MSBRegion
from .parts import MSBPart


@dataclass(slots=True, eq=False, repr=False)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Dark Souls 1."""

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        name_offset: int
        _supertype_index: int
        _subtype_int: int
        _subtype_index: int
        supertype_data_offset: int
        subtype_data_offset: int
        _pad1: bytes = field(**BinaryPad(4))

    @dataclass(slots=True)
    class SUPERTYPE_DATA_STRUCT(BinaryStruct):
        _attached_part_index: int
        _attached_region_index: int
        entity_id: int
        unknowns: list[byte] = field(**BinaryArray(4))

    NAME_ENCODING: tp.ClassVar[str] = "shift-jis"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None

    unknowns: list[int] = field(default_factory=lambda: [0, 0, 0, 0], **BinaryArray(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBLightEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Light

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        point_light_id: int

    point_light_id: int = field(default=0, **MapFieldInfo(game_type=PointLightParam))


@dataclass(slots=True, eq=False, repr=False)
class MSBSoundEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Sound

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        sound_type: int
        sound_id: int

    sound_type: int = field(default=SoundType.m_Music.value, **MapFieldInfo(game_type=SoundType))
    sound_id: int = -1


@dataclass(slots=True, eq=False, repr=False)
class MSBVFXEvent(MSBEvent):
    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.VFX

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        vfx_id: int

    vfx_id: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBWindEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Wind

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        wind_vector_min: Vector3
        unk_x04_x08: float
        wind_vector_max: Vector3
        unk_x0c_x10: float
        wind_swing_cycles: list[float] = field(**BinaryArray(4))
        wind_swing_powers: list[float] = field(**BinaryArray(4))

    wind_vector_min: Vector3 = field(default_factory=Vector3.zero)
    unk_x04_x08: float = 0.0
    wind_vector_max: Vector3 = field(default_factory=Vector3.zero)
    unk_x0c_x10: float = 0.0
    wind_swing_cycles: list[float] = field(default_factory=lambda: [0.0] * 4, **BinaryArray(4))
    wind_swing_powers: list[float] = field(default_factory=lambda: [0.0] * 4, **BinaryArray(4))


@dataclass(slots=True, eq=False, repr=False)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "treasure_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(**BinaryPad(4))
        _treasure_part_index: int
        item_lot_1: int
        _minus_one_1: int = field(**Binary(asserted=-1))
        item_lot_2: int
        _minus_one_2: int = field(**Binary(asserted=-1))
        item_lot_3: int
        _minus_one_3: int = field(**Binary(asserted=-1))
        item_lot_4: int
        _minus_one_4: int = field(**Binary(asserted=-1))
        item_lot_5: int
        _minus_one_5: int = field(**Binary(asserted=-1))
        is_in_chest: bool
        is_hidden: bool
        _pad2: bytes = field(**BinaryPad(2))

    treasure_part: MSBPart = None
    item_lot_1: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_2: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_3: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_4: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    item_lot_5: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    is_in_chest: bool = False
    is_hidden: bool = False

    _treasure_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        # TODO: My MSB entry `duplicate()` (copying entries) is doing a deep copy on referenced fields.
        #  Create a custom `MSBEntry.copy()` method that does a shallow copy only
        super(MSBEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "treasure_part")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _treasure_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "treasure_part"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_parts", "spawn_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        max_count: byte
        spawner_type: sbyte
        limit_count: short
        min_spawner_count: short
        max_spawner_count: short
        min_interval: float
        max_interval: float
        initial_spawn_count: int
        _pad1: bytes = field(**BinaryPad(28))
        _spawn_regions_indices: list[int] = field(**BinaryArray(4))
        _spawn_parts_indices: list[int] = field(**BinaryArray(32))
        _pad2: bytes = field(**BinaryPad(64))

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 32)))
    )
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 4, **MapFieldInfo(GameObjectIntSequence((Region, 4)))
    )

    _spawn_parts_indices: list[int] = field(default=None, **BinaryArray(32))
    _spawn_regions_indices: list[int] = field(default=None, **BinaryArray(4))

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBSpawnerEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _spawn_parts_indices=self.try_index(entry_lists["PARTS_PARAM_ST"], "spawn_parts"),
            _spawn_regions_indices=self.try_index(entry_lists["POINT_PARAM_ST"], "spawn_regions"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBMessageEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Message

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        text_id: short
        unk_x02_x04: short
        is_hidden: bool
        _pad1: bytes = field(**BinaryPad(3))

    text_id: int = field(default=-1, **MapFieldInfo(game_type=SoapstoneMessage))
    unk_x02_x04: int = 2
    is_hidden: bool = False


@dataclass(slots=True, eq=False, repr=False)
class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.ObjAct
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "obj_act_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        obj_act_entity_id: int
        _obj_act_part_index: int
        obj_act_param_id: short
        obj_act_state: byte
        _pad1: bytes = field(**BinaryPad(1))
        obj_act_flag: int

    obj_act_entity_id: int = -1
    obj_act_part: MSBPart = None
    obj_act_param_id: int = field(default=-1, **MapFieldInfo(game_type=ObjActParam))
    obj_act_state: int = 0
    obj_act_flag: int = field(default=0, **MapFieldInfo(game_type=Flag))

    _obj_act_part_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBObjActEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "obj_act_part")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _obj_act_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "obj_act_part"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnPointEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.SpawnPoint
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_point_region"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _spawn_point_region_index: int
        _pad1: bytes = field(**BinaryPad(12))

    spawn_point_region: MSBRegion = None

    _spawn_point_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBSpawnPointEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "spawn_point_region")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _spawn_point_region_index=self.try_index(entry_lists["POINT_PARAM_ST"], "spawn_point_region"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBMapOffsetEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.MapOffset

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        translate: Vector3
        rotate_y: float

    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate_y: float = 0.0


@dataclass(slots=True, eq=False, repr=False)
class MSBNavigationEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Navigation
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "navigation_region"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _navigation_region_index: int
        _pad1: bytes = field(**BinaryPad(12))

    navigation_region: MSBRegion = None

    _navigation_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBNavigationEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "navigation_region")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _navigation_region_index=self.try_index(entry_lists["POINT_PARAM_ST"], "navigation_region"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBEnvironmentEvent(MSBEvent):
    """I believe this marks the location (and some data) of the baking point of a cube reflection map. These
    textures can be found in `mAA/GI_EnvM_mAA.tpfbhd` with names `GI_Env_mAA_BB_####.tpf.dcx`. Each TPF contains an
    `EnvDif` cube map DDS and an `EnvSpc` cube map DDS (possibly multiple `EnvSpc` maps with `_I` index suffix). These
    cube maps are used by the `BakedLight` (internal name "LightBank") DrawParam table.

    In other words: I don't think the location of these events does anything in the actual game. But I'm not 100% sure
    and haven't tested that hypothesis yet (i.e., moving all the events).

    `MSBCollision` parts reference the environment event whose reflection map should be used while the player is
    standing on that collision, I assume (although I'd expect this to create visible transitions?).
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Environment

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        unk_x00_x04: int
        unk_x04_x08: float
        unk_x08_x0c: float
        unk_x0c_x10: float
        unk_x10_x14: float
        unk_x14_x18: float
        _pad1: bytes = field(**BinaryPad(8))

    unk_x00_x04: int = 0
    unk_x04_x08: float = 1.0
    unk_x08_x0c: float = 1.0
    unk_x0c_x10: float = 1.0
    unk_x10_x14: float = 1.0
    unk_x14_x18: float = 1.0


@dataclass(slots=True, eq=False, repr=False)
class MSBNPCInvasionEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.NPCInvasion
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_point_region"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        host_entity_id: int
        invasion_flag_id: int
        _spawn_point_region_index: int
        _pad1: bytes = field(**BinaryPad(4))

    host_entity_id: int = -1
    invasion_flag_id: int = field(default=-1, **MapFieldInfo(game_type=Flag))
    spawn_point_region: MSBRegion = None

    _spawn_point_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBNPCInvasionEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "spawn_point_region")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _spawn_point_region_index=self.try_index(entry_lists["POINT_PARAM_ST"], "spawn_point_region"),
        )
