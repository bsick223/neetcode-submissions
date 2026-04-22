class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # sort the array...

        # if the next term is the same, skip

        # use a left and right pointer for after the first term...
        # if sum is > 0, then decrease the sum and move the right pointer. vice versa

        # don't reuse the same l and r nums, move it

        # O(nlogn) + O(n^2)

        # O(1)

        '''
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        '''

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum_nums = nums[r] + nums[l] + a
                if sum_nums > 0:
                    r -= 1
                elif sum_nums < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
                    




