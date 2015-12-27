alphabet = set("abcdefghijklmnopqrstuvwxyz")
panagram = set(raw_input().strip().lower())
if len(alphabet - panagram):
	print "not pangram"
else:
	print "pangram"