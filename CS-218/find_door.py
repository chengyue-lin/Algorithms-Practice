"""
Imagine that you are facing a high wall that stretches infinitely in both directions. There
is a door in the wall, but you don’t know how far away is the door or in which direction. It
is pitch dark, but you have a very dim lighted candle that will enable you to see the door
when you are right next to it.
Show an algorithm that enables you to find the door by walking at most O(n) steps in
the worst case, where n is the number of steps that you would have taken if you knew
where the door is and walked directly to it (note that your algorithm does not know
the value of n in advance)
"""
def find_door(wall, door, initial_pos ):
	i = 0
	direction = 1
	move = 0
	to = initial_pos + move
	if initial_pos == door :
		return initial_pos
	while True :
		move = 2** i
		for __ in xrange(2):
			for index, k in enumerate(wall[initial_pos + direction :to + direction : direction]):
				if k == door :
					return initial_pos + ( direction * index ) + direction
			direction *= -1
			to = initial_pos + move if direction == 1 else initial_pos - move
		i+=1