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


# bfs generate shortest distance for and from every node
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


print('done')
