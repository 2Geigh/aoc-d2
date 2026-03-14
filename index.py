import os

file = open('./input')

for report in file:
    levels = []
    for char in report:
        if char.strip() != "":
            levels.append(int(char))
    print(levels)

file.close()