import math


def row(seat_id_row_binary):
    min = 0
    max = 127
    for char in seat_id_row_binary[:7]:
        mid_point = (min + max)/2
        if char == 'F':
            max = int(math.floor(mid_point))
        if char == 'B':
            min = int(math.ceil(mid_point))
    return(min)


def column(seat_id_column_binary):
    min = 0
    max = 7
    for char in seat_id_column_binary[-3:]:
        mid_point = (min + max)/2
        if char == 'L':
            max = int(math.floor(mid_point))
        if char == 'R':
            min = int(math.ceil(mid_point))
    return(min)


def seat_id(seat_id_binary):
    return row(seat_id_binary) * 8 + column(seat_id_binary)


def find_max(input_data):
    max_id = seat_id(input_data[0])
    for seat_id_binary in input_data:
        seat = seat_id(seat_id_binary)
        if seat > max_id:
            max_id = seat
    return(max_id)


input_file = open("day5", "r")
content = input_file.read()
content_list = content.split("\n")
print(find_max(content_list))
