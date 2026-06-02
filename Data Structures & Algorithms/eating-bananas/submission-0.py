"""
-- Real world example: resource allocation under a time constraint. 
 piles[i] 
 h -> height of each pile
 k -> no. of banana's per hour min

e.g. 1: 
- piles = [1,4,3,2], h = 9 
    k = 1 => 10 more than 9. So, k = 2

e.g. 2:
- piles = [25,10,23,4], h = 4
    k = 25 b/c len(piles) = 4. 
    So, when h = len(piles), k = max(piles)



"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res       