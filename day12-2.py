def data_set():
    input_file = open("day12", "r")
    content = input_file.read()
    list_content = content.split("\n")
    return list_content

def go_thru_list_direction(lst):
    waypoint_EW, waypoint_EW_num = 'E', 10
    waypoint_NS, waypoint_NS_num = 'N', 1
    ship_EW, ship_EW_num = 'E', 0
    ship_NS, ship_NS_num = 'N', 0
    for action in lst:
        # print('action:', action[0], action[1:])

        # action for forward
        if action[0] == 'F':
            units_to_move_EW, units_direct_EW = int(
                action[1:]) * waypoint_EW_num, waypoint_EW
            units_to_move_NS, units_direct_NS = int(
                action[1:]) * waypoint_NS_num, waypoint_NS

            if units_direct_EW == ship_EW:
                ship_EW_num += units_to_move_EW
            else:
                ship_EW_num -= units_to_move_EW
                if ship_EW_num < 0:
                    if ship_EW == 'E':
                        ship_EW = 'W'
                    else:
                        ship_EW = 'E'
                    ship_EW_num = abs(ship_EW_num)
            if units_direct_NS == ship_NS:
                ship_NS_num += units_to_move_NS
            else:
                ship_NS_num -= units_to_move_NS
                if ship_NS_num < 0:
                    if ship_NS == 'N':
                        ship_NS = 'S'
                    else:
                        ship_NS = 'N'
                    ship_NS_num = abs(ship_NS_num)

        # action for turn
        if action[0] == 'R' or action[0] == 'L':
            if action[1:] == '180':
                if waypoint_EW == 'E':
                    waypoint_EW = 'W'
                else:
                    waypoint_EW = 'E'
                if waypoint_NS == 'N':
                    waypoint_NS = 'S'
                else:
                    waypoint_NS = 'N'
            if (action[0] == 'R' and action[1:] == '90') or (action[0] == 'L' and action[1:] == '270'):
                waypoint_EW_num, waypoint_NS_num = waypoint_NS_num, waypoint_EW_num
                if waypoint_NS == 'N' and waypoint_EW == 'E':
                    waypoint_NS = 'S'
                elif waypoint_EW == 'E' and waypoint_NS == 'S':
                    waypoint_EW = 'W'
                elif waypoint_NS == 'S' and waypoint_EW == 'W':
                    waypoint_NS = 'N'
                elif waypoint_EW == 'W' and waypoint_NS == 'N':
                    waypoint_EW = 'E'
            if (action[0] == 'R' and action[1:] == '270') or (action[0] == 'L' and action[1:] == '90'):
                waypoint_EW_num, waypoint_NS_num = waypoint_NS_num, waypoint_EW_num
                if waypoint_NS == 'N' and waypoint_EW == 'E':
                    waypoint_EW = 'W'
                elif waypoint_EW == 'E' and waypoint_NS == 'S':
                    waypoint_NS = 'N'
                elif waypoint_NS == 'S' and waypoint_EW == 'W':
                    waypoint_EW = 'E'
                elif waypoint_EW == 'W' and waypoint_NS == 'N':
                    waypoint_NS = 'S'
        # action for E/W updated
        if action[0] == 'E' or action[0] == 'W':
            if waypoint_EW == action[0]:
                waypoint_EW_num += int(action[1:])
            else:
                waypoint_EW_num -= int(action[1:])
                if waypoint_EW_num < 0:
                    if waypoint_EW == 'E':
                        waypoint_EW = 'W'
                    else:
                        waypoint_EW = 'E'
                    waypoint_EW_num = abs(waypoint_EW_num)
        # action for N/S updated
        if action[0] == 'N' or action[0] == 'S':
            if waypoint_NS == action[0]:
                waypoint_NS_num += int(action[1:])
            else:
                waypoint_NS_num -= int(action[1:])
                if waypoint_NS_num < 0:
                    if waypoint_NS == 'N':
                        waypoint_NS = 'S'
                    else:
                        waypoint_NS = 'N'
                    waypoint_NS_num = abs(waypoint_NS_num)
        # print('ship:', ship_EW, ship_EW_num, ship_NS, ship_NS_num)
        # print('waypoint:', waypoint_EW, waypoint_EW_num, waypoint_NS, waypoint_NS_num, '\n')
    return ship_EW_num + ship_NS_num


list_direction = data_set()
print(go_thru_list_direction(list_direction))
