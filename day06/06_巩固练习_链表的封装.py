"""
参考链接 https://www.cnblogs.com/klyjb/p/11237361.html
数组: 需要连续的内存空间
链表: 不需要连续的内存空间
                数组              链表
增加元素        O(n)                O(1)
删除元素        O(n)                O(1)
修改元素        O(1)                O(n)
查看元素        O(1)                O(n)
"""
# 封装节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def travel(self, head):
        """遍历链表里面的每一个元素"""
        while head:
            print(head.val, end=',')
            head = head.next

def create_l1():
    # l1 = 2,4,3
    # l2 = 5, 6, 4
    l1 = ListNode()
    node1 = ListNode(val=2)
    node2 = ListNode(val=4)
    node3 = ListNode(val=3)
    l1.next = node1
    node1.next = node2
    node2.next = node3
    return  l1.next

def create_l2():
    # l1 = 2,4,3
    # l2 = 5, 6, 4
    l2 = ListNode()
    node1 = ListNode(val=5)
    node2 = ListNode(val=6)
    node3 = ListNode(val=4)
    l2.next = node1
    node1.next = node2
    node2.next = node3
    return  l2.next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = 0
    l3 = ListNode()
    cur = l3
    while(l1 or l2):
        if(l1):
            res += l1.val  # res=2
            l1 = l1.next
        if(l2):
            res += l2.val # res=2+5=7
            l2 = l2.next
        # res=10, val=0, res=>val val=res%10
        # res=14, val=4, 14%10=4
        l3.next = ListNode(res%10)
        l3 = l3.next
        # res=10, 进位为1， 10//10=1
        # res=14, 进位为1， 14//10=1
        res  //= 10
    if res == 1:
        l3.next = ListNode(1)
    return cur.next



# 中午留个作业:查一下它的功能
if __name__ == '__main__':
    l1 = create_l1()
    l2 = create_l2()
    l3 = addTwoNumbers(l1, l2)
    l3.travel(l3)

