import math
input_file = open("day3", "r")
content = input_file.read()
content_list = content.split("\n")

list_paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(right, down):
    counter = 0
    curr = 1
    for i, line in enumerate(content_list):
        if i == 0:
            continue
        elif i % down == 0:
            string = line.strip() * ((len(content_list)//len(line)+1)*right)
            if string[right * curr] == '#':
                counter += 1
            curr += 1
    return counter


def paths(paths):
    lst = []
    for path in paths:
        lst.append(count_trees(path[0], path[1]))
    print(lst, math.prod(lst))


paths(list_paths)
