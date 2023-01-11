def more_frequent_item(lst, item1, item2):
    n1 = lst.count(item1)
    n2 = lst.count(item2)
    if n1 >= n2:
        return item1
    return item2
