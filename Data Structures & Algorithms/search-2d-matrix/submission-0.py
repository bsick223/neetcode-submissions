class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # loop through each outer list

        # if start < target < end

        # then binary search this list..

        for outer in matrix:
            if outer[0] <= target <= outer[-1]:
                l, r = 0, len(outer)
                while l <= r:
                    
                    m = (l + r) // 2

                    if target > outer[m]:
                        l = m + 1

                    elif target < outer[m]:
                        r = m - 1

                    else:
                        return True

        return False
            