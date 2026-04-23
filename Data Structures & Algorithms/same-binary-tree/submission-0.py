# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # assume it's true;

        # traverse recursively using DFS

        # optimization: the moment it's false, exit
        # could be done iteratively in that case using break
        # or I could check each recursion to see if sameTree is true.


        self.isSame = True

        def dfs(currP, currQ):
            
            if not currP and not currQ:
                return
            
            if not currP or not currQ or currP.val != currQ.val:
                self.isSame = False
            else:
                dfs(currP.left, currQ.left)
                dfs(currP.right, currQ.right)
                

        dfs(p, q)

        return self.isSame

