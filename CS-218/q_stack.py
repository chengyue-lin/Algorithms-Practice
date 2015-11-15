"""
Show how to implement a queue using two stacks S1 and S2 so that the amortized cost
of each operation on the queue is O(1).
"""

S1 = [] # Stack 1
S2 = [] # Stack 2

def enqueue(x):
	S1.append(x)

def dequeue():
	if not len(S2):
		while len(S1):
			S2.append(S1.pop())
	return S2.pop()