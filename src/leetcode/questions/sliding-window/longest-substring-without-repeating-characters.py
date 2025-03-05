'''
    Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Time Took: 25 mins

    Time Complexity: O(N)

    Space Complexity: O(M) (M = size of longest substring)

    Date: 02/27/2025

    Problem Type: sliding-window

    Solution Explained: Sliding window. Have a left and a right pointer. Store the current window in a set. Keep movinig
    the right side of the window by 1. If the new char is in the window, trim the window from the left until the duplicate is no longer there.
    There is a further opitimzation that could be made if you use a map instead of a set, but I really don't like that idea.

    Notes: 
'''

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        seen = set(s[0])
        longest = 1
        right = 1

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            
            longest = max(longest, right - left + 1)

            right += 1
        
        return longest
