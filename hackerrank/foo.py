import datetime
a = datetime.datetime.now() + datetime.timedelta(33,0)
for __ in xrange(12):
	a = a + datetime.timedelta(28, 0)
	print a