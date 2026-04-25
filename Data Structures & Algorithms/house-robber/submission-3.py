class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dfs(i, cache):

        #     if i >= len(nums):
        #         return 0
        #     if i not in cache:
        #         cache[i] = max(nums[i] + dfs(i + 2, cache), dfs(i + 1, cache))

        #     return cache[i]
            

        # return dfs(0, {})

        rob1, rob2 = 0, 0

        for n in nums:

            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

        