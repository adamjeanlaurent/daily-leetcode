'''
    Link: https://leetcode.com/problems/two-sum/

    Time Took: 10 Mins

    Time Complexity: O(N)

    Space Complexity: O(N)

    Date: 03/05/2025

    Problem Type: array

    Solution Explained: Create a map from val to index. loop through array, calculate the compliment to make the target. Lookup compliment in the map.

    Notes:
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            compliment = target - num

            index = lookup.get(compliment)

            if index != None:
                return [i, index]

            lookup[num] = i
        
        return []

