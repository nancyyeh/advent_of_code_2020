def sum_2020_product(list_nums):
    set_list_nums = set(list_nums)
    for i, num1 in enumerate(list_nums):
        second_total = 2020 - num1
        for num2 in list_nums[i+1:]:
            num3 = second_total - num2
            if num3 in set_list_nums:
                return num1 * num2 * num3


# test_nums = [1721, 979, 366, 299, 675, 1456]
# print(sum_2020_product(test_nums))

f = open("day1", "r")
input_list = []
for line in f:
    input_list.append(int(line.strip()))
f.close()

print(sum_2020_product(input_list))
