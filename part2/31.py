class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1: return
        list1 = [nums[-1]]
        index = -1
        for i in range(len(nums)-1)[::-1]:
            if nums[i] >= list1[-1]:
                list1.append(nums[i])
            else:
                index = i
                break

        if index == -1:
            ret = sorted(nums)
        else:
            ret = nums[0:i]

            for i in sorted(list1):
                if i > nums[index]:
                    num = i
                    break
            ret.append(num)
            list1.remove(num)
            list1.append(nums[index])
            ret.extend(sorted(list1))

        for i in range(len(nums)):
            nums[i] = ret[i]
        return




print(Solution().nextPermutation([1,2,3]))