import os

def isSafe(report: [int]) -> bool:
    """
    A predicate for:
        1. Levels (report elements) are all decreasing or all increasing
        2. No two adjascent levels differ by less than 1 or more than 3.

    EXAMPLES:

    >>> isSafe([])
    false

    >>> isSafe([99])
    false

    >>> isSafe([0, 0])
    false

    >>> isSafe([0, 3])
    true

    >>> isSafe([3, 0])
    true

    >>> isSafe([0, 1, 0])
    false

    >>> isSafe([0, 4])
    false

    """

    if len(report) < 2:
        return false

    if len(report < 3):
        if report[0] == report [1]:
            return false

    i = 1
    while (i < len(report) - 1):
        previous = report[i-1]
        current = report[i]
        nextItem = report[i+1]

        difNextCurr = nextItem - current
        difCurrPrev = current - previous

        # Condition 1
        if abs(difCurrPrev) > 3:
            return false
        elif abs(difCurrPrev) < 1:
            return false

        # Condition 1
        if abs(difNextCurr) > 3:
            return false
        elif abs(difNextCurr) < 1:
            return false

        # We can infer these conditions because we already filtered out
        # constant element pairs with pairs with condition 1
        wasIncreasing = difCurrPrev > 0
        wasDecreasing = difCurrPrev < 0
        isIncreasing = difNextCurr > 0
        isDecreasing = difNextCurr < 0

        # Condition 2
        if wasIncreasing and isIncreasing:
            return true
        elif wasDecreasing and isDecreasing:
            return true

    return false

file = open('./input')

for report in file:
    levels = []
    for char in report:
        if char.strip() != "":
            levels.append(int(char))
    print(levels)

file.close()