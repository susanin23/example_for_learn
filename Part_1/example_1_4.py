"""
Вывести на экран числа 5, 10, и 21 одно под другим.
"""

target_list = [5, 10, 21]
i = 0
while True:
    print(target_list[i])
    i += 1
    if i == 3:
        break
