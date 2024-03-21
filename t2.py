import math
import networkx as nx
import matplotlib.pyplot as plt

coordinates = {
    "JKIA": (-1.331242504, 36.9252553),
    "WILSON": (-1.321944444, 36.81472222),
    "UAP TOWER": (-1.3006, 36.8131),
    "KICC": (-1.28579, 36.82003),
    "TIMES TOWER": (-1.2903, 36.8239),
    "NAIROBI WEST HOSPITAL": (-1.32087, 36.820042),
    "UON TOWER": (-1.28076, 36.81719),
    "Britam Tower": (-1.3, 36.813056),
    "Nairobi GTC Office Tower": (-1.2710817, 36.80842),
    "UAP Old Mutual Tower": (-1.3006, 36.8131),
    "Nairobi GTC Hotel Tower": (-1.2710817, 36.80842),
    "Times Tower": (-1.2903, 36.8239),
    "Prism Tower": (-1.291708, 36.810855),
    "Le’mac Towers": (-1.261909, 36.789265),
    "Parliament Tower": (-1.290591, 36.820786),
    "Telposta House": (-1.286086, 36.819735),
    "kcb plaza": (-1.282541, 36.832268),
    "Kenyatta International Convention Centre": (-1.28579, 36.82003),
    "Social Security House": (-1.289755, 36.811945),
    "Kangemi Health Center": (-1.258, 36.751),
    "Kariobangi North Health Center": (-1.251, 36.886),
    "Dandora Phase 4": (-1.252, 36.904),
    "KMD Dagoretti Corner Nairobi": (-1.302, 36.737),
    "Kenyatta University City Campus": (-1.257, 36.813),
    "Kara Office": (-1.293, 36.811),
    "Nairobi National Park": (-1.406, 36.852),
    "UNEP HQ, Main Entrance": (-1.298, 36.794),
    "NYERERE ROAD": (-1.288, 36.822),
    "EIK Office": (-1.264, 36.804)
}

def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371000  # Earth radius in meters
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Create a graph
G = nx.Graph()

# Add nodes
for node, coord in coordinates.items():
    G.add_node(node, pos=coord)

# Add edges with weight as distance
for node1, coord1 in coordinates.items():
    for node2, coord2 in coordinates.items():
        if node1 != node2:
            distance = haversine(coord1, coord2)
            G.add_edge(node1, node2, weight=distance)

# Find the shortest path between all pairs of locations
shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Plotting the graph
plt.figure(figsize=(15, 10))
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue')
plt.title('Shortest Path between Locations')
plt.show()

# Display the shortest paths
for node1 in coordinates:
    for node2 in coordinates:
        if node1 != node2:
            path_length = shortest_paths[node1][node2]
            print(f"Shortest path from {node1} to {node2}: {path_length:.2f} meters")
