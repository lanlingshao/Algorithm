import random

from sort.insertion_sort import insertion_sort_sub


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


class QuickSortI(object):
    """
    选取最右边的数作为枢纽，如果最右边数是最大的，就是最坏的情况, 没法把数组分别两部分
    from https://www.geeksforgeeks.org/python-program-for-quicksort/
    """
    def quick_sort(self, array, left=None, right=None):
        if not left:
            left = 0
        if not right:
            right = len(array) - 1
        if left < right:
            pivot = self.partition(array, left, right)
            self.quick_sort(array, left, pivot - 1)
            self.quick_sort(array, pivot + 1, right)

    def partition(self, array, left, right):
        # 从left-1开始很巧妙
        #
        i = left - 1
        for j in range(left, right):
            # j左边的都是比array[right]大
            if array[j] <= array[right]:
                i += 1
                swap(array, i, j)
        swap(array, i + 1, right)
        return i + 1


class QuickSortII(object):
    """
    三值中值分割法(消除了预排序输入的最坏情况)
    小数组用插入排序比快排更好,可以节约15%时间
    详情见《数据结构与算法分析 c语言描述》
    """
    def quick_sort(self, array, left=None, right=None):
        if not left:
            left = 0
        if not right:
            right = len(array) - 1
        if left + 3 <= right:
            pivot = self.medium3(array, left, right)
            i, j = left, right - 2
            while True:
                i += 1 # 先加1,使不需要考虑特殊情况
                while array[i] < pivot:
                    i += 1
                j -= 1
                while array[j] > pivot:
                    j -= 1
                if i < j:
                    swap(array, i, j)
                else:
                    break
            swap(array, i, right - 1)
            self.quick_sort(array, left, i - 1)
            self.quick_sort(array, i + 1, right)
        else:
            insertion_sort_sub(array, left, right)

    def medium3(self, array, left, right):
        mid = left + (right - left) // 2
        if array[left] > array[mid]:
            swap(array, left, mid)
        if array[mid] > array[right]:
            swap(array, mid, right)
        if array[left] > array[right]:
            swap(array, left, right)
        swap(array, mid, right - 1)
        return array[right - 1]


if __name__ == "__main__":
    for i in range(10):
        nums = random.choices(range(1, 100), k=10)
        print('********************************')
        print(nums)
        QuickSortII().quick_sort(nums)
        print(nums)
        print('********************************')
