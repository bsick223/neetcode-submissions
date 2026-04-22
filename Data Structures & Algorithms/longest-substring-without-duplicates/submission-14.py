class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # use a set to seen
        # remove it if seen, otherwise add it.
        # longest is the max, perhaps use the length..
        # sliding window, 2 pointer

        longest = 0

        seen = set()

        l = 0

        for r in range(len(s)):

            while s[r] in seen:

                seen.remove(s[l])
                l += 1

            if s[r] not in seen:
                seen.add(s[r])

            longest = max(longest, (r - l + 1))

        return longest



        



























        # input of a string

        # output the length of longest substring
        # 2 pointer

        # find length, if character is the same, subtract r - l
        # then assign l = r

        # keep that as a max length 
         
        

        





























        # sliding window











        # l, r = 0, 1
        # longest_substring = 0

        # if len(s) == 1:
        #     return 1

        # while r < len(s):

        #     current_slice = str(s[l:r])

        #     if s[r] in current_slice:
        #         res = r - l
        #         longest_substring = max(longest_substring, res)
        #         l = r
        #         r += 1
        #     elif r == len(s)-1 and s[r] not in current_slice:
        #         res = r - l
        #         longest_substring = max(longest_substring, res)
        #         break

        #     else:
        #         r += 1

        # return longest_substring

        