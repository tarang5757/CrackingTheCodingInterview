from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # A dictionary to map original nodes to their clones
        node_map = {}

        def dfs(node):
            # If the node is already cloned, return the clone
            if node in node_map:
                return node_map[node]

            # Clone the node
            clone = Node(node.val)
            node_map[node] = clone

            # Clone all the neighbors recursively
            for neighbor in node.neighbors:
                #clone neighbor
                clone_neighbor = dfs(neighbor)
                clone.neighbors.append(clone_neighbor)

            return clone

        return dfs(node)