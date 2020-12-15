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
                        (line_list[idx][2:], int(line_list[idx][0])))
                else:
                    dictionary_bags[line_list[0]] = [
                        (line_list[idx][2:], int(line_list[idx][0]))]
    return dictionary_bags


bags_structured_dict = strcutured_data()
total_bags_dict = {}


def contains_total_other_bags_within_bag_color(bag_color, total_bags_dict):
    if bags_structured_dict[bag_color] == None:
        total_bags_dict[bag_color] = 0
        return 0
    if bag_color in total_bags_dict:
        return total_bags_dict[bag_color]
    else:
        counter = 0
        for bags in bags_structured_dict[bag_color]:
            counter += bags[1] + bags[1] * \
                contains_total_other_bags_within_bag_color(
                    bags[0], total_bags_dict)
        total_bags_dict[bag_color] = counter
        return counter


print(contains_total_other_bags_within_bag_color(
    'shiny gold', total_bags_dict))
