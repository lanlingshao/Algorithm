"""
堆排序（英语：HeapSort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆的性质：
即子节点的键值或索引总是小于（或者大于）它的父节点。

概述:
若以升序排序说明，把数组转换成最大堆(Max-Heap Heap)，这是一种满足最大堆性质(Max-Heap Property)的二叉树：
对于除了根之外的每个节点i, A[parent(i)] ≥ A[i]。
重复从最大堆取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，并让残余的堆维持最大堆性质。

堆节点的访问:
通常堆是通过一维数组来实现的。在数组起始位置为0的情形中：

父节点i的左子节点在位置(2i+1)
父节点i的右子节点在位置(2i+2)
子节点i的父节点在位置floor((i-1)/2)
注：《算法导论》和《数据结构与算法分析》中左字节点为2i,右字节点为2i+1,父节点为i/2，因为他们的数组下表为0的位置不存放值，第一个根结点从1开始

堆的操作:
在堆的数据结构中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build Max Heap）：将堆中的所有数据重新排序，时间复杂度为O(n)，见《数据结构与算法分析c语言描述》的P142页推导
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算，时间复杂度为O(nlogn)
所以堆排序总的时间复杂度为O(nlogn)

"""
import math


class HeapSort:
    # 见《算法导论》伪代码
    def __init__(self, arr):
        self.arr = arr
        self.heap_len = len(arr)  # 数组中最大堆长度（从0到length-1为最大堆）

    def build_max_heap(self):
        # i = 第一个非叶子节点。
        # 从第一个非叶子节点开始即可。无需从最后一个叶子节点开始。
        # 叶子节点可以看作已符合堆要求的节点，根节点就是它自己且自己以下值为最大。
        for i in range(math.floor(len(self.arr) / 2), -1, -1):
            self.heapify(i)

    def heapify(self, root):  # 将以root为根的子树变为最大堆
        left = 2 * root + 1
        right = 2 * root + 2
        largest = root
        # 找出root，left，right中最大的一个作为根节点
        if left < self.heap_len and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.heap_len and self.arr[right] > self.arr[largest]:
            largest = right
        # 如果父节点被子节点调换，则需要继续判断换下后的父节点是否符合堆的特性。
        if largest != root:
            self.swap(largest, root)
            self.heapify(largest)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def sort(self):
        # 第一步：将数组堆化
        self.build_max_heap()
        # 第二步：对堆化数据排序
        # 每次都是移出最顶层的根节点A[0]，与最尾部节点位置调换，同时遍历长度 - 1。
        # 然后从新整理被换到根节点的末尾元素，使其符合堆的特性。
        # 直至未排序的堆长度为0。
        for i in range(len(self.arr) - 1, 0, -1):
            self.swap(i, 0)
            self.heap_len -= 1
            self.heapify(0)


if __name__ == "__main__":
    import random
    for i in range(10):
        nums = random.choices(range(1, 100), k=10)
        print(nums)
        HeapSort(nums).sort()
        print(nums)
        print('********************************')