# coding: utf-8
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
        while pre:
            cur = pre
            last = head = None
            # 每一层内节点
            while cur:
                if cur.left:
                    if last:
                        last.next = cur.left
                    else:
                        head = cur.left
                    last = cur.left
                if cur.right:
                    if last:
                        last.next = cur.right
                    else:
                        head = cur.right
                    last = cur.right
                cur = cur.next
            pre = head