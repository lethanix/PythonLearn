def larger_sum(lst1: list, lst2: list):
    sum1 = 0
    sum2 = 0

    for num in lst1:
        sum1 += num

    for num in lst2:
        sum2 += num

    if sum2 > sum1:
        return lst2
    return lst1


def larger_sum_oneliner(lst1: list, lst2: list) -> list:
    return lst2 if sum(lst2) > sum(lst1) else lst1


if __name__ == "__main__":
    print(larger_sum([1, 9, 5], [2, 3, 7]))
    print(larger_sum_oneliner([1, 9, 5], [2, 3, 7]))
