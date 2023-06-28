from gendiff.formats.stylish import make_view
from gendiff.formats.plain import make_view_plain
from gendiff.formats.json_formater import make_view_json


def choice_format(sorted_result, format):
    if format == 'plain':
        return make_view_plain(sorted_result)
    elif format == 'json':
        return make_view_json(sorted_result)
    else:
        return make_view(sorted_result)
