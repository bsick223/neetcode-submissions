import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        ready_string = ''

        for c in s:
            if c not in string.punctuation and not c.isspace():
                ready_string += c.lower()

        
        return (ready_string == ready_string[::-1])
        