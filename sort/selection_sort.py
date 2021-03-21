"""
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。
唯一的好处可能就是不占用额外的内存空间了吧。
1. 算法步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
"""

# 选择排序不稳定  比如数字[8, 8, 7], 第一个数字8会被交换后第二个8右边来

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
