import random

from sort.insertion_sort import insertion_sort_sub


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


"""快排不是稳定的"""


# 来自《算法第四版》2.3.1 P184页解法
class Solution:
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
        pivot_value = array[left]
        while True:
            # 不是i < j
            while i < right and array[i] < pivot_value:
                i += 1
            # 不是j > i
            while j > left and array[j] > pivot_value:
                j -= 1
            if i >= j:
                break
            swap(array, i, j)
            i += 1
            j -= 1
        # 返回j这个很巧妙, 为什么用j呢？j是左子数组的最右边的点，j的值肯定是比pivot小的，i就可能比pivot大，
        # 所以让j和pivot交换位置，不会导致比piovt大的数值换到左半部分
        swap(array, left, j)
        return j


class Solution1:
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
        if left >= right:
            return
        if left + 3 < right:
            pivot = self.medium3_partion(array, left, right)
            self.quick_sort(array, left, pivot - 1)
            self.quick_sort(array, pivot + 1, right)
        else:
            insertion_sort_sub(array, left, right)

    def medium3_partion(self, array, left, right):
        # 先把最大值放到最右边，再将左值跟中值比较，将中值放在最左边
        mid = left + (right - left) // 2
        if array[right] < array[mid]:
            swap(array, right, mid)
        if array[right] < array[left]:
            swap(array, right, left)
        if array[left] < array[mid]:
            swap(array, left, mid)

        i = left + 1
        j = right
        pivot_value = array[left]
        while True:
            # 不是i < j
            while i < right and array[i] < pivot_value:
                i += 1
            # 不是j > i
            while j > left and array[j] > pivot_value:
                j -= 1
            if i >= j:
                break
            swap(array, i, j)
            i += 1
            j -= 1
        # 返回j这个很巧妙, 为什么用j呢？j是左子数组的最右边的点，j的值肯定是比pivot小的，i就可能比pivot大，
        # 所以让j和pivot交换位置，不会导致比piovt大的数值换到左半部分
        swap(array, left, j)
        return j


class Solution2:
    """
    选取最右边的数作为枢纽，如果最右边数是最大的，就是最坏的情况, 没法把数组分别两部分
    跟《算法导论》的伪代码差不多, 这个方法虽然代码看起来简短，实际上却不容易想出来，也不容易写出来
    """
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


if __name__ == "__main__":
    s = Solution1
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

    nums = [5,4,6,8,0,5,1,2,9,7]
    s().quick_sort(nums)
    print(nums)


