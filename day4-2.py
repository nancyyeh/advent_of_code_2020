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
        if key == 'byr' and 1920 <= int(dictionary[key]) <= 2002:
            return True
        if key == 'iyr' and 2010 <= int(dictionary[key]) <= 2020:
            return True
        if key == 'eyr' and 2020 <= int(dictionary[key]) <= 2030:
            return True
        if key == 'hgt':
            height = dictionary[key]
            if height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193:
                return True
            if height[-2:] == 'in' and 59 <= int(height[:-2]) <= 76:
                return True
        if key == 'hcl' and dictionary[key][0] == '#' and len(dictionary[key]) == 7:
            if bool(re.match("[0-9]|[a-f]", dictionary[key][1])) and bool(re.match("[0-9]|[a-f]", dictionary[key][2])) and bool(re.match("[0-9]|[a-f]", dictionary[key][3])) and bool(re.match("[0-9]|[a-f]", dictionary[key][4])) and bool(re.match("[0-9]|[a-f]", dictionary[key][5])) and bool(re.match("[0-9]|[a-f]", dictionary[key][6])):
                return True
        if key == 'ecl':
            options = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
            if dictionary[key] in options:
                return True
        if key == 'pid' and bool(re.search(re.compile('^[0-9]+$'), dictionary[key])) and len(dictionary[key]) == 9:
            return True

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
