class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # mapping characterCount to list of Anagrams
        

        # get the count of each word
        for word in strs:
            count = [0] * 26 # a ... z
            for char in word:
                count[ord(char) - ord("a")] += 1 # +1 to count how can of each character we have?

            dict[tuple(count)].append(word)
        # print the list of anagrams
        return(list(dict.values()))

