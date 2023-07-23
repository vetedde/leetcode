# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    p = 0
    neg_nums = []
    for neg_n in nums:
        if neg_n >= 0:
            break

        neg_nums.append(neg_n * -1)
        p += 1

    nums = nums[p:]
    p_neg = len(neg_nums) - 1
    p = 0

    while p < len(nums) or p_neg >= 0:
        if p < len(nums) and p_neg >= 0:
            if neg_nums[p_neg] <= nums[p]:
                nums = nums[:p] + [neg_nums[p_neg]*neg_nums[p_neg]] + nums[p:]
                p += 1
                p_neg -= 1
            else:
                nums[p] *= nums[p]
                p += 1
        elif p < len(nums) and not(p_neg >= 0):
            nums[p] *= nums[p]
            p += 1
        elif not(p < len(nums)) and p_neg >= 0:
            nums = nums[:p] + [neg_nums[p_neg] * neg_nums[p_neg]] + nums[p:]
            p_neg -= 1
            p += 1
        else:
            print("!Attention")
            break
    return nums

print(sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100])
print(sortedSquares([-4,-1,3,10]) == [1, 9, 16, 100])
print(sortedSquares([-4,-1,2,3,10]) == [1, 4, 9, 16, 100])
print(sortedSquares([-4,-1]) == [1, 16])
print(sortedSquares([1, 4]) == [1, 16])
print(sortedSquares([-4, 1, 4]) == [1, 16, 16])
