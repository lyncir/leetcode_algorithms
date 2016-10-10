# -*- coding: utf-8 -*-

# 1. Two Sum
def two_sum(nums, target):
    '''
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    '''
    for num in nums:
        other = target - num
        other_nums = nums[nums.index(num) + 1:]

        if other in other_nums:
            return [nums.index(num), nums.index(other, nums.index(num) + 1)]


# 7. Reverse Integer
def reverse(x):
    '''
    :type x: int
    :rtype: int
    '''
    if x > 0:
        num = reversed(str(x))
        result = int(''.join(num))
    elif x < 0:
        num = reversed(str(abs(x)))
        result = -int(''.join(num))
    else:
        result = x

    # 32-bit integer overflow
    if not (-2**32/2 <= result <= 2**32/2):
        result = 0

    return result
        
