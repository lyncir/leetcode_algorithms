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

# 338. Counting Bits
def count_bits(num):
    """
    :type num: int
    :rtype: list[int]
    """
    rets = [0 for i in xrange(num + 1)]
    pow = 1
    t = 0
    for i in xrange(1, num +1):
        if i == pow:
            pow *= 2
            t = 0
        rets[i] = rets[t] + 1
        i += 1
        t += 1
    return rets


# 412. Fizz Buzz
def fizz_buzz(n):
    """
    :type n: int
    :rtype: list[str]
    """
    rets = [str(i) for i in xrange(1, n+1)]
    for i in xrange(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            rets[i-1] = "FizzBuzz"
        elif i % 3 == 0:
            rets[i-1] = "Fizz"
        elif i % 5 == 0:
            rets[i-1] = "Buzz"
    return rets


# 344. Reverse String
def reverse_string(s):
    """
    :type s: str
    :trype: str
    """
    return s[::-1]
