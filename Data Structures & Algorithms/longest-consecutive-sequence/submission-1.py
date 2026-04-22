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


        pull = set(nums)
        res = []
        for num in nums:
            if num - 1 in pull:
                continue
            else:
                temp_res = []
                while num in pull:
                    temp_res.append(num)
                    num += 1
                res.append(temp_res)
                
        max_length = 0
        for array in res:

            length = len(array)

            max_length = max(max_length, length)

        return max_length

                


                        


        