"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self, level=0):
        #ret = "\t"*level+repr(self.value)+"\n"
        #if self.left:
        #    ret += "L: " + self.left.__str__(level+1)
        #if self.right:
        #    ret += "R: " + self.right.__str__(level+1)
        #return ret
 
        return str(self.value)

def addToBinaryTree(arr, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    root = Node(arr[mid])
    root.left = addToBinaryTree(arr, start, mid - 1)
    root.right = addToBinaryTree(arr, mid + 1, end)
    return root

def createLinkedList(root, lists, level):
    if root == None:
        return None
    _list = []
    if len(lists) != level:
        lists[level].append(root.value)
    else:
        _list.append(root.value)
        lists.append(_list)
    left = createLinkedList(root.left, lists, level + 1)
    right = createLinkedList(root.right, lists, level + 1)
    if left:
        lists.extend(left)
    if right:
        lists.extend(right)
    return lists


def createByBFS(root):
    result = list()
    current = list()
    if root != None:
        current.append(root)

    while len(current):
        result.append(current)
        parents = current
        current = []
        for node in parents:
            if node.left != None:
                current.append(node.left)
            if node.right != None:
                current.append(node.right)
    return result

def preorder(root):
    if root == None:
        return
    print root.value
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
 #  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 19, 22, 45, 190, 220]
    arr = [1,2,3,4,5]
    root = addToBinaryTree(arr, 0, len(arr) - 1)
    preorder(root)
    """
    print "#" * 50
    left = Node(2)
    left.left = Node(1)
    right = Node(4)
    right.right = Node(5)
    root = Node(3)
    root.left = left
    root.right = right
    preorder(root)
    """

    lists = list()
    lists = createByBFS(root)
    print map(lambda x: map(str, x), lists)
    lists = list()
    lists = createLinkedList(root, lists, 0)
    print lists
