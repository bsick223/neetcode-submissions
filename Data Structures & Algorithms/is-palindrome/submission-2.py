class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.alphaNum(s[l]):
                l +=1
            
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    

    def alphaNum(self, c):

        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))

























        # solution 1:

        # res = ""

        # for c in s:

        #     if c.isalnum():
        #         res += c.lower()

        # return res == res[::-1]



        # solution 2

        # check each character on both sides, 2 pointers

        # we can check to see if there contains symbols, and skip

        # remove spaces

        # I am not sure about checking the symbol



    #     l = 0 
    #     r = len(s) - 1

    #     while l < r:

    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1

    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1

    #         if s[l].lower() != s[r].lower():
    #             return False

    #         l, r = l+1, r-1

    #     return True

    # # check the bounds manually
    # def alphaNum(self, c):

    #     return (ord('A') <= ord(c) <= ord('Z') or
    #         ord('a') <= ord(c) <= ord('z') or
    #         ord('0') <= ord(c) <= ord('9'))


