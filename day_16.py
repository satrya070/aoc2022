from collections import defaultdict

with open('data/day_16ex.txt') as handle:
    lines = handle.readlines()
    lines = [line[:-1] for line in lines]

tunnel_data = defaultdict(dict)

for line in lines:
    parts = line.split(' ')
    valve_id = parts[1]
    flowrate = int(''.join([char for char in parts[4] if char.isdigit()]))
    connections = parts[9:]
    connections = [connection.replace(',', '') for connection in connections]
    
    tunnel_data[valve_id]['flowrate'] = flowrate
    tunnel_data[valve_id]['connections'] = connections


# ---- BFS generate shortest distance for and from every node ----
distance_map_unfiltered  = {}

for source_node in tunnel_data.keys():

    node_distances = {}
    distance = 0  # init to self 
    children = [source_node]

    while children:
        next_children = []

        for child in children:
            node_distances[child] = distance
            next_children = next_children + tunnel_data[child]['connections']
        
        children = list(set([child for child in next_children if child not in node_distances]))
        distance += 1

    distance_map_unfiltered[source_node] = node_distances


# map of all relevant valve with their rate
valve_flowrates = {
    valve: data['flowrate'] for valve, data in tunnel_data.items()
    if data['flowrate'] > 0 or
    valve == 'AA'
}

# distance map with worthess valves removed
# valves_zero = ['II', 'GG', 'FF']
distance_map = {}

for key, valve_distances_unfiltered in distance_map_unfiltered.items():
    if key in valve_flowrates:
        valve_distances = {}
        for valve in valve_distances_unfiltered:
            if valve in valve_flowrates:
                valve_distances[valve] = valve_distances_unfiltered[valve]
        
        distance_map[key] = valve_distances


# ------ small example -------
# valve_flowrates = {
#     'a': 0,
#     'b': 20,
#     'c': 25
# }

# del distance_map
# distance_map = {
#     'a': {'b': 1, 'c': 2},
#     'b': {'a': 1, 'c': 1},
#     'c': {'a': 2, 'b': 2}
# }

# ---------------------------

def explore_max_branch(current, flowrate, opened, remaining):
    
    # get neighbors and filter out opened and neighbors outside time limit
    neighbors = {
        neighbor: dist for neighbor, dist in distance_map[current].items()
        if (neighbor not in opened) and
        neighbor != current and
        ((remaining - dist - 1) > 0)
    }

    if not neighbors:
        return flowrate * remaining

    # calculate flowrates
    branches_accumulated = []

    for neighbor, distance in neighbors.items():
        pressure = flowrate * (distance + 1)
        # print(pressure, neighbor, distance, flowrate, remaining)

        branches_accumulated.append(pressure + (explore_max_branch(
            neighbor,
            flowrate + valve_flowrates[neighbor],
            opened + [current],
            remaining - (distance + 1)
        )))

    return max(branches_accumulated)


maxval = explore_max_branch('AA', 0, [], 30)
# explore_max_branch('b', 20, ['a'], 3)



print('done')
