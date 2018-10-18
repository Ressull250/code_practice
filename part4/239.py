import collections
class Solution(object):
    def maxSlidingWindow0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        def findnewMax(begin):
            end = begin+k if begin+k<=len(nums) else len(nums)
            return max([(v,idx) for idx,v in enumerate(nums[begin:end])])
        maxnum, maxidx = findnewMax(0)
        res = [maxnum]
        for i in range(k,len(nums)):
            if nums[i] >= maxnum:
                maxnum = nums[i]
                maxidx = i
            elif i-maxidx >= k:
                maxnum, maxidx = findnewMax(i-k+1)
                pass
            res.append(maxnum)
        return res

    def maxSlidingWindow(self, nums, k):
        if not nums: return []

        res = []
        queue = collections.deque()

        for i,num in enumerate(nums):
            if queue and i - queue[0] >= k:
                queue.popleft()
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])

        return res

print Solution().maxSlidingWindow([7,2,4],
2)



