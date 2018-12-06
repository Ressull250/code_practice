class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        d = []
        def preorder(node):
            if not node:
                d.append("#")
                return
            d.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return d

    def deserialize(self, data):

        def dfs():
            if data[0] == '#':
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()