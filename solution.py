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


# 413. Arithmetic Slices
def number_of_arithmetic_slices(A):
    """
    :type A: list[int]
    :rtype: int
    question: when A = [7, 7, 7, 7, 7] return 6? why 3?
    """
    size = len(A)
    if size < 3:
        return 0
    ans = cnt = 0
    delta = A[1] - A[0]
    for i in range(2, size):
        if A[i] - A[i-1] == delta:
            cnt += 1
            ans += cnt
        else:
            delta = A[i] - A[i -1]
            cnt = 0

    return ans


# 136. Single Number
def single_number(nums):
    """
    :type nums: list[int]
    :rtype: int
    """
    return reduce(lambda x,y: x^y, nums)


# 406. Queue Reconstruction by Height
def reconstruct_queue(people):
    """
    :type people: list[list[int]]
    :trype: list[list[int]]
    """
    people = sorted(people, key=lambda n: (-n[0], n[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res


# 371. Sum of Two Integers
def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000

    while b:
        ans = a ^ b
        carry = (a & b) << 1
        a = ans % MASK
        b = carry % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


# 104. Maximum Depth of Binary Tree
class TreeNode(object):
    
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop()
        print node.val
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
