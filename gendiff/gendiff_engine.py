import json
import yaml
from gendiff.parser import find_diff
from gendiff.formats.choice_format import choice_format


def generate_diff(file1, file2, format='stylish'):
    dict_1 = make_argument(file1)
    dict_2 = make_argument(file2)
    diff_list = find_diff(dict_1, dict_2)
    result = choice_format(diff_list, format)
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
