import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # We'll keep track of the smallest difference we find so far.
        # Start with a very large number so any real difference will be smaller.
        self.minimum_difference_found = float('inf')

        # This will hold the value of the previously visited node during our
        # in-order traversal. It's crucial for calculating differences.
        self.previous_node_value = None

    def get_min_absolute_difference(self, current_node: Node) -> int:
        # If we've hit an empty spot in the tree, there's nothing to do here.
        if not current_node:
            return self.minimum_difference_found

        # First, go as far left as possible. In a BST, this means visiting
        # smaller values first, which is key for our strategy.
        self.get_min_absolute_difference(current_node.left)

        # Now, we're at the 'middle' node (the current_node) in our in-order sequence.
        # Let's compare its value with the one we just visited (previous_node_value).
        if self.previous_node_value is not None:
            # Calculate the absolute difference between the current node and the previous.
            current_diff = abs(current_node.val - self.previous_node_value)

            # Update our overall minimum difference if this one is smaller.
            self.minimum_difference_found = min(self.minimum_difference_found, current_diff)

        # After processing the current node, its value becomes the 'previous'
        # for the next node we visit (which will be to our right).
        self.previous_node_value = current_node.val

        # Finally, go right to explore larger values.
        self.get_min_absolute_difference(current_node.right)

        # Once all nodes have been visited, return the smallest difference we found.
        return self.minimum_difference_found

# --- Test Cases ---

# Test Case 1: Simple BST
# This tree looks like:
#      5
#     / \
#    3   7
#   / \ / \
#  2  4 6  8
print("--- Test Case 1 ---")
tree1 = Node(5)
tree1.left = Node(3)
tree1.right = Node(7)
tree1.left.left = Node(2)
tree1.left.right = Node(4)
tree1.right.left = Node(6)
tree1.right.right = Node(8)

solution1 = Solution()
result1 = solution1.get_min_absolute_difference(tree1)
print(f"Result: {result1}, Expected: 1 (e.g., between 2 and 3, or 3 and 4, or 5 and 6, etc.)")

# Test Case 2: Another common BST pattern
# This tree looks like:
#   1
#    \
#     3
#    /
#   2
print("\n--- Test Case 2 ---")
tree2 = Node(1)
tree2.right = Node(3)
tree2.right.left = Node(2)

solution2 = Solution()
result2 = solution2.get_min_absolute_difference(tree2)
print(f"Result: {result2}, Expected: 1 (e.g., between 1 and 2, or 2 and 3)")

# Test Case 3: Larger values and potentially larger differences
# This tree looks like:
#       10
#      /  \
#     5    15
#    / \     \
#   3   7     20
print("\n--- Test Case 3 ---")
tree3 = Node(10)
tree3.left = Node(5)
tree3.right = Node(15)
tree3.left.left = Node(3)
tree3.left.right = Node(7)
tree3.right.right = Node(20)

solution3 = Solution()
result3 = solution3.get_min_absolute_difference(tree3)
print(f"Result: {result3}, Expected: 2 (between 3 and 5, or 5 and 7)")