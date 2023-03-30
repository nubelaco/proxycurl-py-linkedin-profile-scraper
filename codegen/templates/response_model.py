from __future__ import annotations
import sys
import typing

from enum import Enum, auto

if sys.version_info >= (3, 8):
    from typing import TypedDict, List, Tuple, Optional
else:
    from typing_extensions import TypedDict
    from typing import List, Tuple, Optional



{%- for result_class in result_classes['enums'] %}


class {{result_class}}(Enum):
{%- for param in result_classes['enums'][result_class] %}
    {{param}} = auto()
{%- endfor %}

{%- endfor %}


{%- for result_class in result_classes['classes'] %}
{%- macro parse_datatype(datatype) %}
{%- if datatype['type'] == 'basic' or datatype['type'] == 'object'%}{{datatype['value'] if datatype['nullable'] == False else 'Optional[' + datatype['value'] + ']'}}{%- endif %}
{%- if datatype['type'] == 'list' %}{{"List[" + datatype['value'] + "]" if datatype['nullable'] == False else "Optional[List[" + datatype['value'] + "]]"}}{%- endif %}
{%- if datatype['type'] == 'tuple' %}{{"Tuple[" + ", ".join(datatype['value']) + "]" if datatype['nullable'] == False else "Optional[Tuple[" + ", ".join(datatype['value']) + "]]"}}{%- endif %}
{%- endmacro %}


class {{result_class}}(TypedDict):
{%- for param in result_classes['classes'][result_class] %}
    {{param}}: {{parse_datatype(result_classes['classes'][result_class][param])}}
{%- endfor %}

{%- endfor %}

