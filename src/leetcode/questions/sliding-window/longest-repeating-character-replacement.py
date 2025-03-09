'''
    Link: https://leetcode.com/problems/longest-repeating-character-replacement/

    Time Took: Watched solution.

    Time Complexity: O(N)

    Space Complexity: O(N)

    Date: 03/09/2025

    Problem Type: sliding-window

    Solution Explained: Use a sliding window technique. Use a hashmap to store the counts of each char in the window.
    The condition to keep growing the window is, if you can still make character replacements to get a possible answer.
    You calculate this by finding the max occuring character, and minus it's count from the window size.
    This result you get here is the number of character replacements you would need to make in order
    for the entire window to be the same as the max occuring character.
    You need to check if that value if less than or equal to K.
    If so, keep growing the window, if not shorten the window until it's true.

    Notes: 
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        left = 0

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            res = max(right - left + 1, res)

        return res
