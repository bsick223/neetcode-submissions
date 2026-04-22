class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs]

        # use lists as keys for hash map

        group = defaultdict(list)

        for word in strs:
            key_list = [0] * 26

            for c in word:
                key_list[ord(c) - ord("a")] += 1

            group[tuple(key_list)].append(word)

        return group.values()


        

            















































        # res = defaultdict(list)

        # for word in strs:

        #     count = [0] * 26

        #     for c in word:
        #         count[ord(c) - ord("a")] += 1
            
        #     res[tuple(count)].append(word)

        # return res.values()






























        # use a hashmap

        # append the lists and treat them as a tuple

        # save the index's

        # res = defaultdict(list) # to handle the edge case of no value in dictionary
        
        # for word in strs:

        #     count = [0] * 26

        #     for c in word:

        #         count[ord(c) - ord("a")] += 1
    
        #     res[tuple(count)].append(word) # lists cannot be keys, but tuples can.

        # return res.values()

            # O(m * n) m = number of strings

            
