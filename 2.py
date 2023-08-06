class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(nums):
    root = ListNode(val=nums[0])
    node = root
    for i in range(1, len(nums)):
        next_node = ListNode(val=nums[i])
        node.next = next_node
        node = next_node

    return root
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    root = ListNode()
    node = root
    while True:
        if l1:
            node.val += l1.val
            l1 = l1.next

        if l2:
            node.val += l2.val
            l2 = l2.next

        discharge = node.val // 10
        node.val %= 10

        if l1 or l2:
            next_node = ListNode()
            node.next = next_node
            node = next_node
            node.val = discharge
        else:
            if discharge != 0:
                next_node = ListNode(val=1)
                node.next = next_node
            break

    return root



n1 = createList([3,2,4])
n2 = createList([9])

r = addTwoNumbers(n1,n2)
print(r)