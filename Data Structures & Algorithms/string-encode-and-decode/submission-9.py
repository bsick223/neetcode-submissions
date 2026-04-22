class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for word in strs:
            length = str(len(word))
            res += length + "#" + word

        return res

        """
        4#neet4#code
        """
                


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):

            j = i

            while s[j] != "#":

                j += 1

            length = int(s[i:j])
            i = j + 1

            j = i + length 

            res.append(s[i:j])

            i = j

        return res
        

            


