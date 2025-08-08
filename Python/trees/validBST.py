# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        """
            - Why does this work?
            - a binary search tree left subtree is always lower parent node and right subtree always greater than parent node.

            - We use dfs method to iterate over the tree checking conditions on each node to validate the tree.
            - we first check if node exists and return true if it does.
            - we check if current_node is greater than minimum (-inf initially) and lower than maximum. (infinite initially)

            - we then recursively call its left children and right children updating the bounds.
            - if its left children, we need to check that its lower than parent hence update maximum to be parent node's value
            - if its right children, we need to check that its greater than lower bound hencce update minimum to be parent node's value.
            - we use "and" to check its children. if left is false, we shortcircuit it and no longer need to check right and return False immediately.

            Time Complexity: O(n) - we visot  every node once.
            space complexity: o(n) - the space complexity is o(n) where n represents the number of calls in the stack, it can go up to o(h), where h is the height of the tree in the worst case scenario.
        """

        def dfs(node, minimum, maximum):
            # if node is empty, we return true
            if not node:
                return True

            # check if current node meets the bounds.
            if  not minimum < node.val < maximum:
                return False


            # recurse left and right children
            return (dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum))


        return dfs(root, float("-inf"), float("inf"))

# Test cases
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

object2 =  Solution()
print("got: ", object2.isValidBST(root), "Expected: True")

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

object2 =  Solution()

print("got: ", object2.isValidBST(root), "Expected: False")














