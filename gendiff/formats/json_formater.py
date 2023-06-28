import json


def make_view_json(data):
    formatted_data = json.dumps(data, indent=2)
    return formatted_data
