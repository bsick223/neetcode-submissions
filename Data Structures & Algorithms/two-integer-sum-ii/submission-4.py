class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # must use O(1) additional space

        # using the right and left pointers...

        # if sum < target -> move right.   vice versa

        # reutrn 1 indexed


        l, r = 0, len(numbers) - 1

        # [-5,-3,0,2,4,6,8]
        #      1         6
        # sumVal = 3

        while l<r:

            sumVal = numbers[l] + numbers[r]
            print(sumVal)
            if sumVal > target:
                r -= 1

            elif sumVal < target:
                l += 1

            else:
                return [l + 1, r + 1]
        