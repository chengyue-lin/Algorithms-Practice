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

def print_list(head):
    while head != None:
        print head.data
        head = head.next

if __name__ == "__main__":
	node = Node()
	for i in xrange(10):
		val = input("Enter Value: ")
		Insert_At_Head(node, val)
	print_list(node)