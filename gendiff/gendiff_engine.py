import json, yaml
from gendiff.parser import find_diff


def generate_diff(file1, file2):
    dict_1 = make_argument(file1)
    dict_2 = make_argument(file2)
    diff_list = find_diff(dict_1, dict_2)
    result = get_sort(diff_list)
    return result


def make_argument(path):
    check_format = path.split(".")[-1]
    if check_format == 'json':
        with open(path, 'r') as f:
            content = json.load(f)
            new_dict = dict(content)
        return new_dict
    elif check_format == 'yml' or check_format == 'yaml':
        with open(path, 'r') as f:
            content = yaml.load(f, Loader=yaml.Loader)
            new_dict = dict(content)
        return new_dict


def get_sort(diff_string):
    sorted_string = sorted(diff_string, key=lambda x: x['key'][0])
    sorted_result = []
    for x in sorted_string:
        if x['type'] == 'added':
            sorted_result.append(f"  + {x['key']}: {to_str(x['value'])}")
        elif x['type'] == 'removed':
            sorted_result.append(f"  - {x['key']}: {to_str(x['value'])}")
        else:
            sorted_result.append(f"    {x['key']}: {to_str(x['value'])}")
    result = '{' + '\n' + '\n'.join(sorted_result) + '\n' + '}'
    return result


def to_str(value):
    if type(value) is bool:
        value = str(value).lower()
    return value
