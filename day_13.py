import itertools

with open('data/day_13ex.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]
    lines = [line for line in lines if line != '']

def pairer(lines):
    pairs = []
    for pnum in range(0, len(lines), 2):
        com_a = eval(lines[pnum])
        com_b = eval(lines[pnum+1])
        pairs.append(tuple((com_a, com_b)))
    
    return pairs

def vals_to_list(val_a, val_b):
    # if one is list convert both to list first
    val_a = list([val_a]) if type(val_a) == int else val_a
    val_b = list([val_b]) if type(val_b) == int else val_b

    return val_a, val_b

pairs = pairer(lines)




def comparator(list_a, list_b):

    for val_a, val_b in zip(list_a, list_b):

        # convert to both to list and recur into comparator
        if type(val_a) != type(val_b):
            val_a, val_b = vals_to_list(val_a, val_b)
            nested_comparison = comparator(val_a, val_b)

            if nested_comparison is False:
                return False
            elif nested_comparison: 
                return True
            else:
                continue
        
        # when both are list recur into comparator
        if type(val_a) == list and type(val_b) == list:
            nested_comparison = comparator(val_a, val_b)
            
            if nested_comparison is False:
                return False
            elif nested_comparison: 
                return True
            else:
                continue
        
        # flow if both vals are numbers
        if val_a < val_b:
            return True
        elif val_a > val_b:
            return False
        else:  # even
            continue

# test cases
list_a, list_b = pairs[0]
ex1 = comparator(list_a, list_b)

list_a, list_b = pairs[1]
ex2 = comparator(list_a, list_b)
print(ex2)

list_a, list_b = pairs[2]
ex3 = comparator(list_a, list_b)
print(ex3)

list_a, list_b = pairs[3]
ex4 = comparator(list_a, list_b)
print(ex4)

print(lines)