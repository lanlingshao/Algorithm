"""
桶排序（Bucket sort）或所谓的箱排序，是一个排序算法，工作的原理是将数组分到有限数量的桶里。每个桶再个别排序
（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。桶排序是鸽巢排序的一种归纳结果。当要被排序的数组内的数值是均匀分配的时候，
桶排序使用线性时间O(n)。但桶排序并不是比较排序，他不受到O(nlogn)下限的影响。

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

在额外空间充足的情况下，尽量增大桶的数量
使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

1. 什么时候最快
当输入的数据可以均匀的分配到每一个桶中。

2. 什么时候最慢
当输入的数据被分配到了同一个桶中。

时间复杂度分析：
如果要排序的数据有n个，我们把它们分在m个桶中，这样每个桶里的数据就是k = n / m。每个桶内排序的时间复杂度就为O(k*logk)。
m个桶就是m * O(k * logk)=m * O((n / m)*log(n / m))=O(nlog(n / m))。当桶的个数m接近数据个数n时，log（n/m）就是一个较小的常数，
所以时间复杂度接近O(n)。

桶排序以下列程序进行：

1、设置一个定量的数组当作空桶子。
2、寻访序列，并且把项目一个一个放到对应的桶子去。
3、对每个不是空的桶子进行排序。
4、从不是空的桶子里把项目再放回原来的序列中。
"""

from sort.insertion_sort import insertion_sort

# 这个方法是稳定的，因为桶内使用的是插入排序，而插入排序是稳定的，如果桶内部用快排，那就是稳定的了
def bucket_sort(nums):
    min, max = nums[0], nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    step = 9
    bucket_num = max // step - min // step + 1
    bucket_list = []
    for i in range(bucket_num):
        bucket_list.append([])
    for i in range(len(nums)):
        index = index_for(nums[i], min, step)
        bucket_list[index].append(nums[i])
    index = 0
    for i in range(bucket_num):
        bucket = bucket_list[i]
        insertion_sort(bucket)
        for k in bucket:
            nums[index] = k
            index += 1


def index_for(num, min, step):
    return (num - min) // step


if __name__ == "__main__":
    import random
    sort = bucket_sort
    for i in range(10):
        nums = random.choices(range(1, 100), k=10)
        print(nums)
        sort(nums)
        print(nums)
        print('********************************')
