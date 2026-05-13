print("Hello, World! This is run on Googe cloud Engine")
from collections import deque

def bfs(graph, start_node):
    # Keep track of visited nodes to avoid infinite loops
    visited = set()
    # Initialize a queue with the starting node
    queue = deque([start_node])
    
    # Mark the start node as visited
    visited.add(start_node)
    
    while queue:
        # Remove the first node added to the queue (FIFO)
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Look at all neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# --- Example Usage ---
# A dictionary representing an adjacency list for a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal starting from node A:")
bfs(graph, 'A')
