/*
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Time Took: 8 minutes 

    Time Complexity: O(N)

    Space Complexity: O(N)

    Solution Explained: You can do bfs or dfs for this. For bfs you would traverse the tree level by level.
        The number of levels if your answer. For a dfs solution you do a bubble up approach.
        At each node, the depth of the longest binary tree starting at that node, is 
        1 + Math.max(depth(left), depth(right))
*/

namespace MaximumDepthOfBinaryTree {
    class TreeNode {
        val: number
        left: TreeNode | null
        right: TreeNode | null
        constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
            this.val = (val===undefined ? 0 : val)
            this.left = (left===undefined ? null : left)
            this.right = (right===undefined ? null : right)
        }
   }
   
   function maxDepth(root: TreeNode | null): number {
       if (!root)
           return 0;
   
       const leftDepth: number = maxDepth(root.left);
       const rightDepth: number = maxDepth(root.right);
   
       return 1 + Math.max(leftDepth, rightDepth);
   }
}
