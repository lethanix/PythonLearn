def double_index(lst, index):
    if index >= len(lst):
        return lst
    new_lst = lst[0:index]
    new_lst.append(lst[index] * 2)
    return new_lst + lst[index + 1 :]
