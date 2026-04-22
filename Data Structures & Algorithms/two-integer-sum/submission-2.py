class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        j = {}

        for i in range(len(nums)):

            if target - nums[i] not in j:
                j[nums[i]] = i

            else:
                return [j[target-nums[i]], i]








































        # use hash table to check for difference

        # difference lookup inside dictionary 

        # target minus i == j

        # return [i, j]































        # difference = {}

        # def check_if_difference(nums):


        #     for i in nums:
        #         return True if target - nums[i] in difference else 

        
        # flag = check_if_difference()

        # if flag:
        #     return [i, j]
        