def make_view(sorted_result):
    def make_level(node, level):
        indent = '    ' * level
        if node['type'] == 'container':
            children = list(map(lambda child: make_level(child, level + 1), node['value']))
            result_output = '\n'.join(children)
            return f"{indent}{node['key']}: {{\n{result_output}\n{indent}}}"
        elif node['type'] == 'added':
            return f"{indent}+ {node['key']}: {to_str(node['value'])}"
        else:
            return f"{indent}- {node['key']}: {to_str(node['value'])}"
    final_result = list(map(lambda node: make_level(node, 1), sorted_result))
    result = '{' + '\n' + '\n'.join(final_result) + '\n' + '}'
    return result


def to_str(value):
    if type(value) is bool:
        value = str(value).lower()
    return value
