class Tree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, data):
    	if data == self.data:
    		return False
		elif data < self.data:
			if self.left is None:
				self.left = Tree(data)
				return True
			else:
				return self.left.add(data)
		elif data > self.data:
			if self.right is None:
				self.right = Tree(data)
				return True
			else:
				return self.right.add(data)
		return False

	def preorder(self, root):
		pass

	def inorder(self, root):
		pass

	def postorder(self, root):
		pass

def create_tree(vals=[]):
	root = Tree()
	for val in vals:
		root.add(val)
	return root


if __name__ == "__main__":
	from random import shuffle
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	shuffle(a)
	print a
	root = create_tree(a)