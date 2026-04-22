class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # define our variables

        # figure out which side the middle is on

        # check if the array is already sorted, return l
        
        # if on the left sorted side, check right.  vice versa

        minimum = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] <= nums[r]:

                minimum = min(minimum, nums[l])
                break
            
            m = (r + l) // 2

            minimum = min(minimum, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return minimum

            


            