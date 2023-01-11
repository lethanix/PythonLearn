def remove_middle(lst, start, end):
    return [element for i, element in enumerate(lst) if i < start or i > end]


# def remove_middle(lst, start, end):
#     return lst[:start] lst[end+1:]
