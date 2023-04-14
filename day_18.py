example = [
    [2,2,2],
    [1,2,2],
    [3,2,2],
    [2,1,2],
    [2,3,2],
    [2,2,1],
    [2,2,3],
    [2,2,4],
    [2,2,6],
    [1,2,5],
    [3,2,5],
    [2,1,5],
    [2,3,5]
]

for block in example:
    x, y, z = block 

def is_adjacent(block_a, block_b):
    # check horizontal adjacent
    x1, y1, z1 = block_a
    x2, y2, z2 = block_b

    if (x2, y2) in [(x1-1, y1), (x1+1, y1), (x1, y1-1), (x1, y1+1)]:
        print('yes')
        return True

    # check vertical adjacent
    if (x2, y2, z2) in [(x1, y1, z1+1), (x1, y1, z1-1)]:
        return True
    
    return False
    
x = is_adjacent((0,0,1), (0,0,0))
print(x)
