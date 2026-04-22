class Solution:

    def encode(self, strs: List[str]) -> str:

        # use length as a part of delimeter
        # length#

        encode_string = ""

        for word in strs:
            length = str(len(word))
            encode_string += length + "#" + word

        print("encode_string" + encode_string)


        # return str
        return encode_string


    def decode(self, s: str) -> List[str]:

        res = []

        i = 0

        j = 0

        # 4#neet3#wow
      
        while i < len(s):

            while s[j] != "#":

                j += 1



                # find the slice

            length = int(s[i:j])

            i = j

            res.append(s[i + 1: j + length + 1])

            j = j + length + 1

            i = j
            



        return res

