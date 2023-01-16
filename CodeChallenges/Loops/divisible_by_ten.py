def divisible_by_ten(nums: list):
    counter = 0
    for value in nums:
        if value % 10 == 0:
            counter += 1
    return counter

if __name__ == "__main__":
    print(divisible_by_ten([12, 23, 34, 3, 39,40, 80]))
