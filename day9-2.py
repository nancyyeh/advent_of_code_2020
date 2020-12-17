def data_set():
    input_file = open("day9", "r")
    content = input_file.read()
    list_content = content.split("\n")
    for i, num in enumerate(list_content):
        list_content[i] = int(num)
    return list_content


def list_contains_sum(lst, total):
    for i, num in enumerate(lst):
        if total - num in set(lst[i:]):
            return True
    return False


def invalid_number(lst, preamble):
    for i, num in enumerate(lst):
        if i < preamble:
            continue
        else:
            if not list_contains_sum(lst[i-preamble:i], num):
                return(num)


def find_list_return_sum_max_min_invalid_number(lst, invalid):
    for start_i in range(len(lst)):
        for end_i in range(start_i+1, len(lst)):
            if sum(lst[start_i:end_i]) == invalid and end_i - start_i > 1:
                return min(lst[start_i:end_i]) + max(lst[start_i:end_i])


list_numbers = data_set()
invalid_num = invalid_number(list_numbers, 25)
print(find_list_return_sum_max_min_invalid_number(list_numbers, invalid_num))
