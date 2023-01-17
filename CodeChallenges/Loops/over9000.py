def over_nine_thousand(lst: list):
    if not lst:
        return 0

    total = 0
    for number in lst:
        total += number
        if total > 9_000:
            break # return total
    return total
