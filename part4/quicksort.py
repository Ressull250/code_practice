def qsort(nums, l, r):
    if l > r: return
    p = partition(nums, l, r)
    qsort(nums, l, p-1)
    qsort(nums, p+1, r)
    pass

def partition(nums, l, r):
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

list = [0]
qsort(list,0,len(list)-1)
print list




