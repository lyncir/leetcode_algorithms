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
