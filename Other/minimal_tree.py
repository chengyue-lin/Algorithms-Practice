"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        if self.left:
            ret += "L: " + self.left.__str__(level+1)
        if self.right:
            ret += "R: " + self.right.__str__(level+1)
        return ret

def addToBinaryTree(arr, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    root = Node(arr[mid])
    root.left = addToBinaryTree(arr, 0, mid - 1)
    root.right = addToBinaryTree(arr, mid + 1, end)
    return root


if __name__ == "__main__":
 #   arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 19, 22, 45, 190, 220]
    arr = [1,2,3,4]
    print str(addToBinaryTree(arr, 0, len(arr) - 1))
