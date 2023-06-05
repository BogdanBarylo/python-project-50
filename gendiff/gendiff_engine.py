import json


def generate_diff(file1, file2):
    f1 = json.load(open('json_test_files/' + file1, 'r')) # скорее всего запись не верная, нужно переделать
    f2 = json.load(open('json_test_files/' + file2,'r'))
    diff = []
    diff_minus = [] # очень много ресурсов для сортировки, тем более это будет как-то по дурацки
    diff_plus = [] 
    for first, second in zip(f1 ,f2): # вроде first = f1.keys()//// вообще логика плохая, если будет не равно количество элементов
        if first == second:                                        #то остаток не добавится, и мы получим не верный ответ
            if f1[first] == f2[second]:
                diff.append(f1)            #спросить Глеба про логику
            elif f1[first] != f2[second]:
                diff_minus.append(f1)
                diff_plus.append(f2)
        else:
            diff_minus.append(f1)
            diff_plus.append(f2)
    f1.close()
    f2.close()
    return make_correct_view(diff, diff_minus, diff_plus) # cкорее всего результат не будет выглядеть как список, может если добавить +\n то ок
    

def make_correct_view(diff, diff_minus, diff_plus):
    diff.extend(diff_minus).extend(diff_plus)
    diff.sort()
    for i in diff:
        if i in diff_minus:             
            i = '- ' + ''.join(i)
        elif i in diff_plus:
            i = '+ ' + ''.join(i)
        else:
            continue
    return diff
