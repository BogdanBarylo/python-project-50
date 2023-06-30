DEFAULT_INDENT = " " * 2


def make_view(sorted_result):
    final_result = list(map(lambda node: make_level(node, 1), sorted_result))
    result = '{' + '\n' + '\n'.join(final_result) + '\n' + '}'
    return result


def make_level(node, level):
    indent = DEFAULT_INDENT * level
    node_type = node['type']
    if node_type in NODE_TO_STR:
        return NODE_TO_STR[node_type](node, level, indent)


def container_to_str(node, level, indent):
    children = list(map(lambda child: make_level(child, level + 2),
                        node['value']))
    result_output = '\n'.join(children)
    return f"  {indent}{node['key']}: {{\n{result_output}\n{indent}  }}"


def added_to_str(node, level, indent):
    return f"{indent}+ {node['key']}: {to_str(node['value'], level + 2)}"


def removed_to_str(node, level, indent):
    return f"{indent}- {node['key']}: {to_str(node['value'], level + 2)}"


def changed_to_str(node, level, indent):
    return (f"{indent}- {node['key']}: "
            f"{to_str(node['value_before'], level + 2)}\n"
            f"{indent}+ {node['key']}: "
            f"{to_str(node['value_after'], level + 2)}")


def default_to_str(node, level, indent):
    return f"{indent}  {node['key']}: {to_str(node['value'], level + 2)}"


NODE_TO_STR = {
    'container': container_to_str,
    'added': added_to_str,
    'removed': removed_to_str,
    'changed': changed_to_str,
    'default': default_to_str
}


def to_str(value, level=0):
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
