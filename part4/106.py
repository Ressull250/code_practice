# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder: return None
        root = TreeNode(postorder[-1])
        # slice
        index = inorder.index(postorder[-1])
        inorderl = inorder[0:index]
        inorderr = inorder[index+1:]
        postl = postorder[0:len(inorderl)]
        postr = postorder[len(inorderl):-1]

        # build
        l = self.buildTree(inorderl, postl)
        r = self.buildTree(inorderr, postr)
        root.left = l
        root.right = r
        return root

a = Solution().buildTree([9,3,15,20,7],\
[9,15,7,20,3])
a = 1