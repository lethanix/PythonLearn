def middle_element(lst):
    x = len(lst)
    if len(lst) % 2 == 0:
        sum = lst[int(x / 2)] + lst[int(x / 2) - 1]
        return sum / 2
    else:
        return lst[int(x / 2)]
