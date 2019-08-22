"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp


if __name__ == "__main__":
    nums = [3,1,4,6,7,8,2,0]
    insertion_sort(nums)
    print(nums)
