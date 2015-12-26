import re

time = raw_input().strip()

match = re.findall('[AP]M', time)

if len(match):
	time = re.sub("[AP]M", "", time)
	splittime = time.split(":")
	if match[0] == "PM":
		time = str("12" if splittime[0] == "12" else int(splittime[0]) + 12) + ":" + splittime[1] + ":" + splittime[2]
	else:
		time = str("00" if splittime[0] == "12" else splittime[0]) + ":" + splittime[1] + ":" + splittime[2]
	print time