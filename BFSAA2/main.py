import random
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def generate_connected_graph(num_nodes):
    graph = {node: [] for node in range(num_nodes)} # empty graph dict with all nodes as keys and empty lists as values
    visited = set()
    edges = []

    start_node = random.randint(0, num_nodes - 1)
    visited.add(start_node)
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        unvisited_neighbors = [n for n in range(num_nodes) if n != node and n not in visited]
        if unvisited_neighbors:
            neighbor = random.choice(unvisited_neighbors)
            visited.add(neighbor)
            edges.append((node, neighbor))
            graph[node].append(neighbor)
            graph[neighbor].append(node)
            queue.append(neighbor)

    return edges


def bfs(graph, start_node, exit_node, speed):
    visited = set()
    queue = deque([(start_node, 0)])

    while queue:
        node, distance = queue.popleft() # retrieve the next node and the corresponding distance

        if node == exit_node:
            return distance / speed

        visited.add(node)

        for neighbor in graph[node]: # graph[node] -> neighbors of the current node
            if neighbor not in visited:
                visited.add(neighbor) # Mark the neighbor as visited
                queue.append((neighbor, distance + 1))

    return float('inf')


def visualize_graph(graph):
    G = nx.Graph()
    G.add_edges_from(graph)

    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()



# Example usage
num_nodes = 10
graph = generate_connected_graph(num_nodes)

start_nodes = [0, 3, 7]  # Initial positions of the wizards
exit_node = num_nodes - 1

wizard_speeds = [2, 3, 4]  # Speeds of the wizards in corridors per minute

times = []
for i, wizard in enumerate(start_nodes):
    speed = wizard_speeds[i]
    time = bfs(graph, wizard, exit_node, speed)
    times.append(time)

min_time = min(times)
winning_wizard = times.index(min_time)

print(f"The wizard {winning_wizard + 1} will reach the exit first in {min_time} minutes.")
visualize_graph(graph)
