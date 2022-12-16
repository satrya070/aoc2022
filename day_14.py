import numpy as np
import matplotlib.pyplot as plt

map_ = []
for row in range(200):
    map_.append([0 for i in range(100)])

with open('data/day_14ex.txt') as handle:
    lines = handle.readlines()
    lines = [line[:-1] for line in lines]


def generate_line(start, end):
    """ generate line of number between 2 points """

    # ascend flow
    if start < end: 
        line = list(range(start, end + 1))
    # descend
    else:
        line = list(range(start, end - 1, -1))

    return line


wall_coords = []

# generate walls
for line in lines:
    str_vertexes = (line.split(' -> '))
    vertexes = [vertex.split(',') for vertex in str_vertexes]
    vertexes = [(int(vertex[0]), int(vertex[1])) for vertex in vertexes]
    
    # processes every edge in vertexes
    for i in range(len(vertexes) - 1):
        vertex_a = vertexes[i]
        vertex_b = vertexes[i+1]

        vert_a_col, vert_a_row = vertex_a
        vert_b_col, vert_b_row = vertex_b

        # generate row coords
        if vert_a_col == vert_b_col:
            row_coords = generate_line(vert_a_row, vert_b_row)
            edge_coords = [(vert_a_col, row) for row in row_coords]
            wall_coords = wall_coords + edge_coords

        # generate col coords
        else:
            col_coords = generate_line(vert_a_col, vert_b_col)
            edge_coords = [(col, vert_a_row) for col in col_coords]
            wall_coords = wall_coords + edge_coords

wall_coords = list(set(wall_coords))
print(sorted(wall_coords))
    
        
# draw
canvas = np.zeros((200, 100), dtype='uint8')
for coord in wall_coords:
    c = coord[0] - 450
    r = coord[1]
    canvas[r, c] = 1

plt.imsave('./day14.png', canvas)

print('done')    
