def make_view_plain(sorted_result):
    def walk(node, path):
        name = node['key']
        if node['type'] == 'container':
            children = list(map(
                lambda child: walk(child, path + name + '.'), node['value']))
            result_output = '\n'.join(list(filter(
                lambda x: x != '', children)))
            return result_output
        if node['type'] == 'added':
            return (f"Property '{path + name}' was added "
                    f"with value: {to_str(node['value'])}")
        elif node['type'] == 'removed':
            return f"Property '{path + name}' was removed"
        elif node['type'] == 'changed':
            return (f"Property '{path + name}' was updated. "
                    f"From {to_str(node['value_before'])} "
                    f"to {to_str(node['value_after'])}")
        else:
            return ''
    result = list(map(lambda node: walk(node, ''), sorted_result))
    final_result = '\n'.join(list(filter(lambda x: x != '', result)))
    return final_result


def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return str(value)
    else:
        return f"'{str(value)}'"
