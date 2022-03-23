def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    end = 0
    begin = 0
    while end < len(nums) and begin < len(nums):
        while end < len(nums) and nums[end] == 0:
            end += 1
        while begin < end and nums[begin] != 0:
            begin += 1
        if end == len(nums) or begin == len(nums):
            return
        (nums[begin], nums[end]) = (nums[end], nums[begin])


moveZeroes(nums=[0, 2, 4, 0])
