class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]

        res = [0] * len(temperatures)
        # loop through the array using i
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
                j += 1

        return res

            


        # while loop to count j = i, and get a resulting_day = j - i

        # set to the res array.

