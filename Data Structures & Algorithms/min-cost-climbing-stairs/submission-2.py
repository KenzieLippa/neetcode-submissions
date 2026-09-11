
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #first decide index one or index 2
        #well really its the same code for all of it
        def getMin(x, cache):
            if x >= len(cost) :
                # return cache.min # the idea here being the cost will be returned though im not sure because we want the min
                #maybe we actually want to return the min of cache.values
                return 0 #return our current cost
                #lets just start by getting the current cost
            elif x in cache:
                return cache[x] 
            else:
                a = getMin(x + 1, cache)
                b = getMin(x + 2, cache)
                minVal = min(a,b)
                cache[x] = minVal + cost[x]
                print(cache)
                return cache[x]
        z = getMin(0,{})
        y = getMin(1,{})
        minStep = min(z,y)
        print(z)
        return minStep

            
        