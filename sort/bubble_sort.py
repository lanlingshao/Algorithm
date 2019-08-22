"""
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
"""


def bubble_sort(nums):
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                print(j, j+1)
                nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == "__main__":
    nums = [3,1,4,6,7,8,2,0]
    bubble_sort(nums)
    print(nums)

