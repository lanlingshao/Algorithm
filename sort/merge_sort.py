"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
    自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
    自下而上的迭代；
和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间

2. 算法步骤
    申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
    设定两个指针，最初位置分别为两个已经排序序列的起始位置；
    比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
    重复步骤 3 直到某一指针达到序列尾；
    将另一序列剩下的所有元素直接复制到合并序列尾。
"""


class Solution:
    def merge_sortII(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left_half = nums[0:mid]
        right_half = nums[mid:]
        return self.merge(self.merge_sortII(left_half), self.merge_sortII(right_half))

    def merge(self, nums1, nums2):
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        return res


# Solution1相对于Solution变成了对nums原地排序，只是多了temp_right_sub_nums占用的辅助空间，但是temp_right_sub_nums最多也就占用len(nums) / 2长度的空间
class Solution1:
    def merge_sort(self, left, right, nums):
        if left < right:
            mid = left + (right - left) // 2
            self.merge_sort(left, mid, nums)
            self.merge_sort(mid + 1, right, nums)
            self.merge(left, mid, right, nums)

    def merge(self, left, mid, right, nums):
        temp_right_sub_nums = []
        for i in range(mid + 1, right + 1):
            temp_right_sub_nums.append(nums[i])
        i, j, k = mid, len(temp_right_sub_nums) - 1, right
        while i >= left and j >= 0:
            if nums[i] > temp_right_sub_nums[j]:
                nums[k] = nums[i]
                i -= 1
            else:
                nums[k] = temp_right_sub_nums.pop()
                j -= 1
            k -= 1
        while j >= 0:
            nums[k] = temp_right_sub_nums.pop()
            j -= 1
            k -= 1


if __name__ == "__main__":
    nums1 = [3,1,4,6,7,8,2,0]
    merge_sort(nums1)
    print(nums1)
    nums2 = [3,1,4,6,7,8,2,0]
    print(merge_sortII(nums2))
