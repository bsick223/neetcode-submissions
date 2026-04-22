class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # nums = [-1,0,2,4,6,8]
        # target = 4

        low = 0
        high = len(nums) - 1
        while (low <= high):

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

        
        return -1


        

        # middle
        # 5
        


        