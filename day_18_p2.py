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


def is_adjacent(block_a, block_b, block_dict, checkid):
    x1, y1, z1 = block_a
    x2, y2, z2 = block_b

    # check horizontal adjacent ----------------------------------
    horizontal_adjacents = [(x1-1, y1, z1), (x1, y1+1, z1), (x1+1, y1, z1), (x1, y1-1, z1)]
    horizontal_adjacents_ids = [0, 1, 2, 3]
    if (x2, y2, z2) in horizontal_adjacents:
        surface_id = horizontal_adjacents_ids[horizontal_adjacents.index((x2, y2, z2))]
        block_dict[block_a][surface_id] = checkid
        
        return

    # check vertical adjacent ----------------------------------
    vertical_adjacents = [(x1, y1, z1+1), (x1, y1, z1-1)]
    vertical_adjacents_ids = [4, 5]

    if (x2, y2, z2) in vertical_adjacents:
        surface_id = vertical_adjacents_ids[vertical_adjacents.index((x2, y2, z2))]
        block_dict[block_a][surface_id] = checkid
        
        return
    
    return

stone_blocks = example # lines

# generate dict with all surface for each block
# block_surfaces = {}
# for block in blocks_todo:
#     # left: 0, up: 1, right: 2, down: 3, top: 4, bottom: 5
#     block_surfaces[block] = [
#         True, True, True, True, True, True
#     ]

# go through all blocks and check if they are adjacent and update surfaces dict
# for main, block in enumerate(blocks_todo):
#     for sub, sub_block in enumerate(blocks_todo):
#         if main == sub:
#             continue

#         block_surfaces = is_adjacent(block, sub_block, block_surfaces)

# count all uncovered surfaces
# uncovered_surfaces = 0

# for block, surfaces in block_surfaces.items():
#     uncovered_surfaces += surfaces.count(True)

# part 2 ---------------------------------------------------------

air_blocks = {}

# get all possible adjacent blocks position
for stone_block in stone_blocks:
    x, y, z = stone_block
    adjacent_blocks = [
        (x-1, y, z), (x, y+1, z), (x+1, y, z), (x, y-1, z),
        (x, y, z+1), (x, y, z-1)
    ]

    # collect all air blocks := if an adjacent block and not a real block
    for air_block in adjacent_blocks:
        
        if air_block not in air_blocks and air_block not in stone_blocks:
            air_blocks[air_block] = [0, 0, 0, 0, 0, 0]

# check all air blocks with stone blocks: stone_id = 1
for main, air_block in enumerate(air_blocks):
    for sub, stone_block in enumerate(stone_blocks):
        is_adjacent(air_block, stone_block, air_blocks, 1)

print("checkout stone surfaces")

# check which airblocks are adjacent to each other --------
for main, air_block in enumerate(air_blocks):
    for sub, other_air_block in enumerate(air_blocks):
        is_adjacent(air_block, other_air_block, air_blocks, 2)

print('checked out air surfaces')

# for adjacent_airblock, check which one theyre connected to, and isolated ones
# group id these blocks
# requirement: all blocks within a group must have air or block surfaces
# otherwise air is flowing out. I should


# 3326 too high 3320
