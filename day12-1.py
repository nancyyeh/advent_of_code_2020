def data_set():
    input_file = open("day12", "r")
    content = input_file.read()
    list_content = content.split("\n")
    return list_content


def go_thru_list_direction(lst):
    curr_EW, curr_EW_num = 'E', 0
    curr_NS, curr_NS_num = 'N', 0
    curr_facing = 'E'
    direction = ['N', 'E', 'S', 'W']
    for action in lst:
        # print('action:', action[0], action[1:])
        # action for forward
        if action[0] == 'F':
            if curr_facing == 'E' or curr_facing == 'W':
                if curr_facing == curr_EW:
                    curr_EW_num += int(action[1:])
                else:
                    curr_EW_num -= int(action[1:])
                    if curr_EW_num < 0:
                        if curr_EW == 'E':
                            curr_EW = 'W'
                        else:
                            curr_EW = 'E'
                        curr_EW_num = abs(curr_EW_num)
            if curr_facing == 'S' or curr_facing == 'N':
                if curr_facing == curr_NS:
                    curr_NS_num += int(action[1:])
                else:
                    curr_NS_num -= int(action[1:])
                    if curr_NS_num < 0:
                        if curr_NS == 'N':
                            curr_NS = 'S'
                        else:
                            curr_NS = 'N'
                        curr_NS_num = abs(curr_NS_num)
        # action for turn
        if action[0] == 'R' or action[0] == 'L':
            steps = int(int(action[1:]) / 90)
            curr_facing_idx = direction.index(curr_facing)
            if action[0] == 'R':
                new_direction_idx = curr_facing_idx + steps
            if action[0] == 'L':
                new_direction_idx = curr_facing_idx - steps
            if new_direction_idx < 0:
                new_direction_idx += 4
            if new_direction_idx > 3:
                new_direction_idx -= 4
            curr_facing = direction[new_direction_idx]
            # print('steps:', steps, curr_facing_idx, new_direction_idx)
        # action for E/W
        if action[0] == 'E' or action[0] == 'W':
            if curr_EW == action[0]:
                curr_EW_num += int(action[1:])
            else:
                curr_EW_num -= int(action[1:])
                if curr_EW_num < 0:
                    if curr_EW == 'E':
                        curr_EW = 'W'
                    else:
                        curr_EW = 'E'
                    curr_EW_num = abs(curr_EW_num)
        # action for N/S
        if action[0] == 'N' or action[0] == 'S':
            if curr_NS == action[0]:
                curr_NS_num += int(action[1:])
            else:
                curr_NS_num -= int(action[1:])
                if curr_NS_num < 0:
                    if curr_NS == 'N':
                        curr_NS = 'S'
                    else:
                        curr_NS = 'N'
                    curr_NS_num = abs(curr_NS_num)
        # print(curr_EW, curr_EW_num, curr_NS, curr_NS_num, curr_facing, '\n')
    return curr_EW_num + curr_NS_num


list_direction = data_set()
print(go_thru_list_direction(list_direction))
