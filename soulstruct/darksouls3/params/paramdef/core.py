from __future__ import annotations

__all__ = ["ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEFBND"]

import logging
import typing as tp
from dataclasses import dataclass

from soulstruct.base.params.paramdef import ParamDef as _BaseParamDef, ParamDefBND as _BaseParamDefBND

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


@dataclass(slots=True)
class ParamDef(_BaseParamDef):

    unicode: bool = True
    format_version = 202


@dataclass(slots=True)
class ParamDefBND(_BaseParamDefBND):
    # TODO: I don't think DS3 has a `ParamDefBND`. Will need Paramdex, like Elden Ring.
    PARAMDEF_CLASS: tp.ClassVar = ParamDef


def GET_BUNDLED_PARAMDEFBND() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.get_game().name}.")
        _BUNDLED = ParamDefBND.from_bundled()
    return _BUNDLED
