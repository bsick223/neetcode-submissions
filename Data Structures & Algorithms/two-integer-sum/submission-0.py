class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Goal is to search through target - num and find the other num that = target

        # Goal: mapping the value to the index

        # initialize an empty hashmap

        hashmap = {}

        # visiting the element,

        for index, num in enumerate(nums):
            difference = target - num

        # if not in hashmap
        # add it
        # then move to the next index
            if difference in hashmap:
                return [hashmap[difference], index]
            
            hashmap[num] = index
                

        

        # if it exists 
        # return it's indices.



        
        