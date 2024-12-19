# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #This is the recursive approach
    # if not root:
    #     return 0

    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    #lets solve this using depth



        if not root:
            return 0

        q = deque()
        q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            level += 1
        
        return level







        

        