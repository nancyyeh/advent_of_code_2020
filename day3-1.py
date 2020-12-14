input_file = open("day3", "r")
content = input_file.read()
content_list = content.split("\n")


def count_trees():
    counter = 0
    for i, line in enumerate(content_list):
        string = line.strip() * ((len(content_list)//len(line)+1)*3)
        if string[3*i] == '#':
            counter += 1
    print(counter)


count_trees()
