class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        resDuplicate = 0
        resMissing = 0
        mySet = set()
        for g in grid:
            for num in g:
                if num in mySet:
                    resDuplicate = num
                else:
                    mySet.add(num)

            
        for i in range(1, len(grid) * len(grid) + 1):
            if i not in mySet:
                resMissing = i

        return [resDuplicate, resMissing]