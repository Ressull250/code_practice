#coding=utf-8
import Queue
class Solution(object):
    def findKthLargest1(self, nums, k):
        # 暴力出奇迹
        return sorted(nums)[-k]

    def findKthLargest2(self, nums, k):
        q = Queue.PriorityQueue()
        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()

        return q.get()

    def partition(self,nums, l, r):
        key = r
        keyval = nums[r]
        while l < r:
            while l < r and nums[l] <= keyval:
                l += 1
            while l < r and nums[r] >= keyval:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[l], nums[key] = nums[key], nums[l]
        return l

    def findKthLargest(self, nums, k):
        l,r = 0,len(nums)-1
        # 第k大逆序index=k-1 正序index就是len(nums)-k
        k = len(nums)-k
        while l <= r:
            p = self.partition(nums, l, r)
            if p > k:
                r = p-1
            elif p < k:
                l = p+1
            else:
                break
        return nums[p]




print(Solution().findKthLargest([3], 1))