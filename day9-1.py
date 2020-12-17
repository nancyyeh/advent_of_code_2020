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


list_numbers = data_set()
invalid_num = invalid_number(list_numbers, 25)
print(invalid_num)
