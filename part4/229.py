class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,num2,count1,count2 = -1,-1,0,0
        for i in nums:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1,count1 = i,1
            elif count2 == 0:
                num2,count2 = i,1
            else:
                count1 -= 1
                count2 -= 1
        return [i for i in (num1,num2) if nums.count(i) > len(nums)/3]

print Solution().majorityElement([1,2])