class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # nums = [1,2,4,6]
        # define output array
        output = [0] * len(nums)
        

        for i in range(len(output)):
            # 0-4
            result = 1
            for j in range(len(nums)):
                # 0 - 4
                if j != i:
                    result *= nums[j]

                    # 2, 8, 48

            output[i] = result
            
        return output