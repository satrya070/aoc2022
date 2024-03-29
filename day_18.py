example0 = [
    (1, 1, 1), 
    (2, 1, 1)
]

example = [
    (2,2,2),
    (1,2,2),
    (3,2,2),
    (2,1,2),
    (2,3,2),
    (2,2,1),
    (2,2,3),
    (2,2,4),
    (2,2,6),
    (1,2,5),
    (3,2,5),
    (2,1,5),
    (2,3,5)
]

with open('data/day_18.txt') as f:
    lines = f.readlines()
    lines = [eval(line[:-1]) for line in lines]


def is_adjacent(block_a, block_b):
    x1, y1, z1 = block_a
    x2, y2, z2 = block_b

    # check horizontal adjacent ----------------------------------
    horizontal_adjacents = [(x1-1, y1, z1), (x1, y1+1, z1), (x1+1, y1, z1), (x1, y1-1, z1)]
    horizontal_adjacents_ids = [0, 1, 2, 3]
    if (x2, y2, z2) in horizontal_adjacents:
        surface_id = horizontal_adjacents_ids[horizontal_adjacents.index((x2, y2, z2))]
        block_surfaces[block_a][surface_id] = False
        return

    # check vertical adjacent ----------------------------------
    vertical_adjacents = [(x1, y1, z1+1), (x1, y1, z1-1)]
    vertical_adjacents_ids = [4, 5]

    if (x2, y2, z2) in vertical_adjacents:
        surface_id = vertical_adjacents_ids[vertical_adjacents.index((x2, y2, z2))]
        block_surfaces[block_a][surface_id] = False
        return
    
    return False

blocks_todo = lines

# generate dict with all surface for each block
block_surfaces = {}
for block in blocks_todo:
    # left: 0, up: 1, right: 2, down: 3, top: 4, bottom: 5
    block_surfaces[block] = [
        True, True, True, True, True, True
    ]

# go through all blocks and check if they are adjacent and update surfaces dict
for main, block in enumerate(blocks_todo):
    for sub, sub_block in enumerate(blocks_todo):
        if main == sub:
            continue

        adjacent = is_adjacent(block, sub_block)

# count all uncovered surfaces
uncovered_surfaces = 0
for block, surfaces in block_surfaces.items():
    uncovered_surfaces += surfaces.count(True)

print(uncovered_surfaces)
print('done!')

# x = is_adjacent((1, 1, 1), (2, 1, 1))

