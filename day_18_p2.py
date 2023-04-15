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


def is_adjacent(block_a, block_b, block_dict):
    x1, y1, z1 = block_a
    x2, y2, z2 = block_b

    # check horizontal adjacent ----------------------------------
    horizontal_adjacents = [(x1-1, y1, z1), (x1, y1+1, z1), (x1+1, y1, z1), (x1, y1-1, z1)]
    horizontal_adjacents_ids = [0, 1, 2, 3]
    if (x2, y2, z2) in horizontal_adjacents:
        surface_id = horizontal_adjacents_ids[horizontal_adjacents.index((x2, y2, z2))]
        block_dict[block_a][surface_id] = False
        
        return block_dict

    # check vertical adjacent ----------------------------------
    vertical_adjacents = [(x1, y1, z1+1), (x1, y1, z1-1)]
    vertical_adjacents_ids = [4, 5]

    if (x2, y2, z2) in vertical_adjacents:
        surface_id = vertical_adjacents_ids[vertical_adjacents.index((x2, y2, z2))]
        block_dict[block_a][surface_id] = False
        
        return block_dict
    
    return block_dict

blocks_todo = example

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

        block_surfaces = is_adjacent(block, sub_block, block_surfaces)

# count all uncovered surfaces
uncovered_surfaces = 0

for block, surfaces in block_surfaces.items():
    uncovered_surfaces += surfaces.count(True)

# part 2 ---------------------------------------------------------

all_adjacent_blocks = {}

# get all possible adjacent blocks position
for block in blocks_todo:
    x, y, z = block
    adjacent_blocks = [
        (x-1, y, z), (x, y+1, z), (x+1, y, z), (x, y-1, z),
        (x, y, z+1), (x, y, z-1)
    ]

    for adjacent_block in adjacent_blocks:
        if adjacent_block not in all_adjacent_blocks and adjacent_block not in blocks_todo:
            all_adjacent_blocks[adjacent_block] = [True, True, True, True, True, True]

    # check if adjacent block is in blocks_todo
    # for adjacent_block in adjacent_blocks:
    #     if adjacent_block in blocks_todo:
    #         is_adjacent(block, adjacent_block)

# check all adjacent blocks with actual blocks
for main, block in enumerate(all_adjacent_blocks):
    for sub, sub_block in enumerate(blocks_todo):
        adjacent = is_adjacent(block, sub_block)

# print(uncovered_surfaces)
# print('done!')

# x = is_adjacent((1, 1, 1), (2, 1, 1))

