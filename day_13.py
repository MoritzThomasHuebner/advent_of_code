import numpy as np

# earliest_time = 939
# bus_ids = [7, 13, 'x', 'x', 59, 'x', 31, 19]
#
earliest_time = 1006605
bus_ids = [19, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 37, 'x', 'x', 'x', 'x', 'x', 883, 'x', 'x',
           'x', 'x', 'x', 'x', 'x', 23, 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 'x', 'x', 'x',
           'x', 'x', 'x', 'x', 'x', 'x', 797, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 41, 'x', 'x', 'x', 'x', 'x',
           'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 29]

# bus_ids = [1789,37,47,1889]

lowest_waiting_time = np.inf
lowest_waiting_bus_id = np.nan

for bus_id in bus_ids:
    if bus_id == 'x':
        continue
    waiting_time = bus_id - (earliest_time % bus_id)
    if waiting_time < lowest_waiting_time:
        lowest_waiting_time = waiting_time
        lowest_waiting_bus_id = bus_id

print(lowest_waiting_time * lowest_waiting_bus_id)

# Part 2

def check_departures(t, bus_ids):
    for i, bus_id in enumerate(bus_ids):
        if bus_id == 'x':
            continue
        condition = (t + i) % bus_id
        if condition != 0:
            return False
    return True


def find_t_naive(bus_ids):
    t = 0
    while check_departures(t=t, bus_ids=bus_ids) is False:
        t += 1
    return t


def find_t_somwhat_smart(bus_ids):
    max_id = 0
    max_index = 0
    for i, bus_id in enumerate(bus_ids):
        if bus_id == 'x':
            continue
        if bus_id > max_id:
            max_id = bus_id
            max_index = i
    t = max_id - max_index
    i = 0
    while check_departures(t=t, bus_ids=bus_ids) is False:
        t += max_id
        i += 1
        if i % 1000000 == 0:
            print(t)
    return t


def find_t_really_smart(bus_ids):
    t = 0
    buses = [(i, b) for i, b in enumerate(bus_ids) if isinstance(b, int)]
    step = 1
    for i, bus in buses:
        t += step
        while (t + i) % bus != 0:
            t += step
        step *= bus
    return t


print(find_t_really_smart(bus_ids=bus_ids))
