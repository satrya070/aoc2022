with open('data/day_15ex.txt') as handle:
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
seekrow = 10

seekrow_ranges = []
seekrow_beacons = []

for sensor_beacon in sensors[6:]:

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


# calculate complete range
complete_range = []

print('done')
