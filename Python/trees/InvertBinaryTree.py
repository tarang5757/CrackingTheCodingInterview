# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def invertTreeIteratively(self, root):
        if not root:
            return None
        stack = [root]

        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return root


    def printTree(self, root):
        if not root:
            return
        self.printTree(root.left)
        print(root.val, end=" ")
        self.printTree(root.right)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(8)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.right = TreeNode(4)


invertTree = Solution()
inverted_root = invertTree.invertTree(root)
print("Inverted tree in-order traversal: ", end="")
invertTree.printTree(inverted_root)




