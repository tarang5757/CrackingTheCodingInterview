graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List to keep track of visited nodes.
queue = []    # Initialize a queue for BFS.

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)  # Dequeue a vertex from the queue.
        print(m, end=" ")  # Print the current node.

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Test the BFS algorithm starting from node '5'
bfs(visited, graph, '5')