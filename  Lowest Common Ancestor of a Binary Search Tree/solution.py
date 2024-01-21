# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Time complexity O(n*h) where h is the height of binary tree
Space complexity O(h)
TODO: Binary lifting (linear time preprocessing constant time query)

Another implementation of linear(h) time and linear(h) space can be implemented 
Store the path for both p and q 
and iterate through them (lca will be when the path diverges)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        def find(root, p):
            if root is None:
                return False
            if root == p:
                return True
            return find(root.left, p) or find(root.right, p)
        
        p_in_left = find(root.left, p)
        q_in_left = find(root.left, q)
        p_in_right = find(root.right, p)
        q_in_right = find(root.right, q)

        print(root.val)
        print(p_in_left, q_in_left, p_in_right, q_in_right)
            
        if (p_in_left and q_in_right) or (p_in_right and q_in_left):
            return root
        elif p_in_left and q_in_left:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
    
    