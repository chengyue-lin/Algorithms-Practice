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
        head.next = node
    return head

def print_list(head):
    while head != None:
        print head.data
        head = head.next

if __name__ == "__main__":
	val = input("Enter Value: ")
	node = Node()
	Insert(node, val)
	print_list(node)