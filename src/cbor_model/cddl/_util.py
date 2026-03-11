# ruff: noqa: ANN401
from types import NoneType
from typing import Any, TypeGuard, Union, get_args, get_origin


def is_union_type(annotation: Any) -> bool:
    """Return True when ``annotation`` is a typing.Union."""
    # Accept either the full annotation (e.g. ``str | int``) or an
    # already-extracted origin (``typing.Union``) for compatibility.
    return annotation is Union or get_origin(annotation) is Union


def is_optional(annotation: Any) -> bool:
    """Return True when ``annotation`` is Optional[...] (Union[..., None])."""
    return is_union_type(annotation) and NoneType in get_args(annotation)


def is_type_of[T](annotation: Any, target: type[T]) -> TypeGuard[type[T]]:
    return isinstance(annotation, type) and issubclass(annotation, target)


def extract_types_matching[T](
    annotation: Any,
    predicate: type[T],
) -> list[type[T]]:
    types: list[type[T]] = []
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is not None:
        for arg in args:
            types.extend(extract_types_matching(arg, predicate))
    elif is_type_of(annotation, predicate):
        types.append(annotation)

    return types
