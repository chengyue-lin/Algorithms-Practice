h = int(raw_input().strip())
m = int(raw_input().strip())

dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
           11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
           20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty'}


if m == 0:
	print dic[h] + " o' clock"
elif m > 30:
	if m == 45:
		print "quarter to", dic[h+1]
	else:
		minute = 60 - m
		if minute == 1:
			print "one minute to " + dic[h+1]
		else:
			if dic.has_key(minute):
				print dic[minute] + " minutes to " + dic[h+1]
			else:
				min1 = (minute / 10) * 10
				min2 = minute % 10
				print (dic[min1] + " " if min1 != 0 else "") + (dic[min2] + " " if min2 != 0 else "") + "minutes to " + dic[h+1]
elif m == 30:
	print "half past " + dic[h]
elif m == 15:
	print "quarter past " + dic[h]
else:
	if m == 1:
		print "one minute past " + dic[h]
	else:
		if dic.has_key(m):
				print dic[m] + " minutes past " + dic[h]
		else:
			min1 = (m / 10)*10
			min2 = m % 10
			print (dic[min1] + " " if min1 != 0 else "") + (dic[min2] + " " if min2 != 0 else "") + "minutes past " + dic[h]
