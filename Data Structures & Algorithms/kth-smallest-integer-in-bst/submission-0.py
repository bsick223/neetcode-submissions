# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # brute force, put values into an array and then grab the kth item

        self.res = []
        #using in order dfs traversal

        def dfs(curr):

            if not curr:
                return 

            dfs(curr.left)
            self.res.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return self.res[k -1]
            
