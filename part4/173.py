# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.root else False


    def next(self):
        """
        :rtype: int
        """
        def findMin(node):
            t = node.left
            if not t:
                self.root = self.root.right
                return t.val
            while t.left:
                node = node.left
                t = t.left
            node.left = t.right
            return t.val

        if self.hasNext():
            return findMin(self.root)
        else:
            return None



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())