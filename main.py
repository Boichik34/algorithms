
def found_near(str):
    massiv = str.split('\n')
    target = int(massiv[-1])
    lst = massiv[0].split()
    dif = 20002
    i = target
    for el in lst:
        if target - int(el) == 0:
            return int(el)
        if abs(target - int(el)) <= dif and int(el) != i:
            if abs(target - int(el)) < dif:
                dif = abs(target - int(el))
                i = int(el)
                j = None
            else:
                j = int(el)
    if j == None:
        return i
    else:
        return f'{i} или {j}'


def count_worlds(strinng: str) -> int:
    count = len(set(strinng.split()))
    return count

def count_worlds_2(strr: str) -> int:
    lst = strr.split()
    lst_2 = []
    for el in lst:
        if el not in lst_2:
            lst_2.append(el)
    return len(lst_2)



