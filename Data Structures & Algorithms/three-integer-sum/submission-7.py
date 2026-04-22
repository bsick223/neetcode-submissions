class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i, a in enumerate(nums):

            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                

        return res
        
                

                






     






















        # remember when comparing the sum with the current add,
        # we need to be move the left pointer up if it's below target
        # vice versa: sum > 0 and sum < 0

        # sort the list so we can work with duplicates

        # solution:
        
        
            