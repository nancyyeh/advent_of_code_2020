import re
from collections import Counter
input_file = open("day2", "r")


def count_valid_password():
    counter = 0
    for line in input_file:
        string = line.strip()
        string_list = re.split(' |-', string)
        min_num = int(string_list[0])
        max_num = int(string_list[1])
        char = string_list[2][0]
        password = string_list[3]
        counted = Counter(password)
        if min_num <= counted[char] <= max_num:
            counter += 1

    print(counter)


count_valid_password()

input_file.close()
