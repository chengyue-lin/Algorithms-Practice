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

if __name__ == "__main__":
	node = None
	node = FillVals(node)
	print_list(node)
	# ReversePrint(node)
	print_list(Reverse(node))
	# delPos = input("Enter position to delete node:")
	# while delPos != -1:
	# 	node = Delete(node, delPos)
	# 	print_list(node)
	# 	delPos = input("Enter position to delete node:")