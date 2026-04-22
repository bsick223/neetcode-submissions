class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        countT, window = {}, {}

        l = 0

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res = [-1, -1]
        resLen = float("infinity")

        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

                
            while have == need:
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = [l, r]

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        print(l, r)

        return s[l:r + 1] if resLen != float("infinity") else ""
                    



            




        





























        
            

        """ 
        
        catch the edge case of empty.
        have a count for t, and a count for your window
        use res length for seeing you minimum window, and res for upacking the string slice
        establish your have and need, with 

        1. get the count of T
        2. gather the count of window, dynamically
        3. update have, if the char is in t and window
        4. while have == need
            a. set the new res if have == need, and less than resLength.
            b. pop from the left window
            c. if the condition is not met, subtract from have (if c not in t, and the window c < t[c], pseudo)
            d. move left pointer

        5. unpack res for l and r
        6. return slice, if res == inf then ""



        """
        




































        # if t == "":
        #     return ""

        # countT, window = {}, {}

        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)

        # have, need = 0, len(countT) # this counts the unique characters in t

        # res, resLen = [-1, -1], float("infinity")
        # l = 0

        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         # update our result
        #         if (r - l + 1) < resLen:
        #             res = [l, r]
        #             resLen = (r - l + 1)
        #         # pop from the left of our window
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1

        #         l += 1

        # l, r = res
        # return s[l:r+1] if resLen != float("infinity") else ""