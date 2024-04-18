# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.


# Example 1:

# Input: root = [1, 2, 3]
# Output: 25
# Explanation:
# The root-to-leaf path 1 -> 2 represents the number 12.
# The root-to-leaf path 1 -> 3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:

# Input: root = [4, 9, 0, 5, 1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4 -> 9 -> 5 represents the number 495.
# The root-to-leaf path 4 -> 9 -> 1 represents the number 491.
# The root-to-leaf path 4 -> 0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        ans = 0

        def dfs(root, gen):
            nonlocal ans
            if not root:
                return
            
            if not root.left and not root.right:
                ans += gen * 10 + root.val
                return

            dfs(root.left, gen * 10 + root.val)
            dfs(root.right, gen * 10 + root.val)

        dfs(root, 0)

        return ans
        

                          