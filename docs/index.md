# CBOR Model

`cbor-model` adds [CBOR] serialization and [CDDL] schema generation to [Pydantic] models.

## Installation

=== "`uv`"
    ```
    uv add cbor-model
    ```

=== "`pip`"
    ```
    pip install cbor-model
    ```


## Map encoding

Fields are encoded as a CBOR map keyed by the integer or string supplied to
`CBORField(key=...)`.

```python
from typing import Annotated
from cbor_model import CBORModel, CBORField

class Sensor(CBORModel):
    name: Annotated[str, CBORField(key=0)]
    value: Annotated[float, CBORField(key=1)]

sensor = Sensor(name="temp", value=21.5)
data = sensor.model_dump_cbor()
assert Sensor.model_validate_cbor(data) == sensor
```

## Array encoding

Switch to array encoding by setting `CBORConfig(encoding="array")` and using
`CBORField(index=...)` - fields are serialized in index order.

```python
from typing import Annotated
from cbor_model import CBORModel, CBORField, CBORConfig

class Point(CBORModel):
    cbor_config = CBORConfig(encoding="array")

    x: Annotated[int, CBORField(index=0)]
    y: Annotated[int, CBORField(index=1)]

pt = Point(x=4, y=2)
data = pt.model_dump_cbor()
assert Point.model_validate_cbor(data) == pt
```

## CDDL generation

Generate a [CDDL] schema from one or more models:

```python
from cbor_model.cddl import CDDLGenerator

print(CDDLGenerator().generate(Sensor))
# sensor_name = 0
# sensor_value = 1
#
# Sensor = {
#     ? sensor_name: tstr,
#     ? sensor_value: float
# }
```

[CBOR]: https://cbor.io/
[CDDL]: https://www.rfc-editor.org/rfc/rfc8610
[Pydantic]: https://github.com/pydantic/pydantic
