class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # use a hashmap
        # majority
        # if majority - K > 0, calculate
        # else, lower the left char in the dict..

        chars = {}

        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            c = s[r]
            # get max freq 
            chars[c] = chars.get(c, 0) + 1

            if (chars[c] > maxf):
                maxf = chars[c]

            if ((r - l + 1) - maxf <= k):
                res = (r - l + 1)
            else:
                chars[s[l]] -= 1
                l += 1
        return res
            
