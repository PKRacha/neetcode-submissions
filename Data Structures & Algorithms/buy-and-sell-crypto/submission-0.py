"""
prices: list
pick a single day to buy
different day in future to sell

e.g.1:
prices =    10, 1, 5, 6, 7, 1 
result =        B        S      = 7 - 1  = 6
Means ->>  find min in the array and find max after the min position. 
            That will be max profit.

Two pointer solution... is the best TC: O(n) and SC: O(1)

corner cases: 
1. when empty prices -> X
2. when 1 values -> 0
3. Its all descending -> 0 


"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices): # right pointer until end
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            # When we find the less value in the right, we move left
            else:
                l = r
            r += 1
        return maxP
        