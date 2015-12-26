import re

time = raw_input().strip()

match = re.findall('[AP]M', time)

if len(match):
	time = re.sub("[AP]M", "", time)
	if match[0] == "PM":
		splittime = time.split(":")
		time = str(int(splittime[0]) + 12) + ":" + splittime[1] + ":" + splittime[2]
	print time