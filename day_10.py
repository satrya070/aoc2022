with open('data/day_10ex.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

with open('data/day_10.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

X = 1
intervals = [20, 60, 100, 140, 180, 220]
interval_results = []
cycles = 0

for line in lines:

    if line == 'noop':
        for cycle in range(1):
            cycles += 1

            if cycles in intervals:
                interval_val = intervals[intervals.index(cycles)] * X
                interval_results.append(interval_val) 

    else:
        for cycle in range(2):
            cycles += 1

            if cycles in intervals:
                interval_val = intervals[intervals.index(cycles)] * X
                interval_results.append(interval_val) 
        
        val = int(line.split()[1])
        X += val


print(sum(interval_results))
print('done')