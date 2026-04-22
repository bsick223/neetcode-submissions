class Solution:

    def encode(self, strs: List[str]) -> str:

        # use the # as a delimeter
        # we will count the length of each word,

        # "#4neet#4code#4love#3you"

        encode_string = ""

        # loop, 
        for word in strs:
        # get length
            length = str(len(word))
        # append to encode_string
            encode_string=encode_string + length + "#" + word # or +=


        # return str
        return encode_string


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            res.append(s[j+1: j + 1 +length])
            i = j + 1 + length
            

        return res

 





        # # "#4neet#4code#4love#3you"

        # # [2:6], [8:12], [14:18],[21:24] 
        # result = []
        # # for each character
        # for c in range(len(s)):

        # # if char == #
        #     if s[c] == "#":
        #         length = int(s[c + 1])

        # # then i+1 is the length
        #         # for j in range(c+2, length + 2) # maybe string slice instead?

        #         word = s[c+2:c + length + 2]
        #         result.append(word)
        # # which is the string we will append to the list
        # return result
