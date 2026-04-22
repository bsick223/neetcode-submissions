class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for c in range(len(s)):
            s_map[s[c]] = 1 + s_map.get(s[c],0)
            t_map[t[c]] = 1 + t_map.get(t[c],0)

        print(s_map)
        print(t_map)

        return s_map == t_map
    

        