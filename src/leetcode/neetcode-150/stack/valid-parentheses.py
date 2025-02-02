'''
    Link: https://leetcode.com/problems/valid-parentheses/

    Time Took: 19 minutes

    Time Complexity: O(N)

    Space Complexity: O(N)
    
    Date: 02-02-2025

    Problem Type: Stack

    Solution Explained: When you see an opening bracket push it on the stack, when you see a closeing bracket, pop from the stack and ensure the last opening matches the type.

    Notes: If order didn't matter here, i.e if something like ([)] were valid, you wouldn't need to stack at all and could just count, but you need the stack to preserve order.
'''

# extreanous with no later close == flase
# close with no previous opening == false
# every opening bracket must have a closing partner

# logic:
# scan string char by char
    # if opening bracket, take note
    # if closing bracket, look at note
        # if not previous opening, return false
        # if previous opening, remove note
# check if any opens left
    # if so return false
# return true
    
# opensLeft = int

# [(]) = valid ?
# I think not so let's use stack.

# scan string char by char
    # if opening bracket, push on stack
    # if closing bracket, pop from stack
        # if not previous opening same type, return false
        # if previous opening same type
# check if stack empty
    # if so return false
# return true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in openToClose:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                lastOpening = stack.pop()
                if openToClose.get(lastOpening) != char:
                    return False

        return len(stack) == 0
