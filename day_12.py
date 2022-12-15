import queue
import numpy as np
import string

with open('data/day_12ex.txt') as handle:
    lines = handle.readlines()
    lines = [line[:-1] for line in lines]


def convert_heightmap():
    # convert letters to number values
    letter_map = {letter:k+1 for k, letter in enumerate(string.ascii_lowercase)}
    
    height_map = []
    for line in lines:
        val_line = []
        for letter in line:
            if letter == 'S':
                val_line.append(0)
            elif letter == 'E':
                val_line.append(27)
            else:
                val_line.append(letter_map[letter])
        
        height_map.append(val_line)
    
    return np.array(height_map)

def get_adjacent_coords(row, col, heightmap):
    MAXROW = heightmap.shape[0]-1
    MAXCOL = MAXCOL=heightmap.shape[1]-1
    
    adjacent_coords = []
    for coord in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        
        # exceeds bounds
        if any([(coord[0] < 0),(coord[1] < 0), (coord[0] > MAXROW),(coord[1] > MAXCOL)]):
            continue
        
        adjacent_coords.append(coord)

    return adjacent_coords


heightmap = convert_heightmap()

distmap = np.zeros(heightmap.shape, dtype='uint16')
distmap[np.where(distmap == 0)] = 9999

priority_queue = queue.PriorityQueue()
start = (0, 0)
END = (2, 5)
distmap[start] = 0
val = heightmap[start]
visited = []

searching = True

priority_queue.put((val, start))

# main loop
while searching:
    current_dist, current = priority_queue.get()

    if current in visited:
        continue
    
    # ensure already visited lower finds for position persist
    if current_dist != distmap[current]:
        continue
    
    low_tier = heightmap[current] - 1
    high_tier = heightmap[current] + 1
        
    neighbors = get_adjacent_coords(current[0], current[1], heightmap)
    # filter non height-adjadcents neighbors
    neighbors = [neighbor for neighbor in neighbors if low_tier <= heightmap[neighbor] <= high_tier]
    
    # filter out visited
    neighbors = list(filter(lambda x: x not in visited, neighbors))
    
    # visit flow
    for neighbor in neighbors:
        
        if neighbor == END:
            distmap[END] = current_dist + 1
            print('DONE')
            searching = False
        
        current_neighbor_dist = distmap[neighbor]
        alt_neighbor_dist = current_dist + 1  # every neighbor dist is 1
        
        if alt_neighbor_dist < current_neighbor_dist:
            distmap[neighbor] = current_dist + 1
        
        priority_queue.put((distmap[neighbor], neighbor))
            
    visited.append(current)

    # break


print('done')
