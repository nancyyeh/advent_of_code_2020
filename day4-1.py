import re


def clean_data():
    list_passport = []
    input_file = open("day4", "r")
    content = input_file.read()
    content_list = content.split("\n\n")
    for passport in content_list:
        passport_info_list = re.split(" |\n", passport)
        passport_dict = {}
        for key_value in passport_info_list:
            item = key_value.split(":")
            passport_dict[item[0]] = item[1]
        list_passport.append(passport_dict)
    return(list_passport)


def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False


def count_valid_passport(passport_list):
    counter = 0
    for passport_dict in passport_list:
        if check_key(passport_dict, 'byr') and check_key(passport_dict, 'iyr') and check_key(passport_dict, 'eyr') and check_key(passport_dict, 'hgt') and check_key(passport_dict, 'hcl') and check_key(passport_dict, 'ecl') and check_key(passport_dict, 'pid'):
            counter += 1
        print(passport_dict, counter)
    print(counter)


passports = clean_data()
count_valid_passport(passports)
