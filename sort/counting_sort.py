"""
1. 计数排序的特征
当输入的元素是 n 个 0 到 k 之间的整数时，它的运行时间是 Θ(n + k)。计数排序不是比较排序，排序的速度快于任何比较排序算法。

由于用来计数的数组C的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，
需要大量时间和内存。例如：计数排序是用来排序0到100之间的数字的最好的算法，但是它不适合按字母顺序排序人名。但是，计数排序可以用在基数排序中的算法来排序数据范围很大的数组。

 算法的步骤如下：

（1）找出待排序的数组中最大和最小的元素
（2）统计数组中每个值为i的元素出现的次数，存入数组C的第i项
（4）遍历数组C，通过下表i和最小值算出值num,将num加入最终数组中，然后count - 1
"""


def counting_sort(nums):
    ret = []
    min, max = nums[0], nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    count_nums = [0] * (max - min + 1)
    for num in nums:
        count_nums[num - min] += 1
    for i, count in enumerate(count_nums):
        while count > 0:
            num = min + i
            ret.append(num)
            count -= 1
    return ret


if __name__ == "__main__":
    print(counting_sort([2,3,6,6,6,4,7,8]))
    print(counting_sort([9,1,3,5,6,8,4,7,2]))
    print(counting_sort([9,1,1,5,6,8,4,7,2]))


