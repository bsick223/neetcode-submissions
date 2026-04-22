class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # input: nums

        # must be O(n) time
        # gather the longest consecutive sequence

        # take the initial array into a set

        # to find the start value, look at left neighbor
        # once at start value, look right for next number in set

        # Remove the number from set each time it's added
        # once it's done, append the array to res.

        # output: length of the longest res array: int

        # SOLUTION

        pull = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in pull:
                length = 1
                while num + length in pull:
                    length += 1
                longest = max(length, longest)
                
        return longest

        # return max_length

                


                        


        