# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre, inl):
            if not pre: return None
            root = TreeNode(pre[0])
            # slice
            index = inl.index(pre[0])
            inorderl = inl[0:index]
            inorderr = inl[index+1:]
            prel = pre[1:len(inorderl)+1]
            prer = pre[len(inorderl)+1:]

            # build
            l = build(prel, inorderl)
            r = build(prer, inorderr)
            root.left = l
            root.right = r
            return root

        return build(preorder,inorder)

a = Solution().buildTree([],[])
a = 1