class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()  # Sort the numbers first

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # Skip duplicates at i
                continue

            l, r = i + 1, len(nums) - 1  # Two-pointer approach
            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1  # Too large, decrease sum
                elif threesum < 0:
                    l += 1  # Too small, increase sum
                else:
                    res.append([a, nums[l], nums[r]])  # Found triplet
                    l += 1

                    # Skip duplicates at l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

