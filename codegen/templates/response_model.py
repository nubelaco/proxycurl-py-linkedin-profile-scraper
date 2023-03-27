from __future__ import annotations
import sys
import typing

from enum import Enum

if sys.version_info >= (3, 8):
    from typing import TypedDict, List, Dict, Tuple, Optional
else:
    from typing_extensions import TypedDict
    from typing import List, Dict, Tuple, Optional


NoneType = type(None)
class UnknownType(object):
    pass


{%- for result_class in result_classes['enums'] %}


class {{result_class}}(Enum):
{%- for param in result_classes['enums'][result_class] %}
    {{param}} = {{result_classes['enums'][result_class][param]}}
{%- endfor %}

{%- endfor %}


{%- for result_class in result_classes['classes'] %}
{%- macro parse_datatype(datatype) %}
{%- if datatype['kind'] == 'basic' %}{{datatype['name']}}{%- endif %}
{%- if datatype['kind'] == 'record' %}{{datatype['name']}}{%- endif %}
{%- if datatype['kind'] == 'list' %}List[{{datatype['element']}}]{%- endif %}
{%- if datatype['kind'] == 'tuple' %}Tuple[{{", ".join(datatype['args'])}}]{%- endif %}
{%- if datatype['kind'] == 'typing' %}{{datatype['element']}}{%- endif %}
{%- endmacro %}


class {{result_class}}(TypedDict):
{%- for param in result_classes['classes'][result_class] %}
    {{param}}: {{parse_datatype(result_classes['classes'][result_class][param])}}
{%- endfor %}

{%- endfor %}

