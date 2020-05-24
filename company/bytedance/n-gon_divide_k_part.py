"""
有一个n边形(P0, P1, ..., Pn)， 每一条边皆为垂直或水平线段。现给定数值k，以P0为起点将n边形的周长分为k段，每段的长度相等，
请打印出k等分点的坐标(T0, T1, ..., Tk）的坐标。
"""


class Solution:
    def find_n_gon_position(self, arr, k):
        res = []
        len_arr = self.find_len(arr)
        avg_len = sum(len_arr[:-1]) / k
        # 考虑分点在最后一条边上的边界条件
        arr.append(arr[0])

        last_length = 0
        for i in range(1, len(arr)):
            cur_length = len_arr[i - 1] + last_length
            if cur_length > avg_len:
                last_length = cur_length - avg_len
                direction = self.find_direction(i, arr)
                if direction == 'up':
                    res.append([arr[i][0], arr[i][1] - last_length])
                elif direction == 'down':
                    res.append([arr[i][0], arr[i][1] + last_length])
                elif direction == 'right':
                    res.append([arr[i][0] - last_length, arr[i][1]])
                else:
                    res.append([arr[i][0] + last_length, arr[i][1]])

                # 一条边上不止一个分点的时候
                while last_length >= avg_len:
                    cur_length = cur_length - avg_len
                    last_length = cur_length - avg_len
                    if direction == 'up':
                        res.append([arr[i][0], arr[i][1] - last_length])
                    elif direction == 'down':
                        res.append([arr[i][0], arr[i][1] + last_length])
                    elif direction == 'right':
                        res.append([arr[i][0] - last_length, arr[i][1]])
                    else:
                        res.append([arr[i][0] + last_length, arr[i][1]])
            elif cur_length < avg_len:
                last_length = cur_length
            else:
                res.append(arr[i])
                last_length = 0

        return res

    def find_direction(self, i, arr):
        cur_postion = arr[i]
        last_postion = arr[i - 1]
        if cur_postion[0] == last_postion[0]:
            if cur_postion[1] > last_postion[0]:
                direction = 'up'
            else:
                direction = 'down'
        else:
            if cur_postion[0] > last_postion[0]:
                direction = 'right'
            else:
                direction = 'left'
        return direction

    def find_len(self, arr):
        len_arr = []
        arr_len = len(arr)
        for i in range(arr_len):
            cur_point = arr[i]
            next_point = arr[(i + 1) % arr_len]
            if cur_point[0] == next_point[0]:
                len_arr.append(abs(cur_point[1] - next_point[1]))
            else:
                len_arr.append(abs(cur_point[0] - next_point[0]))
        # 考虑分点在最后一条边上的边界条件
        len_arr.append(len_arr[0])
        return len_arr


if __name__ == "__main__":
    su = Solution()
    arr = [[1, 1], [1, 2], [2, 2], [2, 3], [4, 3], [4, 1]]
    k = 8
    res = su.find_n_gon_position(arr, k)
    print(res)

    su = Solution()
    arr = [[4, 1], [1, 1], [1, 2], [2, 2], [2, 3], [4, 3]]
    k = 8
    res = su.find_n_gon_position(arr, k)
    print(res)
