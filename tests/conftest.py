from enum import IntEnum, auto
from typing import Annotated

import pytest
from pydantic import Field, HttpUrl

from cbor_model import CBORField, CBORModel


class SomeEnum(IntEnum):
    A = auto()
    B = auto()
    C = auto()


class Contact(CBORModel):
    street: Annotated[str, CBORField(key=0)]
    city: Annotated[str, CBORField(key=1)]
    postal_code: Annotated[str | None, CBORField(key=2)] = None
    website: Annotated[HttpUrl | None, CBORField(key=3)] = None


class Item(CBORModel):
    product_id: Annotated[str, CBORField(key=0)]
    quantity: Annotated[int, CBORField(key=1)]


class TaggedItem(Item):
    tags: Annotated[str | None, CBORField(key=2)] = None


class Inner(CBORModel):
    name: Annotated[str, CBORField(key=0)]
    value: Annotated[int, CBORField(key=1)]
    maybe: Annotated[str | None, CBORField(key=2)] = None


class ComplexModel(CBORModel):
    id: Annotated[str, CBORField(key=0)]
    contact: Annotated[Contact, CBORField(key=1)]
    items: Annotated[list[Item], CBORField(key=2)]
    metadata: Annotated[dict[str, str] | None, CBORField(key=3)] = None
    some_state: Annotated[SomeEnum, CBORField(key=4)]
    nested_option: Annotated[Inner | None, CBORField(key=5)] = None
    raw_blob: Annotated[bytes, CBORField(key=6, tag=50024)]
    inner_list: Annotated[
        list[Inner | None],
        CBORField(key=7),
        Field(default_factory=list),
    ]


@pytest.fixture
def complex_model() -> ComplexModel:
    return ComplexModel(
        id="12345",
        contact=Contact(
            street="123 Main St",
            city="Anytown",
            postal_code="12345",
        ),
        items=[
            TaggedItem(product_id="A1", quantity=2, tags="fragile"),
            Item(product_id="B2", quantity=5),
        ],
        metadata={"source": "test"},
        some_state=SomeEnum.A,
        nested_option=Inner(name="option1", value=10),
        raw_blob=b"\x01\x02\x03\x04",
        inner_list=[
            Inner(name="list_item1", value=100),
            None,
            Inner(name="list_item2", value=200, maybe="optional"),
        ],
    )
