'''
    Link: https://leetcode.com/problems/same-tree/

    Time Took: 9 Minutes

    Time Complexity: O(N)

    Space Complexity: O(N)

    Date: 03/10/2025

    Problem Type: tree

    Solution Explained: You must traverse both trees at the same time. You can either do bfs or dfs for this. In this case I did DFS. Do null checks, and recurse
    on whether the left and right subtrees are equal.

    Notes:
'''

from typing import Optional

class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

