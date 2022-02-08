lst = [int(i) for i in input().split()]
some_list = []


def chetValue(lstOut, lstIn: list) -> list:
    for i in lstOut:
        if i % 2 == 0 and i != 0:
            lstIn.append(i)
    return lstIn

print(chetValue(lst, some_list))
