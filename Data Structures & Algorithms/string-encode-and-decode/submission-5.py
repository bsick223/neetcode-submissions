class Solution:

    def encode(self, strs: List[str]) -> str:

        """

        4#neet4#code

        """

        res = ""

        for word in strs:

            length = len(word)
            res += str(length) + "#" + word

        print(res)

        return res



     


    def decode(self, s: str) -> List[str]:

        """

        4#neet4#code

        12 len

        """
        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j +1
            j = i + length

            res.append(s[i:j])

            i = j

        return res































































        # res = []

        # i = 0

        # # 4#neet3#wow
      
        # while i < len(s):
        #     j = i

        #     while s[j] != "#":

        #         j += 1

        #         # find the slice

        #     length = int(s[i:j])

        #     i = j + 1

        #     j = i + length

        #     res.append(s[i: j])

        #     i = j
            



        # return res

