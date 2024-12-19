# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time & Space Complexity
        Time complexity: O(n)
        Space complexity: O(h) 

        - Best case (balanced tree): O(logn)
        - worst case (degenerate tree): O(n)
        """
        self.res = 0

        #returns height
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Calculate and store the Diameter in res 
            self.res = max(self.res, left + right)

            #returns the max height of the subtree from curr(add +1)
            return 1 + max(left, right)

        dfs(root)

        return self.res
