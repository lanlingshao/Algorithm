import heapq


class TopK(object):
    def __init__(self, array, capacity, top_type='max'):
        """
        :param array:
        :param capacity: 最大或最小的k个数
        :param top_type: max - 最大的topk  min - 最小的topk
        """
        self.heap = []
        self.capacity = capacity
        self.top_type = top_type
        self.initialize(array)

    def initialize(self, array):
        count = 0
        for item in array:
            if self.top_type == 'min':
                item = -item
            if count < self.capacity:
                heapq.heappush(self.heap, item)
                count += 1
            else:
                heapq.heappushpop(self.heap, item)

    def get_top_k(self):
        if self.top_type == 'min':
            return [-item for item in self.heap]
        return self.heap


if __name__ == "__main__":
    import random
    import time
    sort_time = 0
    heap_time = 0
    for i in range(10):
        a = random.sample(range(1,1000), 30)
        print(a)
        start_time = time.time()
        print(sorted(a)[-10:])
        middle_time = time.time()
        print(TopK(a, 10).get_top_k())
        end_time = time.time()
        sort_time += middle_time - start_time
        heap_time += end_time - middle_time
        print('***************************************')

    print(sort_time, heap_time)

    sort_time = 0
    heap_time = 0
    for i in range(10):
        a = random.sample(range(1,1000), 30)
        print(a)
        start_time = time.time()
        print(sorted(a)[:10])
        middle_time = time.time()
        print(TopK(a, 10, 'min').get_top_k())
        end_time = time.time()
        sort_time += middle_time - start_time
        heap_time += end_time - middle_time
        print('***************************************')

