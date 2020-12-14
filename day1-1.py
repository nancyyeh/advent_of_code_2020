def sum_2020_product(list_nums):
    list_nums = set(list_nums)
    for num in list_nums:
        first_num = num
        second_num = 2020 - num
        if second_num in list_nums:
            return first_num * second_num


# test_nums = [1721, 979, 366, 299, 675, 1456]
# print(sum_2020_product(test_nums))

f = open("day1", "r")
input_list = []
for line in f:
    input_list.append(int(line.strip()))
f.close()

print(sum_2020_product(input_list))
