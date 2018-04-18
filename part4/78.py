class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dp(0,len(nums),nums,[],res)
        return res

    def dp(self, pos, n, nums, tlist, res):
        if n==0:
            res.append(tlist)
            return
        self.dp(pos+1,n-1,nums,tlist+[],res)
        self.dp(pos+1,n-1,nums,tlist+[nums[pos]],res)

print(Solution().subsets([]))
