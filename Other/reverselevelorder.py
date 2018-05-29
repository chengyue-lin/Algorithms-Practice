class Node:
 
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

def reverse_level_order(node):
    if node is None:
        return

    queue = []

    queue.append(node)

    stack = []

    while len(queue):
        #print queue[0].data
        stack.append(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
    for item in stack[-1::-1]:
        print item

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    reverse_level_order(root)
