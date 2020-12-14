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


def your_seat_num(input_data):
    seat_id_list = []
    for seat_id_binary in input_data:
        seat = seat_id(seat_id_binary)
        seat_id_list.append(seat)
    return sorted(set(range(seat_id_list[0], seat_id_list[-1])) - set(seat_id_list))


input_file = open("day5", "r")
content = input_file.read()
content_list = content.split("\n")
print(your_seat_num(content_list))
