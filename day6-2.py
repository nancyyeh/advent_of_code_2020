import re
from collections import Counter


def clean_data(input_data):
    result = []
    group_list = input_data.split("\n\n")
    for answer_yes in group_list:
        answer_yes = answer_yes.split("\n")
        result.append(answer_yes)
    return(result)


def counts(input_data):
    counts_list = []
    for group in input_data:
        size_group = len(group)
        num_all_yes = 0
        joined_chars = []
        for answer in group:
            joined_chars += answer
            counter_dict = Counter(joined_chars)
            for char, count in counter_dict.items():
                if count == size_group:
                    num_all_yes += 1
        counts_list.append(num_all_yes)
    print(sum(counts_list))


input_file = open("day6", "r")
content = input_file.read()
data_list = clean_data(content)
counts(data_list)
