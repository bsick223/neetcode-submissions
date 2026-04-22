class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # algorithm, take the windowLen - max(freq) <= k

        count = {}

        l = 0

        res = 0
        maxf = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)

            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = r - l + 1

        return res




























        #

































            # len of window - most frequent char
            # if less than or equal to k, calculate result
            # otherwise move left in.

            # left starts at 0, along with R but it's for loop

            # use a counter dictionary for the frequency

            # optimal solution, O(N)
            












            




            # o(26 N)

            # l, res = 0, 0

            # count = {}

            # for r in range(len(s)):
            #     count[s[r]] = 1 + count.get(s[r], 0) 

            #     while (r - l + 1) - max(count.values()) > k:
            #         count[s[l]] -= 1
            #         l += 1

            #     res = max(res, r - l + 1)

            # return res


            




























        # original K

        # while loop continuing on until k == 0 and a new char, or it's the end.

        # we can use k as a marker to stop when k is 0

        # original_k = k # memory address

        # L, longest = 0, 0 

        # for R in range(len(s)):
            
        #     if s[R] != s[L] and k != 0:
        #         while k != 0:
        #             longest = max(R - L + 1, longest)
        #             R += 1
        #             k -= 1
        #     elif s[R] == s[L]:
        #         longest = max(R - L + 1, longest)
        #     else:
        #         L = R
        #         k = original_k
        # return longest