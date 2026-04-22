class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]
            

        # [1, 1, 2, 8]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res