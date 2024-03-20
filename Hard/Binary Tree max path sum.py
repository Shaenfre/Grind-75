'''
Time complexity O(n)
Space complexity O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -10 ** 20

        def traverse(node: Optional[TreeNode]):
            if node is None:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            current_sum = node.val + max(left, 0) + max(right, 0)
            nonlocal best
            best = max(best, current_sum)

            return node.val + max(max(left, right), 0)

        traverse(root)
        return best