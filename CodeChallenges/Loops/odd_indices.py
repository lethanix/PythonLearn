def odd_indices(lst: list):
    odd = []
    for idx in range(1, len(lst), 2):
        odd.append(lst[idx])
    return odd


if __name__ == "__main__":
    print(odd_indices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
