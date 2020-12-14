import re


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
        unique_chars = set()
        for answer in group:
            for char in answer:
                unique_chars.add(char)
        counts_list.append(len(unique_chars))
    return sum(counts_list)


input_file = open("day6", "r")
content = input_file.read()
data_list = clean_data(content)
print(counts(data_list))
