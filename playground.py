import pydantic
from pydantic import BaseModel
from dataclasses import dataclass, field, fields
@dataclass
class Omega:
    om: str = "omega"
@dataclass
class A():
    a: int | None
    d: list[int]

@dataclass
class B():
    a_b: A
    c: str
    om: Omega = field(default_factory=Omega)

a = A(a=None, d=[3,6])

b = B(a_b=a, c="c")
# print(str(b))
# print(b.model_dump(by_alias=True))
print(str(b))
from pprint import pformat

# Convert to dict first, then pretty print
#print(pformat(b.model_dump(), width=40, sort_dicts=False))

def pretty_dataclass(obj, indent=0):
    if hasattr(obj, '__dataclass_fields__'):
        indent_str = "  " * indent
        field_strs = []
        for field in fields(obj):
            value = getattr(obj, field.name)
            if hasattr(value, '__dataclass_fields__'):
                field_strs.append(f"{indent_str}  {field.name}={pretty_dataclass(value, indent+1)}")
            else:
                field_strs.append(f"{indent_str}  {field.name}={value!r}")
        return f"{obj.__class__.__name__}(\n{',\n'.join(field_strs)},\n{indent_str})"
    return repr(obj)

print(pretty_dataclass(b))


b = B(
  a_b=A(
    a=None,
    d=[3, 6],
  ),
  c='c',
  om=Omega(
    om='omega',
  ),
)


from dataclasses import dataclass, asdict
from pprint import pprint

@dataclass
class A:
    a: int

@dataclass
class B:
    a_b: A
    c: str

a = A(a=8)
b = B(a_b=a, c="c")

# Convert to dict and pretty print
pprint(asdict(b), sort_dicts=False)

from rich.pretty import pprint
from rich import print as rprint
import rich.pretty
pprint(b, expand_all=True, )  # or
rprint(b, sep="(")
print(rich.pretty.pretty_repr(b, expand_all=True, indent_size=2))