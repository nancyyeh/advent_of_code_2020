import re

input_file = open("day7", "r")
content = input_file.read()
list_content = content.split("\n")


def strcutured_data():
    dictionary_bags = {}
    for line in list_content:
        line = line.strip()
        line_list = re.split(
            " bags contain | bags, | bag, | bags.| bag.", line)
        size = len(line_list)
        for idx in range(1, size-1):
            if line_list[idx] == "no other":
                dictionary_bags[line_list[0]] = None
            else:
                if line_list[0] in dictionary_bags:
                    dictionary_bags[line_list[0]].append(
                        (line_list[idx][2:], line_list[idx][0]))
                else:
                    dictionary_bags[line_list[0]] = [
                        (line_list[idx][2:], line_list[idx][0])]
    return dictionary_bags


memory_dict = set()


def count(input_data):
    def contains_shiny_gold(bag_color):
        if input_data[bag_color] == None:
            return False
        for sub_bag in input_data[bag_color]:
            if sub_bag[0] == "shiny gold":
                memory_dict.add(bag_color)
                return True
            if sub_bag[0] in memory_dict:
                return True
            elif contains_shiny_gold(sub_bag[0]):
                return True
        return False

    count = 0
    for bag_color, bags in input_data.items():
        if contains_shiny_gold(bag_color):
            count += 1
    return count


bags = strcutured_data()
print(count(bags))
print(memory_dict)
