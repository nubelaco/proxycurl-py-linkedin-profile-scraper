import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, List, Dict, Tuple
else:
    from typing_extensions import TypedDict
    from typing import List, Dict, Tuple

{%- for result_class in result_classes %}
{%- macro parse_datatype(datatype) %}
{%- if datatype['kind'] == 'basic' %}{{datatype['name']}}{%- endif %}
{%- if datatype['kind'] == 'record' %}{{datatype['name']}}{%- endif %}
{%- if datatype['kind'] == 'list' %}List[{{datatype['element']}}]{%- endif %}
{%- if datatype['kind'] == 'tuple' %}Tuple[{{", ".join(datatype['args'])}}]{%- endif %}
{%- endmacro %}


class {{result_class}}(TypedDict):
{%- for param in result_classes[result_class] %}
    {{param}}: {{parse_datatype(result_classes[result_class][param])}}
{%- endfor %}

{%- endfor %}

