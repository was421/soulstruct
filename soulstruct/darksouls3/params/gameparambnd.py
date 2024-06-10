from __future__ import annotations

__all__ = ["GameParamBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.games import DARK_SOULS_3

from soulstruct.containers import BinderVersion
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.base.params.param import Param
from soulstruct.utilities.misc import BiDict

from . import paramdef
from .paramdef import *




@dataclass(slots=True)
class GameParamBND(_BaseGameParamBND):

    PARAMDEF_MODULE: tp.ClassVar = paramdef

    dcx_type = DARK_SOULS_3.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    

    GET_BUNDLED_PARAMDEFBND: tp.ClassVar[tp.Callable] = GET_BUNDLED_PARAMDEFBND

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str) -> str:
        return f"N:\\FRPG\\data\\INTERROOT_x64\\param\\GameParam\\{entry_name}"