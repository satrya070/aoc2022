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

source_node = 'AA'
paths = [[source_node]]

updated_paths = []

for path in paths:
    tail_nodes = [path[-1] for path in paths]
    
    for tail_node in tail_nodes:
        for connection in tunnel_data[tail_node]['connections']:
            updated_path = path.copy()
            updated_path.append(connection)
            
            updated_paths.append(updated_path)

print(updated_paths)