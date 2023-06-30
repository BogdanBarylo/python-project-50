from gendiff.formats.stylish import make_view
from gendiff.formats.plain import make_view_plain
from gendiff.formats.json_formater import make_view_json


def select_format(format):
    if format == 'plain':
        return make_view_plain
    elif format == 'json':
        return make_view_json
    elif format == 'stylish':
        return make_view
    else:
        raise Exception("Your format isn't correct, chose correct format")
