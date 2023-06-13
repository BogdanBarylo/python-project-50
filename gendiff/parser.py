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
    for i in intersection_set:
        if dict_1.get(i) == dict_2.get(i):
            intersection_string.append({'key': i,
                                        'value': dict_1.get(i),
                                        'type': 'default'})
        else:
            intersection_string.append({'key': i,
                                        'value': dict_1.get(i),
                                        'type': 'removed'})
            intersection_string.append({'key': i,
                                        'value': dict_2.get(i),
                                        'type': 'added'})
    result_string = []
    result_string.extend(removed_string)
    result_string.extend(added_string)
    result_string.extend(intersection_string)
    return result_string