import random


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    node = Node()
    node.data = data
    node.next = None
    if head == None:
        head = node
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = node
    return head


def Insert_At_Head(head, data):
    node = Node()
    node.data = data
    node.next = None
    if head is not None:
        node.next = head
    head = node
    return head


def InsertNth(head, data, position):
    node = Node()
    node.next = None
    node.data = data
    if head == None:
        return node
    elif position == 0:
        node.next = head
        return node
    else:
        temp = head
        for __ in xrange(1, position):
            if temp.next == None:
                temp.next = node
                return head
            temp = temp.next

        temp2 = temp.next
        temp.next = node
        node.next = temp2
        return head


def Delete(head, position):
    if head == None:
        return head
    elif position == 0:
        node = head.next
        head = node
        return head
    else:
        temp = head
        for __ in xrange(1, position):
            temp = temp.next
        temp.next = temp.next.next
        return head


def print_list(head):
    while head != None:
        print head.data, "=>",
        head = head.next
    print "None\n"


def ReversePrint(head):
    if head == None:
        return
    ReversePrint(head.next)
    print head.data


def Reverse(head):
    curr_node = head
    prev_node = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


def CompareLists(headA, headB):
    while headA is not None and headB is not None:
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next
    if headA is not None or headB is not None:
        return 0
    return 1


def MergeLists(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA
    if headA.data < headB.data:
        headA.next = MergeLists(headA.next, headB)
        return headA
    else:
        headB.next = MergeLists(headB.next, headA)
        return headB


def GetNode(head, position):
    count = 0
    temp = head
    while temp.next is not None:
        temp = temp.next
        count += 1
    temp = head
    for __ in xrange(int(count - position)):
        temp = temp.next
    return temp.data


def RemoveDuplicates(head):
    node = head
    while node.next is not None:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head


def FillVals(node):
    for i in xrange(10):
        pos = random.randint(0, 3)
        for __ in xrange(pos):
            node = Insert(node, i)
    return node


"""
	Brent's Cycle Detection
	http://www.siafoo.net/algorithm/11
"""
def HasCycle(head):
    rabbit = head
    turtle = head
    count = 0
    step_limit = 2
    while rabbit is not None:
        rabbit = rabbit.next
        count += 1
        if rabbit == turtle:
            return 1
        if count == step_limit:
            count = 0
            step_limit *= 2
            turtle = rabbit
    return 0


"""
	I know this sucks. Will improve
	TODO Improve this
"""

def FindMergeNode(headA, headB):
    iter1 = headA
    while iter1 is not None:
        iter2 = headB
        while iter2 is not None:
            if iter1 == iter2:
                return iter1.data
            iter2 = iter2.next
        iter1 = iter1.next
    return None


"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
"""

def SortedInsert(head, data):
    node = Node()
    node.data = data
    node.prev = None
    node.next = None
    if head is None:
        return node
    temp = head
    length = 0
    while temp is not None:
        temp = temp.next
        length += 1
    temp = head
    while True:
        i = 0
        while i < length / 2:
            temp = temp.next
            i += 1
        if temp.next is None and data > temp.data:
            temp.next = node
            node.prev = temp
            return head
        if temp.data <= data <= temp.next.data:
            temp.next.prev = node
            node.prev = temp
            node.next = temp.next
            temp.next = node
            return head
        elif data < temp.data:
            length /= 2
            temp = head
        elif data > temp.data:
            length /= 2
            temp = temp.next

"""
	Reverse a doubly linked list
	head could be None as well for empty list
 	Node is defined as
"""
def reverse_doubly(head):
	node = head
    while node is not None:
        temp = node.prev
        node.prev = node.next
        node.next = temp
        head = node
        node = node.prev
    return head

# if __name__ == "__main__":
#     node = None
#     node = FillVals(node)
#     print_list(node)
#     print_list(Reverse(node))