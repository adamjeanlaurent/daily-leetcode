'''
    Link: https://leetcode.com/problems/min-cost-climbing-stairs/

    Time Took:  35 minutes

    Time Complexity: O(N)

    Space Complexity: O(1)

    Date: 02/28/2025

    Problem Type: 1d-dynamic

    Solution Explained: The min cost to get to a step = 
        min (
            (min cost of getting to prev step + prev step),
            (min cost of getting to prev prev step + prev prev step)
        )
    Base cases are that you can start at step 0 or 1 with no cost. So zero for both.

    Notes: This was a tough one, I think I did a good job understanding fundementally that there were 3 solutions, 1. brute force calc all possibilites (dfs every path), 2. opitimized brute force with memoization.
    3. current min step cost = function of min cost of prev 2 steps. My trouble was that I misunderstood the starting point and fumbled on the code for a bit.
    Fundemental question to ask myself here to arrive at the solution, was, at step 0 or 1 how can I know the min cost of getting there, and then use that for step 3 and so on.
'''
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevPrevCost = 0
        prevCost = 0

        for i in range(2, len(cost) + 1): 
            costToGetToIthStep = min(prevPrevCost + cost[i - 2], prevCost + cost[i - 1])
            prevPrevCost = prevCost
            prevCost = costToGetToIthStep

        return prevCost


