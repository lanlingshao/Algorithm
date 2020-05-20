"""
有一个n边形(P0, P1, ..., Pn)， 每一条边皆为垂直或水平线段。现给定数值k，以P0为起点将n边形的周长分为k段，每段的长度相等，
请打印出k等分点的坐标(T0, T1, ..., Tk）的坐标。
"""


class Solution1:
    def find_n_gon_position(self, arr, k):
        res = []
        len_arr = self.find_len(arr)
        avg_len = sum(len_arr) / k
        print(avg_len)

        last_length = 0
        for i in range(1, len(arr)):
            cur_length = arr[i - 1] + last_length
            if cur_length > avg_len:
                pass
            else:
                last_length = cur_length





        return res

    def find_direction(self, i, arr):
        cur_postion = arr[i]
        last_postion = arr[i - 1]
        if cur_postion[0] == last_postion[0] and cur_postion[1] > last_postion:
            cur_position = 'north'
        elif cur_postion[1]

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
        print(len_arr)
        return len_arr


class Solution:
    def find_position(self,arr,k):
        res = []
        arr_len = self.find_len(arr)  # relative array with the length of edges
        average_len = sum(arr_len[:-1])/k # average length of ploygon basing on k(delete last one)
        last_len = 0 #record the length of last edges when find the target points
        arr += [arr[0]] #put the first on the last to do iteration(help we judge the last edge)
        for i in range(1,len(arr)):#go through all points of polygon
            current_len = arr_len[i-1] +last_len #when we come to new edge, the length equals to last + itself
            a,b = divmod(current_len,average_len) # divmod to find quotient and remainder
            a= int(a) # avoid of decimal
            if a >0:#mean target point is on this edge
                x_tend = arr[i][0] - arr[i-1][0]
                y_tend = arr[i][1] - arr[i-1][1]
                if x_tend ==0:#target point has same x with arr[i]
                    y_gain = y_tend/abs(y_tend)#the direction of y(up or down)
                    for j in range(1,a+1):#mean several target points are on this edge
                        gain = j*average_len - last_len
                        point = [arr[i-1][0],arr[i-1][1]+gain*y_gain]#gain and its direction
                        res.append(point)
                else:#y
                    x_gain = x_tend/abs(x_tend)
                    for k in range(1,a+1):
                        gain = k*average_len - last_len
                        point = [arr[i-1][0]+gain*x_gain,arr[i-1][1]]
                        res.append(point)
                last_len = b # in next iteration, last_ is the remainder
            elif a ==0:#when a =0, the target point are not on this edge, last_ equals to current_
                last_len = current_len
        return res
    def find_len(self,arr):
        arr_len = []
        for i in range(1,len(arr)):
            x = arr[i][0]
            x0 = arr[i-1][0]
            if x == x0:
                leng = abs(arr[i][1]-arr[i-1][1])
            else:
                leng = abs(x-x0)
            arr_len.append(leng)
        arr_len.append(abs(arr[-1][0] - arr[0][0]))
        return arr_len+[arr_len[0]] #put the first on the last to do iteration(help we judge the last edge)


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
