class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res,nums,p = [],[],0
        self.trackback(candidates,target,nums,res,p)
        return res

    def trackback(self, candidates, target, nums, res, p):
        for i in range(p,len(candidates)):
            k,num = 0,candidates[i]
            while k*num <= target:
                tmp = target-k*num
                mynum = nums.copy()
                for _ in range(k):
                    mynum.append(num)
                if tmp == 0:
                    res.append(mynum)
                    return
                else:
                    self.trackback(candidates, tmp, mynum, res, p+1)
                k+=1
            else:
                return
        return

print(Solution().combinationSum([7,6,3,2
                                 ],7))