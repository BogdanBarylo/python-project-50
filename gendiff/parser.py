def find_diff(dict_1, dict_2):
    set_keys_1 = set(dict_1.keys())
    set_keys_2 = set(dict_2.keys())
    intersection_set = set_keys_1.intersection(set_keys_2)
    only_diff_keys_1 = set_keys_1 - set_keys_2
    only_diff_keys_2 = set_keys_2 - set_keys_1
    removed_string = [{'key': x, 'value': dict_1.get(x), 'type': 'removed'}
                      for x in only_diff_keys_1]
    added_string = [{'key': x, 'value': dict_2.get(x), 'type': 'added'}
                    for x in only_diff_keys_2]
    intersection_string = []
    for key in intersection_set:
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)
        if value_1 == value_2:
            intersection_string.append({'key': key,
                                        'value': value_1,
                                        'type': 'default'})
        elif isinstance(value_1, dict) and isinstance(value_2, dict):
            intersection_string.append({'key': key,
                                        'value': find_diff(value_1, value_2),
                                        'type': 'container'})
        else:
            intersection_string.append({'key': key,
                                        'value_before': value_1,
                                        'value_after': value_2,
                                        'type': 'changed'})
    result = []
    result.extend(removed_string)
    result.extend(added_string)
    result.extend(intersection_string)
    sorted_result = make_sort(result)
    return sorted_result


def make_sort(result):
    sorted_result = sorted(result, key=lambda x: x['key'])
    return sorted_result
