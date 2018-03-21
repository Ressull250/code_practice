# -*- coding:utf-8 -*-

# python不允许程序员选择采用传值还是传引用。
# python参数传递采用的肯定是“传对象引用”的方式。
# 这种方式相当于传值和传引用的一种综合。
# 如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
# 如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象

# 看到这类题心中只有暴力v1，TLE
# 根据别人的解法写的v2

#v1
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = []
        self.tkback(nums, 0, flag)
        if flag: return True
        else: return False

    def tkback(self, nums, cpos, flag):
        if flag or cpos == len(nums)-1:
            flag.append(True)
            return
        for i in range(nums[cpos]):
            self.tkback(nums, cpos+i+1, flag)

#v2
class Solution(object):
    def canJump(self, nums):
        val = 0
        for i in range(len(nums)):
            val = max(i+nums[i], val)
            if val <= i != len(nums)-1: return False
        return True


print Solution().canJump([20])
