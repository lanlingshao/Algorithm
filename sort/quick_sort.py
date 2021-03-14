import random

from sort.insertion_sort import insertion_sort_sub


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


"""
选取最右边的数作为枢纽，如果最右边数是最大的，就是最坏的情况, 没法把数组分别两部分
from https://www.geeksforgeeks.org/python-program-for-quicksort/
跟《算法导论》的伪代码差不多
"""
class Solution(object):
    def quick_sort(self, array, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(array) - 1
        if left < right:
            pivot = self.partition(array, left, right)
            self.quick_sort(array, left, pivot - 1)
            self.quick_sort(array, pivot + 1, right)

    def partition(self, array, left, right):
        i = left - 1
        pivot = array[right]
        for j in range(left, right):
            if array[j] < pivot: # 小于等于使左边的子数组都是小于等于pivot,用小于也是可以的
                i += 1
                swap(array, i, j)
        swap(array, i + 1, right)
        return i + 1


class Solution1(object):
    """
    三值中值分割法(消除了预排序输入的最坏情况)
    小数组用插入排序比快排更好,可以节约15%时间
    详情见《数据结构与算法分析 c语言描述》
    """
    def quick_sort(self, array, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(array) - 1
        if left + 3 <= right:
            pivot_index = self.medium3_partion(array, left, right)
            self.quick_sort(array, left, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, right)
        else:
            insertion_sort_sub(array, left, right)

    def medium3_partion(self, array, left, right):
        mid = left + (right - left) // 2
        # 取中值的比较顺序必须使left-mid,left-right,mid-right,比较完left再比较其他值，不能是left-mid,mid-right,left-right，如24,29,22
        if array[left] > array[mid]:
            swap(array, left, mid)
        if array[left] > array[right]:
            swap(array, left, right)
        if array[mid] > array[right]:
            swap(array, mid, right)
        swap(array, mid, right - 1)

        pivot = array[right - 1]
        i, j = left, right - 1  # 虽然array[i]已经是比pivot小了，但因为后面i要先加1，所以直接从i开始，不从i+1开始,j同理
        while i < j:
            i += 1  # 先加1,使不需要考虑特殊情况
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i < j:  # 必须i < j才交换，因为i可能大于等于j
                swap(array, i, j)
        swap(array, i, right - 1)
        return i


# 来自《算法第四版》解法
class Solution2:
    def quick_sort(self, array, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(array) - 1
        if left >= right:
            return
        pivot = self.partion(array, left, right)
        self.quick_sort(array, left, pivot - 1)
        self.quick_sort(array, pivot + 1, right)

    def partion(self, array, left, right):
        i = left + 1
        j = right
        pivot = array[left]
        while True:
            # 不是i < j
            while i < right and array[i] < pivot:
                i += 1
            # 不是j > i
            while j > left and array[j] > pivot:
                j -= 1
            if i >= j:
                break
            swap(array, i, j)
            i += 1
            j -= 1
        # 返回j这个很巧妙
        swap(array, left, j)
        return j



if __name__ == "__main__":
    s = Solution2
    nums = list(range(0,10))
    for i in range(10):
        random.shuffle(nums)
        print(nums)
        s().quick_sort(nums)
        print(nums)
        print('*****************************')

    nums = [5,4,6,8,0,3,1,2,9,7]
    s().quick_sort(nums)
    print(nums)



