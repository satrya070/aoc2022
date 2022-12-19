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
distance_map  = {}

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

    distance_map[source_node] = node_distances


# ----- calculate max flowrate -----
minute = 0
flowrate = 0
total_pressure = 0
non_empty_nodes = [node for node, data in tunnel_data.items() if data['flowrate'] > 0]

current_node = 'AA'
visited = [current_node]

while not all([req in visited for req in non_empty_nodes]) or len(visited) == 0:
    max_dist = max(distance_map[current_node].values()) + 2  # step + open + 1 flow

    node_values = []
    for node, dist in distance_map[current_node].items():
        if node == current_node or node in visited:
            continue

        flowsteps = max_dist - (dist + 1)
        node_value = flowsteps * tunnel_data[node]['flowrate'] 

        node_values.append((node_value, node))

    next_node = max(node_values)[1]
    minutes_added = distance_map[current_node][next_node] + 1

    minute += minutes_added
    total_pressure += (minutes_added * flowrate)
    flowrate += tunnel_data[next_node]['flowrate']

    print(minute, flowrate, current_node, next_node, total_pressure)

    visited.append(current_node)
    current_node = next_node

print((30 - minute) * flowrate, total_pressure)




print('done')
