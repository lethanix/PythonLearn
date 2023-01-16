def exponents(bases: list, powers: list):
    # raised = [0]*len(bases)
    raised = []
    for base in bases:
        for power in powers:
            raised.append(base ** power)
    return raised

if __name__ == "__main__":
    print(exponents([2,3,4], [2,3,4]))
