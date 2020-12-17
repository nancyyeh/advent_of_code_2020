def data_set():
    input_file = open("day10", "r")
    content = input_file.read()
    list_content = content.split("\n")
    for i, num in enumerate(list_content):
        list_content[i] = int(num)
    return list_content


def add_device_outlet(lst):
    lst.append(0)
    lst.append(max(lst)+3)
    return sorted(lst)


def product_differences_1_3(lst):
    diff_1 = 0
    diff_3 = 0
    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]
        if diff == 3:
            diff_3 += 1
        if diff == 1:
            diff_1 += 1
    return diff_1 * diff_3


adapter_list = data_set()
sorted_adapter_list = add_device_outlet(adapter_list)
print(product_differences_1_3(sorted_adapter_list))
