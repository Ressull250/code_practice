class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res,t = [],[]
        stack = [None]
        while root or stack:
            # root为空，栈不空
            if root == 'end':
                break
            if not root:
                stack.append(None)
                res.append(t)
                t=[]
                root = stack.pop(0)
            # root非空
            else:
                t.append(root.val)
                if root.left: stack.append(root.left)
                if root.right: stack.append(root.right)
                if stack:
                    root = stack.pop(0)
                else:
                    root = 'end'
        if t: res.append(t)
        res.reverse()
        return res