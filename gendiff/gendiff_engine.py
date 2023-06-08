import json



def generate_diff(file1, file2):
    dict_1 = make_argument(file1)
    dict_2 = make_argument(file2)
    diff_list = find_diff(dict_1, dict_2)
    sorted_result = get_sort(diff_list)
    result = make_view(sorted_result)
    return result


def make_argument(path):
    with open(path, 'r') as f:
        content = json.load(f)
        new_dict = dict(content)
    return new_dict


def find_diff(dict_1, dict_2):
    set_keys_1 = set(dict_1.keys())
    set_keys_2 = set(dict_2.keys())
    intersection_set = set_keys_1.intersection(set_keys_2)
    only_diff_keys_1 = set_keys_1 - set_keys_2
    only_diff_keys_2 = set_keys_2 - set_keys_1
    removed_string =[{'key': x, 'value': dict_1.get(x), 'type': 'removed'} for x in only_diff_keys_1]
    added_string = [{'key': x, 'value': dict_2.get(x), 'type': 'added'} for x in only_diff_keys_2]
    intersection_string = []
    for i in intersection_set:
        if dict_1.get(i) == dict_2.get(i):
            intersection_string.append({'key': i, 'value': dict_1.get(i), 'type': 'default'})
        else:
            intersection_string.append({'key': i, 'value': dict_1.get(i), 'type': 'removed'})
            intersection_string.append({'key': i, 'value': dict_2.get(i), 'type': 'added'})
    result_string = []
    result_string.extend(removed_string)
    result_string.extend(added_string)
    result_string.extend(intersection_string)
    return result_string
    

def get_sort(diff_string):
    sorted_string = sorted(diff_string, key=lambda x: x['key'][0])
    sorted_result = []
    for x in sorted_string:
        if x['type'] == 'added':
            sorted_result.append(f"+ {x['key']}: {x['value']}")
        elif x['type'] == 'removed':
            sorted_result.append(f"- {x['key']}: {x['value']}")
        else:
            sorted_result.append(f"  {x['key']}: {x['value']}")
    return sorted_result


def make_view(sorted_result):
    result = '\n'.join(sorted_result)                                   #Спросить Глеба насчет неймингов, норм ли 3 раза переписывать переменную
    result = result.replace('True','true').replace('False','false')
    result = '{' + '\n' + result + '\n' +'}'
    return result

        