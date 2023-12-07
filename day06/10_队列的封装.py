class Queue(object):
    """
    队列的封装
    1. 列表的左侧队尾
    2. 列表的右侧队头
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """入队"""
        self.queue.insert(0, value)
        print("入队元素为:", value)

    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise Exception("队列为空")
        item = self.queue.pop()
        print("出队元素:", item)
        return item

    def __len__(self):
        """获取队列的长度"""
        return len(self.queue)

    def first(self):
        """获取队头元素"""
        if self.is_empty():
            raise Exception("队列为空")
        return self.queue[-1]

    def last(self):
        """获取队尾元素"""
        if self.is_empty():
            raise Exception("队列为空")
        return self.queue[0]

    def is_empty(self):
        """判断队列是否为空"""
        return len(self.queue) == 0


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.is_empty())  # False
    queue.dequeue()  # 1出队， 队列只剩32
    print(queue.first())  # 2
    print(queue.last())  # 3
