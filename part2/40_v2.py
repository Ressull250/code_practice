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

    def trackback(self, candidates, targer, nums, res, pos):
        if targer == 0:
            res.append(nums)
            return
        if targer < 0:
            return
        for i in range(pos,len(candidates)):
            if i > pos and candidates[pos] == candidates[pos-1]: continue
            else:
                self.trackback(candidates, targer-candidates[i], nums+[candidates[i]], res, i+1)
        return

print(Solution().combinationSum2([1,1,2,3,6,7,1],7))