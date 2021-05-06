from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEF"]

import logging
import typing as tp

from soulstruct.games import BloodborneType
from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)
from soulstruct.utilities.binary import BinaryStruct

from .display_info import get_param_info, get_param_info_field

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


class ParamDefField(_BaseParamDefField):

    def get_display_info(self, row: ParamRow):
        try:
            field_info = get_param_info_field(self.param_name, self.name)
        except ValueError:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return field_info(row)


class ParamDef(_BaseParamDef):
    BYTE_ORDER = "<"
    HEADER_STRUCT = BinaryStruct(
        ("size", "i"),
        ("header_size", "H", 255),
        ("data_version", "H"),
        ("field_count", "H"),
        ("field_size", "H", 208),
        ("param_name", "32j"),
        ("big_endian", "B", 0),
        ("unicode", "?"),
        ("format_version", "h", 201),
        ("unk1", "q", 56),
    )
    FIELD_CLASS = ParamDefField

    @property
    def param_info(self):
        try:
            return get_param_info(self.param_type)
        except KeyError:
            # This param has no extra information.
            return None


class ParamDefBND(_BaseParamDefBND, BloodborneType):
    PARAMDEF_CLASS = ParamDef


def GET_BUNDLED_PARAMDEF() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.GAME.name}.")
        _BUNDLED = ParamDefBND()
    return _BUNDLED
