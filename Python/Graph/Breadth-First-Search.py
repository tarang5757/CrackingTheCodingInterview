from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

#adjacency list representation of graph.
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# visited = []  # List to keep track of visited nodes.
# queue = deque([])    # Initialize a queue for BFS.

# def bfs(visited, graph, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         node = queue.popleft()  # Dequeue a vertex from the queue.
#         print(node, end=" ")  # Print the current node.

#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)





# Another type of implementation of BFS

def bfs(node: GraphNode):
    visited = set()
    queue = deque([node])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if node not in visited:
            visited.add(node)
            # process Node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Test the BFS algorithm starting from node '5'
bfs('5')