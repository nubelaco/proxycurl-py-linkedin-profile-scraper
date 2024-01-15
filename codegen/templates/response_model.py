from enum import Enum, auto
from typing import Optional, List, Tuple
import sys
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict



{%- for enum in enums %}


class {{enum}}(Enum):
{%- for member in enums[enum] %}
    {{member}} = auto()
{%- endfor %}
{%- endfor %}



{%- macro parse_datatype(datatype) %}
{%- if datatype['nullable'] == true %}{{"Optional["}}{%- endif %}
{%- if datatype['type'] == 'basic' %}{{datatype['value']}}{%- endif %}
{%- if datatype['type'] == 'object' %}{{datatype['value']}}{%- endif %}
{%- if datatype['type'] == 'list' %}List[{{datatype['value']}}]{%- endif %}
{%- if datatype['type'] == 'tuple' %}Tuple[{{", ".join(datatype['value'])}}]{%- endif %}
{%- if datatype['nullable'] == true %}{{"]"}}{%- endif %}
{%- endmacro %}
{%- for result_class in result_classes %}


class {{result_class}}(TypedDict):
{%- for param in result_classes[result_class] %}
    {{param}}: {{parse_datatype(result_classes[result_class][param])}}
{%- endfor %}
{%- endfor %}

