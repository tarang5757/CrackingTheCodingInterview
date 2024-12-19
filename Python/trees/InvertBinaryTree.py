# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        

        #swap the left children and the right children of the root node
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively repeat the process by passing left children and right children to become root node in another iteration.
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


