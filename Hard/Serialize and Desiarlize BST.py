# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    Time complexity O(n)
    Space complexity O(n)
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        INF = 10**20
        
        def go(node):
            if node is None:
                ans.append(INF)
                return

            ans.append(node.val)
            go(node.left)
            go(node.right)

        go(root)
        return ",".join(map(str, ans))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        r = iter(map(int, data.split(",")))
        INF = 10**20

        def go():
            x = next(r)

            if x == INF:
                return None

            node = TreeNode(x)
            node.left = go()
            node.right = go()

            return node

        return go()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))