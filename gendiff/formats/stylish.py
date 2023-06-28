DEFAULT_INDENT = " " * 2


def make_view(sorted_result):
    def make_level(node, level):
        indent = DEFAULT_INDENT * level
        if node['type'] == 'container':
            children = list(map(lambda child:
                                make_level(child, level + 2), node['value']))
            result_output = '\n'.join(children)
            return f"  {indent}{node['key']}: {{\n{result_output}\n{indent}  }}"
        elif node['type'] == 'added':
            return (f"{indent}+ {node['key']}: "
                    f"{to_str(node['value'], level + 2)}")
        elif node['type'] == 'removed':
            return (f"{indent}- {node['key']}: "
                    f"{to_str(node['value'], level + 2)}")
        elif node['type'] == 'changed':
            return (f"{indent}- {node['key']}: "
                    f"{to_str(node['value_before'], level + 2)}\n"
                    f"{indent}+ {node['key']}: "
                    f"{to_str(node['value_after'], level + 2)}")
        else:
            return (f"{indent}  {node['key']}: "
                    f"{to_str(node['value'], level + 2)}")
    final_result = list(map(lambda node: make_level(node, 1), sorted_result))
    result = '{' + '\n' + '\n'.join(final_result) + '\n' + '}'
    return result


def to_str(value, level=1):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            formatted_body = (f'{DEFAULT_INDENT * (level + 1)}{k}: '
                              f'{to_str(v, level + 2)}')
            lines.append(formatted_body)
        lines.append(f'{DEFAULT_INDENT * (level - 1)}}}')
        return "\n".join(lines)
    else:
        return str(value)
