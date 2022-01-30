# This is the code for finding the largest and smallest element in a list

def most_elem(list1):
    ab = 0
    k = ''
    for i in list1:
        if list1.count(i) > ab:
            ab = list1.count(i)
            k = i
    return k


def min_elem(list2):
    ab = len(list2)
    k = ''
    for i in list2:
        if list2.count(i) <= ab:
            ab = list2.count(i)
            k = i
    return k
