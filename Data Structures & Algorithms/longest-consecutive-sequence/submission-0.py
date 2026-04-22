class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_list = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in new_list:
                length = 0
                while (n + length) in new_list:
                    length += 1
                longest = max(length, longest)

        return longest

        
        