# This is the code for finding the largest and smallest element in a list

def most_elem(list1):
    d = {}
    
    for x in set(list1):
        d[x] = list1.count(x)
    ss = sorted(d.values())
    for k, v in d.items():
        if v == ss[-1]:
            return k


def min_elem(list2):
    d = {}
    if '\n' in list2:
        list2.remove('\n')

    for x in set(list2):
        d[x] = list2.count(x)
    ss = sorted(d.values())
    for k, v in d.items():
        if v == ss[0]:
            return k
