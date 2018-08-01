# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        t = []
        stack = [None]
        while root or stack:
            # root为空，栈不空
            if root == 'end':
                break
            if not root:
                stack.append(None)
                for i,tree in enumerate(t):
                    if i+1 < len(t):
                        tree.next = t[i+1]
                t=[]
                root = stack.pop(0)
            # root非空
            else:
                t.append(root)
                if root.left: stack.append(root.left)
                if root.right: stack.append(root.right)
                if stack:
                    root = stack.pop(0)
                else:
                    root = 'end'
        if t:
            for i, tree in enumerate(t):
                if i + 1 < len(t):
                    tree.next = t[i + 1]

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        pre = root
        cur = None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next: cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left