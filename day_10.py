import numpy as np
import pickle as pkl

with open('data/day_10ex.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

with open('data/day_10.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

X = 1
intervals = [20, 60, 100, 140, 180, 220]
cycles = 0
crt = 0

image = np.zeros((1, 240), dtype='uint8')

for line in lines:

    if line == 'noop':
        for cycle in range(1):
            cycles += 1

            if crt % 40 in [X-1, X, X+1]:
                image[0][crt] = 1
                print(X, cycles)

            
            crt += 1

            # if cycles in intervals:
            #     interval_val = intervals[intervals.index(cycles)] * X
            #     interval_results.append(interval_val) 

    else:
        for cycle in range(2):
            cycles += 1

            if crt % 40 in [X-1, X, X+1]:
                image[0][crt] = 1
                print(X, cycles)

            
            crt += 1

            # if cycles in intervals:
            #     interval_val = intervals[intervals.index(cycles)] * X
            #     interval_results.append(interval_val) 
        
        val = int(line.split()[1])
        X += val
    
with open('./message.pkl', 'wb') as handle:
    pkl.dump(image, handle)

print('done')