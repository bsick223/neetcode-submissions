class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)

        # we can use asci and an array of alphabet as keys
        
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            anagrams[tuple(key)].append(word)

        res = []
        for key, anagram in anagrams.items():
            res.append(anagram)
        return res
        

        # using a hasmap with the key a list and the value, the list of similar anagrams

        # then we can group the anagrams together for the result.
