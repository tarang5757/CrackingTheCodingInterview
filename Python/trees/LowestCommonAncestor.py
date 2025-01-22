class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                print("we returned here 1" )
            
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
                print("we returned here 2")
            
            else:
                return cur
