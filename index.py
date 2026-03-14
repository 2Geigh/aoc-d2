import os

def isSafe(report: [int]) -> bool:
    """
    A predicate for:
        1. Levels (report elements) are all decreasing or all increasing
        2. No two adjascent levels differ by less than 1 or more than 3.

    EXAMPLES:

    >>> isSafe([])
    False

    >>> isSafe([99])
    False

    >>> isSafe([0, 0])
    False

    >>> isSafe([0, 3])
    True

    >>> isSafe([3, 0])
    True

    >>> isSafe([0, 1, 0])
    False

    >>> isSafe([0, 4])
    False

    """

    if len(report) < 2:
        return False

    if len(report) < 3:
        if report[0] == report [1]:
            return False

    i = 1
    while (i < len(report) - 1):
        previous = report[i-1]
        current = report[i]
        nextItem = report[i+1]

        difNextCurr = nextItem - current
        difCurrPrev = current - previous

        # Condition 1
        if abs(difCurrPrev) > 3:
            return False
        elif abs(difCurrPrev) < 1:
            return False

        # Condition 1
        if abs(difNextCurr) > 3:
            return False
        elif abs(difNextCurr) < 1:
            return False

        # We can infer these conditions because we already filtered out
        # constant element pairs with pairs with condition 1
        wasIncreasing = difCurrPrev > 0
        wasDecreasing = difCurrPrev < 0
        isIncreasing = difNextCurr > 0
        isDecreasing = difNextCurr < 0

        # Condition 2
        if wasIncreasing and isIncreasing:
            return True
        elif wasDecreasing and isDecreasing:
            return True

        i += 1

    return False

file = open('./input')

for report in file:
    levels = []
    for char in report:
        if char.strip() != "":
            levels.append(int(char))
    print(levels)

file.close()