'''
    Link: https://leetcode.com/problems/climbing-stairs/

    Time Took: 12 Minutes

    Time Complexity: O(N)

    Space Complexity: O(1)

    Date: 02/28/2025

    Problem Type: 1d-dynamic

    Solution Explained: Is essentially, the fibonacci sequence. The ways to get to step i = 
    ways to get to step i-1 + ways to get to step i - 2. Base cases are ways to get to 1st step = 1, ways to get to 2nd step = 2.

    Notes:
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prevPrevStepWays = 1
        prevStepWays = 2

        for _ in range(2,n):
            temp = prevPrevStepWays + prevStepWays
            prevPrevStepWays = prevStepWays
            prevStepWays = temp
        
        return prevStepWays
