"""
计数排序（Counting sort）是一种稳定的线性时间排序算法。该算法于1954年由 Harold H. Seward 提出。计数排序使用一个额外的数组C ，
其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C 来将A中的元素排到正确的位置。
1. 计数排序的特征
当输入的元素是 n 个 0 到 k 之间的整数时，它的运行时间是 Θ(n + k)。计数排序不是比较排序，因此不被nlogn的下界限制。排序的速度快于任何比较排序算法。

由于用来计数的数组C的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，
需要大量时间和内存。例如：计数排序是用来排序0到100之间的数字的最好的算法，但是它不适合按字母顺序排序人名。但是，计数排序可以用在基数排序中的算法来排序数据范围很大的数组。

 算法的步骤如下：
（1）找出待排序的数组中最大和最小的元素
（2）统计数组中每个值为i的元素出现的次数，存入数组C的第i项
（3）遍历数组C，通过下表i和最小值算出值num,将num加入最终数组中，然后count - 1
此方法破坏了稳定性，只适用于纯数字的,如果是用于卫星数据排序的话，就把原来关键字相同的数组顺序打乱了

算法II的步骤如下：
（1）找出待排序的数组中最大和最小的元素
（2）统计数组中每个值为i的元素出现的次数，存入数组C的第i项
（3）对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
（4）反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
"""


# 此方法破坏了稳定性，只适用于纯数字的,如果是用于卫星数据排序的话，就把原来关键字相同的数组顺序打乱了
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


def counting_sort_2(nums):
    b = [0] * len(nums)
    min, max = nums[0], nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    c = [0] * (max - min + 1)
    for num in nums:
        c[num - min] += 1
    for i in range(1, len(c)):  # c[i]为nums中小于等于nums[min+i]的数量
        c[i] = c[i - 1] + c[i]
    for i in range(len(nums) - 1, -1, -1): # 倒序可以保证之前相同数字的顺序，保证稳定性
        c[nums[i] - min] -= 1
        b[c[nums[i] - min]] = nums[i]
    return b


if __name__ == "__main__":
    sort = counting_sort_2
    print(sort([2,3,6,6,6,4,7,8]))
    print(sort([9,1,3,5,6,8,8,7,2]))
    print(sort([9,1,1,5,6,8,4,7,2]))


