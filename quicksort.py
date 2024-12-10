def quicksort(nums=[int]) -> [int]:
    pivot,l,r = 0,0,(len(nums)-1)

    if len(nums) < 2:
        return nums

    while l < r:
        if nums[l] <= nums[pivot]:
            l += 1
        while True:
            if nums[r] < nums[pivot]:
                nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            break
        quicksort(nums[:l])
        quicksort(nums[l+1:])

print(quicksort([4,3,2,6]))