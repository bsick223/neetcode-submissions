class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (r + l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:

                if nums[l] <= target <= nums[m]:
                    r = m - 1

                else:
                    l = m + 1

            else:

                if nums[m] <= target <= nums[r]:
                    l = m + 1

                else:
                    r = m - 1

        return -1

            



























        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid

        #     # [5,1,2,3,4]
        #     # target = 1

        #     # left sorted portion
        #     if nums[mid] >= nums[l]:
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        #     # right sorted portion
        #     else:
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return -1

