def twoSum(numbers, target: int):
    end = len(numbers)-1
    begin = 0
    while numbers[end] + numbers[begin] != target:
        if numbers[end] + numbers[begin] > target:
            end -= 1
        else:
            begin += 1
    return [begin, end]

twoSum([2,7,11,15],9)