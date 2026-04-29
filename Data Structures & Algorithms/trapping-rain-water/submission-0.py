class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxL = [0] * len(height)
        maxR = [0] * len(height)


        for h in range(1, len(height)):
            maxL[h] = max(maxL[h - 1], height[h - 1])

        for h in range(len(height) - 2, -1, -1):
            maxR[h] = max(maxR[h + 1], height[h + 1])
        
        res = 0

        for h in range(1, len(height) - 1):
            res += max(0, min(maxL[h], maxR[h]) - height[h])

        return res

            

