class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # i = the bar
        # heights[i] is the height

        # what can produce the greatest area.
         
        # area = x * y

        # find x by subtracting 2 pointers to find the length
        # x = r - l

        # y is the lesser height.

        # we need to find the maximum.

        # 2 pointer with a max variable?

        # move the pointer with the smaller value

        # even?

        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            x = r - l
            if heights[l] > heights[r] and l < r:
                y = heights[r]
                max_area = max(max_area, x * y)
                r -= 1

            elif heights[l] < heights[r] and l < r:
                y = heights[l]
                max_area = max(max_area, x * y)
                l += 1
            else:
                y = heights[l] # default
                max_area = max(max_area, x * y)
                r -= 1

        return max_area            


        