# -*- coding: utf-8 -*-

# 1. Two Sum
def two_sum(nums, target):
    '''
    :type nums: list[int]
    :type target: int
    :rtype: list[int]
    '''
    left = 0
    for num in nums:
        x = target - num
        right = 0
        for y in nums[left+1:]:
            if y == x:
                return [left, left + 1 + right]
            right += 1
        left += 1


# 128. Longest Consecutive Sequence
def longest_consecutive_seq(nums):
    '''
    :type nums: list
    :rtype: int
    '''
    # 排除重复元素
    nums = set(nums)

    ans = 0

    while nums:
        l = r = nums.pop()

        while l - 1 in nums:
            l -= 1
            nums.remove(l)

        while r + 1 in nums:
            r += 1
            nums.remove(r)

        ans = max(ans, r - l + 1)

    return ans
