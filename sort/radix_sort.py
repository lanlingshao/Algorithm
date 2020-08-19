"""
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

1. 基数排序 vs 计数排序 vs 桶排序
这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：
基数排序：根据键值的每位数字来分配桶；
计数排序：每个桶只存储单一键值；
桶排序：每个桶存储一定范围的数值；

参考https://www.runoob.com/w3cnote/radix-sort.html
"""


def radix_sort(arr):
    def get_max_num():
        max_num = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_num:
                max_num = arr[i]
        return max_num

    def get_max_digits():
        max_digit = 0
        temp_max_num = max_num
        while temp_max_num > 0:
            max_digit += 1
            temp_max_num //= 10
        return max_digit

    max_num = get_max_num()
    max_digit = get_max_digits()
    for i in range(max_digit):
        bucket_list = [[] for i in range(10)]
        for n in arr:
            x = (n // 10**i) % 10
            bucket_list[x].append(n)
        i = 0
        for bucket in bucket_list:
            for num in bucket:
                arr[i] = num
                i += 1
    return arr


if __name__ == "__main__":
    import random
    for i in range(100):
        nums = random.choices(range(1, 1000), k=10)
        print(nums)
        copy_nums = nums.copy()
        radix_sort(nums)
        assert(sorted(copy_nums) == nums)
        print(nums)
        print('********************************')