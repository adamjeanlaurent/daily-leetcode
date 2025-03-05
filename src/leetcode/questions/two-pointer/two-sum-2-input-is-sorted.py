
'''
    Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Time Took: 12 minutes

    Time Complexity: O(N)

    Space Complexity: O(1)
    
    Date: 02-08-2025

    Problem Type: two-pointer

    Solution Explained: Since array is sorted, you can do a one pass. have a left ptr at the beginning, right ptr at the end, and move move them forward and backward respectively seeing if you get your sum, if they cross then it's over.

    Notes: 
'''

# duplicates are possible 
# array is not decreasing, only increasing and duplicates
# find index (+1) of 2 numbers that add up to target

# time: O(N)
# space: O(1)

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return []


