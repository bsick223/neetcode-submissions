# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # brute force, put values into an array and then grab the kth item

        self.cnt = 0
        self.val = None
        #using in order dfs traversal

        def dfs(curr):

            if not curr:
                return 

            dfs(curr.left)
            self.cnt += 1
            if self.cnt == k:
                self.val = curr.val
            dfs(curr.right)

        dfs(root)
        return self.val
            
