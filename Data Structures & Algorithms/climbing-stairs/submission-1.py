class Solution:
    def climbStairs(self, n: int) -> int:
        def getCount(x, cache):
            if x == n:
                return 1
            elif x >n:
                return 0
            elif x in cache:
                return cache[x]
            else:
                a = getCount(1 + x, cache)
                b = getCount(2 + x, cache)
                cache[x] =  a+b
                return cache[x]
        return getCount(0, {})
        