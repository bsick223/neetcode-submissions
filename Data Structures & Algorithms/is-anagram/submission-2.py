class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # we could sort but we can have a better space and time complexity

        # we could use hashmaps, to account for the duplicate characters

        sCount = {}
        tCount = {}

        for c in s:
            if c not in sCount:
                sCount[c] = 1
            else:
                sCount[c] += 1

        for c in t:
            if c not in tCount:
                tCount[c] = 1
            else:
                tCount[c] += 1

        return sCount == tCount