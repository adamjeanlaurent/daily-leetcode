
'''
    Link: https://leetcode.com/problems/koko-eating-bananas/

    Time Took: A long time 

    Time Complexity: O(nLogM)

    Space Complexity: O(1)

    Date: 02-08-2025

    Problem Type: binary-search

    Solution Explained: Okay soooo essentially, the goal is try find k. There isn't an exact forumla to get K, so you need to try Ks. You can be smart about it if you use binary search to determine K. you know that the largest possible K is the largest pile, and that the smallest K is always 1. so in the range 1....max(pile). binary search through there. 
    
    Notes: python has math.ceil(), python has math.inf (which is a float that you can't turn into an int), python you can't do if !bool:, have to use not keyword. Definitely, this is the type of problem where you should have started with the dumbest possible thing, and improved it. Searching for the exact formula to solve htis is too hard.
'''

import math
from typing import List

class Solution:
    # return true if can finish bananas before time is up
    def tryK(self, k):
        hoursTaken = 0

        for pile in self.piles:
            hoursTaken += math.ceil(pile / k)

            if hoursTaken > self.hours:
                return False

        return True
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.hours = h

        minK = 1
        maxK = max(piles)
        res = int(math.inf)
        
        while minK <= maxK:
            mid = (minK + maxK) // 2

            # try mid as k
            possible: bool = self.tryK(mid)

            if not possible:
                # too small
                minK = mid + 1
            else:
                #  is possible
                # either this is the exact answer
                # or it's too large
                res = mid
                maxK = mid - 1
                
        return res
