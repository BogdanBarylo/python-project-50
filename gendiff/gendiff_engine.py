import json
import yaml
from gendiff.parser import find_diff
from gendiff.formats.choice_format import select_format


def generate_diff(file1, file2, format='stylish'):
    dict_1 = make_argument(file1)
    dict_2 = make_argument(file2)
    diff_list = find_diff(dict_1, dict_2)
    formater = select_format(format)
    result = formater(diff_list)
    return result


def make_argument(path):
    content_and_extension = get_file_content_and_extension(path)
    new_argument = get_dict(*content_and_extension)
    return new_argument


def get_file_content_and_extension(path):
    check_extension = path.split(".")[-1]
    with open(path, 'r') as f:
        content = f.read()
    result = (check_extension, content)
    return result


def get_dict(check_extension, content):
    if check_extension == 'json':
        result = json.loads(content)
        return dict(result)
    elif check_extension == 'yml' or check_extension == 'yaml':
        result = yaml.load(content, Loader=yaml.Loader)
        return dict(result)
