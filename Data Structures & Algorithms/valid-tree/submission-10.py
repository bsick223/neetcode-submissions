class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection -> add everything to a set, and if both nodes in set already, not possible

        # every node must be reachable -> 
        # after adding first, then if the [a,b], a or b is not in set, return false.
        # if n ==1:
        #     return False

        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)