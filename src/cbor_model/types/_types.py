"""Annotated integer type aliases for CBOR-constrained integer fields.

These are pre-built `typing.Annotated` shorthands that combine a plain
``int`` with a `pydantic.Field` range constraint, making them
drop-in replacements for bare ``int`` annotations wherever a fixed-width CBOR
integer type is required.
"""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

Int1 = Annotated[int, Field(ge=-128, le=127)]
"""Signed 8-bit integer (``-128`` … ``127``)."""
UInt = Annotated[int, Field(ge=0)]
"""Unsigned integer (no upper bound)."""
UInt1 = Annotated[int, Field(ge=0, le=0xFF)]
"""Unsigned 8-bit integer (``0`` … ``255``)."""
UInt2 = Annotated[int, Field(ge=0, le=0xFFFF)]
"""Unsigned 16-bit integer (``0`` … ``65 535``)."""
UInt4 = Annotated[int, Field(ge=0, le=0xFFFFFFFF)]
"""Unsigned 32-bit integer (``0`` … ``4 294 967 295``)."""
