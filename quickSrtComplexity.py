def insertionSort(nums):
    count = 0
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i-1
        while j>=0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            count += 1
            j -= 1
        nums[j+1] = tmp
    return count

def partition(nums, l, r, c):
    pivot = nums[r]
    lo = l
    for i in range(l, r):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            c.append(None)
            lo += 1
    nums[lo], nums[r] = nums[r], nums[lo]
    c.append(None)
    return lo

def quickSort(nums, l, r, c):
    if l < r:
        pos = partition(nums, l, r, c)
        quickSort(nums, l, pos-1, c)
        quickSort(nums, pos+1, r, c)

n = input()
nums = list(map(int, input().strip().split()))
import copy
numsCopy = copy.copy(nums)
c = []
quickSort(nums, 0, len(nums)-1, c)
print (insertionSort(numsCopy) - len(c))
