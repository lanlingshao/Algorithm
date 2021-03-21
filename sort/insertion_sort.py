"""
插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。
插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。
1. 算法步骤
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""

import random


# 插入排序是稳定的，时间复杂度最好是O(n)(当数组已经是排序的时候), 最差时O(n^2)
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp


# 对数组部分进行插入排序
def insertion_sort_sub(nums, left=None, right=None):
    if not left:
        left = 0
    if not right:
        right = len(nums) - 1
    for i in range(left + 1, right + 1):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp


if __name__ == "__main__":
    for i in range(10):
        nums = random.choices(range(1, 100), k=10)
        print(nums)
        insertion_sort(nums)
        print(nums)
        print('********************************')
