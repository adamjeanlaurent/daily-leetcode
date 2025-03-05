'''
    Link: https://leetcode.com/problems/subsets/

    Time Took: 17 Mins

    Time Complexity: O(n * 2^n) (I guess because  this is the number of subsets. At each index in the array, we spawn a subtree)

    Space Complexity: O(n) (since we are re-using the same subset array, and only copy on append to result)

    Date: 03/02/2025

    Problem Type: backtracking

    Solution Explained: Essentially create a decision tree of all possibilities. At each index you have 2 options to branch off into, add index X to subset, and don't.
    Your answers are the leaf nodes of this tree.

    Notes:
'''

from typing import List

class Solution:
    res: List[List[int]]
    nums: List[int]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums

        self.subsets_helper(0, [])
        return self.res

    def subsets_helper(self, index, subset):
        if index == len(self.nums):
            self.res.append(subset.copy())
            return
        
        # branch off twice
        subset.append(self.nums[index])
        index += 1

        self.subsets_helper(index, subset)
        subset.pop()
        self.subsets_helper(index, subset)
