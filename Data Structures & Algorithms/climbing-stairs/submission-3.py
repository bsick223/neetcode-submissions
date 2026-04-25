class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, cache):
            if n <= 2:
                return n

            if n not in cache: 
                cache[n] = dp(n-1, cache) + dp(n-2, cache)

            return cache[n]

        return dp(n, {})