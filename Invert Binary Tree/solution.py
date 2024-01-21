# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Did post order traversal (can be done with preorder or inorder as well)
Time complexity : O(n)
Space complexity : O(h) where h is the height of binary tree (could be n or logn) (depending on the type of binary tree)
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        # print(root.val)
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root