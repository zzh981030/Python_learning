class Stack(object):
    """栈的封装[1, 2, 3, 4]"""

    def __init__(self):
        self.stack = []

    def push(self, value):
        """入栈"""
        self.stack.append(value)
        print(f"入栈元素为{value}")

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise  Exception("栈为空")
        item = self.stack.pop()
        print(f"出栈元素为{item}")
        return  item

    def is_empty(self):
        """判断栈是否为空"""
        return  len(self.stack) == 0

    def top(self):
        """返回栈顶元素"""
        if self.is_empty():
            raise  Exception("栈为空")
        return  self.stack[-1]

    def __len__(self):
        """魔术方法, len(object)自动执行的方法"""
        return  len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(len(stack))  # 3
    stack.pop()
    print(stack.is_empty()) # False
    print(stack.top())  # 2