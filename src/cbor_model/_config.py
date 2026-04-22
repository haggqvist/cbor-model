from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Literal

type CBOREncoders = dict[type, Callable[[Any], Any]]


@dataclass(frozen=True, slots=True)
class CBORConfig:
    """Configuration options for :class:`~cbor_model.CBORModel` instances.

    Attributes:
        encoding: Whether to encode the model as a CBOR map (keyed by
            `CBORField(key=...)`) or as a CBOR array (ordered by
            `CBORField(index=...)`). Defaults to `"map"`.
        tag: Wrap the encoded model in a CBOR tag with this tag number.
            `None` disables tagging (default).
        canonical: Use canonical CBOR encoding (deterministic key ordering
            and minimal integer encoding). Defaults to `False`.
        encoders: Custom encoders for types not natively supported by
            cbor2. Keys are Python types; values are callables that
            convert an instance of that type to a cbor2-encodable value
            (e.g. `str`, `int`, `list`, `dict`).

    """

    encoding: Literal["map", "array"] = "map"
    """Whether to encode the model as a CBOR map (key-value pairs) or array
    (positional). Defaults to "map"."""

    tag: int | None = None
    """Wrap the CBORModel in a CBOR Tag on serialization."""

    canonical: bool = False
    """Whether to use canonical CBOR encoding. Defaults to `False`."""

    encoders: CBOREncoders = field(default_factory=dict)
    """Custom encoders for types that are not natively supported by cbor2.
    The keys should be types, and the values should be callables that take an
    instance of the type and return a value that can be encoded by cbor2 (e.g.
    a string, int, list, dict, etc.)."""

    def __post_init__(self) -> None:
        if self.tag is not None and self.tag < 0:
            err = f"CBOR tag {self.tag} is invalid. Tags must be non-negative integers."
            raise ValueError(err)
