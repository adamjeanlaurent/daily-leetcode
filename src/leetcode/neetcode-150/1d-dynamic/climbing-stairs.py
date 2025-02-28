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


'''
    order of steps matters

    questions:
        n is always positive?
        what if n is 0
        do you start on first step or off the stairs?

    n = 3

    1st step = 1 ways (i.e 1 step)
    2nd step = 2 ways (+ 1 from the previous step, or + 2 step from the bottom)
    3rd step =  3 ways (+ 1 from the previous step, or + 2 step from the prev prev step)
    4th step = 5 ways
    nth step = ways to get to prev step + ways to get to prev prev step

    base cases:
        1st step = 1 way
        2nd step = 2 ways
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
