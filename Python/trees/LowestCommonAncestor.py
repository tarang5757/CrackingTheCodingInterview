class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        # Start at the curr root node
        cur = root

        while cur:
            # Check to see our nodes fall on the right subtree.
            if p.val > cur.val and q.val > cur.val:
                # Search in the right subtree
                cur = cur.right
                print("we returned here 1" )
            
            # Check to see if our nodes fall on the left subtree
            elif p.val < cur.val and q.val < cur.val:
                
                #search in the left subtree
                cur = cur.left
                print("we returned here 2")
            
            else:
                # if a split is seen between p and q then we found a common ancestor
                return cur
