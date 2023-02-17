"""
As always, courtesy of SoulsFormats by TKGP:
    https://github.com/JKAnderson/SoulsFormats/blob/master/SoulsFormats/Formats/TPF/DDS.cs
"""
from __future__ import annotations

__all__ = ["DDS", "DDSD", "DDSCAPS", "DDSCAPS2", "texconv", "get_converted_texture_data", "convert_dds_file"]

import logging
import subprocess
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum, auto
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.binary import *

try:
    Self = tp.Self
except AttributeError:
    Self = "DDS"

_LOGGER = logging.getLogger(__name__)


class DDSD(IntEnum):
    CAPS = 0x1
    HEIGHT = 0x2
    WIDTH = 0x4
    PITCH = 0x8
    PIXELFORMAT = 0x1000
    MIPMAPCOUNT = 0x20000
    LINEARSIZE = 0x80000
    DEPTH = 0x800000


HEADER_FLAGS_TEXTURE = DDSD.CAPS | DDSD.HEIGHT | DDSD.WIDTH | DDSD.PIXELFORMAT


class DDSCAPS(IntEnum):
    COMPLEX = 0x8
    TEXTURE = 0x1000
    MIPMAP = 0x400000


class DDSCAPS2(IntEnum):
    CUBEMAP = 0x200
    CUBEMAP_POSITIVEX = 0x400
    CUBEMAP_NEGATIVEX = 0x800
    CUBEMAP_POSITIVEY = 0x1000
    CUBEMAP_NEGATIVEY = 0x2000
    CUBEMAP_POSITIVEZ = 0x4000
    CUBEMAP_NEGATIVEZ = 0x8000
    VOLUME = 0x200000


CUBEMAP_ALLFACES = (
    DDSCAPS2.CUBEMAP | DDSCAPS2.CUBEMAP_POSITIVEX | DDSCAPS2.CUBEMAP_NEGATIVEX | DDSCAPS2.CUBEMAP_POSITIVEY |
    DDSCAPS2.CUBEMAP_NEGATIVEY | DDSCAPS2.CUBEMAP_POSITIVEZ | DDSCAPS2.CUBEMAP_NEGATIVEZ
)


class DDPF(IntEnum):
    ALPHAPIXELS = 0x1
    ALPHA = 0x2
    FOURCC = 0x4
    RGB = 0x40
    YUV = 0x200
    LUMINANCE = 0x20000


class DIMENSION(IntEnum):
    TEXTURE1D = 2
    TEXTURE2D = 3
    TEXTURE3D = 4


class RESOURCE_MISC(IntEnum):
    TEXTURECUBE = 0x4


class ALPHA_MODE(IntEnum):
    UNKNOWN = 0
    STRAIGHT = 1
    PREMULTIPLIED = 2
    OPAQUE = 3
    CUSTOM = 4


# Extra enum in `DX10` files.
class DXGI_FORMAT(IntEnum):
    UNKNOWN = auto()
    R32G32B32A32_TYPELESS = auto()
    R32G32B32A32_FLOAT = auto()
    R32G32B32A32_UINT = auto()
    R32G32B32A32_SINT = auto()
    R32G32B32_TYPELESS = auto()
    R32G32B32_FLOAT = auto()
    R32G32B32_UINT = auto()
    R32G32B32_SINT = auto()
    R16G16B16A16_TYPELESS = auto()
    R16G16B16A16_FLOAT = auto()
    R16G16B16A16_UNORM = auto()
    R16G16B16A16_UINT = auto()
    R16G16B16A16_SNORM = auto()
    R16G16B16A16_SINT = auto()
    R32G32_TYPELESS = auto()
    R32G32_FLOAT = auto()
    R32G32_UINT = auto()
    R32G32_SINT = auto()
    R32G8X24_TYPELESS = auto()
    D32_FLOAT_S8X24_UINT = auto()
    R32_FLOAT_X8X24_TYPELESS = auto()
    X32_TYPELESS_G8X24_UINT = auto()
    R10G10B10A2_TYPELESS = auto()
    R10G10B10A2_UNORM = auto()
    R10G10B10A2_UINT = auto()
    R11G11B10_FLOAT = auto()
    R8G8B8A8_TYPELESS = auto()
    R8G8B8A8_UNORM = auto()
    R8G8B8A8_UNORM_SRGB = auto()
    R8G8B8A8_UINT = auto()
    R8G8B8A8_SNORM = auto()
    R8G8B8A8_SINT = auto()
    R16G16_TYPELESS = auto()
    R16G16_FLOAT = auto()
    R16G16_UNORM = auto()
    R16G16_UINT = auto()
    R16G16_SNORM = auto()
    R16G16_SINT = auto()
    R32_TYPELESS = auto()
    D32_FLOAT = auto()
    R32_FLOAT = auto()
    R32_UINT = auto()
    R32_SINT = auto()
    R24G8_TYPELESS = auto()
    D24_UNORM_S8_UINT = auto()
    R24_UNORM_X8_TYPELESS = auto()
    X24_TYPELESS_G8_UINT = auto()
    R8G8_TYPELESS = auto()
    R8G8_UNORM = auto()
    R8G8_UINT = auto()
    R8G8_SNORM = auto()
    R8G8_SINT = auto()
    R16_TYPELESS = auto()
    R16_FLOAT = auto()
    D16_UNORM = auto()
    R16_UNORM = auto()
    R16_UINT = auto()
    R16_SNORM = auto()
    R16_SINT = auto()
    R8_TYPELESS = auto()
    R8_UNORM = auto()
    R8_UINT = auto()
    R8_SNORM = auto()
    R8_SINT = auto()
    A8_UNORM = auto()
    R1_UNORM = auto()
    R9G9B9E5_SHAREDEXP = auto()
    R8G8_B8G8_UNORM = auto()
    G8R8_G8B8_UNORM = auto()
    BC1_TYPELESS = auto()
    BC1_UNORM = auto()
    BC1_UNORM_SRGB = auto()
    BC2_TYPELESS = auto()
    BC2_UNORM = auto()
    BC2_UNORM_SRGB = auto()
    BC3_TYPELESS = auto()
    BC3_UNORM = auto()
    BC3_UNORM_SRGB = auto()
    BC4_TYPELESS = auto()
    BC4_UNORM = auto()
    BC4_SNORM = auto()
    BC5_TYPELESS = auto()
    BC5_UNORM = auto()
    BC5_SNORM = auto()
    B5G6R5_UNORM = auto()
    B5G5R5A1_UNORM = auto()
    B8G8R8A8_UNORM = auto()
    B8G8R8X8_UNORM = auto()
    R10G10B10_XR_BIAS_A2_UNORM = auto()
    B8G8R8A8_TYPELESS = auto()
    B8G8R8A8_UNORM_SRGB = auto()
    B8G8R8X8_TYPELESS = auto()
    B8G8R8X8_UNORM_SRGB = auto()
    BC6H_TYPELESS = auto()
    BC6H_UF16 = auto()
    BC6H_SF16 = auto()
    BC7_TYPELESS = auto()
    BC7_UNORM = auto()
    BC7_UNORM_SRGB = auto()
    AYUV = auto()
    Y410 = auto()
    Y416 = auto()
    NV12 = auto()
    P010 = auto()
    P016 = auto()
    OPAQUE_420 = auto()  # DXGI_FORMAT_420_OPAQUE
    YUY2 = auto()
    Y210 = auto()
    Y216 = auto()
    NV11 = auto()
    AI44 = auto()
    IA44 = auto()
    P8 = auto()
    A8P8 = auto()
    B4G4R4A4_UNORM = auto()
    P208 = auto()
    V208 = auto()
    V408 = auto()
    FORCE_UINT = auto()


@dataclass(slots=True)
class DDSHeader(BinaryStruct):
    magic: bytes = field(**BinaryString(4, asserted=b"DDS\0"))
    size: int = field(**Binary(asserted=0x7C))
    flags: uint
    height: int
    width: int
    pitch_or_linear_size: int
    depth: int
    mipmap_count: int
    reserved_1: list[int] = field(**BinaryArray(11))
    # Start of `PIXELFORMAT` in SoulsFormats.
    pixelformat_size: int = field(**Binary(asserted=32))
    pixelformat_flags: DDPF = field(**Binary(uint))
    fourcc: bytes = field(**BinaryString(4))
    rgb_bit_count: int
    r_bitmask: uint
    g_bitmask: uint
    b_bitmask: uint
    a_bitmask: uint
    # End of `PIXELFORMAT`.
    caps1: uint
    caps2: uint
    caps3: uint
    caps4: uint
    reserved_2: int


@dataclass(slots=True)
class DXT10Header(BinaryStruct):

    dxgi_format: DXGI_FORMAT = field(**Binary(uint))
    resource_dimension: DIMENSION = field(**Binary(uint))
    misc_flag: uint  # RESOURCE_MISC
    array_size: uint
    alpha_mode: ALPHA_MODE = field(**Binary(uint))


@dataclass(slots=True)
class DDS(GameFile):
    """Unpacks DDS header information.

    Does NOT unpack actual DDS information or support packing or writing.
    """

    header: DDSHeader = None
    dxt10_header: DXT10Header | None = None

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        header = DDSHeader.from_bytes(reader)
        dxt10_header = DXT10Header.from_bytes(reader) if header.fourcc == b"DX10" else None
        return cls(header=header, dxt10_header=dxt10_header)

    def to_writer(self) -> BinaryWriter:
        raise TypeError("Cannot write `DDS` files. Only the header can be unpacked.")

    @property
    def fourcc(self) -> str:
        return self.header.fourcc.decode()

    @property
    def dxgi_format(self) -> DXGI_FORMAT | None:
        return self.dxt10_header.dxgi_format if self.dxt10_header else None

    @property
    def texconv_format(self) -> str:
        """Returns DXGI format name if present, or `fourcc` otherwise."""
        if self.dxt10_header:
            return self.dxt10_header.dxgi_format.name
        return self.fourcc

    def __repr__(self):
        if self.dxt10_header:
            return f"DDS(DX10, dxgi_format={self.dxt10_header.dxgi_format.name})"
        return f"DDS({self.header.fourcc.decode()})"


def texconv(*args):
    texconv_path = PACKAGE_PATH("base/textures/texconv.exe")
    if not texconv_path.is_file():
        raise FileNotFoundError("Cannot find `texconv.exe` that should be bundled with Soulstruct in 'base/textures'.")
    return subprocess.run(
        [texconv_path, *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


# TODO: use `tempfile` module
def get_converted_texture_data(input_source: bytes | Path | str, *texconv_args) -> bytes:
    if isinstance(input_source, bytes):
        temp_dds_path = Path(__file__).parent / "__temp__.dds"
        temp_dds_path.write_bytes(input_source)
        result = texconv("-o", str(Path(__file__).parent), "-y", *texconv_args, str(temp_dds_path))
        if result.returncode == 0:
            return temp_dds_path.read_bytes()
        raise ValueError(
            f"Could not convert texture source bytes.\n"
            f"   stdout: {result.stdout}\n"
            f"   stderr: {result.stderr}"
        )
    else:
        result = texconv(*texconv_args, str(input_source))
        output_path = Path(input_source).with_suffix(".DDS")
        if result.returncode == 0 and output_path.is_file():
            return output_path.read_bytes()
        else:
            raise ValueError(
                f"Could not convert texture source {input_source}.\n"
                f"   stdout: {result.stdout}\n"
                f"   stderr: {result.stderr}"
            )


def convert_dds_file(
    dds_path: str | Path, output_dir: str | Path, output_format: str, input_fourcc: str = None
):
    """Convert DDS file path to a different format using DirectX-powered `texconv.exe`.

    If `input_format` is given, the source DDS will be checked to make sure it matches that format.
    """
    if input_fourcc is not None:
        # Check that DDS starts with the asserted format.
        dds = DDS(dds_path)
        if dds.header.fourcc.decode() != input_fourcc:
            raise ValueError(f"DDS format {dds.header.fourcc} does not match `input_format` {input_fourcc}")
    return texconv("-f", output_format, "-o", output_dir, "-y", dds_path)
