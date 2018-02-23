class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, nums, p = [], [], 0
        self.trackback(sorted(candidates), target, [], res, 0)
        return res

    def trackback(self, candidates, target, nums, res, p):
        if target==0:
            if nums not in res:
                res.append(nums)
            return
        if target<0 or p>=len(candidates): return
        self.trackback(candidates, target-candidates[p], nums+[candidates[p]], res, p+1)
        self.trackback(candidates, target, nums.copy(), res, p+1)

print(Solution().combinationSum2([2],2))