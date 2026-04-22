class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use a set to check for duplicats

        # use a left and right pointer..

        # check to see empty string
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 0
        seen = set()
        res = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            res = max(res, r - l + 1)

        return res


