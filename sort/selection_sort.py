"""
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""


def selection_sort(nums):
    for i in range(0, len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == "__main__":
    nums = [3,1,4,6,7,8,2,0]
    selection_sort(nums)
    print(nums)
