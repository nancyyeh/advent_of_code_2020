def data_set():
    input_file = open("day13", "r")
    content = input_file.read()
    list_content = content.split("\n")
    return list_content


data = data_set()
timestamp = int(data[0])
buses_time = data[1].split(",")
buses_times_clean = []

for bus_time in buses_time:
    if bus_time != 'x':
        buses_times_clean.append(int(bus_time))


def closest_time_to_timestamp(bus_id, timestamp):
    counter = 0
    total_time = 0
    while total_time < timestamp:
        total_time += int(bus_id)
        counter += 1
    return total_time-timestamp


# print(buses_times_clean)


def closest_bus(buses_times, time):
    smallest_busid = buses_times[0]
    smallest_time = closest_time_to_timestamp(buses_times[0], time)

    for bus_id in buses_times:
        # print(bus_id)
        time = closest_time_to_timestamp(bus_id, timestamp)
        if time < smallest_time:
            smallest_busid = bus_id
            smallest_time = time
        # print(bus_id, time, bus_id*time, smallest_busid)
    return smallest_busid * smallest_time


print(closest_bus(buses_times_clean, timestamp))
