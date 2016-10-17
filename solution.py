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
        

# 9. Palindrome Number
def is_palindrome(x):
    '''
    :type x: int
    :trype: bool
    '''
    if x < 0:
        return False

    if x < 10:
        return True

    s = str(x)
    if len(s)%2 == 0:
        left = s[:len(s)/2]
        right = s[-len(s)/2:]
    else:
        left = s[:len(s)/2]
        right = s[-len(s)/2 + 1:]
    right = ''.join(reversed(right))

    if left == right:
        return True
    else:
        return False

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
