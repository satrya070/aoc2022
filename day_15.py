import numpy as np

with open('data/day_15ex.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

with open('data/day_15.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]


def parse_sensors():
    sensors = []

    for line in lines:
        parts = line.split(' ')
        sensor_x, sensor_y = parts[2:4]
        beacon_x, beacon_y = parts[-2:]
            
        position_parsed = []
        for pos in [sensor_x, sensor_y, beacon_x, beacon_y]:
            position_parsed.append(int(''.join([x for x in pos if x.isdigit() or x == '-'])))
            
        sensor_x, sensor_y, beacon_x, beacon_y = position_parsed
        sensors.append((
            (sensor_x, sensor_y),
            (beacon_x, beacon_y)
        ))
    
    return sensors

# -----method---------
sensors = parse_sensors()
seekrow = 2000000  # 10

seekrow_ranges = []
seekrow_beacons = []

for sensor_beacon in sensors:

    sensor, beacon = sensor_beacon

    sensor_x, sensor_y = sensor
    beacon_x, beacon_y = beacon

    # manhatten distance
    sensor_reach = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    distance_seekrow = abs(seekrow - sensor_y)

    # sensor coverage does not reach seekrow
    if sensor_reach < distance_seekrow:
        continue

    # decides howmuch to grow from sides
    side_coverage = sensor_reach - distance_seekrow
    seekrow_coverage = side_coverage + 1 + side_coverage

    coverage_range = ((sensor_x - side_coverage), (sensor_x + side_coverage))

    seekrow_ranges.append(
        (coverage_range)
    )

    if beacon_y == seekrow:
        seekrow_beacons.append(beacon)

# merge to unique beacons
seekrow_beacons = list(set(seekrow_beacons))


def process_ranges(ranges):
    """
    ranges need to SORTED for this crap to actually work
    """
    # if one range just return it
    if len(ranges) == 1:
        return ranges
    
    processed = []

    for idx in range(len(ranges[:-1])):
        a_range_start, a_range_end = ranges[idx]
        b_range_start, b_range_end = ranges[idx + 1]

        # b is contained
        if a_range_start <= b_range_start and b_range_end <= a_range_end:
            processed.append((a_range_start, a_range_end))
            processed = processed + ranges[idx + 2:]

            return process_ranges(processed)
        
        # a is contained
        elif a_range_start >= b_range_start and a_range_end <= b_range_end:
            processed.append((b_range_start, b_range_end))
            processed = processed + ranges[idx + 2:]

            return process_ranges(processed)

        # b completely isolated (left)
        elif b_range_start < a_range_start and b_range_end < a_range_start:
            processed.append((a_range_start, a_range_end))

        # b completely isolated (right)
        elif b_range_start > a_range_end and b_range_end > a_range_end:
            processed.append((a_range_start, a_range_end))

        # b overlaps left
        elif b_range_start < a_range_start and a_range_start <= b_range_end < a_range_end:

            processed.append((b_range_start, a_range_end))
            processed = processed + ranges[idx + 2:]

            return process_ranges(processed)

        # b overlaps right
        else:
            processed.append((a_range_start, b_range_end))
            processed = processed + ranges[idx + 2:]

            return process_ranges(processed)
            
    
    return processed


# --------- main --------- #
seekrow_ranges = sorted(seekrow_ranges)
end_range = process_ranges(seekrow_ranges)


print('done?')

# test cases
test1 = process_ranges([(1, 3), (4, 5), (7, 9)])  # isolates
test2 = process_ranges([(1, 3), (-3, -1)])  # isolate left
test3 = process_ranges([(1, 2), (-3, 3), (4, 5)])  # a_contained -> isolates
test4 = process_ranges([(2, 6), (4, 9), (1, 4)])  # overlap right -> overlap left
test5 = process_ranges([(1, 2), (6, 8), (1, 7), (2, 2), (6, 10)])


print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

