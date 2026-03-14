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

    print(report)

    if len(report) < 2:
        return False

    if len(report) < 3:
        if report[0] == report [1]:
            return False

    i = 1
    numberOfLevels = len(report)
    print('numberOfLevels', numberOfLevels)
    while (i < numberOfLevels - 1):
        print('i',i)
        previous = report[i-1]
        current = report[i]
        nextItem = report[i+1]
        print('previous:', previous)
        print('current:', current)
        print('nextItem:', nextItem)

        difNextCurr = nextItem - current
        difCurrPrev = current - previous
        print('difNextCurr', difNextCurr)
        print('difCurrPrev', difCurrPrev)

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
        if wasIncreasing and isDecreasing:
            return False
        elif wasDecreasing and isIncreasing:
            return False

        i += 1

    return True

file = open('./input')

safeLevels = 0
for report in file:
    levels = []
    for char in report:
        levels = [int(x) for x in report.split()]

    print(levels,isSafe(levels))
    if isSafe(levels):
        safeLevels += 1

print(safeLevels)
file.close()