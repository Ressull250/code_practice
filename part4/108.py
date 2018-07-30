class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(nums):
            if not nums: return None
            n = len(nums)/2
            root = TreeNode(nums[n])
            l = build(nums[0:n])
            r = build(nums[n+1:])
            root.left = l
            root.right = r
            return root

        return build(nums)

