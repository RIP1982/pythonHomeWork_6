# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# Пример:
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]

newLst = []

def unic_list(lst):
    for i in range(len(lst)):
        if lst[i] not in lst[i+1::] and lst[i] not in lst[:i-1:]:
            newLst.append(lst[i])
    return newLst

print(f'{lst} => {unic_list((lst))}')



