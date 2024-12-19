# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True  # boolean flag

        def dfs(root):
            if not root:
                return 0  

            left = dfs(root.left)   # Height of left subtree
            right = dfs(root.right) # Height of right subtree

            # Check if the current subtree is balanced
            if abs(left - right) > 1:
                self.balanced = False

            return 1 + max(left, right)  # Return the height of the current subtree

        dfs(root)  # Initiate the DFS
        return self.balanced  # Return the result
