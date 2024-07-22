/*
    Link: https://leetcode.com/problems/diameter-of-binary-tree/

    Time Took: 14 minutes 

    Time Complexity: O(N)

    Space Complexity: O(N) 

    Solution Explained: The maximum diameter going through a node is 
        diameter = depth(left) + depth(right)

        So, we need to need track of 2 things.
        1: The max depth of each node (the return value)
        2: The maximum diameter of the longest path running through each node (the out value)
*/

namespace DiameterOfBinaryTree {
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

   class DiameterOfBinaryTreeResult {
    maxDiameter: number = 0;
   }

    function diameterOfBinaryTree(root: TreeNode | null): number {
        const result: DiameterOfBinaryTreeResult = new DiameterOfBinaryTreeResult();
        diameterOfBinaryTreeHelper(root, result);

        return result.maxDiameter;
    }
    
    function diameterOfBinaryTreeHelper(root: TreeNode | null, result: DiameterOfBinaryTreeResult): number {
        if (!root)
            return 0;
        
        const leftDepth: number = diameterOfBinaryTreeHelper(root.left, result);
        const rightDepth: number = diameterOfBinaryTreeHelper(root.right, result);

        result.maxDiameter = Math.max(result.maxDiameter, leftDepth + rightDepth);

        return 1 + Math.max(leftDepth, rightDepth);
    }
}