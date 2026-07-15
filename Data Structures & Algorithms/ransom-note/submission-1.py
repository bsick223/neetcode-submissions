class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ranMap = [0] * 26
        ranMag = [0] * 26

        for c in ransomNote:
            ch = ord(c) - ord("a")
            ranMap[ch] += 1

        for c in magazine:
            ch = ord(c) - ord("a")
            ranMag[ch] += 1

        
        for i in range(26):

            if ranMap[i] > ranMag[i]:
                return False

        return True