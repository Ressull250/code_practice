class Solution0(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        last,res = nums[0],1
        maxres = 1
        for i in range(1,len(nums)):
            if nums[i] == last:
                continue
            elif nums[i]==last+1:
                res+=1
            else:
                maxres = max(maxres,res)
                res=1
            last=nums[i]
        maxres=max(maxres,res)
        return maxres

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        table = {}
        res = 1
        for num in nums:
            if num not in table:
                left = table.get(num-1) if num-1 in table else 0
                right = table.get(num+1) if num+1 in table else 0

                sum = left + right + 1
                table[num] = sum
                table[num-left] = sum
                table[num+right] = sum
                res = max(res, sum)
        return res

print(Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))

