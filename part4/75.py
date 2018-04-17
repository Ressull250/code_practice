# -*- coding:utf-8 -*-
class Solution0:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort();

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j,n = 0,0,len(nums)-1
        #i指向最后一个0的下一个位置，j指向最后一个1的下一位置，n指向第一个2的上一个位置
        #这个问题是竟然有范式的 https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        # procedure three - way - partition(A: array of values, mid: value):
        # i ← 0
        # j ← 0
        # n ← size of A - 1
        #
        # while j ≤ n:
        #     if A[j] < mid:
        #         swap
        #         A[i] and A[j]
        #         i ← i + 1
        #         j ← j + 1
        #     else if A[j] > mid:
        #         swap
        #         A[j] and A[n]
        #         n ← n - 1
        #     else:
        #     j ← j + 1

        while j <= n:
            val = nums[j]
            if val == 0:
                nums[i],nums[j] = val,nums[i]
                i+=1
                j+=1
            elif val == 2:
                nums[n],nums[j] = nums[j],nums[n]
                n-=1
            else:
                j+=1