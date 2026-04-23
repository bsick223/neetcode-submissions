# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # when I find the left child is p or...q?, then check the right side desecendents

        # if not then check left child, and it's descendents, if true than return the left child.

        # or check the right child, it's descendents...

        curr = root

        while curr:
        
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
                
            
        
        

            
            
            