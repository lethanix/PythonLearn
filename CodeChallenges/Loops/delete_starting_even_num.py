def delete_starting_evens(lst: list):
    while len(lst) and lst[0] % 2 == 0:
        lst.pop(0)

    return lst


# def delete_starting_evens(lst):
#     while len(lst) > 0 and lst[0] % 2 == 0:
#         lst = lst[1:]
#         return lst


if __name__ == "__main__":
    print(delete_starting_evens([3, 5, 7, 4, 3, 3]))
    print(delete_starting_evens([]))
