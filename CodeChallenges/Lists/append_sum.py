def append_sum(lst):
    for _ in range(0,3):
        lst.append(lst[-2] + lst[-1])
    return lst
