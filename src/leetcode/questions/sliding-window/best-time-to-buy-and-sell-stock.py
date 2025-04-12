'''
    Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Time Took: 10 Mins.

    Time Complexity: O(N)

    Space Complexity: O(1)

    Date: 04/12/2025

    Problem Type: sliding-window

    Solution Explained: walk array, if a[i] is smallest price you've seen keep track, otherwise you can potentially sell so see your potential profit.

    Notes:
'''

'''
must buy and sell on dif days
you want the maximum profit
if no profit can be made, return 0

walk array, 
if a[i] is smallest price seen, use as buy day
if a[i] is bigger than smallest price seen, see potential profit from selling
return biggest profit
'''

from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = int(math.inf)

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice 
                result = max(profit, result)

        return result



